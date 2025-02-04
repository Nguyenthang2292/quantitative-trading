from typing import overload
import abc
import typing

import System
import System.Collections
import System.Collections.Generic
import System.IO
import System.IO.Enumeration
import System.Runtime.ConstrainedExecution

System_IO_Enumeration_FileSystemEnumerator_TResult = typing.TypeVar("System_IO_Enumeration_FileSystemEnumerator_TResult")
System_IO_Enumeration_FileSystemEnumerable_TResult = typing.TypeVar("System_IO_Enumeration_FileSystemEnumerable_TResult")


class FileSystemEntry:
    """Provides a lower level view of System.IO.FileSystemInfo to help process and filter find results."""

    @property
    def _info(self) -> typing.Any:
        ...

    @_info.setter
    def _info(self, value: typing.Any):
        ...

    @property
    def Directory(self) -> System.ReadOnlySpan[str]:
        """Gets the full path of the directory this entry resides in."""
        ...

    @Directory.setter
    def Directory(self, value: System.ReadOnlySpan[str]):
        """Gets the full path of the directory this entry resides in."""
        ...

    @property
    def RootDirectory(self) -> System.ReadOnlySpan[str]:
        """Gets the full path of the root directory used for the enumeration."""
        ...

    @RootDirectory.setter
    def RootDirectory(self, value: System.ReadOnlySpan[str]):
        """Gets the full path of the root directory used for the enumeration."""
        ...

    @property
    def OriginalRootDirectory(self) -> System.ReadOnlySpan[str]:
        """Gets the root directory for the enumeration as specified in the constructor."""
        ...

    @OriginalRootDirectory.setter
    def OriginalRootDirectory(self, value: System.ReadOnlySpan[str]):
        """Gets the root directory for the enumeration as specified in the constructor."""
        ...

    @property
    def FileName(self) -> System.ReadOnlySpan[str]:
        """Gets the file name for this entry."""
        ...

    @property
    def Attributes(self) -> int:
        """
        Gets the attributes for this entry.
        
        This property contains the int value of a member of the System.IO.FileAttributes enum.
        """
        ...

    @property
    def Length(self) -> int:
        """Gets the length of the file, in bytes."""
        ...

    @property
    def CreationTimeUtc(self) -> System.DateTimeOffset:
        """Gets the creation time for the entry or the oldest available time stamp if the operating system does not support creation time stamps."""
        ...

    @property
    def LastAccessTimeUtc(self) -> System.DateTimeOffset:
        """Gets a datetime offset that represents the last access time in UTC."""
        ...

    @property
    def LastWriteTimeUtc(self) -> System.DateTimeOffset:
        """Gets a datetime offset that represents the last write time in UTC."""
        ...

    @property
    def IsDirectory(self) -> bool:
        """Gets a value that indicates whether this entry is a directory."""
        ...

    @property
    def IsHidden(self) -> bool:
        """Gets a value that indicates whether the file has the hidden attribute."""
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsSymbolicLink(self) -> bool:
        ...

    @overload
    def ToFileSystemInfo(self) -> System.IO.FileSystemInfo:
        """
        Converts the value of this instance to a System.IO.FileSystemInfo.
        
        :returns: The value of this instance as a System.IO.FileSystemInfo.
        """
        ...

    @overload
    def ToFileSystemInfo(self) -> System.IO.FileSystemInfo:
        ...

    @overload
    def ToFullPath(self) -> str:
        """
        Returns the full path of the find result.
        
        :returns: A string representing the full path.
        """
        ...

    @overload
    def ToFullPath(self) -> str:
        """Returns the full path of the find result."""
        ...

    def ToSpecifiedFullPath(self) -> str:
        """
        Returns the full path for the find results, based on the initially provided path.
        
        :returns: A string representing the full path.
        """
        ...


class FileSystemEnumerator(typing.Generic[System_IO_Enumeration_FileSystemEnumerator_TResult], System.Runtime.ConstrainedExecution.CriticalFinalizerObject, metaclass=abc.ABCMeta):
    """Enumerates the file system elements of the provided type that are being searched and filtered by a Enumeration.FileSystemEnumerable{T}."""

    @property
    def Current(self) -> System_IO_Enumeration_FileSystemEnumerator_TResult:
        """Gets the currently visited element."""
        ...

    def __init__(self, directory: str, options: System.IO.EnumerationOptions = None) -> None:
        """
        Encapsulates a find operation.
        
        :param directory: The directory to search in.
        :param options: Enumeration options to use.
        """
        ...

    def ContinueOnError(self, error: int) -> bool:
        """
        When overridden in a derived class, returns a value that indicates whether to continue execution or throw the default exception.
        
        This method is protected.
        
        :param error: The native error code.
        :returns: true to continue; false to throw the default exception for the given error.
        """
        ...

    @overload
    def Dispose(self) -> None:
        """Releases the resources used by the current instance of the Enumeration.FileSystemEnumerator{T} class."""
        ...

    @overload
    def Dispose(self, disposing: bool) -> None:
        """
        When overridden in a derived class, releases the unmanaged resources used by the Enumeration.FileSystemEnumerator{T} class and optionally releases the managed resources.
        
        This method is protected.
        
        :param disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        ...

    @overload
    def MoveNext(self) -> bool:
        ...

    @overload
    def MoveNext(self) -> bool:
        """
        Advances the enumerator to the next item of the Enumeration.FileSystemEnumerator{T}.
        
        :returns: true if the enumerator successfully advanced to the next item; false if the end of the enumerator has been passed.
        """
        ...

    def OnDirectoryFinished(self, directory: System.ReadOnlySpan[str]) -> None:
        """
        When overridden in a derived class, this method is called whenever the end of a directory is reached.
        
        This method is protected.
        
        :param directory: The directory path as a read-only span.
        """
        ...

    def Reset(self) -> None:
        """Always throws System.NotSupportedException."""
        ...

    def ShouldIncludeEntry(self, entry: System.IO.Enumeration.FileSystemEntry) -> bool:
        """
        When overridden in a derived class, determines whether the specified file system entry should be included in the results.
        
        This method is protected.
        
        :param entry: A file system entry reference.
        :returns: true if the specified file system entry should be included in the results; otherwise, false.
        """
        ...

    def ShouldRecurseIntoEntry(self, entry: System.IO.Enumeration.FileSystemEntry) -> bool:
        """
        When overridden in a derived class, determines whether the specified file system entry should be recursed.
        
        This method is protected.
        
        :param entry: A file system entry reference.
        :returns: true if the specified directory entry should be recursed into; otherwise, false.
        """
        ...

    def TransformEntry(self, entry: System.IO.Enumeration.FileSystemEntry) -> System_IO_Enumeration_FileSystemEnumerator_TResult:
        """
        When overridden in a derived class, generates the result type from the current entry.
        
        This method is protected.
        
        :param entry: A file system entry reference.
        :returns: The result type from the current entry.
        """
        ...


class FileSystemEnumerable(typing.Generic[System_IO_Enumeration_FileSystemEnumerable_TResult], System.Object, typing.Iterable[System_IO_Enumeration_FileSystemEnumerable_TResult]):
    """Enumerable that allows utilizing custom filter predicates and transform delegates."""

    @property
    def ShouldIncludePredicate(self) -> typing.Callable[[System.IO.Enumeration.FileSystemEntry], bool]:
        ...

    @ShouldIncludePredicate.setter
    def ShouldIncludePredicate(self, value: typing.Callable[[System.IO.Enumeration.FileSystemEntry], bool]):
        ...

    @property
    def ShouldRecursePredicate(self) -> typing.Callable[[System.IO.Enumeration.FileSystemEntry], bool]:
        ...

    @ShouldRecursePredicate.setter
    def ShouldRecursePredicate(self, value: typing.Callable[[System.IO.Enumeration.FileSystemEntry], bool]):
        ...

    def __init__(self, directory: str, transform: typing.Callable[[System.IO.Enumeration.FileSystemEntry], System_IO_Enumeration_FileSystemEnumerable_TResult], options: System.IO.EnumerationOptions = None) -> None:
        ...

    def FindPredicate(self, entry: System.IO.Enumeration.FileSystemEntry) -> bool:
        """Delegate for filtering out find results."""
        ...

    def FindTransform(self, entry: System.IO.Enumeration.FileSystemEntry) -> System_IO_Enumeration_FileSystemEnumerable_TResult:
        """Delegate for transforming raw find data into a result."""
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System_IO_Enumeration_FileSystemEnumerable_TResult]:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        ...


class FileSystemName(System.Object):
    """Provides methods for matching file system names."""

    @staticmethod
    def MatchesSimpleExpression(expression: System.ReadOnlySpan[str], name: System.ReadOnlySpan[str], ignoreCase: bool = True) -> bool:
        """
        Verifies whether the given expression matches the given name. Supports the following wildcards: '*' and '?'. The backslash character '\\\\' escapes.
        
        :param expression: The expression to match with.
        :param name: The name to check against the expression.
        :param ignoreCase: true to ignore case (default); false if the match should be case-sensitive.
        :returns: true if the given expression matches the given name; otherwise, false.
        """
        ...

    @staticmethod
    def MatchesWin32Expression(expression: System.ReadOnlySpan[str], name: System.ReadOnlySpan[str], ignoreCase: bool = True) -> bool:
        """
        Verifies whether the given Win32 expression matches the given name. Supports the following wildcards: '*', '?', '<', '>', '"'. The backslash character '\\' escapes.
        
        :param expression: The expression to match with, such as "*.foo".
        :param name: The name to check against the expression.
        :param ignoreCase: true to ignore case (default), false if the match should be case-sensitive.
        :returns: true if the given expression matches the given name; otherwise, false.
        """
        ...

    @staticmethod
    def TranslateWin32Expression(expression: str) -> str:
        """
        Translates the given Win32 expression. Change '*' and '?' to '<', '>' and '"' to match Win32 behavior.
        
        :param expression: The expression to translate.
        :returns: A string with the translated Win32 expression.
        """
        ...


