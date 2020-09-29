from loggingUtils import Logger
import os

logger = Logger(__name__).logger

logger.info("testing this works")

log2 = Logger("log2", log_file=os.path.join("logs", "example.log")).logger

log2.debug("testing this prints to both console and file")