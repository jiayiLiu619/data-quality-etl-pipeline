from pathlib import Path
import pandas as pd

# Find the project root folder.
# __file__ means this file: src/extract.py
# parents[1] means go up one level to the project root.
ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"


def extract_customers() -> pd.DataFrame:
    """
    Read raw customer data from CSV.
    """
    customers_path = RAW_DIR / "raw_customers.csv"
    return pd.read_csv(customers_path)


def extract_transactions() -> pd.DataFrame:
    """
    Read raw transaction data from CSV.
    """
    transactions_path = RAW_DIR / "raw_transactions.csv"
    return pd.read_csv(transactions_path)


if __name__ == "__main__":
    customers = extract_customers()
    transactions = extract_transactions()

    print("Customers data loaded successfully.")
    print(customers.head())
    print("Customers shape:", customers.shape)

    print("\nTransactions data loaded successfully.")
    print(transactions.head())
    print("Transactions shape:", transactions.shape)