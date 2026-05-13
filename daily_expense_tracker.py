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

    elif option == "2":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for i, valor in enumerate(expenses, 1):
                print(f"{i}.{valor}")
        input("\nPress Enter to return to menu...")

    elif option == "3":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            total = sum(expenses)
            average = total/len(expenses)
            print(f"Total expense: {total}")
            print(f"Average expense: {average}")
        input("\nPress Enter to return to menu...")

    elif option == "4":
        expenses.clear()
        print("All expenses cleared.")
        input("\nPress Enter to return to menu...")

    else:
        print("Invalid choice. Please try again.")
