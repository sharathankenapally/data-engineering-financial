import pandas as pd
import os

def extract_data():
    folder = os.path.join(os.path.dirname(__file__), '..', 'data')
    csv_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.csv')]

    print("Looking for CSV files in:", folder)
    print("Found files:", csv_files)

    dfs = []
    for f in csv_files:
        try:
            # Try reading CSV with robust options
            df = pd.read_csv(
                f,
                encoding='utf-8-sig',  # handles BOM if present
                skip_blank_lines=True
            )
            if df.empty:
                print(f"File {f} is empty, skipping.")
                continue
            dfs.append(df)
        except Exception as e:
            print(f"Skipped file {f} due to error: {e}")

    if not dfs:
        raise ValueError("No valid CSVs could be loaded. Check file content or formatting.")

    combined = pd.concat(dfs, ignore_index=True)
    print(f"Extracted {combined.shape[0]} records from {len(dfs)} CSV files.")
    return combined
