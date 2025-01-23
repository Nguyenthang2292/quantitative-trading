from typing import overload
import abc
import datetime
import typing
import warnings

import Microsoft.Win32.SafeHandles
import System
import System.Collections.Generic
import System.IO
import System.Runtime.InteropServices
import System.Runtime.Serialization
import System.Text
import System.Threading
import System.Threading.Tasks

System_IO_UnmanagedMemoryAccessor_Write_T = typing.TypeVar("System_IO_UnmanagedMemoryAccessor_Write_T")
System_IO_UnmanagedMemoryAccessor_Read_T = typing.TypeVar("System_IO_UnmanagedMemoryAccessor_Read_T")
System_IO_UnmanagedMemoryAccessor_ReadArray_T = typing.TypeVar("System_IO_UnmanagedMemoryAccessor_ReadArray_T")
System_IO_UnmanagedMemoryAccessor_WriteArray_T = typing.TypeVar("System_IO_UnmanagedMemoryAccessor_WriteArray_T")


class FileAccess(System.Enum):
    """This class has no documentation."""

    Read = 1

    Write = 2

    ReadWrite = 3


class EnumerationOptions(System.Object):
    """Provides file and directory enumeration options."""

    DefaultMaxRecursionDepth: int = ...

    Compatible: System.IO.EnumerationOptions
    """
    For internal use. These are the options we want to use if calling the existing Directory/File APIs where you don't
    explicitly specify EnumerationOptions.
    """

    Default: System.IO.EnumerationOptions
    """Internal singleton for default options."""

    @property
    def RecurseSubdirectories(self) -> bool:
        """Gets or sets a value that indicates whether to recurse into subdirectories while enumerating. The default is false."""
        ...

    @RecurseSubdirectories.setter
    def RecurseSubdirectories(self, value: bool):
        """Gets or sets a value that indicates whether to recurse into subdirectories while enumerating. The default is false."""
        ...

    @property
    def IgnoreInaccessible(self) -> bool:
        """Gets or sets a value that indicates whether to skip files or directories when access is denied (for example, System.UnauthorizedAccessException or System.Security.SecurityException). The default is true."""
        ...

    @IgnoreInaccessible.setter
    def IgnoreInaccessible(self, value: bool):
        """Gets or sets a value that indicates whether to skip files or directories when access is denied (for example, System.UnauthorizedAccessException or System.Security.SecurityException). The default is true."""
        ...

    @property
    def BufferSize(self) -> int:
        """Gets or sets the suggested buffer size, in bytes. The default is 0 (no suggestion)."""
        ...

    @BufferSize.setter
    def BufferSize(self, value: int):
        """Gets or sets the suggested buffer size, in bytes. The default is 0 (no suggestion)."""
        ...

    @property
    def AttributesToSkip(self) -> int:
        """
        Gets or sets the attributes to skip. The default is FileAttributes.Hidden | FileAttributes.System.
        
        This property contains the int value of a member of the System.IO.FileAttributes enum.
        """
        ...

    @AttributesToSkip.setter
    def AttributesToSkip(self, value: int):
        """
        Gets or sets the attributes to skip. The default is FileAttributes.Hidden | FileAttributes.System.
        
        This property contains the int value of a member of the System.IO.FileAttributes enum.
        """
        ...

    @property
    def MatchType(self) -> int:
        """
        Gets or sets the match type.
        
        This property contains the int value of a member of the System.IO.MatchType enum.
        """
        ...

    @MatchType.setter
    def MatchType(self, value: int):
        """
        Gets or sets the match type.
        
        This property contains the int value of a member of the System.IO.MatchType enum.
        """
        ...

    @property
    def MatchCasing(self) -> int:
        """
        Gets or sets the case matching behavior.
        
        This property contains the int value of a member of the System.IO.MatchCasing enum.
        """
        ...

    @MatchCasing.setter
    def MatchCasing(self, value: int):
        """
        Gets or sets the case matching behavior.
        
        This property contains the int value of a member of the System.IO.MatchCasing enum.
        """
        ...

    @property
    def MaxRecursionDepth(self) -> int:
        """Gets or sets a value that indicates the maximum directory depth to recurse while enumerating, when RecurseSubdirectories is set to true."""
        ...

    @MaxRecursionDepth.setter
    def MaxRecursionDepth(self, value: int):
        """Gets or sets a value that indicates the maximum directory depth to recurse while enumerating, when RecurseSubdirectories is set to true."""
        ...

    @property
    def ReturnSpecialDirectories(self) -> bool:
        """Gets or sets a value that indicates whether to return the special directory entries "." and ".."."""
        ...

    @ReturnSpecialDirectories.setter
    def ReturnSpecialDirectories(self, value: bool):
        """Gets or sets a value that indicates whether to return the special directory entries "." and ".."."""
        ...

    def __init__(self) -> None:
        """Initializes a new instance of the EnumerationOptions class with the recommended default options."""
        ...


class TextReader(System.MarshalByRefObject, System.IDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    Null: System.IO.TextReader = ...

    def __init__(self) -> None:
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

    def Peek(self) -> int:
        ...

    @overload
    def Read(self) -> int:
        ...

    @overload
    def Read(self, buffer: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def Read(self, buffer: System.Span[str]) -> int:
        ...

    @overload
    def ReadAsync(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def ReadAsync(self, buffer: System.Memory[str], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    @overload
    def ReadBlock(self, buffer: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def ReadBlock(self, buffer: System.Span[str]) -> int:
        ...

    @overload
    def ReadBlockAsync(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def ReadBlockAsync(self, buffer: System.Memory[str], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def ReadLine(self) -> str:
        ...

    @overload
    def ReadLineAsync(self) -> System.Threading.Tasks.Task[str]:
        ...

    @overload
    def ReadLineAsync(self, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.ValueTask[str]:
        """
        Reads a line of characters asynchronously and returns the data as a string.
        
        :param cancellationToken: The token to monitor for cancellation requests.
        :returns: A value task that represents the asynchronous read operation. The value of the TResult parameter contains the next line from the text reader, or is null if all of the characters have been read.
        """
        ...

    def ReadToEnd(self) -> str:
        ...

    @overload
    def ReadToEndAsync(self) -> System.Threading.Tasks.Task[str]:
        ...

    @overload
    def ReadToEndAsync(self, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[str]:
        """
        Reads all characters from the current position to the end of the text reader asynchronously and returns them as one string.
        
        :param cancellationToken: The token to monitor for cancellation requests.
        :returns: A task that represents the asynchronous read operation. The value of the TResult parameter contains a string with the characters from the current position to the end of the text reader.
        """
        ...

    @staticmethod
    def Synchronized(reader: System.IO.TextReader) -> System.IO.TextReader:
        ...


class SeekOrigin(System.Enum):
    """This class has no documentation."""

    Begin = 0

    Current = 1

    End = 2


class Stream(System.MarshalByRefObject, System.IDisposable, System.IAsyncDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    Null: System.IO.Stream = ...

    @property
    @abc.abstractmethod
    def CanRead(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def CanWrite(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def CanSeek(self) -> bool:
        ...

    @property
    def CanTimeout(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def Length(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def Position(self) -> int:
        ...

    @Position.setter
    @abc.abstractmethod
    def Position(self, value: int):
        ...

    @property
    def ReadTimeout(self) -> int:
        ...

    @ReadTimeout.setter
    def ReadTimeout(self, value: int):
        ...

    @property
    def WriteTimeout(self) -> int:
        ...

    @WriteTimeout.setter
    def WriteTimeout(self, value: int):
        ...

    def BeginRead(self, buffer: typing.List[int], offset: int, count: int, callback: typing.Callable[[System.IAsyncResult], None], state: typing.Any) -> System.IAsyncResult:
        ...

    def BeginWrite(self, buffer: typing.List[int], offset: int, count: int, callback: typing.Callable[[System.IAsyncResult], None], state: typing.Any) -> System.IAsyncResult:
        ...

    def Close(self) -> None:
        ...

    @overload
    def CopyTo(self, destination: System.IO.Stream) -> None:
        ...

    @overload
    def CopyTo(self, destination: System.IO.Stream, bufferSize: int) -> None:
        ...

    @overload
    def CopyToAsync(self, destination: System.IO.Stream) -> System.Threading.Tasks.Task:
        ...

    @overload
    def CopyToAsync(self, destination: System.IO.Stream, bufferSize: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def CopyToAsync(self, destination: System.IO.Stream, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def CopyToAsync(self, destination: System.IO.Stream, bufferSize: int, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    def CreateWaitHandle(self) -> System.Threading.WaitHandle:
        """
        This method is protected.
        
        CreateWaitHandle has been deprecated. Use the ManualResetEvent(false) constructor instead.
        """
        warnings.warn("CreateWaitHandle has been deprecated. Use the ManualResetEvent(false) constructor instead.", DeprecationWarning)

    @overload
    def Dispose(self) -> None:
        ...

    @overload
    def Dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def DisposeAsync(self) -> System.Threading.Tasks.ValueTask:
        ...

    def EndRead(self, asyncResult: System.IAsyncResult) -> int:
        ...

    def EndWrite(self, asyncResult: System.IAsyncResult) -> None:
        ...

    def Flush(self) -> None:
        ...

    @overload
    def FlushAsync(self) -> System.Threading.Tasks.Task:
        ...

    @overload
    def FlushAsync(self, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    def ObjectInvariant(self) -> None:
        """
        This method is protected.
        
        Do not call or override this method.
        """
        warnings.warn("Do not call or override this method.", DeprecationWarning)

    @overload
    def Read(self, buffer: typing.List[int], offset: int, count: int) -> int:
        ...

    @overload
    def Read(self, buffer: System.Span[int]) -> int:
        ...

    @overload
    def ReadAsync(self, buffer: typing.List[int], offset: int, count: int) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def ReadAsync(self, buffer: typing.List[int], offset: int, count: int, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def ReadAsync(self, buffer: System.Memory[int], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def ReadAtLeast(self, buffer: System.Span[int], minimumBytes: int, throwOnEndOfStream: bool = True) -> int:
        """
        Reads at least a minimum number of bytes from the current stream and advances the position within the stream by the number of bytes read.
        
        :param buffer: A region of memory. When this method returns, the contents of this region are replaced by the bytes read from the current stream.
        :param minimumBytes: The minimum number of bytes to read into the buffer.
        :param throwOnEndOfStream: true to throw an exception if the end of the stream is reached before reading  of bytes; false to return less than  when the end of the stream is reached. The default is true.
        :returns: The total number of bytes read into the buffer. This is guaranteed to be greater than or equal to  when  is true. This will be less than  when the end of the stream is reached and  is false. This can be less than the number of bytes allocated in the buffer if that many bytes are not currently available.
        """
        ...

    def ReadAtLeastAsync(self, buffer: System.Memory[int], minimumBytes: int, throwOnEndOfStream: bool = True, cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        """
        Asynchronously reads at least a minimum number of bytes from the current stream, advances the position within the stream by the
        number of bytes read, and monitors cancellation requests.
        
        :param buffer: The region of memory to write the data into.
        :param minimumBytes: The minimum number of bytes to read into the buffer.
        :param throwOnEndOfStream: true to throw an exception if the end of the stream is reached before reading  of bytes; false to return less than  when the end of the stream is reached. The default is true.
        :param cancellationToken: The token to monitor for cancellation requests.
        :returns: A task that represents the asynchronous read operation. The value of its ValueTask{TResult}.Result property contains the total number of bytes read into the buffer. This is guaranteed to be greater than or equal to  when  is true. This will be less than  when the end of the stream is reached and  is false. This can be less than the number of bytes allocated in the buffer if that many bytes are not currently available.
        """
        ...

    def ReadByte(self) -> int:
        ...

    @overload
    def ReadExactly(self, buffer: System.Span[int]) -> None:
        """
        Reads bytes from the current stream and advances the position within the stream until the  is filled.
        
        :param buffer: A region of memory. When this method returns, the contents of this region are replaced by the bytes read from the current stream.
        """
        ...

    @overload
    def ReadExactly(self, buffer: typing.List[int], offset: int, count: int) -> None:
        """
        Reads  number of bytes from the current stream and advances the position within the stream.
        
        :param buffer: An array of bytes. When this method returns, the buffer contains the specified byte array with the values between  and ( +  - 1) replaced by the bytes read from the current stream.
        :param offset: The byte offset in  at which to begin storing the data read from the current stream.
        :param count: The number of bytes to be read from the current stream.
        """
        ...

    @overload
    def ReadExactlyAsync(self, buffer: System.Memory[int], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        """
        Asynchronously reads bytes from the current stream, advances the position within the stream until the  is filled,
        and monitors cancellation requests.
        
        :param buffer: The buffer to write the data into.
        :param cancellationToken: The token to monitor for cancellation requests.
        :returns: A task that represents the asynchronous read operation.
        """
        ...

    @overload
    def ReadExactlyAsync(self, buffer: typing.List[int], offset: int, count: int, cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        """
        Asynchronously reads  number of bytes from the current stream, advances the position within the stream,
        and monitors cancellation requests.
        
        :param buffer: The buffer to write the data into.
        :param offset: The byte offset in  at which to begin writing data from the stream.
        :param count: The number of bytes to be read from the current stream.
        :param cancellationToken: The token to monitor for cancellation requests.
        :returns: A task that represents the asynchronous read operation.
        """
        ...

    def Seek(self, offset: int, origin: System.IO.SeekOrigin) -> int:
        ...

    def SetLength(self, value: int) -> None:
        ...

    @staticmethod
    def Synchronized(stream: System.IO.Stream) -> System.IO.Stream:
        ...

    @staticmethod
    def ValidateBufferArguments(buffer: typing.List[int], offset: int, count: int) -> None:
        """
        Validates arguments provided to reading and writing methods on Stream.
        
        This method is protected.
        
        :param buffer: The array "buffer" argument passed to the reading or writing method.
        :param offset: The integer "offset" argument passed to the reading or writing method.
        :param count: The integer "count" argument passed to the reading or writing method.
        """
        ...

    @staticmethod
    def ValidateCopyToArguments(destination: System.IO.Stream, bufferSize: int) -> None:
        """
        Validates arguments provided to the CopyTo(Stream, int) or CopyToAsync(Stream, int, CancellationToken) methods.
        
        This method is protected.
        
        :param destination: The Stream "destination" argument passed to the copy method.
        :param bufferSize: The integer "bufferSize" argument passed to the copy method.
        """
        ...

    @overload
    def Write(self, buffer: typing.List[int], offset: int, count: int) -> None:
        ...

    @overload
    def Write(self, buffer: System.ReadOnlySpan[int]) -> None:
        ...

    @overload
    def WriteAsync(self, buffer: typing.List[int], offset: int, count: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteAsync(self, buffer: typing.List[int], offset: int, count: int, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteAsync(self, buffer: System.ReadOnlyMemory[int], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        ...

    def WriteByte(self, value: int) -> None:
        ...


class UnixFileMode(System.Enum):
    """Represents the Unix filesystem permissions.This enumeration supports a bitwise combination of its member values."""

    # Cannot convert to Python: None = 0
    """No permissions."""

    OtherExecute = 1
    """Execute permission for others."""

    OtherWrite = 2
    """Write permission for others."""

    OtherRead = 4
    """Read permission for others."""

    GroupExecute = 8
    """Execute permission for group."""

    GroupWrite = 16
    """Write permission for group."""

    GroupRead = 32
    """Read permission for group."""

    UserExecute = 64
    """Execute permission for owner."""

    UserWrite = 128
    """Write permission for owner."""

    UserRead = 256
    """Read permission for owner."""

    StickyBit = 512
    """Sticky bit permission."""

    SetGroup = 1024
    """Set Group permission."""

    SetUser = 2048
    """Set User permission."""


class FileStreamOptions(System.Object):
    """This class has no documentation."""

    @property
    def Mode(self) -> int:
        """
        One of the enumeration values that determines how to open or create the file.
        
        This property contains the int value of a member of the System.IO.FileMode enum.
        """
        ...

    @Mode.setter
    def Mode(self, value: int):
        """
        One of the enumeration values that determines how to open or create the file.
        
        This property contains the int value of a member of the System.IO.FileMode enum.
        """
        ...

    @property
    def Access(self) -> int:
        """
        A bitwise combination of the enumeration values that determines how the file can be accessed by the FileStream object. This also determines the values returned by the System.IO.FileStream.CanRead and System.IO.FileStream.CanWrite properties of the FileStream object.
        
        This property contains the int value of a member of the System.IO.FileAccess enum.
        """
        ...

    @Access.setter
    def Access(self, value: int):
        """
        A bitwise combination of the enumeration values that determines how the file can be accessed by the FileStream object. This also determines the values returned by the System.IO.FileStream.CanRead and System.IO.FileStream.CanWrite properties of the FileStream object.
        
        This property contains the int value of a member of the System.IO.FileAccess enum.
        """
        ...

    @property
    def Share(self) -> int:
        """
        A bitwise combination of the enumeration values that determines how the file will be shared by processes. The default value is System.IO.FileShare.Read.
        
        This property contains the int value of a member of the System.IO.FileShare enum.
        """
        ...

    @Share.setter
    def Share(self, value: int):
        """
        A bitwise combination of the enumeration values that determines how the file will be shared by processes. The default value is System.IO.FileShare.Read.
        
        This property contains the int value of a member of the System.IO.FileShare enum.
        """
        ...

    @property
    def Options(self) -> int:
        """
        A bitwise combination of the enumeration values that specifies additional file options. The default value is System.IO.FileOptions.None, which indicates synchronous IO.
        
        This property contains the int value of a member of the System.IO.FileOptions enum.
        """
        ...

    @Options.setter
    def Options(self, value: int):
        """
        A bitwise combination of the enumeration values that specifies additional file options. The default value is System.IO.FileOptions.None, which indicates synchronous IO.
        
        This property contains the int value of a member of the System.IO.FileOptions enum.
        """
        ...

    @property
    def PreallocationSize(self) -> int:
        """
        The initial allocation size in bytes for the file. A positive value is effective only when a regular file is being created, overwritten, or replaced.
        Negative values are not allowed.
        In other cases (including the default 0 value), it's ignored.
        """
        ...

    @PreallocationSize.setter
    def PreallocationSize(self, value: int):
        """
        The initial allocation size in bytes for the file. A positive value is effective only when a regular file is being created, overwritten, or replaced.
        Negative values are not allowed.
        In other cases (including the default 0 value), it's ignored.
        """
        ...

    @property
    def BufferSize(self) -> int:
        """
        The size of the buffer used by FileStream for buffering. The default buffer size is 4096.
        0 or 1 means that buffering should be disabled. Negative values are not allowed.
        """
        ...

    @BufferSize.setter
    def BufferSize(self, value: int):
        """
        The size of the buffer used by FileStream for buffering. The default buffer size is 4096.
        0 or 1 means that buffering should be disabled. Negative values are not allowed.
        """
        ...

    @property
    def UnixCreateMode(self) -> typing.Optional[System.IO.UnixFileMode]:
        """Unix file mode used when a new file is created."""
        ...

    @UnixCreateMode.setter
    def UnixCreateMode(self, value: typing.Optional[System.IO.UnixFileMode]):
        """Unix file mode used when a new file is created."""
        ...


class StreamReader(System.IO.TextReader):
    """This class has no documentation."""

    Null: System.IO.StreamReader = ...

    @property
    def CurrentEncoding(self) -> System.Text.Encoding:
        ...

    @property
    def BaseStream(self) -> System.IO.Stream:
        ...

    @property
    def EndOfStream(self) -> bool:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, detectEncodingFromByteOrderMarks: bool) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding, detectEncodingFromByteOrderMarks: bool) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding = None, detectEncodingFromByteOrderMarks: bool = True, bufferSize: int = -1, leaveOpen: bool = False) -> None:
        ...

    @overload
    def __init__(self, path: str) -> None:
        ...

    @overload
    def __init__(self, path: str, detectEncodingFromByteOrderMarks: bool) -> None:
        ...

    @overload
    def __init__(self, path: str, encoding: System.Text.Encoding) -> None:
        ...

    @overload
    def __init__(self, path: str, encoding: System.Text.Encoding, detectEncodingFromByteOrderMarks: bool) -> None:
        ...

    @overload
    def __init__(self, path: str, encoding: System.Text.Encoding, detectEncodingFromByteOrderMarks: bool, bufferSize: int) -> None:
        ...

    @overload
    def __init__(self, path: str, options: System.IO.FileStreamOptions) -> None:
        ...

    @overload
    def __init__(self, path: str, encoding: System.Text.Encoding, detectEncodingFromByteOrderMarks: bool, options: System.IO.FileStreamOptions) -> None:
        ...

    def Close(self) -> None:
        ...

    def DiscardBufferedData(self) -> None:
        ...

    def Dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def Peek(self) -> int:
        ...

    @overload
    def Read(self) -> int:
        ...

    @overload
    def Read(self, buffer: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def Read(self, buffer: System.Span[str]) -> int:
        ...

    @overload
    def ReadAsync(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def ReadAsync(self, buffer: System.Memory[str], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    @overload
    def ReadBlock(self, buffer: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def ReadBlock(self, buffer: System.Span[str]) -> int:
        ...

    @overload
    def ReadBlockAsync(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def ReadBlockAsync(self, buffer: System.Memory[str], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def ReadLine(self) -> str:
        ...

    @overload
    def ReadLineAsync(self) -> System.Threading.Tasks.Task[str]:
        ...

    @overload
    def ReadLineAsync(self, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.ValueTask[str]:
        """
        Reads a line of characters asynchronously from the current stream and returns the data as a string.
        
        :param cancellationToken: The token to monitor for cancellation requests.
        :returns: A value task that represents the asynchronous read operation. The value of the TResult parameter contains the next line from the stream, or is null if all of the characters have been read.
        """
        ...

    def ReadToEnd(self) -> str:
        ...

    @overload
    def ReadToEndAsync(self) -> System.Threading.Tasks.Task[str]:
        ...

    @overload
    def ReadToEndAsync(self, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[str]:
        """
        Reads all characters from the current position to the end of the stream asynchronously and returns them as one string.
        
        :param cancellationToken: The token to monitor for cancellation requests.
        :returns: A task that represents the asynchronous read operation. The value of the TResult parameter contains a string with the characters from the current position to the end of the stream.
        """
        ...


class TextWriter(System.MarshalByRefObject, System.IDisposable, System.IAsyncDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    Null: System.IO.TextWriter = ...

    @property
    def CoreNewLine(self) -> typing.List[str]:
        """
        This is the 'NewLine' property expressed as a char[].
        It is exposed to subclasses as a protected field for read-only
        purposes.  You should only modify it by using the 'NewLine' property.
        In particular you should never modify the elements of the array
        as they are shared among many instances of TextWriter.
        
        This field is protected.
        """
        ...

    @CoreNewLine.setter
    def CoreNewLine(self, value: typing.List[str]):
        """
        This is the 'NewLine' property expressed as a char[].
        It is exposed to subclasses as a protected field for read-only
        purposes.  You should only modify it by using the 'NewLine' property.
        In particular you should never modify the elements of the array
        as they are shared among many instances of TextWriter.
        
        This field is protected.
        """
        ...

    @property
    def FormatProvider(self) -> System.IFormatProvider:
        ...

    @property
    @abc.abstractmethod
    def Encoding(self) -> System.Text.Encoding:
        ...

    @property
    def NewLine(self) -> str:
        """
        Returns the line terminator string used by this TextWriter. The default line
        terminator string is Environment.NewLine, which is platform specific.
        On Windows this is a carriage return followed by a line feed ("\\r\\n").
        On OSX and Linux this is a line feed ("\\n").
        """
        ...

    @NewLine.setter
    def NewLine(self, value: str):
        """
        Returns the line terminator string used by this TextWriter. The default line
        terminator string is Environment.NewLine, which is platform specific.
        On Windows this is a carriage return followed by a line feed ("\\r\\n").
        On OSX and Linux this is a line feed ("\\n").
        """
        ...

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, formatProvider: System.IFormatProvider) -> None:
        """This method is protected."""
        ...

    def Close(self) -> None:
        ...

    @overload
    def Dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    @overload
    def Dispose(self) -> None:
        ...

    def DisposeAsync(self) -> System.Threading.Tasks.ValueTask:
        ...

    def Flush(self) -> None:
        ...

    def FlushAsync(self) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    def Synchronized(writer: System.IO.TextWriter) -> System.IO.TextWriter:
        ...

    @overload
    def Write(self, value: str) -> None:
        ...

    @overload
    def Write(self, buffer: typing.List[str]) -> None:
        ...

    @overload
    def Write(self, buffer: typing.List[str], index: int, count: int) -> None:
        ...

    @overload
    def Write(self, buffer: System.ReadOnlySpan[str]) -> None:
        ...

    @overload
    def Write(self, value: bool) -> None:
        ...

    @overload
    def Write(self, value: int) -> None:
        ...

    @overload
    def Write(self, value: int) -> None:
        ...

    @overload
    def Write(self, value: int) -> None:
        ...

    @overload
    def Write(self, value: int) -> None:
        ...

    @overload
    def Write(self, value: float) -> None:
        ...

    @overload
    def Write(self, value: float) -> None:
        ...

    @overload
    def Write(self, value: float) -> None:
        ...

    @overload
    def Write(self, value: str) -> None:
        ...

    @overload
    def Write(self, value: typing.Any) -> None:
        ...

    @overload
    def Write(self, value: System.Text.StringBuilder) -> None:
        """
        Equivalent to Write(stringBuilder.ToString()) however it uses the
        StringBuilder.GetChunks() method to avoid creating the intermediate string
        
        :param value: The string (as a StringBuilder) to write to the stream
        """
        ...

    @overload
    def Write(self, format: str, arg0: typing.Any) -> None:
        ...

    @overload
    def Write(self, format: str, arg0: typing.Any, arg1: typing.Any) -> None:
        ...

    @overload
    def Write(self, format: str, arg0: typing.Any, arg1: typing.Any, arg2: typing.Any) -> None:
        ...

    @overload
    def Write(self, format: str, *arg: typing.Any) -> None:
        ...

    @overload
    def WriteAsync(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteAsync(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteAsync(self, value: System.Text.StringBuilder, cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        """
        Equivalent to WriteAsync(stringBuilder.ToString()) however it uses the
        StringBuilder.GetChunks() method to avoid creating the intermediate string
        
        :param value: The string (as a StringBuilder) to write to the stream
        :param cancellationToken: The token to monitor for cancellation requests.
        """
        ...

    @overload
    def WriteAsync(self, buffer: typing.List[str]) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteAsync(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteAsync(self, buffer: System.ReadOnlyMemory[str], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteLine(self) -> None:
        ...

    @overload
    def WriteLine(self, value: str) -> None:
        ...

    @overload
    def WriteLine(self, buffer: typing.List[str]) -> None:
        ...

    @overload
    def WriteLine(self, buffer: typing.List[str], index: int, count: int) -> None:
        ...

    @overload
    def WriteLine(self, buffer: System.ReadOnlySpan[str]) -> None:
        ...

    @overload
    def WriteLine(self, value: bool) -> None:
        ...

    @overload
    def WriteLine(self, value: int) -> None:
        ...

    @overload
    def WriteLine(self, value: int) -> None:
        ...

    @overload
    def WriteLine(self, value: int) -> None:
        ...

    @overload
    def WriteLine(self, value: int) -> None:
        ...

    @overload
    def WriteLine(self, value: float) -> None:
        ...

    @overload
    def WriteLine(self, value: float) -> None:
        ...

    @overload
    def WriteLine(self, value: float) -> None:
        ...

    @overload
    def WriteLine(self, value: str) -> None:
        ...

    @overload
    def WriteLine(self, value: System.Text.StringBuilder) -> None:
        """
        Equivalent to WriteLine(stringBuilder.ToString()) however it uses the
        StringBuilder.GetChunks() method to avoid creating the intermediate string
        """
        ...

    @overload
    def WriteLine(self, value: typing.Any) -> None:
        ...

    @overload
    def WriteLine(self, format: str, arg0: typing.Any) -> None:
        ...

    @overload
    def WriteLine(self, format: str, arg0: typing.Any, arg1: typing.Any) -> None:
        ...

    @overload
    def WriteLine(self, format: str, arg0: typing.Any, arg1: typing.Any, arg2: typing.Any) -> None:
        ...

    @overload
    def WriteLine(self, format: str, *arg: typing.Any) -> None:
        ...

    @overload
    def WriteLineAsync(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteLineAsync(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteLineAsync(self, value: System.Text.StringBuilder, cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        """
        Equivalent to WriteLineAsync(stringBuilder.ToString()) however it uses the
        StringBuilder.GetChunks() method to avoid creating the intermediate string
        
        :param value: The string (as a StringBuilder) to write to the stream
        :param cancellationToken: The token to monitor for cancellation requests.
        """
        ...

    @overload
    def WriteLineAsync(self, buffer: typing.List[str]) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteLineAsync(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteLineAsync(self, buffer: System.ReadOnlyMemory[str], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteLineAsync(self) -> System.Threading.Tasks.Task:
        ...


class StreamWriter(System.IO.TextWriter):
    """This class has no documentation."""

    Null: System.IO.StreamWriter = ...

    @property
    def AutoFlush(self) -> bool:
        ...

    @AutoFlush.setter
    def AutoFlush(self, value: bool):
        ...

    @property
    def BaseStream(self) -> System.IO.Stream:
        ...

    @property
    def Encoding(self) -> System.Text.Encoding:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding, bufferSize: int) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding = None, bufferSize: int = -1, leaveOpen: bool = False) -> None:
        ...

    @overload
    def __init__(self, path: str) -> None:
        ...

    @overload
    def __init__(self, path: str, append: bool) -> None:
        ...

    @overload
    def __init__(self, path: str, append: bool, encoding: System.Text.Encoding) -> None:
        ...

    @overload
    def __init__(self, path: str, append: bool, encoding: System.Text.Encoding, bufferSize: int) -> None:
        ...

    @overload
    def __init__(self, path: str, options: System.IO.FileStreamOptions) -> None:
        ...

    @overload
    def __init__(self, path: str, encoding: System.Text.Encoding, options: System.IO.FileStreamOptions) -> None:
        ...

    def Close(self) -> None:
        ...

    def Dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def DisposeAsync(self) -> System.Threading.Tasks.ValueTask:
        ...

    def Flush(self) -> None:
        ...

    def FlushAsync(self) -> System.Threading.Tasks.Task:
        ...

    @overload
    def Write(self, value: str) -> None:
        ...

    @overload
    def Write(self, buffer: typing.List[str]) -> None:
        ...

    @overload
    def Write(self, buffer: typing.List[str], index: int, count: int) -> None:
        ...

    @overload
    def Write(self, buffer: System.ReadOnlySpan[str]) -> None:
        ...

    @overload
    def Write(self, value: str) -> None:
        ...

    @overload
    def Write(self, format: str, arg0: typing.Any) -> None:
        ...

    @overload
    def Write(self, format: str, arg0: typing.Any, arg1: typing.Any) -> None:
        ...

    @overload
    def Write(self, format: str, arg0: typing.Any, arg1: typing.Any, arg2: typing.Any) -> None:
        ...

    @overload
    def Write(self, format: str, *arg: typing.Any) -> None:
        ...

    @overload
    def WriteAsync(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteAsync(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteAsync(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteAsync(self, buffer: System.ReadOnlyMemory[str], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteLine(self, value: str) -> None:
        ...

    @overload
    def WriteLine(self, buffer: System.ReadOnlySpan[str]) -> None:
        ...

    @overload
    def WriteLine(self, format: str, arg0: typing.Any) -> None:
        ...

    @overload
    def WriteLine(self, format: str, arg0: typing.Any, arg1: typing.Any) -> None:
        ...

    @overload
    def WriteLine(self, format: str, arg0: typing.Any, arg1: typing.Any, arg2: typing.Any) -> None:
        ...

    @overload
    def WriteLine(self, format: str, *arg: typing.Any) -> None:
        ...

    @overload
    def WriteLineAsync(self) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteLineAsync(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteLineAsync(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteLineAsync(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteLineAsync(self, buffer: System.ReadOnlyMemory[str], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...


class FileShare(System.Enum):
    """This class has no documentation."""

    # Cannot convert to Python: None = 0

    Read = 1

    Write = 2

    ReadWrite = 3

    Delete = 4

    Inheritable = ...


class FileMode(System.Enum):
    """This class has no documentation."""

    CreateNew = 1

    Create = 2

    Open = 3

    OpenOrCreate = 4

    Truncate = 5

    Append = 6


class FileOptions(System.Enum):
    """This class has no documentation."""

    # Cannot convert to Python: None = 0

    WriteThrough = ...

    Asynchronous = ...

    RandomAccess = ...

    DeleteOnClose = ...

    SequentialScan = ...

    Encrypted = ...


class FileStream(System.IO.Stream):
    """This class has no documentation."""

    DefaultBufferSize: int = 4096

    DefaultShare: System.IO.FileShare = ...

    @property
    def Handle(self) -> System.IntPtr:
        """FileStream.Handle has been deprecated. Use FileStream's SafeFileHandle property instead."""
        warnings.warn("FileStream.Handle has been deprecated. Use FileStream's SafeFileHandle property instead.", DeprecationWarning)

    @property
    def CanRead(self) -> bool:
        """Gets a value indicating whether the current stream supports reading."""
        ...

    @property
    def CanWrite(self) -> bool:
        """Gets a value indicating whether the current stream supports writing."""
        ...

    @property
    def SafeFileHandle(self) -> Microsoft.Win32.SafeHandles.SafeFileHandle:
        ...

    @property
    def Name(self) -> str:
        """Gets the path that was passed to the constructor."""
        ...

    @property
    def IsAsync(self) -> bool:
        """Gets a value indicating whether the stream was opened for I/O to be performed synchronously or asynchronously."""
        ...

    @property
    def Length(self) -> int:
        """Gets the length of the stream in bytes."""
        ...

    @property
    def Position(self) -> int:
        """Gets or sets the position within the current stream"""
        ...

    @Position.setter
    def Position(self, value: int):
        """Gets or sets the position within the current stream"""
        ...

    @property
    def CanSeek(self) -> bool:
        ...

    @overload
    def __init__(self, handle: Microsoft.Win32.SafeHandles.SafeFileHandle, access: System.IO.FileAccess) -> None:
        ...

    @overload
    def __init__(self, handle: Microsoft.Win32.SafeHandles.SafeFileHandle, access: System.IO.FileAccess, bufferSize: int) -> None:
        ...

    @overload
    def __init__(self, handle: Microsoft.Win32.SafeHandles.SafeFileHandle, access: System.IO.FileAccess, bufferSize: int, isAsync: bool) -> None:
        ...

    @overload
    def __init__(self, path: str, mode: System.IO.FileMode) -> None:
        ...

    @overload
    def __init__(self, path: str, mode: System.IO.FileMode, access: System.IO.FileAccess) -> None:
        ...

    @overload
    def __init__(self, path: str, mode: System.IO.FileMode, access: System.IO.FileAccess, share: System.IO.FileShare) -> None:
        ...

    @overload
    def __init__(self, path: str, mode: System.IO.FileMode, access: System.IO.FileAccess, share: System.IO.FileShare, bufferSize: int) -> None:
        ...

    @overload
    def __init__(self, path: str, mode: System.IO.FileMode, access: System.IO.FileAccess, share: System.IO.FileShare, bufferSize: int, useAsync: bool) -> None:
        ...

    @overload
    def __init__(self, path: str, mode: System.IO.FileMode, access: System.IO.FileAccess, share: System.IO.FileShare, bufferSize: int, options: System.IO.FileOptions) -> None:
        ...

    @overload
    def __init__(self, path: str, options: System.IO.FileStreamOptions) -> None:
        """
        Initializes a new instance of the System.IO.FileStream class with the specified path, creation mode, read/write and sharing permission, the access other FileStreams can have to the same file, the buffer size,  additional file options and the allocation size.
        
        :param path: A relative or absolute path for the file that the current System.IO.FileStream instance will encapsulate.
        :param options: An object that describes optional System.IO.FileStream parameters to use.
        """
        ...

    @overload
    def __init__(self, handle: System.IntPtr, access: System.IO.FileAccess) -> None:
        """This constructor has been deprecated. Use FileStream(SafeFileHandle handle, FileAccess access) instead."""
        ...

    @overload
    def __init__(self, handle: System.IntPtr, access: System.IO.FileAccess, ownsHandle: bool) -> None:
        """This constructor has been deprecated. Use FileStream(SafeFileHandle handle, FileAccess access) and optionally make a new SafeFileHandle with ownsHandle=false if needed instead."""
        ...

    @overload
    def __init__(self, handle: System.IntPtr, access: System.IO.FileAccess, ownsHandle: bool, bufferSize: int) -> None:
        """This constructor has been deprecated. Use FileStream(SafeFileHandle handle, FileAccess access, int bufferSize) and optionally make a new SafeFileHandle with ownsHandle=false if needed instead."""
        ...

    @overload
    def __init__(self, handle: System.IntPtr, access: System.IO.FileAccess, ownsHandle: bool, bufferSize: int, isAsync: bool) -> None:
        """This constructor has been deprecated. Use FileStream(SafeFileHandle handle, FileAccess access, int bufferSize, bool isAsync) and optionally make a new SafeFileHandle with ownsHandle=false if needed instead."""
        ...

    def BeginRead(self, buffer: typing.List[int], offset: int, count: int, callback: typing.Callable[[System.IAsyncResult], None], state: typing.Any) -> System.IAsyncResult:
        ...

    def BeginWrite(self, buffer: typing.List[int], offset: int, count: int, callback: typing.Callable[[System.IAsyncResult], None], state: typing.Any) -> System.IAsyncResult:
        ...

    def CopyTo(self, destination: System.IO.Stream, bufferSize: int) -> None:
        ...

    def CopyToAsync(self, destination: System.IO.Stream, bufferSize: int, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    def Dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def DisposeAsync(self) -> System.Threading.Tasks.ValueTask:
        ...

    def EndRead(self, asyncResult: System.IAsyncResult) -> int:
        ...

    def EndWrite(self, asyncResult: System.IAsyncResult) -> None:
        ...

    @overload
    def Flush(self) -> None:
        """Clears buffers for this stream and causes any buffered data to be written to the file."""
        ...

    @overload
    def Flush(self, flushToDisk: bool) -> None:
        """
        Clears buffers for this stream, and if  is true,
        causes any buffered data to be written to the file.
        """
        ...

    def FlushAsync(self, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    def Lock(self, position: int, length: int) -> None:
        ...

    @overload
    def Read(self, buffer: typing.List[int], offset: int, count: int) -> int:
        ...

    @overload
    def Read(self, buffer: System.Span[int]) -> int:
        ...

    @overload
    def ReadAsync(self, buffer: typing.List[int], offset: int, count: int, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def ReadAsync(self, buffer: System.Memory[int], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def ReadByte(self) -> int:
        """
        Reads a byte from the file stream.  Returns the byte cast to an int
        or -1 if reading from the end of the stream.
        """
        ...

    def Seek(self, offset: int, origin: System.IO.SeekOrigin) -> int:
        ...

    def SetLength(self, value: int) -> None:
        """
        Sets the length of this stream to the given value.
        
        :param value: The new length of the stream.
        """
        ...

    def Unlock(self, position: int, length: int) -> None:
        ...

    @overload
    def Write(self, buffer: typing.List[int], offset: int, count: int) -> None:
        ...

    @overload
    def Write(self, buffer: System.ReadOnlySpan[int]) -> None:
        ...

    @overload
    def WriteAsync(self, buffer: typing.List[int], offset: int, count: int, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteAsync(self, buffer: System.ReadOnlyMemory[int], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        ...

    def WriteByte(self, value: int) -> None:
        """
        Writes a byte to the current position in the stream and advances the position
        within the stream by one byte.
        
        :param value: The byte to write to the stream.
        """
        ...


class FileAttributes(System.Enum):
    """This class has no documentation."""

    ReadOnly = ...

    Hidden = ...

    System = ...

    Directory = ...

    Archive = ...

    Device = ...

    Normal = ...

    Temporary = ...

    SparseFile = ...

    ReparsePoint = ...

    Compressed = ...

    Offline = ...

    NotContentIndexed = ...

    Encrypted = ...

    IntegrityStream = ...

    NoScrubData = ...


class FileSystemInfo(System.MarshalByRefObject, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    @property
    def Attributes(self) -> int:
        """This property contains the int value of a member of the System.IO.FileAttributes enum."""
        ...

    @Attributes.setter
    def Attributes(self, value: int):
        """This property contains the int value of a member of the System.IO.FileAttributes enum."""
        ...

    @property
    def ExistsCore(self) -> bool:
        ...

    @property
    def CreationTimeCore(self) -> System.DateTimeOffset:
        ...

    @CreationTimeCore.setter
    def CreationTimeCore(self, value: System.DateTimeOffset):
        ...

    @property
    def LastAccessTimeCore(self) -> System.DateTimeOffset:
        ...

    @LastAccessTimeCore.setter
    def LastAccessTimeCore(self, value: System.DateTimeOffset):
        ...

    @property
    def LastWriteTimeCore(self) -> System.DateTimeOffset:
        ...

    @LastWriteTimeCore.setter
    def LastWriteTimeCore(self, value: System.DateTimeOffset):
        ...

    @property
    def LengthCore(self) -> int:
        ...

    @property
    def UnixFileModeCore(self) -> int:
        """This property contains the int value of a member of the System.IO.UnixFileMode enum."""
        ...

    @UnixFileModeCore.setter
    def UnixFileModeCore(self, value: int):
        """This property contains the int value of a member of the System.IO.UnixFileMode enum."""
        ...

    @property
    def NormalizedPath(self) -> str:
        ...

    @property
    def FullPath(self) -> str:
        """This field is protected."""
        ...

    @FullPath.setter
    def FullPath(self, value: str):
        """This field is protected."""
        ...

    @property
    def OriginalPath(self) -> str:
        """This field is protected."""
        ...

    @OriginalPath.setter
    def OriginalPath(self, value: str):
        """This field is protected."""
        ...

    @property
    def _name(self) -> str:
        ...

    @_name.setter
    def _name(self, value: str):
        ...

    @property
    def FullName(self) -> str:
        ...

    @property
    def Extension(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def Exists(self) -> bool:
        ...

    @property
    def CreationTime(self) -> datetime.datetime:
        ...

    @CreationTime.setter
    def CreationTime(self, value: datetime.datetime):
        ...

    @property
    def CreationTimeUtc(self) -> datetime.datetime:
        ...

    @CreationTimeUtc.setter
    def CreationTimeUtc(self, value: datetime.datetime):
        ...

    @property
    def LastAccessTime(self) -> datetime.datetime:
        ...

    @LastAccessTime.setter
    def LastAccessTime(self, value: datetime.datetime):
        ...

    @property
    def LastAccessTimeUtc(self) -> datetime.datetime:
        ...

    @LastAccessTimeUtc.setter
    def LastAccessTimeUtc(self, value: datetime.datetime):
        ...

    @property
    def LastWriteTime(self) -> datetime.datetime:
        ...

    @LastWriteTime.setter
    def LastWriteTime(self, value: datetime.datetime):
        ...

    @property
    def LastWriteTimeUtc(self) -> datetime.datetime:
        ...

    @LastWriteTimeUtc.setter
    def LastWriteTimeUtc(self, value: datetime.datetime):
        ...

    @property
    def LinkTarget(self) -> str:
        """
        If this FileSystemInfo instance represents a link, returns the link target's path.
        If a link does not exist in FullName, or this instance does not represent a link, returns null.
        """
        ...

    @property
    def UnixFileMode(self) -> int:
        """
        Gets or sets the Unix file mode for the current file or directory.
        
        This property contains the int value of a member of the System.IO.UnixFileMode enum.
        """
        ...

    @UnixFileMode.setter
    def UnixFileMode(self, value: int):
        """
        Gets or sets the Unix file mode for the current file or directory.
        
        This property contains the int value of a member of the System.IO.UnixFileMode enum.
        """
        ...

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...

    def CreateAsSymbolicLink(self, pathToTarget: str) -> None:
        """
        Creates a symbolic link located in FullName that points to the specified .
        
        :param pathToTarget: The path of the symbolic link target.
        """
        ...

    def Delete(self) -> None:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    @overload
    def Refresh(self) -> None:
        ...

    @overload
    def Refresh(self) -> None:
        ...

    def ResolveLinkTarget(self, returnFinalTarget: bool) -> System.IO.FileSystemInfo:
        """
        Gets the target of the specified link.
        
        :param returnFinalTarget: true to follow links to the final target; false to return the immediate next link.
        :returns: A FileSystemInfo instance if the link exists, independently if the target exists or not; null if this file or directory is not a link.
        """
        ...

    def ToString(self) -> str:
        """Returns the original path. Use FullName or Name properties for the full path or file/directory name."""
        ...


class File(System.Object):
    """This class has no documentation."""

    DefaultBufferSize: int = 4096

    @staticmethod
    @overload
    def AppendAllLines(path: str, contents: System.Collections.Generic.IEnumerable[str]) -> None:
        ...

    @staticmethod
    @overload
    def AppendAllLines(path: str, contents: System.Collections.Generic.IEnumerable[str], encoding: System.Text.Encoding) -> None:
        ...

    @staticmethod
    @overload
    def AppendAllLinesAsync(path: str, contents: System.Collections.Generic.IEnumerable[str], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def AppendAllLinesAsync(path: str, contents: System.Collections.Generic.IEnumerable[str], encoding: System.Text.Encoding, cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def AppendAllText(path: str, contents: str) -> None:
        ...

    @staticmethod
    @overload
    def AppendAllText(path: str, contents: str, encoding: System.Text.Encoding) -> None:
        ...

    @staticmethod
    @overload
    def AppendAllTextAsync(path: str, contents: str, cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def AppendAllTextAsync(path: str, contents: str, encoding: System.Text.Encoding, cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    def AppendText(path: str) -> System.IO.StreamWriter:
        ...

    @staticmethod
    @overload
    def Copy(sourceFileName: str, destFileName: str) -> None:
        """
        Copies an existing file to a new file.
        An exception is raised if the destination file already exists.
        """
        ...

    @staticmethod
    @overload
    def Copy(sourceFileName: str, destFileName: str, overwrite: bool) -> None:
        """
        Copies an existing file to a new file.
        If  is false, an exception will be
        raised if the destination exists. Otherwise it will be overwritten.
        """
        ...

    @staticmethod
    @overload
    def Create(path: str) -> System.IO.FileStream:
        ...

    @staticmethod
    @overload
    def Create(path: str, bufferSize: int) -> System.IO.FileStream:
        ...

    @staticmethod
    @overload
    def Create(path: str, bufferSize: int, options: System.IO.FileOptions) -> System.IO.FileStream:
        ...

    @staticmethod
    def CreateSymbolicLink(path: str, pathToTarget: str) -> System.IO.FileSystemInfo:
        """
        Creates a file symbolic link identified by  that points to .
        
        :param path: The path where the symbolic link should be created.
        :param pathToTarget: The path of the target to which the symbolic link points.
        :returns: A FileInfo instance that wraps the newly created file symbolic link.
        """
        ...

    @staticmethod
    def CreateText(path: str) -> System.IO.StreamWriter:
        ...

    @staticmethod
    def Decrypt(path: str) -> None:
        ...

    @staticmethod
    def Delete(path: str) -> None:
        ...

    @staticmethod
    def Encrypt(path: str) -> None:
        ...

    @staticmethod
    def Exists(path: str) -> bool:
        ...

    @staticmethod
    @overload
    def GetAttributes(path: str) -> int:
        """:returns: This method returns the int value of a member of the System.IO.FileAttributes enum."""
        ...

    @staticmethod
    @overload
    def GetAttributes(fileHandle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> int:
        """
        Gets the specified FileAttributes of the file or directory associated to
        
        :param fileHandle: A SafeFileHandle to the file or directory for which the attributes are to be retrieved.
        :returns: The FileAttributes of the file or directory. This method returns the int value of a member of the System.IO.FileAttributes enum.
        """
        ...

    @staticmethod
    @overload
    def GetCreationTime(path: str) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def GetCreationTime(fileHandle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> datetime.datetime:
        """
        Returns the creation date and time of the specified file or directory.
        
        :param fileHandle: A SafeFileHandle to the file or directory for which to obtain creation date and time information.
        :returns: A DateTime structure set to the creation date and time for the specified file or directory. This value is expressed in local time.
        """
        ...

    @staticmethod
    @overload
    def GetCreationTimeUtc(path: str) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def GetCreationTimeUtc(fileHandle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> datetime.datetime:
        """
        Returns the creation date and time, in coordinated universal time (UTC), of the specified file or directory.
        
        :param fileHandle: A SafeFileHandle to the file or directory for which to obtain creation date and time information.
        :returns: A DateTime structure set to the creation date and time for the specified file or directory. This value is expressed in UTC time.
        """
        ...

    @staticmethod
    @overload
    def GetLastAccessTime(path: str) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def GetLastAccessTime(fileHandle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> datetime.datetime:
        """
        Returns the last access date and time of the specified file or directory.
        
        :param fileHandle: A SafeFileHandle to the file or directory for which to obtain last access date and time information.
        :returns: A DateTime structure set to the last access date and time for the specified file or directory. This value is expressed in local time.
        """
        ...

    @staticmethod
    @overload
    def GetLastAccessTimeUtc(path: str) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def GetLastAccessTimeUtc(fileHandle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> datetime.datetime:
        """
        Returns the last access date and time, in coordinated universal time (UTC), of the specified file or directory.
        
        :param fileHandle: A SafeFileHandle to the file or directory for which to obtain last access date and time information.
        :returns: A DateTime structure set to the last access date and time for the specified file or directory. This value is expressed in UTC time.
        """
        ...

    @staticmethod
    @overload
    def GetLastWriteTime(path: str) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def GetLastWriteTime(fileHandle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> datetime.datetime:
        """
        Returns the last write date and time of the specified file or directory.
        
        :param fileHandle: A SafeFileHandle to the file or directory for which to obtain last write date and time information.
        :returns: A DateTime structure set to the last write date and time for the specified file or directory. This value is expressed in local time.
        """
        ...

    @staticmethod
    @overload
    def GetLastWriteTimeUtc(path: str) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def GetLastWriteTimeUtc(fileHandle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> datetime.datetime:
        """
        Returns the last write date and time, in coordinated universal time (UTC), of the specified file or directory.
        
        :param fileHandle: A SafeFileHandle to the file or directory for which to obtain last write date and time information.
        :returns: A DateTime structure set to the last write date and time for the specified file or directory. This value is expressed in UTC time.
        """
        ...

    @staticmethod
    @overload
    def GetUnixFileMode(path: str) -> int:
        """
        Gets the System.IO.UnixFileMode of the file on the path.
        
        :param path: The path to the file.
        :returns: The System.IO.UnixFileMode of the file on the path. This method returns the int value of a member of the System.IO.UnixFileMode enum.
        """
        ...

    @staticmethod
    @overload
    def GetUnixFileMode(fileHandle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> int:
        """
        Gets the System.IO.UnixFileMode of the specified file handle.
        
        :param fileHandle: The file handle.
        :returns: The System.IO.UnixFileMode of the file handle. This method returns the int value of a member of the System.IO.UnixFileMode enum.
        """
        ...

    @staticmethod
    @overload
    def Move(sourceFileName: str, destFileName: str) -> None:
        ...

    @staticmethod
    @overload
    def Move(sourceFileName: str, destFileName: str, overwrite: bool) -> None:
        ...

    @staticmethod
    @overload
    def Open(path: str, options: System.IO.FileStreamOptions) -> System.IO.FileStream:
        """Initializes a new instance of the FileStream class with the specified path, creation mode, read/write and sharing permission, the access other FileStreams can have to the same file, the buffer size, additional file options and the allocation size."""
        ...

    @staticmethod
    @overload
    def Open(path: str, mode: System.IO.FileMode) -> System.IO.FileStream:
        ...

    @staticmethod
    @overload
    def Open(path: str, mode: System.IO.FileMode, access: System.IO.FileAccess) -> System.IO.FileStream:
        ...

    @staticmethod
    @overload
    def Open(path: str, mode: System.IO.FileMode, access: System.IO.FileAccess, share: System.IO.FileShare) -> System.IO.FileStream:
        ...

    @staticmethod
    def OpenHandle(path: str, mode: System.IO.FileMode = ..., access: System.IO.FileAccess = ..., share: System.IO.FileShare = ..., options: System.IO.FileOptions = ..., preallocationSize: int = 0) -> Microsoft.Win32.SafeHandles.SafeFileHandle:
        """
        Initializes a new instance of the Microsoft.Win32.SafeHandles.SafeFileHandle class with the specified path, creation mode, read/write and sharing permission, the access other SafeFileHandles can have to the same file, additional file options and the allocation size.
        
        :param path: A relative or absolute path for the file that the current Microsoft.Win32.SafeHandles.SafeFileHandle instance will encapsulate.
        :param mode: One of the enumeration values that determines how to open or create the file. The default value is FileMode.Open
        :param access: A bitwise combination of the enumeration values that determines how the file can be accessed. The default value is FileAccess.Read
        :param share: A bitwise combination of the enumeration values that determines how the file will be shared by processes. The default value is FileShare.Read.
        :param options: An object that describes optional Microsoft.Win32.SafeHandles.SafeFileHandle parameters to use.
        :param preallocationSize: The initial allocation size in bytes for the file. A positive value is effective only when a regular file is being created, overwritten, or replaced. Negative values are not allowed. In other cases (including the default 0 value), it's ignored.
        """
        ...

    @staticmethod
    def OpenRead(path: str) -> System.IO.FileStream:
        ...

    @staticmethod
    def OpenText(path: str) -> System.IO.StreamReader:
        ...

    @staticmethod
    def OpenWrite(path: str) -> System.IO.FileStream:
        ...

    @staticmethod
    def ReadAllBytes(path: str) -> typing.List[int]:
        ...

    @staticmethod
    def ReadAllBytesAsync(path: str, cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task[typing.List[int]]:
        ...

    @staticmethod
    @overload
    def ReadAllLines(path: str) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def ReadAllLines(path: str, encoding: System.Text.Encoding) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def ReadAllLinesAsync(path: str, cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task[typing.List[str]]:
        ...

    @staticmethod
    @overload
    def ReadAllLinesAsync(path: str, encoding: System.Text.Encoding, cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task[typing.List[str]]:
        ...

    @staticmethod
    @overload
    def ReadAllText(path: str) -> str:
        ...

    @staticmethod
    @overload
    def ReadAllText(path: str, encoding: System.Text.Encoding) -> str:
        ...

    @staticmethod
    @overload
    def ReadAllTextAsync(path: str, cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task[str]:
        ...

    @staticmethod
    @overload
    def ReadAllTextAsync(path: str, encoding: System.Text.Encoding, cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task[str]:
        ...

    @staticmethod
    @overload
    def ReadLines(path: str) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def ReadLines(path: str, encoding: System.Text.Encoding) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def ReadLinesAsync(path: str, cancellationToken: System.Threading.CancellationToken = ...) -> System.Collections.Generic.IAsyncEnumerable[str]:
        """
        Asynchronously reads the lines of a file.
        
        :param path: The file to read.
        :param cancellationToken: The token to monitor for cancellation requests. The default value is CancellationToken.None.
        :returns: The async enumerable that represents all the lines of the file, or the lines that are the result of a query.
        """
        ...

    @staticmethod
    @overload
    def ReadLinesAsync(path: str, encoding: System.Text.Encoding, cancellationToken: System.Threading.CancellationToken = ...) -> System.Collections.Generic.IAsyncEnumerable[str]:
        """
        Asynchronously reads the lines of a file that has a specified encoding.
        
        :param path: The file to read.
        :param encoding: The encoding that is applied to the contents of the file.
        :param cancellationToken: The token to monitor for cancellation requests. The default value is CancellationToken.None.
        :returns: The async enumerable that represents all the lines of the file, or the lines that are the result of a query.
        """
        ...

    @staticmethod
    @overload
    def Replace(sourceFileName: str, destinationFileName: str, destinationBackupFileName: str) -> None:
        ...

    @staticmethod
    @overload
    def Replace(sourceFileName: str, destinationFileName: str, destinationBackupFileName: str, ignoreMetadataErrors: bool) -> None:
        ...

    @staticmethod
    def ResolveLinkTarget(linkPath: str, returnFinalTarget: bool) -> System.IO.FileSystemInfo:
        """
        Gets the target of the specified file link.
        
        :param linkPath: The path of the file link.
        :param returnFinalTarget: true to follow links to the final target; false to return the immediate next link.
        :returns: A FileInfo instance if  exists, independently if the target exists or not. null if  is not a link.
        """
        ...

    @staticmethod
    @overload
    def SetAttributes(path: str, fileAttributes: System.IO.FileAttributes) -> None:
        ...

    @staticmethod
    @overload
    def SetAttributes(fileHandle: Microsoft.Win32.SafeHandles.SafeFileHandle, fileAttributes: System.IO.FileAttributes) -> None:
        """
        Sets the specified FileAttributes of the file or directory associated to .
        
        :param fileHandle: A SafeFileHandle to the file or directory for which  should be set.
        :param fileAttributes: A bitwise combination of the enumeration values.
        """
        ...

    @staticmethod
    @overload
    def SetCreationTime(path: str, creationTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def SetCreationTime(fileHandle: Microsoft.Win32.SafeHandles.SafeFileHandle, creationTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Sets the date and time the file or directory was created.
        
        :param fileHandle: A SafeFileHandle to the file or directory for which to set the creation date and time information.
        :param creationTime: A DateTime containing the value to set for the creation date and time of . This value is expressed in local time.
        """
        ...

    @staticmethod
    @overload
    def SetCreationTimeUtc(path: str, creationTimeUtc: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def SetCreationTimeUtc(fileHandle: Microsoft.Win32.SafeHandles.SafeFileHandle, creationTimeUtc: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Sets the date and time, in coordinated universal time (UTC), that the file or directory was created.
        
        :param fileHandle: A SafeFileHandle to the file or directory for which to set the creation date and time information.
        :param creationTimeUtc: A DateTime containing the value to set for the creation date and time of . This value is expressed in UTC time.
        """
        ...

    @staticmethod
    @overload
    def SetLastAccessTime(path: str, lastAccessTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def SetLastAccessTime(fileHandle: Microsoft.Win32.SafeHandles.SafeFileHandle, lastAccessTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Sets the date and time the specified file or directory was last accessed.
        
        :param fileHandle: A SafeFileHandle to the file or directory for which to set the last access date and time information.
        :param lastAccessTime: A DateTime containing the value to set for the last access date and time of . This value is expressed in local time.
        """
        ...

    @staticmethod
    @overload
    def SetLastAccessTimeUtc(path: str, lastAccessTimeUtc: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def SetLastAccessTimeUtc(fileHandle: Microsoft.Win32.SafeHandles.SafeFileHandle, lastAccessTimeUtc: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Sets the date and time, in coordinated universal time (UTC), that the specified file or directory was last accessed.
        
        :param fileHandle: A SafeFileHandle to the file or directory for which to set the last access date and time information.
        :param lastAccessTimeUtc: A DateTime containing the value to set for the last access date and time of . This value is expressed in UTC time.
        """
        ...

    @staticmethod
    @overload
    def SetLastWriteTime(path: str, lastWriteTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def SetLastWriteTime(fileHandle: Microsoft.Win32.SafeHandles.SafeFileHandle, lastWriteTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Sets the date and time that the specified file or directory was last written to.
        
        :param fileHandle: A SafeFileHandle to the file or directory for which to set the last write date and time information.
        :param lastWriteTime: A DateTime containing the value to set for the last write date and time of . This value is expressed in local time.
        """
        ...

    @staticmethod
    @overload
    def SetLastWriteTimeUtc(path: str, lastWriteTimeUtc: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def SetLastWriteTimeUtc(fileHandle: Microsoft.Win32.SafeHandles.SafeFileHandle, lastWriteTimeUtc: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Sets the date and time, in coordinated universal time (UTC), that the specified file or directory was last written to.
        
        :param fileHandle: A SafeFileHandle to the file or directory for which to set the last write date and time information.
        :param lastWriteTimeUtc: A DateTime containing the value to set for the last write date and time of . This value is expressed in UTC time.
        """
        ...

    @staticmethod
    @overload
    def SetUnixFileMode(path: str, mode: System.IO.UnixFileMode) -> None:
        """
        Sets the specified System.IO.UnixFileMode of the file on the specified path.
        
        :param path: The path to the file.
        :param mode: The unix file mode.
        """
        ...

    @staticmethod
    @overload
    def SetUnixFileMode(fileHandle: Microsoft.Win32.SafeHandles.SafeFileHandle, mode: System.IO.UnixFileMode) -> None:
        """
        Sets the specified System.IO.UnixFileMode of the specified file handle.
        
        :param fileHandle: The file handle.
        :param mode: The unix file mode.
        """
        ...

    @staticmethod
    def WriteAllBytes(path: str, bytes: typing.List[int]) -> None:
        ...

    @staticmethod
    def WriteAllBytesAsync(path: str, bytes: typing.List[int], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def WriteAllLines(path: str, contents: typing.List[str]) -> None:
        ...

    @staticmethod
    @overload
    def WriteAllLines(path: str, contents: System.Collections.Generic.IEnumerable[str]) -> None:
        ...

    @staticmethod
    @overload
    def WriteAllLines(path: str, contents: typing.List[str], encoding: System.Text.Encoding) -> None:
        ...

    @staticmethod
    @overload
    def WriteAllLines(path: str, contents: System.Collections.Generic.IEnumerable[str], encoding: System.Text.Encoding) -> None:
        ...

    @staticmethod
    @overload
    def WriteAllLinesAsync(path: str, contents: System.Collections.Generic.IEnumerable[str], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def WriteAllLinesAsync(path: str, contents: System.Collections.Generic.IEnumerable[str], encoding: System.Text.Encoding, cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def WriteAllText(path: str, contents: str) -> None:
        ...

    @staticmethod
    @overload
    def WriteAllText(path: str, contents: str, encoding: System.Text.Encoding) -> None:
        ...

    @staticmethod
    @overload
    def WriteAllTextAsync(path: str, contents: str, cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def WriteAllTextAsync(path: str, contents: str, encoding: System.Text.Encoding, cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...


class RandomAccess(System.Object):
    """This class has no documentation."""

    @staticmethod
    def GetLength(handle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> int:
        """
        Gets the length of the file in bytes.
        
        :param handle: The file handle.
        :returns: A long value representing the length of the file in bytes.
        """
        ...

    @staticmethod
    @overload
    def Read(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffer: System.Span[int], fileOffset: int) -> int:
        """
        Reads a sequence of bytes from given file at given offset.
        
        :param handle: The file handle.
        :param buffer: A region of memory. When this method returns, the contents of this region are replaced by the bytes read from the file.
        :param fileOffset: The file position to read from.
        :returns: The total number of bytes read into the buffer. This can be less than the number of bytes allocated in the buffer if that many bytes are not currently available, or zero (0) if the end of the file has been reached.
        """
        ...

    @staticmethod
    @overload
    def Read(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffers: System.Collections.Generic.IReadOnlyList[System.Memory[int]], fileOffset: int) -> int:
        """
        Reads a sequence of bytes from given file at given offset.
        
        :param handle: The file handle.
        :param buffers: A list of memory buffers. When this method returns, the contents of the buffers are replaced by the bytes read from the file.
        :param fileOffset: The file position to read from.
        :returns: The total number of bytes read into the buffers. This can be less than the number of bytes allocated in the buffers if that many bytes are not currently available, or zero (0) if the end of the file has been reached.
        """
        ...

    @staticmethod
    @overload
    def ReadAsync(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffer: System.Memory[int], fileOffset: int, cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        """
        Reads a sequence of bytes from given file at given offset.
        
        :param handle: The file handle.
        :param buffer: A region of memory. When this method returns, the contents of this region are replaced by the bytes read from the file.
        :param fileOffset: The file position to read from.
        :param cancellationToken: The token to monitor for cancellation requests. The default value is System.Threading.CancellationToken.None.
        :returns: The total number of bytes read into the buffer. This can be less than the number of bytes allocated in the buffer if that many bytes are not currently available, or zero (0) if the end of the file has been reached.
        """
        ...

    @staticmethod
    @overload
    def ReadAsync(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffers: System.Collections.Generic.IReadOnlyList[System.Memory[int]], fileOffset: int, cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        """
        Reads a sequence of bytes from given file at given offset.
        
        :param handle: The file handle.
        :param buffers: A list of memory buffers. When this method returns, the contents of these buffers are replaced by the bytes read from the file.
        :param fileOffset: The file position to read from.
        :param cancellationToken: The token to monitor for cancellation requests. The default value is System.Threading.CancellationToken.None.
        :returns: The total number of bytes read into the buffers. This can be less than the number of bytes allocated in the buffers if that many bytes are not currently available, or zero (0) if the end of the file has been reached.
        """
        ...

    @staticmethod
    def SetLength(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, length: int) -> None:
        """
        Sets the length of the file to the given value.
        
        :param handle: The file handle.
        :param length: A long value representing the length of the file in bytes.
        """
        ...

    @staticmethod
    @overload
    def Write(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffer: System.ReadOnlySpan[int], fileOffset: int) -> None:
        """
        Writes a sequence of bytes from given buffer to given file at given offset.
        
        :param handle: The file handle.
        :param buffer: A region of memory. This method copies the contents of this region to the file.
        :param fileOffset: The file position to write to.
        """
        ...

    @staticmethod
    @overload
    def Write(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffers: System.Collections.Generic.IReadOnlyList[System.ReadOnlyMemory[int]], fileOffset: int) -> None:
        """
        Writes a sequence of bytes from given buffers to given file at given offset.
        
        :param handle: The file handle.
        :param buffers: A list of memory buffers. This method copies the contents of these buffers to the file.
        :param fileOffset: The file position to write to.
        """
        ...

    @staticmethod
    @overload
    def WriteAsync(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffer: System.ReadOnlyMemory[int], fileOffset: int, cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        """
        Writes a sequence of bytes from given buffer to given file at given offset.
        
        :param handle: The file handle.
        :param buffer: A region of memory. This method copies the contents of this region to the file.
        :param fileOffset: The file position to write to.
        :param cancellationToken: The token to monitor for cancellation requests. The default value is System.Threading.CancellationToken.None.
        :returns: A task representing the asynchronous completion of the write operation.
        """
        ...

    @staticmethod
    @overload
    def WriteAsync(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffers: System.Collections.Generic.IReadOnlyList[System.ReadOnlyMemory[int]], fileOffset: int, cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        """
        Writes a sequence of bytes from given buffers to given file at given offset.
        
        :param handle: The file handle.
        :param buffers: A list of memory buffers. This method copies the contents of these buffers to the file.
        :param fileOffset: The file position to write to.
        :param cancellationToken: The token to monitor for cancellation requests. The default value is System.Threading.CancellationToken.None.
        :returns: A task representing the asynchronous completion of the write operation.
        """
        ...


class MemoryStream(System.IO.Stream):
    """This class has no documentation."""

    @property
    def CanRead(self) -> bool:
        ...

    @property
    def CanSeek(self) -> bool:
        ...

    @property
    def CanWrite(self) -> bool:
        ...

    @property
    def Capacity(self) -> int:
        ...

    @Capacity.setter
    def Capacity(self, value: int):
        ...

    @property
    def Length(self) -> int:
        ...

    @property
    def Position(self) -> int:
        ...

    @Position.setter
    def Position(self, value: int):
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, buffer: typing.List[int]) -> None:
        ...

    @overload
    def __init__(self, buffer: typing.List[int], writable: bool) -> None:
        ...

    @overload
    def __init__(self, buffer: typing.List[int], index: int, count: int) -> None:
        ...

    @overload
    def __init__(self, buffer: typing.List[int], index: int, count: int, writable: bool) -> None:
        ...

    @overload
    def __init__(self, buffer: typing.List[int], index: int, count: int, writable: bool, publiclyVisible: bool) -> None:
        ...

    def CopyTo(self, destination: System.IO.Stream, bufferSize: int) -> None:
        ...

    def CopyToAsync(self, destination: System.IO.Stream, bufferSize: int, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    def Dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def Flush(self) -> None:
        ...

    def FlushAsync(self, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    def GetBuffer(self) -> typing.List[int]:
        ...

    @overload
    def Read(self, buffer: typing.List[int], offset: int, count: int) -> int:
        ...

    @overload
    def Read(self, buffer: System.Span[int]) -> int:
        ...

    @overload
    def ReadAsync(self, buffer: typing.List[int], offset: int, count: int, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def ReadAsync(self, buffer: System.Memory[int], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def ReadByte(self) -> int:
        ...

    def Seek(self, offset: int, loc: System.IO.SeekOrigin) -> int:
        ...

    def SetLength(self, value: int) -> None:
        ...

    def ToArray(self) -> typing.List[int]:
        ...

    def TryGetBuffer(self, buffer: typing.Optional[System.ArraySegment[int]]) -> typing.Union[bool, System.ArraySegment[int]]:
        ...

    @overload
    def Write(self, buffer: typing.List[int], offset: int, count: int) -> None:
        ...

    @overload
    def Write(self, buffer: System.ReadOnlySpan[int]) -> None:
        ...

    @overload
    def WriteAsync(self, buffer: typing.List[int], offset: int, count: int, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteAsync(self, buffer: System.ReadOnlyMemory[int], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        ...

    def WriteByte(self, value: int) -> None:
        ...

    def WriteTo(self, stream: System.IO.Stream) -> None:
        ...


class IOException(System.SystemException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, hresult: int) -> None:
        ...

    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...


class FileLoadException(System.IO.IOException):
    """This class has no documentation."""

    @property
    def Message(self) -> str:
        ...

    @property
    def FileName(self) -> str:
        ...

    @property
    def FusionLog(self) -> str:
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
    def __init__(self, message: str, fileName: str) -> None:
        ...

    @overload
    def __init__(self, message: str, fileName: str, inner: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def ToString(self) -> str:
        ...


class SearchOption(System.Enum):
    """This class has no documentation."""

    TopDirectoryOnly = 0

    AllDirectories = 1


class FileInfo(System.IO.FileSystemInfo):
    """This class has no documentation."""

    @property
    def Name(self) -> str:
        ...

    @property
    def Length(self) -> int:
        ...

    @property
    def DirectoryName(self) -> str:
        ...

    @property
    def Directory(self) -> System.IO.DirectoryInfo:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @IsReadOnly.setter
    def IsReadOnly(self, value: bool):
        ...

    @property
    def Exists(self) -> bool:
        ...

    def __init__(self, fileName: str) -> None:
        ...

    def AppendText(self) -> System.IO.StreamWriter:
        ...

    @overload
    def CopyTo(self, destFileName: str) -> System.IO.FileInfo:
        ...

    @overload
    def CopyTo(self, destFileName: str, overwrite: bool) -> System.IO.FileInfo:
        ...

    def Create(self) -> System.IO.FileStream:
        ...

    def CreateText(self) -> System.IO.StreamWriter:
        ...

    def Decrypt(self) -> None:
        ...

    def Delete(self) -> None:
        ...

    def Encrypt(self) -> None:
        ...

    @overload
    def MoveTo(self, destFileName: str) -> None:
        ...

    @overload
    def MoveTo(self, destFileName: str, overwrite: bool) -> None:
        ...

    @overload
    def Open(self, options: System.IO.FileStreamOptions) -> System.IO.FileStream:
        """Initializes a new instance of the System.IO.FileStream class with the specified creation mode, read/write and sharing permission, the access other FileStreams can have to the same file, the buffer size, additional file options and the allocation size."""
        ...

    @overload
    def Open(self, mode: System.IO.FileMode) -> System.IO.FileStream:
        ...

    @overload
    def Open(self, mode: System.IO.FileMode, access: System.IO.FileAccess) -> System.IO.FileStream:
        ...

    @overload
    def Open(self, mode: System.IO.FileMode, access: System.IO.FileAccess, share: System.IO.FileShare) -> System.IO.FileStream:
        ...

    def OpenRead(self) -> System.IO.FileStream:
        ...

    def OpenText(self) -> System.IO.StreamReader:
        ...

    def OpenWrite(self) -> System.IO.FileStream:
        ...

    @overload
    def Replace(self, destinationFileName: str, destinationBackupFileName: str) -> System.IO.FileInfo:
        ...

    @overload
    def Replace(self, destinationFileName: str, destinationBackupFileName: str, ignoreMetadataErrors: bool) -> System.IO.FileInfo:
        ...


class DirectoryInfo(System.IO.FileSystemInfo):
    """This class has no documentation."""

    @property
    def Name(self) -> str:
        ...

    @property
    def Parent(self) -> System.IO.DirectoryInfo:
        ...

    @property
    def Root(self) -> System.IO.DirectoryInfo:
        ...

    @property
    def Exists(self) -> bool:
        ...

    def __init__(self, path: str) -> None:
        ...

    def Create(self) -> None:
        ...

    def CreateSubdirectory(self, path: str) -> System.IO.DirectoryInfo:
        ...

    @overload
    def Delete(self) -> None:
        ...

    @overload
    def Delete(self, recursive: bool) -> None:
        ...

    @overload
    def EnumerateDirectories(self) -> System.Collections.Generic.IEnumerable[System.IO.DirectoryInfo]:
        ...

    @overload
    def EnumerateDirectories(self, searchPattern: str) -> System.Collections.Generic.IEnumerable[System.IO.DirectoryInfo]:
        ...

    @overload
    def EnumerateDirectories(self, searchPattern: str, searchOption: System.IO.SearchOption) -> System.Collections.Generic.IEnumerable[System.IO.DirectoryInfo]:
        ...

    @overload
    def EnumerateDirectories(self, searchPattern: str, enumerationOptions: System.IO.EnumerationOptions) -> System.Collections.Generic.IEnumerable[System.IO.DirectoryInfo]:
        ...

    @overload
    def EnumerateFiles(self) -> System.Collections.Generic.IEnumerable[System.IO.FileInfo]:
        ...

    @overload
    def EnumerateFiles(self, searchPattern: str) -> System.Collections.Generic.IEnumerable[System.IO.FileInfo]:
        ...

    @overload
    def EnumerateFiles(self, searchPattern: str, searchOption: System.IO.SearchOption) -> System.Collections.Generic.IEnumerable[System.IO.FileInfo]:
        ...

    @overload
    def EnumerateFiles(self, searchPattern: str, enumerationOptions: System.IO.EnumerationOptions) -> System.Collections.Generic.IEnumerable[System.IO.FileInfo]:
        ...

    @overload
    def EnumerateFileSystemInfos(self) -> System.Collections.Generic.IEnumerable[System.IO.FileSystemInfo]:
        ...

    @overload
    def EnumerateFileSystemInfos(self, searchPattern: str) -> System.Collections.Generic.IEnumerable[System.IO.FileSystemInfo]:
        ...

    @overload
    def EnumerateFileSystemInfos(self, searchPattern: str, searchOption: System.IO.SearchOption) -> System.Collections.Generic.IEnumerable[System.IO.FileSystemInfo]:
        ...

    @overload
    def EnumerateFileSystemInfos(self, searchPattern: str, enumerationOptions: System.IO.EnumerationOptions) -> System.Collections.Generic.IEnumerable[System.IO.FileSystemInfo]:
        ...

    @overload
    def GetDirectories(self) -> typing.List[System.IO.DirectoryInfo]:
        ...

    @overload
    def GetDirectories(self, searchPattern: str) -> typing.List[System.IO.DirectoryInfo]:
        ...

    @overload
    def GetDirectories(self, searchPattern: str, searchOption: System.IO.SearchOption) -> typing.List[System.IO.DirectoryInfo]:
        ...

    @overload
    def GetDirectories(self, searchPattern: str, enumerationOptions: System.IO.EnumerationOptions) -> typing.List[System.IO.DirectoryInfo]:
        ...

    @overload
    def GetFiles(self) -> typing.List[System.IO.FileInfo]:
        ...

    @overload
    def GetFiles(self, searchPattern: str) -> typing.List[System.IO.FileInfo]:
        ...

    @overload
    def GetFiles(self, searchPattern: str, searchOption: System.IO.SearchOption) -> typing.List[System.IO.FileInfo]:
        ...

    @overload
    def GetFiles(self, searchPattern: str, enumerationOptions: System.IO.EnumerationOptions) -> typing.List[System.IO.FileInfo]:
        ...

    @overload
    def GetFileSystemInfos(self) -> typing.List[System.IO.FileSystemInfo]:
        ...

    @overload
    def GetFileSystemInfos(self, searchPattern: str) -> typing.List[System.IO.FileSystemInfo]:
        ...

    @overload
    def GetFileSystemInfos(self, searchPattern: str, searchOption: System.IO.SearchOption) -> typing.List[System.IO.FileSystemInfo]:
        ...

    @overload
    def GetFileSystemInfos(self, searchPattern: str, enumerationOptions: System.IO.EnumerationOptions) -> typing.List[System.IO.FileSystemInfo]:
        ...

    def MoveTo(self, destDirName: str) -> None:
        ...


class Directory(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def CreateDirectory(path: str) -> System.IO.DirectoryInfo:
        ...

    @staticmethod
    @overload
    def CreateDirectory(path: str, unixCreateMode: System.IO.UnixFileMode) -> System.IO.DirectoryInfo:
        """
        Creates all directories and subdirectories in the specified path with the specified permissions unless they already exist.
        
        :param path: The directory to create.
        :param unixCreateMode: Unix file mode used to create directories.
        :returns: An object that represents the directory at the specified path. This object is returned regardless of whether a directory at the specified path already exists.
        """
        ...

    @staticmethod
    def CreateSymbolicLink(path: str, pathToTarget: str) -> System.IO.FileSystemInfo:
        """
        Creates a directory symbolic link identified by  that points to .
        
        :param path: The absolute path where the symbolic link should be created.
        :param pathToTarget: The target directory of the symbolic link.
        :returns: A DirectoryInfo instance that wraps the newly created directory symbolic link.
        """
        ...

    @staticmethod
    def CreateTempSubdirectory(prefix: str = None) -> System.IO.DirectoryInfo:
        """
        Creates a uniquely-named, empty directory in the current user's temporary directory.
        
        :param prefix: An optional string to add to the beginning of the subdirectory name.
        :returns: An object that represents the directory that was created.
        """
        ...

    @staticmethod
    @overload
    def Delete(path: str) -> None:
        ...

    @staticmethod
    @overload
    def Delete(path: str, recursive: bool) -> None:
        ...

    @staticmethod
    @overload
    def EnumerateDirectories(path: str) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def EnumerateDirectories(path: str, searchPattern: str) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def EnumerateDirectories(path: str, searchPattern: str, searchOption: System.IO.SearchOption) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def EnumerateDirectories(path: str, searchPattern: str, enumerationOptions: System.IO.EnumerationOptions) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def EnumerateFiles(path: str) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def EnumerateFiles(path: str, searchPattern: str) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def EnumerateFiles(path: str, searchPattern: str, searchOption: System.IO.SearchOption) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def EnumerateFiles(path: str, searchPattern: str, enumerationOptions: System.IO.EnumerationOptions) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def EnumerateFileSystemEntries(path: str) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def EnumerateFileSystemEntries(path: str, searchPattern: str) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def EnumerateFileSystemEntries(path: str, searchPattern: str, searchOption: System.IO.SearchOption) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def EnumerateFileSystemEntries(path: str, searchPattern: str, enumerationOptions: System.IO.EnumerationOptions) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    def Exists(path: str) -> bool:
        ...

    @staticmethod
    def GetCreationTime(path: str) -> datetime.datetime:
        ...

    @staticmethod
    def GetCreationTimeUtc(path: str) -> datetime.datetime:
        ...

    @staticmethod
    def GetCurrentDirectory() -> str:
        ...

    @staticmethod
    @overload
    def GetDirectories(path: str) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def GetDirectories(path: str, searchPattern: str) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def GetDirectories(path: str, searchPattern: str, searchOption: System.IO.SearchOption) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def GetDirectories(path: str, searchPattern: str, enumerationOptions: System.IO.EnumerationOptions) -> typing.List[str]:
        ...

    @staticmethod
    def GetDirectoryRoot(path: str) -> str:
        ...

    @staticmethod
    @overload
    def GetFiles(path: str) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def GetFiles(path: str, searchPattern: str) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def GetFiles(path: str, searchPattern: str, searchOption: System.IO.SearchOption) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def GetFiles(path: str, searchPattern: str, enumerationOptions: System.IO.EnumerationOptions) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def GetFileSystemEntries(path: str) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def GetFileSystemEntries(path: str, searchPattern: str) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def GetFileSystemEntries(path: str, searchPattern: str, searchOption: System.IO.SearchOption) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def GetFileSystemEntries(path: str, searchPattern: str, enumerationOptions: System.IO.EnumerationOptions) -> typing.List[str]:
        ...

    @staticmethod
    def GetLastAccessTime(path: str) -> datetime.datetime:
        ...

    @staticmethod
    def GetLastAccessTimeUtc(path: str) -> datetime.datetime:
        ...

    @staticmethod
    def GetLastWriteTime(path: str) -> datetime.datetime:
        ...

    @staticmethod
    def GetLastWriteTimeUtc(path: str) -> datetime.datetime:
        ...

    @staticmethod
    def GetLogicalDrives() -> typing.List[str]:
        ...

    @staticmethod
    def GetParent(path: str) -> System.IO.DirectoryInfo:
        ...

    @staticmethod
    def Move(sourceDirName: str, destDirName: str) -> None:
        ...

    @staticmethod
    def ResolveLinkTarget(linkPath: str, returnFinalTarget: bool) -> System.IO.FileSystemInfo:
        """
        Gets the target of the specified directory link.
        
        :param linkPath: The path of the directory link.
        :param returnFinalTarget: true to follow links to the final target; false to return the immediate next link.
        :returns: A DirectoryInfo instance if  exists, independently if the target exists or not. null if  is not a link.
        """
        ...

    @staticmethod
    def SetCreationTime(path: str, creationTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    def SetCreationTimeUtc(path: str, creationTimeUtc: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    def SetCurrentDirectory(path: str) -> None:
        ...

    @staticmethod
    def SetLastAccessTime(path: str, lastAccessTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    def SetLastAccessTimeUtc(path: str, lastAccessTimeUtc: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    def SetLastWriteTime(path: str, lastWriteTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    def SetLastWriteTimeUtc(path: str, lastWriteTimeUtc: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...


class HandleInheritability(System.Enum):
    """Specifies whether the underlying handle is inheritable by child processes."""

    # Cannot convert to Python: None = 0
    """Specifies that the handle is not inheritable by child processes."""

    Inheritable = 1
    """Specifies that the handle is inheritable by child processes."""


class MatchCasing(System.Enum):
    """Specifies the type of character casing to match."""

    PlatformDefault = 0
    """Matches using the default casing for the given platform."""

    CaseSensitive = 1
    """Matches respecting character casing."""

    CaseInsensitive = 2
    """Matches ignoring character casing."""


class StringReader(System.IO.TextReader):
    """This class has no documentation."""

    def __init__(self, s: str) -> None:
        ...

    def Close(self) -> None:
        ...

    def Dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def Peek(self) -> int:
        ...

    @overload
    def Read(self) -> int:
        ...

    @overload
    def Read(self, buffer: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def Read(self, buffer: System.Span[str]) -> int:
        ...

    @overload
    def ReadAsync(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def ReadAsync(self, buffer: System.Memory[str], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def ReadBlock(self, buffer: System.Span[str]) -> int:
        ...

    @overload
    def ReadBlockAsync(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def ReadBlockAsync(self, buffer: System.Memory[str], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def ReadLine(self) -> str:
        ...

    @overload
    def ReadLineAsync(self) -> System.Threading.Tasks.Task[str]:
        ...

    @overload
    def ReadLineAsync(self, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.ValueTask[str]:
        """
        Reads a line of characters asynchronously from the current string and returns the data as a string.
        
        :param cancellationToken: The token to monitor for cancellation requests.
        :returns: A value task that represents the asynchronous read operation. The value of the TResult parameter contains the next line from the string reader, or is null if all of the characters have been read.
        """
        ...

    def ReadToEnd(self) -> str:
        ...

    @overload
    def ReadToEndAsync(self) -> System.Threading.Tasks.Task[str]:
        ...

    @overload
    def ReadToEndAsync(self, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[str]:
        """
        Reads all characters from the current position to the end of the string asynchronously and returns them as a single string.
        
        :param cancellationToken: The token to monitor for cancellation requests.
        :returns: A task that represents the asynchronous read operation. The value of the TResult parameter contains a string with the characters from the current position to the end of the string.
        """
        ...


class UnmanagedMemoryStream(System.IO.Stream):
    """This class has no documentation."""

    @property
    def CanRead(self) -> bool:
        """Returns true if the stream can be read; otherwise returns false."""
        ...

    @property
    def CanSeek(self) -> bool:
        """Returns true if the stream can seek; otherwise returns false."""
        ...

    @property
    def CanWrite(self) -> bool:
        """Returns true if the stream can be written to; otherwise returns false."""
        ...

    @property
    def Length(self) -> int:
        """Number of bytes in the stream."""
        ...

    @property
    def Capacity(self) -> int:
        """Number of bytes that can be written to the stream."""
        ...

    @property
    def Position(self) -> int:
        """ReadByte will read byte at the Position in the stream"""
        ...

    @Position.setter
    def Position(self, value: int):
        """ReadByte will read byte at the Position in the stream"""
        ...

    @property
    def PositionPointer(self) -> typing.Any:
        """Pointer to memory at the current Position in the stream."""
        ...

    @PositionPointer.setter
    def PositionPointer(self, value: typing.Any):
        """Pointer to memory at the current Position in the stream."""
        ...

    @overload
    def __init__(self) -> None:
        """
        Creates a closed stream.
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, buffer: System.Runtime.InteropServices.SafeBuffer, offset: int, length: int) -> None:
        """Creates a stream over a SafeBuffer."""
        ...

    @overload
    def __init__(self, buffer: System.Runtime.InteropServices.SafeBuffer, offset: int, length: int, access: System.IO.FileAccess) -> None:
        """Creates a stream over a SafeBuffer."""
        ...

    @overload
    def __init__(self, pointer: typing.Any, length: int) -> None:
        """Creates a stream over a byte*."""
        ...

    @overload
    def __init__(self, pointer: typing.Any, length: int, capacity: int, access: System.IO.FileAccess) -> None:
        """Creates a stream over a byte*."""
        ...

    def Dispose(self, disposing: bool) -> None:
        """
        Closes the stream. The stream's memory needs to be dealt with separately.
        
        This method is protected.
        """
        ...

    def Flush(self) -> None:
        """Since it's a memory stream, this method does nothing."""
        ...

    def FlushAsync(self, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """Since it's a memory stream, this method does nothing specific."""
        ...

    @overload
    def Initialize(self, buffer: System.Runtime.InteropServices.SafeBuffer, offset: int, length: int, access: System.IO.FileAccess) -> None:
        """
        Subclasses must call this method (or the other overload) to properly initialize all instance fields.
        
        This method is protected.
        """
        ...

    @overload
    def Initialize(self, pointer: typing.Any, length: int, capacity: int, access: System.IO.FileAccess) -> None:
        """
        Subclasses must call this method (or the other overload) to properly initialize all instance fields.
        
        This method is protected.
        """
        ...

    @overload
    def Read(self, buffer: typing.List[int], offset: int, count: int) -> int:
        """
        Reads bytes from stream and puts them into the buffer
        
        :param buffer: Buffer to read the bytes to.
        :param offset: Starting index in the buffer.
        :param count: Maximum number of bytes to read.
        :returns: Number of bytes actually read.
        """
        ...

    @overload
    def Read(self, buffer: System.Span[int]) -> int:
        ...

    @overload
    def ReadAsync(self, buffer: typing.List[int], offset: int, count: int, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[int]:
        """
        Reads bytes from stream and puts them into the buffer
        
        :param buffer: Buffer to read the bytes to.
        :param offset: Starting index in the buffer.
        :param count: Maximum number of bytes to read.
        :param cancellationToken: Token that can be used to cancel this operation.
        :returns: Task that can be used to access the number of bytes actually read.
        """
        ...

    @overload
    def ReadAsync(self, buffer: System.Memory[int], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        """
        Reads bytes from stream and puts them into the buffer
        
        :param buffer: Buffer to read the bytes to.
        :param cancellationToken: Token that can be used to cancel this operation.
        """
        ...

    def ReadByte(self) -> int:
        """Returns the byte at the stream current Position and advances the Position."""
        ...

    def Seek(self, offset: int, loc: System.IO.SeekOrigin) -> int:
        """
        Advanced the Position to specific location in the stream.
        
        :param offset: Offset from the loc parameter.
        :param loc: Origin for the offset parameter.
        """
        ...

    def SetLength(self, value: int) -> None:
        """Sets the Length of the stream."""
        ...

    @overload
    def Write(self, buffer: typing.List[int], offset: int, count: int) -> None:
        """
        Writes buffer into the stream
        
        :param buffer: Buffer that will be written.
        :param offset: Starting index in the buffer.
        :param count: Number of bytes to write.
        """
        ...

    @overload
    def Write(self, buffer: System.ReadOnlySpan[int]) -> None:
        ...

    @overload
    def WriteAsync(self, buffer: typing.List[int], offset: int, count: int, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Writes buffer into the stream. The operation completes synchronously.
        
        :param buffer: Buffer that will be written.
        :param offset: Starting index in the buffer.
        :param count: Number of bytes to write.
        :param cancellationToken: Token that can be used to cancel the operation.
        :returns: Task that can be awaited.
        """
        ...

    @overload
    def WriteAsync(self, buffer: System.ReadOnlyMemory[int], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        """
        Writes buffer into the stream. The operation completes synchronously.
        
        :param buffer: Buffer that will be written.
        :param cancellationToken: Token that can be used to cancel the operation.
        """
        ...

    def WriteByte(self, value: int) -> None:
        """Writes a byte to the stream and advances the current Position."""
        ...


class BinaryReader(System.Object, System.IDisposable):
    """This class has no documentation."""

    @property
    def BaseStream(self) -> System.IO.Stream:
        ...

    @overload
    def __init__(self, input: System.IO.Stream) -> None:
        ...

    @overload
    def __init__(self, input: System.IO.Stream, encoding: System.Text.Encoding) -> None:
        ...

    @overload
    def __init__(self, input: System.IO.Stream, encoding: System.Text.Encoding, leaveOpen: bool) -> None:
        ...

    def Close(self) -> None:
        ...

    @overload
    def Dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    @overload
    def Dispose(self) -> None:
        ...

    def FillBuffer(self, numBytes: int) -> None:
        """This method is protected."""
        ...

    def PeekChar(self) -> int:
        ...

    @overload
    def Read(self) -> int:
        ...

    @overload
    def Read(self, buffer: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def Read(self, buffer: System.Span[str]) -> int:
        ...

    @overload
    def Read(self, buffer: typing.List[int], index: int, count: int) -> int:
        ...

    @overload
    def Read(self, buffer: System.Span[int]) -> int:
        ...

    def Read7BitEncodedInt(self) -> int:
        ...

    def Read7BitEncodedInt64(self) -> int:
        ...

    def ReadBoolean(self) -> bool:
        ...

    def ReadByte(self) -> int:
        ...

    def ReadBytes(self, count: int) -> typing.List[int]:
        ...

    def ReadChar(self) -> str:
        ...

    def ReadChars(self, count: int) -> typing.List[str]:
        ...

    def ReadDecimal(self) -> float:
        ...

    def ReadDouble(self) -> float:
        ...

    def ReadHalf(self) -> System.Half:
        ...

    def ReadInt16(self) -> int:
        ...

    def ReadInt32(self) -> int:
        ...

    def ReadInt64(self) -> int:
        ...

    def ReadSByte(self) -> int:
        ...

    def ReadSingle(self) -> float:
        ...

    def ReadString(self) -> str:
        ...

    def ReadUInt16(self) -> int:
        ...

    def ReadUInt32(self) -> int:
        ...

    def ReadUInt64(self) -> int:
        ...


class Path(System.Object):
    """This class has no documentation."""

    DirectorySeparatorChar: str = ...

    AltDirectorySeparatorChar: str = ...

    VolumeSeparatorChar: str = ...

    PathSeparator: str = ...

    InvalidPathChars: typing.List[str] = ...
    """Path.InvalidPathChars has been deprecated. Use GetInvalidPathChars or GetInvalidFileNameChars instead."""

    @staticmethod
    def ChangeExtension(path: str, extension: str) -> str:
        ...

    @staticmethod
    @overload
    def Combine(path1: str, path2: str) -> str:
        ...

    @staticmethod
    @overload
    def Combine(path1: str, path2: str, path3: str) -> str:
        ...

    @staticmethod
    @overload
    def Combine(path1: str, path2: str, path3: str, path4: str) -> str:
        ...

    @staticmethod
    @overload
    def Combine(*paths: str) -> str:
        ...

    @staticmethod
    @overload
    def EndsInDirectorySeparator(path: System.ReadOnlySpan[str]) -> bool:
        """Returns true if the path ends in a directory separator."""
        ...

    @staticmethod
    @overload
    def EndsInDirectorySeparator(path: str) -> bool:
        """Returns true if the path ends in a directory separator."""
        ...

    @staticmethod
    def Exists(path: str) -> bool:
        """
        Determines whether the specified file or directory exists.
        
        :param path: The path to check
        :returns: true if the caller has the required permissions and  contains the name of an existing file or directory; otherwise, false. This method also returns false if  is null, an invalid path, or a zero-length string. If the caller does not have sufficient permissions to read the specified path, no exception is thrown and the method returns false regardless of the existence of .
        """
        ...

    @staticmethod
    @overload
    def GetDirectoryName(path: str) -> str:
        """
        Returns the directory portion of a file path. This method effectively
        removes the last segment of the given file path, i.e. it returns a
        string consisting of all characters up to but not including the last
        backslash ("\\") in the file path. The returned value is null if the
        specified path is null, empty, or a root (such as "\\", "C:", or
        "\\\\server\\share").
        """
        ...

    @staticmethod
    @overload
    def GetDirectoryName(path: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        """
        Returns the directory portion of a file path. The returned value is empty
        if the specified path is null, empty, or a root (such as "\\", "C:", or
        "\\\\server\\share").
        """
        ...

    @staticmethod
    @overload
    def GetExtension(path: str) -> str:
        """
        Returns the extension of the given path. The returned value includes the period (".") character of the
        extension except when you have a terminal period when you get string.Empty, such as ".exe" or ".cpp".
        The returned value is null if the given path is null or empty if the given path does not include an
        extension.
        """
        ...

    @staticmethod
    @overload
    def GetExtension(path: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        """Returns the extension of the given path."""
        ...

    @staticmethod
    @overload
    def GetFileName(path: str) -> str:
        """
        Returns the name and extension parts of the given path. The resulting string contains
        the characters of path that follow the last separator in path. The resulting string is
        null if path is null.
        """
        ...

    @staticmethod
    @overload
    def GetFileName(path: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        """The returned ReadOnlySpan contains the characters of the path that follows the last separator in path."""
        ...

    @staticmethod
    @overload
    def GetFileNameWithoutExtension(path: str) -> str:
        ...

    @staticmethod
    @overload
    def GetFileNameWithoutExtension(path: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        """Returns the characters between the last separator and last (.) in the path."""
        ...

    @staticmethod
    @overload
    def GetFullPath(path: str) -> str:
        ...

    @staticmethod
    @overload
    def GetFullPath(path: str, basePath: str) -> str:
        ...

    @staticmethod
    @overload
    def GetFullPath(path: str) -> str:
        ...

    @staticmethod
    @overload
    def GetFullPath(path: str, basePath: str) -> str:
        ...

    @staticmethod
    @overload
    def GetInvalidFileNameChars() -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def GetInvalidFileNameChars() -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def GetInvalidPathChars() -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def GetInvalidPathChars() -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def GetPathRoot(path: str) -> str:
        ...

    @staticmethod
    @overload
    def GetPathRoot(path: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    @overload
    def GetPathRoot(path: str) -> str:
        """Returns the path root or null if path is empty or null."""
        ...

    @staticmethod
    @overload
    def GetPathRoot(path: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    def GetRandomFileName() -> str:
        """
        Returns a cryptographically strong random 8.3 string that can be
        used as either a folder name or a file name.
        """
        ...

    @staticmethod
    def GetRelativePath(relativeTo: str, path: str) -> str:
        """
        Create a relative path from one path to another. Paths will be resolved before calculating the difference.
        Default path comparison for the active platform will be used (OrdinalIgnoreCase for Windows or Mac, Ordinal for Unix).
        
        :param relativeTo: The source path the output should be relative to. This path is always considered to be a directory.
        :param path: The destination path.
        :returns: The relative path or  if the paths don't share the same root.
        """
        ...

    @staticmethod
    @overload
    def GetTempFileName() -> str:
        ...

    @staticmethod
    @overload
    def GetTempFileName() -> str:
        ...

    @staticmethod
    @overload
    def GetTempPath() -> str:
        ...

    @staticmethod
    @overload
    def GetTempPath() -> str:
        ...

    @staticmethod
    @overload
    def HasExtension(path: str) -> bool:
        """
        Tests if a path's file name includes a file extension. A trailing period
        is not considered an extension.
        """
        ...

    @staticmethod
    @overload
    def HasExtension(path: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    @overload
    def IsPathFullyQualified(path: str) -> bool:
        """
        Returns true if the path is fixed to a specific drive or UNC path. This method does no
        validation of the path (URIs will be returned as relative as a result).
        Returns false if the path specified is relative to the current drive or working directory.
        """
        ...

    @staticmethod
    @overload
    def IsPathFullyQualified(path: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    @overload
    def IsPathRooted(path: str) -> bool:
        ...

    @staticmethod
    @overload
    def IsPathRooted(path: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    @overload
    def IsPathRooted(path: str) -> bool:
        ...

    @staticmethod
    @overload
    def IsPathRooted(path: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    @overload
    def Join(path1: System.ReadOnlySpan[str], path2: System.ReadOnlySpan[str]) -> str:
        ...

    @staticmethod
    @overload
    def Join(path1: System.ReadOnlySpan[str], path2: System.ReadOnlySpan[str], path3: System.ReadOnlySpan[str]) -> str:
        ...

    @staticmethod
    @overload
    def Join(path1: System.ReadOnlySpan[str], path2: System.ReadOnlySpan[str], path3: System.ReadOnlySpan[str], path4: System.ReadOnlySpan[str]) -> str:
        ...

    @staticmethod
    @overload
    def Join(path1: str, path2: str) -> str:
        ...

    @staticmethod
    @overload
    def Join(path1: str, path2: str, path3: str) -> str:
        ...

    @staticmethod
    @overload
    def Join(path1: str, path2: str, path3: str, path4: str) -> str:
        ...

    @staticmethod
    @overload
    def Join(*paths: str) -> str:
        ...

    @staticmethod
    @overload
    def TrimEndingDirectorySeparator(path: str) -> str:
        """Trims one trailing directory separator beyond the root of the path."""
        ...

    @staticmethod
    @overload
    def TrimEndingDirectorySeparator(path: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        """Trims one trailing directory separator beyond the root of the path."""
        ...

    @staticmethod
    @overload
    def TryJoin(path1: System.ReadOnlySpan[str], path2: System.ReadOnlySpan[str], destination: System.Span[str], charsWritten: typing.Optional[int]) -> typing.Union[bool, int]:
        ...

    @staticmethod
    @overload
    def TryJoin(path1: System.ReadOnlySpan[str], path2: System.ReadOnlySpan[str], path3: System.ReadOnlySpan[str], destination: System.Span[str], charsWritten: typing.Optional[int]) -> typing.Union[bool, int]:
        ...


class EndOfStreamException(System.IO.IOException):
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


class FileNotFoundException(System.IO.IOException):
    """This class has no documentation."""

    @property
    def Message(self) -> str:
        ...

    @property
    def FileName(self) -> str:
        ...

    @property
    def FusionLog(self) -> str:
        ...

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
    def __init__(self, message: str, fileName: str) -> None:
        ...

    @overload
    def __init__(self, message: str, fileName: str, innerException: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def ToString(self) -> str:
        ...


class UnmanagedMemoryAccessor(System.Object, System.IDisposable):
    """This class has no documentation."""

    @property
    def Capacity(self) -> int:
        ...

    @property
    def CanRead(self) -> bool:
        ...

    @property
    def CanWrite(self) -> bool:
        ...

    @property
    def IsOpen(self) -> bool:
        """This property is protected."""
        ...

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, buffer: System.Runtime.InteropServices.SafeBuffer, offset: int, capacity: int) -> None:
        ...

    @overload
    def __init__(self, buffer: System.Runtime.InteropServices.SafeBuffer, offset: int, capacity: int, access: System.IO.FileAccess) -> None:
        ...

    @overload
    def Dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    @overload
    def Dispose(self) -> None:
        ...

    def Initialize(self, buffer: System.Runtime.InteropServices.SafeBuffer, offset: int, capacity: int, access: System.IO.FileAccess) -> None:
        """This method is protected."""
        ...

    def Read(self, position: int, structure: typing.Optional[System_IO_UnmanagedMemoryAccessor_Read_T]) -> typing.Union[None, System_IO_UnmanagedMemoryAccessor_Read_T]:
        ...

    def ReadArray(self, position: int, array: typing.List[System_IO_UnmanagedMemoryAccessor_ReadArray_T], offset: int, count: int) -> int:
        ...

    def ReadBoolean(self, position: int) -> bool:
        ...

    def ReadByte(self, position: int) -> int:
        ...

    def ReadChar(self, position: int) -> str:
        ...

    def ReadDecimal(self, position: int) -> float:
        ...

    def ReadDouble(self, position: int) -> float:
        ...

    def ReadInt16(self, position: int) -> int:
        ...

    def ReadInt32(self, position: int) -> int:
        ...

    def ReadInt64(self, position: int) -> int:
        ...

    def ReadSByte(self, position: int) -> int:
        ...

    def ReadSingle(self, position: int) -> float:
        ...

    def ReadUInt16(self, position: int) -> int:
        ...

    def ReadUInt32(self, position: int) -> int:
        ...

    def ReadUInt64(self, position: int) -> int:
        ...

    @overload
    def Write(self, position: int, value: bool) -> None:
        ...

    @overload
    def Write(self, position: int, value: int) -> None:
        ...

    @overload
    def Write(self, position: int, value: str) -> None:
        ...

    @overload
    def Write(self, position: int, value: int) -> None:
        ...

    @overload
    def Write(self, position: int, value: int) -> None:
        ...

    @overload
    def Write(self, position: int, value: int) -> None:
        ...

    @overload
    def Write(self, position: int, value: float) -> None:
        ...

    @overload
    def Write(self, position: int, value: float) -> None:
        ...

    @overload
    def Write(self, position: int, value: float) -> None:
        ...

    @overload
    def Write(self, position: int, value: int) -> None:
        ...

    @overload
    def Write(self, position: int, value: int) -> None:
        ...

    @overload
    def Write(self, position: int, value: int) -> None:
        ...

    @overload
    def Write(self, position: int, value: int) -> None:
        ...

    @overload
    def Write(self, position: int, structure: System_IO_UnmanagedMemoryAccessor_Write_T) -> None:
        ...

    def WriteArray(self, position: int, array: typing.List[System_IO_UnmanagedMemoryAccessor_WriteArray_T], offset: int, count: int) -> None:
        ...


class DirectoryNotFoundException(System.IO.IOException):
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


class PathTooLongException(System.IO.IOException):
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


class StringWriter(System.IO.TextWriter):
    """This class has no documentation."""

    @property
    def Encoding(self) -> System.Text.Encoding:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, formatProvider: System.IFormatProvider) -> None:
        ...

    @overload
    def __init__(self, sb: System.Text.StringBuilder) -> None:
        ...

    @overload
    def __init__(self, sb: System.Text.StringBuilder, formatProvider: System.IFormatProvider) -> None:
        ...

    def Close(self) -> None:
        ...

    def Dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def FlushAsync(self) -> System.Threading.Tasks.Task:
        ...

    def GetStringBuilder(self) -> System.Text.StringBuilder:
        ...

    def ToString(self) -> str:
        ...

    @overload
    def Write(self, value: str) -> None:
        ...

    @overload
    def Write(self, buffer: typing.List[str], index: int, count: int) -> None:
        ...

    @overload
    def Write(self, buffer: System.ReadOnlySpan[str]) -> None:
        ...

    @overload
    def Write(self, value: str) -> None:
        ...

    @overload
    def Write(self, value: System.Text.StringBuilder) -> None:
        ...

    @overload
    def WriteAsync(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteAsync(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteAsync(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteAsync(self, buffer: System.ReadOnlyMemory[str], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteAsync(self, value: System.Text.StringBuilder, cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteLine(self, buffer: System.ReadOnlySpan[str]) -> None:
        ...

    @overload
    def WriteLine(self, value: System.Text.StringBuilder) -> None:
        ...

    @overload
    def WriteLineAsync(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteLineAsync(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteLineAsync(self, value: System.Text.StringBuilder, cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteLineAsync(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteLineAsync(self, buffer: System.ReadOnlyMemory[str], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...


class InvalidDataException(System.SystemException):
    """The exception that is thrown when a data stream is in an invalid format."""

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the System.IO.InvalidDataException class."""
        ...

    @overload
    def __init__(self, message: str) -> None:
        """
        Initializes a new instance of the System.IO.InvalidDataException class with a specified error message.
        
        :param message: The error message that explains the reason for the exception.
        """
        ...

    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None:
        """
        Initializes a new instance of the System.IO.InvalidDataException class with a reference to the inner exception that is the cause of this exception.
        
        :param message: The error message that explains the reason for the exception.
        :param innerException: The exception that is the cause of the current exception. If the  parameter is not null, the current exception is raised in a catch block that handles the inner exception.
        """
        ...


class BinaryWriter(System.Object, System.IDisposable, System.IAsyncDisposable):
    """This class has no documentation."""

    Null: System.IO.BinaryWriter = ...

    @property
    def OutStream(self) -> System.IO.Stream:
        """This field is protected."""
        ...

    @OutStream.setter
    def OutStream(self, value: System.IO.Stream):
        """This field is protected."""
        ...

    @property
    def BaseStream(self) -> System.IO.Stream:
        ...

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, output: System.IO.Stream) -> None:
        ...

    @overload
    def __init__(self, output: System.IO.Stream, encoding: System.Text.Encoding) -> None:
        ...

    @overload
    def __init__(self, output: System.IO.Stream, encoding: System.Text.Encoding, leaveOpen: bool) -> None:
        ...

    def Close(self) -> None:
        ...

    @overload
    def Dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    @overload
    def Dispose(self) -> None:
        ...

    def DisposeAsync(self) -> System.Threading.Tasks.ValueTask:
        ...

    def Flush(self) -> None:
        ...

    def Seek(self, offset: int, origin: System.IO.SeekOrigin) -> int:
        ...

    @overload
    def Write(self, value: bool) -> None:
        ...

    @overload
    def Write(self, value: int) -> None:
        ...

    @overload
    def Write(self, value: int) -> None:
        ...

    @overload
    def Write(self, buffer: typing.List[int]) -> None:
        ...

    @overload
    def Write(self, buffer: typing.List[int], index: int, count: int) -> None:
        ...

    @overload
    def Write(self, ch: str) -> None:
        ...

    @overload
    def Write(self, chars: typing.List[str]) -> None:
        ...

    @overload
    def Write(self, chars: typing.List[str], index: int, count: int) -> None:
        ...

    @overload
    def Write(self, value: float) -> None:
        ...

    @overload
    def Write(self, value: float) -> None:
        ...

    @overload
    def Write(self, value: int) -> None:
        ...

    @overload
    def Write(self, value: int) -> None:
        ...

    @overload
    def Write(self, value: int) -> None:
        ...

    @overload
    def Write(self, value: int) -> None:
        ...

    @overload
    def Write(self, value: int) -> None:
        ...

    @overload
    def Write(self, value: int) -> None:
        ...

    @overload
    def Write(self, value: float) -> None:
        ...

    @overload
    def Write(self, value: System.Half) -> None:
        ...

    @overload
    def Write(self, value: str) -> None:
        ...

    @overload
    def Write(self, buffer: System.ReadOnlySpan[int]) -> None:
        ...

    @overload
    def Write(self, chars: System.ReadOnlySpan[str]) -> None:
        ...

    def Write7BitEncodedInt(self, value: int) -> None:
        ...

    def Write7BitEncodedInt64(self, value: int) -> None:
        ...


class MatchType(System.Enum):
    """Specifies the type of wildcard matching to use."""

    Simple = 0
    """Matches using '*' and '?' wildcards.* matches from zero to any amount of characters. ? matches exactly one character. *.* matches any name with a period in it (with , this would match all items)."""

    Win32 = 1
    """Match using Win32 DOS style matching semantics.'*', '?', '<', '>', and '"' are all considered wildcards. Matches in a traditional DOS / Windows command prompt way. *.* matches all files. ? matches collapse to periods. file.??t will match file.t, file.at, and file.txt."""


class BufferedStream(System.IO.Stream):
    """
    One of the design goals here is to prevent the buffer from getting in the way and slowing
    down underlying stream accesses when it is not needed. If you always read & write for sizes
    greater than the internal buffer size, then this class may not even allocate the internal buffer.
    See a large comment in Write for the details of the write buffer heuristic.
    
    This class buffers reads & writes in a shared buffer.
    (If you maintained two buffers separately, one operation would always trash the other buffer
    anyways, so we might as well use one buffer.)
    The assumption here is you will almost always be doing a series of reads or writes, but rarely
    alternate between the two of them on the same stream.
    
    Class Invariants:
    The class has one buffer, shared for reading & writing.
    It can only be used for one or the other at any point in time - not both.
    The following should be true:
    
      * 0 <= _readPos <= _readLen < _bufferSize
      * 0 <= _writePos < _bufferSize
      * _readPos == _readLen && _readPos > 0 implies the read buffer is valid, but we're at the end of the buffer.
      * _readPos == _readLen == 0 means the read buffer contains garbage.
      * Either _writePos can be greater than 0, or _readLen & _readPos can be greater than zero,
        but neither can be greater than zero at the same time.
     
    This class will never cache more bytes than the max specified buffer size.
    However, it may use a temporary buffer of up to twice the size in order to combine several IO operations on
    the underlying stream into a single operation. This is because we assume that memory copies are significantly
    faster than IO operations on the underlying stream (if this was not true, using buffering is never appropriate).
    The max size of this "shadow" buffer is limited as to not allocate it on the LOH.
    Shadowing is always transient. Even when using this technique, this class still guarantees that the number of
    bytes cached (not yet written to the target stream or not yet consumed by the user) is never larger than the
    actual specified buffer size.
    """

    @property
    def UnderlyingStream(self) -> System.IO.Stream:
        ...

    @property
    def BufferSize(self) -> int:
        ...

    @property
    def CanRead(self) -> bool:
        ...

    @property
    def CanWrite(self) -> bool:
        ...

    @property
    def CanSeek(self) -> bool:
        ...

    @property
    def Length(self) -> int:
        ...

    @property
    def Position(self) -> int:
        ...

    @Position.setter
    def Position(self, value: int):
        ...

    @overload
    def __init__(self, stream: System.IO.Stream) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, bufferSize: int) -> None:
        ...

    def BeginRead(self, buffer: typing.List[int], offset: int, count: int, callback: typing.Callable[[System.IAsyncResult], None], state: typing.Any) -> System.IAsyncResult:
        ...

    def BeginWrite(self, buffer: typing.List[int], offset: int, count: int, callback: typing.Callable[[System.IAsyncResult], None], state: typing.Any) -> System.IAsyncResult:
        ...

    def CopyTo(self, destination: System.IO.Stream, bufferSize: int) -> None:
        ...

    def CopyToAsync(self, destination: System.IO.Stream, bufferSize: int, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    def Dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def DisposeAsync(self) -> System.Threading.Tasks.ValueTask:
        ...

    def EndRead(self, asyncResult: System.IAsyncResult) -> int:
        ...

    def EndWrite(self, asyncResult: System.IAsyncResult) -> None:
        ...

    def Flush(self) -> None:
        ...

    def FlushAsync(self, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def Read(self, buffer: typing.List[int], offset: int, count: int) -> int:
        ...

    @overload
    def Read(self, destination: System.Span[int]) -> int:
        ...

    @overload
    def ReadAsync(self, buffer: typing.List[int], offset: int, count: int, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def ReadAsync(self, buffer: System.Memory[int], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def ReadByte(self) -> int:
        ...

    def Seek(self, offset: int, origin: System.IO.SeekOrigin) -> int:
        ...

    def SetLength(self, value: int) -> None:
        ...

    @overload
    def Write(self, buffer: typing.List[int], offset: int, count: int) -> None:
        ...

    @overload
    def Write(self, buffer: System.ReadOnlySpan[int]) -> None:
        ...

    @overload
    def WriteAsync(self, buffer: typing.List[int], offset: int, count: int, cancellationToken: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def WriteAsync(self, buffer: System.ReadOnlyMemory[int], cancellationToken: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        ...

    def WriteByte(self, value: int) -> None:
        ...


