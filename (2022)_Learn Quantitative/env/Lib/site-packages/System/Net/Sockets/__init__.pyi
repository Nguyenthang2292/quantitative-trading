from typing import overload
import typing

import System
import System.ComponentModel
import System.Net.Sockets
import System.Runtime.Serialization


class SocketException(System.ComponentModel.Win32Exception):
    """Provides socket exceptions to the application."""

    @property
    def Message(self) -> str:
        ...

    @property
    def SocketErrorCode(self) -> int:
        """This property contains the int value of a member of the System.Net.Sockets.SocketError enum."""
        ...

    @property
    def ErrorCode(self) -> int:
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new instance of the System.Net.Sockets.SocketException class with the default error code."""
        ...

    @overload
    def __init__(self, errorCode: int) -> None:
        """Creates a new instance of the System.Net.Sockets.SocketException class with the specified error code."""
        ...

    @overload
    def __init__(self, errorCode: int, message: str) -> None:
        """Initializes a new instance of the System.Net.Sockets.SocketException class with the specified error code and optional message."""
        ...

    @overload
    def __init__(self, serializationInfo: System.Runtime.Serialization.SerializationInfo, streamingContext: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new instance of the System.Net.Sockets.SocketException class with the default error code."""
        ...


class AddressFamily(System.Enum):
    """Specifies the addressing scheme that an instance of the Socket class can use."""

    Unknown = -1

    Unspecified = 0

    Unix = 1

    InterNetwork = 2

    ImpLink = 3

    Pup = 4

    Chaos = 5

    NS = 6

    Ipx = ...

    Iso = 7

    Osi = ...

    Ecma = 8

    DataKit = 9

    Ccitt = 10

    Sna = 11

    DecNet = 12

    DataLink = 13

    Lat = 14

    HyperChannel = 15

    AppleTalk = 16

    NetBios = 17

    VoiceView = 18

    FireFox = 19

    Banyan = 21

    Atm = 22

    InterNetworkV6 = 23

    Cluster = 24

    Ieee12844 = 25

    Irda = 26

    NetworkDesigners = 28

    Max = 29

    Packet = 65536

    ControllerAreaNetwork = 65537


class SocketError(System.Enum):
    """This class has no documentation."""

    Success = 0

    SocketError = ...

    Interrupted = ...

    AccessDenied = ...

    Fault = ...

    InvalidArgument = ...

    TooManyOpenSockets = ...

    WouldBlock = ...

    InProgress = ...

    AlreadyInProgress = ...

    NotSocket = ...

    DestinationAddressRequired = ...

    MessageSize = ...

    ProtocolType = ...

    ProtocolOption = ...

    ProtocolNotSupported = ...

    SocketNotSupported = ...

    OperationNotSupported = ...

    ProtocolFamilyNotSupported = ...

    AddressFamilyNotSupported = ...

    AddressAlreadyInUse = ...

    AddressNotAvailable = ...

    NetworkDown = ...

    NetworkUnreachable = ...

    NetworkReset = ...

    ConnectionAborted = ...

    ConnectionReset = ...

    NoBufferSpaceAvailable = ...

    IsConnected = ...

    NotConnected = ...

    Shutdown = ...

    TimedOut = ...

    ConnectionRefused = ...

    HostDown = ...

    HostUnreachable = ...

    ProcessLimit = ...

    SystemNotReady = ...

    VersionNotSupported = ...

    NotInitialized = ...

    Disconnecting = ...

    TypeNotFound = ...

    HostNotFound = ...

    TryAgain = ...

    NoRecovery = ...

    NoData = ...

    IOPending = ...

    OperationAborted = ...


