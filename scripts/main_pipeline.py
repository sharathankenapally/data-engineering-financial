# main_pipeline.py
from extract_data import extract_data
from transform_data import transform_data
from data_quality_check import data_quality_check
from load_data import load_data
from generate_report import generate_report
from visualize_report import visualize_report
from logger_setup import setup_logger
import os
import pandas as pd

# Initialize logger
logger = setup_logger()
logger.info("Starting Financial Data Pipeline...")

try:
    # Extract
    df = extract_data()
    logger.info(f"Extracted {df.shape[0]} records")

    # Transform
    df = transform_data(df)
    logger.info("Transformation complete")

    # Save processed data for verification
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'output')
    os.makedirs(data_dir, exist_ok=True)
    processed_path = os.path.join(data_dir, 'processed_transactions.csv')
    df.to_csv(processed_path, index=False)
    logger.info(f"Processed data saved at: {processed_path}")

    # Data Quality Check
    if not data_quality_check(df):
        logger.error("Data Quality Check Failed. Pipeline stopped.")
        exit()

    # Load into SQLite
    load_data(df)
    logger.info("Data successfully loaded into SQLite database")

    # Generate summary reports
    generate_report(df)

    # Get latest report files
    reports_dir = os.path.join(os.path.dirname(__file__), '..', 'reports')
    summary_file = max(
        [os.path.join(reports_dir, f) for f in os.listdir(reports_dir) if f.startswith('summary_report_')],
        key=os.path.getctime
    )
    monthly_file = max(
        [os.path.join(reports_dir, f) for f in os.listdir(reports_dir) if f.startswith('monthly_summary_')],
        key=os.path.getctime
    )

    # Create visualization
    visualize_report(summary_file, monthly_file)
    logger.info("Visualization created successfully")
    logger.info("Pipeline finished successfully!")

except Exception as e:
    logger.exception(f"Pipeline failed due to error: {e}")
