import time
import logging
from scripts.extract_data import extract_data
from scripts.transform_data import transform_data
from scripts.data_quality_check import data_quality_check
from scripts.load_data import load_data
from scripts.generate_report import generate_report
from scripts.visualize_report import visualize_report
import os
import pandas as pd

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger()

def run_pipeline():
    logger.info("🏦 Starting Financial Data Pipeline (Simulated DAG)...")

    try:
        # Task 1: Extract
        logger.info("🔹 Task 1: Extracting data")
        df = extract_data()
        logger.info(f"✅ Extracted {df.shape[0]} records")
        time.sleep(1)  # simulate task duration

        # Task 2: Transform
        logger.info("🔹 Task 2: Transforming data")
        df = transform_data(df)
        logger.info("✅ Transformation complete")
        time.sleep(1)

        # Task 3: Data Quality Check
        logger.info("🔹 Task 3: Data Quality Check")
        if not data_quality_check(df):
            logger.error("⚠️ Data Quality Check Failed. Stopping pipeline.")
            return
        logger.info("✅ Data Quality Check passed")
        time.sleep(1)

        # Task 4: Load
        logger.info("🔹 Task 4: Loading data into database")
        load_data(df)
        logger.info("✅ Data successfully loaded")
        time.sleep(1)

        # Task 5: Generate Reports
        logger.info("🔹 Task 5: Generating reports")
        generate_report(df)
        reports_dir = os.path.join(os.path.dirname(__file__), '..', 'reports')
        summary_file = max(
            [os.path.join(reports_dir, f) for f in os.listdir(reports_dir) if f.startswith('summary_report_')],
            key=os.path.getctime
        )
        monthly_file = max(
            [os.path.join(reports_dir, f) for f in os.listdir(reports_dir) if f.startswith('monthly_summary_')],
            key=os.path.getctime
        )
        visualize_report(summary_file, monthly_file)
        logger.info("✅ Reports and visualization generated")
        time.sleep(1)

        logger.info("🎉 Pipeline finished successfully!")

    except Exception as e:
        logger.exception(f"❌ Pipeline failed due to error: {e}")

# Simulate scheduling
if __name__ == "__main__":
    import schedule

    # Run every 1 minute (demo)
    schedule.every(1).minutes.do(run_pipeline)

    logger.info("⏰ DAG simulator started. Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(1)
