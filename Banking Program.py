# Banking Program

def bal(balance) :
    print(f"Your balance is ${balance:.2f}")
    print()

def dep() :
    amount = float(input("Enter an amount to deposit : $"))

    if amount < 0 :
        print("invalid deposit amount")
        return 0
    else :
        return amount

def withdraw(balance) :
    amount = float(input("Enter an amount to withdraw : $"))

    if amount > balance :
        print("Insufficient funds")
        return 0
    elif amount < 0 :
        print("invalid withdraw amount")
        return 0
    else :
        return amount    

balance = 0
running = True

while running :
    print("~~~BANKING PROGRAM~~~")
    print("1. Show Balance ")
    print("2. Deposit ")
    print("3. Withdraw")
    print("4. Exit")
    print()

    choice = int(input("Enter your choice [1/2/3/4] : "))

    if choice == 1 :
        bal(balance)
    elif choice == 2 :
        balance += dep()
    elif choice == 3 :
        balance -= withdraw(balance)
    elif choice == 4 :
        break
    else :
        print("Invalid choice")

print("Thank you, Have a nice day !")

