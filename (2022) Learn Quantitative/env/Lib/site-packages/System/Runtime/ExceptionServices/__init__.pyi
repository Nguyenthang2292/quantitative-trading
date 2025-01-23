from typing import overload
import typing

import System
import System.Runtime.ExceptionServices


class HandleProcessCorruptedStateExceptionsAttribute(System.Attribute):
    """Obsoletions.CorruptedStateRecoveryMessage"""

    def __init__(self) -> None:
        ...


class ExceptionDispatchInfo(System.Object):
    """This class has no documentation."""

    @property
    def SourceException(self) -> System.Exception:
        ...

    @staticmethod
    def Capture(source: System.Exception) -> System.Runtime.ExceptionServices.ExceptionDispatchInfo:
        ...

    @staticmethod
    def SetCurrentStackTrace(source: System.Exception) -> System.Exception:
        """
        Stores the current stack trace into the specified Exception instance.
        
        :param source: The unthrown Exception instance.
        :returns: The  exception instance.
        """
        ...

    @staticmethod
    def SetRemoteStackTrace(source: System.Exception, stackTrace: str) -> System.Exception:
        """
        Stores the provided stack trace into the specified Exception instance.
        
        :param source: The unthrown Exception instance.
        :param stackTrace: The stack trace string to persist within . This is normally acquired from the Exception.StackTrace property from the remote exception instance.
        :returns: The  exception instance.
        """
        ...

    @overload
    def Throw(self) -> None:
        ...

    @staticmethod
    @overload
    def Throw(source: System.Exception) -> None:
        ...


class FirstChanceExceptionEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def Exception(self) -> System.Exception:
        ...

    def __init__(self, exception: System.Exception) -> None:
        ...


