# Data Quality & ETL Pipeline Project

This project is a small data engineering and data management workflow built with Python, SQL, Pandas, and SQLite.

It simulates a common business data problem: raw customer and transaction data may contain missing values, duplicate records, invalid dates, invalid categories, negative transaction amounts, and records linked to unknown customers. The pipeline extracts raw CSV files, profiles data quality issues, applies validation and cleaning rules, loads cleaned data into a SQLite database, and provides SQL queries for reporting.

## Project Goals

The goal of this project is to demonstrate practical skills in:

- Data extraction from CSV files
- Data profiling and validation
- Data cleaning and transformation
- ETL workflow design
- Data quality checks
- Relational database loading with SQLite
- SQL reporting queries
- Data dictionary, business rules, and lineage documentation

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
  - extract.py
  - validate.py
  - transform.py
  - load.py
  - run_pipeline.py
- .gitignore
- README.md
- requirements.txt

## Data Quality Issues Covered

The raw data intentionally includes common data quality problems, such as:

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

## ETL Workflow

The pipeline follows this flow:

Raw CSV files  
→ Extract  
→ Validate and profile data quality  
→ Transform and clean data  
→ Save cleaned CSV files  
→ Load into SQLite database  
→ Run SQL data quality and reporting queries  

## How to Run

Install dependencies:

`pip install -r requirements.txt`

Run the full pipeline:

`python src/run_pipeline.py`

Expected output:

- ETL pipeline completed successfully.
- Raw customers: 8
- Cleaned customers: 6
- Raw transactions: 11
- Cleaned transactions: 6
- Cleaned CSV files saved in data/cleaned/
- Data quality report saved in data/reports/
- SQLite database saved in database/

## Output Files

After running the pipeline, the project creates:

- data/cleaned/customers_cleaned.csv
- data/cleaned/transactions_cleaned.csv
- data/reports/data_quality_report.json
- database/customer_transactions.db

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

- sql/reporting_queries.sql
- sql/data_quality_checks.sql

## Documentation

The project includes supporting data documentation:

- docs/data_dictionary.md describes fields, data types, and examples.
- docs/business_rules.md defines validation and transformation rules.
- docs/lineage.md explains how data moves through the pipeline.

## Technologies Used

- Python
- Pandas
- SQL
- SQLite
- Git / GitHub
- Markdown documentation

## Interview Summary

A short explanation of this project:

I built a small ETL workflow using Python, SQL, Pandas, and SQLite. The pipeline extracts raw customer and transaction data, profiles common data quality issues, applies validation and cleaning rules, loads cleaned data into a relational database, and provides SQL queries for business reporting. I also documented the data dictionary, business rules, and data lineage to make the workflow easier to understand and maintain.