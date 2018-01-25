import logging

# Create a logger with the program name and level=DEBUG
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler that will write to the file “app.log”
fh = logging.FileHandler("log.txt")

# Create a handler that will write log to stderr
ch = logging.StreamHandler()

# Create a formatter and add it to the handlers
formatter = logging.Formatter("TIME=%(asctime)s, %(name)s, [%(levelname)s] : %(message)s")
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(ch)
logger.addHandler(fh)

logger.info("Hello!")
