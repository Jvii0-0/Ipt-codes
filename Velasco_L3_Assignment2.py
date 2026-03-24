def deposit(balance):
    try:
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Amount must be positive.")
        else:
            balance += amount
            print("Deposit successful.")
    except:
        print("Invalid input.")
    return balance


def withdraw(balance):
    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Amount must be positive.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print("Withdrawal successful.")
    except:
        print("Invalid input.")
    return balance


def check_balance(balance):
    print("Current balance:", balance)


balance = 10000

while True:
    print("\nMenu")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        balance = deposit(balance)
    elif choice == "2":
        balance = withdraw(balance)
    elif choice == "3":
        check_balance(balance)
    elif choice == "4":
        print("Program ended.")
        break
    else:
        print("Invalid choice.")
