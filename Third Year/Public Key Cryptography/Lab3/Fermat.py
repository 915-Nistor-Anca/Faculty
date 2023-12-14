# Fermat’s algorithm.
import math

def isPerfectSquare(n): #this function checks if a number is a perfect square
    root = math.isqrt(n) #the square root of n
    if root*root == n:
        return True
    return False

if __name__ == '__main__':
    n = int(input("n=")) #9709, for example
    print(f"n is {n}. ")
    t0 = math.isqrt(n)
    print(f"t0 is {t0}.")

    k = 1
    t = t0 + k

    print("\nIterations:")
    while k <= 20 and isPerfectSquare(t*t - n) is False: #while it doesn't find a perfect square, it keeps searching
        t = t0 + k
        print(f"t = {t0} + {k}; t*t - n = {t*t - n}.")
        print(f"{t*t - n} is a perfect square: {isPerfectSquare(t*t - n)}.")
        k += 1

    s = math.isqrt(t*t - n)

    print(f"\nConclusion: the 2 factors of {n} are {t+s} and {t-s}.") #n = (t+s)(t-s)
