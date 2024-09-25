from .logger import Logger
from .formatter import LogFormatter
import threading

class LogManager:

    loggers: dict[str, Logger] = {}
    dftformatter: LogFormatter = LogFormatter("{time} | {level:<7} | {message}")
    lock = threading.Lock()

    @staticmethod
    def getLogger(name: str, formatter: LogFormatter = dftformatter, enqueue: bool = False, is_async: bool = False) -> Logger:
        """
        获取一个日志记录器对象,注意,如果is_async为True,则确保必须再异步环境内调用此方法,否则会报错
        """
        with LogManager.lock:
            if LogManager.loggers.get(name) is None:
                LogManager.loggers[name] = Logger(name=name, enqueue=enqueue, is_async=is_async)
            return LogManager.loggers[name]