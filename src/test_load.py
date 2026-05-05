import sqlite3
from pathlib import Path

from extract import extract_customers, extract_transactions
from transform import clean_customers, clean_transactions
from load import load_to_sqlite


ROOT = Path(__file__).resolve().parents[1]
DATABASE_PATH = ROOT / "database" / "customer_transactions.db"


customers_raw = extract_customers()
transactions_raw = extract_transactions()

customers_cleaned = clean_customers(customers_raw)
transactions_cleaned = clean_transactions(transactions_raw, customers_cleaned)

load_to_sqlite(customers_cleaned, transactions_cleaned)

with sqlite3.connect(DATABASE_PATH) as conn:
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM customers")
    customer_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM transactions")
    transaction_count = cursor.fetchone()[0]

print("Customers loaded:", customer_count)
print("Transactions loaded:", transaction_count)