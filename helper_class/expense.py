import datetime

from helper_function.command_handler import cprint
from utilities.Table import Table

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
            cprint("Please enter the amount:", end="")
            amount = input().strip()
            cprint("Please enter the category (ex. food , transportation..):", end="")
            category = input().strip()
            cprint("Please enter the description:", end="")
            description = input().strip()
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

    def delete_expense(self):
        id = None

        while (not id):
            id = input("Please enter the amount: ")
            try:
                id = int(id)
            except ValueError:
                print("Invalid input. Please try again.")
                id = None

        for category, expenses in self.expenses.items():
            print(category)
            # for expense in expenses:
            #     if expense.get_id() == id:
            #         self.total_val -= expense.get_amount()
            #         expenses.remove(expense)
            #         print(f"Expense {id} has been deleted successfully!")
            #         return

    def view_category(self):
        pass

    def find_description(self, description):
        pass

    def find_expense(self, id):
        pass
