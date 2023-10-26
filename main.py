from helper_class.expense import ExpenseRegistry
from helper_function.command_handler import handle_command, welcome_prompt, clear_terminal, cprint, command_list

expense_registry = ExpenseRegistry()
username = None

clear_terminal()

username = welcome_prompt(username)

while True:
    command_list()
    cprint("Please input one of the key words above:", end='')
    user_input = input().strip()

    handle_command(expense_registry,user_input,username)




