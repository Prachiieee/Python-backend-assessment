from postgres_handler import get_all_customers, insert_transaction, get_customer_transactions

sample_amounts = [149.99, 249.50, 310.00, 99.99, 500.00, 75.75, 88.80, 199.99, 60.60, 349.90]

customers = get_all_customers()

if not customers:
    print("No customers found.")
else:
    print("Customers and their Unique Transactions:\n")

    for idx, customer in enumerate(customers):
        customer_id = customer['id']
        name = customer['name']
        email = customer['email']
        amount = sample_amounts[idx % len(sample_amounts)]  

        print(f"Customer ID: {customer_id}, Name: {name}, Email: {email}")

        insert_transaction(customer_id, amount)
        print(f"Inserted ₹{amount} transaction for {name}")

        transactions = get_customer_transactions(customer_id)
        print(f"Transactions for {name}:")
        for txn in transactions:
            print(f"  → ID: {txn['id']}, Amount: {txn['amount']}, Time: {txn['timestamp']}")
        print("-" * 50)
