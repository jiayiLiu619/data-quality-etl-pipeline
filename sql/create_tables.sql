-- Create relational tables for the cleaned customer and transaction data.

DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id TEXT PRIMARY KEY,
    customer_name TEXT,
    email TEXT,
    signup_date DATE,
    segment TEXT,
    province TEXT
);

CREATE TABLE transactions (
    transaction_id TEXT PRIMARY KEY,
    customer_id TEXT,
    transaction_date DATE,
    channel TEXT,
    status TEXT,
    amount REAL,
    cost REAL,
    gross_profit REAL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);