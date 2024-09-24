
from .loglevel import LogLevel
from ..utils.color import Color

_logColors = {
    LogLevel.TRACE : Color.GREY,
    LogLevel.DEBUG : Color.BLUE,
    LogLevel.INFO : Color.CYAN,
    LogLevel.WARN : Color.YELLOW,
    LogLevel.ERROR : Color.RED,
    LogLevel.FATAL : Color.MAGENTA
}