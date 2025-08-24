# banking_app/bankcore.py

# Branch ID fixed
branch_id = 2057  

# Storage for users {customer_id: {"name": str, "password": str}}
users_info = {}  

# Counter to generate unique user numbers
user_number = 0  


def create_account(name, password):
    """
    Create a new customer account.
    Format: customer_id = <branch_id>-<user_number>
    """
    global user_number
    user_number += 1
    customer_id = f"{branch_id}-{user_number}"
    users_info[customer_id] = {"name": name, "password": password}

    print("\nAccount created successfully!")
    print(f"Your Customer ID: {customer_id}")
    return customer_id


def login(customer_id, password):
    """
    Validate login credentials.
    """
    if customer_id in users_info and users_info[customer_id]["password"] == password:
        print(f"\nLogin successful! Welcome, {users_info[customer_id]['name']}.")
        return True
    else:
        print("\nInvalid login. Please try again.")
        return False