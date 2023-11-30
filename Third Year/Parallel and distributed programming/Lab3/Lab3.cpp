
#include <iostream>
#include <vector>
#include <list>
#include <thread>
#include <functional>
#include <queue>
#include <mutex>
#include <condition_variable>
#include <future>
#include <random>
#include <chrono>

using namespace std;

class ThreadPool {
public:
    explicit ThreadPool(size_t nrThreads)
        :m_end(false) {
        m_threads.reserve(nrThreads);
        for (size_t i = 0; i < nrThreads; ++i) {
            m_threads.emplace_back([this]() {this->run(); });
        }
    }

    ~ThreadPool() {
        close();
        for (std::thread& t : m_threads) {
            t.join();
        }
    }

    void close() {
        std::unique_lock<std::mutex> lck(m_mutex);
        m_end = true;
        m_cond.notify_all();
    }

    void enqueue(std::function<void()> func) {
        std::unique_lock<std::mutex> lck(m_mutex);
        m_queue.push_back(std::move(func));
        m_cond.notify_one();
    }
private:
    void run() {
        while (true) {
            std::function<void()> toExec;
            {
                std::unique_lock<std::mutex> lck(m_mutex);
                while (m_queue.empty() && !m_end) {
                    m_cond.wait(lck);
                }
                if (m_queue.empty()) {
                    return;
                }
                toExec = std::move(m_queue.front());
                m_queue.pop_front();
            }
            toExec();
        }
    }

    std::mutex m_mutex;
    std::condition_variable m_cond;
    std::list<std::function<void()>> m_queue;
    bool m_end;
    std::vector<std::thread> m_threads;
};


void printMatrix(vector<vector<int>> matrix, int nr_rows, int nr_columns) {
    cout << "Result matrix:\n";
    for (int i = 0; i < nr_rows; i++) {
        cout << "ROW " << i << ':';
        for (int j = 0; j < nr_columns; j++) cout << matrix[i][j] << ' ';
        cout << '\n'<<'\n';
    }
    cout << '\n';
}


int computeSingleElement(int row_first_matrix, int column_second_matrix, vector<vector<int>> matrix1, vector<vector<int>> matrix2) {
    int result = 0;
    //cout << "row " << row_first_matrix << ", column " << column_second_matrix << '\n';
    for (int column = 0; column < matrix1[row_first_matrix].size(); column++) {
        result += matrix1[row_first_matrix][column] * matrix2[column][column_second_matrix];
    }
    //cout << result << '\n';
    return result;
}

void computeRowAfterRow(int nr_columns_second_matrix, vector<vector<int>> matrix1, vector<vector<int>> maxtrix2, vector<vector<int>> &result, int nr_elements_to_be_computed, int last_row, int last_column) {
    int i = last_row;
    int j = last_column;
    for (int k = 1; k <= nr_elements_to_be_computed; k++) {
        if (j == nr_columns_second_matrix) {
            j = 0;
            i++;
        }
        result[i][j] = computeSingleElement(i, j, matrix1, maxtrix2);
        j++;
    }
    //printMatrix(result, 3, 5);
}


void computeColumnAfterColumn(int nr_columns_second_matrix, vector<vector<int>> matrix1, vector<vector<int>> matrix2, vector<vector<int>>& result, int nr_elements_to_be_computed, int last_row, int last_column) {
    int i = last_row;
    int j = last_column;
    for (int k = 1; k <= nr_elements_to_be_computed; k++) {
        if (i == matrix1.size()) {
            i = 0;
            j++;
        }
        result[i][j] = computeSingleElement(i, j, matrix1, matrix2);
        i++;
    }
}

void computeEveryKthElement(int nr_rows_first_matrix, int nr_columns_second_matrix, vector<vector<int>> matrix1, vector<vector<int>> matrix2, vector<vector<int>>& result, int k, int nr_task) {
    int i = 0;
    int j = nr_task;
    
    while (i < nr_rows_first_matrix) {
        while (j < nr_columns_second_matrix) {
            result[i][j] = computeSingleElement(i, j, matrix1, matrix2);
            j += k;
            if (j >= nr_columns_second_matrix) {
                j = j % k;
                i++;
                break;
            }
        }
    }
}

vector<vector<int>> generateRandomMatrix(int rows, int columns) {
    vector<vector<int>> matrix(rows, vector<int>(columns, 0));
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < columns; j++) {
            int lower_bound = 1;
            int upper_bound = 100;

            std::random_device rd;
            std::mt19937 gen(rd());

            std::uniform_int_distribution<> distrib(lower_bound, upper_bound);
            matrix[i][j] = distrib(gen);
        }
    return matrix;
}

int main()
{
    int nr_rows_result_matrix;
    int nr_columns_result_matrix;

    vector<vector<int>> matrix1, matrix2;

   /*nr_rows_result_matrix = 3;
   nr_columns_result_matrix = 5;
   matrix1 = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };
    matrix2 = {
        {12, 10, 5, 9, 4},
        {6, 7, 2, 10, 5},
        {9, 2, 10, 4, 3},
        {15, 3, 4, 1, 10}
    };*/

    matrix1 = generateRandomMatrix(100, 40);
    matrix2 = generateRandomMatrix(40, 500);
    nr_rows_result_matrix = 100;
    nr_columns_result_matrix = 500;
    


    int approach, number_of_tasks, way;
    std::cout << "Approach 1: create thread for each task.\nApproach 2: use a thread pool.\nApproach:";
    std::cin >> approach;
    std::cout << "\nNumber of tasks:";
    std::cin >> number_of_tasks;
    std::cout << "\nWay 1: row after row.\nWay 2: column after column.\nWay 3: every k-th element.\n";
    std::cin >> way;
    
    auto start_time = std::chrono::high_resolution_clock::now();

    vector<vector<int>> result(nr_rows_result_matrix, vector<int>(nr_columns_result_matrix, 0));
    //printMatrix(result, nr_rows_result_matrix, nr_columns_result_matrix);

    if (approach == 1) {
        if (way == 1) {
            std::list<std::thread> threads;
            int last_row = 0, last_column = 0, nr_elements_to_be_computed_by_task = nr_rows_result_matrix * nr_columns_result_matrix / number_of_tasks, elements_remaining = nr_rows_result_matrix * nr_columns_result_matrix % number_of_tasks;
            for (int task = 1; task <= number_of_tasks; task++) {
                if (task == number_of_tasks) threads.push_back(std::thread(computeRowAfterRow, nr_columns_result_matrix, cref(matrix1), cref(matrix2), ref(result), nr_elements_to_be_computed_by_task + elements_remaining, last_row, last_column));
                if (task != number_of_tasks) threads.push_back(std::thread(computeRowAfterRow, nr_columns_result_matrix, cref(matrix1), cref(matrix2), ref(result), nr_elements_to_be_computed_by_task, last_row, last_column));
                last_column += nr_elements_to_be_computed_by_task % nr_columns_result_matrix;
                last_row += nr_elements_to_be_computed_by_task / nr_columns_result_matrix;
                if (last_column >= nr_columns_result_matrix) {
                    last_row++;
                    last_column %= nr_columns_result_matrix;
                }
            }
            for (std::thread& t : threads) {
                t.join();
            }
            printMatrix(result, nr_rows_result_matrix, nr_columns_result_matrix);


            auto end_time = std::chrono::high_resolution_clock::now();
            auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time);
            auto duration_seconds = std::chrono::duration_cast<std::chrono::seconds>(duration);
            std::cout << "Time taken for Approach 1, Way 1: " << duration.count() << " microseconds" << std::endl;
            std::cout << "Time taken for Approach 1, Way 1: " << duration_seconds.count() << " seconds" << std::endl;


        }
        else if (way == 2) {
            std::list<std::thread> threads;
            int last_row = 0, last_column = 0, nr_elements_to_be_computed_by_task = nr_rows_result_matrix * nr_columns_result_matrix / number_of_tasks, elements_remaining = nr_rows_result_matrix * nr_columns_result_matrix % number_of_tasks;
            //cout << "nr elems " << nr_elements_to_be_computed_by_task << ' ' << elements_remaining << '\n';
            for (int task = 1; task <= number_of_tasks; task++) {
                //cout << last_row << ' ' << last_column << '\n';
                if (task == number_of_tasks) threads.push_back(std::thread(computeColumnAfterColumn, nr_columns_result_matrix, cref(matrix1), cref(matrix2), ref(result), nr_elements_to_be_computed_by_task + elements_remaining, last_row, last_column));
                if (task != number_of_tasks) threads.push_back(std::thread(computeColumnAfterColumn, nr_columns_result_matrix, cref(matrix1), cref(matrix2), ref(result), nr_elements_to_be_computed_by_task, last_row, last_column));
                last_row += nr_elements_to_be_computed_by_task % nr_rows_result_matrix;
                last_column += nr_elements_to_be_computed_by_task / nr_rows_result_matrix;
                if (last_row >= nr_rows_result_matrix) {
                    last_column++;
                    last_row %= nr_rows_result_matrix;
                }
            }
            for (std::thread& t : threads) {
                t.join();
            }
            printMatrix(result, nr_rows_result_matrix, nr_columns_result_matrix);

            auto end_time = std::chrono::high_resolution_clock::now();
            auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time);
            auto duration_seconds = std::chrono::duration_cast<std::chrono::seconds>(duration);
            std::cout << "Time taken for Approach 1, Way 2: " << duration.count() << " microseconds" << std::endl;
            std::cout << "Time taken for Approach 1, Way 2: " << duration_seconds.count() << " seconds" << std::endl;

        }
        else if (way == 3) {
            std::list<std::thread> threads;
            //printMatrix(result, nr_rows_result_matrix, nr_columns_result_matrix);
            for (int task = 0; task < number_of_tasks; task++) {
                threads.push_back(std::thread(computeEveryKthElement, nr_rows_result_matrix, nr_columns_result_matrix, cref(matrix1), cref(matrix2), ref(result), number_of_tasks, task));
            }
            for (std::thread& t : threads) {
                t.join();
            }
            printMatrix(result, nr_rows_result_matrix, nr_columns_result_matrix);

            auto end_time = std::chrono::high_resolution_clock::now();
            auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time);
            auto duration_seconds = std::chrono::duration_cast<std::chrono::seconds>(duration);
            std::cout << "Time taken for Approach 1, Way 3: " << duration.count() << " microseconds" << std::endl;
            std::cout << "Time taken for Approach 1, Way 3: " << duration_seconds.count() << " seconds" << std::endl;
        }
    }


    else if (approach == 2) {
        ThreadPool pool(number_of_tasks);
        cout << "At the beggining:\n";
        printMatrix(result, nr_rows_result_matrix, nr_columns_result_matrix);

        if (way == 1) {
            int last_row = 0, last_column = 0, nr_elements_to_be_computed_by_task = nr_rows_result_matrix * nr_columns_result_matrix / number_of_tasks, elements_remaining = nr_rows_result_matrix * nr_columns_result_matrix % number_of_tasks;

            for (int task = 1; task <= number_of_tasks; task++) {
                if (task == number_of_tasks) pool.enqueue([&matrix1, &matrix2, &result, nr_columns_result_matrix, nr_elements_to_be_computed_by_task, task, last_row, last_column, elements_remaining]() {
                    computeRowAfterRow(nr_columns_result_matrix, matrix1, matrix2, result, nr_elements_to_be_computed_by_task + elements_remaining, last_row, last_column);
                    //printMatrix(result, 3, 5);
                });

                if (task != number_of_tasks) pool.enqueue([&matrix1, &matrix2, &result, nr_columns_result_matrix, nr_elements_to_be_computed_by_task, task, last_row, last_column]() {
                    computeRowAfterRow(nr_columns_result_matrix, matrix1, matrix2, result, nr_elements_to_be_computed_by_task, last_row, last_column);
                    //printMatrix(result, 3, 5);
                });

                last_column += nr_elements_to_be_computed_by_task % nr_columns_result_matrix;
                last_row += nr_elements_to_be_computed_by_task / nr_columns_result_matrix;
                if (last_column >= nr_columns_result_matrix) {
                    last_row++;
                    last_column %= nr_columns_result_matrix;
                }
            }

            auto end_time = std::chrono::high_resolution_clock::now();
            auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time);
            auto duration_seconds = std::chrono::duration_cast<std::chrono::seconds>(duration);
            std::cout << "Time taken for Approach 2, Way 1: " << duration.count() << " microseconds" << std::endl;
            std::cout << "Time taken for Approach 2, Way 1: " << duration_seconds.count() << " seconds" << std::endl;

        }
        else if (way == 2) {
            int last_row = 0, last_column = 0, nr_elements_to_be_computed_by_task = nr_rows_result_matrix * nr_columns_result_matrix / number_of_tasks, elements_remaining = nr_rows_result_matrix * nr_columns_result_matrix % number_of_tasks;

            for (int task = 1; task <= number_of_tasks; task++) {
                if (task == number_of_tasks) pool.enqueue([&matrix1, &matrix2, &result, nr_columns_result_matrix, nr_elements_to_be_computed_by_task, task, last_row, last_column, elements_remaining]() {
                    computeColumnAfterColumn(nr_columns_result_matrix, matrix1, matrix2, result, nr_elements_to_be_computed_by_task + elements_remaining, last_row, last_column);
                });

                if (task != number_of_tasks) pool.enqueue([&matrix1, &matrix2, &result, nr_columns_result_matrix, nr_elements_to_be_computed_by_task, task, last_row, last_column]() {
                    computeColumnAfterColumn(nr_columns_result_matrix, matrix1, matrix2, result, nr_elements_to_be_computed_by_task, last_row, last_column);
                });

                last_row += nr_elements_to_be_computed_by_task % nr_rows_result_matrix;
                last_column += nr_elements_to_be_computed_by_task / nr_rows_result_matrix;
                if (last_row >= nr_rows_result_matrix) {
                    last_column++;
                    last_row %= nr_rows_result_matrix;
                }
            }

            auto end_time = std::chrono::high_resolution_clock::now();
            auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time);
            auto duration_seconds = std::chrono::duration_cast<std::chrono::seconds>(duration);
            std::cout << "Time taken for Approach 2, Way 2: " << duration.count() << " microseconds" << std::endl;
            std::cout << "Time taken for Approach 2, Way 2: " << duration_seconds.count() << " seconds" << std::endl;
        }
        else if (way == 3) {
            for (int task = 0; task < number_of_tasks; task++) {
                pool.enqueue([&matrix1, &matrix2, &result, nr_rows_result_matrix, nr_columns_result_matrix, number_of_tasks, task]() {
                    computeEveryKthElement(nr_rows_result_matrix, nr_columns_result_matrix, matrix1, matrix2, result, number_of_tasks, task);
                });
            }

            auto end_time = std::chrono::high_resolution_clock::now();
            auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end_time - start_time);
            auto duration_seconds = std::chrono::duration_cast<std::chrono::seconds>(duration);
            std::cout << "Time taken for Approach 2, Way 3: " << duration.count() << " microseconds" << std::endl;
            std::cout << "Time taken for Approach 2, Way 3: " << duration_seconds.count() << " seconds" << std::endl;
        }

        //pool.close();
        cout << "At the end:\n";
        printMatrix(result, nr_rows_result_matrix, nr_columns_result_matrix);
    }
}