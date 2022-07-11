def sum_of_the_divisors(n):
    """
    This function does the sum of the divisors for the given number.
    :param n: a natural number
    :return: the sum of the divisors of n
    """
    s=0
    for i in range(1,int(n/2)+1):
        if n%i==0:
            s+=i
    return s

def is_perfect(n):
    """
    This functions checks if n is perfect or not. A perfect number is equal to the sum of its divisors.
    :param n: a natural number
    :return: True, if n is perfect and False, on the contrary.
    """
    if n==sum_of_the_divisors(n):
        return True
    return False

def the_previous_perfect_number(n):
    """
    This function searches for the largest perfect number smaller than n.
    It substracts from n until the formed number is perfect.
    If it doesn't find such a number, it displays a message.

    :param n: a natural number
    :return: a natural number, which represents the largest perfect number smaller than n
    """
    cn=n
    n-=1
    found=0
    while n>0 and found==0:
        if is_perfect(n):
            found=1
            print('The largest perfect number smaller than ', cn, ' is ', n, '.')
        n-=1
    if found == 0:
        print('A perfect number smaller than ', cn, ' does not exist.')

if __name__ == '__main__':
    n=int(input('Enter the number:'))
    the_previous_perfect_number(n)
