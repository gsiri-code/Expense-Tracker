
try:
    expenses_file = open("expenses.txt", "a+")
    expenses_file.write("id | amount | category | description \n")
except:
    print("failed to open file")



total_expenses = 0
exp_id = 0
name_given = False

def handle_command(user_input):
    if user_input == 'log':
        pass
    elif user_input == "view":
        pass
    elif user_input == "delete":
        pass
    elif user_input == "summarize":
        pass
    elif user_input == "search":
        pass
    elif user_input == "exit":
        pass
    else:
        print("Invalid command. Please try again.")

def handle_command_loop(name_given):
    if (not name_given):
        print("Welcome to your personal expense tracker!")

        user_name = input("Please enter your name: ")
        name_given = True

        print(f"""Welcome {user_name}, to your personal expense tracker!
    Please choose one of the following commands:
        log - to log a new expense
        view - to view all expenses
        delete - to delete an expense
        summarize - to summarize your expenses
        search - to search for a specific expense
        exit - to exit the program \n""")



while True:
    handle_command_loop(name_given)

    user_input = input("Please input one of the key words above: ")

    if user_input == "exit":
        break

    handle_command(user_input)

expenses_file.close()
