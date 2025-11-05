def data_quality_check(df):
    errors = []

    # Check negative amounts
    if df['amount'].lt(0).any():
        errors.append("Negative transaction amounts found")

    # Check duplicate transaction IDs
    if df['transaction_id'].duplicated().any():
        errors.append("Duplicate transaction IDs")

    # Check missing account IDs after transformation
    missing_account = df['account_id'].isna() | (df['account_id'].str.strip() == '') | (df['account_id'].str.upper() == 'UNKNOWN')
    if missing_account.any():
        errors.append("Missing account IDs detected")

    # Check currency validity
    valid_currencies = ['USD', 'EUR', 'INR']
    if not df['currency'].isin(valid_currencies).all():
        errors.append("Invalid currency code found")

    if errors:
        print("❌ Data Quality Check Failed:")
        for err in errors:
            print(" -", err)
        return False
    else:
        print("✅ Data Quality Check Passed")
        return True
