print("Welcome to the Daily Expense Tracker!")

print("\nMenu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

expenses = []

while True:
    choice = (input())
    if choice == "1":
        #add expense
        amount = float(input())
        expenses.append(amount)
        print("Expense added successfully!")
    elif choice == "2":
        if expenses == []:
            print("No expenses recorded yet.")
        else:
            print ("Your expenses:")
            a = 0
            while a < len(expenses):
                for i in range(1, len(expenses)+1):
                    print(f"{i}. {expenses[a]}")
                    a += 1
    elif choice == "3":
        if expenses == []:
            print("No expenses recorded yet.")
        else:
            print(f"Total expense: {float(sum(expenses))}")
            print(f"Average expense: {float(sum(expenses)/len(expenses))}")
    elif choice == "4":
        expenses.clear()
        print("All expenses cleared.")
    elif choice == "5":
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")





    
