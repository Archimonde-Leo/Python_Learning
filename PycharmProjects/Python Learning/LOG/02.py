'''
1.需求
    1）所有级别日志写入磁盘
    2）all.log文件记录所有日志信息。日志格式为：日期和时间-日志级别-日志信息
    3）error.log文件记录error及以上级别日志信息。日志格式为：日期和时间-日志级别-文件名[:行号]-日志信息
    4）all.log文件每天凌晨日志切割

2.分析
    1）所有级别日志==>日志器level需设置为最低级别
    2）两个不同目的地且都是磁盘文件==>两个Handler且都是FileHandler
    3）all.log文件每天凌晨日志切割==>logging.handlers.TimedRotatingFileHandler
    4）两个日志文件格式不同==>需要对两个handler分别设置格式器
'''

import logging
import logging.handlers
import datetime

# 定义logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)
# 设置不同的handler
rf_handler = logging.handlers.TimedRotatingFileHandler('all.log',
                                                       when='midnight',
                                                       interval=1,
                                                       backupCount=7,
                                                       atTime=None)
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname) - %(message)s"))

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname) - %(filename)s[:%(lineno)d] - %(message)s"))
# 把相应处理器组装到logger
logger.addHandler(rf_handler)
logger.addHandler(f_handler)

logging.debug("This is a debug log.")
logging.info("This is an info log.")
logging.warning("This is a warning log.")
logging.error("This is an error log.")
logging.critical("This is a critical log.")