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
        self.total_categories = 0


    def get_total(self):
        return self.total_val

    def isempty(self):
        return len(self.expenses) == 0

    def add_expense(self):
        amount = category = description = None
        while not (amount and category and description):
            try:
                cprint("Please enter the amount:", end="")
                amount = float(input())
            except ValueError:
                cprint("Please enter a valid amount.")
                continue
            cprint("Please enter the category (ex. food , transportation..):", end="")
            category = input().strip()
            cprint("Please enter the description:", end="")
            description = input().strip()

        self.exp_id += 1
        self.total_val += amount
        self.amount_of_exp += 1
        old_category = False

        for expense in self.expenses.values():
            if expense.get_category() == category:
                old_category = True
                break
        if not old_category:
            self.total_categories += 1



        new_expense = ExpenseRegistry.Expense(self.exp_id, amount, category, description)
        self.expenses[self.exp_id] = new_expense

        self.display_single_expense(self.exp_id)


        # TODO: make the expense created be added to the expenses.txt file and output to terminal

    def __repr__(self):
        table = Table('ID', 'Amount', 'Category', 'Description', 'Date')
        for exp_id, expense in self.expenses.items():
            table.add_row(
                [exp_id, expense.get_amount(), expense.get_category(), expense.get_description(), expense.date_time])
        return str(table)

    def display_single_expense(self, exp_id):
        table = Table('ID', 'Amount', 'Category', 'Description', 'Date')
        table.add_row([self.expenses[exp_id].get_id(), self.expenses[exp_id].get_amount(),
                       self.expenses[exp_id].get_category(), self.expenses[exp_id].get_description(),
                       self.expenses[exp_id].date_time])
        print(table)

    def delete_expense(self, ):
        cprint("Please enter the ID of the expense you would like to delete:", end='')
        delete_id = int(input().strip())
        try:
            del self.expenses[delete_id]
            return True

        except KeyError:
            return False

    def search(self):
        lprint(Table('ID', 'Category', 'Description'))

        cprint("Please enter how you would like to view your expense(s):", end='')
        search_type = input().strip().lower()
        if search_type == "id":
            self.search_by_id()
        elif search_type == "category":
            self.view_category()
        elif search_type == "description":
            pass
        else:
            cprint("Please enter a valid search type.")

    def search_by_id(self, search_id):
        lprint("Please enter the id of the expense you would like to view: ", end='')
        search_id = int(input())
        while True:
            try:
                self.display_single_expense(search_id)
                break
            except KeyError:
                cprint("Please enter a valid id.")
                continue
    def view_category(self):
        cprint("Please enter the category you would like to see:", end='')
        category = None
        while not category:
            category = input().strip()
        while True:
            try:
                table = Table('ID', 'Amount', 'Category', 'Description', 'Date')
                for exp_id, expense in self.expenses.items():
                    table.add_row(
                        [exp_id, expense.get_amount(), expense.get_category(), expense.get_description(),
                         expense.date_time])
                lprint(table)
                break
            except KeyError:
                cprint("Please enter a valid category.")
                continue

    def summarize(self):
        table = Table('Total Expenses Value', 'Amount of Expenses', 'Amount of Categories')
        table.add_row([self.total_val, self.amount_of_exp,self.total_categories])
        lprint(table)

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
