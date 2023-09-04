"""************************************************************************************************
File          : log.py
About         : Logging object for this set of exercises
Author        : Freddie Mercer
*************************************************************************************************"""

import logging

class myLogger:
    def __init__(self, log_level=logging.INFO):
        self.log_level = log_level
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.log_level)
        
        # Create a console handler and set the log level
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.log_level)
        
        # Create a formatter and set it for both handlers
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        
        # Add both handlers to the logger
        self.logger.addHandler(console_handler)

    def log(self, message):
        self.logger.log(self.log_level, message)

# Example usage:
if __name__ == "__main__":
    logger = myLogger()
    logger.log("This is a log message.")