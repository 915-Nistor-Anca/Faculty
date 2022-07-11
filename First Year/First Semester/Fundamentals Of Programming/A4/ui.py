"""
  User interface module
"""
from functions import add_expense, replace_amount, get_amount, get_number, get_type, get_command_and_args, create_list_with_apartments
from functions import remove_options, first_ten_expenses, sum_type, maximum_amount_per_expense_type, sort_apartment, sort_type
from functions import calculate_amount_all_expenses_each_type, is_type, filter_type, filter_value, add_list_to_changes
from functions import the_last_element, remove_list_from_changes

def ui_add_expense(expenses, *args):
    expenses, ok = add_expense(expenses, *args)
    if ok == 0:
        print('The application did not add the expense.')

def print_no_expense(arg):
    print('There is no such expense for apartment ', arg, '.')

def ui_replace_amount(expenses, *args):
    expenses, ok = replace_amount(expenses, *args)
    if ok == 0:
        print_no_expense(args[0])

def list_one_expense(expenses, i):
    # This function prints the number, the amount and the type of one given expense.
    print('Expense ', i + 1, ':')
    print('The number of the apartment is', get_number(expenses[i]), '.')
    print('The amount of the expense is', get_amount(expenses[i]), '.')
    print('This expense is for', get_type(expenses[i]), '.')

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

def print_apartments_with_specific_total_amount(expenses, sign, amount):
    list = []
    list = create_list_with_apartments(expenses, sign, amount)
    print('The corresponding apartments are:')
    for i in range(0, len(list)):
        print(list[i])

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


def print_sum_type(expenses, *args):
    s = sum_type(expenses, *args)
    print('The total amount for the expenses having type', args[0], 'is', s, '.')

def print_maximum_amount_per_expense_type(expense, *args):
    list = maximum_amount_per_expense_type(expense, *args)
    ok = list['water'] != 0 or list['electricity'] != 0 or list['gas'] != 0 or list['other'] != 0 or list['heating'] != 0
    if ok == 1:
        #print(list)
        print('Water:', list['water'])
        print('Electricity:', list['electricity'])
        print('Heating:', list['heating'])
        print('Gas:', list['gas'])
        print('Other:', list['other'])
    else:
        print('Apartment number', args[0], 'has no expenses.')

def print_sort_apartment(expenses, *args):
    numbers = sort_apartment(expenses, *args)
    print('These are the numbers of all the apartments sorted ascending by total amount of expenses:')
    for i in numbers:
        print(i)

def print_sort_types(expenses, *args):
    list = sort_type(expenses, *args)
    amount_types = calculate_amount_all_expenses_each_type(expenses, *args)
    for i in range(0, len(list)):
        print('The total amount of expenses for', list[i], 'is', amount_types[list[i]], '.')

def sort_options(expenses, *args):
    if args[0] == 'apartment':
        print_sort_apartment(expenses, *args)
    elif args[0] == 'type':
        print_sort_types(expenses, *args)
    else:
        print('This application cannot sort that.')

def filter_options(expenses, *args):
    if is_type(args[0]):
        filter_type(expenses, *args)
    else:
        filter_value(expenses, *args)

def print_undo(expenses, changes):
    if len(changes) > 1:
        remove_list_from_changes(changes)
        expenses = the_last_element(changes).copy()
        print('Operation reversed.')
    else:
        print('Cannot reverse operation.')
    return expenses


def run_commands():
    expenses = []
    changes = []
    first_ten_expenses(expenses)
    changes = add_list_to_changes(expenses, changes)
    #for i in range(0, len(changes)):
        #print(changes[i], '\n')
    commands = {'add': ui_add_expense, 'remove': remove_options, 'replace': ui_replace_amount, 'list': ui_list_options,
                'sum': print_sum_type, 'max': print_maximum_amount_per_expense_type, 'sort': sort_options, 'filter': filter_options, 'undo': print_undo}
    while True:
        print_commands(commands)
        command_line = input('Enter command line:')
        if command_line == 'exit':
            break
        command, args = get_command_and_args(command_line)
        try:
            if command != 'undo':
                commands[command](expenses, *args)
                if command == 'add' or command == 'remove' or command == 'replace' or command == 'filter':
                    changes = add_list_to_changes(expenses, changes)
                    ##for i in range(0, len(changes)):
                        #print(changes[i], '\n')
            else:
                expenses = commands[command](expenses, changes)
                #for i in range(0, len(changes)):
                    #print(changes[i], '\n')
            print('Command executed successfully.', '\n')
        except KeyError:
            print('This option is not yet implemented.', '\n')
        except IndexError:
            print('The application does not know what it should do.', '\n')
        except ValueError:
            print('It cannot do that.')
        except TypeError:
            print('This operation is not supported.')