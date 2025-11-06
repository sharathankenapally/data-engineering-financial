import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

def visualize_report(summary_file, monthly_file):
    report_folder = os.path.join(os.path.dirname(__file__), '..', 'reports')
    os.makedirs(report_folder, exist_ok=True)

    # Load CSV reports
    summary = pd.read_csv(summary_file)
    monthly = pd.read_csv(monthly_file)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    plot_file = os.path.join(report_folder, f'report_visualization_{timestamp}.png')

    plt.figure(figsize=(12,6))

    # Bar chart for monthly transactions
    sns.barplot(data=monthly, x='month', y='transactions_count', palette='Blues_d')
    plt.title('Transactions per Month')
    plt.xlabel('Month')
    plt.ylabel('Number of Transactions')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(plot_file)
    plt.close()

    print(f"Visualization saved: {plot_file}")
