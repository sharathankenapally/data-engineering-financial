import sqlite3

def load_data(df):
    conn = sqlite3.connect('../database/finance.db')
    df.to_sql('transactions', conn, if_exists='replace', index=False)
    conn.close()
    print("Data successfully loaded into SQLite database")
