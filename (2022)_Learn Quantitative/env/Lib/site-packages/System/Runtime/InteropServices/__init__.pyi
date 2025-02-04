from typing import overload
import abc
import typing
import warnings

import Microsoft.Win32.SafeHandles
import System
import System.Collections
import System.Collections.Generic
import System.Globalization
import System.Numerics
import System.Reflection
import System.Runtime.ConstrainedExecution
import System.Runtime.InteropServices
import System.Runtime.InteropServices.ComTypes
import System.Runtime.Serialization
import System.Security

System_Runtime_InteropServices_ArrayWithOffset = typing.Any
System_Runtime_InteropServices_CULong = typing.Any
System_Runtime_InteropServices_OSPlatform = typing.Any
System_Runtime_InteropServices_NFloat = typing.Any
System_Runtime_InteropServices_GCHandle = typing.Any
System_Runtime_InteropServices_CLong = typing.Any

System_Runtime_InteropServices_Marshal_SizeOf_T = typing.TypeVar("System_Runtime_InteropServices_Marshal_SizeOf_T")
System_Runtime_InteropServices_Marshal_StructureToPtr_T = typing.TypeVar("System_Runtime_InteropServices_Marshal_StructureToPtr_T")
System_Runtime_InteropServices_Marshal_PtrToStructure_T = typing.TypeVar("System_Runtime_InteropServices_Marshal_PtrToStructure_T")
System_Runtime_InteropServices_Marshal_GetDelegateForFunctionPointer_TDelegate = typing.TypeVar("System_Runtime_InteropServices_Marshal_GetDelegateForFunctionPointer_TDelegate")
System_Runtime_InteropServices_Marshal_GetFunctionPointerForDelegate_TDelegate = typing.TypeVar("System_Runtime_InteropServices_Marshal_GetFunctionPointerForDelegate_TDelegate")
System_Runtime_InteropServices_Marshal_CreateAggregatedObject_T = typing.TypeVar("System_Runtime_InteropServices_Marshal_CreateAggregatedObject_T")
System_Runtime_InteropServices_Marshal_CreateWrapperOfType_TWrapper = typing.TypeVar("System_Runtime_InteropServices_Marshal_CreateWrapperOfType_TWrapper")
System_Runtime_InteropServices_Marshal_CreateWrapperOfType_T = typing.TypeVar("System_Runtime_InteropServices_Marshal_CreateWrapperOfType_T")
System_Runtime_InteropServices_Marshal_GetComInterfaceForObject_T = typing.TypeVar("System_Runtime_InteropServices_Marshal_GetComInterfaceForObject_T")
System_Runtime_InteropServices_Marshal_GetNativeVariantForObject_T = typing.TypeVar("System_Runtime_InteropServices_Marshal_GetNativeVariantForObject_T")
System_Runtime_InteropServices_Marshal_GetObjectForNativeVariant_T = typing.TypeVar("System_Runtime_InteropServices_Marshal_GetObjectForNativeVariant_T")
System_Runtime_InteropServices_Marshal_UnsafeAddrOfPinnedArrayElement_T = typing.TypeVar("System_Runtime_InteropServices_Marshal_UnsafeAddrOfPinnedArrayElement_T")
System_Runtime_InteropServices_Marshal_GetObjectsForNativeVariants_T = typing.TypeVar("System_Runtime_InteropServices_Marshal_GetObjectsForNativeVariants_T")
System_Runtime_InteropServices_SafeBuffer_Read_T = typing.TypeVar("System_Runtime_InteropServices_SafeBuffer_Read_T")
System_Runtime_InteropServices_SafeBuffer_Write_T = typing.TypeVar("System_Runtime_InteropServices_SafeBuffer_Write_T")
System_Runtime_InteropServices_SafeBuffer_ReadArray_T = typing.TypeVar("System_Runtime_InteropServices_SafeBuffer_ReadArray_T")
System_Runtime_InteropServices_SafeBuffer_ReadSpan_T = typing.TypeVar("System_Runtime_InteropServices_SafeBuffer_ReadSpan_T")
System_Runtime_InteropServices_SafeBuffer_WriteArray_T = typing.TypeVar("System_Runtime_InteropServices_SafeBuffer_WriteArray_T")
System_Runtime_InteropServices_SafeBuffer_WriteSpan_T = typing.TypeVar("System_Runtime_InteropServices_SafeBuffer_WriteSpan_T")
System_Runtime_InteropServices_ComWrappers_GetInstance_ComInterfaceDispatch_T = typing.TypeVar("System_Runtime_InteropServices_ComWrappers_GetInstance_ComInterfaceDispatch_T")
System_Runtime_InteropServices_CollectionsMarshal_GetValueRefOrNullRef_TKey = typing.TypeVar("System_Runtime_InteropServices_CollectionsMarshal_GetValueRefOrNullRef_TKey")
System_Runtime_InteropServices_CollectionsMarshal_GetValueRefOrAddDefault_TKey = typing.TypeVar("System_Runtime_InteropServices_CollectionsMarshal_GetValueRefOrAddDefault_TKey")
System_Runtime_InteropServices_CollectionsMarshal_AsSpan_T = typing.TypeVar("System_Runtime_InteropServices_CollectionsMarshal_AsSpan_T")
System_Runtime_InteropServices_CollectionsMarshal_GetValueRefOrNullRef_TValue = typing.TypeVar("System_Runtime_InteropServices_CollectionsMarshal_GetValueRefOrNullRef_TValue")
System_Runtime_InteropServices_CollectionsMarshal_GetValueRefOrAddDefault_TValue = typing.TypeVar("System_Runtime_InteropServices_CollectionsMarshal_GetValueRefOrAddDefault_TValue")
System_Runtime_InteropServices_MemoryMarshal_Read_T = typing.TypeVar("System_Runtime_InteropServices_MemoryMarshal_Read_T")
System_Runtime_InteropServices_MemoryMarshal_Write_T = typing.TypeVar("System_Runtime_InteropServices_MemoryMarshal_Write_T")
System_Runtime_InteropServices_MemoryMarshal_TryWrite_T = typing.TypeVar("System_Runtime_InteropServices_MemoryMarshal_TryWrite_T")
System_Runtime_InteropServices_MemoryMarshal_AsBytes_T = typing.TypeVar("System_Runtime_InteropServices_MemoryMarshal_AsBytes_T")
System_Runtime_InteropServices_MemoryMarshal_AsMemory_T = typing.TypeVar("System_Runtime_InteropServices_MemoryMarshal_AsMemory_T")
System_Runtime_InteropServices_MemoryMarshal_GetReference_T = typing.TypeVar("System_Runtime_InteropServices_MemoryMarshal_GetReference_T")
System_Runtime_InteropServices_MemoryMarshal_Cast_TTo = typing.TypeVar("System_Runtime_InteropServices_MemoryMarshal_Cast_TTo")
System_Runtime_InteropServices_MemoryMarshal_Cast_TFrom = typing.TypeVar("System_Runtime_InteropServices_MemoryMarshal_Cast_TFrom")
System_Runtime_InteropServices_MemoryMarshal_TryGetArray_T = typing.TypeVar("System_Runtime_InteropServices_MemoryMarshal_TryGetArray_T")
System_Runtime_InteropServices_MemoryMarshal_TryGetMemoryManager_TManager = typing.TypeVar("System_Runtime_InteropServices_MemoryMarshal_TryGetMemoryManager_TManager")
System_Runtime_InteropServices_MemoryMarshal_TryGetMemoryManager_T = typing.TypeVar("System_Runtime_InteropServices_MemoryMarshal_TryGetMemoryManager_T")
System_Runtime_InteropServices_MemoryMarshal_ToEnumerable_T = typing.TypeVar("System_Runtime_InteropServices_MemoryMarshal_ToEnumerable_T")
System_Runtime_InteropServices_MemoryMarshal_TryRead_T = typing.TypeVar("System_Runtime_InteropServices_MemoryMarshal_TryRead_T")
System_Runtime_InteropServices_MemoryMarshal_CreateFromPinnedArray_T = typing.TypeVar("System_Runtime_InteropServices_MemoryMarshal_CreateFromPinnedArray_T")
System_Runtime_InteropServices_MemoryMarshal_GetArrayDataReference_T = typing.TypeVar("System_Runtime_InteropServices_MemoryMarshal_GetArrayDataReference_T")


class ICustomAdapter(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def GetUnderlyingObject(self) -> System.Object:
        ...


class ClassInterfaceType(System.Enum):
    """This class has no documentation."""

    # Cannot convert to Python: None = 0

    AutoDispatch = 1

    AutoDual = 2


class ClassInterfaceAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Value(self) -> int:
        """This property contains the int value of a member of the System.Runtime.InteropServices.ClassInterfaceType enum."""
        ...

    @overload
    def __init__(self, classInterfaceType: System.Runtime.InteropServices.ClassInterfaceType) -> None:
        ...

    @overload
    def __init__(self, classInterfaceType: int) -> None:
        ...


class ExternalException(System.SystemException):
    """This class has no documentation."""

    @property
    def ErrorCode(self) -> int:
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
    def __init__(self, message: str, errorCode: int) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...

    def ToString(self) -> str:
        ...


class CharSet(System.Enum):
    """This class has no documentation."""

    # Cannot convert to Python: None = 1

    Ansi = 2

    Unicode = 3

    Auto = 4


class CallingConvention(System.Enum):
    """This class has no documentation."""

    Winapi = 1

    Cdecl = 2

    StdCall = 3

    ThisCall = 4

    FastCall = 5


class UnmanagedFunctionPointerAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def CallingConvention(self) -> int:
        """This property contains the int value of a member of the System.Runtime.InteropServices.CallingConvention enum."""
        ...

    @property
    def BestFitMapping(self) -> bool:
        ...

    @BestFitMapping.setter
    def BestFitMapping(self, value: bool):
        ...

    @property
    def SetLastError(self) -> bool:
        ...

    @SetLastError.setter
    def SetLastError(self, value: bool):
        ...

    @property
    def ThrowOnUnmappableChar(self) -> bool:
        ...

    @ThrowOnUnmappableChar.setter
    def ThrowOnUnmappableChar(self, value: bool):
        ...

    @property
    def CharSet(self) -> System.Runtime.InteropServices.CharSet:
        ...

    @CharSet.setter
    def CharSet(self, value: System.Runtime.InteropServices.CharSet):
        ...

    def __init__(self, callingConvention: System.Runtime.InteropServices.CallingConvention) -> None:
        ...


class DefaultParameterValueAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Value(self) -> System.Object:
        ...

    def __init__(self, value: typing.Any) -> None:
        ...


class SafeHandle(System.Runtime.ConstrainedExecution.CriticalFinalizerObject, System.IDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def handle(self) -> System.IntPtr:
        """This field is protected."""
        ...

    @handle.setter
    def handle(self, value: System.IntPtr):
        """This field is protected."""
        ...

    @property
    def OwnsHandle(self) -> bool:
        ...

    @property
    def IsClosed(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def IsInvalid(self) -> bool:
        ...

    def __init__(self, invalidHandleValue: System.IntPtr, ownsHandle: bool) -> None:
        """
        Creates a SafeHandle class.
        
        This method is protected.
        """
        ...

    def Close(self) -> None:
        ...

    def DangerousAddRef(self, success: bool) -> None:
        ...

    def DangerousGetHandle(self) -> System.IntPtr:
        ...

    def DangerousRelease(self) -> None:
        ...

    @overload
    def Dispose(self) -> None:
        ...

    @overload
    def Dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def ReleaseHandle(self) -> bool:
        """This method is protected."""
        ...

    def SetHandleAsInvalid(self) -> None:
        ...


class CustomQueryInterfaceMode(System.Enum):
    """This class has no documentation."""

    Ignore = 0

    Allow = 1


class Marshal(System.Object):
    """
    This class contains methods that are mainly used to marshal between unmanaged
    and managed types.
    """

    SystemDefaultCharSize: int = 2
    """
    The default character size for the system. This is always 2 because
    the framework only runs on UTF-16 systems.
    """

    SystemMaxDBCSCharSize: int = ...
    """The max DBCS character size for the system."""

    IsBuiltInComSupported: bool

    @staticmethod
    def AddRef(pUnk: System.IntPtr) -> int:
        ...

    @staticmethod
    @overload
    def AllocCoTaskMem(cb: int) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def AllocCoTaskMem(cb: int) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def AllocHGlobal(cb: int) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def AllocHGlobal(cb: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def AllocHGlobal(cb: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    def AreComObjectsAvailableForCleanup() -> bool:
        ...

    @staticmethod
    def BindToMoniker(monikerName: str) -> System.Object:
        ...

    @staticmethod
    def ChangeWrapperHandleStrength(otp: typing.Any, fIsWeak: bool) -> None:
        ...

    @staticmethod
    def CleanupUnusedObjectsInCurrentContext() -> None:
        ...

    @staticmethod
    @overload
    def Copy(source: typing.List[int], startIndex: int, destination: System.IntPtr, length: int) -> None:
        ...

    @staticmethod
    @overload
    def Copy(source: typing.List[str], startIndex: int, destination: System.IntPtr, length: int) -> None:
        ...

    @staticmethod
    @overload
    def Copy(source: typing.List[int], startIndex: int, destination: System.IntPtr, length: int) -> None:
        ...

    @staticmethod
    @overload
    def Copy(source: typing.List[int], startIndex: int, destination: System.IntPtr, length: int) -> None:
        ...

    @staticmethod
    @overload
    def Copy(source: typing.List[float], startIndex: int, destination: System.IntPtr, length: int) -> None:
        ...

    @staticmethod
    @overload
    def Copy(source: typing.List[float], startIndex: int, destination: System.IntPtr, length: int) -> None:
        ...

    @staticmethod
    @overload
    def Copy(source: typing.List[int], startIndex: int, destination: System.IntPtr, length: int) -> None:
        ...

    @staticmethod
    @overload
    def Copy(source: typing.List[System.IntPtr], startIndex: int, destination: System.IntPtr, length: int) -> None:
        ...

    @staticmethod
    @overload
    def Copy(source: System.IntPtr, destination: typing.List[int], startIndex: int, length: int) -> None:
        ...

    @staticmethod
    @overload
    def Copy(source: System.IntPtr, destination: typing.List[str], startIndex: int, length: int) -> None:
        ...

    @staticmethod
    @overload
    def Copy(source: System.IntPtr, destination: typing.List[int], startIndex: int, length: int) -> None:
        ...

    @staticmethod
    @overload
    def Copy(source: System.IntPtr, destination: typing.List[int], startIndex: int, length: int) -> None:
        ...

    @staticmethod
    @overload
    def Copy(source: System.IntPtr, destination: typing.List[float], startIndex: int, length: int) -> None:
        ...

    @staticmethod
    @overload
    def Copy(source: System.IntPtr, destination: typing.List[float], startIndex: int, length: int) -> None:
        ...

    @staticmethod
    @overload
    def Copy(source: System.IntPtr, destination: typing.List[int], startIndex: int, length: int) -> None:
        ...

    @staticmethod
    @overload
    def Copy(source: System.IntPtr, destination: typing.List[System.IntPtr], startIndex: int, length: int) -> None:
        ...

    @staticmethod
    @overload
    def CreateAggregatedObject(pOuter: System.IntPtr, o: typing.Any) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def CreateAggregatedObject(pOuter: System.IntPtr, o: System_Runtime_InteropServices_Marshal_CreateAggregatedObject_T) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def CreateWrapperOfType(o: typing.Any, t: typing.Type) -> System.Object:
        ...

    @staticmethod
    @overload
    def CreateWrapperOfType(o: System_Runtime_InteropServices_Marshal_CreateWrapperOfType_T) -> System_Runtime_InteropServices_Marshal_CreateWrapperOfType_TWrapper:
        ...

    @staticmethod
    @overload
    def DestroyStructure(ptr: System.IntPtr) -> None:
        ...

    @staticmethod
    @overload
    def DestroyStructure(ptr: System.IntPtr, structuretype: typing.Type) -> None:
        ...

    @staticmethod
    def FinalReleaseComObject(o: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def FreeBSTR(ptr: System.IntPtr) -> None:
        ...

    @staticmethod
    @overload
    def FreeBSTR(ptr: System.IntPtr) -> None:
        ...

    @staticmethod
    @overload
    def FreeCoTaskMem(ptr: System.IntPtr) -> None:
        ...

    @staticmethod
    @overload
    def FreeCoTaskMem(ptr: System.IntPtr) -> None:
        ...

    @staticmethod
    @overload
    def FreeHGlobal(hglobal: System.IntPtr) -> None:
        ...

    @staticmethod
    @overload
    def FreeHGlobal(hglobal: System.IntPtr) -> None:
        ...

    @staticmethod
    def GenerateGuidForType(type: typing.Type) -> System.Guid:
        """
        Generates a GUID for the specified type. If the type has a GUID in the
        metadata then it is returned otherwise a stable guid is generated based
        on the fully qualified name of the type.
        """
        ...

    @staticmethod
    def GenerateProgIdForType(type: typing.Type) -> str:
        """
        This method generates a PROGID for the specified type. If the type has
        a PROGID in the metadata then it is returned otherwise a stable PROGID
        is generated based on the fully qualified name of the type.
        """
        ...

    @staticmethod
    @overload
    def GetComInterfaceForObject(o: typing.Any, T: typing.Type) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def GetComInterfaceForObject(o: typing.Any, T: typing.Type, mode: System.Runtime.InteropServices.CustomQueryInterfaceMode) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def GetComInterfaceForObject(o: System_Runtime_InteropServices_Marshal_GetComInterfaceForObject_T) -> System.IntPtr:
        ...

    @staticmethod
    def GetComObjectData(obj: typing.Any, key: typing.Any) -> System.Object:
        ...

    @staticmethod
    @overload
    def GetDelegateForFunctionPointer(ptr: System.IntPtr, t: typing.Type) -> System.Delegate:
        ...

    @staticmethod
    @overload
    def GetDelegateForFunctionPointer(ptr: System.IntPtr) -> System_Runtime_InteropServices_Marshal_GetDelegateForFunctionPointer_TDelegate:
        ...

    @staticmethod
    def GetEndComSlot(t: typing.Type) -> int:
        ...

    @staticmethod
    def GetExceptionCode() -> int:
        """GetExceptionCode() may be unavailable in future releases."""
        warnings.warn("GetExceptionCode() may be unavailable in future releases.", DeprecationWarning)

    @staticmethod
    @overload
    def GetExceptionForHR(errorCode: int) -> System.Exception:
        ...

    @staticmethod
    @overload
    def GetExceptionForHR(errorCode: int, errorInfo: System.IntPtr) -> System.Exception:
        ...

    @staticmethod
    def GetExceptionPointers() -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def GetFunctionPointerForDelegate(d: System.Delegate) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def GetFunctionPointerForDelegate(d: System_Runtime_InteropServices_Marshal_GetFunctionPointerForDelegate_TDelegate) -> System.IntPtr:
        ...

    @staticmethod
    def GetHINSTANCE(m: System.Reflection.Module) -> System.IntPtr:
        ...

    @staticmethod
    def GetHRForException(e: System.Exception) -> int:
        ...

    @staticmethod
    def GetHRForLastWin32Error() -> int:
        ...

    @staticmethod
    def GetIDispatchForObject(o: typing.Any) -> System.IntPtr:
        ...

    @staticmethod
    def GetIUnknownForObject(o: typing.Any) -> System.IntPtr:
        ...

    @staticmethod
    def GetLastPInvokeError() -> int:
        """
        Get the last platform invoke error on the current thread
        
        :returns: The last platform invoke error.
        """
        ...

    @staticmethod
    def GetLastPInvokeErrorMessage() -> str:
        """
        Gets the system error message for the last PInvoke error code.
        
        :returns: The error message associated with the last PInvoke error code.
        """
        ...

    @staticmethod
    @overload
    def GetLastSystemError() -> int:
        """
        Gets the last system error on the current thread.
        
        :returns: The last system error.
        """
        ...

    @staticmethod
    @overload
    def GetLastSystemError() -> int:
        ...

    @staticmethod
    def GetLastWin32Error() -> int:
        ...

    @staticmethod
    @overload
    def GetNativeVariantForObject(obj: typing.Any, pDstNativeVariant: System.IntPtr) -> None:
        ...

    @staticmethod
    @overload
    def GetNativeVariantForObject(obj: System_Runtime_InteropServices_Marshal_GetNativeVariantForObject_T, pDstNativeVariant: System.IntPtr) -> None:
        ...

    @staticmethod
    def GetObjectForIUnknown(pUnk: System.IntPtr) -> System.Object:
        ...

    @staticmethod
    @overload
    def GetObjectForNativeVariant(pSrcNativeVariant: System.IntPtr) -> System.Object:
        ...

    @staticmethod
    @overload
    def GetObjectForNativeVariant(pSrcNativeVariant: System.IntPtr) -> System_Runtime_InteropServices_Marshal_GetObjectForNativeVariant_T:
        ...

    @staticmethod
    @overload
    def GetObjectsForNativeVariants(aSrcNativeVariant: System.IntPtr, cVars: int) -> typing.List[System.Object]:
        ...

    @staticmethod
    @overload
    def GetObjectsForNativeVariants(aSrcNativeVariant: System.IntPtr, cVars: int) -> typing.List[System_Runtime_InteropServices_Marshal_GetObjectsForNativeVariants_T]:
        ...

    @staticmethod
    @overload
    def GetPInvokeErrorMessage(error: int) -> str:
        """
        Gets the system error message for the supplied error code.
        
        :param error: The error code.
        :returns: The error message associated with .
        """
        ...

    @staticmethod
    @overload
    def GetPInvokeErrorMessage(error: int) -> str:
        """
        Gets the system error message for the supplied error code.
        
        :param error: The error code.
        :returns: The error message associated with .
        """
        ...

    @staticmethod
    def GetStartComSlot(t: typing.Type) -> int:
        ...

    @staticmethod
    def GetTypedObjectForIUnknown(pUnk: System.IntPtr, t: typing.Type) -> System.Object:
        ...

    @staticmethod
    def GetTypeFromCLSID(clsid: System.Guid) -> typing.Type:
        ...

    @staticmethod
    def GetTypeInfoName(typeInfo: System.Runtime.InteropServices.ComTypes.ITypeInfo) -> str:
        ...

    @staticmethod
    def GetUniqueObjectForIUnknown(unknown: System.IntPtr) -> System.Object:
        ...

    @staticmethod
    def InitHandle(safeHandle: System.Runtime.InteropServices.SafeHandle, handle: System.IntPtr) -> None:
        """
        Initializes the underlying handle of a newly created SafeHandle to the provided value.
        
        :param safeHandle: The SafeHandle instance to update.
        :param handle: The pre-existing handle.
        """
        ...

    @staticmethod
    def IsComObject(o: typing.Any) -> bool:
        ...

    @staticmethod
    def IsTypeVisibleFromCom(t: typing.Type) -> bool:
        ...

    @staticmethod
    @overload
    def OffsetOf(fieldName: str) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def OffsetOf(t: typing.Type, fieldName: str) -> System.IntPtr:
        ...

    @staticmethod
    def Prelink(m: System.Reflection.MethodInfo) -> None:
        ...

    @staticmethod
    def PrelinkAll(c: typing.Type) -> None:
        ...

    @staticmethod
    @overload
    def PtrToStringAnsi(ptr: System.IntPtr) -> str:
        ...

    @staticmethod
    @overload
    def PtrToStringAnsi(ptr: System.IntPtr, len: int) -> str:
        ...

    @staticmethod
    @overload
    def PtrToStringAuto(ptr: System.IntPtr, len: int) -> str:
        ...

    @staticmethod
    @overload
    def PtrToStringAuto(ptr: System.IntPtr) -> str:
        ...

    @staticmethod
    @overload
    def PtrToStringAuto(ptr: System.IntPtr, len: int) -> str:
        ...

    @staticmethod
    @overload
    def PtrToStringAuto(ptr: System.IntPtr) -> str:
        ...

    @staticmethod
    def PtrToStringBSTR(ptr: System.IntPtr) -> str:
        ...

    @staticmethod
    @overload
    def PtrToStringUni(ptr: System.IntPtr) -> str:
        ...

    @staticmethod
    @overload
    def PtrToStringUni(ptr: System.IntPtr, len: int) -> str:
        ...

    @staticmethod
    @overload
    def PtrToStringUTF8(ptr: System.IntPtr) -> str:
        ...

    @staticmethod
    @overload
    def PtrToStringUTF8(ptr: System.IntPtr, byteLen: int) -> str:
        ...

    @staticmethod
    @overload
    def PtrToStructure(ptr: System.IntPtr, structureType: typing.Type) -> System.Object:
        """
        Creates a new instance of "structuretype" and marshals data from a
        native memory block to it.
        """
        ...

    @staticmethod
    @overload
    def PtrToStructure(ptr: System.IntPtr, structure: typing.Any) -> None:
        """Marshals data from a native memory block to a preallocated structure class."""
        ...

    @staticmethod
    @overload
    def PtrToStructure(ptr: System.IntPtr, structure: System_Runtime_InteropServices_Marshal_PtrToStructure_T) -> None:
        ...

    @staticmethod
    @overload
    def PtrToStructure(ptr: System.IntPtr) -> System_Runtime_InteropServices_Marshal_PtrToStructure_T:
        ...

    @staticmethod
    def QueryInterface(pUnk: System.IntPtr, iid: System.Guid, ppv: typing.Optional[System.IntPtr]) -> typing.Union[int, System.IntPtr]:
        ...

    @staticmethod
    @overload
    def ReadByte(ptr: System.IntPtr, ofs: int) -> int:
        ...

    @staticmethod
    @overload
    def ReadByte(ptr: System.IntPtr) -> int:
        ...

    @staticmethod
    @overload
    def ReadByte(ptr: typing.Any, ofs: int) -> int:
        """ReadByte(Object, Int32) may be unavailable in future releases."""
        ...

    @staticmethod
    @overload
    def ReadInt16(ptr: System.IntPtr, ofs: int) -> int:
        ...

    @staticmethod
    @overload
    def ReadInt16(ptr: System.IntPtr) -> int:
        ...

    @staticmethod
    @overload
    def ReadInt16(ptr: typing.Any, ofs: int) -> int:
        """ReadInt16(Object, Int32) may be unavailable in future releases."""
        ...

    @staticmethod
    @overload
    def ReadInt32(ptr: System.IntPtr, ofs: int) -> int:
        ...

    @staticmethod
    @overload
    def ReadInt32(ptr: System.IntPtr) -> int:
        ...

    @staticmethod
    @overload
    def ReadInt32(ptr: typing.Any, ofs: int) -> int:
        """ReadInt32(Object, Int32) may be unavailable in future releases."""
        ...

    @staticmethod
    @overload
    def ReadInt64(ptr: System.IntPtr, ofs: int) -> int:
        ...

    @staticmethod
    @overload
    def ReadInt64(ptr: System.IntPtr) -> int:
        ...

    @staticmethod
    @overload
    def ReadInt64(ptr: typing.Any, ofs: int) -> int:
        """ReadInt64(Object, Int32) may be unavailable in future releases."""
        ...

    @staticmethod
    @overload
    def ReadIntPtr(ptr: System.IntPtr, ofs: int) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def ReadIntPtr(ptr: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def ReadIntPtr(ptr: typing.Any, ofs: int) -> System.IntPtr:
        """ReadIntPtr(Object, Int32) may be unavailable in future releases."""
        ...

    @staticmethod
    @overload
    def ReAllocCoTaskMem(pv: System.IntPtr, cb: int) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def ReAllocCoTaskMem(pv: System.IntPtr, cb: int) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def ReAllocHGlobal(pv: System.IntPtr, cb: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def ReAllocHGlobal(pv: System.IntPtr, cb: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    def Release(pUnk: System.IntPtr) -> int:
        ...

    @staticmethod
    def ReleaseComObject(o: typing.Any) -> int:
        ...

    @staticmethod
    def SecureStringToBSTR(s: System.Security.SecureString) -> System.IntPtr:
        ...

    @staticmethod
    def SecureStringToCoTaskMemAnsi(s: System.Security.SecureString) -> System.IntPtr:
        ...

    @staticmethod
    def SecureStringToCoTaskMemUnicode(s: System.Security.SecureString) -> System.IntPtr:
        ...

    @staticmethod
    def SecureStringToGlobalAllocAnsi(s: System.Security.SecureString) -> System.IntPtr:
        ...

    @staticmethod
    def SecureStringToGlobalAllocUnicode(s: System.Security.SecureString) -> System.IntPtr:
        ...

    @staticmethod
    def SetComObjectData(obj: typing.Any, key: typing.Any, data: typing.Any) -> bool:
        ...

    @staticmethod
    def SetLastPInvokeError(error: int) -> None:
        """
        Set the last platform invoke error on the current thread
        
        :param error: Error to set
        """
        ...

    @staticmethod
    @overload
    def SetLastSystemError(error: int) -> None:
        """
        Sets the last system error on the current thread.
        
        :param error: The error to set.
        """
        ...

    @staticmethod
    @overload
    def SetLastSystemError(error: int) -> None:
        """
        Sets the last system error on the current thread.
        
        :param error: The error to set.
        """
        ...

    @staticmethod
    @overload
    def SizeOf(structure: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def SizeOf(structure: System_Runtime_InteropServices_Marshal_SizeOf_T) -> int:
        ...

    @staticmethod
    @overload
    def SizeOf(t: typing.Type) -> int:
        ...

    @staticmethod
    @overload
    def SizeOf() -> int:
        ...

    @staticmethod
    def StringToBSTR(s: str) -> System.IntPtr:
        ...

    @staticmethod
    def StringToCoTaskMemAnsi(s: str) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def StringToCoTaskMemAuto(s: str) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def StringToCoTaskMemAuto(s: str) -> System.IntPtr:
        ...

    @staticmethod
    def StringToCoTaskMemUni(s: str) -> System.IntPtr:
        ...

    @staticmethod
    def StringToCoTaskMemUTF8(s: str) -> System.IntPtr:
        ...

    @staticmethod
    def StringToHGlobalAnsi(s: str) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def StringToHGlobalAuto(s: str) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def StringToHGlobalAuto(s: str) -> System.IntPtr:
        ...

    @staticmethod
    def StringToHGlobalUni(s: str) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def StructureToPtr(structure: System_Runtime_InteropServices_Marshal_StructureToPtr_T, ptr: System.IntPtr, fDeleteOld: bool) -> None:
        ...

    @staticmethod
    @overload
    def StructureToPtr(structure: typing.Any, ptr: System.IntPtr, fDeleteOld: bool) -> None:
        ...

    @staticmethod
    @overload
    def ThrowExceptionForHR(errorCode: int) -> None:
        ...

    @staticmethod
    @overload
    def ThrowExceptionForHR(errorCode: int, errorInfo: System.IntPtr) -> None:
        ...

    @staticmethod
    @overload
    def UnsafeAddrOfPinnedArrayElement(arr: System.Array, index: int) -> System.IntPtr:
        """
        IMPORTANT NOTICE: This method does not do any verification on the array.
        It must be used with EXTREME CAUTION since passing in invalid index or
        an array that is not pinned can cause unexpected results.
        """
        ...

    @staticmethod
    @overload
    def UnsafeAddrOfPinnedArrayElement(arr: typing.List[System_Runtime_InteropServices_Marshal_UnsafeAddrOfPinnedArrayElement_T], index: int) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def WriteByte(ptr: System.IntPtr, ofs: int, val: int) -> None:
        ...

    @staticmethod
    @overload
    def WriteByte(ptr: System.IntPtr, val: int) -> None:
        ...

    @staticmethod
    @overload
    def WriteByte(ptr: typing.Any, ofs: int, val: int) -> None:
        """WriteByte(Object, Int32, Byte) may be unavailable in future releases."""
        ...

    @staticmethod
    @overload
    def WriteInt16(ptr: System.IntPtr, ofs: int, val: int) -> None:
        ...

    @staticmethod
    @overload
    def WriteInt16(ptr: System.IntPtr, val: int) -> None:
        ...

    @staticmethod
    @overload
    def WriteInt16(ptr: System.IntPtr, ofs: int, val: str) -> None:
        ...

    @staticmethod
    @overload
    def WriteInt16(ptr: System.IntPtr, val: str) -> None:
        ...

    @staticmethod
    @overload
    def WriteInt16(ptr: typing.Any, ofs: int, val: str) -> None:
        """WriteInt16(Object, Int32, Char) may be unavailable in future releases."""
        ...

    @staticmethod
    @overload
    def WriteInt16(ptr: typing.Any, ofs: int, val: int) -> None:
        """WriteInt16(Object, Int32, Int16) may be unavailable in future releases."""
        ...

    @staticmethod
    @overload
    def WriteInt32(ptr: System.IntPtr, ofs: int, val: int) -> None:
        ...

    @staticmethod
    @overload
    def WriteInt32(ptr: System.IntPtr, val: int) -> None:
        ...

    @staticmethod
    @overload
    def WriteInt32(ptr: typing.Any, ofs: int, val: int) -> None:
        """WriteInt32(Object, Int32, Int32) may be unavailable in future releases."""
        ...

    @staticmethod
    @overload
    def WriteInt64(ptr: System.IntPtr, ofs: int, val: int) -> None:
        ...

    @staticmethod
    @overload
    def WriteInt64(ptr: System.IntPtr, val: int) -> None:
        ...

    @staticmethod
    @overload
    def WriteInt64(ptr: typing.Any, ofs: int, val: int) -> None:
        """WriteInt64(Object, Int32, Int64) may be unavailable in future releases."""
        ...

    @staticmethod
    @overload
    def WriteIntPtr(ptr: System.IntPtr, ofs: int, val: System.IntPtr) -> None:
        ...

    @staticmethod
    @overload
    def WriteIntPtr(ptr: System.IntPtr, val: System.IntPtr) -> None:
        ...

    @staticmethod
    @overload
    def WriteIntPtr(ptr: typing.Any, ofs: int, val: System.IntPtr) -> None:
        """WriteIntPtr(Object, Int32, IntPtr) may be unavailable in future releases."""
        ...

    @staticmethod
    def ZeroFreeBSTR(s: System.IntPtr) -> None:
        ...

    @staticmethod
    def ZeroFreeCoTaskMemAnsi(s: System.IntPtr) -> None:
        ...

    @staticmethod
    def ZeroFreeCoTaskMemUnicode(s: System.IntPtr) -> None:
        ...

    @staticmethod
    def ZeroFreeCoTaskMemUTF8(s: System.IntPtr) -> None:
        ...

    @staticmethod
    def ZeroFreeGlobalAllocAnsi(s: System.IntPtr) -> None:
        ...

    @staticmethod
    def ZeroFreeGlobalAllocUnicode(s: System.IntPtr) -> None:
        ...


class ComImportAttribute(System.Attribute):
    """This class has no documentation."""


class ArrayWithOffset(System.IEquatable[System_Runtime_InteropServices_ArrayWithOffset]):
    """This class has no documentation."""

    def __init__(self, array: typing.Any, offset: int) -> None:
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def Equals(self, obj: System.Runtime.InteropServices.ArrayWithOffset) -> bool:
        ...

    def GetArray(self) -> System.Object:
        ...

    def GetHashCode(self) -> int:
        ...

    def GetOffset(self) -> int:
        ...


class ComDefaultInterfaceAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Value(self) -> typing.Type:
        ...

    def __init__(self, defaultInterface: typing.Type) -> None:
        ...


class ComInterfaceType(System.Enum):
    """This class has no documentation."""

    InterfaceIsDual = 0

    InterfaceIsIUnknown = 1

    InterfaceIsIDispatch = 2

    InterfaceIsIInspectable = 3


class InterfaceTypeAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Value(self) -> int:
        """This property contains the int value of a member of the System.Runtime.InteropServices.ComInterfaceType enum."""
        ...

    @overload
    def __init__(self, interfaceType: System.Runtime.InteropServices.ComInterfaceType) -> None:
        ...

    @overload
    def __init__(self, interfaceType: int) -> None:
        ...


class VarEnum(System.Enum):
    """This class has no documentation."""

    VT_EMPTY = 0

    VT_NULL = 1

    VT_I2 = 2

    VT_I4 = 3

    VT_R4 = 4

    VT_R8 = 5

    VT_CY = 6

    VT_DATE = 7

    VT_BSTR = 8

    VT_DISPATCH = 9

    VT_ERROR = 10

    VT_BOOL = 11

    VT_VARIANT = 12

    VT_UNKNOWN = 13

    VT_DECIMAL = 14

    VT_I1 = 16

    VT_UI1 = 17

    VT_UI2 = 18

    VT_UI4 = 19

    VT_I8 = 20

    VT_UI8 = 21

    VT_INT = 22

    VT_UINT = 23

    VT_VOID = 24

    VT_HRESULT = 25

    VT_PTR = 26

    VT_SAFEARRAY = 27

    VT_CARRAY = 28

    VT_USERDEFINED = 29

    VT_LPSTR = 30

    VT_LPWSTR = 31

    VT_RECORD = 36

    VT_FILETIME = 64

    VT_BLOB = 65

    VT_STREAM = 66

    VT_STORAGE = 67

    VT_STREAMED_OBJECT = 68

    VT_STORED_OBJECT = 69

    VT_BLOB_OBJECT = 70

    VT_CF = 71

    VT_CLSID = 72

    VT_VECTOR = ...

    VT_ARRAY = ...

    VT_BYREF = ...


class UnmanagedType(System.Enum):
    """This class has no documentation."""

    Bool = ...

    I1 = ...

    U1 = ...

    I2 = ...

    U2 = ...

    I4 = ...

    U4 = ...

    I8 = ...

    U8 = ...

    R4 = ...

    R8 = ...

    Currency = ...

    BStr = ...

    LPStr = ...

    LPWStr = ...

    LPTStr = ...

    ByValTStr = ...

    IUnknown = ...

    IDispatch = ...

    Struct = ...

    Interface = ...

    SafeArray = ...

    ByValArray = ...

    SysInt = ...

    SysUInt = ...

    VBByRefStr = ...

    AnsiBStr = ...

    TBStr = ...

    VariantBool = ...

    FunctionPtr = ...

    AsAny = ...

    LPArray = ...

    LPStruct = ...

    CustomMarshaler = ...

    Error = ...

    IInspectable = ...

    HString = ...

    LPUTF8Str = ...


class MarshalAsAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Value(self) -> int:
        """This property contains the int value of a member of the System.Runtime.InteropServices.UnmanagedType enum."""
        ...

    @property
    def SafeArraySubType(self) -> System.Runtime.InteropServices.VarEnum:
        ...

    @SafeArraySubType.setter
    def SafeArraySubType(self, value: System.Runtime.InteropServices.VarEnum):
        ...

    @property
    def SafeArrayUserDefinedSubType(self) -> typing.Type:
        ...

    @SafeArrayUserDefinedSubType.setter
    def SafeArrayUserDefinedSubType(self, value: typing.Type):
        ...

    @property
    def IidParameterIndex(self) -> int:
        ...

    @IidParameterIndex.setter
    def IidParameterIndex(self, value: int):
        ...

    @property
    def ArraySubType(self) -> System.Runtime.InteropServices.UnmanagedType:
        ...

    @ArraySubType.setter
    def ArraySubType(self, value: System.Runtime.InteropServices.UnmanagedType):
        ...

    @property
    def SizeParamIndex(self) -> int:
        ...

    @SizeParamIndex.setter
    def SizeParamIndex(self, value: int):
        ...

    @property
    def SizeConst(self) -> int:
        ...

    @SizeConst.setter
    def SizeConst(self, value: int):
        ...

    @property
    def MarshalType(self) -> str:
        ...

    @MarshalType.setter
    def MarshalType(self, value: str):
        ...

    @property
    def MarshalTypeRef(self) -> typing.Type:
        ...

    @MarshalTypeRef.setter
    def MarshalTypeRef(self, value: typing.Type):
        ...

    @property
    def MarshalCookie(self) -> str:
        ...

    @MarshalCookie.setter
    def MarshalCookie(self, value: str):
        ...

    @overload
    def __init__(self, unmanagedType: System.Runtime.InteropServices.UnmanagedType) -> None:
        ...

    @overload
    def __init__(self, unmanagedType: int) -> None:
        ...


class PosixSignal(System.Enum):
    """Specifies a POSIX signal number."""

    SIGHUP = -1
    """Hangup"""

    SIGINT = -2
    """Interrupt"""

    SIGQUIT = -3
    """Quit"""

    SIGTERM = -4
    """Termination"""

    SIGCHLD = -5
    """Child stopped"""

    SIGCONT = -6
    """Continue if stopped"""

    SIGWINCH = -7
    """Window resized"""

    SIGTTIN = -8
    """Terminal input for background process"""

    SIGTTOU = -9
    """Terminal output for background process"""

    SIGTSTP = -10
    """Stop typed at terminal"""


class PosixSignalContext(System.Object):
    """Provides data for a PosixSignalRegistration event."""

    @property
    def Signal(self) -> int:
        """
        Gets the signal that occurred.
        
        This property contains the int value of a member of the System.Runtime.InteropServices.PosixSignal enum.
        """
        ...

    @Signal.setter
    def Signal(self, value: int):
        """
        Gets the signal that occurred.
        
        This property contains the int value of a member of the System.Runtime.InteropServices.PosixSignal enum.
        """
        ...

    @property
    def Cancel(self) -> bool:
        """Gets or sets a value that indicates whether to cancel the default handling of the signal. The default is false."""
        ...

    @Cancel.setter
    def Cancel(self, value: bool):
        """Gets or sets a value that indicates whether to cancel the default handling of the signal. The default is false."""
        ...

    def __init__(self, signal: System.Runtime.InteropServices.PosixSignal) -> None:
        """Initializes a new instance of the PosixSignalContext class."""
        ...


class PosixSignalRegistration(System.Object, System.IDisposable):
    """Handles a PosixSignal."""

    @staticmethod
    def Create(signal: System.Runtime.InteropServices.PosixSignal, handler: typing.Callable[[System.Runtime.InteropServices.PosixSignalContext], None]) -> System.Runtime.InteropServices.PosixSignalRegistration:
        """
        Registers a  that is invoked when the  occurs.
        
        :param signal: The signal to register for.
        :param handler: The handler that gets invoked.
        :returns: A PosixSignalRegistration instance that can be disposed to unregister the handler.
        """
        ...

    def Dispose(self) -> None:
        """Unregister the handler."""
        ...

    def Unregister(self) -> None:
        ...


class SafeBuffer(Microsoft.Win32.SafeHandles.SafeHandleZeroOrMinusOneIsInvalid, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def ByteLength(self) -> int:
        """Returns the number of bytes in the memory region."""
        ...

    def __init__(self, ownsHandle: bool) -> None:
        """This method is protected."""
        ...

    def AcquirePointer(self, pointer: typing.Any) -> None:
        ...

    @overload
    def Initialize(self, numBytes: int) -> None:
        """
        Specifies the size of the region of memory, in bytes.  Must be
        called before using the SafeBuffer.
        
        :param numBytes: Number of valid bytes in memory.
        """
        ...

    @overload
    def Initialize(self, numElements: int, sizeOfEachElement: int) -> None:
        """
        Specifies the size of the region in memory, as the number of
        elements in an array.  Must be called before using the SafeBuffer.
        """
        ...

    @overload
    def Initialize(self, numElements: int) -> None:
        """
        Specifies the size of the region in memory, as the number of
        elements in an array.  Must be called before using the SafeBuffer.
        """
        ...

    def Read(self, byteOffset: int) -> System_Runtime_InteropServices_SafeBuffer_Read_T:
        """
        Read a value type from memory at the given offset.  This is
        equivalent to:  return *(T*)(bytePtr + byteOffset);
        
        :param byteOffset: Where to start reading from memory.  You may have to consider alignment.
        :returns: An instance of T read from memory.
        """
        ...

    def ReadArray(self, byteOffset: int, array: typing.List[System_Runtime_InteropServices_SafeBuffer_ReadArray_T], index: int, count: int) -> None:
        """
        Reads the specified number of value types from memory starting at the offset, and writes them into an array starting at the index.
        
        :param byteOffset: The location from which to start reading.
        :param array: The output array to write to.
        :param index: The location in the output array to begin writing to.
        :param count: The number of value types to read from the input array and to write to the output array.
        """
        ...

    def ReadSpan(self, byteOffset: int, buffer: System.Span[System_Runtime_InteropServices_SafeBuffer_ReadSpan_T]) -> None:
        """
        Reads value types from memory starting at the offset, and writes them into a span. The number of value types that will be read is determined by the length of the span.
        
        :param byteOffset: The location from which to start reading.
        :param buffer: The output span to write to.
        """
        ...

    def ReleasePointer(self) -> None:
        ...

    def Write(self, byteOffset: int, value: System_Runtime_InteropServices_SafeBuffer_Write_T) -> None:
        """
        Write a value type to memory at the given offset.  This is
        equivalent to:  *(T*)(bytePtr + byteOffset) = value;
        
        :param byteOffset: The location in memory to write to.  You may have to consider alignment.
        :param value: The value type to write to memory.
        """
        ...

    def WriteArray(self, byteOffset: int, array: typing.List[System_Runtime_InteropServices_SafeBuffer_WriteArray_T], index: int, count: int) -> None:
        """
        Writes the specified number of value types to a memory location by reading bytes starting from the specified location in the input array.
        
        :param byteOffset: The location in memory to write to.
        :param array: The input array.
        :param index: The offset in the array to start reading from.
        :param count: The number of value types to write.
        """
        ...

    def WriteSpan(self, byteOffset: int, data: System.ReadOnlySpan[System_Runtime_InteropServices_SafeBuffer_WriteSpan_T]) -> None:
        """
        Writes the value types from a read-only span to a memory location.
        
        :param byteOffset: The location in memory to write to.
        :param data: The input span.
        """
        ...


class InvalidOleVariantTypeException(System.SystemException):
    """
    Exception thrown when the type of an OLE variant that was passed into the
    runtime is invalid.
    """

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...


class CreateComInterfaceFlags(System.Enum):
    """Enumeration of flags for ComWrappers.GetOrCreateComInterfaceForObject(object, CreateComInterfaceFlags)."""

    # Cannot convert to Python: None = 0

    CallerDefinedIUnknown = 1
    """The caller will provide an IUnknown Vtable."""

    TrackerSupport = 2
    """
    Flag used to indicate the COM interface should implement https://docs.microsoft.com/windows/win32/api/windows.ui.xaml.hosting.referencetracker/nn-windows-ui-xaml-hosting-referencetracker-ireferencetrackertarget.
    When this flag is passed, the resulting COM interface will have an internal implementation of IUnknown
    and as such none should be supplied by the caller.
    """


class CreateObjectFlags(System.Enum):
    """Enumeration of flags for ComWrappers.GetOrCreateObjectForComInstance(IntPtr, CreateObjectFlags)."""

    # Cannot convert to Python: None = 0

    TrackerObject = 1
    """Indicate if the supplied external COM object implements the https://docs.microsoft.com/windows/win32/api/windows.ui.xaml.hosting.referencetracker/nn-windows-ui-xaml-hosting-referencetracker-ireferencetracker."""

    UniqueInstance = 2
    """Ignore any internal caching and always create a unique instance."""

    Aggregation = 4
    """Defined when COM aggregation is involved (that is an inner instance supplied)."""

    Unwrap = 8
    """
    Check if the supplied instance is actually a wrapper and if so return the underlying
    managed object rather than creating a new wrapper.
    """


class ComWrappers(System.Object, metaclass=abc.ABCMeta):
    """Class for managing wrappers of COM IUnknown types."""

    class ComInterfaceEntry:
        """Interface type and pointer to targeted VTable."""

        @property
        def IID(self) -> System.Guid:
            """Interface IID."""
            ...

        @IID.setter
        def IID(self, value: System.Guid):
            """Interface IID."""
            ...

        @property
        def Vtable(self) -> System.IntPtr:
            """Memory must have the same lifetime as the memory returned from the call to ComputeVtables(object, CreateComInterfaceFlags, out int)."""
            ...

        @Vtable.setter
        def Vtable(self, value: System.IntPtr):
            """Memory must have the same lifetime as the memory returned from the call to ComputeVtables(object, CreateComInterfaceFlags, out int)."""
            ...

    class ComInterfaceDispatch:
        """ABI for function dispatch of a COM interface."""

        @property
        def Vtable(self) -> System.IntPtr:
            ...

        @Vtable.setter
        def Vtable(self, value: System.IntPtr):
            ...

        @staticmethod
        def GetInstance(dispatchPtr: typing.Any) -> System_Runtime_InteropServices_ComWrappers_GetInstance_ComInterfaceDispatch_T:
            ...

    def ComputeVtables(self, obj: typing.Any, flags: System.Runtime.InteropServices.CreateComInterfaceFlags, count: typing.Optional[int]) -> typing.Union[typing.Any, int]:
        """
        Compute the desired Vtable for  respecting the values of .
        
        This method is protected.
        
        :param obj: Target of the returned Vtables.
        :param flags: Flags used to compute Vtables.
        :param count: The number of elements contained in the returned memory.
        :returns: ComInterfaceEntry pointer containing memory for all COM interface entries.
        """
        ...

    def CreateObject(self, externalComObject: System.IntPtr, flags: System.Runtime.InteropServices.CreateObjectFlags) -> System.Object:
        """
        Create a managed object for the object pointed at by  respecting the values of .
        
        This method is protected.
        
        :param externalComObject: Object to import for usage into the .NET runtime.
        :param flags: Flags used to describe the external object.
        :returns: Returns a managed object associated with the supplied external COM object.
        """
        ...

    @staticmethod
    def GetIUnknownImpl(fpQueryInterface: typing.Optional[System.IntPtr], fpAddRef: typing.Optional[System.IntPtr], fpRelease: typing.Optional[System.IntPtr]) -> typing.Union[None, System.IntPtr, System.IntPtr, System.IntPtr]:
        """This method is protected."""
        ...

    def GetOrCreateComInterfaceForObject(self, instance: typing.Any, flags: System.Runtime.InteropServices.CreateComInterfaceFlags) -> System.IntPtr:
        ...

    def GetOrCreateObjectForComInstance(self, externalComObject: System.IntPtr, flags: System.Runtime.InteropServices.CreateObjectFlags) -> System.Object:
        ...

    @overload
    def GetOrRegisterObjectForComInstance(self, externalComObject: System.IntPtr, flags: System.Runtime.InteropServices.CreateObjectFlags, wrapper: typing.Any) -> System.Object:
        ...

    @overload
    def GetOrRegisterObjectForComInstance(self, externalComObject: System.IntPtr, flags: System.Runtime.InteropServices.CreateObjectFlags, wrapper: typing.Any, inner: System.IntPtr) -> System.Object:
        ...

    @staticmethod
    def RegisterForMarshalling(instance: System.Runtime.InteropServices.ComWrappers) -> None:
        ...

    @staticmethod
    def RegisterForTrackerSupport(instance: System.Runtime.InteropServices.ComWrappers) -> None:
        ...

    def ReleaseObjects(self, objects: System.Collections.IEnumerable) -> None:
        """
        Called when a request is made for a collection of objects to be released outside of normal object or COM interface lifetime.
        
        This method is protected.
        
        :param objects: Collection of objects to release.
        """
        ...


class IDynamicInterfaceCastable(metaclass=abc.ABCMeta):
    """Interface used to participate in a type cast failure."""

    def GetInterfaceImplementation(self, interfaceType: System.RuntimeTypeHandle) -> System.RuntimeTypeHandle:
        """
        Called during interface dispatch when the given interface type cannot be found
        in the class's metadata.
        
        :param interfaceType: The interface type.
        :returns: The type that should be used to dispatch for  on the current object.
        """
        ...

    def IsInterfaceImplemented(self, interfaceType: System.RuntimeTypeHandle, throwIfNotImplemented: bool) -> bool:
        """
        Called when an implementing class instance is cast to an interface type that
        is not contained in the class's metadata.
        
        :param interfaceType: The interface type.
        :param throwIfNotImplemented: Indicates if the function should throw an exception instead of returning false.
        :returns: Whether or not this object can be cast to the given interface.
        """
        ...


class DynamicInterfaceCastableImplementationAttribute(System.Attribute):
    """Attribute required by any type that is returned by IDynamicInterfaceCastable.GetInterfaceImplementation(RuntimeTypeHandle)."""

    def __init__(self) -> None:
        ...


class InvalidComObjectException(System.SystemException):
    """
    The exception thrown when an invalid COM object is used. This happens
    when a the __ComObject type is used directly without having a backing
    class factory.
    """

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...


class BStrWrapper(System.Object):
    """This class has no documentation."""

    @property
    def WrappedObject(self) -> str:
        ...

    @overload
    def __init__(self, value: str) -> None:
        ...

    @overload
    def __init__(self, value: typing.Any) -> None:
        ...


class AllowReversePInvokeCallsAttribute(System.Attribute):
    """Obsoletions.CodeAccessSecurityMessage"""

    def __init__(self) -> None:
        ...


class CustomQueryInterfaceResult(System.Enum):
    """This class has no documentation."""

    Handled = 0

    NotHandled = 1

    Failed = 2


class TypeIdentifierAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Scope(self) -> str:
        ...

    @property
    def Identifier(self) -> str:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, scope: str, identifier: str) -> None:
        ...


class VariantWrapper(System.Object):
    """This class has no documentation."""

    @property
    def WrappedObject(self) -> System.Object:
        ...

    def __init__(self, obj: typing.Any) -> None:
        ...


class ComMemberType(System.Enum):
    """This class has no documentation."""

    Method = 0

    PropGet = 1

    PropSet = 2


class DefaultCharSetAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def CharSet(self) -> int:
        """This property contains the int value of a member of the System.Runtime.InteropServices.CharSet enum."""
        ...

    def __init__(self, charSet: System.Runtime.InteropServices.CharSet) -> None:
        ...


class NativeMemory(System.Object):
    """This class contains methods that are mainly used to manage native memory."""

    @staticmethod
    @overload
    def AlignedAlloc(byteCount: System.UIntPtr, alignment: System.UIntPtr) -> typing.Any:
        """
        Allocates an aligned block of memory of the specified size and alignment, in bytes.
        
        :param byteCount: The size, in bytes, of the block to allocate.
        :param alignment: The alignment, in bytes, of the block to allocate. This must be a power of 2.
        :returns: A pointer to the allocated aligned block of memory.
        """
        ...

    @staticmethod
    @overload
    def AlignedAlloc(byteCount: System.UIntPtr, alignment: System.UIntPtr) -> typing.Any:
        """
        Allocates an aligned block of memory of the specified size and alignment, in bytes.
        
        :param byteCount: The size, in bytes, of the block to allocate.
        :param alignment: The alignment, in bytes, of the block to allocate. This must be a power of 2.
        :returns: A pointer to the allocated aligned block of memory.
        """
        ...

    @staticmethod
    @overload
    def AlignedFree(ptr: typing.Any) -> None:
        """
        Frees an aligned block of memory.
        
        :param ptr: A pointer to the aligned block of memory that should be freed.
        """
        ...

    @staticmethod
    @overload
    def AlignedFree(ptr: typing.Any) -> None:
        """
        Frees an aligned block of memory.
        
        :param ptr: A pointer to the aligned block of memory that should be freed.
        """
        ...

    @staticmethod
    @overload
    def AlignedRealloc(ptr: typing.Any, byteCount: System.UIntPtr, alignment: System.UIntPtr) -> typing.Any:
        """
        Reallocates an aligned block of memory of the specified size and alignment, in bytes.
        
        :param ptr: The previously allocated block of memory.
        :param byteCount: The size, in bytes, of the block to allocate.
        :param alignment: The alignment, in bytes, of the block to allocate. This must be a power of 2.
        :returns: A pointer to the reallocated aligned block of memory.
        """
        ...

    @staticmethod
    @overload
    def AlignedRealloc(ptr: typing.Any, byteCount: System.UIntPtr, alignment: System.UIntPtr) -> typing.Any:
        """
        Reallocates an aligned block of memory of the specified size and alignment, in bytes.
        
        :param ptr: The previously allocated block of memory.
        :param byteCount: The size, in bytes, of the block to allocate.
        :param alignment: The alignment, in bytes, of the block to allocate. This must be a power of 2.
        :returns: A pointer to the reallocated aligned block of memory.
        """
        ...

    @staticmethod
    @overload
    def Alloc(byteCount: System.UIntPtr) -> typing.Any:
        """
        Allocates a block of memory of the specified size, in bytes.
        
        :param byteCount: The size, in bytes, of the block to allocate.
        :returns: A pointer to the allocated block of memory.
        """
        ...

    @staticmethod
    @overload
    def Alloc(elementCount: System.UIntPtr, elementSize: System.UIntPtr) -> typing.Any:
        """
        Allocates a block of memory of the specified size, in elements.
        
        :param elementCount: The count, in elements, of the block to allocate.
        :param elementSize: The size, in bytes, of each element in the allocation.
        :returns: A pointer to the allocated block of memory.
        """
        ...

    @staticmethod
    @overload
    def Alloc(byteCount: System.UIntPtr) -> typing.Any:
        """
        Allocates a block of memory of the specified size, in bytes.
        
        :param byteCount: The size, in bytes, of the block to allocate.
        :returns: A pointer to the allocated block of memory.
        """
        ...

    @staticmethod
    @overload
    def AllocZeroed(elementCount: System.UIntPtr, elementSize: System.UIntPtr) -> typing.Any:
        """
        Allocates and zeroes a block of memory of the specified size, in elements.
        
        :param elementCount: The count, in elements, of the block to allocate.
        :param elementSize: The size, in bytes, of each element in the allocation.
        :returns: A pointer to the allocated and zeroed block of memory.
        """
        ...

    @staticmethod
    @overload
    def AllocZeroed(byteCount: System.UIntPtr) -> typing.Any:
        """
        Allocates and zeroes a block of memory of the specified size, in bytes.
        
        :param byteCount: The size, in bytes, of the block to allocate.
        :returns: A pointer to the allocated and zeroed block of memory.
        """
        ...

    @staticmethod
    @overload
    def AllocZeroed(elementCount: System.UIntPtr, elementSize: System.UIntPtr) -> typing.Any:
        """
        Allocates and zeroes a block of memory of the specified size, in elements.
        
        :param elementCount: The count, in elements, of the block to allocate.
        :param elementSize: The size, in bytes, of each element in the allocation.
        :returns: A pointer to the allocated and zeroed block of memory.
        """
        ...

    @staticmethod
    def Clear(ptr: typing.Any, byteCount: System.UIntPtr) -> None:
        """
        Clears a block of memory.
        
        :param ptr: A pointer to the block of memory that should be cleared.
        :param byteCount: The size, in bytes, of the block to clear.
        """
        ...

    @staticmethod
    def Copy(source: typing.Any, destination: typing.Any, byteCount: System.UIntPtr) -> None:
        """
        Copies a block of memory from memory location 
        to memory location .
        
        :param source: A pointer to the source of data to be copied.
        :param destination: A pointer to the destination memory block where the data is to be copied.
        :param byteCount: The size, in bytes, to be copied from the source location to the destination.
        """
        ...

    @staticmethod
    def Fill(ptr: typing.Any, byteCount: System.UIntPtr, value: int) -> None:
        """
        Copies the byte  to the first  bytes
        of the memory located at .
        
        :param ptr: A pointer to the block of memory to fill.
        :param byteCount: The number of bytes to be set to .
        :param value: The value to be set.
        """
        ...

    @staticmethod
    @overload
    def Free(ptr: typing.Any) -> None:
        """
        Frees a block of memory.
        
        :param ptr: A pointer to the block of memory that should be freed.
        """
        ...

    @staticmethod
    @overload
    def Free(ptr: typing.Any) -> None:
        """
        Frees a block of memory.
        
        :param ptr: A pointer to the block of memory that should be freed.
        """
        ...

    @staticmethod
    @overload
    def Realloc(ptr: typing.Any, byteCount: System.UIntPtr) -> typing.Any:
        """
        Reallocates a block of memory to be the specified size, in bytes.
        
        :param ptr: The previously allocated block of memory.
        :param byteCount: The size, in bytes, of the reallocated block.
        :returns: A pointer to the reallocated block of memory.
        """
        ...

    @staticmethod
    @overload
    def Realloc(ptr: typing.Any, byteCount: System.UIntPtr) -> typing.Any:
        """
        Reallocates a block of memory to be the specified size, in bytes.
        
        :param ptr: The previously allocated block of memory.
        :param byteCount: The size, in bytes, of the reallocated block.
        :returns: A pointer to the reallocated block of memory.
        """
        ...


class MarshalDirectiveException(System.SystemException):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...


class UnknownWrapper(System.Object):
    """This class has no documentation."""

    @property
    def WrappedObject(self) -> System.Object:
        ...

    def __init__(self, obj: typing.Any) -> None:
        ...


class ComEventsHelper(System.Object):
    """This class has no documentation."""

    @staticmethod
    def Combine(rcw: typing.Any, iid: System.Guid, dispid: int, d: System.Delegate) -> None:
        ...

    @staticmethod
    def Remove(rcw: typing.Any, iid: System.Guid, dispid: int, d: System.Delegate) -> System.Delegate:
        ...


class GCHandleType(System.Enum):
    """This class has no documentation."""

    Weak = 0

    WeakTrackResurrection = 1

    Normal = 2

    Pinned = 3


class PreserveSigAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class InAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class DllImportSearchPath(System.Enum):
    """This class has no documentation."""

    UseDllDirectoryForDependencies = ...

    ApplicationDirectory = ...

    UserDirectories = ...

    System32 = ...

    SafeDirectories = ...

    AssemblyDirectory = ...

    LegacyBehavior = ...


class NativeLibrary(System.Object):
    """APIs for managing Native Libraries"""

    @staticmethod
    def Free(handle: System.IntPtr) -> None:
        """
        Free a loaded library
        Given a library handle, free it.
        No action if the input handle is null.
        
        :param handle: The native library handle to be freed.
        """
        ...

    @staticmethod
    def GetExport(handle: System.IntPtr, name: str) -> System.IntPtr:
        """
        Get the address of an exported Symbol
        This is a simple wrapper around OS calls, and does not perform any name mangling.
        
        :param handle: The native library handle.
        :param name: The name of the exported symbol.
        :returns: The address of the symbol.
        """
        ...

    @staticmethod
    def GetMainProgramHandle() -> System.IntPtr:
        """
        Get a handle that can be used with GetExport or TryGetExport to resolve exports from the entry point module.
        
        :returns: The handle that can be used to resolve exports from the entry point module.
        """
        ...

    @staticmethod
    @overload
    def Load(libraryPath: str) -> System.IntPtr:
        """
        NativeLibrary Loader: Simple API
        This method is a wrapper around OS loader, using "default" flags.
        
        :param libraryPath: The name of the native library to be loaded.
        :returns: The handle for the loaded native library.
        """
        ...

    @staticmethod
    @overload
    def Load(libraryName: str, assembly: System.Reflection.Assembly, searchPath: typing.Optional[System.Runtime.InteropServices.DllImportSearchPath]) -> System.IntPtr:
        """
        NativeLibrary Loader: High-level API
        Given a library name, this function searches specific paths based on the
        runtime configuration, input parameters, and attributes of the calling assembly.
        If DllImportSearchPath parameter is non-null, the flags in this enumeration are used.
        Otherwise, the flags specified by the DefaultDllImportSearchPaths attribute on the
        calling assembly (if any) are used.
        This method follows the native library resolution for the AssemblyLoadContext of the
        specified assembly. It will invoke the managed extension points:
        * AssemblyLoadContext.LoadUnmanagedDll()
        * AssemblyLoadContext.ResolvingUnmanagedDllEvent
        It does not invoke extension points that are not tied to the AssemblyLoadContext:
        * The per-assembly registered DllImportResolver callback
        
        :param libraryName: The name of the native library to be loaded.
        :param assembly: The assembly loading the native library.
        :param searchPath: The search path.
        :returns: The handle for the loaded library.
        """
        ...

    @staticmethod
    def SetDllImportResolver(assembly: System.Reflection.Assembly, resolver: typing.Callable[[str, System.Reflection.Assembly, typing.Optional[System.Runtime.InteropServices.DllImportSearchPath]], System.IntPtr]) -> None:
        """
        Set a callback for resolving native library imports from an assembly.
        This per-assembly resolver is the first attempt to resolve native library loads
        initiated by this assembly.
        
        Only one resolver can be registered per assembly.
        Trying to register a second resolver fails with InvalidOperationException.
        
        :param assembly: The assembly for which the resolver is registered.
        :param resolver: The resolver callback to register.
        """
        ...

    @staticmethod
    def TryGetExport(handle: System.IntPtr, name: str, address: typing.Optional[System.IntPtr]) -> typing.Union[bool, System.IntPtr]:
        """
        Get the address of an exported Symbol, but do not throw
        
        :param handle: The  native library handle.
        :param name: The name of the exported symbol.
        :param address: The out-parameter for the symbol address, if it exists.
        :returns: True on success, false otherwise.
        """
        ...

    @staticmethod
    @overload
    def TryLoad(libraryPath: str, handle: typing.Optional[System.IntPtr]) -> typing.Union[bool, System.IntPtr]:
        """
        NativeLibrary Loader: Simple API that doesn't throw
        
        :param libraryPath: The name of the native library to be loaded.
        :param handle: The out-parameter for the loaded native library handle.
        :returns: True on successful load, false otherwise.
        """
        ...

    @staticmethod
    @overload
    def TryLoad(libraryName: str, assembly: System.Reflection.Assembly, searchPath: typing.Optional[System.Runtime.InteropServices.DllImportSearchPath], handle: typing.Optional[System.IntPtr]) -> typing.Union[bool, System.IntPtr]:
        """
        NativeLibrary Loader: High-level API that doesn't throw.
        Given a library name, this function searches specific paths based on the
        runtime configuration, input parameters, and attributes of the calling assembly.
        If DllImportSearchPath parameter is non-null, the flags in this enumeration are used.
        Otherwise, the flags specified by the DefaultDllImportSearchPaths attribute on the
        calling assembly (if any) are used.
        This method follows the native library resolution for the AssemblyLoadContext of the
        specified assembly. It will invoke the managed extension points:
        * AssemblyLoadContext.LoadUnmanagedDll()
        * AssemblyLoadContext.ResolvingUnmanagedDllEvent
        It does not invoke extension points that are not tied to the AssemblyLoadContext:
        * The per-assembly registered DllImportResolver callback
        
        :param libraryName: The name of the native library to be loaded.
        :param assembly: The assembly loading the native library.
        :param searchPath: The search path.
        :param handle: The out-parameter for the loaded native library handle.
        :returns: True on successful load, false otherwise.
        """
        ...


class LCIDConversionAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Value(self) -> int:
        ...

    def __init__(self, lcid: int) -> None:
        ...


class Architecture(System.Enum):
    """Indicates the processor architecture."""

    X86 = 0
    """An Intel-based 32-bit processor architecture."""

    X64 = 1
    """An Intel-based 64-bit processor architecture."""

    Arm = 2
    """A 32-bit ARM processor architecture."""

    Arm64 = 3
    """A 64-bit ARM processor architecture."""

    Wasm = 4
    """The WebAssembly platform."""

    S390x = 5
    """A S390x platform architecture."""

    LoongArch64 = 6
    """A LoongArch64 processor architecture."""

    Armv6 = 7
    """A 32-bit ARMv6 processor architecture."""

    Ppc64le = 8
    """A PowerPC 64-bit (little-endian) processor architecture."""


class OSPlatform(System.IEquatable[System_Runtime_InteropServices_OSPlatform]):
    """This class has no documentation."""

    FreeBSD: System.Runtime.InteropServices.OSPlatform

    Linux: System.Runtime.InteropServices.OSPlatform

    OSX: System.Runtime.InteropServices.OSPlatform

    Windows: System.Runtime.InteropServices.OSPlatform

    @property
    def Name(self) -> str:
        ...

    @staticmethod
    def Create(osPlatform: str) -> System.Runtime.InteropServices.OSPlatform:
        """Creates a new OSPlatform instance."""
        ...

    @overload
    def Equals(self, other: System.Runtime.InteropServices.OSPlatform) -> bool:
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        ...

    def GetHashCode(self) -> int:
        ...

    def ToString(self) -> str:
        ...


class RuntimeInformation(System.Object):
    """This class has no documentation."""

    OSDescription: str

    OSArchitecture: int
    """This property contains the int value of a member of the System.Runtime.InteropServices.Architecture enum."""

    FrameworkDescription: str

    RuntimeIdentifier: str
    """Returns an opaque string that identifies the platform on which an app is running."""

    ProcessArchitecture: System.Runtime.InteropServices.Architecture

    @staticmethod
    def IsOSPlatform(osPlatform: System.Runtime.InteropServices.OSPlatform) -> bool:
        """Indicates whether the current application is running on the specified platform."""
        ...


class HandleRef:
    """This class has no documentation."""

    @property
    def Wrapper(self) -> System.Object:
        ...

    @property
    def Handle(self) -> System.IntPtr:
        ...

    def __init__(self, wrapper: typing.Any, handle: System.IntPtr) -> None:
        ...

    @staticmethod
    def ToIntPtr(value: System.Runtime.InteropServices.HandleRef) -> System.IntPtr:
        ...


class GuidAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Value(self) -> str:
        ...

    def __init__(self, guid: str) -> None:
        ...


class DispatchWrapper(System.Object):
    """This class has no documentation."""

    @property
    def WrappedObject(self) -> System.Object:
        ...

    def __init__(self, obj: typing.Any) -> None:
        ...


class CULong(System.IEquatable[System_Runtime_InteropServices_CULong]):
    """
    CULong is an immutable value type that represents the unsigned long type in C and C++.
    It is meant to be used as an exchange type at the managed/unmanaged boundary to accurately represent
    in managed code unmanaged APIs that use the unsigned long type.
    This type has 32-bits of storage on all Windows platforms and 32-bit Unix-based platforms.
    It has 64-bits of storage on 64-bit Unix platforms.
    """

    @property
    def Value(self) -> System.UIntPtr:
        """The underlying integer value of this instance."""
        ...

    @overload
    def __init__(self, value: int) -> None:
        """
        Constructs an instance from a 32-bit unsigned integer.
        
        :param value: The integer vaule.
        """
        ...

    @overload
    def __init__(self, value: System.UIntPtr) -> None:
        """
        Constructs an instance from a native sized unsigned integer.
        
        :param value: The integer vaule.
        """
        ...

    @overload
    def Equals(self, o: typing.Any) -> bool:
        """
        Returns a value indicating whether this instance is equal to a specified object.
        
        :param o: An object to compare with this instance.
        :returns: true if  is an instance of CULong and equals the value of this instance; otherwise, false.
        """
        ...

    @overload
    def Equals(self, other: System.Runtime.InteropServices.CULong) -> bool:
        """
        Returns a value indicating whether this instance is equal to a specified CLong value.
        
        :param other: A CULong value to compare to this instance.
        :returns: true if  has the same value as this instance; otherwise, false.
        """
        ...

    def GetHashCode(self) -> int:
        """
        Returns the hash code for this instance.
        
        :returns: A 32-bit signed integer hash code.
        """
        ...

    def ToString(self) -> str:
        """
        Converts the numeric value of this instance to its equivalent string representation.
        
        :returns: The string representation of the value of this instance, consisting of a sequence of digits ranging from 0 to 9 with no leading zeroes.
        """
        ...


class ComVisibleAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Value(self) -> bool:
        ...

    def __init__(self, visibility: bool) -> None:
        ...


class CoClassAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def CoClass(self) -> typing.Type:
        ...

    def __init__(self, coClass: typing.Type) -> None:
        ...


class DispIdAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Value(self) -> int:
        ...

    def __init__(self, dispId: int) -> None:
        ...


class SafeArrayRankMismatchException(System.SystemException):
    """
    The exception is thrown when the runtime rank of a safe array is different
    than the array rank specified in the metadata.
    """

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...


class CollectionsMarshal(System.Object):
    """An unsafe class that provides a set of methods to access the underlying data representations of collections."""

    @staticmethod
    def AsSpan(list: System.Collections.Generic.List[System_Runtime_InteropServices_CollectionsMarshal_AsSpan_T]) -> System.Span[System_Runtime_InteropServices_CollectionsMarshal_AsSpan_T]:
        """
        Get a Span{T} view over a List{T}'s data.
        Items should not be added or removed from the List{T} while the Span{T} is in use.
        
        :param list: The list to get the data view over.
        """
        ...

    @staticmethod
    def GetValueRefOrAddDefault(dictionary: System.Collections.Generic.Dictionary[System_Runtime_InteropServices_CollectionsMarshal_GetValueRefOrAddDefault_TKey, System_Runtime_InteropServices_CollectionsMarshal_GetValueRefOrAddDefault_TValue], key: System_Runtime_InteropServices_CollectionsMarshal_GetValueRefOrAddDefault_TKey, exists: typing.Optional[bool]) -> typing.Union[typing.Any, bool]:
        """
        Gets a ref to a TValue in the Dictionary{TKey, TValue}, adding a new entry with a default value if it does not exist in the .
        
        :param dictionary: The dictionary to get the ref to TValue from.
        :param key: The key used for lookup.
        :param exists: Whether or not a new entry for the given key was added to the dictionary.
        """
        ...

    @staticmethod
    def GetValueRefOrNullRef(dictionary: System.Collections.Generic.Dictionary[System_Runtime_InteropServices_CollectionsMarshal_GetValueRefOrNullRef_TKey, System_Runtime_InteropServices_CollectionsMarshal_GetValueRefOrNullRef_TValue], key: System_Runtime_InteropServices_CollectionsMarshal_GetValueRefOrNullRef_TKey) -> typing.Any:
        """
        Gets either a ref to a TValue in the Dictionary{TKey, TValue} or a ref null if it does not exist in the .
        
        :param dictionary: The dictionary to get the ref to TValue from.
        :param key: The key used for lookup.
        """
        ...


class OutAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class CriticalHandle(System.Runtime.ConstrainedExecution.CriticalFinalizerObject, System.IDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def handle(self) -> System.IntPtr:
        """This field is protected."""
        ...

    @handle.setter
    def handle(self, value: System.IntPtr):
        """This field is protected."""
        ...

    @property
    def IsClosed(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def IsInvalid(self) -> bool:
        ...

    def __init__(self, invalidHandleValue: System.IntPtr) -> None:
        """This method is protected."""
        ...

    def Close(self) -> None:
        ...

    @overload
    def Dispose(self) -> None:
        ...

    @overload
    def Dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def ReleaseHandle(self) -> bool:
        """This method is protected."""
        ...

    def SetHandle(self, handle: System.IntPtr) -> None:
        """This method is protected."""
        ...

    def SetHandleAsInvalid(self) -> None:
        ...


class MemoryMarshal(System.Object):
    """
    Provides a collection of methods for interoperating with Memory{T}, ReadOnlyMemory{T},
    Span{T}, and ReadOnlySpan{T}.
    """

    @staticmethod
    @overload
    def AsBytes(span: System.Span[System_Runtime_InteropServices_MemoryMarshal_AsBytes_T]) -> System.Span[int]:
        """
        Casts a Span of one primitive type T to Span of bytes.
        That type may not contain pointers or references. This is checked at runtime in order to preserve type safety.
        
        :param span: The source slice, of type T.
        """
        ...

    @staticmethod
    @overload
    def AsBytes(span: System.ReadOnlySpan[System_Runtime_InteropServices_MemoryMarshal_AsBytes_T]) -> System.ReadOnlySpan[int]:
        """
        Casts a ReadOnlySpan of one primitive type T to ReadOnlySpan of bytes.
        That type may not contain pointers or references. This is checked at runtime in order to preserve type safety.
        
        :param span: The source slice, of type T.
        """
        ...

    @staticmethod
    def AsMemory(memory: System.ReadOnlyMemory[System_Runtime_InteropServices_MemoryMarshal_AsMemory_T]) -> System.Memory[System_Runtime_InteropServices_MemoryMarshal_AsMemory_T]:
        """
        Creates a Memory{T} from a ReadOnlyMemory{T}.
        
        :param memory: The ReadOnlyMemory{T}.
        :returns: A Memory{T} representing the same memory as the ReadOnlyMemory{T}, but writable.
        """
        ...

    @staticmethod
    @overload
    def AsRef(span: System.Span[int]) -> typing.Any:
        """
        Re-interprets a span of bytes as a reference to structure of type T.
        The type may not contain pointers or references. This is checked at runtime in order to preserve type safety.
        """
        ...

    @staticmethod
    @overload
    def AsRef(span: System.ReadOnlySpan[int]) -> typing.Any:
        """
        Re-interprets a span of bytes as a reference to structure of type T.
        The type may not contain pointers or references. This is checked at runtime in order to preserve type safety.
        """
        ...

    @staticmethod
    @overload
    def Cast(span: System.Span[System_Runtime_InteropServices_MemoryMarshal_Cast_TFrom]) -> System.Span[System_Runtime_InteropServices_MemoryMarshal_Cast_TTo]:
        ...

    @staticmethod
    @overload
    def Cast(span: System.ReadOnlySpan[System_Runtime_InteropServices_MemoryMarshal_Cast_TFrom]) -> System.ReadOnlySpan[System_Runtime_InteropServices_MemoryMarshal_Cast_TTo]:
        """
        Casts a ReadOnlySpan of one primitive type TFrom to another primitive type TTo.
        These types may not contain pointers or references. This is checked at runtime in order to preserve type safety.
        
        :param span: The source slice, of type TFrom.
        """
        ...

    @staticmethod
    def CreateFromPinnedArray(array: typing.List[System_Runtime_InteropServices_MemoryMarshal_CreateFromPinnedArray_T], start: int, length: int) -> System.Memory[System_Runtime_InteropServices_MemoryMarshal_CreateFromPinnedArray_T]:
        """
        Creates a new memory over the portion of the pre-pinned target array beginning
        at 'start' index and ending at 'end' index (exclusive).
        
        :param array: The pre-pinned target array.
        :param start: The index at which to begin the memory.
        :param length: The number of items in the memory.
        """
        ...

    @staticmethod
    @overload
    def CreateReadOnlySpanFromNullTerminated(value: typing.Any) -> System.ReadOnlySpan[str]:
        """
        Creates a new read-only span for a null-terminated string.
        
        :param value: The pointer to the null-terminated string of characters.
        :returns: A read-only span representing the specified null-terminated string, or an empty span if the pointer is null.
        """
        ...

    @staticmethod
    @overload
    def CreateReadOnlySpanFromNullTerminated(value: typing.Any) -> System.ReadOnlySpan[int]:
        """
        Creates a new read-only span for a null-terminated UTF8 string.
        
        :param value: The pointer to the null-terminated string of bytes.
        :returns: A read-only span representing the specified null-terminated string, or an empty span if the pointer is null.
        """
        ...

    @staticmethod
    @overload
    def GetArrayDataReference(array: typing.List[System_Runtime_InteropServices_MemoryMarshal_GetArrayDataReference_T]) -> typing.Any:
        """
        Returns a reference to the 0th element of . If the array is empty, returns a reference to where the 0th element
        would have been stored. Such a reference may be used for pinning but must never be dereferenced.
        """
        ...

    @staticmethod
    @overload
    def GetArrayDataReference(array: System.Array) -> typing.Any:
        """
        Returns a reference to the 0th element of . If the array is empty, returns a reference to where the 0th element
        would have been stored. Such a reference may be used for pinning but must never be dereferenced.
        """
        ...

    @staticmethod
    @overload
    def GetReference(span: System.Span[System_Runtime_InteropServices_MemoryMarshal_GetReference_T]) -> typing.Any:
        """
        Returns a reference to the 0th element of the Span. If the Span is empty, returns a reference to the location where the 0th element
        would have been stored. Such a reference may or may not be null. It can be used for pinning but must never be dereferenced.
        """
        ...

    @staticmethod
    @overload
    def GetReference(span: System.ReadOnlySpan[System_Runtime_InteropServices_MemoryMarshal_GetReference_T]) -> typing.Any:
        """
        Returns a reference to the 0th element of the ReadOnlySpan. If the ReadOnlySpan is empty, returns a reference to the location where the 0th element
        would have been stored. Such a reference may or may not be null. It can be used for pinning but must never be dereferenced.
        """
        ...

    @staticmethod
    def Read(source: System.ReadOnlySpan[int]) -> System_Runtime_InteropServices_MemoryMarshal_Read_T:
        """Reads a structure of type T out of a read-only span of bytes."""
        ...

    @staticmethod
    def ToEnumerable(memory: System.ReadOnlyMemory[System_Runtime_InteropServices_MemoryMarshal_ToEnumerable_T]) -> System.Collections.Generic.IEnumerable[System_Runtime_InteropServices_MemoryMarshal_ToEnumerable_T]:
        """
        Creates an IEnumerable{T} view of the given  to allow
        the  to be used in existing APIs that take an IEnumerable{T}.
        
        :param memory: The ReadOnlyMemory to view as an IEnumerable{T}
        :returns: An IEnumerable{T} view of the given.
        """
        ...

    @staticmethod
    def TryGetArray(memory: System.ReadOnlyMemory[System_Runtime_InteropServices_MemoryMarshal_TryGetArray_T], segment: typing.Optional[System.ArraySegment[System_Runtime_InteropServices_MemoryMarshal_TryGetArray_T]]) -> typing.Union[bool, System.ArraySegment[System_Runtime_InteropServices_MemoryMarshal_TryGetArray_T]]:
        """
        Get an array segment from the underlying memory.
        If unable to get the array segment, return false with a default array segment.
        """
        ...

    @staticmethod
    @overload
    def TryGetMemoryManager(memory: System.ReadOnlyMemory[System_Runtime_InteropServices_MemoryMarshal_TryGetMemoryManager_T], manager: typing.Optional[System_Runtime_InteropServices_MemoryMarshal_TryGetMemoryManager_TManager]) -> typing.Union[bool, System_Runtime_InteropServices_MemoryMarshal_TryGetMemoryManager_TManager]:
        """
        Gets an MemoryManager{T} from the underlying read-only memory.
        If unable to get the TManager type, returns false.
        
        :param memory: The memory to get the manager for.
        :param manager: The returned manager of the ReadOnlyMemory{T}.
        :returns: A bool indicating if it was successful.
        """
        ...

    @staticmethod
    @overload
    def TryGetMemoryManager(memory: System.ReadOnlyMemory[System_Runtime_InteropServices_MemoryMarshal_TryGetMemoryManager_T], manager: typing.Optional[System_Runtime_InteropServices_MemoryMarshal_TryGetMemoryManager_TManager], start: typing.Optional[int], length: typing.Optional[int]) -> typing.Union[bool, System_Runtime_InteropServices_MemoryMarshal_TryGetMemoryManager_TManager, int, int]:
        """
        Gets an MemoryManager{T} and ,  from the underlying read-only memory.
        If unable to get the TManager type, returns false.
        
        :param memory: The memory to get the manager for.
        :param manager: The returned manager of the ReadOnlyMemory{T}.
        :param start: The offset from the start of the  that the  represents.
        :param length: The length of the  that the  represents.
        :returns: A bool indicating if it was successful.
        """
        ...

    @staticmethod
    def TryGetString(memory: System.ReadOnlyMemory[str], text: typing.Optional[str], start: typing.Optional[int], length: typing.Optional[int]) -> typing.Union[bool, str, int, int]:
        """
        Attempts to get the underlying string from a ReadOnlyMemory{T}.
        
        :param memory: The memory that may be wrapping a string object.
        :param text: The string.
        :param start: The starting location in .
        :param length: The number of items in .
        """
        ...

    @staticmethod
    def TryRead(source: System.ReadOnlySpan[int], value: typing.Optional[System_Runtime_InteropServices_MemoryMarshal_TryRead_T]) -> typing.Union[bool, System_Runtime_InteropServices_MemoryMarshal_TryRead_T]:
        """
        Reads a structure of type T out of a span of bytes.
        
        :returns: If the span is too small to contain the type T, return false.
        """
        ...

    @staticmethod
    def TryWrite(destination: System.Span[int], value: System_Runtime_InteropServices_MemoryMarshal_TryWrite_T) -> bool:
        """
        Writes a structure of type T into a span of bytes.
        
        :returns: If the span is too small to contain the type T, return false.
        """
        ...

    @staticmethod
    def Write(destination: System.Span[int], value: System_Runtime_InteropServices_MemoryMarshal_Write_T) -> None:
        """Writes a structure of type T into a span of bytes."""
        ...


class UnmanagedCallConvAttribute(System.Attribute):
    """
    Provides an equivalent to UnmanagedCallersOnlyAttribute for native
    functions declared in .NET.
    """

    @property
    def CallConvs(self) -> typing.List[typing.Type]:
        """Types indicating calling conventions for the unmanaged target."""
        ...

    @CallConvs.setter
    def CallConvs(self, value: typing.List[typing.Type]):
        """Types indicating calling conventions for the unmanaged target."""
        ...

    def __init__(self) -> None:
        ...


class ErrorWrapper(System.Object):
    """This class has no documentation."""

    @property
    def ErrorCode(self) -> int:
        ...

    @overload
    def __init__(self, errorCode: int) -> None:
        ...

    @overload
    def __init__(self, errorCode: typing.Any) -> None:
        ...

    @overload
    def __init__(self, e: System.Exception) -> None:
        ...


class ICustomQueryInterface(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def GetInterface(self, iid: System.Guid, ppv: typing.Optional[System.IntPtr]) -> typing.Union[int, System.IntPtr]:
        """:returns: This method returns the int value of a member of the System.Runtime.InteropServices.CustomQueryInterfaceResult enum."""
        ...


class NFloat(System.Numerics.IBinaryFloatingPointIeee754[System_Runtime_InteropServices_NFloat], System.IMinMaxValue[System_Runtime_InteropServices_NFloat]):
    """Defines an immutable value type that represents a floating type that has the same size as the native integer size."""

    Epsilon: System.Runtime.InteropServices.NFloat
    """Represents the smallest positive NFloat value that is greater than zero."""

    MaxValue: System.Runtime.InteropServices.NFloat
    """Represents the largest finite value of a NFloat."""

    MinValue: System.Runtime.InteropServices.NFloat
    """Represents the smallest finite value of a NFloat."""

    NaN: System.Runtime.InteropServices.NFloat
    """Represents a value that is not a number (NaN)."""

    NegativeInfinity: System.Runtime.InteropServices.NFloat
    """Represents negative infinity."""

    PositiveInfinity: System.Runtime.InteropServices.NFloat
    """Represents positive infinity."""

    Size: int
    """Gets the size, in bytes, of an NFloat."""

    @property
    def Value(self) -> float:
        """The underlying floating-point value of this instance."""
        ...

    AdditiveIdentity: System.Runtime.InteropServices.NFloat

    AllBitsSet: System.Runtime.InteropServices.NFloat

    @property
    def value(self) -> System.Runtime.InteropServices.NFloat:
        ...

    @value.setter
    def value(self, value: System.Runtime.InteropServices.NFloat):
        ...

    @property
    def bits(self) -> int:
        ...

    @bits.setter
    def bits(self, value: int):
        ...

    @property
    def result(self) -> float:
        ...

    @result.setter
    def result(self, value: float):
        ...

    @staticmethod
    def () -> System.Runtime.InteropServices.NFloat:
        ...

    @overload
    def __init__(self, value: float) -> None:
        """
        Constructs an instance from a 32-bit floating point value.
        
        :param value: The floating-point value.
        """
        ...

    @overload
    def __init__(self, value: float) -> None:
        """
        Constructs an instance from a 64-bit floating point value.
        
        :param value: The floating-point value.
        """
        ...

    @overload
    def CompareTo(self, obj: typing.Any) -> int:
        """
        Compares this instance to a specified object and returns an integer that indicates whether the value of this instance is less than, equal to, or greater than the value of the specified object.
        
        :param obj: An object to compare, or null.
        :returns: A signed number indicating the relative values of this instance and .Return ValueDescriptionLess than zeroThis instance is less than , or this instance is not a number and  is a number.ZeroThis instance is equal to , or both this instance and  are not a number.Greater than zeroThis instance is greater than , or this instance is a number and  is not a number or  is null.
        """
        ...

    @overload
    def CompareTo(self, other: System.Runtime.InteropServices.NFloat) -> int:
        """
        Compares this instance to a specified floating-point number and returns an integer that indicates whether the value of this instance is less than, equal to, or greater than the value of the specified floating-point number.
        
        :param other: A floating-point number to compare.
        :returns: A signed number indicating the relative values of this instance and .Return ValueDescriptionLess than zeroThis instance is less than , or this instance is not a number and  is a number.ZeroThis instance is equal to , or both this instance and  are not a number.Greater than zeroThis instance is greater than , or this instance is a number and  is not a number.
        """
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        """
        Returns a value indicating whether this instance is equal to a specified object.
        
        :param obj: An object to compare with this instance.
        :returns: true if  is an instance of NFloat and equals the value of this instance; otherwise, false.
        """
        ...

    @overload
    def Equals(self, other: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Returns a value indicating whether this instance is equal to a specified NFloat value.
        
        :param other: An NFloat value to compare to this instance.
        :returns: true if  has the same value as this instance; otherwise, false.
        """
        ...

    def GetHashCode(self) -> int:
        """
        Returns the hash code for this instance.
        
        :returns: A 32-bit signed integer hash code.
        """
        ...

    @staticmethod
    def IsFinite(value: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Determines whether the specified value is finite (zero, subnormal, or normal).
        
        :param value: The floating-point value.
        :returns: true if the value is finite (zero, subnormal or normal); false otherwise.
        """
        ...

    @staticmethod
    def IsInfinity(value: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Determines whether the specified value is infinite (positive or negative infinity).
        
        :param value: The floating-point value.
        :returns: true if the value is infinite (positive or negative infinity); false otherwise.
        """
        ...

    @staticmethod
    def IsNaN(value: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Determines whether the specified value is NaN (not a number).
        
        :param value: The floating-point value.
        :returns: true if the value is NaN (not a number); false otherwise.
        """
        ...

    @staticmethod
    def IsNegative(value: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Determines whether the specified value is negative.
        
        :param value: The floating-point value.
        :returns: true if the value is negative; false otherwise.
        """
        ...

    @staticmethod
    def IsNegativeInfinity(value: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Determines whether the specified value is negative infinity.
        
        :param value: The floating-point value.
        :returns: true if the value is negative infinity; false otherwise.
        """
        ...

    @staticmethod
    def IsNormal(value: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Determines whether the specified value is normal.
        
        :param value: The floating-point value.
        :returns: true if the value is normal; false otherwise.
        """
        ...

    @staticmethod
    def IsPositiveInfinity(value: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Determines whether the specified value is positive infinity.
        
        :param value: The floating-point value.
        :returns: true if the value is positive infinity; false otherwise.
        """
        ...

    @staticmethod
    def IsPow2(value: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @staticmethod
    def IsSubnormal(value: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Determines whether the specified value is subnormal.
        
        :param value: The floating-point value.
        :returns: true if the value is subnormal; false otherwise.
        """
        ...

    @staticmethod
    def Log2(value: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def Parse(s: str) -> System.Runtime.InteropServices.NFloat:
        """
        Converts the string representation of a number to its floating-point number equivalent.
        
        :param s: A string that contains the number to convert.
        :returns: A floating-point number that is equivalent to the numeric value or symbol specified in .
        """
        ...

    @staticmethod
    @overload
    def Parse(s: str, style: System.Globalization.NumberStyles) -> System.Runtime.InteropServices.NFloat:
        """
        Converts the string representation of a number in a specified style to its floating-point number equivalent.
        
        :param s: A string that contains the number to convert.
        :param style: A bitwise combination of enumeration values that indicate the style elements that can be present in .
        :returns: A floating-point number that is equivalent to the numeric value or symbol specified in .
        """
        ...

    @staticmethod
    @overload
    def Parse(s: str, provider: System.IFormatProvider) -> System.Runtime.InteropServices.NFloat:
        """
        Converts the string representation of a number in a specified culture-specific format to its floating-point number equivalent.
        
        :param s: A string that contains the number to convert.
        :param provider: An object that supplies culture-specific formatting information about .
        :returns: A floating-point number that is equivalent to the numeric value or symbol specified in .
        """
        ...

    @staticmethod
    @overload
    def Parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> System.Runtime.InteropServices.NFloat:
        """
        Converts the string representation of a number in a specified style and culture-specific format to its floating-point number equivalent.
        
        :param s: A string that contains the number to convert.
        :param style: A bitwise combination of enumeration values that indicate the style elements that can be present in .
        :param provider: An object that supplies culture-specific formatting information about .
        :returns: A floating-point number that is equivalent to the numeric value or symbol specified in .
        """
        ...

    @staticmethod
    @overload
    def Parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.Runtime.InteropServices.NFloat:
        """
        Converts a character span that contains the string representation of a number in a specified style and culture-specific format to its floating-point number equivalent.
        
        :param s: A character span that contains the number to convert.
        :param style: A bitwise combination of enumeration values that indicate the style elements that can be present in .
        :param provider: An object that supplies culture-specific formatting information about .
        :returns: A floating-point number that is equivalent to the numeric value or symbol specified in .
        """
        ...

    @overload
    def ToString(self) -> str:
        """
        Converts the numeric value of this instance to its equivalent string representation.
        
        :returns: The string representation of the value of this instance.
        """
        ...

    @overload
    def ToString(self, format: str) -> str:
        """
        Converts the numeric value of this instance to its equivalent string representation using the specified format.
        
        :param format: A numeric format string.
        :returns: The string representation of the value of this instance as specified by .
        """
        ...

    @overload
    def ToString(self, provider: System.IFormatProvider) -> str:
        """
        Converts the numeric value of this instance to its equivalent string representation using the specified culture-specific format information.
        
        :param provider: An object that supplies culture-specific formatting information.
        :returns: The string representation of the value of this instance as specified by .
        """
        ...

    @overload
    def ToString(self, format: str, provider: System.IFormatProvider) -> str:
        """
        Converts the numeric value of this instance to its equivalent string representation using the specified format and culture-specific format information.
        
        :param format: A numeric format string.
        :param provider: An object that supplies culture-specific formatting information.
        :returns: The string representation of the value of this instance as specified by  and .
        """
        ...

    def TryFormat(self, destination: System.Span[str], charsWritten: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Union[bool, int]:
        """
        Tries to format the value of the current instance into the provided span of characters.
        
        :param destination: The span in which to write this instance's value formatted as a span of characters.
        :param charsWritten: When this method returns, contains the number of characters that were written in .
        :param format: A span containing the characters that represent a standard or custom format string that defines the acceptable format for .
        :param provider: An optional object that supplies culture-specific formatting information for .
        :returns: true if the formatting was successful; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def TryParse(s: str, result: typing.Optional[System.Runtime.InteropServices.NFloat]) -> typing.Union[bool, System.Runtime.InteropServices.NFloat]:
        """
        Tries to convert the string representation of a number to its floating-point number equivalent.
        
        :param s: A read-only character span that contains the number to convert.
        :param result: When this method returns, contains a floating-point number equivalent of the numeric value or symbol contained in  if the conversion succeeded or zero if the conversion failed. The conversion fails if the  is null, string.Empty, or is not in a valid format. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def TryParse(s: System.ReadOnlySpan[str], result: typing.Optional[System.Runtime.InteropServices.NFloat]) -> typing.Union[bool, System.Runtime.InteropServices.NFloat]:
        """
        Tries to convert a character span containing the string representation of a number to its floating-point number equivalent.
        
        :param s: A read-only character span that contains the number to convert.
        :param result: When this method returns, contains a floating-point number equivalent of the numeric value or symbol contained in  if the conversion succeeded or zero if the conversion failed. The conversion fails if the  is string.Empty or is not in a valid format. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def TryParse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.Runtime.InteropServices.NFloat]) -> typing.Union[bool, System.Runtime.InteropServices.NFloat]:
        """
        Tries to convert the string representation of a number in a specified style and culture-specific format to its floating-point number equivalent.
        
        :param s: A read-only character span that contains the number to convert.
        :param style: A bitwise combination of enumeration values that indicate the style elements that can be present in .
        :param provider: An object that supplies culture-specific formatting information about .
        :param result: When this method returns, contains a floating-point number equivalent of the numeric value or symbol contained in  if the conversion succeeded or zero if the conversion failed. The conversion fails if the  is null, string.Empty, or is not in a format compliant with , or if  is not a valid combination of NumberStyles enumeration constants. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def TryParse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.Runtime.InteropServices.NFloat]) -> typing.Union[bool, System.Runtime.InteropServices.NFloat]:
        """
        Tries to convert a character span containing the string representation of a number in a specified style and culture-specific format to its floating-point number equivalent.
        
        :param s: A read-only character span that contains the number to convert.
        :param style: A bitwise combination of enumeration values that indicate the style elements that can be present in .
        :param provider: An object that supplies culture-specific formatting information about .
        :param result: When this method returns, contains a floating-point number equivalent of the numeric value or symbol contained in  if the conversion succeeded or zero if the conversion failed. The conversion fails if the  is string.Empty or is not in a format compliant with , or if  is not a valid combination of NumberStyles enumeration constants. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...


class GCHandle(System.IEquatable[System_Runtime_InteropServices_GCHandle]):
    """
    Represents an opaque, GC handle to a managed object. A GC handle is used when an
    object reference must be reachable from unmanaged memory.
    """

    @property
    def Target(self) -> System.Object:
        ...

    @Target.setter
    def Target(self, value: System.Object):
        ...

    @property
    def IsAllocated(self) -> bool:
        """Determine whether this handle has been allocated or not."""
        ...

    def AddrOfPinnedObject(self) -> System.IntPtr:
        """
        Retrieve the address of an object in a Pinned handle.  This throws
        an exception if the handle is any type other than Pinned.
        """
        ...

    @staticmethod
    @overload
    def Alloc(value: typing.Any) -> System.Runtime.InteropServices.GCHandle:
        """
        Creates a new GC handle for an object.
        
        :param value: The object that the GC handle is created for.
        :returns: A new GC handle that protects the object.
        """
        ...

    @staticmethod
    @overload
    def Alloc(value: typing.Any, type: System.Runtime.InteropServices.GCHandleType) -> System.Runtime.InteropServices.GCHandle:
        """
        Creates a new GC handle for an object.
        
        :param value: The object that the GC handle is created for.
        :param type: The type of GC handle to create.
        :returns: A new GC handle that protects the object.
        """
        ...

    @overload
    def Equals(self, o: typing.Any) -> bool:
        ...

    @overload
    def Equals(self, other: System.Runtime.InteropServices.GCHandle) -> bool:
        """
        Indicates whether the current instance is equal to another instance of the same type.
        
        :param other: An instance to compare with this instance.
        :returns: true if the current instance is equal to the other instance; otherwise, false.
        """
        ...

    def Free(self) -> None:
        """Frees a GC handle."""
        ...

    @staticmethod
    def FromIntPtr(value: System.IntPtr) -> System.Runtime.InteropServices.GCHandle:
        ...

    def GetHashCode(self) -> int:
        ...

    @staticmethod
    def ToIntPtr(value: System.Runtime.InteropServices.GCHandle) -> System.IntPtr:
        ...


class ICustomFactory(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def CreateInstance(self, serverType: typing.Type) -> System.MarshalByRefObject:
        ...


class UnmanagedCallersOnlyAttribute(System.Attribute):
    """
    Any method marked with System.Runtime.InteropServices.UnmanagedCallersOnlyAttribute can be directly called from
    native code. The function token can be loaded to a local variable using the https://docs.microsoft.com/dotnet/csharp/language-reference/operators/pointer-related-operators#address-of-operator- operator
    in C# and passed as a callback to a native method.
    """

    @property
    def CallConvs(self) -> typing.List[typing.Type]:
        """Optional. If omitted, the runtime will use the default platform calling convention."""
        ...

    @CallConvs.setter
    def CallConvs(self, value: typing.List[typing.Type]):
        """Optional. If omitted, the runtime will use the default platform calling convention."""
        ...

    @property
    def EntryPoint(self) -> str:
        """Optional. If omitted, no named export is emitted during compilation."""
        ...

    @EntryPoint.setter
    def EntryPoint(self, value: str):
        """Optional. If omitted, no named export is emitted during compilation."""
        ...

    def __init__(self) -> None:
        ...


class LayoutKind(System.Enum):
    """This class has no documentation."""

    Sequential = 0

    Explicit = 2

    Auto = 3


class FieldOffsetAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Value(self) -> int:
        ...

    def __init__(self, offset: int) -> None:
        ...


class StandardOleMarshalObject(System.MarshalByRefObject, System.Runtime.InteropServices.IMarshal):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    def DisconnectObject(self, dwReserved: int) -> int:
        ...

    def GetMarshalSizeMax(self, riid: System.Guid, pv: System.IntPtr, dwDestContext: int, pvDestContext: System.IntPtr, mshlflags: int, pSize: typing.Optional[int]) -> typing.Union[int, int]:
        ...

    def GetUnmarshalClass(self, riid: System.Guid, pv: System.IntPtr, dwDestContext: int, pvDestContext: System.IntPtr, mshlflags: int, pCid: typing.Optional[System.Guid]) -> typing.Union[int, System.Guid]:
        ...

    def MarshalInterface(self, pStm: System.IntPtr, riid: System.Guid, pv: System.IntPtr, dwDestContext: int, pvDestContext: System.IntPtr, mshlflags: int) -> int:
        ...

    def ReleaseMarshalData(self, pStm: System.IntPtr) -> int:
        ...

    def UnmarshalInterface(self, pStm: System.IntPtr, riid: System.Guid, ppv: typing.Optional[System.IntPtr]) -> typing.Union[int, System.IntPtr]:
        ...


class CurrencyWrapper(System.Object):
    """CurrencyWrapper and support for marshalling to the VARIANT type may be unavailable in future releases."""

    @property
    def WrappedObject(self) -> float:
        ...

    @overload
    def __init__(self, obj: float) -> None:
        ...

    @overload
    def __init__(self, obj: typing.Any) -> None:
        ...


class ProgIdAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Value(self) -> str:
        ...

    def __init__(self, progId: str) -> None:
        ...


class ComSourceInterfacesAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Value(self) -> str:
        ...

    @overload
    def __init__(self, sourceInterfaces: str) -> None:
        ...

    @overload
    def __init__(self, sourceInterface: typing.Type) -> None:
        ...

    @overload
    def __init__(self, sourceInterface1: typing.Type, sourceInterface2: typing.Type) -> None:
        ...

    @overload
    def __init__(self, sourceInterface1: typing.Type, sourceInterface2: typing.Type, sourceInterface3: typing.Type) -> None:
        ...

    @overload
    def __init__(self, sourceInterface1: typing.Type, sourceInterface2: typing.Type, sourceInterface3: typing.Type, sourceInterface4: typing.Type) -> None:
        ...


class ComEventInterfaceAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def SourceInterface(self) -> typing.Type:
        ...

    @property
    def EventProvider(self) -> typing.Type:
        ...

    def __init__(self, SourceInterface: typing.Type, EventProvider: typing.Type) -> None:
        ...


class OptionalAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class CLong(System.IEquatable[System_Runtime_InteropServices_CLong]):
    """
    CLong is an immutable value type that represents the long type in C and C++.
    It is meant to be used as an exchange type at the managed/unmanaged boundary to accurately represent
    in managed code unmanaged APIs that use the long type.
    This type has 32-bits of storage on all Windows platforms and 32-bit Unix-based platforms.
    It has 64-bits of storage on 64-bit Unix platforms.
    """

    @property
    def Value(self) -> System.IntPtr:
        """The underlying integer value of this instance."""
        ...

    @overload
    def __init__(self, value: int) -> None:
        """
        Constructs an instance from a 32-bit integer.
        
        :param value: The integer vaule.
        """
        ...

    @overload
    def __init__(self, value: System.IntPtr) -> None:
        """
        Constructs an instance from a native sized integer.
        
        :param value: The integer vaule.
        """
        ...

    @overload
    def Equals(self, o: typing.Any) -> bool:
        """
        Returns a value indicating whether this instance is equal to a specified object.
        
        :param o: An object to compare with this instance.
        :returns: true if  is an instance of CLong and equals the value of this instance; otherwise, false.
        """
        ...

    @overload
    def Equals(self, other: System.Runtime.InteropServices.CLong) -> bool:
        """
        Returns a value indicating whether this instance is equal to a specified CLong value.
        
        :param other: A CLong value to compare to this instance.
        :returns: true if  has the same value as this instance; otherwise, false.
        """
        ...

    def GetHashCode(self) -> int:
        """
        Returns the hash code for this instance.
        
        :returns: A 32-bit signed integer hash code.
        """
        ...

    def ToString(self) -> str:
        """
        Converts the numeric value of this instance to its equivalent string representation.
        
        :returns: The string representation of the value of this instance, consisting of a negative sign if the value is negative, and a sequence of digits ranging from 0 to 9 with no leading zeroes.
        """
        ...


class BestFitMappingAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def BestFitMapping(self) -> bool:
        ...

    @property
    def ThrowOnUnmappableChar(self) -> bool:
        ...

    @ThrowOnUnmappableChar.setter
    def ThrowOnUnmappableChar(self, value: bool):
        ...

    def __init__(self, BestFitMapping: bool) -> None:
        ...


class ICustomMarshaler(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def CleanUpManagedData(self, ManagedObj: typing.Any) -> None:
        ...

    def CleanUpNativeData(self, pNativeData: System.IntPtr) -> None:
        ...

    def GetNativeDataSize(self) -> int:
        ...

    def MarshalManagedToNative(self, ManagedObj: typing.Any) -> System.IntPtr:
        ...

    def MarshalNativeToManaged(self, pNativeData: System.IntPtr) -> System.Object:
        ...


class SafeArrayTypeMismatchException(System.SystemException):
    """
    The exception is thrown when the runtime type of an array is different
    than the safe array sub type specified in the metadata.
    """

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...


class DefaultDllImportSearchPathsAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Paths(self) -> int:
        """This property contains the int value of a member of the System.Runtime.InteropServices.DllImportSearchPath enum."""
        ...

    def __init__(self, paths: System.Runtime.InteropServices.DllImportSearchPath) -> None:
        ...


class COMException(System.Runtime.InteropServices.ExternalException):
    """This class has no documentation."""

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
    def __init__(self, message: str, errorCode: int) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...

    def ToString(self) -> str:
        ...


class DllImportAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Value(self) -> str:
        ...

    @property
    def EntryPoint(self) -> str:
        ...

    @EntryPoint.setter
    def EntryPoint(self, value: str):
        ...

    @property
    def CharSet(self) -> System.Runtime.InteropServices.CharSet:
        ...

    @CharSet.setter
    def CharSet(self, value: System.Runtime.InteropServices.CharSet):
        ...

    @property
    def SetLastError(self) -> bool:
        ...

    @SetLastError.setter
    def SetLastError(self, value: bool):
        ...

    @property
    def ExactSpelling(self) -> bool:
        ...

    @ExactSpelling.setter
    def ExactSpelling(self, value: bool):
        ...

    @property
    def CallingConvention(self) -> System.Runtime.InteropServices.CallingConvention:
        ...

    @CallingConvention.setter
    def CallingConvention(self, value: System.Runtime.InteropServices.CallingConvention):
        ...

    @property
    def BestFitMapping(self) -> bool:
        ...

    @BestFitMapping.setter
    def BestFitMapping(self, value: bool):
        ...

    @property
    def PreserveSig(self) -> bool:
        ...

    @PreserveSig.setter
    def PreserveSig(self, value: bool):
        ...

    @property
    def ThrowOnUnmappableChar(self) -> bool:
        ...

    @ThrowOnUnmappableChar.setter
    def ThrowOnUnmappableChar(self, value: bool):
        ...

    def __init__(self, dllName: str) -> None:
        ...


class SEHException(System.Runtime.InteropServices.ExternalException):
    """Exception for Structured Exception Handler exceptions."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...

    def CanResume(self) -> bool:
        ...


class StructLayoutAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Value(self) -> int:
        """This property contains the int value of a member of the System.Runtime.InteropServices.LayoutKind enum."""
        ...

    @property
    def Pack(self) -> int:
        ...

    @Pack.setter
    def Pack(self, value: int):
        ...

    @property
    def Size(self) -> int:
        ...

    @Size.setter
    def Size(self, value: int):
        ...

    @property
    def CharSet(self) -> System.Runtime.InteropServices.CharSet:
        ...

    @CharSet.setter
    def CharSet(self, value: System.Runtime.InteropServices.CharSet):
        ...

    @overload
    def __init__(self, layoutKind: System.Runtime.InteropServices.LayoutKind) -> None:
        ...

    @overload
    def __init__(self, layoutKind: int) -> None:
        ...


