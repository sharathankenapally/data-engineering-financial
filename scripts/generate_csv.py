import pandas as pd
import os

# Folder for data
script_dir = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.join(script_dir, '..', 'data')
os.makedirs(data_folder, exist_ok=True)

# transactions1.csv
data1 = {
    'transaction_id': [1001, 1002, 1003, 1004, 1005],
    'account_id': ['A101', 'A102', 'A101', 'A103', 'A104'],
    'amount': [500, 200, 150, 0, 1000],
    'transaction_type': ['credit', 'debit', 'credit', 'debit', 'credit'],
    'currency': ['USD']*5,
    'transaction_date': ['2025-01-02','2025-01-03','2025-01-04','2025-01-05','2025-01-05']
}
pd.DataFrame(data1).to_csv(os.path.join(data_folder,'transactions1.csv'), index=False, encoding='utf-8-sig')

# transactions2.csv
data2 = {
    'transaction_id': [2001,2002,2003,2004,2005],
    'account_id': ['A101','A102','A103','A104','A104'],  # no missing
    'amount': [600,250,400,500,1000],
    'transaction_type': ['credit','debit','credit','debit','credit'],
    'currency': ['USD']*5,
    'transaction_date': ['2025-02-02','2025-02-03','2025-02-03','2025-02-04','2025-02-04']
}
pd.DataFrame(data2).to_csv(os.path.join(data_folder,'transactions2.csv'), index=False, encoding='utf-8-sig')

print("Clean CSVs generated in", data_folder)
