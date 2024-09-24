

class FuXLoggerException(Exception):
    """
    Base class for all FuXLogger exceptions.
    """
    pass

class RendererException(FuXLoggerException):
    """
    Exception raised when there is an error in the rendering process.
    """
    pass

class NotImplementedException(FuXLoggerException):
    """
    Exception raised when a method or function is not implemented yet.
    """
    pass

class InvalidConfigurationException(FuXLoggerException):
    """
    Exception raised when there is an error in the configuration file.
    """
    pass

class InvalidHandlerException(FuXLoggerException):
    """
    Exception raised when there is an error in the handler configuration.
    """
    pass