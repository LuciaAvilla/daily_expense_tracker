print("Welcome to the Daily Expense Tracker!")

menu = """
Menu:
1. Add a new expense
2. View all expenses
3. Calculate total and average expense
4. Clear all expenses
5. Exit
"""

expenses = []

while True:
    print(menu)
    option = input("Choose an option: ")

    if option == "5":
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break

    elif option == "1":
        value = float(input("Enter the expense amount: "))
        expenses.append(value)
        print("Expense added successfully!")
