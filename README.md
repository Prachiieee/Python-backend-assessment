# 🐍 Python Backend Assessment

This project is a FastAPI-based backend system for managing customer data and transactions. It uses PostgreSQL for storage and includes analytics and reporting features.

---

## Features

-  Manage customer records
-  Insert and retrieve transactions
-  Top spender analytics
-  Download latest transaction reports (CSV)
-  Simple, modular code with reusable database functions

---

## Tech Stack

- **Python 3.10+**
- **FastAPI** for the web API
- **PostgreSQL** as the database
- **SQLAlchemy** for analytics queries
- **Pandas** for report generation

---

## Setup Instructions

1. Clone the repo

bash
git clone https://github.com/Prachiieee/Python-backend-assessment.git
cd Python-backend-assessment

2. Create database
CREATE DATABASE "Assessment";

3. Install dependencies
pip install -r requirements.txt

4.Create tables and seed data
python create_tables.py
python insert_customer.py
python insert_transaction.py

5.Run the FastAPI server
uvicorn main:app --reload
Visit http://localhost:8000/docs to view the interactive Swagger UI.

 
 API Endpoints
 --------------------
GET /customers → List all customers
GET /customers/{id}/transactions → Get latest transaction of a customer
POST /transactions → Insert a new transaction
GET /analytics/top-spenders → Show top 2 spenders
GET /analytics/download-report → Download CSV report of latest transactions

Author
---------------
Prachi Patel
Email: ppatel2520@gmail.com
GitHub: @Prachiieee
