import logging

LOG_FORMAT = "%(asctime)s=====%(levelname)s++++++%(message)s"

logging.basicConfig(filename="01py.log", level=logging.DEBUG, format=LOG_FORMAT) # 设置级别

logging.debug("This is a debug log.")
logging.info("This is an info log.")
logging.warning("This is a warning log.")
logging.error("This is an error log.")
logging.critical("This is a critical log.")
# 另一种写法：
# logging.log(logging.DEBUG, "This is a debug log.")