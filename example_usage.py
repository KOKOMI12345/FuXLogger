from FuXLogger import LogManager , LogFormatter , StreamHandler , Level
# 配置一个日志记录器
myfmt = LogFormatter("{time} | {levelName:<7} | {module}:{function} | {file}:{line:02d} | {message}")
logger = LogManager.getLogger("main", level=Level.ON, formatter=myfmt , enqueue=True)
console_handler = StreamHandler("console", level=Level.ON, formatter=myfmt, colorize=True, enableXMLRender=True)
logger.addHandler(console_handler)

logger.trace("This is a trace message")
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.fatal("This is a fatal message")