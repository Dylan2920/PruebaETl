import logging
import os

def init_logger():
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        filename="logs/etl.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s: %(message)s"
    )
    return logging.getLogger()

def log_event(logger, message):
    logger.info(message)
