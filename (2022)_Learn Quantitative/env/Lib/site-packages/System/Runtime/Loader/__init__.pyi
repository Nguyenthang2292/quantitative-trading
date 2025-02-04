from typing import overload
import typing

import System
import System.Collections.Generic
import System.IO
import System.Reflection
import System.Runtime.Loader

System_Runtime_Loader__EventContainer_Callable = typing.TypeVar("System_Runtime_Loader__EventContainer_Callable")
System_Runtime_Loader__EventContainer_ReturnType = typing.TypeVar("System_Runtime_Loader__EventContainer_ReturnType")


class AssemblyDependencyResolver(System.Object):
    """This class has no documentation."""

    @overload
    def __init__(self, componentAssemblyPath: str) -> None:
        ...

    @overload
    def __init__(self, componentAssemblyPath: str) -> None:
        ...

    @overload
    def ResolveAssemblyToPath(self, assemblyName: System.Reflection.AssemblyName) -> str:
        ...

    @overload
    def ResolveAssemblyToPath(self, assemblyName: System.Reflection.AssemblyName) -> str:
        ...

    @overload
    def ResolveUnmanagedDllToPath(self, unmanagedDllName: str) -> str:
        ...

    @overload
    def ResolveUnmanagedDllToPath(self, unmanagedDllName: str) -> str:
        ...


class AssemblyLoadContext(System.Object):
    """This class has no documentation."""

    class ContextualReflectionScope(System.IDisposable):
        """Opaque disposable struct used to restore CurrentContextualReflectionContext"""

        def Dispose(self) -> None:
            ...

    @property
    def Assemblies(self) -> System.Collections.Generic.IEnumerable[System.Reflection.Assembly]:
        ...

    @property
    def ResolvingUnmanagedDll(self) -> _EventContainer[typing.Callable[[System.Reflection.Assembly, str], System.IntPtr], System.IntPtr]:
        ...

    @ResolvingUnmanagedDll.setter
    def ResolvingUnmanagedDll(self, value: _EventContainer[typing.Callable[[System.Reflection.Assembly, str], System.IntPtr], System.IntPtr]):
        ...

    @property
    def Resolving(self) -> _EventContainer[typing.Callable[[System.Runtime.Loader.AssemblyLoadContext, System.Reflection.AssemblyName], System.Reflection.Assembly], System.Reflection.Assembly]:
        ...

    @Resolving.setter
    def Resolving(self, value: _EventContainer[typing.Callable[[System.Runtime.Loader.AssemblyLoadContext, System.Reflection.AssemblyName], System.Reflection.Assembly], System.Reflection.Assembly]):
        ...

    @property
    def Unloading(self) -> _EventContainer[typing.Callable[[System.Runtime.Loader.AssemblyLoadContext], None], None]:
        ...

    @Unloading.setter
    def Unloading(self, value: _EventContainer[typing.Callable[[System.Runtime.Loader.AssemblyLoadContext], None], None]):
        ...

    AssemblyLoad: _EventContainer[typing.Callable[[System.Object, System.AssemblyLoadEventArgs], None], None]

    TypeResolve: _EventContainer[typing.Callable[[System.Object, System.ResolveEventArgs], System.Reflection.Assembly], System.Reflection.Assembly]

    ResourceResolve: _EventContainer[typing.Callable[[System.Object, System.ResolveEventArgs], System.Reflection.Assembly], System.Reflection.Assembly]

    AssemblyResolve: _EventContainer[typing.Callable[[System.Object, System.ResolveEventArgs], System.Reflection.Assembly], System.Reflection.Assembly]

    Default: System.Runtime.Loader.AssemblyLoadContext

    @property
    def IsCollectible(self) -> bool:
        ...

    @property
    def Name(self) -> str:
        ...

    All: System.Collections.Generic.IEnumerable[System.Runtime.Loader.AssemblyLoadContext]

    CurrentContextualReflectionContext: System.Runtime.Loader.AssemblyLoadContext
    """Nullable current AssemblyLoadContext used for context sensitive reflection APIs"""

    @property
    def NativeALC(self) -> System.IntPtr:
        ...

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, isCollectible: bool) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, name: str, isCollectible: bool = False) -> None:
        ...

    @overload
    def EnterContextualReflection(self) -> System.Runtime.Loader.AssemblyLoadContext.ContextualReflectionScope:
        """
        Enter scope using this AssemblyLoadContext for ContextualReflection
        
        :returns: A disposable ContextualReflectionScope for use in a using block.
        """
        ...

    @staticmethod
    @overload
    def EnterContextualReflection(activating: System.Reflection.Assembly) -> System.Runtime.Loader.AssemblyLoadContext.ContextualReflectionScope:
        """
        Enter scope using this AssemblyLoadContext for ContextualReflection
        
        :param activating: Set CurrentContextualReflectionContext to the AssemblyLoadContext which loaded activating.
        :returns: A disposable ContextualReflectionScope for use in a using block.
        """
        ...

    @staticmethod
    def GetAssemblyName(assemblyPath: str) -> System.Reflection.AssemblyName:
        ...

    @staticmethod
    def GetLoadContext(assembly: System.Reflection.Assembly) -> System.Runtime.Loader.AssemblyLoadContext:
        ...

    def Load(self, assemblyName: System.Reflection.AssemblyName) -> System.Reflection.Assembly:
        """This method is protected."""
        ...

    def LoadFromAssemblyName(self, assemblyName: System.Reflection.AssemblyName) -> System.Reflection.Assembly:
        ...

    def LoadFromAssemblyPath(self, assemblyPath: str) -> System.Reflection.Assembly:
        ...

    def LoadFromNativeImagePath(self, nativeImagePath: str, assemblyPath: str) -> System.Reflection.Assembly:
        ...

    @overload
    def LoadFromStream(self, assembly: System.IO.Stream) -> System.Reflection.Assembly:
        ...

    @overload
    def LoadFromStream(self, assembly: System.IO.Stream, assemblySymbols: System.IO.Stream) -> System.Reflection.Assembly:
        ...

    def LoadUnmanagedDll(self, unmanagedDllName: str) -> System.IntPtr:
        """This method is protected."""
        ...

    def LoadUnmanagedDllFromPath(self, unmanagedDllPath: str) -> System.IntPtr:
        """This method is protected."""
        ...

    def SetProfileOptimizationRoot(self, directoryPath: str) -> None:
        ...

    def StartProfileOptimization(self, profile: str) -> None:
        ...

    def ToString(self) -> str:
        ...

    def Unload(self) -> None:
        ...


class _EventContainer(typing.Generic[System_Runtime_Loader__EventContainer_Callable, System_Runtime_Loader__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_Runtime_Loader__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_Runtime_Loader__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_Runtime_Loader__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


