# 3. Generalized Fermat’s algorithm. It will first consider k = 1. If not successful, then it will
# consider k = 2, 3, . . . until getting a factor
import math

def isPerfectSquare(n): #this function checks if a number is a perfect square
    root = math.isqrt(n) #the square root of n
    if root*root == n:
        return True
    return False

if __name__ == '__main__':
    n = int(input("n=")) #141467, for example
    print(f"n is {n}. ")
    B = 10
    print(f"B is {B}.\n")

    k = 1
    ok = 0
    while ok == 0:
        t0 = math.isqrt(k * n)
        for t in range(t0 + 1, t0 + B + 1):
            print(f"t = {t}")
            print (f"{t}*{t} - {k}*{n} = {t*t - k*n}, {t*t - k*n} is perfect square: {isPerfectSquare(t*t - k*n)}.\n")
            if isPerfectSquare(t*t - k*n):
                s = math.isqrt(t*t - k*n)
                print(f"s = sqrt({t}*{t} - {k}*{n}) = {s}")
                print(f"{n} = {t-s}*{int((t+s)/k)}")
                ok = 1
                break

        k += 1


#lab 4: problem 2
