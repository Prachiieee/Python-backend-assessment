import pandas as pd
import psycopg2
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from postgres_handler import get_all_customers, get_customer_transactions, insert_transaction
from fastapi.responses import StreamingResponse
import io
from sqlalchemy import create_engine
import traceback

app = FastAPI()

DATABASE_URL = "postgresql://postgres:Prachi%4025@localhost:5432/Assessment"

engine = create_engine(DATABASE_URL)

class TransactionRequest(BaseModel):
    customer_id: int
    amount: float

@app.get("/customers")
def read_customers():
    return get_all_customers()


@app.get("/customers/{customer_id}/transactions")
def read_customer_transactions(customer_id: int):
    customers = get_all_customers()
    if not any(c["id"] == customer_id for c in customers):
        raise HTTPException(status_code=404, detail="Customer ID not found")
    
    transactions = get_customer_transactions(customer_id)
    return transactions


@app.post("/transactions")
def create_transaction(data: TransactionRequest):
    try:
        insert_transaction(data.customer_id, data.amount)
        return {"message": "Transaction inserted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/analytics/top-spenders")
def top_spenders():
    try:
        df = pd.read_sql("""
            SELECT c.id, c.name, SUM(t.amount) AS total_spent
            FROM customers c
            JOIN transactions t ON c.id = t.customer_id
            GROUP BY c.id, c.name
            ORDER BY total_spent DESC
            LIMIT 2
        """, engine)

        return df.to_dict(orient="records")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/analytics/download-report")
def download_report():
    try:
        df = pd.read_sql("""
            SELECT DISTINCT ON (c.id) 
                c.id AS customer_id, 
                c.name, 
                c.email, 
                t.amount, 
                t.timestamp
            FROM customers c
            JOIN transactions t ON c.id = t.customer_id
            ORDER BY c.id, t.timestamp DESC
        """, engine)

        stream = io.StringIO()
        df.to_csv(stream, index=False)
        stream.seek(0)

        return StreamingResponse(stream, media_type="text/csv", headers={
            "Content-Disposition": "attachment; filename=latest_transaction_report.csv"
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
