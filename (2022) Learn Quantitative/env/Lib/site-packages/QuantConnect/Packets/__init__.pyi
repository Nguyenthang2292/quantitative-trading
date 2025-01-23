from typing import overload
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Algorithm.Framework.Alphas
import QuantConnect.Data.Custom.AlphaStreams
import QuantConnect.Notifications
import QuantConnect.Orders
import QuantConnect.Packets
import QuantConnect.Securities
import QuantConnect.Statistics
import System
import System.Collections.Generic
import System.IO


class PacketType(System.Enum):
    """Classifications of internal packet system"""

    # Cannot convert to Python: None = 0

    AlgorithmNode = 1

    AutocompleteWork = 2

    AutocompleteResult = 3

    BacktestNode = 4

    BacktestResult = 5

    BacktestWork = 6

    LiveNode = 7

    LiveResult = 8

    LiveWork = 9

    SecurityTypes = 10

    BacktestError = 11

    AlgorithmStatus = 12

    BuildWork = 13

    BuildSuccess = 14

    BuildError = 15

    RuntimeError = 16

    HandledError = 17

    Log = 18

    Debug = 19

    OrderEvent = 20

    Success = 21

    History = 22

    CommandResult = 23

    GitHubHook = 24

    DocumentationResult = 25

    Documentation = 26

    SystemDebug = 27

    AlphaResult = 28

    AlphaWork = 29

    AlphaNode = 30

    RegressionAlgorithm = 31

    AlphaHeartbeat = 32

    DebuggingStatus = 33

    OptimizationNode = 34

    OptimizationEstimate = 35

    OptimizationStatus = 36

    OptimizationResult = 37

    Aggregated = 38


class Packet(System.Object):
    """Base class for packet messaging system"""

    @property
    def Type(self) -> int:
        """
        Packet type defined by a string enum
        
        This property contains the int value of a member of the QuantConnect.Packets.PacketType enum.
        """
        ...

    @Type.setter
    def Type(self, value: int):
        """
        Packet type defined by a string enum
        
        This property contains the int value of a member of the QuantConnect.Packets.PacketType enum.
        """
        ...

    @property
    def Channel(self) -> str:
        """User unique specific channel endpoint to send the packets"""
        ...

    @Channel.setter
    def Channel(self, value: str):
        """User unique specific channel endpoint to send the packets"""
        ...

    def __init__(self, type: QuantConnect.Packets.PacketType) -> None:
        """
        Initialize the base class and setup the packet type.
        
        :param type: PacketType for the class.
        """
        ...


class DebugPacket(QuantConnect.Packets.Packet):
    """Send a simple debug message from the users algorithm to the console."""

    @property
    def Message(self) -> str:
        """String debug message to send to the users console"""
        ...

    @Message.setter
    def Message(self, value: str):
        """String debug message to send to the users console"""
        ...

    @property
    def AlgorithmId(self) -> str:
        """Associated algorithm Id."""
        ...

    @AlgorithmId.setter
    def AlgorithmId(self, value: str):
        """Associated algorithm Id."""
        ...

    @property
    def CompileId(self) -> str:
        """Compile id of the algorithm sending this message"""
        ...

    @CompileId.setter
    def CompileId(self, value: str):
        """Compile id of the algorithm sending this message"""
        ...

    @property
    def ProjectId(self) -> int:
        """Project Id for this message"""
        ...

    @ProjectId.setter
    def ProjectId(self, value: int):
        """Project Id for this message"""
        ...

    @property
    def Toast(self) -> bool:
        """
        True to emit message as a popup notification (toast),
        false to emit message in console as text
        """
        ...

    @Toast.setter
    def Toast(self, value: bool):
        """
        True to emit message as a popup notification (toast),
        false to emit message in console as text
        """
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, packetType: QuantConnect.Packets.PacketType) -> None:
        """
        Constructor for inherited types
        
        This method is protected.
        
        :param packetType: The type of packet to create
        """
        ...

    @overload
    def __init__(self, projectId: int, algorithmId: str, compileId: str, message: str, toast: bool = False) -> None:
        """Create a new instance of the notify debug packet:"""
        ...


class HistoryRequest(System.Object):
    """
    Specifies request parameters for a single historical request.
    A HistoryPacket is made of multiple requests for data. These
    are used to request data during live mode from a data server
    """

    @property
    def StartTimeUtc(self) -> datetime.datetime:
        """The start time to request data in UTC"""
        ...

    @StartTimeUtc.setter
    def StartTimeUtc(self, value: datetime.datetime):
        """The start time to request data in UTC"""
        ...

    @property
    def EndTimeUtc(self) -> datetime.datetime:
        """The end time to request data in UTC"""
        ...

    @EndTimeUtc.setter
    def EndTimeUtc(self, value: datetime.datetime):
        """The end time to request data in UTC"""
        ...

    @property
    def Symbol(self) -> QuantConnect.Symbol:
        """The symbol to request data for"""
        ...

    @Symbol.setter
    def Symbol(self, value: QuantConnect.Symbol):
        """The symbol to request data for"""
        ...

    @property
    def Resolution(self) -> QuantConnect.Resolution:
        """The requested resolution"""
        ...

    @Resolution.setter
    def Resolution(self, value: QuantConnect.Resolution):
        """The requested resolution"""
        ...

    @property
    def TickType(self) -> QuantConnect.TickType:
        """The type of data to retrieve"""
        ...

    @TickType.setter
    def TickType(self, value: QuantConnect.TickType):
        """The type of data to retrieve"""
        ...


class HistoryPacket(QuantConnect.Packets.Packet):
    """Packet for history jobs"""

    @property
    def QueueName(self) -> str:
        """The queue where the data should be sent"""
        ...

    @QueueName.setter
    def QueueName(self, value: str):
        """The queue where the data should be sent"""
        ...

    @property
    def Requests(self) -> System.Collections.Generic.List[QuantConnect.Packets.HistoryRequest]:
        """The individual requests to be processed"""
        ...

    @Requests.setter
    def Requests(self, value: System.Collections.Generic.List[QuantConnect.Packets.HistoryRequest]):
        """The individual requests to be processed"""
        ...

    def __init__(self) -> None:
        """Initializes a new instance of the HistoryPacket class"""
        ...


class HistoryResultType(System.Enum):
    """Specifies various types of history results"""

    File = 0
    """The requested file data"""

    Status = 1
    """The request's status"""

    Completed = 2
    """The request is completed"""

    Error = 3
    """The request had an error"""


class HistoryResult(System.Object, metaclass=abc.ABCMeta):
    """
    Provides a container for results from history requests. This contains
    the file path relative to the /Data folder where the data can be written
    """

    @property
    def Type(self) -> int:
        """
        Gets the type of history result
        
        This property contains the int value of a member of the QuantConnect.Packets.HistoryResultType enum.
        """
        ...

    @Type.setter
    def Type(self, value: int):
        """
        Gets the type of history result
        
        This property contains the int value of a member of the QuantConnect.Packets.HistoryResultType enum.
        """
        ...

    def __init__(self, type: QuantConnect.Packets.HistoryResultType) -> None:
        """
        Initializes a new instance of the HistoryResult class
        
        This method is protected.
        
        :param type: The type of history result
        """
        ...


class FileHistoryResult(QuantConnect.Packets.HistoryResult):
    """Defines requested file data for a history request"""

    @property
    def Filepath(self) -> str:
        """The relative file path where the data should be written"""
        ...

    @Filepath.setter
    def Filepath(self, value: str):
        """The relative file path where the data should be written"""
        ...

    @property
    def File(self) -> typing.List[int]:
        """The file's contents, this is a zipped csv file"""
        ...

    @File.setter
    def File(self, value: typing.List[int]):
        """The file's contents, this is a zipped csv file"""
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for serializers"""
        ...

    @overload
    def __init__(self, filepath: str, file: typing.List[int]) -> None:
        """
        Initializes a new instance of the HistoryResult class
        
        :param filepath: The relative file path where the file should be written, rooted in /Data, so for example ./forex/fxcm/daily/eurusd.zip
        :param file: The zipped csv file content in bytes
        """
        ...


class CompletedHistoryResult(QuantConnect.Packets.HistoryResult):
    """Specifies the completed message from a history result"""

    def __init__(self) -> None:
        """Initializes a new instance of CompletedHistoryResult class"""
        ...


class ErrorHistoryResult(QuantConnect.Packets.HistoryResult):
    """Specfies an error message in a history result"""

    @property
    def Message(self) -> str:
        """Gets the error that was encountered"""
        ...

    @Message.setter
    def Message(self, value: str):
        """Gets the error that was encountered"""
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for serializers"""
        ...

    @overload
    def __init__(self, message: str) -> None:
        """
        Initializes a new instance of the ErrorHistoryResult class
        
        :param message: The error message
        """
        ...


class StatusHistoryResult(QuantConnect.Packets.HistoryResult):
    """Specifies the progress of a request"""

    @property
    def Progress(self) -> int:
        """Gets the progress of the request"""
        ...

    @Progress.setter
    def Progress(self, value: int):
        """Gets the progress of the request"""
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for serializers"""
        ...

    @overload
    def __init__(self, progress: int) -> None:
        """
        Initializes a new instance of the StatusHistoryResult class
        
        :param progress: The progress, from 0 to 100
        """
        ...


class RuntimeErrorPacket(QuantConnect.Packets.Packet):
    """
    Algorithm runtime error packet from the lean engine.
    This is a managed error which stops the algorithm execution.
    """

    @property
    def Message(self) -> str:
        """Runtime error message from the exception"""
        ...

    @Message.setter
    def Message(self, value: str):
        """Runtime error message from the exception"""
        ...

    @property
    def AlgorithmId(self) -> str:
        """Algorithm id which generated this runtime error"""
        ...

    @AlgorithmId.setter
    def AlgorithmId(self, value: str):
        """Algorithm id which generated this runtime error"""
        ...

    @property
    def StackTrace(self) -> str:
        """Error stack trace information string passed through from the Lean exception"""
        ...

    @StackTrace.setter
    def StackTrace(self, value: str):
        """Error stack trace information string passed through from the Lean exception"""
        ...

    @property
    def UserId(self) -> int:
        """User Id associated with the backtest that threw the error"""
        ...

    @UserId.setter
    def UserId(self, value: int):
        """User Id associated with the backtest that threw the error"""
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, userId: int, algorithmId: str, message: str, stacktrace: str = ...) -> None:
        """Create a new runtime error packet"""
        ...


class SecurityTypesPacket(QuantConnect.Packets.Packet):
    """Security types packet contains information on the markets the user data has requested."""

    @property
    def Types(self) -> System.Collections.Generic.List[QuantConnect.SecurityType]:
        """List of Security Type the user has requested (Equity, Forex, Futures etc)."""
        ...

    @Types.setter
    def Types(self, value: System.Collections.Generic.List[QuantConnect.SecurityType]):
        """List of Security Type the user has requested (Equity, Forex, Futures etc)."""
        ...

    @property
    def TypesCSV(self) -> str:
        """CSV formatted, lower case list of SecurityTypes for the web API."""
        ...

    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...


class MarketHours(System.Object):
    """Market open hours model for pre, normal and post market hour definitions."""

    @property
    def Start(self) -> datetime.datetime:
        """Start time for this market hour category"""
        ...

    @Start.setter
    def Start(self, value: datetime.datetime):
        """Start time for this market hour category"""
        ...

    @property
    def End(self) -> datetime.datetime:
        """End time for this market hour category"""
        ...

    @End.setter
    def End(self, value: datetime.datetime):
        """End time for this market hour category"""
        ...

    def __init__(self, referenceDate: typing.Union[datetime.datetime, datetime.date], defaultStart: float, defaultEnd: float) -> None:
        """
        Market hours initializer given an hours since midnight measure for the market hours today
        
        :param referenceDate: Reference date used for as base date from the specified hour offsets
        :param defaultStart: Time in hours since midnight to start this open period.
        :param defaultEnd: Time in hours since midnight to end this open period.
        """
        ...


class MarketToday(System.Object):
    """Market today information class"""

    @property
    def Date(self) -> datetime.datetime:
        """Date this packet was generated."""
        ...

    @Date.setter
    def Date(self, value: datetime.datetime):
        """Date this packet was generated."""
        ...

    @property
    def Status(self) -> str:
        """Given the dates and times above, what is the current market status - open or closed."""
        ...

    @Status.setter
    def Status(self, value: str):
        """Given the dates and times above, what is the current market status - open or closed."""
        ...

    @property
    def PreMarket(self) -> QuantConnect.Packets.MarketHours:
        """Premarket hours for today"""
        ...

    @PreMarket.setter
    def PreMarket(self, value: QuantConnect.Packets.MarketHours):
        """Premarket hours for today"""
        ...

    @property
    def Open(self) -> QuantConnect.Packets.MarketHours:
        """Normal trading market hours for today"""
        ...

    @Open.setter
    def Open(self, value: QuantConnect.Packets.MarketHours):
        """Normal trading market hours for today"""
        ...

    @property
    def PostMarket(self) -> QuantConnect.Packets.MarketHours:
        """Post market hours for today"""
        ...

    @PostMarket.setter
    def PostMarket(self, value: QuantConnect.Packets.MarketHours):
        """Post market hours for today"""
        ...

    def __init__(self) -> None:
        """Default constructor (required for JSON serialization)"""
        ...


class PythonEnvironmentPacket(QuantConnect.Packets.Packet, metaclass=abc.ABCMeta):
    """
    Python Environment Packet is an abstract packet that contains a PythonVirtualEnvironment
    definition. Intended to be used by inheriting classes that may use a PythonVirtualEnvironment
    """

    @property
    def PythonVirtualEnvironment(self) -> str:
        """
        Virtual environment ID used to find PythonEvironments
        Ideally MD5, but environment names work as well.
        """
        ...

    @PythonVirtualEnvironment.setter
    def PythonVirtualEnvironment(self, value: str):
        """
        Virtual environment ID used to find PythonEvironments
        Ideally MD5, but environment names work as well.
        """
        ...

    def __init__(self, type: QuantConnect.Packets.PacketType) -> None:
        """
        Default constructor for a PythonEnvironmentPacket
        
        This method is protected.
        """
        ...


class LeakyBucketControlParameters(System.Object):
    """
    Provides parameters that control the behavior of a leaky bucket rate limiting algorithm. The
    parameter names below are phrased in the positive, such that the bucket is filled up over time
    vs leaking out over time.
    """

    DefaultCapacity: int = ...

    DefaultTimeInterval: int = ...
    """Default time interval"""

    DefaultRefillAmount: int = ...
    """Default refill amount"""

    @property
    def Capacity(self) -> int:
        """
        Sets the total capacity of the bucket in a leaky bucket algorithm. This is the maximum
        number of 'units' the bucket can hold and also defines the maximum burst rate, assuming
        instantaneous usage of 'units'. In reality, the usage of 'units' takes times, and so it
        is possible for the bucket to incrementally refill while consuming from the bucket.
        """
        ...

    @Capacity.setter
    def Capacity(self, value: int):
        """
        Sets the total capacity of the bucket in a leaky bucket algorithm. This is the maximum
        number of 'units' the bucket can hold and also defines the maximum burst rate, assuming
        instantaneous usage of 'units'. In reality, the usage of 'units' takes times, and so it
        is possible for the bucket to incrementally refill while consuming from the bucket.
        """
        ...

    @property
    def RefillAmount(self) -> int:
        """
        Sets the refill amount of the bucket. This defines the quantity of 'units' that become available
        to a consuming entity after the time interval has elapsed. For example, if the refill amount is
        equal to one, then each time interval one new 'unit' will be made available for a consumer that is
        throttled by the leaky bucket.
        """
        ...

    @RefillAmount.setter
    def RefillAmount(self, value: int):
        """
        Sets the refill amount of the bucket. This defines the quantity of 'units' that become available
        to a consuming entity after the time interval has elapsed. For example, if the refill amount is
        equal to one, then each time interval one new 'unit' will be made available for a consumer that is
        throttled by the leaky bucket.
        """
        ...

    @property
    def TimeIntervalMinutes(self) -> int:
        """
        Sets the time interval for the refill amount of the bucket, in minutes. After this amount of wall-clock
        time has passed, the bucket will refill the refill amount, thereby making more 'units' available
        for a consumer. For example, if the refill amount equals 10 and the time interval is 30 minutes, then
        every 30 minutes, 10 more 'units' become available for a consumer. The available 'units' will
        continue to increase until the bucket capacity is reached.
        """
        ...

    @TimeIntervalMinutes.setter
    def TimeIntervalMinutes(self, value: int):
        """
        Sets the time interval for the refill amount of the bucket, in minutes. After this amount of wall-clock
        time has passed, the bucket will refill the refill amount, thereby making more 'units' available
        for a consumer. For example, if the refill amount equals 10 and the time interval is 30 minutes, then
        every 30 minutes, 10 more 'units' become available for a consumer. The available 'units' will
        continue to increase until the bucket capacity is reached.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the LeakyBucketControlParameters using default values"""
        ...

    @overload
    def __init__(self, capacity: int, refillAmount: int, timeIntervalMinutes: int) -> None:
        """
        Initializes a new instance of the LeakyBucketControlParameters with the specified value
        
        :param capacity: The total capacity of the bucket in minutes
        :param refillAmount: The number of additional minutes to add to the bucket after  has elapsed
        :param timeIntervalMinutes: The interval, in minutes, that must pass before the  is added back to the bucket for reuse
        """
        ...


class Controls(System.Object):
    """Specifies values used to control algorithm limits"""

    @property
    def MaximumRuntimeMinutes(self) -> int:
        """The maximum runtime in minutes"""
        ...

    @MaximumRuntimeMinutes.setter
    def MaximumRuntimeMinutes(self, value: int):
        """The maximum runtime in minutes"""
        ...

    @property
    def MinuteLimit(self) -> int:
        """The maximum number of minute symbols"""
        ...

    @MinuteLimit.setter
    def MinuteLimit(self, value: int):
        """The maximum number of minute symbols"""
        ...

    @property
    def SecondLimit(self) -> int:
        """The maximum number of second symbols"""
        ...

    @SecondLimit.setter
    def SecondLimit(self, value: int):
        """The maximum number of second symbols"""
        ...

    @property
    def TickLimit(self) -> int:
        """The maximum number of tick symbol"""
        ...

    @TickLimit.setter
    def TickLimit(self, value: int):
        """The maximum number of tick symbol"""
        ...

    @property
    def RamAllocation(self) -> int:
        """Ram allocation for this algorithm in MB"""
        ...

    @RamAllocation.setter
    def RamAllocation(self, value: int):
        """Ram allocation for this algorithm in MB"""
        ...

    @property
    def CpuAllocation(self) -> float:
        """CPU allocation for this algorithm"""
        ...

    @CpuAllocation.setter
    def CpuAllocation(self, value: float):
        """CPU allocation for this algorithm"""
        ...

    @property
    def BacktestLogLimit(self) -> int:
        """The user backtesting log limit"""
        ...

    @BacktestLogLimit.setter
    def BacktestLogLimit(self, value: int):
        """The user backtesting log limit"""
        ...

    @property
    def DailyLogLimit(self) -> int:
        """The daily log limit of a user"""
        ...

    @DailyLogLimit.setter
    def DailyLogLimit(self, value: int):
        """The daily log limit of a user"""
        ...

    @property
    def RemainingLogAllowance(self) -> int:
        """The remaining log allowance for a user"""
        ...

    @RemainingLogAllowance.setter
    def RemainingLogAllowance(self, value: int):
        """The remaining log allowance for a user"""
        ...

    @property
    def BacktestingMaxInsights(self) -> int:
        """Maximimum number of insights we'll store and score in a single backtest"""
        ...

    @BacktestingMaxInsights.setter
    def BacktestingMaxInsights(self, value: int):
        """Maximimum number of insights we'll store and score in a single backtest"""
        ...

    @property
    def BacktestingMaxOrders(self) -> int:
        """Maximimum number of orders we'll allow in a backtest."""
        ...

    @BacktestingMaxOrders.setter
    def BacktestingMaxOrders(self, value: int):
        """Maximimum number of orders we'll allow in a backtest."""
        ...

    @property
    def MaximumDataPointsPerChartSeries(self) -> int:
        """Limits the amount of data points per chart series. Applies only for backtesting"""
        ...

    @MaximumDataPointsPerChartSeries.setter
    def MaximumDataPointsPerChartSeries(self, value: int):
        """Limits the amount of data points per chart series. Applies only for backtesting"""
        ...

    @property
    def SecondTimeOut(self) -> int:
        """The amount seconds used for timeout limits"""
        ...

    @SecondTimeOut.setter
    def SecondTimeOut(self, value: int):
        """The amount seconds used for timeout limits"""
        ...

    @property
    def TrainingLimits(self) -> QuantConnect.Packets.LeakyBucketControlParameters:
        """
        Sets parameters used for determining the behavior of the leaky bucket algorithm that
        controls how much time is available for an algorithm to use the training feature.
        """
        ...

    @TrainingLimits.setter
    def TrainingLimits(self, value: QuantConnect.Packets.LeakyBucketControlParameters):
        """
        Sets parameters used for determining the behavior of the leaky bucket algorithm that
        controls how much time is available for an algorithm to use the training feature.
        """
        ...

    @property
    def StorageLimit(self) -> int:
        """Limits the total size of storage used by IObjectStore"""
        ...

    @StorageLimit.setter
    def StorageLimit(self, value: int):
        """Limits the total size of storage used by IObjectStore"""
        ...

    @property
    def StorageFileCount(self) -> int:
        """Limits the number of files to be held under the IObjectStore"""
        ...

    @StorageFileCount.setter
    def StorageFileCount(self, value: int):
        """Limits the number of files to be held under the IObjectStore"""
        ...

    @property
    def StoragePermissions(self) -> System.IO.FileAccess:
        """Holds the permissions for the object store"""
        ...

    @StoragePermissions.setter
    def StoragePermissions(self, value: System.IO.FileAccess):
        """Holds the permissions for the object store"""
        ...

    @property
    def PersistenceIntervalSeconds(self) -> int:
        """
        The interval over which the IObjectStore will persistence the contents of
        the object store
        """
        ...

    @PersistenceIntervalSeconds.setter
    def PersistenceIntervalSeconds(self, value: int):
        """
        The interval over which the IObjectStore will persistence the contents of
        the object store
        """
        ...

    @property
    def CreditCost(self) -> float:
        """The cost associated with running this job"""
        ...

    @CreditCost.setter
    def CreditCost(self, value: float):
        """The cost associated with running this job"""
        ...

    def __init__(self) -> None:
        """Initializes a new default instance of the Controls class"""
        ...


class AlgorithmNodePacket(QuantConnect.Packets.PythonEnvironmentPacket):
    """Algorithm Node Packet is a work task for the Lean Engine"""

    @property
    def HostName(self) -> str:
        """The host name to use if any"""
        ...

    @HostName.setter
    def HostName(self, value: str):
        """The host name to use if any"""
        ...

    @property
    def UserId(self) -> int:
        """User Id placing request"""
        ...

    @UserId.setter
    def UserId(self, value: int):
        """User Id placing request"""
        ...

    @property
    def UserToken(self) -> str:
        ...

    @UserToken.setter
    def UserToken(self, value: str):
        ...

    @property
    def OrganizationId(self) -> str:
        ...

    @OrganizationId.setter
    def OrganizationId(self, value: str):
        ...

    @property
    def ProjectId(self) -> int:
        """Project Id of the request"""
        ...

    @ProjectId.setter
    def ProjectId(self, value: int):
        """Project Id of the request"""
        ...

    @property
    def ProjectName(self) -> str:
        """Project name of the request"""
        ...

    @ProjectName.setter
    def ProjectName(self, value: str):
        """Project name of the request"""
        ...

    @property
    def AlgorithmId(self) -> str:
        """Algorithm Id - BacktestId or DeployId - Common Id property between packets."""
        ...

    @property
    def SessionId(self) -> str:
        """User session Id for authentication"""
        ...

    @SessionId.setter
    def SessionId(self, value: str):
        """User session Id for authentication"""
        ...

    @property
    def Language(self) -> QuantConnect.Language:
        """Language flag: Currently represents IL code or Dynamic Scripted Types."""
        ...

    @Language.setter
    def Language(self, value: QuantConnect.Language):
        """Language flag: Currently represents IL code or Dynamic Scripted Types."""
        ...

    @property
    def ServerType(self) -> QuantConnect.ServerType:
        """Server type for the deployment (512, 1024, 2048)"""
        ...

    @ServerType.setter
    def ServerType(self, value: QuantConnect.ServerType):
        """Server type for the deployment (512, 1024, 2048)"""
        ...

    @property
    def CompileId(self) -> str:
        """Unique compile id of this backtest"""
        ...

    @CompileId.setter
    def CompileId(self, value: str):
        """Unique compile id of this backtest"""
        ...

    @property
    def Version(self) -> str:
        """Version number identifier for the lean engine."""
        ...

    @Version.setter
    def Version(self, value: str):
        """Version number identifier for the lean engine."""
        ...

    @property
    def Redelivered(self) -> bool:
        """
        An algorithm packet which has already been run and is being redelivered on this node.
        In this event we don't want to relaunch the task as it may result in unexpected behaviour for user.
        """
        ...

    @Redelivered.setter
    def Redelivered(self, value: bool):
        """
        An algorithm packet which has already been run and is being redelivered on this node.
        In this event we don't want to relaunch the task as it may result in unexpected behaviour for user.
        """
        ...

    @property
    def Algorithm(self) -> typing.List[int]:
        """Algorithm binary with zip of contents"""
        ...

    @Algorithm.setter
    def Algorithm(self, value: typing.List[int]):
        """Algorithm binary with zip of contents"""
        ...

    @property
    def RequestSource(self) -> str:
        """Request source - Web IDE or API - for controling result handler behaviour"""
        ...

    @RequestSource.setter
    def RequestSource(self, value: str):
        """Request source - Web IDE or API - for controling result handler behaviour"""
        ...

    @property
    def RamAllocation(self) -> int:
        """The maximum amount of RAM (in MB) this algorithm is allowed to utilize"""
        ...

    @property
    def Controls(self) -> QuantConnect.Packets.Controls:
        """Specifies values to control algorithm limits"""
        ...

    @Controls.setter
    def Controls(self, value: QuantConnect.Packets.Controls):
        """Specifies values to control algorithm limits"""
        ...

    @property
    def Parameters(self) -> System.Collections.Generic.Dictionary[str, str]:
        """The parameter values used to set algorithm parameters"""
        ...

    @Parameters.setter
    def Parameters(self, value: System.Collections.Generic.Dictionary[str, str]):
        """The parameter values used to set algorithm parameters"""
        ...

    @property
    def HistoryProvider(self) -> str:
        """String name of the HistoryProvider we're running with"""
        ...

    @HistoryProvider.setter
    def HistoryProvider(self, value: str):
        """String name of the HistoryProvider we're running with"""
        ...

    def __init__(self, type: QuantConnect.Packets.PacketType) -> None:
        """Default constructor for the algorithm node:"""
        ...

    def GetAlgorithmName(self) -> str:
        """Gets a unique name for the algorithm defined by this packet"""
        ...


class LiveNodePacket(QuantConnect.Packets.AlgorithmNodePacket):
    """Live job task packet: container for any live specific job variables"""

    @property
    def DeployId(self) -> str:
        """Deploy Id for this live algorithm."""
        ...

    @DeployId.setter
    def DeployId(self, value: str):
        """Deploy Id for this live algorithm."""
        ...

    @property
    def Brokerage(self) -> str:
        """String name of the brokerage we're trading with"""
        ...

    @Brokerage.setter
    def Brokerage(self, value: str):
        """String name of the brokerage we're trading with"""
        ...

    @property
    def BrokerageData(self) -> System.Collections.Generic.Dictionary[str, str]:
        """String-String Dictionary of Brokerage Data for this Live Job"""
        ...

    @BrokerageData.setter
    def BrokerageData(self, value: System.Collections.Generic.Dictionary[str, str]):
        """String-String Dictionary of Brokerage Data for this Live Job"""
        ...

    @property
    def DataQueueHandler(self) -> str:
        """String name of the DataQueueHandler or LiveDataProvider we're running with"""
        ...

    @DataQueueHandler.setter
    def DataQueueHandler(self, value: str):
        """String name of the DataQueueHandler or LiveDataProvider we're running with"""
        ...

    @property
    def DataChannelProvider(self) -> str:
        """String name of the DataChannelProvider we're running with"""
        ...

    @DataChannelProvider.setter
    def DataChannelProvider(self, value: str):
        """String name of the DataChannelProvider we're running with"""
        ...

    @property
    def DisableAcknowledgement(self) -> bool:
        """Gets flag indicating whether or not the message should be acknowledged and removed from the queue"""
        ...

    @DisableAcknowledgement.setter
    def DisableAcknowledgement(self, value: bool):
        """Gets flag indicating whether or not the message should be acknowledged and removed from the queue"""
        ...

    @property
    def NotificationEvents(self) -> System.Collections.Generic.HashSet[str]:
        """A list of event types to generate notifications for, which will use NotificationTargets"""
        ...

    @NotificationEvents.setter
    def NotificationEvents(self, value: System.Collections.Generic.HashSet[str]):
        """A list of event types to generate notifications for, which will use NotificationTargets"""
        ...

    @property
    def NotificationTargets(self) -> System.Collections.Generic.List[QuantConnect.Notifications.Notification]:
        """A list of notification targets to use"""
        ...

    @NotificationTargets.setter
    def NotificationTargets(self, value: System.Collections.Generic.List[QuantConnect.Notifications.Notification]):
        """A list of notification targets to use"""
        ...

    @property
    def LiveDataTypes(self) -> System.Collections.Generic.HashSet[str]:
        """List of real time data types available in the live trading environment"""
        ...

    @LiveDataTypes.setter
    def LiveDataTypes(self, value: System.Collections.Generic.HashSet[str]):
        """List of real time data types available in the live trading environment"""
        ...

    def __init__(self) -> None:
        """Default constructor for JSON of the Live Task Packet"""
        ...


class AlphaNodePacket(QuantConnect.Packets.LiveNodePacket):
    """Alpha job packet"""

    @property
    def AlphaId(self) -> str:
        """Gets or sets the alpha id"""
        ...

    @AlphaId.setter
    def AlphaId(self, value: str):
        """Gets or sets the alpha id"""
        ...

    def __init__(self) -> None:
        """Initializes a new default instance of the AlgorithmNodePacket class"""
        ...


class SystemDebugPacket(QuantConnect.Packets.DebugPacket):
    """Debug packets generated by Lean"""

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, projectId: int, algorithmId: str, compileId: str, message: str, toast: bool = False) -> None:
        """Create a new instance of the system debug packet"""
        ...


class BaseResultParameters(System.Object):
    """Base parameters used by LiveResultParameters and BacktestResultParameters"""

    @property
    def AlphaRuntimeStatistics(self) -> QuantConnect.AlphaRuntimeStatistics:
        """Contains population averages scores over the life of the algorithm"""
        ...

    @AlphaRuntimeStatistics.setter
    def AlphaRuntimeStatistics(self, value: QuantConnect.AlphaRuntimeStatistics):
        """Contains population averages scores over the life of the algorithm"""
        ...

    @property
    def ProfitLoss(self) -> System.Collections.Generic.IDictionary[datetime.datetime, float]:
        """Trade profit and loss information since the last algorithm result packet"""
        ...

    @ProfitLoss.setter
    def ProfitLoss(self, value: System.Collections.Generic.IDictionary[datetime.datetime, float]):
        """Trade profit and loss information since the last algorithm result packet"""
        ...

    @property
    def Charts(self) -> System.Collections.Generic.IDictionary[str, QuantConnect.Chart]:
        """Charts updates for the live algorithm since the last result packet"""
        ...

    @Charts.setter
    def Charts(self, value: System.Collections.Generic.IDictionary[str, QuantConnect.Chart]):
        """Charts updates for the live algorithm since the last result packet"""
        ...

    @property
    def Orders(self) -> System.Collections.Generic.IDictionary[int, QuantConnect.Orders.Order]:
        """Order updates since the last result packet"""
        ...

    @Orders.setter
    def Orders(self, value: System.Collections.Generic.IDictionary[int, QuantConnect.Orders.Order]):
        """Order updates since the last result packet"""
        ...

    @property
    def OrderEvents(self) -> System.Collections.Generic.List[QuantConnect.Orders.OrderEvent]:
        """Order events updates since the last result packet"""
        ...

    @OrderEvents.setter
    def OrderEvents(self, value: System.Collections.Generic.List[QuantConnect.Orders.OrderEvent]):
        """Order events updates since the last result packet"""
        ...

    @property
    def Statistics(self) -> System.Collections.Generic.IDictionary[str, str]:
        """Statistics information sent during the algorithm operations."""
        ...

    @Statistics.setter
    def Statistics(self, value: System.Collections.Generic.IDictionary[str, str]):
        """Statistics information sent during the algorithm operations."""
        ...

    @property
    def RuntimeStatistics(self) -> System.Collections.Generic.IDictionary[str, str]:
        """Runtime banner/updating statistics in the title banner of the live algorithm GUI."""
        ...

    @RuntimeStatistics.setter
    def RuntimeStatistics(self, value: System.Collections.Generic.IDictionary[str, str]):
        """Runtime banner/updating statistics in the title banner of the live algorithm GUI."""
        ...

    @property
    def AlgorithmConfiguration(self) -> QuantConnect.AlgorithmConfiguration:
        """The algorithm's configuration required for report generation"""
        ...

    @AlgorithmConfiguration.setter
    def AlgorithmConfiguration(self, value: QuantConnect.AlgorithmConfiguration):
        """The algorithm's configuration required for report generation"""
        ...


class LiveResultParameters(QuantConnect.Packets.BaseResultParameters):
    """Defines the parameters for LiveResult"""

    @property
    def Holdings(self) -> System.Collections.Generic.IDictionary[str, QuantConnect.Holding]:
        """Holdings dictionary of algorithm holdings information"""
        ...

    @Holdings.setter
    def Holdings(self, value: System.Collections.Generic.IDictionary[str, QuantConnect.Holding]):
        """Holdings dictionary of algorithm holdings information"""
        ...

    @property
    def CashBook(self) -> QuantConnect.Securities.CashBook:
        """Cashbook for the algorithm's live results."""
        ...

    @CashBook.setter
    def CashBook(self, value: QuantConnect.Securities.CashBook):
        """Cashbook for the algorithm's live results."""
        ...

    @property
    def ServerStatistics(self) -> System.Collections.Generic.IDictionary[str, str]:
        """Server status information, including CPU/RAM usage, ect..."""
        ...

    @ServerStatistics.setter
    def ServerStatistics(self, value: System.Collections.Generic.IDictionary[str, str]):
        """Server status information, including CPU/RAM usage, ect..."""
        ...

    def __init__(self, charts: System.Collections.Generic.IDictionary[str, QuantConnect.Chart], orders: System.Collections.Generic.IDictionary[int, QuantConnect.Orders.Order], profitLoss: System.Collections.Generic.IDictionary[datetime.datetime, float], holdings: System.Collections.Generic.IDictionary[str, QuantConnect.Holding], cashBook: QuantConnect.Securities.CashBook, statistics: System.Collections.Generic.IDictionary[str, str], runtimeStatistics: System.Collections.Generic.IDictionary[str, str], orderEvents: System.Collections.Generic.List[QuantConnect.Orders.OrderEvent], serverStatistics: System.Collections.Generic.IDictionary[str, str] = None, alphaRuntimeStatistics: QuantConnect.AlphaRuntimeStatistics = None, algorithmConfiguration: QuantConnect.AlgorithmConfiguration = None) -> None:
        """Creates a new instance"""
        ...


class LiveResult(QuantConnect.Result):
    """Live results object class for packaging live result data."""

    @property
    def Holdings(self) -> System.Collections.Generic.IDictionary[str, QuantConnect.Holding]:
        """Holdings dictionary of algorithm holdings information"""
        ...

    @Holdings.setter
    def Holdings(self, value: System.Collections.Generic.IDictionary[str, QuantConnect.Holding]):
        """Holdings dictionary of algorithm holdings information"""
        ...

    @property
    def CashBook(self) -> QuantConnect.Securities.CashBook:
        """Cashbook for the algorithm's live results."""
        ...

    @CashBook.setter
    def CashBook(self, value: QuantConnect.Securities.CashBook):
        """Cashbook for the algorithm's live results."""
        ...

    @property
    def Cash(self) -> System.Collections.Generic.Dictionary[str, QuantConnect.Securities.Cash]:
        """Cash for the algorithm's live results."""
        ...

    @Cash.setter
    def Cash(self, value: System.Collections.Generic.Dictionary[str, QuantConnect.Securities.Cash]):
        """Cash for the algorithm's live results."""
        ...

    @property
    def AccountCurrency(self) -> str:
        """The algorithm's account currency"""
        ...

    @AccountCurrency.setter
    def AccountCurrency(self, value: str):
        """The algorithm's account currency"""
        ...

    @property
    def AccountCurrencySymbol(self) -> str:
        """The algorithm's account currency"""
        ...

    @AccountCurrencySymbol.setter
    def AccountCurrencySymbol(self, value: str):
        """The algorithm's account currency"""
        ...

    @overload
    def __init__(self) -> None:
        """Default Constructor"""
        ...

    @overload
    def __init__(self, parameters: QuantConnect.Packets.LiveResultParameters) -> None:
        """Constructor for the result class for dictionary objects"""
        ...


class LiveResultPacket(QuantConnect.Packets.Packet):
    """Live result packet from a lean engine algorithm."""

    @property
    def UserId(self) -> int:
        """User Id sending result packet"""
        ...

    @UserId.setter
    def UserId(self, value: int):
        """User Id sending result packet"""
        ...

    @property
    def ProjectId(self) -> int:
        """Project Id of the result packet"""
        ...

    @ProjectId.setter
    def ProjectId(self, value: int):
        """Project Id of the result packet"""
        ...

    @property
    def SessionId(self) -> str:
        """User session Id who issued the result packet"""
        ...

    @SessionId.setter
    def SessionId(self, value: str):
        """User session Id who issued the result packet"""
        ...

    @property
    def DeployId(self) -> str:
        """Live Algorithm Id (DeployId) for this result packet"""
        ...

    @DeployId.setter
    def DeployId(self, value: str):
        """Live Algorithm Id (DeployId) for this result packet"""
        ...

    @property
    def CompileId(self) -> str:
        """Compile Id algorithm which generated this result packet"""
        ...

    @CompileId.setter
    def CompileId(self, value: str):
        """Compile Id algorithm which generated this result packet"""
        ...

    @property
    def Results(self) -> QuantConnect.Packets.LiveResult:
        """Result data object for this result packet"""
        ...

    @Results.setter
    def Results(self, value: QuantConnect.Packets.LiveResult):
        """Result data object for this result packet"""
        ...

    @property
    def ProcessingTime(self) -> float:
        """Processing time / running time for the live algorithm."""
        ...

    @ProcessingTime.setter
    def ProcessingTime(self, value: float):
        """Processing time / running time for the live algorithm."""
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON Serialization"""
        ...

    @overload
    def __init__(self, json: str) -> None:
        """Compose the packet from a JSON string:"""
        ...

    @overload
    def __init__(self, job: QuantConnect.Packets.LiveNodePacket, results: QuantConnect.Packets.LiveResult) -> None:
        """
        Compose Live Result Data Packet - With tradable dates
        
        :param job: Job that started this request
        :param results: Results class for the Backtest job
        """
        ...

    @staticmethod
    def CreateEmpty(job: QuantConnect.Packets.LiveNodePacket) -> QuantConnect.Packets.LiveResultPacket:
        """
        Creates an empty result packet, useful when the algorithm fails to initialize
        
        :param job: The associated job packet
        :returns: An empty result packet.
        """
        ...


class BacktestResultParameters(QuantConnect.Packets.BaseResultParameters):
    """Defines the parameters for BacktestResult"""

    @property
    def RollingWindow(self) -> System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance]:
        """Rolling window detailed statistics."""
        ...

    @RollingWindow.setter
    def RollingWindow(self, value: System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance]):
        """Rolling window detailed statistics."""
        ...

    @property
    def TotalPerformance(self) -> QuantConnect.Statistics.AlgorithmPerformance:
        """Rolling window detailed statistics."""
        ...

    @TotalPerformance.setter
    def TotalPerformance(self, value: QuantConnect.Statistics.AlgorithmPerformance):
        """Rolling window detailed statistics."""
        ...

    def __init__(self, charts: System.Collections.Generic.IDictionary[str, QuantConnect.Chart], orders: System.Collections.Generic.IDictionary[int, QuantConnect.Orders.Order], profitLoss: System.Collections.Generic.IDictionary[datetime.datetime, float], statistics: System.Collections.Generic.IDictionary[str, str], runtimeStatistics: System.Collections.Generic.IDictionary[str, str], rollingWindow: System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance], orderEvents: System.Collections.Generic.List[QuantConnect.Orders.OrderEvent], totalPerformance: QuantConnect.Statistics.AlgorithmPerformance = None, alphaRuntimeStatistics: QuantConnect.AlphaRuntimeStatistics = None, algorithmConfiguration: QuantConnect.AlgorithmConfiguration = None) -> None:
        """Creates a new instance"""
        ...


class AlgorithmStatusPacket(QuantConnect.Packets.Packet):
    """Algorithm status update information packet"""

    @property
    def Status(self) -> QuantConnect.AlgorithmStatus:
        """Current algorithm status"""
        ...

    @Status.setter
    def Status(self, value: QuantConnect.AlgorithmStatus):
        """Current algorithm status"""
        ...

    @property
    def ChartSubscription(self) -> str:
        """Chart we're subscribed to for live trading."""
        ...

    @ChartSubscription.setter
    def ChartSubscription(self, value: str):
        """Chart we're subscribed to for live trading."""
        ...

    @property
    def Message(self) -> str:
        """Optional message or reason for state change."""
        ...

    @Message.setter
    def Message(self, value: str):
        """Optional message or reason for state change."""
        ...

    @property
    def AlgorithmId(self) -> str:
        """Algorithm Id associated with this status packet"""
        ...

    @AlgorithmId.setter
    def AlgorithmId(self, value: str):
        """Algorithm Id associated with this status packet"""
        ...

    @property
    def OptimizationId(self) -> str:
        """OptimizationId for this result packet if any"""
        ...

    @OptimizationId.setter
    def OptimizationId(self, value: str):
        """OptimizationId for this result packet if any"""
        ...

    @property
    def ProjectId(self) -> int:
        """Project Id associated with this status packet"""
        ...

    @ProjectId.setter
    def ProjectId(self, value: int):
        """Project Id associated with this status packet"""
        ...

    @property
    def ChannelStatus(self) -> str:
        """The current state of the channel"""
        ...

    @ChannelStatus.setter
    def ChannelStatus(self, value: str):
        """The current state of the channel"""
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, algorithmId: str, projectId: int, status: QuantConnect.AlgorithmStatus, message: str = ...) -> None:
        """Initialize algorithm state packet:"""
        ...


class LogPacket(QuantConnect.Packets.Packet):
    """Simple log message instruction from the lean engine."""

    @property
    def Message(self) -> str:
        """Log message to the users console:"""
        ...

    @Message.setter
    def Message(self, value: str):
        """Log message to the users console:"""
        ...

    @property
    def AlgorithmId(self) -> str:
        """Algorithm Id requesting this logging"""
        ...

    @AlgorithmId.setter
    def AlgorithmId(self, value: str):
        """Algorithm Id requesting this logging"""
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, algorithmId: str, message: str) -> None:
        """Create a new instance of the notify Log packet:"""
        ...


class OrderEventPacket(QuantConnect.Packets.Packet):
    """Order event packet for passing updates on the state of an order to the portfolio."""

    @property
    def Event(self) -> QuantConnect.Orders.OrderEvent:
        """Order event object"""
        ...

    @Event.setter
    def Event(self, value: QuantConnect.Orders.OrderEvent):
        """Order event object"""
        ...

    @property
    def AlgorithmId(self) -> str:
        """Algorithm id for this order event"""
        ...

    @AlgorithmId.setter
    def AlgorithmId(self, value: str):
        """Algorithm id for this order event"""
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, algorithmId: str, eventOrder: QuantConnect.Orders.OrderEvent) -> None:
        """Create a new instance of the order event packet"""
        ...


class AlphaResultPacket(QuantConnect.Packets.Packet):
    """Provides a packet type for transmitting alpha insights data"""

    @property
    def UserId(self) -> int:
        """The user's id that deployed the alpha stream"""
        ...

    @UserId.setter
    def UserId(self, value: int):
        """The user's id that deployed the alpha stream"""
        ...

    @property
    def AlphaId(self) -> str:
        """
        The deployed alpha id. This is the id generated upon submssion to the alpha marketplace.
        If this is a user backtest or live algo then this will not be specified
        """
        ...

    @AlphaId.setter
    def AlphaId(self, value: str):
        """
        The deployed alpha id. This is the id generated upon submssion to the alpha marketplace.
        If this is a user backtest or live algo then this will not be specified
        """
        ...

    @property
    def AlgorithmId(self) -> str:
        """The algorithm's unique identifier"""
        ...

    @AlgorithmId.setter
    def AlgorithmId(self, value: str):
        """The algorithm's unique identifier"""
        ...

    @property
    def Insights(self) -> System.Collections.Generic.List[QuantConnect.Algorithm.Framework.Alphas.Insight]:
        """The generated insights"""
        ...

    @Insights.setter
    def Insights(self, value: System.Collections.Generic.List[QuantConnect.Algorithm.Framework.Alphas.Insight]):
        """The generated insights"""
        ...

    @property
    def OrderEvents(self) -> System.Collections.Generic.List[QuantConnect.Orders.OrderEvent]:
        """The generated OrderEvents"""
        ...

    @OrderEvents.setter
    def OrderEvents(self, value: System.Collections.Generic.List[QuantConnect.Orders.OrderEvent]):
        """The generated OrderEvents"""
        ...

    @property
    def Orders(self) -> System.Collections.Generic.List[QuantConnect.Orders.Order]:
        """The new or updated Orders"""
        ...

    @Orders.setter
    def Orders(self, value: System.Collections.Generic.List[QuantConnect.Orders.Order]):
        """The new or updated Orders"""
        ...

    @property
    def Portfolio(self) -> QuantConnect.Data.Custom.AlphaStreams.AlphaStreamsPortfolioState:
        """The algorithms current portfolio state"""
        ...

    @Portfolio.setter
    def Portfolio(self, value: QuantConnect.Data.Custom.AlphaStreams.AlphaStreamsPortfolioState):
        """The algorithms current portfolio state"""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the AlphaResultPacket class"""
        ...

    @overload
    def __init__(self, algorithmId: str, userId: int, insights: System.Collections.Generic.List[QuantConnect.Algorithm.Framework.Alphas.Insight] = None, orderEvents: System.Collections.Generic.List[QuantConnect.Orders.OrderEvent] = None, orders: System.Collections.Generic.List[QuantConnect.Orders.Order] = None, portfolio: QuantConnect.Data.Custom.AlphaStreams.AlphaStreamsPortfolioState = None) -> None:
        """
        Initializes a new instance of the AlphaResultPacket class
        
        :param algorithmId: The algorithm's unique identifier
        :param userId: The user's id
        :param insights: Alphas generated by the algorithm
        :param orderEvents: OrderEvents generated by the algorithm
        :param orders: Orders generated or updated by the algorithm
        :param portfolio: The algorithms current portfolio state
        """
        ...


class BacktestResult(QuantConnect.Result):
    """Backtest results object class - result specific items from the packet."""

    @property
    def RollingWindow(self) -> System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance]:
        """Rolling window detailed statistics."""
        ...

    @RollingWindow.setter
    def RollingWindow(self, value: System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance]):
        """Rolling window detailed statistics."""
        ...

    @property
    def TotalPerformance(self) -> QuantConnect.Statistics.AlgorithmPerformance:
        """Rolling window detailed statistics."""
        ...

    @TotalPerformance.setter
    def TotalPerformance(self, value: QuantConnect.Statistics.AlgorithmPerformance):
        """Rolling window detailed statistics."""
        ...

    @overload
    def __init__(self) -> None:
        """Default Constructor"""
        ...

    @overload
    def __init__(self, parameters: QuantConnect.Packets.BacktestResultParameters) -> None:
        """Constructor for the result class using dictionary objects."""
        ...


class BacktestNodePacket(QuantConnect.Packets.AlgorithmNodePacket):
    """Algorithm backtest task information packet."""

    @property
    def Name(self) -> str:
        """Name of the backtest as randomly defined in the IDE."""
        ...

    @Name.setter
    def Name(self, value: str):
        """Name of the backtest as randomly defined in the IDE."""
        ...

    @property
    def BacktestId(self) -> str:
        """BacktestId / Algorithm Id for this task"""
        ...

    @BacktestId.setter
    def BacktestId(self, value: str):
        """BacktestId / Algorithm Id for this task"""
        ...

    @property
    def OptimizationId(self) -> str:
        """Optimization Id for this task"""
        ...

    @OptimizationId.setter
    def OptimizationId(self, value: str):
        """Optimization Id for this task"""
        ...

    @property
    def PeriodStart(self) -> typing.Optional[datetime.datetime]:
        """Backtest start-date as defined in the Initialize() method."""
        ...

    @PeriodStart.setter
    def PeriodStart(self, value: typing.Optional[datetime.datetime]):
        """Backtest start-date as defined in the Initialize() method."""
        ...

    @property
    def PeriodFinish(self) -> typing.Optional[datetime.datetime]:
        """Backtest end date as defined in the Initialize() method."""
        ...

    @PeriodFinish.setter
    def PeriodFinish(self, value: typing.Optional[datetime.datetime]):
        """Backtest end date as defined in the Initialize() method."""
        ...

    @property
    def TradeableDates(self) -> int:
        """Estimated number of trading days in this backtest task based on the start-end dates."""
        ...

    @TradeableDates.setter
    def TradeableDates(self, value: int):
        """Estimated number of trading days in this backtest task based on the start-end dates."""
        ...

    @property
    def IsDebugging(self) -> bool:
        """True, if this is a debugging backtest"""
        ...

    @IsDebugging.setter
    def IsDebugging(self, value: bool):
        """True, if this is a debugging backtest"""
        ...

    @property
    def CashAmount(self) -> typing.Optional[QuantConnect.Securities.CashAmount]:
        """Optional initial cash amount if set"""
        ...

    @CashAmount.setter
    def CashAmount(self, value: typing.Optional[QuantConnect.Securities.CashAmount]):
        """Optional initial cash amount if set"""
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, userId: int, projectId: int, sessionId: str, algorithmData: typing.List[int], startingCapital: float, name: str) -> None:
        """Initialize the backtest task packet."""
        ...

    @overload
    def __init__(self, userId: int, projectId: int, sessionId: str, algorithmData: typing.List[int], name: str, startingCapital: typing.Optional[QuantConnect.Securities.CashAmount] = None) -> None:
        """Initialize the backtest task packet."""
        ...


class BacktestResultPacket(QuantConnect.Packets.Packet):
    """Backtest result packet: send backtest information to GUI for user consumption."""

    @property
    def UserId(self) -> int:
        """User Id placing this task"""
        ...

    @UserId.setter
    def UserId(self, value: int):
        """User Id placing this task"""
        ...

    @property
    def ProjectId(self) -> int:
        """Project Id of the this task."""
        ...

    @ProjectId.setter
    def ProjectId(self, value: int):
        """Project Id of the this task."""
        ...

    @property
    def SessionId(self) -> str:
        """User Session Id"""
        ...

    @SessionId.setter
    def SessionId(self, value: str):
        """User Session Id"""
        ...

    @property
    def BacktestId(self) -> str:
        """BacktestId for this result packet"""
        ...

    @BacktestId.setter
    def BacktestId(self, value: str):
        """BacktestId for this result packet"""
        ...

    @property
    def OptimizationId(self) -> str:
        """OptimizationId for this result packet if any"""
        ...

    @OptimizationId.setter
    def OptimizationId(self, value: str):
        """OptimizationId for this result packet if any"""
        ...

    @property
    def CompileId(self) -> str:
        """Compile Id for the algorithm which generated this result packet."""
        ...

    @CompileId.setter
    def CompileId(self, value: str):
        """Compile Id for the algorithm which generated this result packet."""
        ...

    @property
    def PeriodStart(self) -> datetime.datetime:
        """Start of the backtest period as defined in Initialize() method."""
        ...

    @PeriodStart.setter
    def PeriodStart(self, value: datetime.datetime):
        """Start of the backtest period as defined in Initialize() method."""
        ...

    @property
    def PeriodFinish(self) -> datetime.datetime:
        """End of the backtest period as defined in the Initialize() method."""
        ...

    @PeriodFinish.setter
    def PeriodFinish(self, value: datetime.datetime):
        """End of the backtest period as defined in the Initialize() method."""
        ...

    @property
    def DateRequested(self) -> datetime.datetime:
        """DateTime (EST) the user requested this backtest."""
        ...

    @DateRequested.setter
    def DateRequested(self, value: datetime.datetime):
        """DateTime (EST) the user requested this backtest."""
        ...

    @property
    def DateFinished(self) -> datetime.datetime:
        """DateTime (EST) when the backtest was completed."""
        ...

    @DateFinished.setter
    def DateFinished(self, value: datetime.datetime):
        """DateTime (EST) when the backtest was completed."""
        ...

    @property
    def Progress(self) -> float:
        """Progress of the backtest as a percentage from 0-1 based on the days lapsed from start-finish."""
        ...

    @Progress.setter
    def Progress(self, value: float):
        """Progress of the backtest as a percentage from 0-1 based on the days lapsed from start-finish."""
        ...

    @property
    def Name(self) -> str:
        """Name of this backtest."""
        ...

    @Name.setter
    def Name(self, value: str):
        """Name of this backtest."""
        ...

    @property
    def Results(self) -> QuantConnect.Packets.BacktestResult:
        """Result data object for this backtest"""
        ...

    @Results.setter
    def Results(self, value: QuantConnect.Packets.BacktestResult):
        """Result data object for this backtest"""
        ...

    @property
    def ProcessingTime(self) -> float:
        """Processing time of the algorithm (from moment the algorithm arrived on the algorithm node)"""
        ...

    @ProcessingTime.setter
    def ProcessingTime(self, value: float):
        """Processing time of the algorithm (from moment the algorithm arrived on the algorithm node)"""
        ...

    @property
    def TradeableDates(self) -> int:
        """Estimated number of tradeable days in the backtest based on the start and end date or the backtest"""
        ...

    @TradeableDates.setter
    def TradeableDates(self, value: int):
        """Estimated number of tradeable days in the backtest based on the start and end date or the backtest"""
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON Serialization"""
        ...

    @overload
    def __init__(self, json: str) -> None:
        """Compose the packet from a JSON string:"""
        ...

    @overload
    def __init__(self, job: QuantConnect.Packets.BacktestNodePacket, results: QuantConnect.Packets.BacktestResult, endDate: typing.Union[datetime.datetime, datetime.date], startDate: typing.Union[datetime.datetime, datetime.date], progress: float = 1) -> None:
        """
        Compose result data packet - with tradable dates from the backtest job task and the partial result packet.
        
        :param job: Job that started this request
        :param results: Results class for the Backtest job
        :param endDate: The algorithms backtest end date
        :param startDate: The algorithms backtest start date
        :param progress: Progress of the packet. For the packet we assume progess of 100%.
        """
        ...

    @staticmethod
    def CreateEmpty(job: QuantConnect.Packets.BacktestNodePacket) -> QuantConnect.Packets.BacktestResultPacket:
        """
        Creates an empty result packet, useful when the algorithm fails to initialize
        
        :param job: The associated job packet
        :returns: An empty result packet.
        """
        ...


class HandledErrorPacket(QuantConnect.Packets.Packet):
    """
    Algorithm runtime error packet from the lean engine.
    This is a managed error which stops the algorithm execution.
    """

    @property
    def Message(self) -> str:
        """Runtime error message from the exception"""
        ...

    @Message.setter
    def Message(self, value: str):
        """Runtime error message from the exception"""
        ...

    @property
    def AlgorithmId(self) -> str:
        """Algorithm id which generated this runtime error"""
        ...

    @AlgorithmId.setter
    def AlgorithmId(self, value: str):
        """Algorithm id which generated this runtime error"""
        ...

    @property
    def StackTrace(self) -> str:
        """Error stack trace information string passed through from the Lean exception"""
        ...

    @StackTrace.setter
    def StackTrace(self, value: str):
        """Error stack trace information string passed through from the Lean exception"""
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor for JSON"""
        ...

    @overload
    def __init__(self, algorithmId: str, message: str, stacktrace: str = ...) -> None:
        """Create a new handled error packet"""
        ...


