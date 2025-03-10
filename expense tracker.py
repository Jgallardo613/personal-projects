class Expense:
    def  __init_(self,date,description,amount):
        self.date = date
        self.description = description
        self.amount = amount

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expenses):
        self.expenses.append(expenses)

    def remove_expense(self, index):
            if 0 <= index < len(self,expense):
                del self.expenses[index]
                print("expense removed sucesfully")
            else:
                print("invalid expense index.")

    def view_expenses (self):
        if len(self.expenses) == 0:
            print("No expenses found")
        else:
            print("Expense List:")
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}. Date:{Expense.date}, Description:{expense.description},amount: ${expense.amount:.2f}")

    def total_expense(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: ${total:.2f}")

def main():
    tracker=ExpenseTracker()   
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2.Remove Expense")
        print("3.View Expenses")
        print("4.Total Expenses")
        print("5. Exit")
        choice = input("Enter your choice (1-5):")
        if choice == "1":
            date = input("enter the date (YYYY-MM-DD):")
            description =input("Enter the description: ")
            amount = float(input("Enter the amount:"))
            expense = expense(date,description,amount)
            tracker.add_expense(expense)
            print("expense added succesfully")
        elif choice == "2":
            index = int(input("enter the expense index to remove: ")) -1
            tracker.remove_expense(index)
        elif choice == "3":
            tracker.view_expenses()
        elif choice == "4":
            tracker.total_expenses()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("invalid choice. please try again")

main()
 