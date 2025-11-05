import pandas as pd

def transform_data(df):
    # Replace missing, empty, or whitespace-only account_id with 'UNKNOWN'
    df['account_id'] = df['account_id'].astype(str)  # convert all to string
    df['account_id'] = df['account_id'].str.strip()  # remove leading/trailing spaces
    df['account_id'] = df['account_id'].replace({'': 'UNKNOWN', 'nan': 'UNKNOWN', 'None': 'UNKNOWN'})

    # Fill missing amounts
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce').fillna(0)

    # Convert transaction_date to datetime
    df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')

    # Standardize types
    df['transaction_type'] = df['transaction_type'].str.lower()
    df['currency'] = df['currency'].str.upper()

    # Add derived columns
    df['month'] = df['transaction_date'].dt.month_name()
    df['is_credit'] = df['transaction_type'].apply(lambda x: 1 if x == 'credit' else 0)
    df['is_debit'] = df['transaction_type'].apply(lambda x: 1 if x == 'debit' else 0)

    print("✅ Transformation complete")
    return df
