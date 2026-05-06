# Data Quality & ETL Pipeline Project

This project is a data engineering and data management workflow built with Python, SQL, Pandas, NumPy, and SQLite.

It simulates a common business data problem: raw customer and transaction data can contain missing IDs, duplicate records, invalid dates, invalid categories, negative transaction amounts, and transactions linked to unknown customers. The pipeline generates synthetic data, profiles data quality issues, applies validation and cleaning rules, loads cleaned data into SQLite, and produces JSON/HTML reports and SQL queries for business analysis.

## Project Goals

The goal of this project is to demonstrate practical skills in:

- Synthetic data generation
- Data extraction from CSV files
- Data profiling and validation
- Data cleaning and transformation
- ETL workflow design
- Automated data quality checks
- Relational database loading with SQLite
- SQL reporting queries
- JSON and HTML data quality reporting
- Data dictionary, business rules, and lineage documentation

## Dataset

The project generates:

- 10,000 raw customer records
- 50,000 raw transaction records

The generated data intentionally includes data quality issues such as:

- Missing customer IDs
- Missing email values
- Duplicate customer IDs
- Duplicate transaction IDs
- Invalid signup dates
- Invalid transaction dates
- Invalid customer segments
- Invalid transaction channels
- Invalid transaction statuses
- Negative transaction amounts
- Transactions linked to unknown customers

## Project Structure

data-quality-etl-pipeline/

- data/
  - raw/
    - raw_customers.csv
    - raw_transactions.csv
  - cleaned/
    - customers_cleaned.csv
    - transactions_cleaned.csv
  - reports/
    - data_quality_report.json
    - data_quality_report.html
- database/
  - customer_transactions.db
- docs/
  - business_rules.md
  - data_dictionary.md
  - lineage.md
- sql/
  - create_tables.sql
  - data_quality_checks.sql
  - reporting_queries.sql
- src/
  - generate_data.py
  - extract.py
  - validate.py
  - transform.py
  - load.py
  - report.py
  - run_pipeline.py
- .gitignore
- README.md
- requirements.txt

## ETL Workflow

The pipeline follows this flow:

Raw synthetic data generation  
→ Extract raw CSV files  
→ Validate and profile data quality  
→ Transform and clean data  
→ Save cleaned CSV files  
→ Load cleaned tables into SQLite  
→ Generate JSON and HTML data quality reports  
→ Run SQL data quality and reporting queries  

## How to Run

Install dependencies:

`pip install -r requirements.txt`

Generate synthetic raw data:

`python src/generate_data.py`

Run the full pipeline:

`python src/run_pipeline.py`

## Current Pipeline Output

The latest pipeline run produced:

- Raw customers: 10,000
- Cleaned customers: 8,000
- Raw transactions: 50,000
- Cleaned transactions: 28,343
- Customer pass rate: 80.0%
- Transaction pass rate: 56.7%

The transaction pass rate is lower because transaction cleaning enforces both transaction-level validation rules and referential integrity. Transactions linked to customers removed during customer cleaning are also removed.

## Data Quality Report

The pipeline generates:

- `data/reports/data_quality_report.json`
- `data/reports/data_quality_report.html`

The report summarizes raw row counts, cleaned row counts, removed rows, pass rates, and issue counts across customer and transaction datasets.

## Example Data Quality Checks

Customer checks include:

- Missing customer IDs
- Missing emails
- Duplicate customer IDs
- Invalid signup dates
- Invalid customer segments

Transaction checks include:

- Duplicate transaction IDs
- Invalid transaction dates
- Invalid transaction channels
- Invalid transaction statuses
- Negative transaction amounts
- Unknown customer references

## SQL Reporting Queries

The project includes SQL queries for:

- Revenue by channel
- Gross profit by channel
- Gross margin rate
- Average order value
- Transaction count by customer segment
- Return rate by channel
- Data quality checks on cleaned tables

These queries are stored in:

- `sql/reporting_queries.sql`
- `sql/data_quality_checks.sql`

## Documentation

The project includes supporting documentation:

- `docs/data_dictionary.md` describes fields, data types, and examples.
- `docs/business_rules.md` defines validation and transformation rules.
- `docs/lineage.md` explains how data moves through the pipeline.

## Technologies Used

- Python
- Pandas
- NumPy
- SQL
- SQLite
- Git / GitHub
- Markdown documentation
