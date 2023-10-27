import datetime
import csv
from helper_function.command_handler import cprint, lprint
from utilities import TUI
from utilities.Table import Table
from fuzzywuzzy import fuzz


class ExpenseRegistry:
    class Expense:

        def __init__(self, exp_id, amount, category, description):
            self.exp_id = exp_id
            self.date_time = datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')

            self.amount = amount
            self.category = category
            self.description = description

        def __repr__(self):
            table = Table('ID', 'Amount', 'Category', 'Description', 'Date')
            table.add_row([self.exp_id, self.amount, self.category, self.description, self.date_time])
            return str(table)

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

        self.load("expenses.csv")

    def isempty(self):
        return len(self.expenses) == 0
    def load(self, file):
        try:
            with open(file, 'r') as f:
                reader = csv.reader(f)
                # Skip the headers
                next(reader)
                # Read each expense
                for row in reader:
                    self.exp_id = int(row[0])
                    self.total_val += float(row[1])
                    self.amount_of_exp += 1
                    old_category = False

                    for expense in self.expenses.values():
                        if expense.get_category() == row[2]:
                            old_category = True
                            break
                    if not old_category:
                        self.total_categories += 1

                    new_expense = ExpenseRegistry.Expense(self.exp_id, float(row[1]), row[2], row[3])
                    self.expenses[self.exp_id] = new_expense
            return True
        except IOError:
            cprint("Error: Unable to load from file.")
            return False

    def get_total(self):
        return self.total_val


    def add_expense(self):
        amount = category = description = None
        while not (amount and category and description):
            try:
                cprint("Please enter the amount or type 'cancel' to exit:", end="")
                amount_input = input().strip()
                if amount_input.lower() == "cancel":
                    return False
                amount = float(amount_input)
            except ValueError:
                cprint("Please enter a valid amount.")
                continue

            # Ensure category is 80 characters or less
            while True:
                cprint("Please enter the category (ex. food , transportation..) or type 'cancel' to exit:", end="")
                category = input().strip()
                if category.lower() == "cancel":
                    return False
                if len(category) <= 80:
                    break
                else:
                    cprint("Please enter a category with 80 characters or less.")

            # Ensure description is 80 characters or less
            while True:
                cprint("Please enter the description or type 'cancel' to exit:", end="")
                description = input().strip()
                if description.lower() == "cancel":
                    return False
                if len(description) <= 80:
                    break
                else:
                    cprint("Please enter a description with 80 characters or less.")

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

        new_expense = ExpenseRegistry.Expense(self.exp_id, amount, category.capitalize(), description)
        self.expenses[self.exp_id] = new_expense

        lprint(new_expense)

        self.save("expenses.csv")

    def __repr__(self):
        table = Table('ID', 'Amount', 'Category', 'Description', 'Date')
        for exp_id, expense in self.expenses.items():
            table.add_row(
                [exp_id, expense.get_amount(), expense.get_category(), expense.get_description(), expense.date_time])
        return str(table)

    def delete_expense(self):
        if self.isempty():
            cprint("Sorry, there are no expenses that have been logged yet.")
            return False
        query = None
        while not query or query != 'q':
            cprint("Please enter (id) of the expense you would like to delete, or (q)uit:", end='')
            delete_id = int(input())
            try:
                del self.expenses[delete_id]
                return True
            except KeyError:
                cprint("Expense of that id not found!.")
                continue
        return False

    def search(self):
        lprint(Table('(id)', '(c)ategory', '(d)escription'))
        search_type = None
        while search_type != 'q':
            cprint("Enter type of the search (id), (c)ategory, (d)escription or (q)uit:", end='')
            search_type = input().strip().lower()
            if search_type == "id":
                self.search_by_id()
            elif search_type == "c":
                self.view_category()
            elif search_type == "d":
                self.find_description()
            elif search_type != "q":
                cprint("Please enter a valid search type.")

    def search_by_id(self):
        lprint("Please enter the id of the expense you would like to view: ", end='')
        search_id = int(input())
        while True:
            try:
                lprint(self.expenses[search_id])
                return self.expenses[search_id]
            except KeyError:
                cprint("Please enter a valid id.")
                continue
        return None

    def view_category(self):
        cprint("Please enter the category you would like to view:", end='')
        category = None
        while not category:
            category = input().strip()
        while True:
            try:
                table = Table('ID', 'Amount', 'Category', 'Description', 'Date')
                for exp_id, expense in self.expenses.items():
                    if expense.get_category() == category:
                        table.add_row(
                            [exp_id, expense.get_amount(), expense.get_category(), expense.get_description(),
                             expense.date_time])
                lprint(table)
                break
            except KeyError:
                cprint("Please enter a valid category.")
                continue

    def find_description(self, threshold=80):
        query = None
        while query != 'q':
            cprint("Please enter the description you would like to find or 'q' to quit:", end='', speed=5)

            table = Table('ID', 'Amount', 'Category', 'Description', 'Date')

            query = None
            while not query:
                query = input().strip()
            if query == 'q':
                break
            matching_expenses = []

            for expense in self.expenses.values():
                ratio = fuzz.ratio(expense.get_description().lower(), query.lower())
                if ratio >= threshold:
                    matching_expenses.append(expense)

            for expense in matching_expenses:
                table.add_row(
                    [expense.get_id(), expense.get_amount(), expense.get_category(), expense.get_description(),
                     expense.date_time])
            TUI.create_view(table)

    def summarize(self):
        if self.isempty():
            cprint("Sorry, there are no expenses that have been logged yet.")
            return False
        else:
            table = Table('Total Expenses Value', 'Amount of Expenses', 'Amount of Categories')
            table.add_row([self.total_val, self.amount_of_exp, self.total_categories])
            TUI.create_view(table)
            return True

    def save(self, file):
        try:
            with open(file, 'w', newline='') as f:
                writer = csv.writer(f)
                # Write the headers
                writer.writerow(['ID', 'Amount', 'Category', 'Description', 'Date'])
                # Write each expense
                for exp_id, expense in self.expenses.items():
                    writer.writerow([exp_id, expense.get_amount(), expense.get_category(),
                                     expense.get_description(), expense.date_time])
            return True
        except IOError:
            cprint("Error: Unable to save to file.")
            return False
