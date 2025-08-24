# banking_app/main.py

from banking_app import bankcore, accounts

def main():
    print("\nWelcome to ABC Bank")

    while True:
        print("\nMain Menu:")
        print("1. Create an Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            password = input("Set a password: ")
            bankcore.create_account(name, password)

        elif choice == "2":
            customer_id = input("Enter Customer ID: ")
            password = input("Enter Password: ")

            if bankcore.login(customer_id, password):
                while True:
                    print("\n--- Account Menu ---")
                    print("1. Deposit Money")
                    print("2. Withdraw Money")
                    print("3. Check Balance")
                    print("4. Logout")

                    option = input("Choose an option: ")

                    if option == "1":
                        amount = float(input("Enter amount to deposit: "))
                        accounts.deposit(customer_id, amount)

                    elif option == "2":
                        amount = float(input("Enter amount to withdraw: "))
                        accounts.withdraw(customer_id, amount)

                    elif option == "3":
                        balance = accounts.check_balance(customer_id)
                        print("\nYour current balance:", balance)

                    elif option == "4":
                        print("\nLogged out successfully.")
                        break

                    else:
                        print("\nInvalid option, try again.")

        elif choice == "3":
            print("\nThank you for banking with us. Goodbye!")
            break

        else:
            print("\nInvalid choice, please try again.")

if __name__ == "__main__":
    main()
