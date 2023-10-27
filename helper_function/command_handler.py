import os
import platform
from time import sleep
import utilities.TUI as TUI


def cprint(*args, sep=' ', end='\n', flush=False, speed=20):
    for arg in args:
        for char in str(arg):
            print(char, end='', flush=True)
            sleep(speed / 1000)
        print(sep, end='', flush=True)
    print(end=end, flush=flush)

def lprint(*args, sep=' ', end='\n', flush=False, speed=150):
    for arg in args:
        print(arg, end='', flush=True)
        sleep(speed / 1000)
    print(end=end, flush=flush)

def clear_terminal():
    system = platform.system()
    if system == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def welcome_prompt(username):
    if not username:
        cprint("Welcome to your personal expense tracker!")

        while not username:
            cprint("Please enter your name: ", end='')
            username = input().strip()
        clear_terminal()
        cprint(f"""Welcome {username.capitalize()}, to your personal expense tracker!\n""")
        return username

def command_list():

    lprint(
        'Please choose one of the following commands:\n',
        '\t(l)og - to log a new expense\n',
        '\t(v)iew - to view all expenses\n',
        '\t(d)elete - to delete an expense\n',
        '\t(s)ummarize - to summarize your expenses\n',
        '\t(f)ind - to search for a specific expense\n',
        '\t(q)uit - to end the program\n'
    )
def handle_command(expense_registry, user_input,username):
    if user_input == 'log' or user_input == 'l':
        clear_terminal()
        expense_registry.add_expense()
    elif user_input == "view" or user_input == "v":
        clear_terminal()
        if expense_registry.isempty():
            cprint("Sorry, there are no expenses that have been logged yet.")
        else:
            TUI.create_view(expense_registry)
    elif user_input == "delete" or user_input == "d":
        clear_terminal()
        if expense_registry.isempty():
            cprint("Sorry, there are no expenses that have been logged yet.")
        elif expense_registry.delete_expense():
            lprint(f"Expense has successfully been deleted.")
        else:
            lprint("Sorry, there is no expense with that ID.")

    elif user_input == "summarize" or user_input == "s":
        clear_terminal()
        expense_registry.summarize()
    elif user_input == "find" or user_input == "f":
        clear_terminal()
        if expense_registry.isempty():
            cprint("Sorry, there are no expenses that have been logged yet.")
        else:
            expense_registry.search()
    elif user_input == "quit" or user_input == "q":
        clear_terminal()
        expense_registry.save("expenses.csv")

        cprint(f"Goodbye {username.capitalize()}, all of your expenses have been saved in expenses.csv!")
        exit()
    else:
        cprint("Invalid command. Please try again.")




