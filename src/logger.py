# It’s Logging means recording important messages or events while your program is running.
# like keeping a diary of everything your program is doing — especially things like 
# errors, warnings, or progress updates.


# 🧠 Why is Logging Important?
# Imagine your program crashes or behaves unexpectedly. How do you find out what went wrong?

# If you used logging:

# You can check the log file and see exactly what your code was doing at each step.

# You can find the error message, location, and time of the issue.

import logging
import os
from datetime import datetime

# 1. Create a log filename with a timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Create a folder named 'logs' in current directory and store the log file inside it
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok= True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)


# for checking purpose the main is created...
# if __name__ == "__main__":
#     logging.info("Logging has started")