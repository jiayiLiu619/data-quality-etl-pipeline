from extract import extract_customers, extract_transactions
from validate import validate_customers, validate_transactions


customers = extract_customers()
transactions = extract_transactions()

valid_customer_ids = set(customers["customer_id"])

customer_report = validate_customers(customers)
transaction_report = validate_transactions(transactions, valid_customer_ids)

print("Customer Data Quality Report:")
print(customer_report)

print("\nTransaction Data Quality Report:")
print(transaction_report)