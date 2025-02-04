from typing import overload
import abc
import datetime
import typing
import warnings

import Microsoft.Win32.SafeHandles
import System
import System.Collections.Generic
import System.Globalization
import System.Runtime.ConstrainedExecution
import System.Runtime.InteropServices
import System.Runtime.Serialization
import System.Security.Principal
import System.Threading
import System.Threading.Tasks

System_Threading_CancellationToken = typing.Any
System_Threading_AsyncFlowControl = typing.Any
System_Threading_CancellationTokenRegistration = typing.Any

System_Threading_AsyncLocal_T = typing.TypeVar("System_Threading_AsyncLocal_T")
System_Threading_AsyncLocalValueChangedArgs_T = typing.TypeVar("System_Threading_AsyncLocalValueChangedArgs_T")
System_Threading_Volatile_Read_T = typing.TypeVar("System_Threading_Volatile_Read_T")
System_Threading_Volatile_Write_T = typing.TypeVar("System_Threading_Volatile_Write_T")
System_Threading_ThreadPool_QueueUserWorkItem_TState = typing.TypeVar("System_Threading_ThreadPool_QueueUserWorkItem_TState")
System_Threading_ThreadPool_UnsafeQueueUserWorkItem_TState = typing.TypeVar("System_Threading_ThreadPool_UnsafeQueueUserWorkItem_TState")
System_Threading_ThreadLocal_T = typing.TypeVar("System_Threading_ThreadLocal_T")
System_Threading_LazyInitializer_EnsureInitialized_T = typing.TypeVar("System_Threading_LazyInitializer_EnsureInitialized_T")
System_Threading_Interlocked_CompareExchange_T = typing.TypeVar("System_Threading_Interlocked_CompareExchange_T")
System_Threading_Interlocked_Exchange_T = typing.TypeVar("System_Threading_Interlocked_Exchange_T")


class WaitHandle(System.MarshalByRefObject, System.IDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    MaxWaitHandles: int = 64

    InvalidHandle: System.IntPtr = ...
    """This field is protected."""

    WaitSuccess: int = 0

    WaitAbandoned: int = ...

    WaitTimeout: int = ...

    @property
    def Handle(self) -> System.IntPtr:
        """WaitHandle.Handle has been deprecated. Use the SafeWaitHandle property instead."""
        warnings.warn("WaitHandle.Handle has been deprecated. Use the SafeWaitHandle property instead.", DeprecationWarning)

    @Handle.setter
    def Handle(self, value: System.IntPtr):
        """WaitHandle.Handle has been deprecated. Use the SafeWaitHandle property instead."""
        warnings.warn("WaitHandle.Handle has been deprecated. Use the SafeWaitHandle property instead.", DeprecationWarning)

    @property
    def SafeWaitHandle(self) -> Microsoft.Win32.SafeHandles.SafeWaitHandle:
        ...

    @SafeWaitHandle.setter
    def SafeWaitHandle(self, value: Microsoft.Win32.SafeHandles.SafeWaitHandle):
        ...

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def Close(self) -> None:
        ...

    @overload
    def Dispose(self, explicitDisposing: bool) -> None:
        """This method is protected."""
        ...

    @overload
    def Dispose(self) -> None:
        ...

    @staticmethod
    @overload
    def SignalAndWait(toSignal: System.Threading.WaitHandle, toWaitOn: System.Threading.WaitHandle) -> bool:
        ...

    @staticmethod
    @overload
    def SignalAndWait(toSignal: System.Threading.WaitHandle, toWaitOn: System.Threading.WaitHandle, timeout: datetime.timedelta, exitContext: bool) -> bool:
        ...

    @staticmethod
    @overload
    def SignalAndWait(toSignal: System.Threading.WaitHandle, toWaitOn: System.Threading.WaitHandle, millisecondsTimeout: int, exitContext: bool) -> bool:
        ...

    @staticmethod
    @overload
    def WaitAll(waitHandles: typing.List[System.Threading.WaitHandle], millisecondsTimeout: int) -> bool:
        ...

    @staticmethod
    @overload
    def WaitAll(waitHandles: typing.List[System.Threading.WaitHandle], timeout: datetime.timedelta) -> bool:
        ...

    @staticmethod
    @overload
    def WaitAll(waitHandles: typing.List[System.Threading.WaitHandle]) -> bool:
        ...

    @staticmethod
    @overload
    def WaitAll(waitHandles: typing.List[System.Threading.WaitHandle], millisecondsTimeout: int, exitContext: bool) -> bool:
        ...

    @staticmethod
    @overload
    def WaitAll(waitHandles: typing.List[System.Threading.WaitHandle], timeout: datetime.timedelta, exitContext: bool) -> bool:
        ...

    @staticmethod
    @overload
    def WaitAny(waitHandles: typing.List[System.Threading.WaitHandle], millisecondsTimeout: int) -> int:
        ...

    @staticmethod
    @overload
    def WaitAny(waitHandles: typing.List[System.Threading.WaitHandle], timeout: datetime.timedelta) -> int:
        ...

    @staticmethod
    @overload
    def WaitAny(waitHandles: typing.List[System.Threading.WaitHandle]) -> int:
        ...

    @staticmethod
    @overload
    def WaitAny(waitHandles: typing.List[System.Threading.WaitHandle], millisecondsTimeout: int, exitContext: bool) -> int:
        ...

    @staticmethod
    @overload
    def WaitAny(waitHandles: typing.List[System.Threading.WaitHandle], timeout: datetime.timedelta, exitContext: bool) -> int:
        ...

    @overload
    def WaitOne(self, millisecondsTimeout: int) -> bool:
        ...

    @overload
    def WaitOne(self, timeout: datetime.timedelta) -> bool:
        ...

    @overload
    def WaitOne(self) -> bool:
        ...

    @overload
    def WaitOne(self, millisecondsTimeout: int, exitContext: bool) -> bool:
        ...

    @overload
    def WaitOne(self, timeout: datetime.timedelta, exitContext: bool) -> bool:
        ...


class RegisteredWaitHandle(System.MarshalByRefObject):
    """An object representing the registration of a WaitHandle via ThreadPool.RegisterWaitForSingleObject."""

    @property
    def Callback(self) -> System.Threading._ThreadPoolWaitOrTimerCallback:
        """The callback to execute when the wait on Handle either times out or completes."""
        ...

    @property
    def Handle(self) -> Microsoft.Win32.SafeHandles.SafeWaitHandle:
        """The SafeWaitHandle that was registered."""
        ...

    @property
    def TimeoutTimeMs(self) -> int:
        """The time this handle times out at in ms."""
        ...

    @TimeoutTimeMs.setter
    def TimeoutTimeMs(self, value: int):
        """The time this handle times out at in ms."""
        ...

    @property
    def TimeoutDurationMs(self) -> int:
        ...

    @property
    def IsInfiniteTimeout(self) -> bool:
        ...

    @property
    def Repeating(self) -> bool:
        """Whether or not the wait is a repeating wait."""
        ...

    @property
    def IsBlocking(self) -> bool:
        ...

    @property
    def WaitThread(self) -> System.Threading.PortableThreadPool.WaitThread:
        """The PortableThreadPool.WaitThread this RegisteredWaitHandle was registered on."""
        ...

    @WaitThread.setter
    def WaitThread(self, value: System.Threading.PortableThreadPool.WaitThread):
        """The PortableThreadPool.WaitThread this RegisteredWaitHandle was registered on."""
        ...

    @overload
    def Unregister(self, waitObject: System.Threading.WaitHandle) -> bool:
        ...

    @overload
    def Unregister(self, waitObject: System.Threading.WaitHandle) -> bool:
        ...


class ThreadStartException(System.SystemException):
    """This class has no documentation."""


class Timeout(System.Object):
    """This class has no documentation."""

    InfiniteTimeSpan: datetime.timedelta = ...

    Infinite: int = -1

    UnsignedInfinite: int = ...


class CancellationTokenRegistration(System.IEquatable[System_Threading_CancellationTokenRegistration], System.IDisposable, System.IAsyncDisposable):
    """Represents a callback delegate that has been registered with a System.Threading.CancellationToken."""

    @property
    def Token(self) -> System.Threading.CancellationToken:
        """Gets the CancellationToken with which this registration is associated."""
        ...

    def Dispose(self) -> None:
        """
        Disposes of the registration and unregisters the target callback from the associated
        System.Threading.CancellationToken.
        If the target callback is currently executing, this method will wait until it completes, except
        in the degenerate cases where a callback method unregisters itself.
        """
        ...

    def DisposeAsync(self) -> System.Threading.Tasks.ValueTask:
        """
        Disposes of the registration and unregisters the target callback from the associated
        System.Threading.CancellationToken.
        The returned ValueTask will complete once the associated callback
        is unregistered without having executed or once it's finished executing, except
        in the degenerate case where the callback itself is unregistering itself.
        """
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the current System.Threading.CancellationTokenRegistration instance is equal to the
        specified object.
        
        :param obj: The other object to which to compare this instance.
        :returns: True, if both this and  are equal. False, otherwise. Two System.Threading.CancellationTokenRegistration instances are equal if they both refer to the output of a single call to the same Register method of a System.Threading.CancellationToken.
        """
        ...

    @overload
    def Equals(self, other: System.Threading.CancellationTokenRegistration) -> bool:
        """
        Determines whether the current System.Threading.CancellationToken instance is equal to the
        specified object.
        
        :param other: The other System.Threading.CancellationTokenRegistration to which to compare this instance.
        :returns: True, if both this and  are equal. False, otherwise. Two System.Threading.CancellationTokenRegistration instances are equal if they both refer to the output of a single call to the same Register method of a System.Threading.CancellationToken.
        """
        ...

    def GetHashCode(self) -> int:
        """
        Serves as a hash function for a System.Threading.CancellationTokenRegistration.
        
        :returns: A hash code for the current System.Threading.CancellationTokenRegistration instance.
        """
        ...

    def Unregister(self) -> bool:
        """
        Disposes of the registration and unregisters the target callback from the associated
        System.Threading.CancellationToken.
        """
        ...


class CancellationToken(System.IEquatable[System_Threading_CancellationToken]):
    """Propagates notification that operations should be canceled."""

    # Cannot convert to Python: None: System.Threading.CancellationToken

    @property
    def IsCancellationRequested(self) -> bool:
        """Gets whether cancellation has been requested for this token."""
        ...

    @property
    def CanBeCanceled(self) -> bool:
        """Gets whether this token is capable of being in the canceled state."""
        ...

    @property
    def WaitHandle(self) -> System.Threading.WaitHandle:
        """Gets a System.Threading.WaitHandle that is signaled when the token is canceled."""
        ...

    def __init__(self, canceled: bool) -> None:
        """
        Initializes the System.Threading.CancellationToken.
        
        :param canceled: The canceled state for the token.
        """
        ...

    @overload
    def Equals(self, other: System.Threading.CancellationToken) -> bool:
        """
        Determines whether the current System.Threading.CancellationToken instance is equal to the
        specified token.
        
        :param other: The other System.Threading.CancellationToken to which to compare this instance.
        :returns: True if the instances are equal; otherwise, false. Two tokens are equal if they are associated with the same System.Threading.CancellationTokenSource or if they were both constructed from public CancellationToken constructors and their IsCancellationRequested values are equal.
        """
        ...

    @overload
    def Equals(self, other: typing.Any) -> bool:
        """
        Determines whether the current System.Threading.CancellationToken instance is equal to the
        specified object.
        
        :param other: The other object to which to compare this instance.
        :returns: True if  is a System.Threading.CancellationToken and if the two instances are equal; otherwise, false. Two tokens are equal if they are associated with the same System.Threading.CancellationTokenSource or if they were both constructed from public CancellationToken constructors and their IsCancellationRequested values are equal.
        """
        ...

    def GetHashCode(self) -> int:
        """
        Serves as a hash function for a System.Threading.CancellationToken.
        
        :returns: A hash code for the current System.Threading.CancellationToken instance.
        """
        ...

    @overload
    def Register(self, callback: typing.Callable[[], None]) -> System.Threading.CancellationTokenRegistration:
        """
        Registers a delegate that will be called when this System.Threading.CancellationToken is canceled.
        
        :param callback: The delegate to be executed when the System.Threading.CancellationToken is canceled.
        :returns: The System.Threading.CancellationTokenRegistration instance that can be used to unregister the callback.
        """
        ...

    @overload
    def Register(self, callback: typing.Callable[[], None], useSynchronizationContext: bool) -> System.Threading.CancellationTokenRegistration:
        """
        Registers a delegate that will be called when this
        System.Threading.CancellationToken is canceled.
        
        :param callback: The delegate to be executed when the System.Threading.CancellationToken is canceled.
        :param useSynchronizationContext: A Boolean value that indicates whether to capture the current System.Threading.SynchronizationContext and use it when invoking the .
        :returns: The System.Threading.CancellationTokenRegistration instance that can be used to unregister the callback.
        """
        ...

    @overload
    def Register(self, callback: typing.Callable[[System.Object], None], state: typing.Any) -> System.Threading.CancellationTokenRegistration:
        """
        Registers a delegate that will be called when this
        System.Threading.CancellationToken is canceled.
        
        :param callback: The delegate to be executed when the System.Threading.CancellationToken is canceled.
        :param state: The state to pass to the  when the delegate is invoked.  This may be null.
        :returns: The System.Threading.CancellationTokenRegistration instance that can be used to unregister the callback.
        """
        ...

    @overload
    def Register(self, callback: typing.Callable[[System.Object, System.Threading.CancellationToken], None], state: typing.Any) -> System.Threading.CancellationTokenRegistration:
        """
        Registers a delegate that will be called when this CancellationToken is canceled.
        
        :param callback: The delegate to be executed when the System.Threading.CancellationToken is canceled.
        :param state: The state to pass to the  when the delegate is invoked.  This may be null.
        :returns: The CancellationTokenRegistration instance that can be used to unregister the callback.
        """
        ...

    @overload
    def Register(self, callback: typing.Callable[[System.Object], None], state: typing.Any, useSynchronizationContext: bool) -> System.Threading.CancellationTokenRegistration:
        """
        Registers a delegate that will be called when this
        System.Threading.CancellationToken is canceled.
        
        :param callback: The delegate to be executed when the System.Threading.CancellationToken is canceled.
        :param state: The state to pass to the  when the delegate is invoked.  This may be null.
        :param useSynchronizationContext: A Boolean value that indicates whether to capture the current System.Threading.SynchronizationContext and use it when invoking the .
        :returns: The System.Threading.CancellationTokenRegistration instance that can be used to unregister the callback.
        """
        ...

    def ThrowIfCancellationRequested(self) -> None:
        """
        Throws a System.OperationCanceledException if
        this token has had cancellation requested.
        """
        ...

    @overload
    def UnsafeRegister(self, callback: typing.Callable[[System.Object], None], state: typing.Any) -> System.Threading.CancellationTokenRegistration:
        """
        Registers a delegate that will be called when this
        System.Threading.CancellationToken is canceled.
        
        :param callback: The delegate to be executed when the System.Threading.CancellationToken is canceled.
        :param state: The state to pass to the  when the delegate is invoked.  This may be null.
        :returns: The System.Threading.CancellationTokenRegistration instance that can be used to unregister the callback.
        """
        ...

    @overload
    def UnsafeRegister(self, callback: typing.Callable[[System.Object, System.Threading.CancellationToken], None], state: typing.Any) -> System.Threading.CancellationTokenRegistration:
        """
        Registers a delegate that will be called when this CancellationToken is canceled.
        
        :param callback: The delegate to be executed when the System.Threading.CancellationToken is canceled.
        :param state: The state to pass to the  when the delegate is invoked.  This may be null.
        :returns: The CancellationTokenRegistration instance that can be used to unregister the callback.
        """
        ...


class AsyncFlowControl(System.IEquatable[System_Threading_AsyncFlowControl], System.IDisposable):
    """This class has no documentation."""

    def Dispose(self) -> None:
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def Equals(self, obj: System.Threading.AsyncFlowControl) -> bool:
        ...

    def GetHashCode(self) -> int:
        ...

    def Undo(self) -> None:
        ...


class ExecutionContext(System.Object, System.IDisposable, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    Default: System.Threading.ExecutionContext = ...

    @property
    def HasChangeNotifications(self) -> bool:
        ...

    @property
    def IsDefault(self) -> bool:
        ...

    @staticmethod
    def Capture() -> System.Threading.ExecutionContext:
        ...

    def CreateCopy(self) -> System.Threading.ExecutionContext:
        ...

    def Dispose(self) -> None:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    @staticmethod
    def IsFlowSuppressed() -> bool:
        ...

    @staticmethod
    def Restore(executionContext: System.Threading.ExecutionContext) -> None:
        """
        Restores a captured execution context to on the current thread.
        
        :param executionContext: The ExecutionContext to set.
        """
        ...

    @staticmethod
    def RestoreFlow() -> None:
        ...

    @staticmethod
    def Run(executionContext: System.Threading.ExecutionContext, callback: typing.Callable[[System.Object], None], state: typing.Any) -> None:
        ...

    @staticmethod
    def SuppressFlow() -> System.Threading.AsyncFlowControl:
        ...


class SynchronizationContext(System.Object):
    """This class has no documentation."""

    Current: System.Threading.SynchronizationContext

    def __init__(self) -> None:
        ...

    def CreateCopy(self) -> System.Threading.SynchronizationContext:
        ...

    def IsWaitNotificationRequired(self) -> bool:
        ...

    def OperationCompleted(self) -> None:
        """Optional override for subclasses, for responding to notification that operation has completed."""
        ...

    def OperationStarted(self) -> None:
        """Optional override for subclasses, for responding to notification that operation is starting."""
        ...

    def Post(self, d: typing.Callable[[System.Object], None], state: typing.Any) -> None:
        ...

    def Send(self, d: typing.Callable[[System.Object], None], state: typing.Any) -> None:
        ...

    @staticmethod
    def SetSynchronizationContext(syncContext: System.Threading.SynchronizationContext) -> None:
        ...

    def SetWaitNotificationRequired(self) -> None:
        """This method is protected."""
        ...

    def Wait(self, waitHandles: typing.List[System.IntPtr], waitAll: bool, millisecondsTimeout: int) -> int:
        ...

    @staticmethod
    def WaitHelper(waitHandles: typing.List[System.IntPtr], waitAll: bool, millisecondsTimeout: int) -> int:
        """This method is protected."""
        ...


class ApartmentState(System.Enum):
    """This class has no documentation."""

    STA = 0

    MTA = 1

    Unknown = 2


class CompressedStack(System.Object, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    @staticmethod
    def Capture() -> System.Threading.CompressedStack:
        ...

    def CreateCopy(self) -> System.Threading.CompressedStack:
        ...

    @staticmethod
    def GetCompressedStack() -> System.Threading.CompressedStack:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    @staticmethod
    def Run(compressedStack: System.Threading.CompressedStack, callback: typing.Callable[[System.Object], None], state: typing.Any) -> None:
        ...


class Thread(System.Runtime.ConstrainedExecution.CriticalFinalizerObject):
    """This class has no documentation."""

    IsThreadStartSupported: bool

    IsInternalThreadStartSupported: bool

    @property
    def CurrentCulture(self) -> System.Globalization.CultureInfo:
        ...

    @CurrentCulture.setter
    def CurrentCulture(self, value: System.Globalization.CultureInfo):
        ...

    @property
    def CurrentUICulture(self) -> System.Globalization.CultureInfo:
        ...

    @CurrentUICulture.setter
    def CurrentUICulture(self, value: System.Globalization.CultureInfo):
        ...

    CurrentPrincipal: System.Security.Principal.IPrincipal

    CurrentThread: System.Threading.Thread

    CurrentOSThreadId: int

    @property
    def ExecutionContext(self) -> System.Threading.ExecutionContext:
        ...

    @property
    def Name(self) -> str:
        ...

    @Name.setter
    def Name(self, value: str):
        ...

    @property
    def ApartmentState(self) -> int:
        """
        This property contains the int value of a member of the System.Threading.ApartmentState enum.
        
        The ApartmentState property has been deprecated. Use GetApartmentState, SetApartmentState or TrySetApartmentState instead.
        """
        warnings.warn("The ApartmentState property has been deprecated. Use GetApartmentState, SetApartmentState or TrySetApartmentState instead.", DeprecationWarning)

    @ApartmentState.setter
    def ApartmentState(self, value: int):
        """
        This property contains the int value of a member of the System.Threading.ApartmentState enum.
        
        The ApartmentState property has been deprecated. Use GetApartmentState, SetApartmentState or TrySetApartmentState instead.
        """
        warnings.warn("The ApartmentState property has been deprecated. Use GetApartmentState, SetApartmentState or TrySetApartmentState instead.", DeprecationWarning)

    @property
    def thread_id(self) -> int:
        ...

    @thread_id.setter
    def thread_id(self, value: int):
        ...

    @property
    def threadpool_thread(self) -> bool:
        ...

    @threadpool_thread.setter
    def threadpool_thread(self, value: bool):
        ...

    @property
    def apartment_state(self) -> int:
        ...

    @apartment_state.setter
    def apartment_state(self, value: int):
        ...

    @property
    def managed_id(self) -> int:
        ...

    @managed_id.setter
    def managed_id(self, value: int):
        ...

    @property
    def _executionContext(self) -> System.Threading.ExecutionContext:
        ...

    @_executionContext.setter
    def _executionContext(self, value: System.Threading.ExecutionContext):
        ...

    @property
    def _synchronizationContext(self) -> System.Threading.SynchronizationContext:
        ...

    @_synchronizationContext.setter
    def _synchronizationContext(self, value: System.Threading.SynchronizationContext):
        ...

    @property
    def IsAlive(self) -> bool:
        ...

    @property
    def IsBackground(self) -> bool:
        ...

    @IsBackground.setter
    def IsBackground(self, value: bool):
        ...

    @property
    def IsThreadPoolThread(self) -> bool:
        ...

    @IsThreadPoolThread.setter
    def IsThreadPoolThread(self, value: bool):
        ...

    @property
    def ManagedThreadId(self) -> int:
        ...

    OptimalMaxSpinWaitsPerSpinIteration: int

    @property
    def Priority(self) -> int:
        """This property contains the int value of a member of the System.Threading.ThreadPriority enum."""
        ...

    @Priority.setter
    def Priority(self, value: int):
        """This property contains the int value of a member of the System.Threading.ThreadPriority enum."""
        ...

    @property
    def ThreadState(self) -> int:
        """This property contains the int value of a member of the System.Threading.ThreadState enum."""
        ...

    @overload
    def __init__(self, start: typing.Callable[[], None]) -> None:
        ...

    @overload
    def __init__(self, start: typing.Callable[[], None], maxStackSize: int) -> None:
        ...

    @overload
    def __init__(self, start: typing.Callable[[System.Object], None]) -> None:
        ...

    @overload
    def __init__(self, start: typing.Callable[[System.Object], None], maxStackSize: int) -> None:
        ...

    @overload
    def Abort(self) -> None:
        """Obsoletions.ThreadAbortMessage"""
        ...

    @overload
    def Abort(self, stateInfo: typing.Any) -> None:
        """Obsoletions.ThreadAbortMessage"""
        ...

    @staticmethod
    def AllocateDataSlot() -> System.LocalDataStoreSlot:
        ...

    @staticmethod
    def AllocateNamedDataSlot(name: str) -> System.LocalDataStoreSlot:
        ...

    @staticmethod
    def BeginCriticalRegion() -> None:
        ...

    @staticmethod
    def BeginThreadAffinity() -> None:
        ...

    def DisableComObjectEagerCleanup(self) -> None:
        ...

    @staticmethod
    def EndCriticalRegion() -> None:
        ...

    @staticmethod
    def EndThreadAffinity() -> None:
        ...

    @staticmethod
    def FreeNamedDataSlot(name: str) -> None:
        ...

    def GetApartmentState(self) -> int:
        """:returns: This method returns the int value of a member of the System.Threading.ApartmentState enum."""
        ...

    def GetCompressedStack(self) -> System.Threading.CompressedStack:
        """Obsoletions.CodeAccessSecurityMessage"""
        warnings.warn("Obsoletions.CodeAccessSecurityMessage", DeprecationWarning)

    @staticmethod
    def GetCurrentProcessorId() -> int:
        ...

    @staticmethod
    def GetData(slot: System.LocalDataStoreSlot) -> System.Object:
        ...

    @staticmethod
    def GetDomain() -> System.AppDomain:
        ...

    @staticmethod
    def GetDomainID() -> int:
        ...

    def GetHashCode(self) -> int:
        ...

    @staticmethod
    def GetNamedDataSlot(name: str) -> System.LocalDataStoreSlot:
        ...

    def Interrupt(self) -> None:
        ...

    @overload
    def Join(self) -> None:
        ...

    @overload
    def Join(self, timeout: datetime.timedelta) -> bool:
        ...

    @overload
    def Join(self, millisecondsTimeout: int) -> bool:
        ...

    @staticmethod
    def MemoryBarrier() -> None:
        ...

    @staticmethod
    def ResetAbort() -> None:
        """Obsoletions.ThreadResetAbortMessage"""
        warnings.warn("Obsoletions.ThreadResetAbortMessage", DeprecationWarning)

    def Resume(self) -> None:
        """Thread.Resume has been deprecated. Use other classes in System.Threading, such as Monitor, Mutex, Event, and Semaphore, to synchronize Threads or protect resources."""
        warnings.warn("Thread.Resume has been deprecated. Use other classes in System.Threading, such as Monitor, Mutex, Event, and Semaphore, to synchronize Threads or protect resources.", DeprecationWarning)

    def SetApartmentState(self, state: System.Threading.ApartmentState) -> None:
        ...

    def SetCompressedStack(self, stack: System.Threading.CompressedStack) -> None:
        """Obsoletions.CodeAccessSecurityMessage"""
        warnings.warn("Obsoletions.CodeAccessSecurityMessage", DeprecationWarning)

    @staticmethod
    def SetData(slot: System.LocalDataStoreSlot, data: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def Sleep(millisecondsTimeout: int) -> None:
        ...

    @staticmethod
    @overload
    def Sleep(timeout: datetime.timedelta) -> None:
        ...

    @staticmethod
    def SpinWait(iterations: int) -> None:
        ...

    @overload
    def Start(self, parameter: typing.Any) -> None:
        """
        Causes the operating system to change the state of the current instance to ThreadState.Running, and optionally supplies an object containing data to be used by the method the thread executes.
        
        :param parameter: An object that contains data to be used by the method the thread executes.
        """
        ...

    @overload
    def Start(self) -> None:
        """Causes the operating system to change the state of the current instance to ThreadState.Running."""
        ...

    def Suspend(self) -> None:
        """Thread.Suspend has been deprecated. Use other classes in System.Threading, such as Monitor, Mutex, Event, and Semaphore, to synchronize Threads or protect resources."""
        warnings.warn("Thread.Suspend has been deprecated. Use other classes in System.Threading, such as Monitor, Mutex, Event, and Semaphore, to synchronize Threads or protect resources.", DeprecationWarning)

    @overload
    def ThreadNameChanged(self, value: str) -> None:
        ...

    @overload
    def ThreadNameChanged(self, value: str) -> None:
        ...

    def TrySetApartmentState(self, state: System.Threading.ApartmentState) -> bool:
        ...

    @overload
    def UnsafeStart(self, parameter: typing.Any) -> None:
        """
        Causes the operating system to change the state of the current instance to ThreadState.Running, and optionally supplies an object containing data to be used by the method the thread executes.
        
        :param parameter: An object that contains data to be used by the method the thread executes.
        """
        ...

    @overload
    def UnsafeStart(self) -> None:
        """Causes the operating system to change the state of the current instance to ThreadState.Running."""
        ...

    @staticmethod
    @overload
    def VolatileRead(address: int) -> int:
        ...

    @staticmethod
    @overload
    def VolatileRead(address: float) -> float:
        ...

    @staticmethod
    @overload
    def VolatileRead(address: int) -> int:
        ...

    @staticmethod
    @overload
    def VolatileRead(address: int) -> int:
        ...

    @staticmethod
    @overload
    def VolatileRead(address: int) -> int:
        ...

    @staticmethod
    @overload
    def VolatileRead(address: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def VolatileRead(address: typing.Any) -> System.Object:
        ...

    @staticmethod
    @overload
    def VolatileRead(address: int) -> int:
        ...

    @staticmethod
    @overload
    def VolatileRead(address: float) -> float:
        ...

    @staticmethod
    @overload
    def VolatileRead(address: int) -> int:
        ...

    @staticmethod
    @overload
    def VolatileRead(address: int) -> int:
        ...

    @staticmethod
    @overload
    def VolatileRead(address: int) -> int:
        ...

    @staticmethod
    @overload
    def VolatileRead(address: System.UIntPtr) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def VolatileWrite(address: int, value: int) -> None:
        ...

    @staticmethod
    @overload
    def VolatileWrite(address: float, value: float) -> None:
        ...

    @staticmethod
    @overload
    def VolatileWrite(address: int, value: int) -> None:
        ...

    @staticmethod
    @overload
    def VolatileWrite(address: int, value: int) -> None:
        ...

    @staticmethod
    @overload
    def VolatileWrite(address: int, value: int) -> None:
        ...

    @staticmethod
    @overload
    def VolatileWrite(address: System.IntPtr, value: System.IntPtr) -> None:
        ...

    @staticmethod
    @overload
    def VolatileWrite(address: typing.Any, value: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def VolatileWrite(address: int, value: int) -> None:
        ...

    @staticmethod
    @overload
    def VolatileWrite(address: float, value: float) -> None:
        ...

    @staticmethod
    @overload
    def VolatileWrite(address: int, value: int) -> None:
        ...

    @staticmethod
    @overload
    def VolatileWrite(address: int, value: int) -> None:
        ...

    @staticmethod
    @overload
    def VolatileWrite(address: int, value: int) -> None:
        ...

    @staticmethod
    @overload
    def VolatileWrite(address: System.UIntPtr, value: System.UIntPtr) -> None:
        ...

    @staticmethod
    def Yield() -> bool:
        ...


class SemaphoreFullException(System.SystemException):
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

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...


class LockRecursionPolicy(System.Enum):
    """This class has no documentation."""

    NoRecursion = 0

    SupportsRecursion = 1


class ReaderWriterLockSlim(System.Object, System.IDisposable):
    """
    A reader-writer lock implementation that is intended to be simple, yet very
    efficient.  In particular only 1 interlocked operation is taken for any lock
    operation (we use spin locks to achieve this).  The spin lock is never held
    for more than a few instructions (in particular, we never call event APIs
    or in fact any non-trivial API while holding the spin lock).
    """

    @property
    def IsReadLockHeld(self) -> bool:
        ...

    @property
    def IsUpgradeableReadLockHeld(self) -> bool:
        ...

    @property
    def IsWriteLockHeld(self) -> bool:
        ...

    @property
    def RecursionPolicy(self) -> int:
        """This property contains the int value of a member of the System.Threading.LockRecursionPolicy enum."""
        ...

    @property
    def CurrentReadCount(self) -> int:
        ...

    @property
    def RecursiveReadCount(self) -> int:
        ...

    @property
    def RecursiveUpgradeCount(self) -> int:
        ...

    @property
    def RecursiveWriteCount(self) -> int:
        ...

    @property
    def WaitingReadCount(self) -> int:
        ...

    @property
    def WaitingUpgradeCount(self) -> int:
        ...

    @property
    def WaitingWriteCount(self) -> int:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, recursionPolicy: System.Threading.LockRecursionPolicy) -> None:
        ...

    def Dispose(self) -> None:
        ...

    def EnterReadLock(self) -> None:
        ...

    def EnterUpgradeableReadLock(self) -> None:
        ...

    def EnterWriteLock(self) -> None:
        ...

    def ExitReadLock(self) -> None:
        ...

    def ExitUpgradeableReadLock(self) -> None:
        ...

    def ExitWriteLock(self) -> None:
        ...

    @overload
    def TryEnterReadLock(self, timeout: datetime.timedelta) -> bool:
        ...

    @overload
    def TryEnterReadLock(self, millisecondsTimeout: int) -> bool:
        ...

    @overload
    def TryEnterUpgradeableReadLock(self, timeout: datetime.timedelta) -> bool:
        ...

    @overload
    def TryEnterUpgradeableReadLock(self, millisecondsTimeout: int) -> bool:
        ...

    @overload
    def TryEnterWriteLock(self, timeout: datetime.timedelta) -> bool:
        ...

    @overload
    def TryEnterWriteLock(self, millisecondsTimeout: int) -> bool:
        ...


class PreAllocatedOverlapped(System.Object, System.IDisposable, System.Threading.IDeferredDisposable):
    """Represents pre-allocated state for native overlapped I/O operations."""

    @property
    def _overlapped(self) -> System.Threading.ThreadPoolBoundHandleOverlapped:
        ...

    @overload
    def __init__(self, callback: typing.Callable[[int, int, typing.Any], None], state: typing.Any, pinData: typing.Any) -> None:
        """
        Initializes a new instance of the PreAllocatedOverlapped class, specifying
            a delegate that is invoked when each asynchronous I/O operation is complete, a user-provided
            object providing context, and managed objects that serve as buffers.
        
        :param callback: An IOCompletionCallback delegate that represents the callback method     invoked when each asynchronous I/O operation completes.
        :param state: A user-provided object that distinguishes NativeOverlapped instance produced from this     object from other NativeOverlapped instances. Can be null.
        :param pinData: An object or array of objects representing the input or output buffer for the operations. Each     object represents a buffer, for example an array of bytes.  Can be null.
        """
        ...

    @overload
    def __init__(self, callback: typing.Callable[[int, int, typing.Any], None], state: typing.Any, pinData: typing.Any) -> None:
        ...

    @overload
    def Dispose(self) -> None:
        """Frees the resources associated with this PreAllocatedOverlapped instance."""
        ...

    @overload
    def Dispose(self) -> None:
        ...

    def OnFinalRelease(self, disposed: bool) -> None:
        ...

    @staticmethod
    @overload
    def UnsafeCreate(callback: typing.Callable[[int, int, typing.Any], None], state: typing.Any, pinData: typing.Any) -> System.Threading.PreAllocatedOverlapped:
        """
        Initializes a new instance of the PreAllocatedOverlapped class, specifying
            a delegate that is invoked when each asynchronous I/O operation is complete, a user-provided
            object providing context, and managed objects that serve as buffers.
        
        :param callback: An IOCompletionCallback delegate that represents the callback method     invoked when each asynchronous I/O operation completes.
        :param state: A user-provided object that distinguishes NativeOverlapped instance produced from this     object from other NativeOverlapped instances. Can be null.
        :param pinData: An object or array of objects representing the input or output buffer for the operations. Each     object represents a buffer, for example an array of bytes.  Can be null.
        """
        ...

    @staticmethod
    @overload
    def UnsafeCreate(callback: typing.Callable[[int, int, typing.Any], None], state: typing.Any, pinData: typing.Any) -> System.Threading.PreAllocatedOverlapped:
        ...


class ThreadPoolBoundHandle(System.Object, System.IDisposable):
    """This class has no documentation."""

    @property
    def Handle(self) -> System.Runtime.InteropServices.SafeHandle:
        """Gets the bound operating system handle."""
        ...

    @overload
    def AllocateNativeOverlapped(self, callback: typing.Callable[[int, int, typing.Any], None], state: typing.Any, pinData: typing.Any) -> typing.Any:
        """
        Returns an unmanaged pointer to a NativeOverlapped structure, specifying
            a delegate that is invoked when the asynchronous I/O operation is complete, a user-provided
            object providing context, and managed objects that serve as buffers.
        
        :param callback: An IOCompletionCallback delegate that represents the callback method     invoked when the asynchronous I/O operation completes.
        :param state: A user-provided object that distinguishes this NativeOverlapped from other     NativeOverlapped instances. Can be null.
        :param pinData: An object or array of objects representing the input or output buffer for the operation. Each     object represents a buffer, for example an array of bytes.  Can be null.
        :returns: An unmanaged pointer to a NativeOverlapped structure.
        """
        ...

    @overload
    def AllocateNativeOverlapped(self, preAllocated: System.Threading.PreAllocatedOverlapped) -> typing.Any:
        """
        Returns an unmanaged pointer to a NativeOverlapped structure, using the callback,
            state, and buffers associated with the specified PreAllocatedOverlapped object.
        
        :param preAllocated: A PreAllocatedOverlapped object from which to create the NativeOverlapped pointer.
        :returns: An unmanaged pointer to a NativeOverlapped structure.
        """
        ...

    @overload
    def AllocateNativeOverlapped(self, callback: typing.Callable[[int, int, typing.Any], None], state: typing.Any, pinData: typing.Any) -> typing.Any:
        ...

    @overload
    def AllocateNativeOverlapped(self, preAllocated: System.Threading.PreAllocatedOverlapped) -> typing.Any:
        ...

    @staticmethod
    @overload
    def BindHandle(handle: System.Runtime.InteropServices.SafeHandle) -> System.Threading.ThreadPoolBoundHandle:
        """
        Returns a ThreadPoolBoundHandle for the specific handle,
            which is bound to the system thread pool.
        
        :param handle: A SafeHandle object that holds the operating system handle. The     handle must have been opened for overlapped I/O on the unmanaged side.
        :returns: ThreadPoolBoundHandle for , which     is bound to the system thread pool.
        """
        ...

    @staticmethod
    @overload
    def BindHandle(handle: System.Runtime.InteropServices.SafeHandle) -> System.Threading.ThreadPoolBoundHandle:
        ...

    @overload
    def Dispose(self) -> None:
        ...

    @overload
    def Dispose(self) -> None:
        ...

    @overload
    def FreeNativeOverlapped(self, overlapped: typing.Any) -> None:
        """
        Frees the unmanaged memory associated with a NativeOverlapped structure
            allocated by the AllocateNativeOverlapped method.
        
        :param overlapped: An unmanaged pointer to the NativeOverlapped structure to be freed.
        """
        ...

    @overload
    def FreeNativeOverlapped(self, overlapped: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def GetNativeOverlappedState(overlapped: typing.Any) -> System.Object:
        """
        Returns the user-provided object specified when the NativeOverlapped instance was
            allocated using the AllocateNativeOverlapped(IOCompletionCallback, object, object).
        
        :param overlapped: An unmanaged pointer to the NativeOverlapped structure from which to return the     associated user-provided object.
        :returns: A user-provided object that distinguishes this NativeOverlapped     from other NativeOverlapped instances, otherwise, null if one was     not specified when the instance was allocated using AllocateNativeOverlapped.
        """
        ...

    @staticmethod
    @overload
    def GetNativeOverlappedState(overlapped: typing.Any) -> System.Object:
        ...

    @overload
    def UnsafeAllocateNativeOverlapped(self, callback: typing.Callable[[int, int, typing.Any], None], state: typing.Any, pinData: typing.Any) -> typing.Any:
        """
        Returns an unmanaged pointer to a NativeOverlapped structure, specifying
            a delegate that is invoked when the asynchronous I/O operation is complete, a user-provided
            object providing context, and managed objects that serve as buffers.
        
        :param callback: An IOCompletionCallback delegate that represents the callback method     invoked when the asynchronous I/O operation completes.
        :param state: A user-provided object that distinguishes this NativeOverlapped from other     NativeOverlapped instances. Can be null.
        :param pinData: An object or array of objects representing the input or output buffer for the operation. Each     object represents a buffer, for example an array of bytes.  Can be null.
        :returns: An unmanaged pointer to a NativeOverlapped structure.
        """
        ...

    @overload
    def UnsafeAllocateNativeOverlapped(self, callback: typing.Callable[[int, int, typing.Any], None], state: typing.Any, pinData: typing.Any) -> typing.Any:
        ...


class AsyncLocalValueChangedArgs(typing.Generic[System_Threading_AsyncLocalValueChangedArgs_T]):
    """The class that provides data change information to AsyncLocal{T} instances that register for change notifications."""

    @property
    def PreviousValue(self) -> System_Threading_AsyncLocalValueChangedArgs_T:
        """Gets the data's previous value."""
        ...

    @property
    def CurrentValue(self) -> System_Threading_AsyncLocalValueChangedArgs_T:
        """Gets the data's current value."""
        ...

    @property
    def ThreadContextChanged(self) -> bool:
        """Returns a value that indicates whether the value changes because of a change of execution context."""
        ...


class AsyncLocal(typing.Generic[System_Threading_AsyncLocal_T], System.Object, System.Threading.IAsyncLocal):
    """Represents ambient data that is local to a given asynchronous control flow, such as an asynchronous method."""

    @property
    def Value(self) -> System_Threading_AsyncLocal_T:
        """Gets or sets the value of the ambient data."""
        ...

    @Value.setter
    def Value(self, value: System_Threading_AsyncLocal_T):
        """Gets or sets the value of the ambient data."""
        ...

    @overload
    def __init__(self) -> None:
        """Instantiates an AsyncLocal{T} instance that does not receive change notifications."""
        ...

    @overload
    def __init__(self, valueChangedHandler: typing.Callable[[System.Threading.AsyncLocalValueChangedArgs[System_Threading_AsyncLocal_T]], None]) -> None:
        """
        Instantiates an AsyncLocal{T} instance that receives change notifications.
        
        :param valueChangedHandler: The delegate that is called whenever the current value changes on any thread.
        """
        ...

    def OnValueChanged(self, previousValueObj: typing.Any, currentValueObj: typing.Any, contextChanged: bool) -> None:
        ...


class ManualResetEventSlim(System.Object, System.IDisposable):
    """This class has no documentation."""

    @property
    def WaitHandle(self) -> System.Threading.WaitHandle:
        ...

    @property
    def IsSet(self) -> bool:
        """Gets whether the event is set."""
        ...

    @IsSet.setter
    def IsSet(self, value: bool):
        """Gets whether the event is set."""
        ...

    @property
    def SpinCount(self) -> int:
        """Gets the number of spin waits that will be occur before falling back to a true wait."""
        ...

    @SpinCount.setter
    def SpinCount(self, value: int):
        """Gets the number of spin waits that will be occur before falling back to a true wait."""
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, initialState: bool) -> None:
        """
        Initializes a new instance of the ManualResetEventSlim
        class with a boolean value indicating whether to set the initial state to signaled.
        
        :param initialState: true to set the initial state signaled; false to set the initial state to nonsignaled.
        """
        ...

    @overload
    def __init__(self, initialState: bool, spinCount: int) -> None:
        """
        Initializes a new instance of the ManualResetEventSlim
        class with a Boolean value indicating whether to set the initial state to signaled and a specified
        spin count.
        
        :param initialState: true to set the initial state to signaled; false to set the initial state to nonsignaled.
        :param spinCount: The number of spin waits that will occur before falling back to a true wait.
        """
        ...

    @overload
    def Dispose(self) -> None:
        """Releases all resources used by the current instance of ManualResetEventSlim."""
        ...

    @overload
    def Dispose(self, disposing: bool) -> None:
        """
        When overridden in a derived class, releases the unmanaged resources used by the
        ManualResetEventSlim, and optionally releases the managed resources.
        
        This method is protected.
        
        :param disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        ...

    def Reset(self) -> None:
        """Sets the state of the event to nonsignaled, which causes threads to block."""
        ...

    def Set(self) -> None:
        """
        Sets the state of the event to signaled, which allows one or more threads waiting on the event to
        proceed.
        """
        ...

    @overload
    def Wait(self) -> None:
        """Blocks the current thread until the current ManualResetEventSlim is set."""
        ...

    @overload
    def Wait(self, cancellationToken: System.Threading.CancellationToken) -> None:
        """
        Blocks the current thread until the current ManualResetEventSlim receives a signal,
        while observing a System.Threading.CancellationToken.
        
        :param cancellationToken: The System.Threading.CancellationToken to observe.
        """
        ...

    @overload
    def Wait(self, timeout: datetime.timedelta) -> bool:
        """
        Blocks the current thread until the current ManualResetEventSlim is set, using a
        System.TimeSpan to measure the time interval.
        
        :param timeout: A System.TimeSpan that represents the number of milliseconds to wait, or a System.TimeSpan that represents -1 milliseconds to wait indefinitely.
        :returns: true if the System.Threading.ManualResetEventSlim was set; otherwise, false.
        """
        ...

    @overload
    def Wait(self, timeout: datetime.timedelta, cancellationToken: System.Threading.CancellationToken) -> bool:
        """
        Blocks the current thread until the current ManualResetEventSlim is set, using a
        System.TimeSpan to measure the time interval, while observing a System.Threading.CancellationToken.
        
        :param timeout: A System.TimeSpan that represents the number of milliseconds to wait, or a System.TimeSpan that represents -1 milliseconds to wait indefinitely.
        :param cancellationToken: The System.Threading.CancellationToken to observe.
        :returns: true if the System.Threading.ManualResetEventSlim was set; otherwise, false.
        """
        ...

    @overload
    def Wait(self, millisecondsTimeout: int) -> bool:
        """
        Blocks the current thread until the current ManualResetEventSlim is set, using a
        32-bit signed integer to measure the time interval.
        
        :param millisecondsTimeout: The number of milliseconds to wait, or Timeout.Infinite(-1) to wait indefinitely.
        :returns: true if the System.Threading.ManualResetEventSlim was set; otherwise, false.
        """
        ...

    @overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: System.Threading.CancellationToken) -> bool:
        """
        Blocks the current thread until the current ManualResetEventSlim is set, using a
        32-bit signed integer to measure the time interval, while observing a System.Threading.CancellationToken.
        
        :param millisecondsTimeout: The number of milliseconds to wait, or Timeout.Infinite(-1) to wait indefinitely.
        :param cancellationToken: The System.Threading.CancellationToken to observe.
        :returns: true if the System.Threading.ManualResetEventSlim was set; otherwise, false.
        """
        ...


class Mutex(System.Threading.WaitHandle):
    """Synchronization primitive that can also be used for interprocess synchronization"""

    @overload
    def __init__(self, initiallyOwned: bool, name: str, createdNew: typing.Optional[bool]) -> typing.Union[None, bool]:
        ...

    @overload
    def __init__(self, initiallyOwned: bool, name: str) -> None:
        ...

    @overload
    def __init__(self, initiallyOwned: bool) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @staticmethod
    def OpenExisting(name: str) -> System.Threading.Mutex:
        ...

    @overload
    def ReleaseMutex(self) -> None:
        ...

    @overload
    def ReleaseMutex(self) -> None:
        ...

    @staticmethod
    def TryOpenExisting(name: str, result: typing.Optional[System.Threading.Mutex]) -> typing.Union[bool, System.Threading.Mutex]:
        ...


class ThreadState(System.Enum):
    """This class has no documentation."""

    Running = 0

    StopRequested = 1

    SuspendRequested = 2

    Background = 4

    Unstarted = 8

    Stopped = 16

    WaitSleepJoin = 32

    Suspended = 64

    AbortRequested = 128

    Aborted = 256


class Volatile(System.Object):
    """Methods for accessing memory with volatile semantics."""

    @staticmethod
    @overload
    def Read(location: bool) -> bool:
        ...

    @staticmethod
    @overload
    def Read(location: int) -> int:
        ...

    @staticmethod
    @overload
    def Read(location: float) -> float:
        ...

    @staticmethod
    @overload
    def Read(location: int) -> int:
        ...

    @staticmethod
    @overload
    def Read(location: int) -> int:
        ...

    @staticmethod
    @overload
    def Read(location: int) -> int:
        ...

    @staticmethod
    @overload
    def Read(location: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def Read(location: int) -> int:
        ...

    @staticmethod
    @overload
    def Read(location: float) -> float:
        ...

    @staticmethod
    @overload
    def Read(location: int) -> int:
        ...

    @staticmethod
    @overload
    def Read(location: int) -> int:
        ...

    @staticmethod
    @overload
    def Read(location: int) -> int:
        ...

    @staticmethod
    @overload
    def Read(location: System.UIntPtr) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def Read(location: System_Threading_Volatile_Read_T) -> System_Threading_Volatile_Read_T:
        ...

    @staticmethod
    @overload
    def Write(location: bool, value: bool) -> None:
        ...

    @staticmethod
    @overload
    def Write(location: int, value: int) -> None:
        ...

    @staticmethod
    @overload
    def Write(location: float, value: float) -> None:
        ...

    @staticmethod
    @overload
    def Write(location: int, value: int) -> None:
        ...

    @staticmethod
    @overload
    def Write(location: int, value: int) -> None:
        ...

    @staticmethod
    @overload
    def Write(location: int, value: int) -> None:
        ...

    @staticmethod
    @overload
    def Write(location: System.IntPtr, value: System.IntPtr) -> None:
        ...

    @staticmethod
    @overload
    def Write(location: int, value: int) -> None:
        ...

    @staticmethod
    @overload
    def Write(location: float, value: float) -> None:
        ...

    @staticmethod
    @overload
    def Write(location: int, value: int) -> None:
        ...

    @staticmethod
    @overload
    def Write(location: int, value: int) -> None:
        ...

    @staticmethod
    @overload
    def Write(location: int, value: int) -> None:
        ...

    @staticmethod
    @overload
    def Write(location: System.UIntPtr, value: System.UIntPtr) -> None:
        ...

    @staticmethod
    @overload
    def Write(location: System_Threading_Volatile_Write_T, value: System_Threading_Volatile_Write_T) -> None:
        ...


class WaitHandleCannotBeOpenedException(System.ApplicationException):
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

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...


class SpinLock:
    """
    Provides a mutual exclusion lock primitive where a thread trying to acquire the lock waits in a loop
    repeatedly checking until the lock becomes available.
    """

    @property
    def IsHeld(self) -> bool:
        """Gets whether the lock is currently held by any thread."""
        ...

    @property
    def IsHeldByCurrentThread(self) -> bool:
        """Gets whether the lock is currently held by any thread."""
        ...

    @property
    def IsThreadOwnerTrackingEnabled(self) -> bool:
        """Gets whether thread ownership tracking is enabled for this instance."""
        ...

    def __init__(self, enableThreadOwnerTracking: bool) -> None:
        """
        Initializes a new instance of the System.Threading.SpinLock
        structure with the option to track thread IDs to improve debugging.
        
        :param enableThreadOwnerTracking: Whether to capture and use thread IDs for debugging purposes.
        """
        ...

    def Enter(self, lockTaken: bool) -> None:
        """
        Initializes a new instance of the System.Threading.SpinLock
        structure with the option to track thread IDs to improve debugging.
        
        :param lockTaken: True if the lock is acquired; otherwise, false.  must be initialized to false prior to calling this method.
        """
        ...

    @overload
    def Exit(self) -> None:
        """Releases the lock."""
        ...

    @overload
    def Exit(self, useMemoryBarrier: bool) -> None:
        """
        Releases the lock.
        
        :param useMemoryBarrier: A Boolean value that indicates whether a memory fence should be issued in order to immediately publish the exit operation to other threads.
        """
        ...

    @overload
    def TryEnter(self, lockTaken: bool) -> None:
        """
        Attempts to acquire the lock in a reliable manner, such that even if an exception occurs within
        the method call,  can be examined reliably to determine whether the
        lock was acquired.
        
        :param lockTaken: True if the lock is acquired; otherwise, false.  must be initialized to false prior to calling this method.
        """
        ...

    @overload
    def TryEnter(self, timeout: datetime.timedelta, lockTaken: bool) -> None:
        """
        Attempts to acquire the lock in a reliable manner, such that even if an exception occurs within
        the method call,  can be examined reliably to determine whether the
        lock was acquired.
        
        :param timeout: A System.TimeSpan that represents the number of milliseconds to wait, or a System.TimeSpan that represents -1 milliseconds to wait indefinitely.
        :param lockTaken: True if the lock is acquired; otherwise, false.  must be initialized to false prior to calling this method.
        """
        ...

    @overload
    def TryEnter(self, millisecondsTimeout: int, lockTaken: bool) -> None:
        """
        Attempts to acquire the lock in a reliable manner, such that even if an exception occurs within
        the method call,  can be examined reliably to determine whether the
        lock was acquired.
        
        :param millisecondsTimeout: The number of milliseconds to wait, or System.Threading.Timeout.Infinite (-1) to wait indefinitely.
        :param lockTaken: True if the lock is acquired; otherwise, false.  must be initialized to false prior to calling this method.
        """
        ...


class Semaphore(System.Threading.WaitHandle):
    """This class has no documentation."""

    @overload
    def __init__(self, initialCount: int, maximumCount: int) -> None:
        ...

    @overload
    def __init__(self, initialCount: int, maximumCount: int, name: str) -> None:
        ...

    @overload
    def __init__(self, initialCount: int, maximumCount: int, name: str, createdNew: typing.Optional[bool]) -> typing.Union[None, bool]:
        ...

    @staticmethod
    def OpenExisting(name: str) -> System.Threading.Semaphore:
        ...

    @overload
    def Release(self) -> int:
        ...

    @overload
    def Release(self, releaseCount: int) -> int:
        ...

    @staticmethod
    def TryOpenExisting(name: str, result: typing.Optional[System.Threading.Semaphore]) -> typing.Union[bool, System.Threading.Semaphore]:
        ...


class Timer(System.MarshalByRefObject, System.IDisposable, System.IAsyncDisposable):
    """This class has no documentation."""

    MaxSupportedTimeout: int = ...

    @property
    def _timer(self) -> System.Threading.TimerHolder:
        ...

    @_timer.setter
    def _timer(self, value: System.Threading.TimerHolder):
        ...

    ActiveCount: int
    """
    Gets the number of timers that are currently active. An active timer is registered to tick at some point in the
    future, and has not yet been canceled.
    """

    @overload
    def __init__(self, callback: typing.Callable[[System.Object], None], state: typing.Any, dueTime: int, period: int) -> None:
        ...

    @overload
    def __init__(self, callback: typing.Callable[[System.Object], None], state: typing.Any, dueTime: datetime.timedelta, period: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self, callback: typing.Callable[[System.Object], None], state: typing.Any, dueTime: int, period: int) -> None:
        ...

    @overload
    def __init__(self, callback: typing.Callable[[System.Object], None], state: typing.Any, dueTime: int, period: int) -> None:
        ...

    @overload
    def __init__(self, callback: typing.Callable[[System.Object], None]) -> None:
        ...

    @overload
    def Change(self, dueTime: int, period: int) -> bool:
        ...

    @overload
    def Change(self, dueTime: datetime.timedelta, period: datetime.timedelta) -> bool:
        ...

    @overload
    def Change(self, dueTime: int, period: int) -> bool:
        ...

    @overload
    def Change(self, dueTime: int, period: int) -> bool:
        ...

    @overload
    def Dispose(self, notifyObject: System.Threading.WaitHandle) -> bool:
        ...

    @overload
    def Dispose(self) -> None:
        ...

    def DisposeAsync(self) -> System.Threading.Tasks.ValueTask:
        ...


class EventResetMode(System.Enum):
    """This class has no documentation."""

    AutoReset = 0

    ManualReset = 1


class EventWaitHandle(System.Threading.WaitHandle):
    """This class has no documentation."""

    @overload
    def __init__(self, initialState: bool, mode: System.Threading.EventResetMode) -> None:
        ...

    @overload
    def __init__(self, initialState: bool, mode: System.Threading.EventResetMode, name: str) -> None:
        ...

    @overload
    def __init__(self, initialState: bool, mode: System.Threading.EventResetMode, name: str, createdNew: typing.Optional[bool]) -> typing.Union[None, bool]:
        ...

    @staticmethod
    def OpenExisting(name: str) -> System.Threading.EventWaitHandle:
        ...

    @overload
    def Reset(self) -> bool:
        ...

    @overload
    def Reset(self) -> bool:
        ...

    @overload
    def Set(self) -> bool:
        ...

    @overload
    def Set(self) -> bool:
        ...

    @staticmethod
    def TryOpenExisting(name: str, result: typing.Optional[System.Threading.EventWaitHandle]) -> typing.Union[bool, System.Threading.EventWaitHandle]:
        ...


class AutoResetEvent(System.Threading.EventWaitHandle):
    """This class has no documentation."""

    def __init__(self, initialState: bool) -> None:
        ...


class LockRecursionException(System.Exception):
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

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...


class LazyThreadSafetyMode(System.Enum):
    """Specifies how a System.Lazy{T} instance should synchronize access among multiple threads."""

    # Cannot convert to Python: None = 0
    """
    This mode makes no guarantees around the thread-safety of the System.Lazy{T} instance.  If used from multiple threads, the behavior of the System.Lazy{T} is undefined.
    This mode should be used when a System.Lazy{T} is guaranteed to never be initialized from more than one thread simultaneously and high performance is crucial.
    If valueFactory throws an exception when the System.Lazy{T} is initialized, the exception will be cached and returned on subsequent accesses to Value. Also, if valueFactory recursively
    accesses Value on this System.Lazy{T} instance, a System.InvalidOperationException will be thrown.
    """

    PublicationOnly = 1
    """
    When multiple threads attempt to simultaneously initialize a System.Lazy{T} instance, this mode allows each thread to execute the
    valueFactory but only the first thread to complete initialization will be allowed to set the final value of the  System.Lazy{T}.
    Once initialized successfully, any future calls to Value will return the cached result.  If valueFactory throws an exception on any thread, that exception will be
    propagated out of Value. If any thread executes valueFactory without throwing an exception and, therefore, successfully sets the value, that value will be returned on
    subsequent accesses to Value from any thread.  If no thread succeeds in setting the value, IsValueCreated will remain false and subsequent accesses to Value will result in
    the valueFactory delegate re-executing.  Also, if valueFactory recursively accesses Value on this  System.Lazy{T} instance, an exception will NOT be thrown.
    """

    ExecutionAndPublication = 2
    """
    This mode uses locks to ensure that only a single thread can initialize a System.Lazy{T} instance in a thread-safe manner.  In general,
    taken if this mode is used in conjunction with a System.Lazy{T} valueFactory delegate that uses locks internally, a deadlock can occur if not
    handled carefully.  If valueFactory throws an exception when theSystem.Lazy{T} is initialized, the exception will be cached and returned on
    subsequent accesses to Value. Also, if valueFactory recursively accesses Value on this System.Lazy{T} instance, a  System.InvalidOperationException will be thrown.
    """


class IThreadPoolWorkItem(metaclass=abc.ABCMeta):
    """Represents a work item that can be executed by the ThreadPool."""

    def Execute(self) -> None:
        ...


class ThreadPool(System.Object):
    """This class has no documentation."""

    YieldFromDispatchLoop: bool

    ThreadCount: int
    """Gets the number of thread pool threads that currently exist."""

    CompletedWorkItemCount: int
    """Gets the number of work items that have been processed by the thread pool so far."""

    WorkerThreadName: str = ".NET TP Worker"

    s_workQueue: System.Threading.ThreadPoolWorkQueue = ...

    s_invokeAsyncStateMachineBox: typing.Callable[[System.Object], None] = ...
    """Shim used to invoke IAsyncStateMachineBox.MoveNext of the supplied IAsyncStateMachineBox."""

    EnableWorkerTracking: bool

    PendingWorkItemCount: int
    """Gets the number of work items that are currently queued to be processed."""

    @staticmethod
    @overload
    def BindHandle(osHandle: System.Runtime.InteropServices.SafeHandle) -> bool:
        ...

    @staticmethod
    @overload
    def BindHandle(osHandle: System.Runtime.InteropServices.SafeHandle) -> bool:
        ...

    @staticmethod
    @overload
    def BindHandle(osHandle: System.Runtime.InteropServices.SafeHandle) -> bool:
        ...

    @staticmethod
    @overload
    def BindHandle(osHandle: System.IntPtr) -> bool:
        """ThreadPool.BindHandle(IntPtr) has been deprecated. Use ThreadPool.BindHandle(SafeHandle) instead."""
        ...

    @staticmethod
    @overload
    def BindHandle(osHandle: System.IntPtr) -> bool:
        """ThreadPool.BindHandle(IntPtr) has been deprecated. Use ThreadPool.BindHandle(SafeHandle) instead."""
        ...

    @staticmethod
    @overload
    def BindHandle(osHandle: System.IntPtr) -> bool:
        """ThreadPool.BindHandle(IntPtr) has been deprecated. Use ThreadPool.BindHandle(SafeHandle) instead."""
        ...

    @staticmethod
    @overload
    def GetAvailableThreads(workerThreads: typing.Optional[int], completionPortThreads: typing.Optional[int]) -> typing.Union[None, int, int]:
        ...

    @staticmethod
    @overload
    def GetAvailableThreads(workerThreads: typing.Optional[int], completionPortThreads: typing.Optional[int]) -> typing.Union[None, int, int]:
        ...

    @staticmethod
    @overload
    def GetMaxThreads(workerThreads: typing.Optional[int], completionPortThreads: typing.Optional[int]) -> typing.Union[None, int, int]:
        ...

    @staticmethod
    @overload
    def GetMaxThreads(workerThreads: typing.Optional[int], completionPortThreads: typing.Optional[int]) -> typing.Union[None, int, int]:
        ...

    @staticmethod
    @overload
    def GetMinThreads(workerThreads: typing.Optional[int], completionPortThreads: typing.Optional[int]) -> typing.Union[None, int, int]:
        ...

    @staticmethod
    @overload
    def GetMinThreads(workerThreads: typing.Optional[int], completionPortThreads: typing.Optional[int]) -> typing.Union[None, int, int]:
        ...

    @staticmethod
    @overload
    def QueueUserWorkItem(callBack: typing.Callable[[System.Object], None]) -> bool:
        ...

    @staticmethod
    @overload
    def QueueUserWorkItem(callBack: typing.Callable[[System.Object], None], state: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def QueueUserWorkItem(callBack: typing.Callable[[System_Threading_ThreadPool_QueueUserWorkItem_TState], None], state: System_Threading_ThreadPool_QueueUserWorkItem_TState, preferLocal: bool) -> bool:
        ...

    @staticmethod
    @overload
    def RegisterWaitForSingleObject(waitObject: System.Threading.WaitHandle, callBack: typing.Callable[[System.Object, bool], None], state: typing.Any, millisecondsTimeOutInterval: int, executeOnlyOnce: bool) -> System.Threading.RegisteredWaitHandle:
        ...

    @staticmethod
    @overload
    def RegisterWaitForSingleObject(waitObject: System.Threading.WaitHandle, callBack: typing.Callable[[System.Object, bool], None], state: typing.Any, millisecondsTimeOutInterval: int, executeOnlyOnce: bool) -> System.Threading.RegisteredWaitHandle:
        ...

    @staticmethod
    @overload
    def RegisterWaitForSingleObject(waitObject: System.Threading.WaitHandle, callBack: typing.Callable[[System.Object, bool], None], state: typing.Any, millisecondsTimeOutInterval: int, executeOnlyOnce: bool) -> System.Threading.RegisteredWaitHandle:
        ...

    @staticmethod
    @overload
    def RegisterWaitForSingleObject(waitObject: System.Threading.WaitHandle, callBack: typing.Callable[[System.Object, bool], None], state: typing.Any, timeout: datetime.timedelta, executeOnlyOnce: bool) -> System.Threading.RegisteredWaitHandle:
        ...

    @staticmethod
    @overload
    def SetMaxThreads(workerThreads: int, completionPortThreads: int) -> bool:
        ...

    @staticmethod
    @overload
    def SetMaxThreads(workerThreads: int, completionPortThreads: int) -> bool:
        ...

    @staticmethod
    @overload
    def SetMinThreads(workerThreads: int, completionPortThreads: int) -> bool:
        ...

    @staticmethod
    @overload
    def SetMinThreads(workerThreads: int, completionPortThreads: int) -> bool:
        ...

    @staticmethod
    @overload
    def UnsafeQueueNativeOverlapped(overlapped: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def UnsafeQueueNativeOverlapped(overlapped: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def UnsafeQueueNativeOverlapped(overlapped: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def UnsafeQueueUserWorkItem(callBack: typing.Callable[[System_Threading_ThreadPool_UnsafeQueueUserWorkItem_TState], None], state: System_Threading_ThreadPool_UnsafeQueueUserWorkItem_TState, preferLocal: bool) -> bool:
        ...

    @staticmethod
    @overload
    def UnsafeQueueUserWorkItem(callBack: typing.Callable[[System.Object], None], state: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def UnsafeQueueUserWorkItem(callBack: System.Threading.IThreadPoolWorkItem, preferLocal: bool) -> bool:
        ...

    @staticmethod
    @overload
    def UnsafeRegisterWaitForSingleObject(waitObject: System.Threading.WaitHandle, callBack: typing.Callable[[System.Object, bool], None], state: typing.Any, millisecondsTimeOutInterval: int, executeOnlyOnce: bool) -> System.Threading.RegisteredWaitHandle:
        ...

    @staticmethod
    @overload
    def UnsafeRegisterWaitForSingleObject(waitObject: System.Threading.WaitHandle, callBack: typing.Callable[[System.Object, bool], None], state: typing.Any, millisecondsTimeOutInterval: int, executeOnlyOnce: bool) -> System.Threading.RegisteredWaitHandle:
        ...

    @staticmethod
    @overload
    def UnsafeRegisterWaitForSingleObject(waitObject: System.Threading.WaitHandle, callBack: typing.Callable[[System.Object, bool], None], state: typing.Any, millisecondsTimeOutInterval: int, executeOnlyOnce: bool) -> System.Threading.RegisteredWaitHandle:
        ...

    @staticmethod
    @overload
    def UnsafeRegisterWaitForSingleObject(waitObject: System.Threading.WaitHandle, callBack: typing.Callable[[System.Object, bool], None], state: typing.Any, timeout: datetime.timedelta, executeOnlyOnce: bool) -> System.Threading.RegisteredWaitHandle:
        ...


class ThreadAbortException(System.SystemException):
    """This class has no documentation."""

    @property
    def ExceptionState(self) -> System.Object:
        ...


class SynchronizationLockException(System.SystemException):
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

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...


class Overlapped(System.Object):
    """This class has no documentation."""

    @property
    def _callback(self) -> System.Object:
        ...

    @_callback.setter
    def _callback(self, value: System.Object):
        ...

    @property
    def AsyncResult(self) -> System.IAsyncResult:
        ...

    @AsyncResult.setter
    def AsyncResult(self, value: System.IAsyncResult):
        ...

    @property
    def OffsetLow(self) -> int:
        ...

    @OffsetLow.setter
    def OffsetLow(self, value: int):
        ...

    @property
    def OffsetHigh(self) -> int:
        ...

    @OffsetHigh.setter
    def OffsetHigh(self, value: int):
        ...

    @property
    def EventHandle(self) -> int:
        """Overlapped.EventHandle is not 64-bit compatible and has been deprecated. Use EventHandleIntPtr instead."""
        warnings.warn("Overlapped.EventHandle is not 64-bit compatible and has been deprecated. Use EventHandleIntPtr instead.", DeprecationWarning)

    @EventHandle.setter
    def EventHandle(self, value: int):
        """Overlapped.EventHandle is not 64-bit compatible and has been deprecated. Use EventHandleIntPtr instead."""
        warnings.warn("Overlapped.EventHandle is not 64-bit compatible and has been deprecated. Use EventHandleIntPtr instead.", DeprecationWarning)

    @property
    def EventHandleIntPtr(self) -> System.IntPtr:
        ...

    @EventHandleIntPtr.setter
    def EventHandleIntPtr(self, value: System.IntPtr):
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, offsetLo: int, offsetHi: int, hEvent: System.IntPtr, ar: System.IAsyncResult) -> None:
        ...

    @overload
    def __init__(self, offsetLo: int, offsetHi: int, hEvent: int, ar: System.IAsyncResult) -> None:
        """This constructor is not 64-bit compatible and has been deprecated. Use the constructor that accepts an IntPtr for the event handle instead."""
        ...

    @staticmethod
    def Free(nativeOverlappedPtr: typing.Any) -> None:
        ...

    @overload
    def Pack(self, iocb: typing.Callable[[int, int, typing.Any], None], userData: typing.Any) -> typing.Any:
        ...

    @overload
    def Pack(self, iocb: typing.Callable[[int, int, typing.Any], None]) -> typing.Any:
        """This overload is not safe and has been deprecated. Use Pack(IOCompletionCallback?, object?) instead."""
        ...

    @staticmethod
    def Unpack(nativeOverlappedPtr: typing.Any) -> System.Threading.Overlapped:
        ...

    @overload
    def UnsafePack(self, iocb: typing.Callable[[int, int, typing.Any], None], userData: typing.Any) -> typing.Any:
        ...

    @overload
    def UnsafePack(self, iocb: typing.Callable[[int, int, typing.Any], None]) -> typing.Any:
        """This overload is not safe and has been deprecated. Use UnsafePack(IOCompletionCallback?, object?) instead."""
        ...


class ThreadExceptionEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def Exception(self) -> System.Exception:
        ...

    def __init__(self, t: System.Exception) -> None:
        ...


class AbandonedMutexException(System.SystemException):
    """This class has no documentation."""

    @property
    def Mutex(self) -> System.Threading.Mutex:
        ...

    @property
    def MutexIndex(self) -> int:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception) -> None:
        ...

    @overload
    def __init__(self, location: int, handle: System.Threading.WaitHandle) -> None:
        ...

    @overload
    def __init__(self, message: str, location: int, handle: System.Threading.WaitHandle) -> None:
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception, location: int, handle: System.Threading.WaitHandle) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...


class CancellationTokenSource(System.Object, System.IDisposable):
    """Signals to a CancellationToken that it should be canceled."""

    s_canceledSource: System.Threading.CancellationTokenSource = ...
    """A CancellationTokenSource that's already canceled."""

    s_neverCanceledSource: System.Threading.CancellationTokenSource = ...
    """A CancellationTokenSource that's never canceled.  This isn't enforced programmatically, only by usage.  Do not cancel!"""

    @property
    def IsCancellationRequested(self) -> bool:
        """Gets whether cancellation has been requested for this CancellationTokenSource."""
        ...

    @property
    def IsCancellationCompleted(self) -> bool:
        """A simple helper to determine whether cancellation has finished."""
        ...

    @property
    def Token(self) -> System.Threading.CancellationToken:
        """Gets the CancellationToken associated with this CancellationTokenSource."""
        ...

    @property
    def WaitHandle(self) -> System.Threading.WaitHandle:
        ...

    @overload
    def __init__(self) -> None:
        """Initializes the CancellationTokenSource."""
        ...

    @overload
    def __init__(self, delay: datetime.timedelta) -> None:
        """
        Constructs a CancellationTokenSource that will be canceled after a specified time span.
        
        :param delay: The time span to wait before canceling this CancellationTokenSource
        """
        ...

    @overload
    def __init__(self, millisecondsDelay: int) -> None:
        """
        Constructs a CancellationTokenSource that will be canceled after a specified time span.
        
        :param millisecondsDelay: The time span to wait before canceling this CancellationTokenSource
        """
        ...

    @overload
    def Cancel(self) -> None:
        """Communicates a request for cancellation."""
        ...

    @overload
    def Cancel(self, throwOnFirstException: bool) -> None:
        """
        Communicates a request for cancellation.
        
        :param throwOnFirstException: Specifies whether exceptions should immediately propagate.
        """
        ...

    @overload
    def CancelAfter(self, delay: datetime.timedelta) -> None:
        """
        Schedules a Cancel operation on this CancellationTokenSource.
        
        :param delay: The time span to wait before canceling this CancellationTokenSource.
        """
        ...

    @overload
    def CancelAfter(self, millisecondsDelay: int) -> None:
        """
        Schedules a Cancel operation on this CancellationTokenSource.
        
        :param millisecondsDelay: The time span to wait before canceling this CancellationTokenSource.
        """
        ...

    @staticmethod
    @overload
    def CreateLinkedTokenSource(token1: System.Threading.CancellationToken, token2: System.Threading.CancellationToken) -> System.Threading.CancellationTokenSource:
        """
        Creates a CancellationTokenSource that will be in the canceled state
        when any of the source tokens are in the canceled state.
        
        :param token1: The first CancellationToken to observe.
        :param token2: The second CancellationToken to observe.
        :returns: A CancellationTokenSource that is linked to the source tokens.
        """
        ...

    @staticmethod
    @overload
    def CreateLinkedTokenSource(token: System.Threading.CancellationToken) -> System.Threading.CancellationTokenSource:
        """
        Creates a CancellationTokenSource that will be in the canceled state
        when the supplied token is in the canceled state.
        
        :param token: The CancellationToken to observe.
        :returns: A CancellationTokenSource that is linked to the source token.
        """
        ...

    @staticmethod
    @overload
    def CreateLinkedTokenSource(*tokens: System.Threading.CancellationToken) -> System.Threading.CancellationTokenSource:
        """
        Creates a CancellationTokenSource that will be in the canceled state
        when any of the source tokens are in the canceled state.
        
        :param tokens: The CancellationToken instances to observe.
        :returns: A CancellationTokenSource that is linked to the source tokens.
        """
        ...

    @overload
    def Dispose(self) -> None:
        """Releases the resources used by this CancellationTokenSource."""
        ...

    @overload
    def Dispose(self, disposing: bool) -> None:
        """
        Releases the unmanaged resources used by the CancellationTokenSource class and optionally releases the managed resources.
        
        This method is protected.
        
        :param disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        ...

    def TryReset(self) -> bool:
        """
        Attempts to reset the CancellationTokenSource to be used for an unrelated operation.
        
        :returns: true if the CancellationTokenSource has not had cancellation requested and could have its state reset to be reused for a subsequent operation; otherwise, false.
        """
        ...


class WaitHandleExtensions(System.Object):
    """This class has no documentation."""

    @staticmethod
    def GetSafeWaitHandle(waitHandle: System.Threading.WaitHandle) -> Microsoft.Win32.SafeHandles.SafeWaitHandle:
        """
        Gets the native operating system handle.
        
        :param waitHandle: The System.Threading.WaitHandle to operate on.
        :returns: A System.Runtime.InteropServices.SafeHandle representing the native operating system handle.
        """
        ...

    @staticmethod
    def SetSafeWaitHandle(waitHandle: System.Threading.WaitHandle, value: Microsoft.Win32.SafeHandles.SafeWaitHandle) -> None:
        """
        Sets the native operating system handle
        
        :param waitHandle: The System.Threading.WaitHandle to operate on.
        :param value: A System.Runtime.InteropServices.SafeHandle representing the native operating system handle.
        """
        ...


class ThreadLocal(typing.Generic[System_Threading_ThreadLocal_T], System.Object, System.IDisposable):
    """Provides thread-local storage of data."""

    @property
    def Value(self) -> System_Threading_ThreadLocal_T:
        """Gets or sets the value of this instance for the current thread."""
        ...

    @Value.setter
    def Value(self, value: System_Threading_ThreadLocal_T):
        """Gets or sets the value of this instance for the current thread."""
        ...

    @property
    def Values(self) -> System.Collections.Generic.IList[System_Threading_ThreadLocal_T]:
        """Gets a list for all of the values currently stored by all of the threads that have accessed this instance."""
        ...

    @property
    def IsValueCreated(self) -> bool:
        """Gets whether Value is initialized on the current thread."""
        ...

    @property
    def ValueForDebugDisplay(self) -> System_Threading_ThreadLocal_T:
        """
        Gets the value of the ThreadLocal<T> for debugging display purposes. It takes care of getting
        the value for the current thread in the ThreadLocal mode.
        """
        ...

    @property
    def ValuesForDebugDisplay(self) -> System.Collections.Generic.List[System_Threading_ThreadLocal_T]:
        """Gets the values of all threads that accessed the ThreadLocal<T>."""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes the System.Threading.ThreadLocal{T} instance."""
        ...

    @overload
    def __init__(self, trackAllValues: bool) -> None:
        """
        Initializes the System.Threading.ThreadLocal{T} instance.
        
        :param trackAllValues: Whether to track all values set on the instance and expose them through the Values property.
        """
        ...

    @overload
    def __init__(self, valueFactory: typing.Callable[[], System_Threading_ThreadLocal_T]) -> None:
        """
        Initializes the System.Threading.ThreadLocal{T} instance with the
        specified  function.
        
        :param valueFactory: The System.Func{T} invoked to produce a lazily-initialized value when an attempt is made to retrieve Value without it having been previously initialized.
        """
        ...

    @overload
    def __init__(self, valueFactory: typing.Callable[[], System_Threading_ThreadLocal_T], trackAllValues: bool) -> None:
        """
        Initializes the System.Threading.ThreadLocal{T} instance with the
        specified  function.
        
        :param valueFactory: The System.Func{T} invoked to produce a lazily-initialized value when an attempt is made to retrieve Value without it having been previously initialized.
        :param trackAllValues: Whether to track all values set on the instance and expose them via the Values property.
        """
        ...

    @overload
    def Dispose(self) -> None:
        ...

    @overload
    def Dispose(self, disposing: bool) -> None:
        """
        Releases the resources used by this System.Threading.ThreadLocal{T} instance.
        
        This method is protected.
        
        :param disposing: A Boolean value that indicates whether this method is being called due to a call to Dispose().
        """
        ...

    def ToString(self) -> str:
        ...


class NativeOverlapped:
    """This class has no documentation."""

    @property
    def InternalLow(self) -> System.IntPtr:
        ...

    @InternalLow.setter
    def InternalLow(self, value: System.IntPtr):
        ...

    @property
    def InternalHigh(self) -> System.IntPtr:
        ...

    @InternalHigh.setter
    def InternalHigh(self, value: System.IntPtr):
        ...

    @property
    def OffsetLow(self) -> int:
        ...

    @OffsetLow.setter
    def OffsetLow(self, value: int):
        ...

    @property
    def OffsetHigh(self) -> int:
        ...

    @OffsetHigh.setter
    def OffsetHigh(self, value: int):
        ...

    @property
    def EventHandle(self) -> System.IntPtr:
        ...

    @EventHandle.setter
    def EventHandle(self, value: System.IntPtr):
        ...


class LazyInitializer(System.Object):
    """Provides lazy initialization routines."""

    @staticmethod
    @overload
    def EnsureInitialized(target: System_Threading_LazyInitializer_EnsureInitialized_T) -> System_Threading_LazyInitializer_EnsureInitialized_T:
        """
        Initializes a target reference type with the type's default constructor if the target has not
        already been initialized.
        
        :param target: A reference of type T to initialize if it has not already been initialized.
        :returns: The initialized reference of type T.
        """
        ...

    @staticmethod
    @overload
    def EnsureInitialized(target: System_Threading_LazyInitializer_EnsureInitialized_T, valueFactory: typing.Callable[[], System_Threading_LazyInitializer_EnsureInitialized_T]) -> System_Threading_LazyInitializer_EnsureInitialized_T:
        """
        Initializes a target reference type using the specified function if it has not already been
        initialized.
        
        :param target: The reference of type T to initialize if it has not already been initialized.
        :param valueFactory: The System.Func{T} invoked to initialize the reference.
        :returns: The initialized reference of type T.
        """
        ...

    @staticmethod
    @overload
    def EnsureInitialized(target: System_Threading_LazyInitializer_EnsureInitialized_T, initialized: bool, syncLock: typing.Any) -> System_Threading_LazyInitializer_EnsureInitialized_T:
        """
        Initializes a target reference or value type with its default constructor if it has not already
        been initialized.
        
        :param target: A reference or value of type T to initialize if it has not already been initialized.
        :param initialized: A reference to a boolean that determines whether the target has already been initialized.
        :param syncLock: A reference to an object used as the mutually exclusive lock for initializing . If  is null, and if the target hasn't already been initialized, a new object will be instantiated.
        :returns: The initialized value of type T.
        """
        ...

    @staticmethod
    @overload
    def EnsureInitialized(target: System_Threading_LazyInitializer_EnsureInitialized_T, initialized: bool, syncLock: typing.Any, valueFactory: typing.Callable[[], System_Threading_LazyInitializer_EnsureInitialized_T]) -> System_Threading_LazyInitializer_EnsureInitialized_T:
        """
        Initializes a target reference or value type with a specified function if it has not already been
        initialized.
        
        :param target: A reference or value of type T to initialize if it has not already been initialized.
        :param initialized: A reference to a boolean that determines whether the target has already been initialized.
        :param syncLock: A reference to an object used as the mutually exclusive lock for initializing . If  is null, and if the target hasn't already been initialized, a new object will be instantiated.
        :param valueFactory: The System.Func{T} invoked to initialize the reference or value.
        :returns: The initialized value of type T.
        """
        ...

    @staticmethod
    @overload
    def EnsureInitialized(target: System_Threading_LazyInitializer_EnsureInitialized_T, syncLock: typing.Any, valueFactory: typing.Callable[[], System_Threading_LazyInitializer_EnsureInitialized_T]) -> System_Threading_LazyInitializer_EnsureInitialized_T:
        """
        Initializes a target reference type with a specified function if it has not already been initialized.
        
        :param target: A reference of type T to initialize if it has not already been initialized.
        :param syncLock: A reference to an object used as the mutually exclusive lock for initializing . If  is null, and if the target hasn't already been initialized, a new object will be instantiated.
        :param valueFactory: The System.Func{T} invoked to initialize the reference.
        :returns: The initialized value of type T.
        """
        ...


class SpinWait:
    """This class has no documentation."""

    YieldThreshold: int = 10

    DefaultSleep1Threshold: int = 20

    SpinCountforSpinBeforeWait: int = ...
    """
    A suggested number of spin iterations before doing a proper wait, such as waiting on an event that becomes signaled
    when the resource becomes available.
    """

    @property
    def Count(self) -> int:
        """Gets the number of times SpinOnce() has been called on this instance."""
        ...

    @Count.setter
    def Count(self, value: int):
        """Gets the number of times SpinOnce() has been called on this instance."""
        ...

    @property
    def NextSpinWillYield(self) -> bool:
        """
        Gets whether the next call to SpinOnce() will yield the processor, triggering a
        forced context switch.
        """
        ...

    def Reset(self) -> None:
        """Resets the spin counter."""
        ...

    @overload
    def SpinOnce(self) -> None:
        """Performs a single spin."""
        ...

    @overload
    def SpinOnce(self, sleep1Threshold: int) -> None:
        """
        Performs a single spin.
        
        :param sleep1Threshold: A minimum spin count after which Thread.Sleep(1) may be used. A value of -1 may be used to disable the use of Thread.Sleep(1).
        """
        ...

    @staticmethod
    @overload
    def SpinUntil(condition: typing.Callable[[], bool]) -> None:
        ...

    @staticmethod
    @overload
    def SpinUntil(condition: typing.Callable[[], bool], timeout: datetime.timedelta) -> bool:
        """
        Spins until the specified condition is satisfied or until the specified timeout is expired.
        
        :param condition: A delegate to be executed over and over until it returns true.
        :param timeout: A TimeSpan that represents the number of milliseconds to wait, or a TimeSpan that represents -1 milliseconds to wait indefinitely.
        :returns: True if the condition is satisfied within the timeout; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def SpinUntil(condition: typing.Callable[[], bool], millisecondsTimeout: int) -> bool:
        """
        Spins until the specified condition is satisfied or until the specified timeout is expired.
        
        :param condition: A delegate to be executed over and over until it returns true.
        :param millisecondsTimeout: The number of milliseconds to wait, or System.Threading.Timeout.Infinite (-1) to wait indefinitely.
        :returns: True if the condition is satisfied within the timeout; otherwise, false.
        """
        ...


class ThreadPriority(System.Enum):
    """This class has no documentation."""

    Lowest = 0

    BelowNormal = 1

    Normal = 2

    AboveNormal = 3

    Highest = 4


class ThreadStateException(System.SystemException):
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

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...


class SemaphoreSlim(System.Object, System.IDisposable):
    """Limits the number of threads that can access a resource or pool of resources concurrently."""

    @property
    def CurrentCount(self) -> int:
        ...

    @property
    def AvailableWaitHandle(self) -> System.Threading.WaitHandle:
        """Returns a System.Threading.WaitHandle that can be used to wait on the semaphore."""
        ...

    @overload
    def __init__(self, initialCount: int) -> None:
        ...

    @overload
    def __init__(self, initialCount: int, maxCount: int) -> None:
        """
        Initializes a new instance of the SemaphoreSlim class, specifying
        the initial and maximum number of requests that can be granted concurrently.
        
        :param initialCount: The initial number of requests for the semaphore that can be granted concurrently.
        :param maxCount: The maximum number of requests for the semaphore that can be granted concurrently.
        """
        ...

    @overload
    def Dispose(self) -> None:
        """Releases all resources used by the current instance of SemaphoreSlim."""
        ...

    @overload
    def Dispose(self, disposing: bool) -> None:
        """
        When overridden in a derived class, releases the unmanaged resources used by the
        System.Threading.ManualResetEventSlim, and optionally releases the managed resources.
        
        This method is protected.
        
        :param disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        ...

    @overload
    def Release(self) -> int:
        """
        Exits the SemaphoreSlim once.
        
        :returns: The previous count of the SemaphoreSlim.
        """
        ...

    @overload
    def Release(self, releaseCount: int) -> int:
        """
        Exits the SemaphoreSlim a specified number of times.
        
        :param releaseCount: The number of times to exit the semaphore.
        :returns: The previous count of the SemaphoreSlim.
        """
        ...

    @overload
    def Wait(self) -> None:
        ...

    @overload
    def Wait(self, cancellationToken: System.Threading.CancellationToken) -> None:
        """
        Blocks the current thread until it can enter the SemaphoreSlim, while observing a
        System.Threading.CancellationToken.
        
        :param cancellationToken: The System.Threading.CancellationToken token to observe.
        """
        ...

    @overload
    def Wait(self, timeout: datetime.timedelta) -> bool:
        """
        Blocks the current thread until it can enter the SemaphoreSlim, using a System.TimeSpan to measure the time interval.
        
        :param timeout: A System.TimeSpan that represents the number of milliseconds to wait, or a System.TimeSpan that represents -1 milliseconds to wait indefinitely.
        :returns: true if the current thread successfully entered the SemaphoreSlim; otherwise, false.
        """
        ...

    @overload
    def Wait(self, timeout: datetime.timedelta, cancellationToken: System.Threading.CancellationToken) -> bool:
        """
        Blocks the current thread until it can enter the SemaphoreSlim, using a System.TimeSpan to measure the time interval, while observing a System.Threading.CancellationToken.
        
        :param timeout: A System.TimeSpan that represents the number of milliseconds to wait, or a System.TimeSpan that represents -1 milliseconds to wait indefinitely.
        :param cancellationToken: The System.Threading.CancellationToken to observe.
        :returns: true if the current thread successfully entered the SemaphoreSlim; otherwise, false.
        """
        ...

    @overload
    def Wait(self, millisecondsTimeout: int) -> bool:
        """
        Blocks the current thread until it can enter the SemaphoreSlim, using a 32-bit
        signed integer to measure the time interval.
        
        :param millisecondsTimeout: The number of milliseconds to wait, or Timeout.Infinite(-1) to wait indefinitely.
        :returns: true if the current thread successfully entered the SemaphoreSlim; otherwise, false.
        """
        ...

    @overload
    def Wait(self, millisecondsTimeout: int, cancellationToken: System.Threading.CancellationToken) -> bool:
        """
        Blocks the current thread until it can enter the SemaphoreSlim,
        using a 32-bit signed integer to measure the time interval,
        while observing a System.Threading.CancellationToken.
        
        :param millisecondsTimeout: The number of milliseconds to wait, or Timeout.Infinite(-1) to wait indefinitely.
        :param cancellationToken: The System.Threading.CancellationToken to observe.
        :returns: true if the current thread successfully entered the SemaphoreSlim; otherwise, false.
        """
        ...

    @overload
    def WaitAsync(self) -> System.Threading.Tasks.Task:
        """
        Asynchronously waits to enter the SemaphoreSlim.
        
        :returns: A task that will complete when the semaphore has been entered.
        """
        ...

    @overload
    def WaitAsync(self, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Asynchronously waits to enter the SemaphoreSlim, while observing a
        System.Threading.CancellationToken.
        
        :param cancellationToken: The System.Threading.CancellationToken token to observe.
        :returns: A task that will complete when the semaphore has been entered.
        """
        ...

    @overload
    def WaitAsync(self, millisecondsTimeout: int) -> System.Threading.Tasks.Task[bool]:
        """
        Asynchronously waits to enter the SemaphoreSlim,
        using a 32-bit signed integer to measure the time interval.
        
        :param millisecondsTimeout: The number of milliseconds to wait, or Timeout.Infinite(-1) to wait indefinitely.
        :returns: A task that will complete with a result of true if the current thread successfully entered the SemaphoreSlim, otherwise with a result of false.
        """
        ...

    @overload
    def WaitAsync(self, timeout: datetime.timedelta) -> System.Threading.Tasks.Task[bool]:
        """
        Asynchronously waits to enter the SemaphoreSlim, using a System.TimeSpan to measure the time interval, while observing a
        System.Threading.CancellationToken.
        
        :param timeout: A System.TimeSpan that represents the number of milliseconds to wait, or a System.TimeSpan that represents -1 milliseconds to wait indefinitely.
        :returns: A task that will complete with a result of true if the current thread successfully entered the SemaphoreSlim, otherwise with a result of false.
        """
        ...

    @overload
    def WaitAsync(self, timeout: datetime.timedelta, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[bool]:
        """
        Asynchronously waits to enter the SemaphoreSlim, using a System.TimeSpan to measure the time interval.
        
        :param timeout: A System.TimeSpan that represents the number of milliseconds to wait, or a System.TimeSpan that represents -1 milliseconds to wait indefinitely.
        :param cancellationToken: The System.Threading.CancellationToken token to observe.
        :returns: A task that will complete with a result of true if the current thread successfully entered the SemaphoreSlim, otherwise with a result of false.
        """
        ...

    @overload
    def WaitAsync(self, millisecondsTimeout: int, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[bool]:
        """
        Asynchronously waits to enter the SemaphoreSlim,
        using a 32-bit signed integer to measure the time interval,
        while observing a System.Threading.CancellationToken.
        
        :param millisecondsTimeout: The number of milliseconds to wait, or Timeout.Infinite(-1) to wait indefinitely.
        :param cancellationToken: The System.Threading.CancellationToken to observe.
        :returns: A task that will complete with a result of true if the current thread successfully entered the SemaphoreSlim, otherwise with a result of false.
        """
        ...


class PeriodicTimer(System.Object, System.IDisposable):
    """Provides a periodic timer that enables waiting asynchronously for timer ticks."""

    def __init__(self, period: datetime.timedelta) -> None:
        """
        Initializes the timer.
        
        :param period: The time interval between invocations of callback..
        """
        ...

    def Dispose(self) -> None:
        """Stops the timer and releases associated managed resources."""
        ...

    def WaitForNextTickAsync(self, cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[bool]:
        """
        Wait for the next tick of the timer, or for the timer to be stopped.
        
        :param cancellationToken: A CancellationToken to use to cancel the asynchronous wait. If cancellation is requested, it affects only the single wait operation; the underlying timer continues firing.
        :returns: A task that will be completed due to the timer firing, Dispose being called to stop the timer, or cancellation being requested.
        """
        ...


class Interlocked(System.Object):
    """Provides atomic operations for variables that are shared by multiple threads."""

    @staticmethod
    @overload
    def Add(location1: int, value: int) -> int:
        ...

    @staticmethod
    @overload
    def Add(location1: int, value: int) -> int:
        """
        Adds two 64-bit unsigned integers and replaces the first integer with the sum, as an atomic operation.
        
        :param location1: A variable containing the first value to be added. The sum of the two values is stored in .
        :param value: The value to be added to the integer at .
        :returns: The new value stored at .
        """
        ...

    @staticmethod
    @overload
    def Add(location1: int, value: int) -> int:
        ...

    @staticmethod
    @overload
    def Add(location1: int, value: int) -> int:
        ...

    @staticmethod
    @overload
    def And(location1: int, value: int) -> int:
        ...

    @staticmethod
    @overload
    def And(location1: int, value: int) -> int:
        """
        Bitwise "ands" two 32-bit unsigned integers and replaces the first integer with the result, as an atomic operation.
        
        :param location1: A variable containing the first value to be combined. The result is stored in .
        :param value: The value to be combined with the integer at .
        :returns: The original value in .
        """
        ...

    @staticmethod
    @overload
    def And(location1: int, value: int) -> int:
        """
        Bitwise "ands" two 64-bit signed integers and replaces the first integer with the result, as an atomic operation.
        
        :param location1: A variable containing the first value to be combined. The result is stored in .
        :param value: The value to be combined with the integer at .
        :returns: The original value in .
        """
        ...

    @staticmethod
    @overload
    def And(location1: int, value: int) -> int:
        """
        Bitwise "ands" two 64-bit unsigned integers and replaces the first integer with the result, as an atomic operation.
        
        :param location1: A variable containing the first value to be combined. The result is stored in .
        :param value: The value to be combined with the integer at .
        :returns: The original value in .
        """
        ...

    @staticmethod
    @overload
    def CompareExchange(location1: int, value: int, comparand: int) -> int:
        ...

    @staticmethod
    @overload
    def CompareExchange(location1: int, value: int, comparand: int) -> int:
        """
        Compares two 64-bit unsigned integers for equality and, if they are equal, replaces the first value.
        
        :param location1: The destination, whose value is compared with  and possibly replaced.
        :param value: The value that replaces the destination value if the comparison results in equality.
        :param comparand: The value that is compared to the value at .
        :returns: The original value in .
        """
        ...

    @staticmethod
    @overload
    def CompareExchange(location1: System.IntPtr, value: System.IntPtr, comparand: System.IntPtr) -> System.IntPtr:
        """
        Compares two platform-specific handles or pointers for equality and, if they are equal, replaces the first one.
        
        :param location1: The destination IntPtr, whose value is compared with the value of  and possibly replaced by .
        :param value: The IntPtr that replaces the destination value if the comparison results in equality.
        :param comparand: The IntPtr that is compared to the value at .
        :returns: The original value in .
        """
        ...

    @staticmethod
    @overload
    def CompareExchange(location1: System.UIntPtr, value: System.UIntPtr, comparand: System.UIntPtr) -> System.UIntPtr:
        """
        Compares two platform-specific handles or pointers for equality and, if they are equal, replaces the first one.
        
        :param location1: The destination UIntPtr, whose value is compared with the value of  and possibly replaced by .
        :param value: The UIntPtr that replaces the destination value if the comparison results in equality.
        :param comparand: The UIntPtr that is compared to the value at .
        :returns: The original value in .
        """
        ...

    @staticmethod
    @overload
    def CompareExchange(location1: int, value: int, comparand: int) -> int:
        ...

    @staticmethod
    @overload
    def CompareExchange(location1: typing.Any, value: typing.Any, comparand: typing.Any) -> System.Object:
        ...

    @staticmethod
    @overload
    def CompareExchange(location1: float, value: float, comparand: float) -> float:
        ...

    @staticmethod
    @overload
    def CompareExchange(location1: int, value: int, comparand: int) -> int:
        ...

    @staticmethod
    @overload
    def CompareExchange(location1: float, value: float, comparand: float) -> float:
        ...

    @staticmethod
    @overload
    def CompareExchange(location1: System_Threading_Interlocked_CompareExchange_T, value: System_Threading_Interlocked_CompareExchange_T, comparand: System_Threading_Interlocked_CompareExchange_T) -> System_Threading_Interlocked_CompareExchange_T:
        ...

    @staticmethod
    @overload
    def Decrement(location: int) -> int:
        ...

    @staticmethod
    @overload
    def Decrement(location: int) -> int:
        """
        Decrements a specified variable and stores the result, as an atomic operation.
        
        :param location: The variable whose value is to be decremented.
        :returns: The decremented value.
        """
        ...

    @staticmethod
    @overload
    def Decrement(location: int) -> int:
        ...

    @staticmethod
    @overload
    def Decrement(location: int) -> int:
        ...

    @staticmethod
    @overload
    def Exchange(location1: int, value: int) -> int:
        ...

    @staticmethod
    @overload
    def Exchange(location1: int, value: int) -> int:
        """
        Sets a 64-bit unsigned integer to a specified value and returns the original value, as an atomic operation.
        
        :param location1: The variable to set to the specified value.
        :param value: The value to which the  parameter is set.
        :returns: The original value of .
        """
        ...

    @staticmethod
    @overload
    def Exchange(location1: System.IntPtr, value: System.IntPtr) -> System.IntPtr:
        """
        Sets a platform-specific handle or pointer to a specified value and returns the original value, as an atomic operation.
        
        :param location1: The variable to set to the specified value.
        :param value: The value to which the  parameter is set.
        :returns: The original value of .
        """
        ...

    @staticmethod
    @overload
    def Exchange(location1: System.UIntPtr, value: System.UIntPtr) -> System.UIntPtr:
        """
        Sets a platform-specific handle or pointer to a specified value and returns the original value, as an atomic operation.
        
        :param location1: The variable to set to the specified value.
        :param value: The value to which the  parameter is set.
        :returns: The original value of .
        """
        ...

    @staticmethod
    @overload
    def Exchange(location1: int, value: int) -> int:
        ...

    @staticmethod
    @overload
    def Exchange(location1: typing.Any, value: typing.Any) -> System.Object:
        ...

    @staticmethod
    @overload
    def Exchange(location1: float, value: float) -> float:
        ...

    @staticmethod
    @overload
    def Exchange(location1: int, value: int) -> int:
        ...

    @staticmethod
    @overload
    def Exchange(location1: float, value: float) -> float:
        ...

    @staticmethod
    @overload
    def Exchange(location1: System_Threading_Interlocked_Exchange_T, value: System_Threading_Interlocked_Exchange_T) -> System_Threading_Interlocked_Exchange_T:
        ...

    @staticmethod
    @overload
    def Increment(location: int) -> int:
        ...

    @staticmethod
    @overload
    def Increment(location: int) -> int:
        """
        Increments a specified variable and stores the result, as an atomic operation.
        
        :param location: The variable whose value is to be incremented.
        :returns: The incremented value.
        """
        ...

    @staticmethod
    @overload
    def Increment(location: int) -> int:
        ...

    @staticmethod
    @overload
    def Increment(location: int) -> int:
        ...

    @staticmethod
    def MemoryBarrier() -> None:
        ...

    @staticmethod
    def MemoryBarrierProcessWide() -> None:
        ...

    @staticmethod
    @overload
    def Or(location1: int, value: int) -> int:
        ...

    @staticmethod
    @overload
    def Or(location1: int, value: int) -> int:
        """
        Bitwise "ors" two 32-bit unsigned integers and replaces the first integer with the result, as an atomic operation.
        
        :param location1: A variable containing the first value to be combined. The result is stored in .
        :param value: The value to be combined with the integer at .
        :returns: The original value in .
        """
        ...

    @staticmethod
    @overload
    def Or(location1: int, value: int) -> int:
        """
        Bitwise "ors" two 64-bit signed integers and replaces the first integer with the result, as an atomic operation.
        
        :param location1: A variable containing the first value to be combined. The result is stored in .
        :param value: The value to be combined with the integer at .
        :returns: The original value in .
        """
        ...

    @staticmethod
    @overload
    def Or(location1: int, value: int) -> int:
        """
        Bitwise "ors" two 64-bit unsigned integers and replaces the first integer with the result, as an atomic operation.
        
        :param location1: A variable containing the first value to be combined. The result is stored in .
        :param value: The value to be combined with the integer at .
        :returns: The original value in .
        """
        ...

    @staticmethod
    @overload
    def Read(location: int) -> int:
        ...

    @staticmethod
    @overload
    def Read(location: int) -> int:
        ...


class ThreadInterruptedException(System.SystemException):
    """An exception class to indicate that the thread was interrupted from a waiting state."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...


class ManualResetEvent(System.Threading.EventWaitHandle):
    """This class has no documentation."""

    def __init__(self, initialState: bool) -> None:
        ...


class Monitor(System.Object):
    """This class has no documentation."""

    LockContentionCount: int

    @staticmethod
    @overload
    def Enter(obj: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def Enter(obj: typing.Any, lockTaken: bool) -> None:
        ...

    @staticmethod
    def Exit(obj: typing.Any) -> None:
        ...

    @staticmethod
    def IsEntered(obj: typing.Any) -> bool:
        ...

    @staticmethod
    def Pulse(obj: typing.Any) -> None:
        ...

    @staticmethod
    def PulseAll(obj: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def TryEnter(obj: typing.Any, timeout: datetime.timedelta) -> bool:
        ...

    @staticmethod
    @overload
    def TryEnter(obj: typing.Any, timeout: datetime.timedelta, lockTaken: bool) -> None:
        ...

    @staticmethod
    @overload
    def TryEnter(obj: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def TryEnter(obj: typing.Any, lockTaken: bool) -> None:
        ...

    @staticmethod
    @overload
    def TryEnter(obj: typing.Any, millisecondsTimeout: int) -> bool:
        ...

    @staticmethod
    @overload
    def TryEnter(obj: typing.Any, millisecondsTimeout: int, lockTaken: bool) -> None:
        ...

    @staticmethod
    @overload
    def Wait(obj: typing.Any, timeout: datetime.timedelta) -> bool:
        ...

    @staticmethod
    @overload
    def Wait(obj: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def Wait(obj: typing.Any, millisecondsTimeout: int, exitContext: bool) -> bool:
        ...

    @staticmethod
    @overload
    def Wait(obj: typing.Any, timeout: datetime.timedelta, exitContext: bool) -> bool:
        ...

    @staticmethod
    @overload
    def Wait(obj: typing.Any, millisecondsTimeout: int) -> bool:
        ...


