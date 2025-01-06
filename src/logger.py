import logging
import os
from datetime import datetime

# Corrected date format to use strftime
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# Creating the log directory
logs_path = os.path.join(os.getcwd(), "logs")  # Create a 'logs' folder for the log files
os.makedirs(logs_path, exist_ok=True)  # Ensure the directory is created

# Corrected path for the log file (should be inside the 'logs' directory)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Setting up logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Sample logging
if __name__ == "__main__":
    logging.info("Logging has started")
