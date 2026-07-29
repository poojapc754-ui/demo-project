import sys

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew ${amount:.2f}")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            print("Invalid withdrawal amount.")

    def display_balance(self):
        print(f"\nAccount Holder: {self.holder}")
        print(f"Current Balance: ${self.balance:.2f}")

def main():
    print("--- Welcome to Apex Digital Bank ---")
    name = input("Enter your name to open an account: ")
    user_account = BankAccount(name)

    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == '1':
            user_account.display_balance()
        elif choice == '2':
            amt = float(input("Enter amount to deposit: "))
            user_account.deposit(amt)
        elif choice == '3':
            amt = float(input("Enter amount to withdraw: "))
            user_account.withdraw(amt)
        elif choice == '4':
            print("Thank you for banking with us!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()