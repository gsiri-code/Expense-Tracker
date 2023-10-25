import os
import platform
from time import sleep
import utilities.TUI as TUI


def cprint(*args, sep=' ', end='\n', flush=False, speed=0):
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


def handle_command(expense_registry, user_input):
    if user_input == 'log':
        clear_terminal()
        expense_registry.add_expense()
    elif user_input == "view":
        clear_terminal()
        if expense_registry.isempty():
            cprint("Sorry, there are no expenses that have been logged yet.")
        else:
            TUI.create_view(expense_registry)
    elif user_input == "delete":
        clear_terminal()
        expense_registry.delete_expense()
    elif user_input == "summarize":
        pass
    elif user_input == "search":
        pass
    elif user_input == "exit":
        pass
    else:
        cprint("Invalid command. Please try again.")


def welcome_prompt(username):
    if not username:
        cprint("Welcome to your personal expense tracker!")

        while not username:
            cprint("Please enter your name: ", end='')
            username = input().strip()
        clear_terminal()
        cprint(f"""Welcome {username}, to your personal expense tracker!\n""")

def command_list():
    """
    Please choose one of the following commands:
        log - to log a new expense
        view - to view all expenses
        delete - to delete an expense
        summarize - to summarize your expenses
        search - to search for a specific expense
        exit - to exit the program
    """
    lprint(
        'Please choose one of the following commands:\n',
        '\tlog - to log a new expense\n',
        '\tview - to view all expenses\n',
        '\tdelete - to delete an expense\n',
        '\tsummarize - to summarize your expenses\n',
        '\tsearch - to search for a specific expense\n',
        '\texit - to exit the program\n'
    )
