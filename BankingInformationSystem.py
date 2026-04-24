# Banking Information System Project

accounts = {}

def create_account():
    acc_no = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Balance: "))
    accounts[acc_no] = {
        "name": name,
        "balance": balance
    }
    print("Account created successfully!\n")


def deposit_money():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        amount = float(input("Enter deposit amount: "))
        accounts[acc_no]["balance"] += amount
        print("Money deposited successfully!\n")
    else:
        print("Account not found!\n")


def withdraw_money():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        amount = float(input("Enter withdrawal amount: "))
        if accounts[acc_no]["balance"] >= amount:
            accounts[acc_no]["balance"] -= amount
            print("Withdrawal successful!\n")
        else:
            print("Insufficient balance!\n")
    else:
        print("Account not found!\n")


def check_balance():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        print("Account Holder:", accounts[acc_no]["name"])
        print("Current Balance:", accounts[acc_no]["balance"])
    else:
        print("Account not found!\n")


def main():
    while True:
        print("\n--- Banking Information System ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            print("Thank you for using Banking Information System!")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
