from structlog import wrap_logger, PrintLogger

from enums.log import LOG
from properties import Properties


class MyLogger:

    @staticmethod
    def log(log_type, msg):
        """
        Method to write a log message
        :param log_type: ENUM
        :param msg: String, the message to log
        :return: Nothing
        """
        filename = None
        if log_type == LOG.SPIDER:
            filename = Properties.SPIDER_LOG_FILE
        elif log_type == LOG.CRAWLER:
            filename = Properties.CRAWLER_LOG_FILE
        with open(filename, "a+") as file:
            logger = wrap_logger(logger=PrintLogger(file=file))
            logger.msg(msg)
