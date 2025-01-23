from typing import overload
import abc
import datetime
import typing

import QuantConnect.Logging
import System
import System.Collections.Concurrent

QuantConnect_Logging__EventContainer_Callable = typing.TypeVar("QuantConnect_Logging__EventContainer_Callable")
QuantConnect_Logging__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Logging__EventContainer_ReturnType")


class LogType(System.Enum):
    """Error level"""

    Debug = 0
    """Debug log level"""

    Trace = 1
    """Trace log level"""

    Error = 2
    """Error log level"""


class LogEntry(System.Object):
    """Log entry wrapper to make logging simpler:"""

    @property
    def Time(self) -> datetime.datetime:
        """Time of the log entry"""
        ...

    @Time.setter
    def Time(self, value: datetime.datetime):
        """Time of the log entry"""
        ...

    @property
    def Message(self) -> str:
        """Message of the log entry"""
        ...

    @Message.setter
    def Message(self, value: str):
        """Message of the log entry"""
        ...

    @property
    def MessageType(self) -> QuantConnect.Logging.LogType:
        """Descriptor of the message type."""
        ...

    @MessageType.setter
    def MessageType(self, value: QuantConnect.Logging.LogType):
        """Descriptor of the message type."""
        ...

    @overload
    def __init__(self, message: str) -> None:
        """Create a default log message with the current time."""
        ...

    @overload
    def __init__(self, message: str, time: typing.Union[datetime.datetime, datetime.date], type: QuantConnect.Logging.LogType = ...) -> None:
        """
        Create a log entry at a specific time in the analysis (for a backtest).
        
        :param message: Message for log
        :param time: Utc time of the message
        :param type: Type of the log entry
        """
        ...

    def ToString(self) -> str:
        """Helper override on the log entry."""
        ...


class ILogHandler(System.IDisposable, metaclass=abc.ABCMeta):
    """Interface for redirecting log output"""

    def Debug(self, text: str) -> None:
        """
        Write debug message to log
        
        :param text: The debug text to log
        """
        ...

    def Error(self, text: str) -> None:
        """
        Write error message to log
        
        :param text: The error text to log
        """
        ...

    def Trace(self, text: str) -> None:
        """
        Write debug message to log
        
        :param text: The trace text to log
        """
        ...


class FileLogHandler(System.Object, QuantConnect.Logging.ILogHandler):
    """Provides an implementation of ILogHandler that writes all log messages to a file on disk."""

    @overload
    def __init__(self, filepath: str, useTimestampPrefix: bool = True) -> None:
        """
        Initializes a new instance of the FileLogHandler class to write messages to the specified file path.
        The file will be opened using FileMode.Append
        
        :param filepath: The file path use to save the log messages
        :param useTimestampPrefix: True to prefix each line in the log which the UTC timestamp, false otherwise
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the FileLogHandler class using 'log.txt' for the filepath."""
        ...

    def CreateMessage(self, text: str, level: str) -> str:
        """
        Creates the message to be logged
        
        This method is protected.
        
        :param text: The text to be logged
        :param level: The logging leel
        """
        ...

    def Debug(self, text: str) -> None:
        """
        Write debug message to log
        
        :param text: The debug text to log
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def Error(self, text: str) -> None:
        """
        Write error message to log
        
        :param text: The error text to log
        """
        ...

    def Trace(self, text: str) -> None:
        """
        Write debug message to log
        
        :param text: The trace text to log
        """
        ...


class ConsoleLogHandler(System.Object, QuantConnect.Logging.ILogHandler):
    """ILogHandler implementation that writes log output to console."""

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the QuantConnect.Logging.ConsoleLogHandler class."""
        ...

    @overload
    def __init__(self, dateFormat: str = ...) -> None:
        """
        Initializes a new instance of the QuantConnect.Logging.ConsoleLogHandler class.
        
        :param dateFormat: Specifies the date format to use when writing log messages to the console window
        """
        ...

    def Debug(self, text: str) -> None:
        """
        Write debug message to log
        
        :param text: The debug text to log
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def Error(self, text: str) -> None:
        """
        Write error message to log
        
        :param text: The error text to log
        """
        ...

    def Trace(self, text: str) -> None:
        """
        Write debug message to log
        
        :param text: The trace text to log
        """
        ...


class ConsoleErrorLogHandler(QuantConnect.Logging.ConsoleLogHandler):
    """Subclass of ConsoleLogHandler that only logs error messages"""

    def Debug(self, text: str) -> None:
        """
        Hide debug messages from log
        
        :param text: The debug text to log
        """
        ...

    def Trace(self, text: str) -> None:
        """
        Hide trace messages from log
        
        :param text: The trace text to log
        """
        ...


class QueueLogHandler(System.Object, QuantConnect.Logging.ILogHandler):
    """ILogHandler implementation that queues all logs and writes them when instructed."""

    @property
    def Logs(self) -> System.Collections.Concurrent.ConcurrentQueue[QuantConnect.Logging.LogEntry]:
        """Public access to the queue for log processing."""
        ...

    @property
    def LogEvent(self) -> _EventContainer[typing.Callable[[QuantConnect.Logging.LogEntry], None], None]:
        """Logging Event Handler"""
        ...

    @LogEvent.setter
    def LogEvent(self, value: _EventContainer[typing.Callable[[QuantConnect.Logging.LogEntry], None], None]):
        """Logging Event Handler"""
        ...

    def __init__(self) -> None:
        """Initializes a new instance of the QueueLogHandler class."""
        ...

    def Debug(self, text: str) -> None:
        """
        Write debug message to log
        
        :param text: The debug text to log
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def Error(self, text: str) -> None:
        """
        Write error message to log
        
        :param text: The error text to log
        """
        ...

    def LogEventRaised(self, log: QuantConnect.Logging.LogEntry) -> None:
        """LOgging event delegate"""
        ...

    def OnLogEvent(self, log: QuantConnect.Logging.LogEntry) -> None:
        """
        Raise a log event safely
        
        This method is protected.
        """
        ...

    def Trace(self, text: str) -> None:
        """
        Write debug message to log
        
        :param text: The trace text to log
        """
        ...


class CompositeLogHandler(System.Object, QuantConnect.Logging.ILogHandler):
    """Provides an ILogHandler implementation that composes multiple handlers"""

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the CompositeLogHandler that pipes log messages to the console and log.txt"""
        ...

    @overload
    def __init__(self, *handlers: QuantConnect.Logging.ILogHandler) -> None:
        """
        Initializes a new instance of the CompositeLogHandler class from the specified handlers
        
        :param handlers: The implementations to compose
        """
        ...

    def Debug(self, text: str) -> None:
        """Write debug message to log"""
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def Error(self, text: str) -> None:
        """Write error message to log"""
        ...

    def Trace(self, text: str) -> None:
        """Write debug message to log"""
        ...


class Log(System.Object):
    """Logging management class."""

    LogHandler: QuantConnect.Logging.ILogHandler
    """Gets or sets the ILogHandler instance used as the global logging implementation."""

    DebuggingEnabled: bool
    """Global flag whether to enable debugging logging:"""

    FilePath: str
    """Global flag to specify file based log path"""

    DebuggingLevel: int
    """Set the minimum message level:"""

    @staticmethod
    def Debug(text: str, level: int = 1) -> None:
        """
        Output to the console
        
        :param text: The message to show
        :param level: debug level
        """
        ...

    @staticmethod
    @overload
    def Error(error: str, overrideMessageFloodProtection: bool = False) -> None:
        """
        Log error
        
        :param error: String Error
        :param overrideMessageFloodProtection: Force sending a message, overriding the "do not flood" directive
        """
        ...

    @staticmethod
    @overload
    def Error(exception: System.Exception, message: str = None, overrideMessageFloodProtection: bool = False) -> None:
        """
        Log error
        
        :param exception: The exception to be logged
        :param message: An optional message to be logged, if null/whitespace the messge text will be extracted
        :param overrideMessageFloodProtection: Force sending a message, overriding the "do not flood" directive
        """
        ...

    @staticmethod
    @overload
    def Error(format: str, *args: typing.Any) -> None:
        """Writes the message in red"""
        ...

    @staticmethod
    @overload
    def Trace(traceText: str, overrideMessageFloodProtection: bool = False) -> None:
        """Log trace"""
        ...

    @staticmethod
    @overload
    def Trace(format: str, *args: typing.Any) -> None:
        """Writes the message in normal text"""
        ...

    @staticmethod
    def VarDump(obj: typing.Any, recursion: int = 0) -> str:
        """C# Equivalent of Print_r in PHP:"""
        ...


class LogHandlerExtensions(System.Object):
    """Logging extensions."""

    @staticmethod
    def Debug(logHandler: QuantConnect.Logging.ILogHandler, text: str, *args: typing.Any) -> None:
        """
        Write debug message to log
        
        :param text: Message
        :param args: Arguments to format.
        """
        ...

    @staticmethod
    def Error(logHandler: QuantConnect.Logging.ILogHandler, text: str, *args: typing.Any) -> None:
        """
        Write error message to log
        
        :param text: Message
        :param args: Arguments to format.
        """
        ...

    @staticmethod
    def Trace(logHandler: QuantConnect.Logging.ILogHandler, text: str, *args: typing.Any) -> None:
        """
        Write debug message to log
        
        :param text: Message
        :param args: Arguments to format.
        """
        ...


class FunctionalLogHandler(System.Object, QuantConnect.Logging.ILogHandler):
    """ILogHandler implementation that writes log output to result handler"""

    @overload
    def __init__(self) -> None:
        """Default constructor to handle MEF."""
        ...

    @overload
    def __init__(self, debug: typing.Callable[[str], None], trace: typing.Callable[[str], None], error: typing.Callable[[str], None]) -> None:
        """Initializes a new instance of the QuantConnect.Logging.FunctionalLogHandler class."""
        ...

    def Debug(self, text: str) -> None:
        """
        Write debug message to log
        
        :param text: The debug text to log
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def Error(self, text: str) -> None:
        """
        Write error message to log
        
        :param text: The error text to log
        """
        ...

    def Trace(self, text: str) -> None:
        """
        Write debug message to log
        
        :param text: The trace text to log
        """
        ...


class RegressionFileLogHandler(QuantConnect.Logging.FileLogHandler):
    """
    Provides an implementation of ILogHandler that writes all log messages to a file on disk
    without timestamps.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the RegressionFileLogHandler class
        that will write to a 'regression.log' file in the executing directory
        """
        ...


class WhoCalledMe(System.Object):
    """Provides methods for determining higher stack frames"""

    @staticmethod
    def GetMethodName(frame: int = 1) -> str:
        """
        Gets the method name of the caller
        
        :param frame: The number of stack frames to retrace from the caller's position
        :returns: The method name of the containing scope 'frame' stack frames above the caller.
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Logging__EventContainer_Callable, QuantConnect_Logging__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Logging__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Logging__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Logging__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


