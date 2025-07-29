import psycopg2
import psycopg2.extras
from datetime import datetime

sample_amounts = [149.99, 249.50, 310.00, 99.99, 500.00, 75.75, 88.80, 199.99, 60.60, 349.90]

# Database connection
conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="Prachi@25",
    dbname="Assessment"
)

cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# Fetch all customers
cursor.execute("SELECT id, name FROM customers")
customers = cursor.fetchall()

if not customers:
    print("No customers found in the database.")
else:
    print("Inserting one unique transaction per customer:\n")

    for i, customer in enumerate(customers):
        customer_id = customer["id"]
        name = customer["name"]
        amount = sample_amounts[i % len(sample_amounts)]  

        # Insert transaction
        cursor.execute(
            "INSERT INTO transactions (customer_id, amount) VALUES (%s, %s)",
            (customer_id, amount)
        )
        print(f"Inserted ₹{amount} for Customer ID {customer_id} ({name})")

conn.commit()
cursor.close()
conn.close()

