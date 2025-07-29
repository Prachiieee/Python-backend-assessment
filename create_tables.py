import psycopg2

conn = psycopg2.connect(
    host="localhost",
    user="postgres",           
    password="Prachi@25",  
    dbname="Assessment"       
)

cursor = conn.cursor()

# customers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
)
""")

# transactions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    amount NUMERIC(10, 2) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
)
""")

conn.commit()
cursor.close()
conn.close()

