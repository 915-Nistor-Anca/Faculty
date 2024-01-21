import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

public class RegularAlgorithmParallelForm {
    private static final int number_of_threads = 5;

    public static Polynomial multiply(Polynomial p1, Polynomial p2) throws InterruptedException {
        int size_result = p1.getDegree() + p2.getDegree() + 1;
        List<Integer> coefficients = new ArrayList<>();
        for (int i = 0; i <= size_result; i++) {
            coefficients.add(0);
        }
        Polynomial result = new Polynomial(coefficients);

        ThreadPoolExecutor executor = (ThreadPoolExecutor) Executors.newFixedThreadPool(number_of_threads);
        int number_of_tasks = size_result / number_of_threads;
        if (number_of_tasks == 0) number_of_tasks = 1;
        int end;
        for (int i = 0; i < size_result; i += number_of_tasks) {
            end = i + number_of_tasks;
            Task task = new Task(i, end, p1, p2, result);
            executor.execute(task);
        }

        executor.shutdown();
        executor.awaitTermination(50, TimeUnit.SECONDS);

        return result;
    }
}
