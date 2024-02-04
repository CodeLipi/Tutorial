# logging

import logging

logging.basicConfig(filename='log.txt', level=logging.DEBUG)
# logging.basicConfig(filename='log.txt', level=logging.WARNING)
# logging.basicConfig(filename='log.txt')

print("python logging demo")

logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
# logging.warning("warning message by default")
logging.error("error message")
logging.critical("critical message")