import logging
import os

def setup_logger():
    log_folder = os.path.join(os.path.dirname(__file__), '..', 'logs')
    os.makedirs(log_folder, exist_ok=True)
    log_file = os.path.join(log_folder, 'pipeline.log')

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s | %(levelname)s | %(message)s',
        filemode='a'
    )
    # Also print to console
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)

    return logging.getLogger()
