# Data Dictionary

This document describes the fields used in the cleaned customer and transaction datasets.

## customers

| Field | Type | Description | Example |
|---|---|---|---|
| customer_id | TEXT | Unique customer identifier | C001 |
| customer_name | TEXT | Customer display name | Ava Chen |
| email | TEXT | Customer email address | ava.chen@example.com |
| signup_date | DATE | Date when the customer signed up | 2024-01-05 |
| segment | TEXT | Customer segment used for reporting | Returning |
| province | TEXT | Province or region code | ON |

## transactions

| Field | Type | Description | Example |
|---|---|---|---|
| transaction_id | TEXT | Unique transaction identifier | T001 |
| customer_id | TEXT | Customer linked to the transaction | C001 |
| transaction_date | DATE | Date of the transaction | 2024-02-01 |
| channel | TEXT | Transaction channel | Web |
| status | TEXT | Transaction status | Completed |
| amount | REAL | Revenue amount for the transaction | 120.00 |
| cost | REAL | Estimated cost associated with the transaction | 70.00 |
| gross_profit | REAL | Calculated as amount minus cost | 50.00 |