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

def ui_add_expense(expenses, *args):
    expenses, ok = add_expense(expenses, *args)
    if ok == 0:
        print('The application did not add the expense.')


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
    assert remove_all_type_expenses([{'apartment': 1, 'amount': 200, 'type': 'gas'}, {'apartment': 2, 'amount': 10, 'type': 'gas'}, {'apartment': 3, 'amount': 120, 'type': 'water'}], 'gas') == [{'apartment': 3, 'amount': 120, 'type': 'water'}]

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



def print_no_expense(arg):
    print('There is no such expense for apartment ', arg, '.')

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

def ui_replace_amount(expenses, *args):
    expenses, ok = replace_amount(expenses, *args)
    if ok == 0:
        print_no_expense(args[0])

def print_expenses_apartment(expenses, number_of_apartment):
    """
    This function prints all the expenses for an apartment in a nice way.
    :param expenses: a list
    :param number_of_apartment: an integer
    """
    for i in range(0, len(expenses)):
        if get_number(expenses[i]) == number_of_apartment:
            list_one_expense(expenses, i)
            print('\n')

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

def print_apartments_with_specific_total_amount(expenses, sign, amount):
    list = []
    list = create_list_with_apartments(expenses, sign, amount)
    print('The corresponding apartments are:')
    for i in range(0, len(list)):
        print(list[i])

def list_one_expense(expenses, i):
    # This function prints the number, the amount and the type of one given expense.
    print('Expense ', i + 1, ':')
    print('The number of the apartment is', get_number(expenses[i]), '.')
    print('The amount of the expense is', get_amount(expenses[i]), '.')
    print('This expense is for', get_type(expenses[i]), '.')

def list_expenses_nicer(expenses):
    # This function prints all the expenses
    for i in range(0, len(expenses)):
        list_one_expense(expenses, i)
        print('\n')

def ui_list_options(expenses, *args):
    """
    This is the function for the "list" command. It can: print all the expenses, print the expenses for an apartment or print the apartments
    with a specific total amount (<, > or = to a given number).
    :param expenses: a list
    :param args: a tuple
    """
    if len(args) == 0:
        list_expenses_nicer(expenses)
    else:
        if len(args) == 1:
            print_expenses_apartment(expenses, int(args[0]))
        if len(args) == 2:
            print_apartments_with_specific_total_amount(expenses, args[0], int(args[1]))

def print_commands(commands):
    print('This application supports the following operations:')
    print(*list(commands.keys()), 'exit', sep='\n')

def first_ten_expenses(expenses):
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

def run_commands():
    expenses = []
    first_ten_expenses(expenses)
    commands = {'add': ui_add_expense, 'remove': remove_options, 'replace': ui_replace_amount, 'list': ui_list_options}
    while True:
        print_commands(commands)
        command_line = input('Enter command line:')
        if command_line == 'exit':
            break
        command, args = get_command_and_args(command_line)
        try:
            commands[command](expenses, *args)
            print('Command executed successfully.', '\n')
        except KeyError:
            print('This option is not yet implemented.', '\n')
        except IndexError:
            print('The application does not know what it should do.', '\n')
        except ValueError:
            print('It cannot do that.')
        except TypeError:
            print('This operation is not supported.')

if __name__ == '__main__':
    run_commands()
