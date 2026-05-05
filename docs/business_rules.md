# Business Rules

This document defines the validation and transformation rules used in the ETL pipeline.

## Customer Rules

1. `customer_id` must not be missing.
2. Duplicate `customer_id` values are removed.
3. When duplicate customer records exist, the latest valid record is kept.
4. `signup_date` must be a valid date.
5. `segment` must be one of the following values:
   - New
   - Returning
   - High Value

## Transaction Rules

1. `transaction_id` must not be missing.
2. Duplicate `transaction_id` values are removed.
3. When duplicate transaction records exist, the latest valid record is kept.
4. `transaction_date` must be a valid date.
5. `amount` and `cost` must be numeric and non-negative.
6. `channel` must be one of the following values:
   - Web
   - Mobile
   - Store
   - Partner
7. `status` must be one of the following values:
   - Completed
   - Returned
   - Cancelled
8. Every transaction must link to a valid `customer_id` in the cleaned customer table.

## Reporting Rules

Gross profit is calculated as:

`gross_profit = amount - cost`

Gross margin rate is calculated as:

`gross_margin_rate = gross_profit / amount`

Return rate is calculated as:

`return_rate = returned_transactions / total_transactions`