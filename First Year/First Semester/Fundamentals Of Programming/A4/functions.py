"""
  Program functionalities module
"""

def create_expense(number_of_apartment, amount, its_type):
    return {'apartment': number_of_apartment, 'amount': amount, 'type': its_type}

def add_new_expense(expenses, number_of_apartment, amount, its_type):
    ex = create_expense(number_of_apartment,amount, its_type)
    expenses.append(ex)

def get_number(expenses):
    return expenses['apartment']

def get_amount(expenses):
    return expenses['amount']

def get_type(expenses):
    return expenses['type']

def set_amount(expenses, new_amount):
    expenses['amount'] = new_amount

def is_type(arg):
    """
    The function checks if the given type is one of the following: water, gas, electricity, heating or other.
    :param arg: a string
    :return: 1, if it finds the given type and 0, on the contrary
    """
    return arg == 'gas' or arg == 'water' or arg == 'heating' or arg == 'electricity' or arg == 'other'

def test_is_type():
    assert is_type('gas') == 1
    assert is_type('flowers') == 0

test_is_type()

def add_expense(expenses, *args):
    """
    This function adds a new expense to the list. Its type, amount and the number of the apartment are stored in args.
    Before adding the expense, the function checks whether it makes sense to do the new addition (if the type/number is well entered) or not.
    In case the introduced data is not correct, it prints a message.
    :param expenses: a list
    :param args: a tuple
    """
    ok = 0
    if is_type(args[1]) and (int(args[0]) >= 0 and int(args[0]) <= 99999999):
        ok = 1
        add_new_expense(expenses, int(args[0]), int(args[-1]), args[1])
    return expenses, ok

def testadd_expense():
    assert add_expense([{'apartment': 1, 'amount': 200, 'type': 'gas'}, {'apartment': 1, 'amount': 10, 'type': 'water'}], '1', 'electricity', '150') == \
           ([{'apartment': 1, 'amount': 200, 'type': 'gas'}, {'apartment': 1, 'amount': 10, 'type': 'water'}, {'apartment': 1, 'amount': 150, 'type': 'electricity'}], 1)

testadd_expense()

def remove_all_type_expenses(expenses, its_type):
    """
    The function removes all the expenses which have the given type. It uses n to define the lenght of the list and functions with "while" because n changes.
    :param expenses: a list
    :param its_type: a string
    :return: the new list of expenses
    """
    n = len(expenses)
    i=0
    while i < n:
        if get_type(expenses[i]) == its_type:
            expenses.remove(expenses[i])
            n-=1
        else:
            i+=1
    return expenses

def testremove_all_type_expenses():
    assert remove_all_type_expenses([{'apartment': 1, 'amount': 200, 'type': 'gas'}, {'apartment': 2, 'amount': 10, 'type': 'gas'},
                                     {'apartment': 3, 'amount': 120, 'type': 'water'}], 'gas') == [{'apartment': 3, 'amount': 120, 'type': 'water'}]

testremove_all_type_expenses()

def remove_all_expenses_for_the_apartment(expenses, number_of_apartment):
    """
    The function removes all the expenses for a given apartment. It uses n to define the lenght of the list and functions with "while" because n changes.
    :param expenses: a list
    :param number_of_apartment: an integer
    """
    n = len(expenses)
    i = 0
    while i < n:
        if get_number(expenses[i]) == number_of_apartment:
            expenses.remove(expenses[i])
            n -= 1
        else:
            i += 1
    return expenses

def testremove_all_expenses_for_the_apartment():
    assert remove_all_expenses_for_the_apartment(
        [{'apartment': 1, 'amount': 200, 'type': 'gas'}, {'apartment': 1, 'amount': 10, 'type': 'water'},
         {'apartment': 3, 'amount': 120, 'type': 'water'}], 1) == [{'apartment': 3, 'amount': 120, 'type': 'water'}]

testremove_all_expenses_for_the_apartment()

def remove_options(expenses, *args):
    """
    This function deals with the remove options.
    It can: remove all the expenses of a type, remove the expenses for an apartment or remove the expenses for all the apartments from a number to other.
    :param expenses: a list
    :param args: a tuple
    """
    if len(args) == 1:
        if(is_type(args[0])):
            remove_all_type_expenses(expenses, args[0])
        else:
            remove_all_expenses_for_the_apartment(expenses, int(args[0]))
    elif len(args) == 3:
        for i in range(int(args[0]), int(args[2])+1):
            remove_all_expenses_for_the_apartment(expenses, i)
    return expenses

def testremove_options():
    assert remove_options([{'apartment': 1, 'amount': 200, 'type': 'gas'}, {'apartment': 1, 'amount': 10, 'type': 'water'},
         {'apartment': 3, 'amount': 120, 'type': 'water'}, {'apartment': 3, 'amount': 120, 'type': 'gas'}], 'gas') == \
           [{'apartment': 1, 'amount': 10, 'type': 'water'}, {'apartment': 3, 'amount': 120, 'type': 'water'}]
    assert remove_options(
        [{'apartment': 1, 'amount': 200, 'type': 'gas'}, {'apartment': 1, 'amount': 10, 'type': 'water'},
         {'apartment': 3, 'amount': 120, 'type': 'water'}, {'apartment': 3, 'amount': 120, 'type': 'gas'}], '1') == \
           [{'apartment': 3, 'amount': 120, 'type': 'water'}, {'apartment': 3, 'amount': 120, 'type': 'gas'}]
    assert remove_options(
        [{'apartment': 1, 'amount': 200, 'type': 'gas'}, {'apartment': 1, 'amount': 10, 'type': 'water'},
         {'apartment': 3, 'amount': 120, 'type': 'water'}, {'apartment': 3, 'amount': 120, 'type': 'gas'},
         {'apartment': 4, 'amount': 220, 'type': 'other'}, {'apartment': 5, 'amount': 125, 'type': 'electricity'}], '2', 'to', '4') == \
         [{'apartment': 1, 'amount': 200, 'type': 'gas'}, {'apartment': 1, 'amount': 10, 'type': 'water'},{'apartment': 5, 'amount': 125, 'type': 'electricity'}]

testremove_options()

def replace_amount(expenses, *args):
    """
    This function replaces the amount of an expense with a new one.
    It takes all the expenses, one by one and modifies the amount if the number of the apartment of an expense is equal to the given number.
    :param expenses: a list
    :param args: a tuple
    """
    ok = 0
    for i in range(0, len(expenses)):
        if get_number(expenses[i]) == int(args[0]):
            if get_type(expenses[i]) == args[1]:
                ok = 1
                set_amount(expenses[i], args[-1])
    return expenses, ok

def testreplace_amount():
    assert replace_amount([{'apartment': 1, 'amount': 200, 'type': 'gas'}, {'apartment': 1, 'amount': 10, 'type': 'water'},
         {'apartment': 3, 'amount': 120, 'type': 'water'}, {'apartment': 3, 'amount': 120, 'type': 'gas'},
         {'apartment': 4, 'amount': 220, 'type': 'other'}, {'apartment': 5, 'amount': 125, 'type': 'electricity'}], '1', 'gas', 'with', 300) == \
           ([{'apartment': 1, 'amount': 300, 'type': 'gas'}, {'apartment': 1, 'amount': 10, 'type': 'water'},
            {'apartment': 3, 'amount': 120, 'type': 'water'}, {'apartment': 3, 'amount': 120, 'type': 'gas'},
            {'apartment': 4, 'amount': 220, 'type': 'other'}, {'apartment': 5, 'amount': 125, 'type': 'electricity'}], 1)

testreplace_amount()

def sum_all_expenses_for_apartment(expenses, number_of_apartment):
    """
    This function calculets the total sum of the expenses for one apartment. The number of the apartment is given.
    The function goes through the entire list of expenses and adds the ones which have the same apartment number as the parameter one.
    :param expenses: a list
    :param number_of_apartment: an integer
    :return: an integer, which represent the sum of all the apartment's expenses.
    """
    s = 0
    for i in range(0, len(expenses)):
        if get_number(expenses[i]) == number_of_apartment:
            s += get_amount(expenses[i])
    return s

def test_sum_all_expenses_for_apartment():
    assert sum_all_expenses_for_apartment([{'apartment': 1, 'amount': 20, 'type': 'gas'}, {'apartment': 1, 'amount': 30, 'type': 'water'}, {'apartment': 1, 'amount': 25, 'type': 'heating'}, {'apartment': 2, 'amount': 200, 'type': 'other'}, {'apartment': 2, 'amount': 150, 'type': 'water'}, {'apartment': 2, 'amount': 130, 'type': 'electricity'}, {'apartment': 2, 'amount': 80, 'type': 'gas'}], 1) == 75

test_sum_all_expenses_for_apartment()

def search_for_number(list, number):
    """
    This function searches if the given number appears in the given list.
    :param list: a list of integers
    :param number: the searched integer
    :return: True, if the number can be found and False, if not.
    """
    for i in range(0, len(list)):
        if list[i] == number:
            return True
    return False

def test_search_for_number():
    assert search_for_number([0, 2, 4, 6, 8], 3) == 0
    assert search_for_number([0, 2, 4, 6, 8], 2) == 1

test_search_for_number()

def specific_total_amount(sign, sum, amount):
    return (sign == '>' and sum > amount) or (sign == '<' and sum < amount) or (sign == '=' and sum == amount)

def testspecific_total_amount():
    assert specific_total_amount('>', 100, 50) == 1
    assert specific_total_amount('<', 50, 100) == 1
    assert specific_total_amount('=', 10, 20) == 0

testspecific_total_amount()

def create_list_with_apartments(expenses, sign, amount):
    """
    This function saves the number of the apartments which are <, > or  = than the given amount (depending on the sign)
    It makes the sum of all the expenses for each apartment. In order to avoid having saved the same number (of an apartment) twice,
    the function checks if that apartment wasn't already saved. (This is necessary, because the function goes through the list of the expenses;
    but what matters are, actually, the apartments (which are not saved in a list.))
    :param expenses: a list
    :param sign: a string
    :param amount: an integer
    """
    list = []
    for i in range(0, len(expenses)):
        sum = sum_all_expenses_for_apartment(expenses, get_number(expenses[i]))
        if specific_total_amount(sign, sum, amount) == 1 and search_for_number(list, get_number(expenses[i])) == 0:
            list.append(get_number(expenses[i]))
    return list

def testcreate_list_with_apartments():
    assert create_list_with_apartments([{'apartment': 1, 'amount': 20, 'type': 'gas'}, {'apartment': 1, 'amount': 30, 'type': 'water'},
                                      {'apartment': 1, 'amount': 25, 'type': 'heating'}], '<', 80) == [1]

testcreate_list_with_apartments()

def first_ten_expenses(expenses):
    """
    This
    :param expenses: a list
    """
    add_new_expense(expenses, 1, 20, 'gas')
    add_new_expense(expenses, 1, 30, 'water')
    add_new_expense(expenses, 1, 25, 'heating')
    add_new_expense(expenses, 2, 200, 'other')
    add_new_expense(expenses, 2, 150, 'water')
    add_new_expense(expenses, 2, 130, 'electricity')
    add_new_expense(expenses, 2, 80, 'gas')
    add_new_expense(expenses, 3, 40, 'heating')
    add_new_expense(expenses, 4, 50, 'electricity')
    add_new_expense(expenses, 4, 30, 'gas')
    add_new_expense(expenses, 6, 120, 'other')
    add_new_expense(expenses, 6, 45, 'water')
    add_new_expense(expenses, 6, 20, 'electricity')
    add_new_expense(expenses, 7, 15, 'heating')
    return expenses

def testfirst_ten_expenses():
    assert first_ten_expenses([]) == [{'apartment': 1, 'amount': 20, 'type': 'gas'}, {'apartment': 1, 'amount': 30, 'type': 'water'},
                                      {'apartment': 1, 'amount': 25, 'type': 'heating'}, {'apartment': 2, 'amount': 200, 'type': 'other'},
                                      {'apartment': 2, 'amount': 150, 'type': 'water'}, {'apartment': 2, 'amount': 130, 'type': 'electricity'},
                                      {'apartment': 2, 'amount': 80, 'type': 'gas'}, {'apartment': 3, 'amount': 40, 'type': 'heating'},
                                      {'apartment': 4, 'amount': 50, 'type': 'electricity'}, {'apartment': 4, 'amount': 30, 'type': 'gas'},
                                      {'apartment': 6, 'amount': 120, 'type': 'other'}, {'apartment': 6, 'amount': 45, 'type': 'water'},
                                      {'apartment': 6, 'amount': 20, 'type': 'electricity'}, {'apartment': 7, 'amount': 15, 'type': 'heating'}]

testfirst_ten_expenses()

def remove_useless_spaces(command_line):
    """
    This function removes the useless spaces between words.
    :param command_line: a string
    :return: the same given string, but without the unnecessary spaces
    """
    new_command_line = ' '
    for i in range(0, len(command_line)):
        if (command_line[i] >='a' and command_line[i] <='z') or (command_line[i] >='A' and command_line[i] <='Z') or (command_line[i] == '<' or command_line[i] == '>' or command_line[i] == '=') or (command_line[i] >='0' and command_line[i] <='9') or (command_line[i] == ' ' and new_command_line[-1]!=' '):
            new_command_line = new_command_line + command_line[i]
    if new_command_line[0] == ' ':
        new_command_line = new_command_line.removeprefix(' ')
    if new_command_line[-1] == ' ':
        new_command_line = new_command_line.removesuffix(' ')
    return new_command_line

def test_remove_useless_spaces():
    assert remove_useless_spaces(' add            2        gas    30  ') == 'add 2 gas 30'

test_remove_useless_spaces()

def get_command_and_args(command_line):
    """
    This function gives the command and the arguments from a command line.
    It uses another defined function to remove the unnecessary spaces, in order to create the arguments list properly.
    :param command_line: a string
    :return: the command and the arguments
    """
    command_line = remove_useless_spaces(command_line)
    position = command_line.find(' ')
    if position == -1:
        return command_line, []
    command = command_line[:position]
    args = command_line[position+1:]
    args = args.split(' ')
    for word in args:
        word=word.replace(' ', '')
    return command, args

def test_get_command_and_args():
    assert get_command_and_args('add      2 gas 30   ') == ('add', ['2', 'gas', '30'])

test_get_command_and_args()

def sum_type(expenses, *args):
    """
    This function adds all the amount for the expenses having the given type.
    :param expenses: a list
    :param args: a tuple
    :return: the sum of all the expenses having a mentioned type
    """
    s = 0
    for i in range(0, len(expenses)):
        if get_type(expenses[i]) == args[0]:
            s +=get_amount(expenses[i])
    return s

def test_sum_type():
    assert sum_type([{'apartment': 1, 'amount': 20, 'type': 'gas'}, {'apartment': 4, 'amount': 30, 'type': 'water'},
                     {'apartment': 3, 'amount': 25, 'type': 'gas'}], 'gas') == 45

test_sum_type()

def create_dict_with_types(water, electricity, heating, gas, other):
    """
    This function returns a dictionary with all the types of expenses.
    :param water: an integer
    :param electricity: an integer
    :param heating: an integer
    :param gas: an integer
    :param other: an integer
    :return: a dictionary
    """
    return {'water': water, 'electricity': electricity, 'heating': heating, 'gas': gas, 'other': other}

def test_create_dict_with_types():
    assert create_dict_with_types(1,2,3,4,5) == {'water': 1, 'electricity': 2, 'heating': 3, 'gas': 4, 'other': 5}

test_create_dict_with_types()

def maximum_amount_per_expense_type(expenses, *args):
    """
    This function returns a dictionary with the maximum amount per each expense type for the given apartment.
    The number of the apartment is in args. The function takes all the expenses and checks if they belong to the apartment.
    If they do, the function checks if the amount of the expense is bigger than the biggest amount found until that moment for that type.
    If so, it changes the current value of the maximum expense with the new one.
    :param expenses: a list
    :param args: a tuple
    :return: a dictionary
    """
    max_values = {'water': 0, 'electricity': 0, 'heating': 0, 'gas': 0, 'other': 0}
    for i in range(0, len(expenses)):
        if get_number(expenses[i]) == int(args[0]):
            if get_amount(expenses[i]) > max_values[get_type(expenses[i])]:
                max_values[get_type(expenses[i])] = get_amount(expenses[i])
    return max_values

def test_maximum_amount_per_expense_type():
    assert maximum_amount_per_expense_type(
        [{'apartment': 1, 'amount': 20, 'type': 'gas'}, {'apartment': 4, 'amount': 30, 'type': 'water'},
                     {'apartment': 1, 'amount': 25, 'type': 'gas'}, {'apartment': 1, 'amount': 50, 'type': 'water'}], 1) == \
           {'water': 50, 'electricity': 0, 'heating': 0, 'gas': 25, 'other': 0}

test_maximum_amount_per_expense_type()

def apartment_amount(expenses, number_of_apartment):
    """
    This function calculates the total amount of the expenses for an apartment.
    :param expenses: a list
    :param number_of_apartment: an integer
    :return: the sum of all the expenses for the given apartment
    """
    s = 0
    for i in range(0, len(expenses)):
        if get_number(expenses[i]) == int(number_of_apartment):
            s += get_amount(expenses[i])
    return s

def test_apartment_amount():
    assert apartment_amount([{'apartment': 1, 'amount': 20, 'type': 'gas'}, {'apartment': 4, 'amount': 30, 'type': 'water'},
                     {'apartment': 1, 'amount': 25, 'type': 'other'}, {'apartment': 1, 'amount': 50, 'type': 'water'}], 1) == 95

test_apartment_amount()

def numbers_of_the_apartments(expenses):
    """
    This function creates a list with the numbers of the apartments which have expenses.
    :param expenses: a list
    :return: a list with the numbers of the apartments
    """
    numbers = []
    for i in range(0, len(expenses)):
        if search_for_number(numbers, get_number(expenses[i])) == 0:
            numbers.append(get_number(expenses[i]))
    return numbers

def test_numbers_of_the_apartments():
    assert numbers_of_the_apartments([{'apartment': 1, 'amount': 20, 'type': 'gas'}, {'apartment': 4, 'amount': 30, 'type': 'water'},
                     {'apartment': 1, 'amount': 25, 'type': 'other'}, {'apartment': 3, 'amount': 50, 'type': 'water'}]) == [1, 4, 3]

test_numbers_of_the_apartments()

def sort_apartment(expenses, *args):
    """
    This function uses BubbleSort to sort the numbers of the apartments ascending by total amount of expenses (for each apartment).
    :param expenses: a list
    :param args: a tuple
    """
    ok = 1
    numbers = []
    numbers = numbers_of_the_apartments(expenses)
    for i in range(0, len(numbers)-1):
        if apartment_amount(expenses, int(numbers[i])) > apartment_amount(expenses, int(numbers[i+1])):
            ok = 0
            aux = int(numbers[i])
            numbers[i] = numbers[i+1]
            numbers[i+1] = aux
    while ok == 0:
        ok = 1
        for i in range(0, len(numbers) - 1):
            if apartment_amount(expenses, int(numbers[i])) > apartment_amount(expenses, int(numbers[i + 1])):
                ok = 0
                aux = int(numbers[i])
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = aux
    return numbers

def test_sort_apartment():
    assert sort_apartment([{'apartment': 1, 'amount': 20, 'type': 'gas'}, {'apartment': 4, 'amount': 30, 'type': 'water'},
                     {'apartment': 1, 'amount': 25, 'type': 'other'}, {'apartment': 3, 'amount': 50, 'type': 'water'}], 'apartment') == [4, 1, 3]

test_sort_apartment()

def calculate_amount_all_expenses_each_type(expenses, *args):
    """
    This function calculates the total amount for each type of expense.
    :param expenses: a list
    :param args: a tuple
    :return: a dictionary
    """
    amount_types = create_dict_with_types(0,0,0,0,0)
    for i in range(0, len(expenses)):
        amount_types[get_type(expenses[i])] += int(get_amount(expenses[i]))
    return amount_types

def test_calculate_amount_all_expenses_each_type():
    assert calculate_amount_all_expenses_each_type([{'apartment': 1, 'amount': 20, 'type': 'gas'}, {'apartment': 4, 'amount': 30, 'type': 'water'},
                     {'apartment': 1, 'amount': 25, 'type': 'other'}, {'apartment': 3, 'amount': 50, 'type': 'water'}], 'type') == \
           {'water': 80, 'electricity': 0, 'heating': 0, 'gas': 20, 'other': 25}

test_calculate_amount_all_expenses_each_type()

def sort_type(expenses, *args):
    """
    This function sorts the types, ascending by amount of money.
    :param expenses: a list
    :param args: a tuple
    :return: a sorted list which contains the types of the expenses
    """
    amount_types = calculate_amount_all_expenses_each_type(expenses, *args)
    list = ['water', 'electricity', 'gas', 'heating', 'other']
    ok = 1
    for i in range (0, len(list)-1):
        if amount_types[list[i]] > amount_types[list[i+1]]:
            ok = 0
            aux = list[i]
            list[i] = list[i+1]
            list[i+1] = aux
    while ok == 0:
        ok = 1
        for i in range(0, len(list) - 1):
            if amount_types[list[i]] > amount_types[list[i + 1]]:
                ok = 0
                aux = list[i]
                list[i] = list[i + 1]
                list[i + 1] = aux
    return list

def test_sort_type():
    assert sort_type([{'apartment': 1, 'amount': 20, 'type': 'gas'}, {'apartment': 4, 'amount': 30, 'type': 'water'},
                     {'apartment': 1, 'amount': 25, 'type': 'other'}, {'apartment': 3, 'amount': 50, 'type': 'water'}], 'type') == \
        ['electricity', 'heating', 'gas', 'other', 'water']

test_sort_type()

def filter_type(expenses, *args):
    """
    This function removes the expenses which are not the given type.
    :param expenses: a list
    :param args: a tuple
    """
    n = len(args)
    i = 0
    while i < n:
        if get_type(expenses[i]) != args[0]:
            expenses.remove(expenses[i])
            n-=1
        else:
            i+=1
        n = len(expenses)
    return expenses

def test_filter_type():
    assert filter_type([{'apartment': 1, 'amount': 20, 'type': 'gas'}, {'apartment': 4, 'amount': 30, 'type': 'water'},
                     {'apartment': 1, 'amount': 25, 'type': 'other'}, {'apartment': 3, 'amount': 50, 'type': 'water'}], 'water') == \
        [{'apartment': 4, 'amount': 30, 'type': 'water'}, {'apartment': 3, 'amount': 50, 'type': 'water'}]

test_filter_type()

def filter_value(expenses, *args):
    """
    This function removes the expenses which have the amount of money bigger than (or equal to) the given value.
    :param expenses: a list
    :param args: a tuple
    """
    n = len(args)
    i = 0
    while i < n:
        if get_amount(expenses[i]) >= int(args[0]):
            expenses.remove(expenses[i])
            n-=1
        else:
            i+=1
        n = len(expenses)
    return expenses

def test_filter_value():
    assert filter_value([{'apartment': 1, 'amount': 20, 'type': 'gas'}, {'apartment': 4, 'amount': 70, 'type': 'water'},
                     {'apartment': 1, 'amount': 25, 'type': 'other'}, {'apartment': 3, 'amount': 50, 'type': 'water'}], 45) == \
        [{'apartment': 1, 'amount': 20, 'type': 'gas'}, {'apartment': 1, 'amount': 25, 'type': 'other'}]

test_filter_value()


def add_list_to_changes(expenses, changes):
    """
    This function adds a new list to a list of lists. Each list represents a change made to the original list of expenses.
    The function copies the lists one by one in a new list, then adds the new change in the same way.
    :param expenses: a list
    :param changes: a list
    :return: the new list with the added change
    """
    new_changes = []
    for i in range(0, len(changes)):
        new = []
        for j in range(0, len(changes[i])):
            new_expense = changes[i][j].copy()
            new.append(new_expense)
        new_changes.append(new) #added the lists which were already there
    new_expenses = []
    for i in range(0, len(expenses)):
        expense = expenses[i].copy()
        new_expenses.append(expense)
    new_changes.append(new_expenses)
    return new_changes


def test_add_list_to_changes():
    assert add_list_to_changes([{'apartment': 1, 'amount': 20, 'type': 'gas'}, {'apartment': 4, 'amount': 70, 'type': 'water'}],
                              [[{'apartment': 7, 'amount': 32, 'type': 'electricity'}, {'apartment': 4, 'amount': 70, 'type': 'water'}],
                               [{'apartment': 1, 'amount': 25, 'type': 'other'}, {'apartment': 1, 'amount': 250, 'type': 'heating'}]]) == \
            [[{'apartment': 7, 'amount': 32, 'type': 'electricity'}, {'apartment': 4, 'amount': 70, 'type': 'water'}],
             [{'apartment': 1, 'amount': 25, 'type': 'other'},{'apartment': 1, 'amount': 250, 'type': 'heating'}],
            [{'apartment': 1, 'amount': 20, 'type': 'gas'}, {'apartment': 4, 'amount': 70, 'type': 'water'}]]
    assert add_list_to_changes([{'apartment': 1, 'amount': 20, 'type': 'gas'}, {'apartment': 4, 'amount': 70, 'type': 'water'}], []) == \
        [[{'apartment': 1, 'amount': 20, 'type': 'gas'}, {'apartment': 4, 'amount': 70, 'type': 'water'}]]
    assert add_list_to_changes([{'apartment': 1, 'amount': 25, 'type': 'other'}], [[{'apartment': 2, 'amount': 251, 'type': 'gas'}]]) == \
        [[{'apartment': 2, 'amount': 251, 'type': 'gas'}], [{'apartment': 1, 'amount': 25, 'type': 'other'}]]

test_add_list_to_changes()


def remove_list_from_changes(changes):
    """
    This function removes the last element from a list.
    :param changes: a list
    """
    changes.pop()
    return changes

def test_remove_list_from_changes():
    assert remove_list_from_changes( [[{'apartment': 1, 'amount': 25, 'type': 'other'}, {'apartment': 1, 'amount': 25, 'type': 'electricity'}],
           [{'apartment': 1, 'amount': 20, 'type': 'gas'}, {'apartment': 4, 'amount': 70, 'type': 'water'}], [{'apartment': 10, 'amount': 25, 'type': 'other'}]]) == \
          [[{'apartment': 1, 'amount': 25, 'type': 'other'}, {'apartment': 1, 'amount': 25, 'type': 'electricity'}],
           [{'apartment': 1, 'amount': 20, 'type': 'gas'}, {'apartment': 4, 'amount': 70, 'type': 'water'}]]

test_remove_list_from_changes()

def the_last_element(changes):
    """
    This function returns the last element of a list.
    :param changes: a list
    :return: the last element of a list
    """
    last_list = changes[-1].copy()
    return last_list

def test_the_last_element():
    assert the_last_element([[{'apartment': 1, 'amount': 25, 'type': 'other'}, {'apartment': 1, 'amount': 25, 'type': 'electricity'}],
                             [{'apartment': 1, 'amount': 20, 'type': 'gas'}, {'apartment': 4, 'amount': 70, 'type': 'water'}]]) == \
           [{'apartment': 1, 'amount': 20, 'type': 'gas'}, {'apartment': 4, 'amount': 70, 'type': 'water'}]

test_the_last_element()

