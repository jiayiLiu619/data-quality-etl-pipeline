from extract import extract_customers, extract_transactions
from transform import clean_customers, clean_transactions


customers_raw = extract_customers()
transactions_raw = extract_transactions()

customers_cleaned = clean_customers(customers_raw)
transactions_cleaned = clean_transactions(transactions_raw, customers_cleaned)

print("Cleaned Customers:")
print(customers_cleaned)
print("Cleaned Customers shape:", customers_cleaned.shape)

print("\nCleaned Transactions:")
print(transactions_cleaned)
print("Cleaned Transactions shape:", transactions_cleaned.shape)