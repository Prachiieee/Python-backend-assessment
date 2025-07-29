import psycopg2
import psycopg2.extras

def get_connection():
    return psycopg2.connect(
        host="localhost",
        user="postgres",            
        password="Prachi@25",       
        dbname="Assessment"         
    )

def get_all_customers():
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [dict(row) for row in rows]


def get_customer_transactions(customer_id):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("""
        SELECT *
        FROM transactions
        WHERE customer_id = %s
        ORDER BY timestamp DESC
        LIMIT 1
    """, (customer_id,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [dict(row) for row in rows]

def insert_transaction(customer_id, amount):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 1 FROM transactions
        WHERE customer_id = %s AND amount = %s
        LIMIT 1
    """, (customer_id, amount))

    if cursor.fetchone():
        print(f"Transaction already exists for customer {customer_id} with amount ₹{amount}. Skipping insert.")
    else:
        cursor.execute("""
            INSERT INTO transactions (customer_id, amount)
            VALUES (%s, %s)
        """, (customer_id, amount))
        conn.commit()

    cursor.close()
    conn.close()
