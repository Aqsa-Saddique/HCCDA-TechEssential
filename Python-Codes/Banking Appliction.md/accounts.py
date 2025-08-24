# banking_app/accounts.py

balance_record = {}   # customer_id -> balance

def check_balance(customer_id):
    return balance_record.get(customer_id, 0)

def deposit(customer_id, amount):
    if customer_id not in balance_record:
        balance_record[customer_id] = 0
    balance_record[customer_id] += amount
    print("\n", amount, "deposited successfully.")
    print("New Balance:", balance_record[customer_id])
    return balance_record[customer_id]

def withdraw(customer_id, amount):
    if customer_id not in balance_record:
        balance_record[customer_id] = 0
    if balance_record[customer_id] >= amount:
        balance_record[customer_id] -= amount
        print("\n", amount, "withdrawn successfully.")
        print("New Balance:", balance_record[customer_id])
    else:
        print("\nInsufficient balance.")
    return balance_record[customer_id]