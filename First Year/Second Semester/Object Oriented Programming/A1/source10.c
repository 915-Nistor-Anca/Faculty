#include <stdio.h>


bool is_prime(int n) {
    /*
    * This function checks whether the given number a is prime.
    * A number is prime if it has no other divisors except itself and the number 1.
    * Parameter: a - integer
    * Return: true, if a is prime and false, if not
    */

    if (n <= 1) {
        return false;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

void goldbach_conjecture(int n, int *n1, int *n2) {
    /*
    * This function receives an even number n which is greater than 2 and finds 
    * two prime numbers n1, n2 with the condition n1 + n2 = n.
    */
    for (int i = 2; i <= n / 2; i++) {
        if (is_prime(i) && is_prime(n - i)) {
            *n1 = i; *n2 = n - i;
            return;
        }
    }
}

void menu() {
    printf("1.Decompose a given even natural number, greater than 2, as a sum of two prime numbers (Goldbach’s conjecture).\n");
    printf("2.Given a vector of numbers, find the longest contiguous subsequence such that any consecutive elements have at least 2 distinct digits in common.\n");
}

int frequency(int n, int d) {
    /*
    This function computes the frequency of a digit in a given number.
    Parameters: n - the given number; d - the digit*/
    int k = 0;
    while (n) {
        if (n % 10 == d) k++;
        n /= 10;
    }
    return k;
}

int digits_in_common(int a, int b) {
    /*
    * This function receives two numbers and calculates how many different digits they have in common.
    */
    int f[10], k = 0;
    for (int i = 0; i < 10; i++) f[i] = 0;
    while (a) {
        if (frequency(b, a % 10) != 0 && f[a%10] == 0) {
            f[a%10] = 1;
            k++;
        }
        a /= 10;
    }
    return k;
}

void longest_sequence(int x[], int n, int* start_poz, int* length) {
    /*
    * This function computes the starting position and the length of 
     the longest contiguous subsequence 
    such that any consecutive elements have at least 2 distinct digits in common.
    */
    *length = 0;
    for (int i = 0; i < n - 1; i++) {
        int j = i + 1;
        while (j < n && digits_in_common(x[i], x[j]) >= 2) {
            j++;
        }
        int len = j - i;
        if (len > *length) {
            *length = len;
            *start_poz = i;
        }
    }
}

void read_numbers(int x[], int* n)
{
    /*
    * This function reads a number and then the same number of integers.
    * Parameters:
    * x - a vector of integers
    * n - integer
    */

    scanf("%d", &*n);
    for (int i = 0; i < *n; i++)
    {
        scanf("%d", &x[i]);
    }
}

void print_numbers(int x[100], int n)
{
    /*
    * This function prints the n number which are saved in the vector x.
    * Parameters:
    * x - vector of integers
    * n - integer
    */
    for (int i = 0; i < n; i++)
        printf("%d ", x[i]);
}

int main()
{
    menu();
    
    while (true) {
        printf("Enter an option (1/2):");
        int choice;
        scanf("%d", &choice);
        if (choice == 0) break;
        if (choice == 1) {
            printf("Enter an even natural number, greater than 2.\n");
            int n;
            scanf("%d", &n);
            int n1, n2;
            goldbach_conjecture(n, &n1, &n2);
            printf("%d = %d + %d\n", n, n1, n2);
        }
        else if (choice == 2)
        {
            printf("You need to add some numbers first! \n");
            int x[100], n = 0;
            printf("The number of numbers is:");
            read_numbers(x, &n);
            printf("The numbers are: ");
            print_numbers(x, n);
            printf(". \n");
            int length = 0, start_poz = -1;
            longest_sequence(x, n, &start_poz, &length);
            if (start_poz == -1) printf("There is no such sequence in the list. \n");
            else {
                printf("The sequence is: ");
                while (length > 0)
                {
                    printf("%d ", x[start_poz]);
                    length--;
                    start_poz++;
                }
            }
             printf("\n");
            
        }
    }
}
