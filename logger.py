"""
Loggers for application modules
"""
import logging

# Create a custom formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Create a handler for console output
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# Create a handler for file output
file_handler = logging.FileHandler("./log/main.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Create loggers for your modules
logger_bot = logging.getLogger("telegram_bot")
logger_bot.setLevel(logging.DEBUG)
logger_bot.addHandler(console_handler)  # Send logs to console
logger_bot.addHandler(file_handler)  # Send logs to file
