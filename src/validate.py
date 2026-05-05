import pandas as pd

VALID_SEGMENTS = {"New", "Returning", "High Value"}
VALID_CHANNELS = {"Web", "Mobile", "Store", "Partner"}
VALID_STATUSES = {"Completed", "Returned", "Cancelled"}


def validate_customers(customers: pd.DataFrame) -> dict:
    """
    Check customer data quality issues.
    """
    report = {}

    report["total_rows"] = int(len(customers))
    report["missing_customer_id"] = int(customers["customer_id"].isna().sum())
    report["missing_email"] = int(customers["email"].isna().sum())
    report["duplicate_customer_id"] = int(customers["customer_id"].duplicated().sum())

    signup_dates = pd.to_datetime(customers["signup_date"], errors="coerce")
    report["invalid_signup_date"] = int(signup_dates.isna().sum())

    invalid_segments = ~customers["segment"].isin(VALID_SEGMENTS)
    report["invalid_segment"] = int(invalid_segments.sum())

    return report


def validate_transactions(transactions: pd.DataFrame, valid_customer_ids: set) -> dict:
    """
    Check transaction data quality issues.
    """
    report = {}

    report["total_rows"] = int(len(transactions))
    report["missing_transaction_id"] = int(transactions["transaction_id"].isna().sum())
    report["duplicate_transaction_id"] = int(transactions["transaction_id"].duplicated().sum())

    transaction_dates = pd.to_datetime(transactions["transaction_date"], errors="coerce")
    report["invalid_transaction_date"] = int(transaction_dates.isna().sum())

    invalid_channels = ~transactions["channel"].isin(VALID_CHANNELS)
    report["invalid_channel"] = int(invalid_channels.sum())

    invalid_statuses = ~transactions["status"].isin(VALID_STATUSES)
    report["invalid_status"] = int(invalid_statuses.sum())

    negative_amounts = transactions["amount"] < 0
    report["negative_amount"] = int(negative_amounts.sum())

    unknown_customers = ~transactions["customer_id"].isin(valid_customer_ids)
    report["unknown_customer_id"] = int(unknown_customers.sum())

    return report