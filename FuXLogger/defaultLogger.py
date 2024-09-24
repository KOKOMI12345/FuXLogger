
from . import StreamHandler , LogFormatter , LogManager , LogLevel

my_log_fmt = LogFormatter("{time} | {levelName:<7} | {module}:{function} | {file}:{line:02} | {message}")

logger = LogManager.getLogger("main", my_log_fmt,enqueue=True)

console_handler = StreamHandler("console", LogLevel.ON, my_log_fmt,colorize=True, enableXMLRender=True)

logger.addHandler(console_handler)

__all__ = ["logger"]