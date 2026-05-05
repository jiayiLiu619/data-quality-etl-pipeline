from pathlib import Path
import sqlite3
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATABASE_DIR = ROOT / "database"
DATABASE_PATH = DATABASE_DIR / "customer_transactions.db"


def load_to_sqlite(customers: pd.DataFrame, transactions: pd.DataFrame) -> None:
    """
    Load cleaned customer and transaction data into a SQLite database.
    """
    DATABASE_DIR.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DATABASE_PATH) as conn:
        customers.to_sql("customers", conn, if_exists="replace", index=False)
        transactions.to_sql("transactions", conn, if_exists="replace", index=False)

    print(f"Data loaded successfully into {DATABASE_PATH}")