# main_pipeline.py
from extract_data import extract_data
from transform_data import transform_data
from data_quality_check import data_quality_check
from load_data import load_data
from generate_report import generate_report
from visualize_report import visualize_report
from logger_setup import setup_logger
import os

# Initialize logger
logger = setup_logger()
logger.info("🏦 Starting Financial Data Pipeline...")

try:
    # 1️⃣ Extract
    df = extract_data()
    logger.info(f"✅ Extracted {df.shape[0]} records")

    # 2️⃣ Transform
    df = transform_data(df)
    logger.info("✅ Transformation complete")

    # 3️⃣ Data Quality Check
    if not data_quality_check(df):
        logger.error("⚠️ Data Quality Check Failed. Pipeline stopped.")
        exit()

    # 4️⃣ Load into SQLite
    load_data(df)
    logger.info("✅ Data successfully loaded into SQLite database")

    # 5️⃣ Generate summary reports
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

    # 6️⃣ Create visualization
    visualize_report(summary_file, monthly_file)
    logger.info("Visualization created successfully")
    logger.info("Pipeline finished successfully!")

except Exception as e:
    logger.exception(f"Pipeline failed due to error: {e}")
