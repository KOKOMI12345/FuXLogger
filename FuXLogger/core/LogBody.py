
from .loglevel import LogLevel

class LogRecord:
    """
    这个类是用来存储日志信息的类
    """
    def __init__(self,
        name: str,
        level: LogLevel,
        levelName: str,
        message: str,
        time: str,
        timestamp: float,
        utctime: float,
        module: str,
        function: str,
        line: int,
        file: str,
        pathname: str,
        processid: int,
        threadid: int,
        threadName: str,
        processName: str,
        stack_info: str,
    ) -> None:
        self.name = name
        self.level = level
        self.levelName = levelName
        self.message = message
        self.timestamp = timestamp
        self.time = time
        self.utctime = utctime
        self.module = module        
        self.function = function
        self.line = line
        self.file = file
        self.pathname = pathname
        self.processid = processid
        self.threadid = threadid
        self.threadName = threadName
        self.processName = processName
        self.stack_info = stack_info

    def __str__(self) -> str:
        return f"""
        Name: {self.name}, 
        Level: {self.level}, 
        LevelName: {self.levelName}, 
        Message: {self.message}, 
        Time: {self.time}, 
        Timestamp: {self.timestamp}, 
        UTCTime: {self.utctime}, 
        Module: {self.module}, 
        Function: {self.function}, 
        Line: {self.line}, 
        File: {self.file}, 
        PathName: {self.pathname}, 
        ProcessID: {self.processid}, 
        ThreadID: {self.threadid}, 
        ThreadName: {self.threadName}, 
        ProcessName: {self.processName}, 
        StackInfo: {self.stack_info}
        """
    
    def getMessage(self) -> str:
        return self.message
    
    def ToDict(self) -> dict:
        return {
            "name": self.name,
            "level": self.level,
            "levelName": self.levelName,
            "message": self.message,
            "time": self.timestamp,
            "timestamp": self.timestamp,
            "utctime": self.utctime,
            "module": self.module,
            "function": self.function,
            "line": self.line,
            "file": self.file,
            "pathname": self.pathname,
            "processid": self.processid,
            "threadid": self.threadid,
            "threadName": self.threadName,
            "processName": self.processName,
            "Stack": self.stack_info
        }
    
    def ToJson(self) -> str:
        import json
        return json.dumps(self.ToDict())
    
    def ToTuple(self) -> tuple:
        return (
            self.name,
            self.level,
            self.levelName,
            self.message,
            self.time,
            self.timestamp,
            self.utctime,
            self.module,
            self.function,
            self.line,
            self.file,
            self.pathname,
            self.processid,
            self.threadid,
            self.threadName,
            self.processName,
            self.stack_info
        )