import datetime

# gcd_sub(a, b) - repeated substractions
def gcd_sub(a, b):
    if a == 0:
        return b
    while b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# gcd_rem(a, b) - always taking the reminder
def gcd_rem(a, b):
    while b != 0:
        r = b
        b = a % b
        a = r
    return a

# gcd_prime_factors(a, b) - the prime factors multiplied
def gcd_prime_factors(a, b):
    if a == b or a == 0:
        return b
    elif b == 0:
        return a
    d = 2
    gcd = 1
    while a > d or b > d:
        while a % d == 0 and b % d == 0:
            a /= d
            b /= d
            gcd *= d
        d += 1
    return gcd

# gcd_min(a, b) - starting from the minimum number, it decreases each time it is not a divisor for both numbers
def gcd_min(a, b):
    if a == b or a == 0:
        return b
    elif b == 0:
        return a
    gcd = min(a, b)
    while True:
        if a % gcd == 0 and b % gcd == 0:
            return gcd
        gcd -= 1




if __name__ == '__main__':
    input = [
        (0, 48),
        (45600, 76800),
        (63525, 105875),
        (84960, 126240),
        (27, 63),
        (724724, 8174734),
        (17, 23),
        (78960, 157920),
        (478863, 368593),
        (50, 75)
    ]

    for pair in input:
        first = pair[0]
        second = pair[1]

        print(f'The numbers are {first} and {second}.')
        start = datetime.datetime.now()
        gcd = gcd_sub(first, second)
        end = datetime.datetime.now()
        print(f'Using the function gcd_sub, this was done in {end-start} seconds.')
        print(f'The greatest common divisor is {gcd}.')
        print('---------')

        print(f'The numbers are {first} and {second}.')
        start = datetime.datetime.now()
        gcd = gcd_prime_factors(first, second)
        end = datetime.datetime.now()
        print(f'Using the function gcd_prime_factors, this was done in {end - start} seconds.')
        print(f'The greatest common divisor is {gcd}.')
        print('---------')

        print(f'The numbers are {first} and {second}.')
        start = datetime.datetime.now()
        gcd = gcd_min(first, second)
        end = datetime.datetime.now()
        print(f'Using the function gcd_min, this was done in {end - start} seconds.')
        print(f'The greatest common divisor is {gcd}.\n\n\n\n\n')

