from .loglevel import LogLevel
from .handlers import Handler
from .LogBody import LogRecord
from ..utils import ExtractException
from ..utils.excformat import GetStackTrace
from ..utils.timeutil import getLocalDateTime , getUTCDateTime
import threading
import multiprocessing
import queue
import os
import sys
import inspect

class Logger:

    def __init__(self,
        name: str,
        level: LogLevel = LogLevel.ON,
        handlers: set[Handler] = set(),
        enqueue: bool = False
    )-> None:
        self.name: str = name
        self.level: LogLevel = level
        self.handlers: set[Handler] = handlers
        self.enqueue: bool = enqueue
        if enqueue:
            self.queue = queue.Queue()
            self.log_thread = threading.Thread(target=self.__enqueueHandler)
            self.log_thread.start()

    def addLevel(self, level: dict[str, int]) -> None:
        LogLevel.addlevel(level) # type: ignore

    def setLevel(self, level: LogLevel) -> None:
        self.level = level

    def addHandler(self, handler: Handler) -> None:
        self.handlers.add(handler)

    def removeHandler(self, handler: Handler) -> None:
        self.handlers.remove(handler)

    def __enqueueHandler(self) -> None:
        while True:
            try:
                record = self.queue.get(timeout=0.1)
                for handler in self.handlers:
                    handler.handle(record)
            except queue.Empty:
                if not threading.main_thread().is_alive():
                    break

    def __makeRecord(self, message: str, level: LogLevel) -> LogRecord:
        frame = inspect.currentframe().f_back.f_back.f_back  # type: ignore
        levelname = level.name
        current_module = inspect.getmodule(frame)
        module = current_module.__name__ if current_module else "__main__"
        return LogRecord(
            name=self.name,
            level=level,
            levelName=levelname,
            time="", # 留给后面格式化处理
            timestamp=getLocalDateTime(),
            utctime=getUTCDateTime(),
            threadid=threading.get_ident(),
            processid=multiprocessing.current_process().pid,  # type: ignore
            processName=multiprocessing.current_process().name,
            threadName=threading.current_thread().name,
            stack_info=GetStackTrace(5),
            file=os.path.basename(frame.f_code.co_filename),  # type: ignore
            pathname=os.getcwd(),
            line=frame.f_lineno,  # type: ignore
            function=frame.f_code.co_name,  # type: ignore
            module=module,  # type: ignore
            message=message
        )
    
    def __log(self, level: LogLevel, message: str) -> None:
        if self.enqueue:
            self.queue.put(self.__makeRecord(message, level))
        else:
            for handler in self.handlers:
                handler.handle(self.__makeRecord(message, level))

    def exception(self, message: str) -> None:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        if exc_traceback is not None:
            exc_info = ExtractException(exc_type, exc_value, exc_traceback)
            self.__log(LogLevel.ERROR, f"{message}\n{exc_info}")
        else:
            self.__log(LogLevel.ERROR, message)

    def log(self, level: LogLevel, message: str) -> None:
        self.__log(level, message)

    def trace(self, message: str) -> None:
        self.__log(LogLevel.TRACE, message)

    def debug(self, message: str) -> None:
        self.__log(LogLevel.DEBUG, message)

    def info(self, message: str) -> None:
        self.__log(LogLevel.INFO, message)

    def warning(self, message: str) -> None:
        self.__log(LogLevel.WARN, message)

    def error(self, message: str) -> None:
        self.__log(LogLevel.ERROR, message)

    def fatal(self, message: str) -> None:
        self.__log(LogLevel.FATAL, message)