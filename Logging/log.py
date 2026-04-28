import logging



# Five security levels in logging: Debug, Info, Warning, Error, Critical
# logging.info("You have got 20 emails in your inbox")
# logging.critical("ALL COMPONENTS HAVE FAILED!")

# # the Critical message shows but not the info. thats because python has the default level of warning.
# # if you switch the level to debug, you will see everything including the info.
# logging.warning("You have got 20 emails in your inbox")
# logging.critical("ALL COMPONENTS HAVE FAILED!")

# # Change python security level
logging.basicConfig(level=logging.DEBUG)
# logging.info("You have got 20 emails in your inbox")

# # Change the root to your login choice
logger = logging.getLogger("Fenris")
# logger.info("Fenris in the house")
# logger.critical("Burn this motha down!")

# # using the .log to set security
# logger.log(logging.CRITICAL, "THIS IS LOG!")

# Best practice is to save the log messages into files.
handler = logging.FileHandler("MyLog.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.debug("This is a debug message!")
logger.info("This is important information!")