import logging
logging.basicConfig(level=logging.DEBUG, filename="errors.log")
# setting the level
"""
CRITICAL Level 5 ---- highest
ERROR Level 4
WARNING level 3
info level 2
debug level 1 ---- lowest

says whats going on execution
"""
logging.critical("THIS IS A CRITICAL LEVEL MESSAGE!!!")
logging.error("This is an Error level message!")
logging.warning("This is a Warning Level Message")
logging.info("This is an Informationa-Level Message")
logging.debug("This is a debugging level message")
