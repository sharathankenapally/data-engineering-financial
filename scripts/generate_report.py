import pandas as pd
import os
from datetime import datetime

def generate_report(df):
    report_folder = os.path.join(os.path.dirname(__file__), '..', 'reports')
    os.makedirs(report_folder, exist_ok=True)

    report = {
        'total_transactions': [df.shape[0]],
        'total_credits': [df['is_credit'].sum()],
        'total_debits': [df['is_debit'].sum()],
        'total_amount': [df['amount'].sum()],
        'high_value_transactions': [df[df['amount'] > 5000].shape[0]],
        'duplicate_transactions': [df['transaction_id'].duplicated().sum()]
    }

    # Transactions per month
    monthly = df.groupby('month')['transaction_id'].count().reset_index()
    monthly.rename(columns={'transaction_id': 'transactions_count'}, inplace=True)

    report_df = pd.DataFrame(report)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = os.path.join(report_folder, f'summary_report_{timestamp}.csv')
    
    # Save main metrics
    report_df.to_csv(report_file, index=False)
    # Save monthly breakdown as a separate sheet (optional: Excel)
    monthly_file = os.path.join(report_folder, f'monthly_summary_{timestamp}.csv')
    monthly.to_csv(monthly_file, index=False)

    print(f"Summary report generated: {report_file}")
    print(f"Monthly summary generated: {monthly_file}")
