from expense import Expense
from datetime import datetime

class ExpenseManager:
    
    def __init__(self):
        self.expenses =[]
        self.next_id = 1

    def id_generator(self):
        current_id = self.next_id
        self.next_id += 1
        return current_id

    def get_expense_details(self):
        print("Enter expense details:")
        expense_name = input("Expense Name: ")
        try:
            cost = float(input("Cost: "))
            if cost <= 0:
                print("Cost must be a positive number.")
                return
        except ValueError:
            print("Invalid cost format. Please enter a valid number.")
            return 
        category = input("Category: ")
        try:
            date = input("Date : ")
            date = datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return 
        expense_id = self.id_generator()
        expense = Expense(expense_name, cost, category, date, expense_id)
        return expense

    def add_expense(self):
        expense = self.get_expense_details()
        if expense is None:
            print("Expense details are not valid. Please try again.")
        else:
            self.expenses.append(expense)
            print("Expense added successfully.")

    def total_expenses(self):
        total = 0
        for expense in self.expenses:
            total += expense.cost
        return total
       
    def month_total(self):
        month = datetime.now().month
        year = datetime.now().year
        month_total = 0
        for expense in self.expenses:
            if expense.date.month == month and expense.date.year == year:
                month_total += expense.cost
        return month_total

    def highest_expense(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        
        highest = max(self.expenses, key=lambda x: x.cost)
        return highest

    def lowest_expense(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        lowest = min(self.expenses, key =lambda x: x.cost)
        return lowest

    def average_expense(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        total = self.total_expenses()
        average = total / len(self.expenses)
        return average

    def get_category_total(self):
        category = {}
        
        for expense in self.expenses:
            if expense.category in category:
                category[expense.category] += expense.cost
            else:
                category[expense.category]= expense.cost
        return category  

    
    def category_wise_expense(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        
        category_expenses = self.get_category_total()
        for category, total in category_expenses.items():
            print(f"{category}: {total}")  

    def most_expensive_category(self):
        if not self.expenses:
            print("No expenses recorded.")
            return

        category_expenses = self.get_category_total()

        most_expensive_category = max(category_expenses, key=category_expenses.get)
        return most_expensive_category, category_expenses[most_expensive_category]

    def summary(self):
        print("-" * 20)
        print("Expense Summary")
        print("-" * 20)
        print(f"Total Expenses: {self.total_expenses()}")
        print("-" * 20)
        print(f"Monthly Total: {self.month_total()}")
        print("-" * 20)
        print(f"Average Expense: {self.average_expense()}")
        print("-" * 20)
        if not self.expenses:
            print("No expenses recorded.")
            return
        highest = self.highest_expense()
        print(f"Highest Expense: {highest.expense_name} - {highest.cost} on {highest.date}")
        print("-" * 20)
        lowest = self.lowest_expense()
        print(f"Lowest Expense: {lowest.expense_name} - {lowest.cost} on {lowest.date}")
        print("-" * 20)
        print("Category-wise Expenses:")
        self.category_wise_expense()
        print("-" * 20)
        result = self.most_expensive_category()
        print(f"Most Expensive Category: {result[0]} - {result[1]}")

    def menu(self):
        while True:
            print("\nExpense Manager Menu:")
            print("1. Add Expense")
            print("2. View Summary")
            print("3. Exit")
            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.summary()
            elif choice == '3':
                print("Exiting Expense Manager.")
                break
            else:
                print("Invalid choice. Please try again.")

ExpenseManager().menu()