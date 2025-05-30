class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.loan = 0
        self.payments = []

    def apply_loan(self, amount):
        self.loan += amount
        print("Loan approved.")

    def make_payment(self, amount):
        if amount <= self.loan:
            self.loan -= amount
            self.payments.append(amount)
            print("Payment successful.")
        else:
            print("Payment exceeds loan amount.")

    def check_balance(self):
        print("Current balance:", self.loan)

    def view_payment_history(self):
        print("Payment history:", self.payments)


class LoanSystem:
    def __init__(self):
        self.users = {}

    def register(self):
        username = input("Enter a new username: ")
        if username in self.users:
            print("Username already exists.")
            return
        password = input("Enter a password: ")
        self.users[username] = User(username, password)
        print("Registration successful.")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = self.users.get(username)
        if user and user.password == password:
            print("Login successful.")
            self.user_menu(user)
        else:
            print("Invalid username or password.")

    def user_menu(self, user):
        while True:
            print("\n1. Apply for Loan\n2. Make Payment\n3. Check Balance\n4. View Payment History\n5. Logout")
            choice = input("Choose an option: ")
            if choice == "1":
                amount = float(input("Enter loan amount: "))
                user.apply_loan(amount)
            elif choice == "2":
                amount = float(input("Enter payment amount: "))
                user.make_payment(amount)
            elif choice == "3":
                user.check_balance()
            elif choice == "4":
                user.view_payment_history()
            elif choice == "5":
                break
            else:
                print("Invalid option.")


def main():
    system = LoanSystem()
    while True:
        choice = input("Do you have an account? (yes/no/exit): ").lower()
        if choice == "yes":
            system.login()
        elif choice == "no":
            system.register()
        elif choice == "exit":
            break
        else:
            print("Invalid input.")

main()
