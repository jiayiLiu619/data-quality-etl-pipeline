
# Data Lineage

This document explains how data moves through the ETL pipeline.

## 1. Source Data

Raw data is stored in CSV files:

- `data/raw/raw_customers.csv`
- `data/raw/raw_transactions.csv`

These files simulate operational customer and transaction records.

## 2. Extract

The extraction step reads raw CSV files into Pandas DataFrames.

Relevant file:

- `src/extract.py`

## 3. Validate

The validation step profiles common data quality issues, including:

- Missing values
- Duplicate IDs
- Invalid dates
- Invalid customer segments
- Invalid transaction channels
- Invalid transaction statuses
- Negative transaction values
- Transactions linked to unknown customers

Relevant file:

- `src/validate.py`

Output:

- `data/reports/data_quality_report.json`

## 4. Transform

The transformation step applies business rules, removes invalid records, standardizes date fields, and creates the derived `gross_profit` field.

Relevant file:

- `src/transform.py`

Outputs:

- `data/cleaned/customers_cleaned.csv`
- `data/cleaned/transactions_cleaned.csv`

## 5. Load

The load step writes cleaned customer and transaction data into a SQLite database.

Relevant file:

- `src/load.py`

Output:

- `database/customer_transactions.db`

## 6. Reporting

SQL queries can be run against the cleaned SQLite tables to support data quality checks and business reporting.

Relevant files:

- `sql/data_quality_checks.sql`
- `sql/reporting_queries.sql`