users = {}

def register():
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists.")
        return False
    password = input("Enter a password: ")
    users[username] = {
        "password": password,
        "loan": 0,
        "payments": []
    }
    print("Registration successful.")
    return True

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username]["password"] == password:
        print("Login successful.")
        return username
    else:
        print("Invalid username or password.")
        return None

def apply_loan(username):
    amount = float(input("Enter loan amount: "))
    users[username]["loan"] += amount
    print("Loan approved.")

def make_payment(username):
    amount = float(input("Enter payment amount: "))
    if amount <= users[username]["loan"]:
        users[username]["loan"] -= amount
        users[username]["payments"].append(amount)
        print("Payment successful.")
    else:
        print("Payment exceeds loan amount.")

def check_balance(username):
    print("Current balance:", users[username]["loan"])

def view_history(username):
    print("Payment history:", users[username]["payments"])

def main():
    while True:
        choice = input("Do you have an account? (yes/no/exit): ").lower()
        if choice == "yes":
            user = login()
            if user:
                while True:
                    print("\n1. Apply for Loan\n2. Make Payment\n3. Check Balance\n4. View History\n5. Logout")
                    option = input("Choose an option: ")
                    if option == "1":
                        apply_loan(user)
                    elif option == "2":
                        make_payment(user)
                    elif option == "3":
                        check_balance(user)
                    elif option == "4":
                        view_history(user)
                    elif option == "5":
                        break
                    else:
                        print("Invalid option.")
        elif choice == "no":
            register()
        elif choice == "exit":
            break
        else:
            print("Invalid input.")

main()
