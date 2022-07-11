import math

def is_prime(n):
    """
    Checks if n is a prime number.

    Given a natural n, the function returns True if it is a prime number. If it isn't, it returns False.
    The function takes all the odd numbers from 3 to the square root of n + 1 (with a step of two) and checks if one of them is a divisor
    for n. If so, that means the number is not prime. The number is also not prime if it's less than 2 or if it's even.

    :param n: a natural number
    :returns: a boolean value, depending if n is prime or not

    """
    if n == 2:
        return True
    if n<2 or n%2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n%i==0:
            return False
    return True


def goldbach_hypothesis(n):
    """
    The function determines all the pairs (p1, p2), where p1 and p2 are prime numbers, which satisfy the statement: n = p1 + p2.
    If the number cannot be written as a sum of two prime numbers, the function will show a proper message.
    :param n: a natural number
    """
    if n%2 == 1:
        print('This natural number cannot be written as a sum of two prime numbers.')
    else:
        p1=2
        p2=n-2
        while p1<=p2:
            if is_prime(p1) and is_prime(p2):
                print(n, '=', p1, '+', p2)
            p1=p1+1
            p2=p2-1


if __name__ == '__main__':
    n=int(input('Enter the number:'))
    goldbach_hypothesis(n)
