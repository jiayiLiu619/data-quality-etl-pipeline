from pathlib import Path
import json
import logging
from datetime import datetime

from extract import extract_customers, extract_transactions
from validate import validate_customers, validate_transactions
from transform import clean_customers, clean_transactions
from load import load_to_sqlite
from report import generate_html_report


ROOT = Path(__file__).resolve().parents[1]
CLEANED_DIR = ROOT / "data" / "cleaned"
REPORTS_DIR = ROOT / "data" / "reports"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)


def main() -> None:
    """
    Run the full ETL pipeline:
    1. Extract raw CSV data
    2. Validate raw data quality
    3. Clean and transform data
    4. Save cleaned CSV files
    5. Load cleaned data into SQLite
    6. Save data quality reports (JSON + HTML)
    """
    CLEANED_DIR.mkdir(parents=True, exist_ok=True)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    pipeline_start = datetime.now()

    log.info("Step 1: Extracting raw data...")
    customers_raw = extract_customers()
    transactions_raw = extract_transactions()
    log.info(f"  Loaded {len(customers_raw):,} customer rows and {len(transactions_raw):,} transaction rows.")

    log.info("Step 2: Validating raw data quality...")
    valid_customer_ids = set(customers_raw["customer_id"])
    quality_report = {
        "raw_customers": validate_customers(customers_raw),
        "raw_transactions": validate_transactions(transactions_raw, valid_customer_ids),
    }
    log.info("  Validation complete.")

    log.info("Step 3: Cleaning and transforming data...")
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
    log.info(f"  Customers: {len(customers_raw):,} → {len(customers_cleaned):,} cleaned.")
    log.info(f"  Transactions: {len(transactions_raw):,} → {len(transactions_cleaned):,} cleaned.")

    log.info("Step 4: Saving cleaned CSV files...")
    customers_cleaned.to_csv(CLEANED_DIR / "customers_cleaned.csv", index=False)
    transactions_cleaned.to_csv(CLEANED_DIR / "transactions_cleaned.csv", index=False)
    log.info("  Cleaned CSV files saved in data/cleaned/")

    log.info("Step 5: Loading cleaned data into SQLite database...")
    load_to_sqlite(customers_cleaned, transactions_cleaned)
    log.info("  SQLite database saved in database/")

    log.info("Step 6: Saving data quality reports...")
    with open(REPORTS_DIR / "data_quality_report.json", "w", encoding="utf-8") as file:
        json.dump(quality_report, file, indent=4)
    generate_html_report(quality_report, REPORTS_DIR)
    log.info("  JSON + HTML reports saved in data/reports/")

    duration = (datetime.now() - pipeline_start).total_seconds()
    log.info(f"\nETL pipeline completed successfully in {duration:.2f}s.")
    log.info(f"  Raw customers:        {len(customers_raw):,}")
    log.info(f"  Cleaned customers:    {len(customers_cleaned):,}")
    log.info(f"  Raw transactions:     {len(transactions_raw):,}")
    log.info(f"  Cleaned transactions: {len(transactions_cleaned):,}")


if __name__ == "__main__":
    main()