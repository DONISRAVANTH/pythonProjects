class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your balance is: ₹{self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. Your new balance is: ₹{self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal successful. Your new balance is: ₹{self.balance}")
        else:
            print("Insufficient funds")

    def save_data(self):
        with open("atm_data.txt", "w") as file:
            file.write(str(self.balance) + '\n')

def load_data():
    try:
        with open("atm_data.txt", "r") as file:
            lines = file.readlines()
            balance = float(lines[0].strip())
            return balance
    except FileNotFoundError:
        return 0

def main():
    balance = load_data()
    atm = ATM(balance)

    username = 'Donisravanth'
    password = 'sravanth'

    user_name = input("Enter your username : ")
    user_pass = input("Enter your password : ")

    if username == user_name and password == user_pass:
        while True:
            print("\nWelcome to the ATM!")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Please select an option (1, 2, 3, 4, or 5): ")

            if choice == "1":
                atm.check_balance()
            elif choice == "2":
                try:
                    amount = float(input("Enter deposit amount: ₹"))
                    atm.deposit(amount)
                    atm.save_data()
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")
            elif choice == "3":
                try:
                    amount = float(input("Enter withdrawal amount: ₹"))
                    atm.withdraw(amount)
                    atm.save_data()
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")
            elif choice == "4":
                atm.save_data()
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
    else:
        print("Incorrect Login details")

if __name__ == "__main__":
    main()