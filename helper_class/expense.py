import datetime
from helper_function.command_handler import cprint, lprint
from utilities.Table import Table
# from fuzzywuzzy import process

class ExpenseRegistry:

    class Expense:

        def __init__(self, exp_id, amount, category, description):
            self.exp_id = exp_id
            self.date_time = datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')

            self.amount = amount
            self.category = category
            self.description = description

        def __str__(self):
            return f' Expense {self.exp_id}: {self.amount}| {self.category} | {self.description} \n'

        def __repr__(self):
            return f' Expense {self.exp_id}: {self.amount}| {self.category} | {self.description} \n'

        def __eq__(self, other):
            return self.amount == other.amount and self.category == other.category and self.description == other.description

        def get_amount(self):
            return self.amount

        def get_category(self):
            return self.category

        def get_description(self):
            return self.description

        def get_id(self):
            return self.exp_id

    def __init__(self):
        self.exp_id = 0
        self.expenses = {}
        self.total_val = 0
        self.amount_of_exp = 0

    def add_expense(self):
        amount = category = description = None
        while not (amount and category and description):
            try:
                cprint("Please enter the amount:", end="")
                amount = float(input())
                cprint("Please enter the category (ex. food , transportation..):", end="")
                category = str(input().strip())
                cprint("Please enter the description:", end="")
                description = str(input().strip())
            except ValueError:
                cprint("Please enter a valid amount.")

        self.exp_id += 1
        new_expense = ExpenseRegistry.Expense(self.exp_id,amount, category, description)
        self.expenses[new_expense.get_id()] = new_expense
        self.expenses[new_expense.get_id()+1] = new_expense
        self.expenses[new_expense.get_id()+2] = new_expense
        self.expenses[new_expense.get_id()+3] = new_expense
        self.expenses[new_expense.get_id()+4] = new_expense
        self.expenses[new_expense.get_id()+5] = new_expense
        self.expenses[new_expense.get_id()+6] = new_expense
        self.expenses[new_expense.get_id()+7] = new_expense
        self.expenses[new_expense.get_id()+8] = new_expense
        self.expenses[new_expense.get_id()+9] = new_expense
        self.expenses[new_expense.get_id()+10] = new_expense
        # TODO: make the expense created be added to the expenses.txt file and output to terminal
    def isempty(self):
        return len(self.expenses) == 0

    def __repr__(self):
        table = Table('ID', 'Amount', 'Category', 'Description', 'Date')
        for exp_id, expense in self.expenses.items():
            table.add_row([exp_id, expense.get_amount(), expense.get_category(), expense.get_description(), expense.date_time])
        return str(table)

    def get_total(self):
        return self.total_val

    def find_expense(self):
        pass
    def delete_expense(self,):
        cprint("Please enter the ID of the expense you would like to delete:", end='')
        delete_id = int(input().strip())
        try:
            del self.expenses[delete_id]
            return True

        except KeyError:
            return False


    def view_category(self):
        cprint("Please enter the category you would like to see:", end='')
        category = input().strip()
        for exp_id, expense in self.expenses.items():
            if expense.get_category() == category:
                lprint(expense)
    def search(self):
        lprint("\tid\n")
        lprint("\tcategory\n")
        lprint("\tdescription\n")
        cprint("Please enter how you would like to view your expense(s):", end='')
        search_type = input().strip()
        if search_type == "id":
            print("Please enter the id of the expense you would like to view:", end='')
        elif search_type == "category":
            pass
        elif search_type == "description":
            pass
        else:
            cprint("Please enter a valid search type.")


    # def find_description(self, description):
        # descriptions = {exp_id: expense.get_description() for exp_id, expense in self.expenses.items()}
        #
        # # Use fuzzywuzzy to find the best matches
        # best_matches = process.extract(description, descriptions, limit=10)  # Adjust limit as needed
        #
        # # Output the best matches
        # for match in best_matches:
        #     exp_id, score = match[0], match[1]
        #     if score > 80:  # Adjust score threshold as needed
        #         expense = self.expenses[exp_id]
        #         print(expense)  # Or do something else with the matching expenses


