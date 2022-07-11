def create_complex_number(real, imag):
    return {'real': real, 'imaginary': imag}

def get_real(number):
    return number['real']

def get_imag(number):
    return number['imaginary']

def set_real(number, real):
    number['real']=real

def set_imag(number, imag):
    number['imaginary']=imag


def add_number(numbers, real, imag):
    number  = create_complex_number(real, imag)
    numbers.append(number)

def ui_add_complex_number(numbers):
    real = int (input('Real part: '))
    imag = int (input('Imaginary part: '))
    add_number(numbers, real, imag)

def print_all_numbers(numbers):
    # The function prints the numbers in a nicer way.
    for i in range(0,len(numbers)):
        if get_imag(numbers[i])>0:
            print('z', i, '= ', get_real(numbers[i]), '+', get_imag(numbers[i]), 'i')
        else:
            print('z', i, '= ', get_real(numbers[i]), get_imag(numbers[i]), 'i')


def print_menu_options():
    #The function prints the menu which appears to the users.
    print('1 - Add number: \n'
          '2 - Print all numbers. \n'
          '3 - The longest sequence of distinct numbers. \n'
          '4 - The longest sequence which can be written with the same digits. \n'
          'x - Exit.')

def first_ten_numbers(numbers):
    add_number(numbers, 2, 3)
    add_number(numbers, 2, -23)
    add_number(numbers, 0, 8)
    add_number(numbers, -4, 43)
    add_number(numbers, -2, 6)
    add_number(numbers, -2, 6)
    add_number(numbers, 4, -3)
    add_number(numbers, 4, -3)
    add_number(numbers, 1, 3)
    add_number(numbers, 13, 11)

def distinct_numbers(number1, number2):
    #It checks if the given numbers are different.
    return number1!=number2

def search(numbers, real_part, imaginary_part):
    #Searches for a complex number and returns True if it finds it.
    for i in range(0, len(numbers)):
        if distinct_numbers(real_part, get_real(numbers[i])) == 0 and distinct_numbers(imaginary_part, get_imag(numbers[i])) ==0:
            return True
    return False

def sequence_distinct_numbers(numbers): #6
    '''
    Given a dictionary with complex numbers, the functions returns the longest sequence of distinct numbers.
    Both real and imaginary part have to be different comparing the other existent numbers.
    :param numbers: dictionary
    :return: the longest sequence of distinct numbers
    '''
    the_longest_sequence = []
    test_sequence = []
    add_number(test_sequence, get_real(numbers[0]), get_imag(numbers[0])) #it adds the first number so the rest of them can be compared to it
    i = 1
    j = 1 # it uses j to know where each sequence will begin
    while i<len(numbers) and j<len(numbers):
        if search(test_sequence, get_real(numbers[i]), get_imag(numbers[i])) == 0:
            add_number(test_sequence, get_real(numbers[i]), get_imag(numbers[i])) #if it the is different to any other number, the function adds it to the list
            i+=1
        else:
            if len(test_sequence) > len(the_longest_sequence): #checks if it has found a longest sequence than the actual one
                the_longest_sequence = test_sequence.copy()  #it copies the new sequence
            test_sequence.clear()
            add_number(test_sequence, get_real(numbers[j]), get_imag(numbers[j]))
            j+=1
            i=j #we continue with the next sequence after we finish checking the last one
        if len(test_sequence) > len(the_longest_sequence): #the last saved sequence needs to be checked too!
            the_longest_sequence = test_sequence.copy()
    return the_longest_sequence

def print_longest_seq_distinct_numbers(numbers):
    print_all_numbers((sequence_distinct_numbers(numbers)))

def digit_frequency(number, digit):
    #This function returns how many times a digit appears in a number.
    c = 0
    if number<0:
        number = -number
    while number!=0:
        if int(number%10) == digit:
            c+=1
        number//=10
    return c

def frequencies_for_a_number(number):
    #This function calculates the frequency of every digit from 0 to 9 for a given number.
    f = {}
    for i in range(10):
        f[i] = digit_frequency(number, i)
    return f

def frequencies_complex_number(real, imaginary):
    #This function checks which digits appear in a complex number.
    f_real = {}
    f_imaginary = {}
    f_real = frequencies_for_a_number(real)
    f_imaginary = frequencies_for_a_number(imaginary)
    f_complex_number = {}
    for i in range(10):
        f_complex_number[i] = f_real[i] + f_imaginary[i]
        if f_complex_number[i] >0: #the only important part is if a digit appears in a number, no how many times it does
            f_complex_number[i] = 1
    return f_complex_number

def same_frequency (number1_r, number1_i, number2_r, number2_i):
    fr1 = {}
    fr2 = {}
    fr1 = frequencies_complex_number(number1_r, number1_i)
    fr2 = frequencies_complex_number(number2_r, number2_i)
    for i in range(10):
        if fr1[i] != fr2[i]: # if one of the digits exists in one complex number but no in the other, this means they do not have the same digit frequency
            return False
    return True

def sequence_same_digits(numbers): #12
    '''
    Given a dictionary with complex numbers, the function finds the longest sequence which can be written with the same base 10 digits.
    :param numbers: dictionary
    :return: the longest sequence which can be written with the same base 10 digits
    '''
    the_longest_sequence = []
    test_sequence = []
    add_number(test_sequence, get_real(numbers[0]), get_imag(numbers[0]))
    precedent = 0
    i = 1
    j = 1
    while i < len(numbers) and j < len(numbers):
        if same_frequency(get_real(numbers[precedent]), get_imag(numbers[precedent]), get_real(numbers[i]), get_imag(numbers[i])):
            add_number(test_sequence, get_real(numbers[i]), get_imag(numbers[i]))
            i += 1
        else:
            if len(test_sequence) > len(the_longest_sequence):
                the_longest_sequence = test_sequence.copy()
            test_sequence.clear()
            add_number(test_sequence, get_real(numbers[j]), get_imag(numbers[j]))
            precedent = j
            j += 1
            i = j
        if len(test_sequence) > len(the_longest_sequence):
            the_longest_sequence = test_sequence.copy()
    return the_longest_sequence

def print_sequence_same_digits(numbers):
    print_all_numbers(sequence_same_digits(numbers))

def run_menu():
    numbers=[]
    first_ten_numbers(numbers)
    options = {1: ui_add_complex_number, 2: print_all_numbers, 3:print_longest_seq_distinct_numbers, 4:print_sequence_same_digits}
    while True:
        print_menu_options()
        opt = input('Insert an option: ')
        if opt == 'x':
            break
        opt = int(opt)
        options[opt](numbers)

if __name__ == '__main__':
    run_menu()