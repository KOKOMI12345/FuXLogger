from .logger import Logger
from .formatter import LogFormatter
import threading

class LogManager:

    loggers: dict[str, Logger] = {}
    dftformatter: LogFormatter = LogFormatter("{time} | {level:<7} | {message}")
    lock = threading.Lock()

    @staticmethod
    def getLogger(name: str, formatter: LogFormatter = dftformatter, enqueue: bool = False) -> Logger:
        with LogManager.lock:
            if LogManager.loggers.get(name) is None:
                LogManager.loggers[name] = Logger(name=name, enqueue=enqueue)
            return LogManager.loggers[name]