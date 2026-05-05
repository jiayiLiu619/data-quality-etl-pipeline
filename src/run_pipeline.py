from pathlib import Path
import json

from extract import extract_customers, extract_transactions
from validate import validate_customers, validate_transactions
from transform import clean_customers, clean_transactions
from load import load_to_sqlite


ROOT = Path(__file__).resolve().parents[1]
CLEANED_DIR = ROOT / "data" / "cleaned"
REPORTS_DIR = ROOT / "data" / "reports"


def main() -> None:
    """
    Run the full ETL pipeline:
    1. Extract raw CSV data
    2. Validate raw data quality
    3. Clean and transform data
    4. Save cleaned CSV files
    5. Load cleaned data into SQLite
    6. Save a data quality report
    """
    CLEANED_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    print("Step 1: Extracting raw data...")
    customers_raw = extract_customers()
    transactions_raw = extract_transactions()

    print("Step 2: Validating raw data quality...")
    valid_customer_ids = set(customers_raw["customer_id"])

    quality_report = {
        "raw_customers": validate_customers(customers_raw),
        "raw_transactions": validate_transactions(transactions_raw, valid_customer_ids),
    }

    print("Step 3: Cleaning and transforming data...")
    customers_cleaned = clean_customers(customers_raw)
    transactions_cleaned = clean_transactions(transactions_raw, customers_cleaned)

    quality_report["cleaned_customers"] = {
        "total_rows": int(len(customers_cleaned)),
        "removed_rows": int(len(customers_raw) - len(customers_cleaned)),
    }

    quality_report["cleaned_transactions"] = {
        "total_rows": int(len(transactions_cleaned)),
        "removed_rows": int(len(transactions_raw) - len(transactions_cleaned)),
    }

    print("Step 4: Saving cleaned CSV files...")
    customers_cleaned.to_csv(CLEANED_DIR / "customers_cleaned.csv", index=False)
    transactions_cleaned.to_csv(CLEANED_DIR / "transactions_cleaned.csv", index=False)

    print("Step 5: Loading cleaned data into SQLite database...")
    load_to_sqlite(customers_cleaned, transactions_cleaned)

    print("Step 6: Saving data quality report...")
    with open(REPORTS_DIR / "data_quality_report.json", "w", encoding="utf-8") as file:
        json.dump(quality_report, file, indent=4)

    print("\nETL pipeline completed successfully.")
    print(f"Raw customers: {len(customers_raw)}")
    print(f"Cleaned customers: {len(customers_cleaned)}")
    print(f"Raw transactions: {len(transactions_raw)}")
    print(f"Cleaned transactions: {len(transactions_cleaned)}")
    print("Cleaned CSV files saved in data/cleaned/")
    print("Data quality report saved in data/reports/")
    print("SQLite database saved in database/")


if __name__ == "__main__":
    main()