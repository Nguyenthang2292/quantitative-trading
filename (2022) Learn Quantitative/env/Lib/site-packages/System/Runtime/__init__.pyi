from typing import overload
import datetime
import typing
import warnings

import System
import System.Runtime
import System.Runtime.ConstrainedExecution
import System.Threading


class GCLargeObjectHeapCompactionMode(System.Enum):
    """This class has no documentation."""

    Default = 1

    CompactOnce = 2


class GCLatencyMode(System.Enum):
    """This class has no documentation."""

    Batch = 0

    Interactive = 1

    LowLatency = 2

    SustainedLowLatency = 3

    NoGCRegion = 4


class GCSettings(System.Object):
    """This class has no documentation."""

    LatencyMode: int
    """This property contains the int value of a member of the System.Runtime.GCLatencyMode enum."""

    LargeObjectHeapCompactionMode: int
    """This property contains the int value of a member of the System.Runtime.GCLargeObjectHeapCompactionMode enum."""

    IsServerGC: bool


class AssemblyTargetedPatchBandAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def TargetedPatchBand(self) -> str:
        ...

    def __init__(self, targetedPatchBand: str) -> None:
        ...


class TargetedPatchingOptOutAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Reason(self) -> str:
        ...

    def __init__(self, reason: str) -> None:
        ...


class AmbiguousImplementationException(System.Exception):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None:
        ...


class MemoryFailPoint(System.Runtime.ConstrainedExecution.CriticalFinalizerObject, System.IDisposable):
    """This class has no documentation."""

    MemoryFailPointReservedMemory: int

    def __init__(self, sizeInMegabytes: int) -> None:
        ...

    def Dispose(self) -> None:
        ...


class ProfileOptimization(System.Object):
    """This class has no documentation."""

    @staticmethod
    def SetProfileRoot(directoryPath: str) -> None:
        ...

    @staticmethod
    def StartProfile(profile: str) -> None:
        ...


class JitInfo(System.Object):
    """A static class for getting information about the Just In Time compiler."""

    @staticmethod
    def GetCompilationTime(currentThread: bool = False) -> datetime.timedelta:
        """
        Get the amount of time the JIT Compiler has spent compiling methods. If  is true,
        then this value is scoped to the current thread, otherwise, this is a global value.
        
        :param currentThread: Whether the returned value should be specific to the current thread. Default: false
        :returns: The amount of time the JIT Compiler has spent compiling methods.
        """
        ...

    @staticmethod
    def GetCompiledILBytes(currentThread: bool = False) -> int:
        """
        Get the number of bytes of IL that have been compiled. If  is true,
        then this value is scoped to the current thread, otherwise, this is a global value.
        
        :param currentThread: Whether the returned value should be specific to the current thread. Default: false
        :returns: The number of bytes of IL the JIT has compiled.
        """
        ...

    @staticmethod
    def GetCompiledMethodCount(currentThread: bool = False) -> int:
        """
        Get the number of methods that have been compiled. If  is true,
        then this value is scoped to the current thread, otherwise, this is a global value.
        
        :param currentThread: Whether the returned value should be specific to the current thread. Default: false
        :returns: The number of methods the JIT has compiled.
        """
        ...


class ControlledExecution(System.Object):
    """This class has no documentation."""

    @staticmethod
    def Run(action: typing.Callable[[], None], cancellationToken: System.Threading.CancellationToken) -> None:
        """Obsoletions.ControlledExecutionRunMessage"""
        warnings.warn("Obsoletions.ControlledExecutionRunMessage", DeprecationWarning)


