from typing import overload
import abc
import datetime
import typing
import warnings

import System
import System.Collections
import System.Collections.Generic
import System.IO
import System.Net
import System.Net.Sockets
import System.Runtime.Serialization
import System.Security
import System.Security.Authentication.ExtendedProtection


class WebUtility(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def HtmlDecode(value: str) -> str:
        ...

    @staticmethod
    @overload
    def HtmlDecode(value: str, output: System.IO.TextWriter) -> None:
        ...

    @staticmethod
    @overload
    def HtmlEncode(value: str) -> str:
        ...

    @staticmethod
    @overload
    def HtmlEncode(value: str, output: System.IO.TextWriter) -> None:
        ...

    @staticmethod
    def UrlDecode(encodedValue: str) -> str:
        ...

    @staticmethod
    def UrlDecodeToBytes(encodedValue: typing.List[int], offset: int, count: int) -> typing.List[int]:
        ...

    @staticmethod
    def UrlEncode(value: str) -> str:
        ...

    @staticmethod
    def UrlEncodeToBytes(value: typing.List[int], offset: int, count: int) -> typing.List[int]:
        ...


class ICredentials(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def GetCredential(self, uri: System.Uri, authType: str) -> System.Net.NetworkCredential:
        ...


class ICredentialsByHost(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def GetCredential(self, host: str, port: int, authenticationType: str) -> System.Net.NetworkCredential:
        ...


class NetworkCredential(System.Object, System.Net.ICredentials, System.Net.ICredentialsByHost):
    """This class has no documentation."""

    @property
    def UserName(self) -> str:
        ...

    @UserName.setter
    def UserName(self, value: str):
        ...

    @property
    def Password(self) -> str:
        ...

    @Password.setter
    def Password(self, value: str):
        ...

    @property
    def SecurePassword(self) -> System.Security.SecureString:
        ...

    @SecurePassword.setter
    def SecurePassword(self, value: System.Security.SecureString):
        ...

    @property
    def Domain(self) -> str:
        ...

    @Domain.setter
    def Domain(self, value: str):
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, userName: str, password: str) -> None:
        ...

    @overload
    def __init__(self, userName: str, password: str, domain: str) -> None:
        ...

    @overload
    def __init__(self, userName: str, password: System.Security.SecureString) -> None:
        ...

    @overload
    def __init__(self, userName: str, password: System.Security.SecureString, domain: str) -> None:
        ...

    @overload
    def GetCredential(self, uri: System.Uri, authenticationType: str) -> System.Net.NetworkCredential:
        ...

    @overload
    def GetCredential(self, host: str, port: int, authenticationType: str) -> System.Net.NetworkCredential:
        ...


class Cookie(System.Object):
    """This class has no documentation."""

    MaxSupportedVersion: int = 1

    MaxSupportedVersionString: str = "1"

    SeparatorLiteral: str = "; "

    EqualsLiteral: str = ...

    QuotesLiteral: str = ...

    SpecialAttributeLiteral: str = "$"

    PortSplitDelimiters: typing.List[str] = ...

    ReservedToName: str = "\\t\\r\\n=;,"

    @property
    def IsQuotedVersion(self) -> bool:
        ...

    @IsQuotedVersion.setter
    def IsQuotedVersion(self, value: bool):
        ...

    @property
    def IsQuotedDomain(self) -> bool:
        ...

    @IsQuotedDomain.setter
    def IsQuotedDomain(self, value: bool):
        ...

    @property
    def Comment(self) -> str:
        ...

    @Comment.setter
    def Comment(self, value: str):
        ...

    @property
    def CommentUri(self) -> System.Uri:
        ...

    @CommentUri.setter
    def CommentUri(self, value: System.Uri):
        ...

    @property
    def HttpOnly(self) -> bool:
        ...

    @HttpOnly.setter
    def HttpOnly(self, value: bool):
        ...

    @property
    def Discard(self) -> bool:
        ...

    @Discard.setter
    def Discard(self, value: bool):
        ...

    @property
    def Domain(self) -> str:
        ...

    @Domain.setter
    def Domain(self, value: str):
        ...

    @property
    def DomainImplicit(self) -> bool:
        ...

    @DomainImplicit.setter
    def DomainImplicit(self, value: bool):
        ...

    @property
    def Expired(self) -> bool:
        ...

    @Expired.setter
    def Expired(self, value: bool):
        ...

    @property
    def Expires(self) -> datetime.datetime:
        ...

    @Expires.setter
    def Expires(self, value: datetime.datetime):
        ...

    @property
    def Name(self) -> str:
        ...

    @Name.setter
    def Name(self, value: str):
        ...

    @property
    def Path(self) -> str:
        ...

    @Path.setter
    def Path(self, value: str):
        ...

    @property
    def Plain(self) -> bool:
        ...

    @property
    def Port(self) -> str:
        ...

    @Port.setter
    def Port(self, value: str):
        ...

    @property
    def PortList(self) -> typing.List[int]:
        ...

    @property
    def Secure(self) -> bool:
        ...

    @Secure.setter
    def Secure(self, value: bool):
        ...

    @property
    def TimeStamp(self) -> datetime.datetime:
        ...

    @property
    def Value(self) -> str:
        ...

    @Value.setter
    def Value(self, value: str):
        ...

    @property
    def Variant(self) -> int:
        """This property contains the int value of a member of the System.Net.CookieVariant enum."""
        ...

    @property
    def DomainKey(self) -> str:
        ...

    @property
    def Version(self) -> int:
        ...

    @Version.setter
    def Version(self, value: int):
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, name: str, value: str) -> None:
        ...

    @overload
    def __init__(self, name: str, value: str, path: str) -> None:
        ...

    @overload
    def __init__(self, name: str, value: str, path: str, domain: str) -> None:
        ...

    def Equals(self, comparand: typing.Any) -> bool:
        ...

    def GetHashCode(self) -> int:
        ...

    def ToString(self) -> str:
        ...


class CookieCollection(System.Object, System.Collections.Generic.ICollection[System.Net.Cookie], System.Collections.Generic.IReadOnlyCollection[System.Net.Cookie], System.Collections.ICollection, typing.Iterable[System.Net.Cookie]):
    """This class has no documentation."""

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def IsOtherVersionSeen(self) -> bool:
        ...

    @overload
    def __getitem__(self, index: int) -> System.Net.Cookie:
        ...

    @overload
    def __getitem__(self, name: str) -> System.Net.Cookie:
        ...

    def __init__(self) -> None:
        ...

    @overload
    def Add(self, cookie: System.Net.Cookie) -> None:
        ...

    @overload
    def Add(self, cookies: System.Net.CookieCollection) -> None:
        ...

    def Clear(self) -> None:
        ...

    def Contains(self, cookie: System.Net.Cookie) -> bool:
        ...

    @overload
    def CopyTo(self, array: System.Array, index: int) -> None:
        ...

    @overload
    def CopyTo(self, array: typing.List[System.Net.Cookie], index: int) -> None:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System.Net.Cookie]:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        ...

    def Remove(self, cookie: System.Net.Cookie) -> bool:
        ...


class CookieContainer(System.Object):
    """This class has no documentation."""

    DefaultCookieLimit: int = 300

    DefaultPerDomainCookieLimit: int = 20

    DefaultCookieLengthLimit: int = 4096

    @property
    def Capacity(self) -> int:
        ...

    @Capacity.setter
    def Capacity(self, value: int):
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def MaxCookieSize(self) -> int:
        ...

    @MaxCookieSize.setter
    def MaxCookieSize(self, value: int):
        ...

    @property
    def PerDomainCapacity(self) -> int:
        ...

    @PerDomainCapacity.setter
    def PerDomainCapacity(self, value: int):
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, capacity: int, perDomainCapacity: int, maxCookieSize: int) -> None:
        ...

    @overload
    def Add(self, cookie: System.Net.Cookie) -> None:
        ...

    @overload
    def Add(self, cookies: System.Net.CookieCollection) -> None:
        ...

    @overload
    def Add(self, uri: System.Uri, cookie: System.Net.Cookie) -> None:
        ...

    @overload
    def Add(self, uri: System.Uri, cookies: System.Net.CookieCollection) -> None:
        ...

    def GetAllCookies(self) -> System.Net.CookieCollection:
        """
        Gets a CookieCollection that contains all of the Cookie instances in the container.
        
        :returns: A CookieCollection that contains all of the Cookie instances in the container.
        """
        ...

    def GetCookieHeader(self, uri: System.Uri) -> str:
        ...

    def GetCookies(self, uri: System.Uri) -> System.Net.CookieCollection:
        ...

    def SetCookies(self, uri: System.Uri, cookieHeader: str) -> None:
        ...


class PathList(System.Object):
    """This class has no documentation."""

    @property
    def Count(self) -> int:
        ...

    @property
    def Values(self) -> System.Collections.ICollection:
        ...

    @property
    def List(self) -> System.Collections.SortedList:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...


class CredentialCache(System.Object, System.Net.ICredentials, System.Net.ICredentialsByHost, System.Collections.IEnumerable):
    """This class has no documentation."""

    DefaultCredentials: System.Net.ICredentials

    DefaultNetworkCredentials: System.Net.NetworkCredential

    def __init__(self) -> None:
        ...

    @overload
    def Add(self, uriPrefix: System.Uri, authType: str, cred: System.Net.NetworkCredential) -> None:
        ...

    @overload
    def Add(self, host: str, port: int, authenticationType: str, credential: System.Net.NetworkCredential) -> None:
        ...

    @overload
    def GetCredential(self, uriPrefix: System.Uri, authType: str) -> System.Net.NetworkCredential:
        ...

    @overload
    def GetCredential(self, host: str, port: int, authenticationType: str) -> System.Net.NetworkCredential:
        ...

    def GetEnumerator(self) -> System.Collections.IEnumerator:
        ...

    @overload
    def Remove(self, uriPrefix: System.Uri, authType: str) -> None:
        ...

    @overload
    def Remove(self, host: str, port: int, authenticationType: str) -> None:
        ...


class AuthenticationSchemes(System.Enum):
    """This class has no documentation."""

    # Cannot convert to Python: None = ...

    Digest = ...

    Negotiate = ...

    Ntlm = ...

    Basic = ...

    Anonymous = ...

    IntegratedWindowsAuthentication = ...


class HttpStatusCode(System.Enum):
    """This class has no documentation."""

    Continue = 100

    SwitchingProtocols = 101

    Processing = 102

    EarlyHints = 103

    OK = 200

    Created = 201

    Accepted = 202

    NonAuthoritativeInformation = 203

    NoContent = 204

    ResetContent = 205

    PartialContent = 206

    MultiStatus = 207

    AlreadyReported = 208

    IMUsed = 226

    MultipleChoices = 300

    Ambiguous = 300

    MovedPermanently = 301

    Moved = 301

    Found = 302

    Redirect = 302

    SeeOther = 303

    RedirectMethod = 303

    NotModified = 304

    UseProxy = 305

    Unused = 306

    TemporaryRedirect = 307

    RedirectKeepVerb = 307

    PermanentRedirect = 308

    BadRequest = 400

    Unauthorized = 401

    PaymentRequired = 402

    Forbidden = 403

    NotFound = 404

    MethodNotAllowed = 405

    NotAcceptable = 406

    ProxyAuthenticationRequired = 407

    RequestTimeout = 408

    Conflict = 409

    Gone = 410

    LengthRequired = 411

    PreconditionFailed = 412

    RequestEntityTooLarge = 413

    RequestUriTooLong = 414

    UnsupportedMediaType = 415

    RequestedRangeNotSatisfiable = 416

    ExpectationFailed = 417

    MisdirectedRequest = 421

    UnprocessableEntity = 422

    Locked = 423

    FailedDependency = 424

    UpgradeRequired = 426

    PreconditionRequired = 428

    TooManyRequests = 429

    RequestHeaderFieldsTooLarge = 431

    UnavailableForLegalReasons = 451

    InternalServerError = 500

    NotImplemented = 501

    BadGateway = 502

    ServiceUnavailable = 503

    GatewayTimeout = 504

    HttpVersionNotSupported = 505

    VariantAlsoNegotiates = 506

    InsufficientStorage = 507

    LoopDetected = 508

    NotExtended = 510

    NetworkAuthenticationRequired = 511


class EndPoint(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def AddressFamily(self) -> int:
        """This property contains the int value of a member of the System.Net.Sockets.AddressFamily enum."""
        ...

    def Create(self, socketAddress: System.Net.SocketAddress) -> System.Net.EndPoint:
        ...

    def Serialize(self) -> System.Net.SocketAddress:
        ...


class IPAddress(System.Object):
    """This class has no documentation."""

    Any: System.Net.IPAddress = ...

    Loopback: System.Net.IPAddress = ...

    Broadcast: System.Net.IPAddress = ...

    # Cannot convert to Python: None: System.Net.IPAddress = ...

    LoopbackMaskHostOrder: int = ...

    IPv6Any: System.Net.IPAddress = ...

    IPv6Loopback: System.Net.IPAddress = ...

    IPv6None: System.Net.IPAddress = ...

    NumberOfLabels: int = ...

    @property
    def AddressFamily(self) -> int:
        """This property contains the int value of a member of the System.Net.Sockets.AddressFamily enum."""
        ...

    @property
    def ScopeId(self) -> int:
        ...

    @ScopeId.setter
    def ScopeId(self, value: int):
        ...

    @property
    def IsIPv6Multicast(self) -> bool:
        ...

    @property
    def IsIPv6LinkLocal(self) -> bool:
        ...

    @property
    def IsIPv6SiteLocal(self) -> bool:
        ...

    @property
    def IsIPv6Teredo(self) -> bool:
        ...

    @property
    def IsIPv6UniqueLocal(self) -> bool:
        """Gets whether the address is an IPv6 Unique Local address."""
        ...

    @property
    def IsIPv4MappedToIPv6(self) -> bool:
        ...

    @property
    def Address(self) -> int:
        """IPAddress.Address is address family dependent and has been deprecated. Use IPAddress.Equals to perform comparisons instead."""
        warnings.warn("IPAddress.Address is address family dependent and has been deprecated. Use IPAddress.Equals to perform comparisons instead.", DeprecationWarning)

    @Address.setter
    def Address(self, value: int):
        """IPAddress.Address is address family dependent and has been deprecated. Use IPAddress.Equals to perform comparisons instead."""
        warnings.warn("IPAddress.Address is address family dependent and has been deprecated. Use IPAddress.Equals to perform comparisons instead.", DeprecationWarning)

    @overload
    def __init__(self, newAddress: int) -> None:
        ...

    @overload
    def __init__(self, address: typing.List[int], scopeid: int) -> None:
        ...

    @overload
    def __init__(self, address: System.ReadOnlySpan[int], scopeid: int) -> None:
        ...

    @overload
    def __init__(self, address: typing.List[int]) -> None:
        ...

    @overload
    def __init__(self, address: System.ReadOnlySpan[int]) -> None:
        ...

    def Equals(self, comparand: typing.Any) -> bool:
        """Compares two IP addresses."""
        ...

    def GetAddressBytes(self) -> typing.List[int]:
        ...

    def GetHashCode(self) -> int:
        ...

    @staticmethod
    @overload
    def HostToNetworkOrder(host: int) -> int:
        ...

    @staticmethod
    @overload
    def HostToNetworkOrder(host: int) -> int:
        ...

    @staticmethod
    @overload
    def HostToNetworkOrder(host: int) -> int:
        ...

    @staticmethod
    def IsLoopback(address: System.Net.IPAddress) -> bool:
        ...

    def MapToIPv4(self) -> System.Net.IPAddress:
        ...

    def MapToIPv6(self) -> System.Net.IPAddress:
        ...

    @staticmethod
    @overload
    def NetworkToHostOrder(network: int) -> int:
        ...

    @staticmethod
    @overload
    def NetworkToHostOrder(network: int) -> int:
        ...

    @staticmethod
    @overload
    def NetworkToHostOrder(network: int) -> int:
        ...

    @staticmethod
    @overload
    def Parse(ipString: str) -> System.Net.IPAddress:
        ...

    @staticmethod
    @overload
    def Parse(ipSpan: System.ReadOnlySpan[str]) -> System.Net.IPAddress:
        ...

    def ToString(self) -> str:
        ...

    def TryFormat(self, destination: System.Span[str], charsWritten: typing.Optional[int]) -> typing.Union[bool, int]:
        ...

    @staticmethod
    @overload
    def TryParse(ipString: str, address: typing.Optional[System.Net.IPAddress]) -> typing.Union[bool, System.Net.IPAddress]:
        ...

    @staticmethod
    @overload
    def TryParse(ipSpan: System.ReadOnlySpan[str], address: typing.Optional[System.Net.IPAddress]) -> typing.Union[bool, System.Net.IPAddress]:
        ...

    def TryWriteBytes(self, destination: System.Span[int], bytesWritten: typing.Optional[int]) -> typing.Union[bool, int]:
        ...


class IPEndPoint(System.Net.EndPoint):
    """Provides an IP address."""

    MinPort: int = ...
    """Specifies the minimum acceptable value for the System.Net.IPEndPoint.Port property."""

    MaxPort: int = ...
    """Specifies the maximum acceptable value for the System.Net.IPEndPoint.Port property."""

    @property
    def AddressFamily(self) -> int:
        """This property contains the int value of a member of the System.Net.Sockets.AddressFamily enum."""
        ...

    @property
    def Address(self) -> System.Net.IPAddress:
        """Gets or sets the IP address."""
        ...

    @Address.setter
    def Address(self, value: System.Net.IPAddress):
        """Gets or sets the IP address."""
        ...

    @property
    def Port(self) -> int:
        """Gets or sets the port."""
        ...

    @Port.setter
    def Port(self, value: int):
        """Gets or sets the port."""
        ...

    @overload
    def __init__(self, address: int, port: int) -> None:
        """Creates a new instance of the IPEndPoint class with the specified address and port."""
        ...

    @overload
    def __init__(self, address: System.Net.IPAddress, port: int) -> None:
        """Creates a new instance of the IPEndPoint class with the specified address and port."""
        ...

    def Create(self, socketAddress: System.Net.SocketAddress) -> System.Net.EndPoint:
        ...

    def Equals(self, comparand: typing.Any) -> bool:
        ...

    def GetHashCode(self) -> int:
        ...

    @staticmethod
    @overload
    def Parse(s: str) -> System.Net.IPEndPoint:
        ...

    @staticmethod
    @overload
    def Parse(s: System.ReadOnlySpan[str]) -> System.Net.IPEndPoint:
        ...

    def Serialize(self) -> System.Net.SocketAddress:
        ...

    def ToString(self) -> str:
        ...

    @staticmethod
    @overload
    def TryParse(s: str, result: typing.Optional[System.Net.IPEndPoint]) -> typing.Union[bool, System.Net.IPEndPoint]:
        ...

    @staticmethod
    @overload
    def TryParse(s: System.ReadOnlySpan[str], result: typing.Optional[System.Net.IPEndPoint]) -> typing.Union[bool, System.Net.IPEndPoint]:
        ...


class DecompressionMethods(System.Enum):
    """This class has no documentation."""

    # Cannot convert to Python: None = 0

    GZip = ...

    Deflate = ...

    Brotli = ...

    All = ...


class DnsEndPoint(System.Net.EndPoint):
    """This class has no documentation."""

    @property
    def Host(self) -> str:
        ...

    @property
    def AddressFamily(self) -> int:
        """This property contains the int value of a member of the System.Net.Sockets.AddressFamily enum."""
        ...

    @property
    def Port(self) -> int:
        ...

    @overload
    def __init__(self, host: str, port: int) -> None:
        ...

    @overload
    def __init__(self, host: str, port: int, addressFamily: System.Net.Sockets.AddressFamily) -> None:
        ...

    def Equals(self, comparand: typing.Any) -> bool:
        ...

    def GetHashCode(self) -> int:
        ...

    def ToString(self) -> str:
        ...


class IWebProxy(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def Credentials(self) -> System.Net.ICredentials:
        ...

    @Credentials.setter
    @abc.abstractmethod
    def Credentials(self, value: System.Net.ICredentials):
        ...

    def GetProxy(self, destination: System.Uri) -> System.Uri:
        ...

    def IsBypassed(self, host: System.Uri) -> bool:
        ...


class HttpVersion(System.Object):
    """This class has no documentation."""

    Unknown: System.Version = ...
    """Defines a Version instance that indicates an unknown version of HTTP."""

    Version10: System.Version = ...
    """Defines a Version instance for HTTP 1.0."""

    Version11: System.Version = ...
    """Defines a Version instance for HTTP 1.1."""

    Version20: System.Version = ...
    """Defines a Version instance for HTTP 2.0."""

    Version30: System.Version = ...
    """Defines a Version instance for HTTP 3.0."""


class CookieException(System.FormatException, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, serializationInfo: System.Runtime.Serialization.SerializationInfo, streamingContext: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...

    @overload
    def GetObjectData(self, serializationInfo: System.Runtime.Serialization.SerializationInfo, streamingContext: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    @overload
    def GetObjectData(self, serializationInfo: System.Runtime.Serialization.SerializationInfo, streamingContext: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class CookieVariant(System.Enum):
    """This class has no documentation."""

    Unknown = 0

    Plain = 1

    Rfc2109 = 2

    Rfc2965 = 3

    Default = ...


class TransportContext(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def GetChannelBinding(self, kind: System.Security.Authentication.ExtendedProtection.ChannelBindingKind) -> System.Security.Authentication.ExtendedProtection.ChannelBinding:
        ...


