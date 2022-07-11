def Fibonacci(n):
    """
    This function searches for the smallest number m from the Fibonacci sequence which is larger than the n given.
    It uses three variables (x, y and m) and creates the Fibonacci sequence until m is larger than n, using the formula:
    x+y=m, then x becomes y, y becomes m and so on.
    :param n: a natural number
    :return: the smallest number m from the Fibonacci sequence, larger than n
    """
    x=1
    y=1
    m=2
    while m<=n:
        x=y
        y=m
        m=x+y
    return m

if __name__ == '__main__':
    n= int(input('Enter the number:'))
    print(Fibonacci(n))
