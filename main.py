from helper_class.expense import ExpenseRegistry
from helper_function.command_handler import handle_command, clear_terminal, cprint, command_list

expense_registry = ExpenseRegistry()

clear_terminal()

cprint("Welcome to your personal expense tracker!")

while True:
    command_list()
    cprint("Please input one of the key words above:", end='')
    user_input = input().strip()

    handle_command(expense_registry,user_input)




