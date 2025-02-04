from typing import overload
import abc
import typing

import System
import System.Threading.Tasks.Sources

System_Threading_Tasks_Sources_ManualResetValueTaskSourceCore_TResult = typing.TypeVar("System_Threading_Tasks_Sources_ManualResetValueTaskSourceCore_TResult")
System_Threading_Tasks_Sources_IValueTaskSource_TResult = typing.TypeVar("System_Threading_Tasks_Sources_IValueTaskSource_TResult")


class ValueTaskSourceOnCompletedFlags(System.Enum):
    """
    Flags passed from ValueTask and ValueTask{TResult} to
    IValueTaskSource.OnCompleted and IValueTaskSource{TResult}.OnCompleted
    to control behavior.
    """

    # Cannot convert to Python: None = 0
    """No requirements are placed on how the continuation is invoked."""

    UseSchedulingContext = ...
    """
    Set if OnCompleted should capture the current scheduling context (e.g. SynchronizationContext)
    and use it when queueing the continuation for execution.  If this is not set, the implementation
    may choose to execute the continuation in an arbitrary location.
    """

    FlowExecutionContext = ...
    """Set if OnCompleted should capture the current ExecutionContext and use it to run the continuation."""


class ManualResetValueTaskSourceCore(typing.Generic[System_Threading_Tasks_Sources_ManualResetValueTaskSourceCore_TResult]):
    """Provides the core logic for implementing a manual-reset IValueTaskSource or IValueTaskSource{TResult}."""

    @property
    def RunContinuationsAsynchronously(self) -> bool:
        """Gets or sets whether to force continuations to run asynchronously."""
        ...

    @RunContinuationsAsynchronously.setter
    def RunContinuationsAsynchronously(self, value: bool):
        """Gets or sets whether to force continuations to run asynchronously."""
        ...

    @property
    def Version(self) -> int:
        """Gets the operation version."""
        ...

    def GetResult(self, token: int) -> System_Threading_Tasks_Sources_ManualResetValueTaskSourceCore_TResult:
        """
        Gets the result of the operation.
        
        :param token: Opaque value that was provided to the ValueTask's constructor.
        """
        ...

    def GetStatus(self, token: int) -> int:
        """
        Gets the status of the operation.
        
        :param token: Opaque value that was provided to the ValueTask's constructor.
        :returns: This method returns the int value of a member of the System.Threading.Tasks.Sources.ValueTaskSourceStatus enum.
        """
        ...

    def OnCompleted(self, continuation: typing.Callable[[System.Object], None], state: typing.Any, token: int, flags: System.Threading.Tasks.Sources.ValueTaskSourceOnCompletedFlags) -> None:
        """
        Schedules the continuation action for this operation.
        
        :param continuation: The continuation to invoke when the operation has completed.
        :param state: The state object to pass to  when it's invoked.
        :param token: Opaque value that was provided to the ValueTask's constructor.
        :param flags: The flags describing the behavior of the continuation.
        """
        ...

    def Reset(self) -> None:
        """Resets to prepare for the next operation."""
        ...

    def SetException(self, error: System.Exception) -> None:
        """
        Completes with an error.
        
        :param error: The exception.
        """
        ...

    def SetResult(self, result: System_Threading_Tasks_Sources_ManualResetValueTaskSourceCore_TResult) -> None:
        """
        Completes with a successful result.
        
        :param result: The result.
        """
        ...


class ValueTaskSourceStatus(System.Enum):
    """Indicates the status of an IValueTaskSource or IValueTaskSource{TResult}."""

    Pending = 0
    """The operation has not yet completed."""

    Succeeded = 1
    """The operation completed successfully."""

    Faulted = 2
    """The operation completed with an error."""

    Canceled = 3
    """The operation completed due to cancellation."""


class IValueTaskSource(typing.Generic[System_Threading_Tasks_Sources_IValueTaskSource_TResult], metaclass=abc.ABCMeta):
    """Represents an object that can be wrapped by a ValueTask{TResult}."""

    @overload
    def GetResult(self, token: int) -> None:
        """
        Gets the result of the IValueTaskSource.
        
        :param token: Opaque value that was provided to the ValueTask's constructor.
        """
        ...

    @overload
    def GetResult(self, token: int) -> System_Threading_Tasks_Sources_IValueTaskSource_TResult:
        """
        Gets the result of the IValueTaskSource{TResult}.
        
        :param token: Opaque value that was provided to the ValueTask's constructor.
        """
        ...

    @overload
    def GetStatus(self, token: int) -> int:
        """
        Gets the status of the current operation.
        
        :param token: Opaque value that was provided to the ValueTask's constructor.
        :returns: This method returns the int value of a member of the System.Threading.Tasks.Sources.ValueTaskSourceStatus enum.
        """
        ...

    @overload
    def GetStatus(self, token: int) -> int:
        """
        Gets the status of the current operation.
        
        :param token: Opaque value that was provided to the ValueTask's constructor.
        :returns: This method returns the int value of a member of the System.Threading.Tasks.Sources.ValueTaskSourceStatus enum.
        """
        ...

    @overload
    def OnCompleted(self, continuation: typing.Callable[[System.Object], None], state: typing.Any, token: int, flags: System.Threading.Tasks.Sources.ValueTaskSourceOnCompletedFlags) -> None:
        """
        Schedules the continuation action for this IValueTaskSource.
        
        :param continuation: The continuation to invoke when the operation has completed.
        :param state: The state object to pass to  when it's invoked.
        :param token: Opaque value that was provided to the ValueTask's constructor.
        :param flags: The flags describing the behavior of the continuation.
        """
        ...

    @overload
    def OnCompleted(self, continuation: typing.Callable[[System.Object], None], state: typing.Any, token: int, flags: System.Threading.Tasks.Sources.ValueTaskSourceOnCompletedFlags) -> None:
        """
        Schedules the continuation action for this IValueTaskSource{TResult}.
        
        :param continuation: The continuation to invoke when the operation has completed.
        :param state: The state object to pass to  when it's invoked.
        :param token: Opaque value that was provided to the ValueTask's constructor.
        :param flags: The flags describing the behavior of the continuation.
        """
        ...


