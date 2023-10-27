from helper_class.expense import ExpenseRegistry
from helper_function.command_handler import handle_command, clear_terminal, cprint, command_list

"""
This is the main file for the expense tracker program. It is the file that should be run to start the program.
"""

expense_registry = ExpenseRegistry()

clear_terminal()

cprint("Welcome to your personal expense tracker!")

while True:
    command_list()
    cprint("Please input one of the key words above:", end='')
    user_input = input().strip()

    handle_command(expense_registry, user_input)
