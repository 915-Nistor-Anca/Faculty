#include <stdio.h>
 
void read_numbers(int x[], int *n)
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

void print_main_menu()
{
	/*
	* This function prints the main menu.
	*/
	printf("1. Read a list of numbers. \n");
	printf("2.1.Print the Pascal triangle. \n");
	printf("2.2. Print the longest contiguous subsequence of prime numbers. \n");
	printf("3. The number of 0 digits of a product of the read numbers. \n");
	printf("4. Exit. \n");
}

int prime_number(int a)
{
	/*
	* This function checks whether the given number a is prime. 
	* A number is prime if it has no other divisors except itself and the number 1.
	* Parameter: a - integer
	* Return: 1, if a is prime and 0, if not
	*/
	if (a < 2) return 0;
	if (a == 2) return 1;
	for (int i = 2; i < a; i ++)
		if (a % i == 0) return 0;
	return  1;
}

int factorial(int n)
{
	/*
	* This function computes the n factorial.
	* Parameter n: integer
	* Return: the factorial of the number
	*/
	if (n == 0 || n == 1) return 1;
	return n * factorial(n - 1);
}

int combinations(int n, int k)
{
	/*
	* This function computes combinations of n taken k.
	* Parameters n, k: integers
	* Return: the value of the formula.
	*/
	return factorial(n) / (factorial(k) * factorial(n - k));
}

void pascal_triangle(int n)
{
	for (int m = 1; m <= n; m++)
	{
		for (int k = 0; k <= m; k++)
			printf("%d ", combinations(m, k));
		printf("\n");
	}
}

void longest_sequence_prime_numbers(int x[], int n, int* start_poz, int* length)
{
	/*
	* This function searches for the longest sequence of prime numbers in the vector x of 
	* n elements and gives the other two parameters the start position of the sequence and its
	* length.
	* Parameters:
	* x - vector of integers
	* n, start_poz, length - integers
	*/
	int i=0;
	while (i < n)
	{
		int j = i, l = 0;
		while (prime_number(x[j])==1  && j< n)
		{
			j++;
			l++;
		}
		if (l > *length)
		{
			*length = l;
			*start_poz = i;
		}
		i++;
	}
	
}

int number_of_zero_digits(int a)
{
	/*
	* This function comptutes how many times the digit 0 appears in a number.
	* Parameter a: integer
	* Return: the number of zero digits
	*/
	int k = 0;
	//if (a == 0) return 1; 
	while (a != 0)
	{
		if (a % 10 == 0) k++;
		a /= 10;
	}
	return k;
}


int power_of_k(int a, int k)
{
	/*
	* This function computes at which power the number k appears in a.
	* Parameters a, k: integers.
	* Return: the power of k in a.
	*/
	int p = 0;
	while (a % k == 0)
	{
		p++;
		a /= k;
	}
	return p;
}

int main()
{
	int x[100], n = 0;
	print_main_menu();
	int choice = 0, ok = 1;
	while (ok == 1)
	{
		printf("Your choice:");
		scanf("%d", &choice);
		if (choice == 1)
		{
			printf("The number of numbers is:");
			//scanf("%d", &n);
			read_numbers(x, &n);
			printf("The numbers are: ");
			print_numbers(x, n);
			printf(". \n");
		}
		else if (choice == 2)
		{
			int choice2 = 0;
			printf("Your choice for number 2:");
			scanf("%d", &choice2);
			if (choice2 == 1)
			{
				printf("The dimension of the triangle:");
				int nn;
				scanf("%d", &nn);
				pascal_triangle(nn);
			}
			else if (choice2 == 2)
			{
				if (n == 0) printf("You need to add some numbers first! \n");
				else
				{
					int length = 0, start_poz = -1;
					longest_sequence_prime_numbers(x, n, &start_poz, &length);
					if (start_poz == -1) printf("There is no prime number in the list. \n");
					else while (length > 0)
					{
						printf("%d ", x[start_poz]);
						length--;
						start_poz++;
					}
					printf("\n");
				}
			}
		}
		else if (choice == 4)
			ok = 0;
		else if (choice == 3)
		{
			int a = -1, number_of_2 = 0, number_of_5 = 0;
			while (a != 0)
			{
				scanf("%d", &a);
				if (a!=0) number_of_2 += power_of_k(a, 2);
				if (a!=0) number_of_5 += power_of_k(a, 5);
			}
			if (number_of_2 > number_of_5) number_of_5 = number_of_2;
			printf("The number of zero digits is %d. \n", number_of_5);
		}
	}
}
