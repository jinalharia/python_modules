from loggingUtils import Logger
from timingUtils import TimingUtil

logger = Logger(__name__).logger
timer = TimingUtil(logger)


logger.info("testing this works")

timer.print("after first logger.info")

log2 = Logger("log2", log_file="example.log").logger

timer.print("after create new logger")

log2.debug("testing this prints to both console and file")

timer.print("after final logger.debug")