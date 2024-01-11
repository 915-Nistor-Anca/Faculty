import random


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return False
    return True


def generateKeys():
    p = 0
    q = 0
    interval_lower_bound = random.randint(0, 150)
    interval_upper_bound = random.randint(151, 300)
    while isPrime(p) is False or isPrime(q) is False or p == q or (p%4 != q%4 or p%4 != 3):
        p = random.randint(interval_lower_bound, interval_upper_bound)
        q = random.randint(interval_lower_bound, interval_upper_bound)
    return p, q


def plaintextIsValid(plaintext, alphabet):
    for character in plaintext:
        if character not in alphabet:
            return False
    return True

def ciphertextIsValid(ciphertext):
    for n in ciphertext:
        if isinstance(n, (int, float, complex)):
            return False
    return True

def convertPlaintextToASCII(plaintext):
    m = int.from_bytes(plaintext.encode('ascii'), byteorder='big')
    return m

def convertASCIIToPlaintext(ascii_value):
    if ascii_value >= 0 and ascii_value <= 128:
        byte_data = ascii_value.to_bytes((ascii_value.bit_length() + 7) // 8, 'big')
        plaintext = byte_data.decode('ascii')
        return plaintext
    return "?"




def convertToBinary(m):
    if m > 0:
        return str(bin(int(m%256))[2:])
    else:
        return str(bin(int((256+m)%256))[3:])


def extendBinary(m):
    x = str(m) + str(m)
    return int(x)


def transformToDecimal(m):
    # m_decimal = []
    # for number in m:
    #    x = int(number, 2)
    #    m_decimal.append(x)
    # return m_decimal

    return int(m, 2)


def encrypt(m, n):
    return (m * m) % n


def extended_gcd(p, q):
    if p == 0:
        return q, 0, 1
    else:
        gcd, x, y = extended_gcd(q % p, p)
        return gcd, y - (q // p) * x, x


def divide_in_half(binary_string):
    length = len(binary_string)
    half_length = length // 2
    first_half = binary_string[:half_length]
    second_half = binary_string[half_length:]
    return first_half, second_half






def convertPlaintextToASCIIList(plaintext):
    ascii_list = []
    for character in plaintext:
        ascii_list.append(convertPlaintextToASCII(character))
    return  ascii_list

def encryptList(m, n):
    encrypted_list = []
    for number in m:
        encrypted_list.append(encrypt(number, n))
    return encrypted_list

def findRightChoice(m1,m2,m3,m4):
    if m1 != "?":
        return m1
    if m2 != "?":
        return m2
    if m3 != "?":
        return m3
    if m4 != "?":
        return m4


def decryptCharacter(character, a, b, p, q, n):
    print(f"The character is {character}.")

    mp = pow(character, (p + 1) // 4, p)
    mq = pow(character, (q + 1) // 4, q)
    print(f"Using the formula, r is {mp} and s is {mq}.")

    X = (a * p * mq + b * q * mp) % n
    Y = (a * p * mq - b * q * mp) % n
    print(f"X = (a*p*r + b*q*s) % n = ({a} * {p} * {mq} + {b} * {q} * {mp}) % {n} = {X}")
    print(f"Y = (a*p*r - b*q*s) % n = ({a} * {p} * {mq} - {b} * {q} * {mp}) % {n} = {Y}")

    m1 = X
    m2 = n-X
    m3 = Y
    m4 = n-Y
    print(f"m1 is {m1}.")
    print(f"m2 is {m2}.")
    print(f"m3 is {m3}.")
    print(f"m4 is {m4}.\n")

    m1 = convertASCIIToPlaintext(m1)
    m2 = convertASCIIToPlaintext(m2)
    m3 = convertASCIIToPlaintext(m3)
    m4 = convertASCIIToPlaintext(m4)

    print(f"m1 is {m1}.")
    print(f"m2 is {m2}.")
    print(f"m3 is {m3}.")
    print(f"m4 is {m4}.\n")

    return findRightChoice(m1,m2,m3,m4)

if __name__ == '__main__':

    p, q = generateKeys()
    n = p * q
    print(f"p = {p}\nq = {q}\nn = p * q = {n}")

    print(f"The public key is {n}, the private key is ({p}, {q}).\n")


    print("ENCRYPTION:")
    plaintext = input("What is the message you would like to encrypt?\nMessage:")
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z',
                ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                '.', ',', ';', '!']
    if plaintextIsValid(plaintext, alphabet) is False:
        print("Plaintext is not valid!!!")
    else:
        print("Plaintext is valid.")


    m = convertPlaintextToASCIIList(plaintext)
    print(f"The converted message to ASCII value is {m}.")

    m = encryptList(m, n)
    print(f"The encrypted message is {m}.\n\n\n")



    print("DECRYPTION:")
    ciphertext = m
    print(f"The ciphertext C is {ciphertext}.")
    if ciphertextIsValid(plaintext) is False:
        print("Ciphertext is not valid!!!")
    else:
        print("Ciphertext is valid.")


    gcd, a, b = extended_gcd(p, q)
    if gcd == 1:
        print(f"a:{a}, b: {b}, a * p + b * q = {a * p + b * q}")
    else:
        print(f"No solution exists as gcd({p}, {q}) != 1")

    decrypted_message = ""
    for character in ciphertext:
        decrypted_message += decryptCharacter(character, a, b, p, q, n)

    print(f"The decrypted message is {decrypted_message}.")
