import enum


class LogLevel(enum.Enum):
    ON = float('-inf')
    TRACE = 0
    DEBUG = 1
    INFO = 2
    WARN = 3
    WARNING = WARN
    ERROR = 4
    FATAL = 5
    CRITICAL = FATAL
    OFF = float('inf')

    __level_to_str = {
        OFF: "OFF",
        TRACE: "TRACE",
        DEBUG: "DEBUG",
        INFO: "INFO",
        WARN: "WARN",
        ERROR: "ERROR",
        FATAL: "FATAL",
        ON: "ON"
    }

    __str_to_level = {
        "OFF": OFF,
        "TRACE": TRACE,
        "DEBUG": DEBUG,
        "INFO": INFO,
        "WARN": WARN,
        "WARNING": WARN,
        "ERROR": ERROR,
        "FATAL": FATAL,
        "CRITICAL": FATAL,
        "ON": ON
    }

    def __str__(self):
        return self.name
    
    @staticmethod
    def addlevel(level: dict[str, int]) -> None:
        for k, v in level.items():
            if k in LogLevel.__str_to_level:
                raise ValueError(f"Level {k} already exists")
            LogLevel.__str_to_level[k] = v
            LogLevel.__level_to_str[v] = k

    @staticmethod
    def levelToStr(level: "LogLevel") -> str:
        if level.value in LogLevel.__level_to_str:
            return LogLevel.__level_to_str[level] # type: ignore
        else:
            return "UNKNOWN"
    
    @staticmethod
    def strToLevel(level: str) -> "LogLevel":
        if level in LogLevel.__str_to_level:
            return LogLevel.__str_to_level[level]
        else:
            return LogLevel.OFF