# Expense Tracker Application

## Introduction
Welcome to the Expense Tracker Application! This intuitive software allows you to manage and track all your expenses, providing a clear overview of your spending patterns. By leveraging the power of fuzzy searching, you can easily find specific expenses or categories. This README provides a comprehensive guide on how to set up, run, and utilize the application.

## Prerequisites

### Dependencies
Before running the application, ensure you have the following libraries installed:
- `datetime`: For managing and formatting dates.
- `csv`: For reading and writing expenses to a CSV file.
- `fuzzywuzzy`: For fuzzy searching through descriptions and categories.
  
You can install `fuzzywuzzy` using pip:

```bash
pip install fuzzywuzzy
```

Note: Ensure you have the other internal modules and their dependencies installed as well.

## Setup

1. Clone or download the Expense Tracker repository to your local machine:

```bash
git clone https://github.com/gsiri-code/Expense-Tracker
```
3. Navigate to the root directory of the project using your terminal or command prompt.
4. Install the required libraries (if you haven't done so already).

## How to Use

1. **Start the Application**: 
   - Run main.py script.
   ```bash
   python3 main.py
   ```

2. **Command Options**: 
   - Upon starting the application, you'll be presented with the following command options:
     - `(l)og`: Log a new expense.
     - `(v)iew`: View all logged expenses.
     - `(d)elete`: Delete an expense using its ID.
     - `(s)ummarize`: Get a summary of your expenses.
     - `(f)ind`: Search for a specific expense.
     - `(q)uit`: Exit the application and save expenses to `expenses.csv`.

3. **Logging an Expense**:
   - Choose the `(l)og` command.
   - Follow the prompts to input the expense amount, category, and description.
   - Note: Ensure the category and description are 80 characters or less.

4. **Viewing Expenses**:
   - Choose the `(v)iew` command to see all your logged expenses in a tabulated format.

5. **Deleting an Expense**:
   - Choose the `(d)elete` command.
   - Input the ID of the expense you wish to delete.

6. **Searching for an Expense**:
   - Choose the `(f)ind` command.
   - You can search by ID, category, or description.
   - For category and description, the app uses fuzzy searching, so you don't need an exact match.

7. **Summarizing Expenses**:
   - Choose the `(s)ummarize` command to get an overview of your total expenses, the number of expenses, and the number of unique categories.

8. **Exiting the Application**:
   - Choose the `(q)uit` command.
   - Your expenses will automatically be saved to `expenses.csv`.

