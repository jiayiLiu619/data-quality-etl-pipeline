import pandas as pd
from validate import VALID_SEGMENTS, VALID_CHANNELS, VALID_STATUSES


def clean_customers(customers: pd.DataFrame) -> pd.DataFrame:
    """
    Clean customer records based on business rules.
    """
    df = customers.copy()

    # Standardize text fields.
    text_columns = ["customer_id", "customer_name", "email", "segment", "province"]
    for col in text_columns:
        df[col] = df[col].fillna("").astype(str).str.strip()

    # Convert signup_date to date format.
    df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce")

    # Remove records with missing customer_id or invalid signup_date.
    df = df[df["customer_id"] != ""]
    df = df.dropna(subset=["signup_date"])

    # Keep only valid customer segments.
    df = df[df["segment"].isin(VALID_SEGMENTS)]

    # Remove duplicate customer IDs and keep the latest valid record.
    df = df.sort_values("signup_date")
    df = df.drop_duplicates(subset=["customer_id"], keep="last")

    # Convert date back to readable string format.
    df["signup_date"] = df["signup_date"].dt.strftime("%Y-%m-%d")

    return df.reset_index(drop=True)


def clean_transactions(transactions: pd.DataFrame, customers_cleaned: pd.DataFrame) -> pd.DataFrame:
    """
    Clean transaction records based on business rules.
    """
    df = transactions.copy()

    # Standardize text fields.
    text_columns = ["transaction_id", "customer_id", "transaction_date", "channel", "status"]
    for col in text_columns:
        df[col] = df[col].fillna("").astype(str).str.strip()

    # Convert dates and numeric fields.
    df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df["cost"] = pd.to_numeric(df["cost"], errors="coerce")

    # Remove records with missing or invalid required fields.
    df = df[df["transaction_id"] != ""]
    df = df[df["customer_id"] != ""]
    df = df.dropna(subset=["transaction_date", "amount", "cost"])

    # Apply business validation rules.
    df = df[df["amount"] >= 0]
    df = df[df["cost"] >= 0]
    df = df[df["channel"].isin(VALID_CHANNELS)]
    df = df[df["status"].isin(VALID_STATUSES)]

    # Keep only transactions linked to valid cleaned customers.
    valid_customer_ids = set(customers_cleaned["customer_id"])
    df = df[df["customer_id"].isin(valid_customer_ids)]

    # Remove duplicate transaction IDs and keep the latest valid record.
    df = df.sort_values("transaction_date")
    df = df.drop_duplicates(subset=["transaction_id"], keep="last")

    # Add derived reporting field.
    df["gross_profit"] = df["amount"] - df["cost"]

    # Convert date back to readable string format.
    df["transaction_date"] = df["transaction_date"].dt.strftime("%Y-%m-%d")

    return df.reset_index(drop=True)