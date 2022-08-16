import logging
from logging.handlers import RotatingFileHandler


# Create and configure logger
handler = RotatingFileHandler(
    "logs/stdout.log", mode='a', maxBytes=50 * 1024 * 1024, backupCount=5)
logging.basicConfig(filename="logs/stdout.log",
                    format='%(asctime)s %(levelname)s %(message)s', level=logging.ERROR)

for _ in range(1):
    logging.debug("Harmless debug Message")
    logging.info("Just an information")
    logging.warning("Its a Warning")
    logging.error("Did you try to divide by zero")
