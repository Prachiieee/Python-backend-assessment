import psycopg2

conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="Prachi@25",
    dbname="Assessment"
)

cursor = conn.cursor()

customers = [
    ("Prachi Patel", "ppatel2520@gmail.com"),
    ("Prince Patel", "prince149@gmail.com"),
    ("Chesta Patel", "chesta118@gmail.com"),
    ("Kashish Verma", "kahishverma301@gmail.com"),
    ("Shyam Aghara", "shyamaghara23@gmail.com"),
    ("Kirit Patel", "kirit252@gmail.com"),
    ("Mitesh Patel", "mitesh252@gmail.com"),
    ("Varsha Patel", "varsha45@gmail.com"),
    ("Asmita Patel", "asmita149@gmail.com"),
    ("Pragnesh Patel", "pragnesh563@gmail.com")
]

cursor.executemany(
    "INSERT INTO customers (name, email) VALUES (%s, %s) ON CONFLICT (email) DO NOTHING",
    customers
)

conn.commit()
cursor.close()
conn.close()

