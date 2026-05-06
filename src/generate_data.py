import random
from pathlib import Path
from datetime import date, timedelta
import numpy as np
import pandas as pd

SEED = 42
N_CUSTOMERS = 10_000
N_TRANSACTIONS = 50_000
DIRTY_RATE = 0.05

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"

VALID_SEGMENTS = ["New", "Returning", "High Value"]
VALID_CHANNELS  = ["Web", "Mobile", "Store", "Partner"]
VALID_STATUSES  = ["Completed", "Returned", "Cancelled"]
PROVINCES = ["ON", "BC", "AB", "QC", "MB", "SK", "NS", "NB", "NL", "PE"]

rng = np.random.default_rng(SEED)
random.seed(SEED)

def random_date(start: date, end: date) -> str:
    delta = (end - start).days
    return (start + timedelta(days=int(rng.integers(0, delta)))).isoformat()

def inject_customer_issues(df):
    n, k = len(df), max(1, int(len(df) * DIRTY_RATE))
    idx = rng.choice(n, size=k * 6, replace=False)
    df.loc[idx[:k], "email"] = np.nan                          # missing email
    dup = df.loc[idx[k:2*k], "customer_id"].values
    df.loc[idx[2*k:3*k], "customer_id"] = dup                 # duplicate ID
    df.loc[idx[3*k:4*k], "signup_date"] = "not-a-date"        # invalid date
    df.loc[idx[4*k:5*k], "segment"] = "Unknown"               # invalid segment
    df.loc[idx[5*k:], "customer_id"] = np.nan                 # missing ID
    return df.sample(frac=1, random_state=SEED).reset_index(drop=True)

def inject_transaction_issues(df, valid_ids):
    n, k = len(df), max(1, int(len(df) * DIRTY_RATE))
    idx = rng.choice(n, size=k * 7, replace=False)
    dup = df.loc[idx[:k], "transaction_id"].values
    df.loc[idx[k:2*k], "transaction_id"] = dup                # duplicate ID
    df.loc[idx[2*k:3*k], "transaction_date"] = "bad-date"     # invalid date
    df.loc[idx[3*k:4*k], "channel"] = "Fax"                   # invalid channel
    df.loc[idx[4*k:5*k], "status"] = "Pending"                # invalid status
    df.loc[idx[5*k:6*k], "amount"] *= -1                      # negative amount
    df.loc[idx[6*k:], "customer_id"] = "C_UNKNOWN"            # unknown customer
    return df.sample(frac=1, random_state=SEED).reset_index(drop=True)

def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    ids    = [f"C{str(i).zfill(6)}" for i in range(1, N_CUSTOMERS+1)]
    customers = pd.DataFrame({
        "customer_id":   ids,
        "customer_name": [f"Customer_{i}" for i in range(1, N_CUSTOMERS+1)],
        "email":         [f"customer_{i}@example.com" for i in range(1, N_CUSTOMERS+1)],
        "signup_date":   [random_date(date(2020,1,1), date(2024,12,31)) for _ in ids],
        "segment":       rng.choice(VALID_SEGMENTS, size=N_CUSTOMERS, p=[0.4,0.4,0.2]).tolist(),
        "province":      rng.choice(PROVINCES, size=N_CUSTOMERS).tolist(),
    })
    customers = inject_customer_issues(customers)
    customers.to_csv(RAW_DIR / "raw_customers.csv", index=False)
    print(f"Saved raw_customers.csv — {len(customers):,} rows")

    t_ids = [f"T{str(i).zfill(7)}" for i in range(1, N_TRANSACTIONS+1)]
    amounts = np.round(rng.uniform(10, 500, size=N_TRANSACTIONS), 2)
    transactions = pd.DataFrame({
        "transaction_id":   t_ids,
        "customer_id":      rng.choice(ids, size=N_TRANSACTIONS).tolist(),
        "transaction_date": [random_date(date(2021,1,1), date(2025,3,31)) for _ in t_ids],
        "channel":          rng.choice(VALID_CHANNELS, size=N_TRANSACTIONS, p=[0.4,0.3,0.2,0.1]).tolist(),
        "status":           rng.choice(VALID_STATUSES, size=N_TRANSACTIONS, p=[0.80,0.12,0.08]).tolist(),
        "amount":           amounts,
        "cost":             np.round(amounts * rng.uniform(0.3, 0.7, size=N_TRANSACTIONS), 2),
    })
    transactions = inject_transaction_issues(transactions, ids)
    transactions.to_csv(RAW_DIR / "raw_transactions.csv", index=False)
    print(f"Saved raw_transactions.csv — {len(transactions):,} rows")

if __name__ == "__main__":
    main()