from typing import overload
import datetime
import typing

import QuantConnect
import QuantConnect.Api
import QuantConnect.Interfaces
import QuantConnect.Notifications
import QuantConnect.Optimizer.Objectives
import QuantConnect.Optimizer.Parameters
import QuantConnect.Orders
import QuantConnect.Packets
import QuantConnect.Statistics
import System
import System.Collections.Generic
import System.Text.RegularExpressions

JsonConverter = typing.Any

QuantConnect_Api_ApiConnection_TryRequest_T = typing.TypeVar("QuantConnect_Api_ApiConnection_TryRequest_T")


class ApiConnection(System.Object):
    """API Connection and Hash Manager"""

    @property
    def Client(self) -> typing.Any:
        """Authorized client to use for requests."""
        ...

    @Client.setter
    def Client(self, value: typing.Any):
        """Authorized client to use for requests."""
        ...

    @property
    def Connected(self) -> bool:
        """Return true if connected successfully."""
        ...

    def __init__(self, userId: int, token: str) -> None:
        """
        Create a new Api Connection Class.
        
        :param userId: User Id number from QuantConnect.com account. Found at www.quantconnect.com/account
        :param token: Access token for the QuantConnect account. Found at www.quantconnect.com/account
        """
        ...

    def TryRequest(self, request: typing.Any, result: typing.Optional[QuantConnect_Api_ApiConnection_TryRequest_T]) -> typing.Union[bool, QuantConnect_Api_ApiConnection_TryRequest_T]:
        """
        Place a secure request and get back an object of type T.
        
        :param result: Result object from the
        :returns: T typed object response.
        """
        ...


class RestResponse(System.Object):
    """Base API response class for the QuantConnect API."""

    @property
    def Success(self) -> bool:
        """Indicate if the API request was successful."""
        ...

    @Success.setter
    def Success(self, value: bool):
        """Indicate if the API request was successful."""
        ...

    @property
    def Errors(self) -> System.Collections.Generic.List[str]:
        """List of errors with the API call."""
        ...

    @Errors.setter
    def Errors(self, value: System.Collections.Generic.List[str]):
        """List of errors with the API call."""
        ...

    def __init__(self) -> None:
        """JSON Constructor"""
        ...


class Project(QuantConnect.Api.RestResponse):
    """Response from reading a project by id."""

    @property
    def ProjectId(self) -> int:
        """Project id"""
        ...

    @ProjectId.setter
    def ProjectId(self, value: int):
        """Project id"""
        ...

    @property
    def Name(self) -> str:
        """Name of the project"""
        ...

    @Name.setter
    def Name(self, value: str):
        """Name of the project"""
        ...

    @property
    def Created(self) -> datetime.datetime:
        """Date the project was created"""
        ...

    @Created.setter
    def Created(self, value: datetime.datetime):
        """Date the project was created"""
        ...

    @property
    def Modified(self) -> datetime.datetime:
        """Modified date for the project"""
        ...

    @Modified.setter
    def Modified(self, value: datetime.datetime):
        """Modified date for the project"""
        ...

    @property
    def Language(self) -> int:
        """
        Programming language of the project
        
        This property contains the int value of a member of the QuantConnect.Language enum.
        """
        ...

    @Language.setter
    def Language(self, value: int):
        """
        Programming language of the project
        
        This property contains the int value of a member of the QuantConnect.Language enum.
        """
        ...


class ProjectResponse(QuantConnect.Api.RestResponse):
    """Project list response"""

    @property
    def Projects(self) -> System.Collections.Generic.List[QuantConnect.Api.Project]:
        """List of projects for the authenticated user"""
        ...

    @Projects.setter
    def Projects(self, value: System.Collections.Generic.List[QuantConnect.Api.Project]):
        """List of projects for the authenticated user"""
        ...


class ProjectFile(System.Object):
    """File for a project"""

    @property
    def Name(self) -> str:
        """Name of a project file"""
        ...

    @Name.setter
    def Name(self, value: str):
        """Name of a project file"""
        ...

    @property
    def Code(self) -> str:
        """Contents of the project file"""
        ...

    @Code.setter
    def Code(self, value: str):
        """Contents of the project file"""
        ...

    @property
    def DateModified(self) -> datetime.datetime:
        """DateTime project file was modified"""
        ...

    @DateModified.setter
    def DateModified(self, value: datetime.datetime):
        """DateTime project file was modified"""
        ...


class ProjectFilesResponse(QuantConnect.Api.RestResponse):
    """Response received when reading all files of a project"""

    @property
    def Files(self) -> System.Collections.Generic.List[QuantConnect.Api.ProjectFile]:
        """List of project file information"""
        ...

    @Files.setter
    def Files(self, value: System.Collections.Generic.List[QuantConnect.Api.ProjectFile]):
        """List of project file information"""
        ...


class Compile(QuantConnect.Api.RestResponse):
    """Response from the compiler on a build event"""

    @property
    def CompileId(self) -> str:
        """Compile Id for a sucessful build"""
        ...

    @CompileId.setter
    def CompileId(self, value: str):
        """Compile Id for a sucessful build"""
        ...

    @property
    def State(self) -> int:
        """
        True on successful compile
        
        This property contains the int value of a member of the QuantConnect.Api.CompileState enum.
        """
        ...

    @State.setter
    def State(self, value: int):
        """
        True on successful compile
        
        This property contains the int value of a member of the QuantConnect.Api.CompileState enum.
        """
        ...

    @property
    def Logs(self) -> System.Collections.Generic.List[str]:
        """Logs of the compilation request"""
        ...

    @Logs.setter
    def Logs(self, value: System.Collections.Generic.List[str]):
        """Logs of the compilation request"""
        ...


class Backtest(QuantConnect.Api.RestResponse):
    """Backtest response packet from the QuantConnect.com API."""

    @property
    def Name(self) -> str:
        """Name of the backtest"""
        ...

    @Name.setter
    def Name(self, value: str):
        """Name of the backtest"""
        ...

    @property
    def Note(self) -> str:
        """Note on the backtest attached by the user"""
        ...

    @Note.setter
    def Note(self, value: str):
        """Note on the backtest attached by the user"""
        ...

    @property
    def BacktestId(self) -> str:
        """Assigned backtest Id"""
        ...

    @BacktestId.setter
    def BacktestId(self, value: str):
        """Assigned backtest Id"""
        ...

    @property
    def Completed(self) -> bool:
        """Boolean true when the backtest is completed."""
        ...

    @Completed.setter
    def Completed(self, value: bool):
        """Boolean true when the backtest is completed."""
        ...

    @property
    def Progress(self) -> float:
        """Progress of the backtest in percent 0-1."""
        ...

    @Progress.setter
    def Progress(self, value: float):
        """Progress of the backtest in percent 0-1."""
        ...

    @property
    def Error(self) -> str:
        """Backtest error message"""
        ...

    @Error.setter
    def Error(self, value: str):
        """Backtest error message"""
        ...

    @property
    def StackTrace(self) -> str:
        """Backtest error stacktrace"""
        ...

    @StackTrace.setter
    def StackTrace(self, value: str):
        """Backtest error stacktrace"""
        ...

    @property
    def Created(self) -> datetime.datetime:
        """Backtest creation date and time"""
        ...

    @Created.setter
    def Created(self, value: datetime.datetime):
        """Backtest creation date and time"""
        ...

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

    @property
    def AlphaRuntimeStatistics(self) -> QuantConnect.AlphaRuntimeStatistics:
        """Contains population averages scores over the life of the algorithm"""
        ...

    @AlphaRuntimeStatistics.setter
    def AlphaRuntimeStatistics(self, value: QuantConnect.AlphaRuntimeStatistics):
        """Contains population averages scores over the life of the algorithm"""
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
    def ParameterSet(self) -> QuantConnect.Optimizer.Parameters.ParameterSet:
        """Optimization parameters"""
        ...

    @ParameterSet.setter
    def ParameterSet(self, value: QuantConnect.Optimizer.Parameters.ParameterSet):
        """Optimization parameters"""
        ...


class BacktestList(QuantConnect.Api.RestResponse):
    """Collection container for a list of backtests for a project"""

    @property
    def Backtests(self) -> System.Collections.Generic.List[QuantConnect.Api.Backtest]:
        """Collection of summarized backtest objects"""
        ...

    @Backtests.setter
    def Backtests(self, value: System.Collections.Generic.List[QuantConnect.Api.Backtest]):
        """Collection of summarized backtest objects"""
        ...


class LiveAlgorithm(QuantConnect.Api.RestResponse):
    """Live algorithm instance result from the QuantConnect Rest API."""

    @property
    def ProjectId(self) -> int:
        """Project id for the live instance"""
        ...

    @ProjectId.setter
    def ProjectId(self, value: int):
        """Project id for the live instance"""
        ...

    @property
    def DeployId(self) -> str:
        """Unique live algorithm deployment identifier (similar to a backtest id)."""
        ...

    @DeployId.setter
    def DeployId(self, value: str):
        """Unique live algorithm deployment identifier (similar to a backtest id)."""
        ...

    @property
    def Status(self) -> int:
        """
        Algorithm status: running, stopped or runtime error.
        
        This property contains the int value of a member of the QuantConnect.AlgorithmStatus enum.
        """
        ...

    @Status.setter
    def Status(self, value: int):
        """
        Algorithm status: running, stopped or runtime error.
        
        This property contains the int value of a member of the QuantConnect.AlgorithmStatus enum.
        """
        ...

    @property
    def Launched(self) -> datetime.datetime:
        """Datetime the algorithm was launched in UTC."""
        ...

    @Launched.setter
    def Launched(self, value: datetime.datetime):
        """Datetime the algorithm was launched in UTC."""
        ...

    @property
    def Stopped(self) -> typing.Optional[datetime.datetime]:
        """Datetime the algorithm was stopped in UTC, null if its still running."""
        ...

    @Stopped.setter
    def Stopped(self, value: typing.Optional[datetime.datetime]):
        """Datetime the algorithm was stopped in UTC, null if its still running."""
        ...

    @property
    def Brokerage(self) -> str:
        """Brokerage"""
        ...

    @Brokerage.setter
    def Brokerage(self, value: str):
        """Brokerage"""
        ...

    @property
    def Subscription(self) -> str:
        """Chart we're subscribed to"""
        ...

    @Subscription.setter
    def Subscription(self, value: str):
        """Chart we're subscribed to"""
        ...

    @property
    def Error(self) -> str:
        """Live algorithm error message from a crash or algorithm runtime error."""
        ...

    @Error.setter
    def Error(self, value: str):
        """Live algorithm error message from a crash or algorithm runtime error."""
        ...


class BaseLiveAlgorithmSettings(System.Object):
    """Base class for settings that must be configured per Brokerage to create new algorithms via the API."""

    @property
    def Id(self) -> str:
        """'Interactive' / 'FXCM' / 'Oanda' / 'Tradier' /'PaperTrading'"""
        ...

    @Id.setter
    def Id(self, value: str):
        """'Interactive' / 'FXCM' / 'Oanda' / 'Tradier' /'PaperTrading'"""
        ...

    @property
    def User(self) -> str:
        """Username associated with brokerage"""
        ...

    @User.setter
    def User(self, value: str):
        """Username associated with brokerage"""
        ...

    @property
    def Password(self) -> str:
        """Password associated with brokerage"""
        ...

    @Password.setter
    def Password(self, value: str):
        """Password associated with brokerage"""
        ...

    @property
    def Environment(self) -> int:
        """
        'live'/'paper'
        
        This property contains the int value of a member of the QuantConnect.BrokerageEnvironment enum.
        """
        ...

    @Environment.setter
    def Environment(self, value: int):
        """
        'live'/'paper'
        
        This property contains the int value of a member of the QuantConnect.BrokerageEnvironment enum.
        """
        ...

    @property
    def Account(self) -> str:
        """Account of the associated brokerage"""
        ...

    @Account.setter
    def Account(self, value: str):
        """Account of the associated brokerage"""
        ...

    @overload
    def __init__(self, user: str, password: str, environment: QuantConnect.BrokerageEnvironment, account: str) -> None:
        """
        Constructor used by FXCM
        
        :param user: Username associated with brokerage
        :param password: Password associated with brokerage
        :param environment: 'live'/'paper'
        :param account: Account id for brokerage
        """
        ...

    @overload
    def __init__(self, user: str, password: str) -> None:
        """
        Constructor used by Interactive Brokers
        
        :param user: Username associated with brokerage
        :param password: Password associated with brokerage
        """
        ...

    @overload
    def __init__(self, environment: QuantConnect.BrokerageEnvironment, account: str) -> None:
        """
        The constructor used by Oanda
        
        :param environment: 'live'/'paper'
        :param account: Account id for brokerage
        """
        ...

    @overload
    def __init__(self, account: str) -> None:
        """
        The constructor used by Tradier
        
        :param account: Account id for brokerage
        """
        ...

    @overload
    def __init__(self) -> None:
        """The constructor used by Bitfinex"""
        ...


class LiveList(QuantConnect.Api.RestResponse):
    """List of the live algorithms running which match the requested status"""

    @property
    def Algorithms(self) -> System.Collections.Generic.List[QuantConnect.Api.LiveAlgorithm]:
        """Algorithm list matching the requested status."""
        ...

    @Algorithms.setter
    def Algorithms(self, value: System.Collections.Generic.List[QuantConnect.Api.LiveAlgorithm]):
        """Algorithm list matching the requested status."""
        ...


class LiveResultsData(System.Object):
    """Holds information about the state and operation of the live running algorithm"""

    @property
    def Version(self) -> int:
        """Results version"""
        ...

    @Version.setter
    def Version(self, value: int):
        """Results version"""
        ...

    @property
    def Resolution(self) -> int:
        """
        Temporal resolution of the results returned from the Api
        
        This property contains the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    @Resolution.setter
    def Resolution(self, value: int):
        """
        Temporal resolution of the results returned from the Api
        
        This property contains the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    @property
    def Results(self) -> QuantConnect.Packets.LiveResult:
        """Class to represent the data groups results return from the Api"""
        ...

    @Results.setter
    def Results(self, value: QuantConnect.Packets.LiveResult):
        """Class to represent the data groups results return from the Api"""
        ...


class LiveAlgorithmResults(QuantConnect.Api.RestResponse):
    """Details a live algorithm from the "live/read" Api endpoint"""

    @property
    def LiveResults(self) -> QuantConnect.Api.LiveResultsData:
        """Represents data about the live running algorithm returned from the server"""
        ...

    @LiveResults.setter
    def LiveResults(self, value: QuantConnect.Api.LiveResultsData):
        """Represents data about the live running algorithm returned from the server"""
        ...


class LiveLog(QuantConnect.Api.RestResponse):
    """Logs from a live algorithm"""

    @property
    def Logs(self) -> System.Collections.Generic.List[str]:
        """List of logs from the live algorithm"""
        ...

    @Logs.setter
    def Logs(self, value: System.Collections.Generic.List[str]):
        """List of logs from the live algorithm"""
        ...


class DataLink(QuantConnect.Api.RestResponse):
    """Data/Read response wrapper, contains link to requested data"""

    @property
    def Url(self) -> str:
        """Url to the data requested"""
        ...

    @Url.setter
    def Url(self, value: str):
        """Url to the data requested"""
        ...

    @property
    def Balance(self) -> float:
        """Remaining QCC balance on account after this transaction"""
        ...

    @Balance.setter
    def Balance(self, value: float):
        """Remaining QCC balance on account after this transaction"""
        ...

    @property
    def Cost(self) -> float:
        """QCC Cost for this data link"""
        ...

    @Cost.setter
    def Cost(self, value: float):
        """QCC Cost for this data link"""
        ...


class DataList(QuantConnect.Api.RestResponse):
    """Data/List response wrapper for available data"""

    @property
    def AvailableData(self) -> System.Collections.Generic.List[str]:
        """List of all available data from this request"""
        ...

    @AvailableData.setter
    def AvailableData(self, value: System.Collections.Generic.List[str]):
        """List of all available data from this request"""
        ...


class PriceEntry(System.Object):
    """Prices entry for Data/Prices response"""

    @property
    def Vendor(self) -> str:
        """Vendor for this price"""
        ...

    @Vendor.setter
    def Vendor(self, value: str):
        """Vendor for this price"""
        ...

    @property
    def RegEx(self) -> System.Text.RegularExpressions.Regex:
        """
        Regex for this data price entry
        Trims regex open, close, and multiline flag
        because it won't match otherwise
        """
        ...

    @property
    def RawRegEx(self) -> str:
        """RegEx directly from response"""
        ...

    @RawRegEx.setter
    def RawRegEx(self, value: str):
        """RegEx directly from response"""
        ...

    @property
    def Price(self) -> typing.Optional[int]:
        """The price for this entry in QCC"""
        ...

    @Price.setter
    def Price(self, value: typing.Optional[int]):
        """The price for this entry in QCC"""
        ...

    @property
    def Type(self) -> str:
        """The type associated to this price entry if any"""
        ...

    @Type.setter
    def Type(self, value: str):
        """The type associated to this price entry if any"""
        ...

    @property
    def Subscribed(self) -> typing.Optional[bool]:
        """True if the user is subscribed"""
        ...

    @Subscribed.setter
    def Subscribed(self, value: typing.Optional[bool]):
        """True if the user is subscribed"""
        ...

    @property
    def ProductId(self) -> int:
        """The associated product id"""
        ...

    @ProductId.setter
    def ProductId(self, value: int):
        """The associated product id"""
        ...

    @property
    def Paths(self) -> System.Collections.Generic.HashSet[str]:
        """The associated data paths"""
        ...

    @Paths.setter
    def Paths(self, value: System.Collections.Generic.HashSet[str]):
        """The associated data paths"""
        ...


class DataPricesList(QuantConnect.Api.RestResponse):
    """Data/Prices response wrapper for prices by vendor"""

    @property
    def Prices(self) -> System.Collections.Generic.List[QuantConnect.Api.PriceEntry]:
        """Collection of prices objects"""
        ...

    @Prices.setter
    def Prices(self, value: System.Collections.Generic.List[QuantConnect.Api.PriceEntry]):
        """Collection of prices objects"""
        ...

    @property
    def AgreementUrl(self) -> str:
        """The Agreement URL for this Organization"""
        ...

    @AgreementUrl.setter
    def AgreementUrl(self, value: str):
        """The Agreement URL for this Organization"""
        ...

    def GetPrice(self, path: str) -> int:
        """
        Get the price in QCC for a given data file
        
        :param path: Lean data path of the file
        :returns: QCC price for data, -1 if no entry found.
        """
        ...


class BacktestReport(QuantConnect.Api.RestResponse):
    """Backtest Report Response wrapper"""

    @property
    def Report(self) -> str:
        """HTML data of the report with embedded base64 images"""
        ...

    @Report.setter
    def Report(self, value: str):
        """HTML data of the report with embedded base64 images"""
        ...


class NodePrices(System.Object):
    """Class for deserializing node prices from node object"""

    @property
    def Monthly(self) -> int:
        """The monthly price of the node in US dollars"""
        ...

    @Monthly.setter
    def Monthly(self, value: int):
        """The monthly price of the node in US dollars"""
        ...

    @property
    def Yearly(self) -> int:
        """The yearly prices of the node in US dollars"""
        ...

    @Yearly.setter
    def Yearly(self, value: int):
        """The yearly prices of the node in US dollars"""
        ...


class Node(System.Object):
    """
    Node class built for API endpoints nodes/read and nodes/create.
    Converts JSON properties from API response into data members for the class.
    Contains all relevant information on a Node to interact through API endpoints.
    """

    @property
    def Speed(self) -> float:
        """The nodes cpu clock speed in GHz"""
        ...

    @Speed.setter
    def Speed(self, value: float):
        """The nodes cpu clock speed in GHz"""
        ...

    @property
    def Prices(self) -> QuantConnect.Api.NodePrices:
        """
        The monthly and yearly prices of the node in US dollars,
        see NodePrices for type.
        """
        ...

    @Prices.setter
    def Prices(self, value: QuantConnect.Api.NodePrices):
        """
        The monthly and yearly prices of the node in US dollars,
        see NodePrices for type.
        """
        ...

    @property
    def CpuCount(self) -> int:
        """CPU core count of node"""
        ...

    @CpuCount.setter
    def CpuCount(self, value: int):
        """CPU core count of node"""
        ...

    @property
    def Ram(self) -> float:
        """Size of RAM in Gigabytes"""
        ...

    @Ram.setter
    def Ram(self, value: float):
        """Size of RAM in Gigabytes"""
        ...

    @property
    def Name(self) -> str:
        """Name of the node"""
        ...

    @Name.setter
    def Name(self, value: str):
        """Name of the node"""
        ...

    @property
    def SKU(self) -> str:
        """Node type identifier for configuration"""
        ...

    @SKU.setter
    def SKU(self, value: str):
        """Node type identifier for configuration"""
        ...

    @property
    def Description(self) -> str:
        """String description of the node"""
        ...

    @Description.setter
    def Description(self, value: str):
        """String description of the node"""
        ...

    @property
    def UsedBy(self) -> str:
        """User currently using the node"""
        ...

    @UsedBy.setter
    def UsedBy(self, value: str):
        """User currently using the node"""
        ...

    @property
    def ProjectName(self) -> str:
        """Project the node is being used for"""
        ...

    @ProjectName.setter
    def ProjectName(self, value: str):
        """Project the node is being used for"""
        ...

    @property
    def Busy(self) -> bool:
        """Boolean if the node is currently busy"""
        ...

    @Busy.setter
    def Busy(self, value: bool):
        """Boolean if the node is currently busy"""
        ...

    @property
    def Id(self) -> str:
        """Full ID of node"""
        ...

    @Id.setter
    def Id(self, value: str):
        """Full ID of node"""
        ...


class CreatedNode(QuantConnect.Api.RestResponse):
    """
    Rest api response wrapper for node/create, reads in the nodes information into a
    node object
    """

    @property
    def Node(self) -> QuantConnect.Api.Node:
        """The created node from node/create"""
        ...

    @Node.setter
    def Node(self, value: QuantConnect.Api.Node):
        """The created node from node/create"""
        ...


class NodeType(System.Enum):
    """
    NodeTypes enum for all possible options of target environments
    Used in conjuction with SKU class as a NodeType is a required parameter for SKU
    """

    Backtest = 0

    Research = 1

    Live = 2


class SKU(System.Object):
    """
    Class for generating a SKU for a node with a given configuration
    Every SKU is made up of 3 variables:
    - Target environment (L for live, B for Backtest, R for Research)
    - CPU core count
    - Dedicated RAM (GB)
    """

    @property
    def Cores(self) -> int:
        """The number of CPU cores in the node"""
        ...

    @Cores.setter
    def Cores(self, value: int):
        """The number of CPU cores in the node"""
        ...

    @property
    def Memory(self) -> int:
        """Size of RAM in GB of the Node"""
        ...

    @Memory.setter
    def Memory(self, value: int):
        """Size of RAM in GB of the Node"""
        ...

    @property
    def Target(self) -> int:
        """
        Target environment for the node
        
        This property contains the int value of a member of the QuantConnect.Api.NodeType enum.
        """
        ...

    @Target.setter
    def Target(self, value: int):
        """
        Target environment for the node
        
        This property contains the int value of a member of the QuantConnect.Api.NodeType enum.
        """
        ...

    def __init__(self, cores: int, memory: int, target: QuantConnect.Api.NodeType) -> None:
        """
        Constructs a SKU object out of the provided node configuration
        
        :param cores: Number of cores
        :param memory: Size of RAM in GBs
        :param target: Target Environment Live/Backtest/Research
        """
        ...

    def ToString(self) -> str:
        """
        Generates the SKU string for API calls based on the specifications of the node
        
        :returns: String representation of the SKU.
        """
        ...


class NodeList(QuantConnect.Api.RestResponse):
    """
    Rest api response wrapper for node/read, contains sets of node lists for each
    target environment. List are composed of Node objects.
    """

    @property
    def BacktestNodes(self) -> System.Collections.Generic.List[QuantConnect.Api.Node]:
        """Collection of backtest nodes"""
        ...

    @BacktestNodes.setter
    def BacktestNodes(self, value: System.Collections.Generic.List[QuantConnect.Api.Node]):
        """Collection of backtest nodes"""
        ...

    @property
    def ResearchNodes(self) -> System.Collections.Generic.List[QuantConnect.Api.Node]:
        """Collection of research nodes"""
        ...

    @ResearchNodes.setter
    def ResearchNodes(self, value: System.Collections.Generic.List[QuantConnect.Api.Node]):
        """Collection of research nodes"""
        ...

    @property
    def LiveNodes(self) -> System.Collections.Generic.List[QuantConnect.Api.Node]:
        """Collection of live nodes"""
        ...

    @LiveNodes.setter
    def LiveNodes(self, value: System.Collections.Generic.List[QuantConnect.Api.Node]):
        """Collection of live nodes"""
        ...


class Card(System.Object):
    """Credit card"""

    @property
    def Brand(self) -> str:
        """Credit card brand"""
        ...

    @Brand.setter
    def Brand(self, value: str):
        """Credit card brand"""
        ...

    @property
    def Expiration(self) -> datetime.datetime:
        """The credit card expiration"""
        ...

    @Expiration.setter
    def Expiration(self, value: datetime.datetime):
        """The credit card expiration"""
        ...

    @property
    def LastFourDigits(self) -> float:
        """The last 4 digits of the card"""
        ...

    @LastFourDigits.setter
    def LastFourDigits(self, value: float):
        """The last 4 digits of the card"""
        ...


class Account(QuantConnect.Api.RestResponse):
    """Account information for an organization"""

    @property
    def OrganizationId(self) -> str:
        """The organization Id"""
        ...

    @OrganizationId.setter
    def OrganizationId(self, value: str):
        """The organization Id"""
        ...

    @property
    def CreditBalance(self) -> float:
        """The current account balance"""
        ...

    @CreditBalance.setter
    def CreditBalance(self, value: float):
        """The current account balance"""
        ...

    @property
    def Card(self) -> QuantConnect.Api.Card:
        """The current organizations credit card"""
        ...

    @Card.setter
    def Card(self, value: QuantConnect.Api.Card):
        """The current organizations credit card"""
        ...


class DataAgreement(System.Object):
    """Organization Data Agreement"""

    @property
    def EpochSignedTime(self) -> typing.Optional[int]:
        """Epoch time the Data Agreement was Signed"""
        ...

    @EpochSignedTime.setter
    def EpochSignedTime(self, value: typing.Optional[int]):
        """Epoch time the Data Agreement was Signed"""
        ...

    @property
    def SignedTime(self) -> typing.Optional[datetime.datetime]:
        """
        DateTime the agreement was signed.
        Uses EpochSignedTime converted to a standard datetime.
        """
        ...

    @property
    def Signed(self) -> bool:
        """True/False if it is currently signed"""
        ...

    @Signed.setter
    def Signed(self, value: bool):
        """True/False if it is currently signed"""
        ...


class Credit(System.Object):
    """Organization Credit Object"""

    class Movement(System.Object):
        """Represents a change in organization credit"""

        @property
        def Date(self) -> datetime.datetime:
            """Date of the change in credit"""
            ...

        @Date.setter
        def Date(self, value: datetime.datetime):
            """Date of the change in credit"""
            ...

        @property
        def Description(self) -> str:
            """Credit description"""
            ...

        @Description.setter
        def Description(self, value: str):
            """Credit description"""
            ...

        @property
        def Amount(self) -> float:
            """Amount of change"""
            ...

        @Amount.setter
        def Amount(self, value: float):
            """Amount of change"""
            ...

        @property
        def Balance(self) -> float:
            """Ending Balance in QCC after Movement"""
            ...

        @Balance.setter
        def Balance(self, value: float):
            """Ending Balance in QCC after Movement"""
            ...

    @property
    def Balance(self) -> float:
        """QCC Current Balance"""
        ...

    @Balance.setter
    def Balance(self, value: float):
        """QCC Current Balance"""
        ...

    @property
    def Movements(self) -> System.Collections.Generic.List[QuantConnect.Api.Credit.Movement]:
        """List of changes to Credit"""
        ...

    @Movements.setter
    def Movements(self, value: System.Collections.Generic.List[QuantConnect.Api.Credit.Movement]):
        """List of changes to Credit"""
        ...


class AlphaLicense(System.Object):
    """An alpha license"""

    @property
    def Shares(self) -> float:
        """Allocated shares"""
        ...

    @Shares.setter
    def Shares(self, value: float):
        """Allocated shares"""
        ...

    @property
    def AlphaId(self) -> str:
        """Gets or sets the alpha id"""
        ...

    @AlphaId.setter
    def AlphaId(self, value: str):
        """Gets or sets the alpha id"""
        ...

    @property
    def Start(self) -> datetime.datetime:
        """The start time of this license"""
        ...

    @Start.setter
    def Start(self, value: datetime.datetime):
        """The start time of this license"""
        ...

    @property
    def End(self) -> datetime.datetime:
        """The end time of this license"""
        ...

    @End.setter
    def End(self, value: datetime.datetime):
        """The end time of this license"""
        ...


class Alpha(System.Object):
    """Alphas"""

    @property
    def Licenses(self) -> System.Collections.Generic.List[QuantConnect.Api.AlphaLicense]:
        """Current licensed alphas"""
        ...

    @Licenses.setter
    def Licenses(self, value: System.Collections.Generic.List[QuantConnect.Api.AlphaLicense]):
        """Current licensed alphas"""
        ...


class ProductItem(System.Object):
    """QuantConnect ProductItem"""

    @property
    def Name(self) -> str:
        """Product Type"""
        ...

    @Name.setter
    def Name(self, value: str):
        """Product Type"""
        ...

    @property
    def Quantity(self) -> int:
        """
        Collection of item subscriptions
        Nodes/Data/Seats/etc
        """
        ...

    @Quantity.setter
    def Quantity(self, value: int):
        """
        Collection of item subscriptions
        Nodes/Data/Seats/etc
        """
        ...

    @property
    def UnitPrice(self) -> int:
        """USD Unit price for this item"""
        ...

    @UnitPrice.setter
    def UnitPrice(self, value: int):
        """USD Unit price for this item"""
        ...

    @property
    def TotalPrice(self) -> int:
        """USD Total price for this product"""
        ...

    @TotalPrice.setter
    def TotalPrice(self, value: int):
        """USD Total price for this product"""
        ...

    @property
    def Id(self) -> int:
        """ID for this product"""
        ...

    @Id.setter
    def Id(self, value: int):
        """ID for this product"""
        ...


class Product(System.Object):
    """QuantConnect Products"""

    @property
    def Type(self) -> int:
        """
        Product Type
        
        This property contains the int value of a member of the QuantConnect.Api.ProductType enum.
        """
        ...

    @Type.setter
    def Type(self, value: int):
        """
        Product Type
        
        This property contains the int value of a member of the QuantConnect.Api.ProductType enum.
        """
        ...

    @property
    def Items(self) -> System.Collections.Generic.List[QuantConnect.Api.ProductItem]:
        """
        Collection of item subscriptions
        Nodes/Data/Seats/etc
        """
        ...

    @Items.setter
    def Items(self, value: System.Collections.Generic.List[QuantConnect.Api.ProductItem]):
        """
        Collection of item subscriptions
        Nodes/Data/Seats/etc
        """
        ...


class Organization(System.Object):
    """Object representation of Organization from QuantConnect Api"""

    @property
    def Id(self) -> str:
        """Organization ID; Used for API Calls"""
        ...

    @Id.setter
    def Id(self, value: str):
        """Organization ID; Used for API Calls"""
        ...

    @property
    def Seats(self) -> int:
        """Seats in Organization"""
        ...

    @Seats.setter
    def Seats(self, value: int):
        """Seats in Organization"""
        ...

    @property
    def DataAgreement(self) -> QuantConnect.Api.DataAgreement:
        """Data Agreement information"""
        ...

    @DataAgreement.setter
    def DataAgreement(self, value: QuantConnect.Api.DataAgreement):
        """Data Agreement information"""
        ...

    @property
    def Products(self) -> System.Collections.Generic.List[QuantConnect.Api.Product]:
        """Organization Product Subscriptions"""
        ...

    @Products.setter
    def Products(self, value: System.Collections.Generic.List[QuantConnect.Api.Product]):
        """Organization Product Subscriptions"""
        ...

    @property
    def Credit(self) -> QuantConnect.Api.Credit:
        """Organization Credit Balance and Transactions"""
        ...

    @Credit.setter
    def Credit(self, value: QuantConnect.Api.Credit):
        """Organization Credit Balance and Transactions"""
        ...

    @property
    def Alpha(self) -> QuantConnect.Api.Alpha:
        """Alphas"""
        ...

    @Alpha.setter
    def Alpha(self, value: QuantConnect.Api.Alpha):
        """Alphas"""
        ...


class Estimate(System.Object):
    """Estimate response packet from the QuantConnect.com API."""

    @property
    def EstimateId(self) -> str:
        """Estimate id"""
        ...

    @EstimateId.setter
    def EstimateId(self, value: str):
        """Estimate id"""
        ...

    @property
    def Time(self) -> int:
        """Estimate time in seconds"""
        ...

    @Time.setter
    def Time(self, value: int):
        """Estimate time in seconds"""
        ...

    @property
    def Balance(self) -> int:
        """Estimate balance in QCC"""
        ...

    @Balance.setter
    def Balance(self, value: int):
        """Estimate balance in QCC"""
        ...


class BaseOptimization(QuantConnect.Api.RestResponse):
    """BaseOptimization item from the QuantConnect.com API."""

    @property
    def OptimizationId(self) -> str:
        """Optimization ID"""
        ...

    @OptimizationId.setter
    def OptimizationId(self, value: str):
        """Optimization ID"""
        ...

    @property
    def ProjectId(self) -> int:
        """Project ID of the project the optimization belongs to"""
        ...

    @ProjectId.setter
    def ProjectId(self, value: int):
        """Project ID of the project the optimization belongs to"""
        ...

    @property
    def Name(self) -> str:
        """Name of the optimization"""
        ...

    @Name.setter
    def Name(self, value: str):
        """Name of the optimization"""
        ...

    @property
    def Status(self) -> int:
        """
        Status of the optimization
        
        This property contains the int value of a member of the QuantConnect.Optimizer.OptimizationStatus enum.
        """
        ...

    @Status.setter
    def Status(self, value: int):
        """
        Status of the optimization
        
        This property contains the int value of a member of the QuantConnect.Optimizer.OptimizationStatus enum.
        """
        ...

    @property
    def NodeType(self) -> str:
        """Optimization node type"""
        ...

    @NodeType.setter
    def NodeType(self, value: str):
        """Optimization node type"""
        ...

    @property
    def Criterion(self) -> QuantConnect.Optimizer.Objectives.Target:
        """Optimization statistical target"""
        ...

    @Criterion.setter
    def Criterion(self, value: QuantConnect.Optimizer.Objectives.Target):
        """Optimization statistical target"""
        ...


class OptimizationBacktest(System.Object):
    """OptimizationBacktest object from the QuantConnect.com API."""

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
        """The backtest name"""
        ...

    @property
    def HostName(self) -> str:
        """The backtest host name"""
        ...

    @HostName.setter
    def HostName(self, value: str):
        """The backtest host name"""
        ...

    @property
    def BacktestId(self) -> str:
        """The backtest id"""
        ...

    @property
    def ParameterSet(self) -> QuantConnect.Optimizer.Parameters.ParameterSet:
        """Represent a combination as key value of parameters, i.e. order doesn't matter"""
        ...

    @property
    def Statistics(self) -> System.Collections.Generic.IDictionary[str, str]:
        """The backtest statistics results"""
        ...

    @Statistics.setter
    def Statistics(self, value: System.Collections.Generic.IDictionary[str, str]):
        """The backtest statistics results"""
        ...

    @property
    def Equity(self) -> QuantConnect.Series:
        """The backtest equity chart series"""
        ...

    @Equity.setter
    def Equity(self, value: QuantConnect.Series):
        """The backtest equity chart series"""
        ...

    @property
    def ExitCode(self) -> int:
        """The exit code of this backtest"""
        ...

    @ExitCode.setter
    def ExitCode(self, value: int):
        """The exit code of this backtest"""
        ...

    def __init__(self, parameterSet: QuantConnect.Optimizer.Parameters.ParameterSet, backtestId: str, name: str) -> None:
        """
        Creates a new instance
        
        :param parameterSet: The parameter set
        :param backtestId: The backtest id if any
        :param name: The backtest name
        """
        ...


class Optimization(QuantConnect.Api.BaseOptimization):
    """Optimization response packet from the QuantConnect.com API."""

    @property
    def RuntimeStatistics(self) -> System.Collections.Generic.IDictionary[str, str]:
        """Runtime banner/updating statistics for the optimization"""
        ...

    @RuntimeStatistics.setter
    def RuntimeStatistics(self, value: System.Collections.Generic.IDictionary[str, str]):
        """Runtime banner/updating statistics for the optimization"""
        ...

    @property
    def Constraints(self) -> System.Collections.Generic.IReadOnlyList[QuantConnect.Optimizer.Objectives.Constraint]:
        """Optimization constraints"""
        ...

    @Constraints.setter
    def Constraints(self, value: System.Collections.Generic.IReadOnlyList[QuantConnect.Optimizer.Objectives.Constraint]):
        """Optimization constraints"""
        ...

    @property
    def Parameters(self) -> System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter]:
        """Optimization parameters"""
        ...

    @Parameters.setter
    def Parameters(self, value: System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter]):
        """Optimization parameters"""
        ...

    @property
    def ParallelNodes(self) -> int:
        """Number of parallel nodes for optimization"""
        ...

    @ParallelNodes.setter
    def ParallelNodes(self, value: int):
        """Number of parallel nodes for optimization"""
        ...

    @property
    def Backtests(self) -> System.Collections.Generic.IDictionary[str, QuantConnect.Api.OptimizationBacktest]:
        """Optimization constraints"""
        ...

    @Backtests.setter
    def Backtests(self, value: System.Collections.Generic.IDictionary[str, QuantConnect.Api.OptimizationBacktest]):
        """Optimization constraints"""
        ...

    @property
    def Strategy(self) -> str:
        """Optimization strategy"""
        ...

    @Strategy.setter
    def Strategy(self, value: str):
        """Optimization strategy"""
        ...

    @property
    def Requested(self) -> datetime.datetime:
        """Optimization requested date and time"""
        ...

    @Requested.setter
    def Requested(self, value: datetime.datetime):
        """Optimization requested date and time"""
        ...


class Api(System.Object, QuantConnect.Interfaces.IApi, QuantConnect.Interfaces.IDownloadProvider):
    """QuantConnect.com Interaction Via API."""

    @property
    def ApiConnection(self) -> QuantConnect.Api.ApiConnection:
        """
        Returns the underlying API connection
        
        This property is protected.
        """
        ...

    @ApiConnection.setter
    def ApiConnection(self, value: QuantConnect.Api.ApiConnection):
        """
        Returns the underlying API connection
        
        This property is protected.
        """
        ...

    @property
    def Connected(self) -> bool:
        """Check if Api is successfully connected with correct credentials"""
        ...

    def AbortOptimization(self, optimizationId: str) -> QuantConnect.Api.RestResponse:
        """
        Abort an optimization
        
        :param optimizationId: Optimization id for the optimization we want to abort
        :returns: RestResponse.
        """
        ...

    def AddProjectFile(self, projectId: int, name: str, content: str) -> QuantConnect.Api.ProjectFilesResponse:
        """
        Add a file to a project
        
        :param projectId: The project to which the file should be added
        :param name: The name of the new file
        :param content: The content of the new file
        :returns: ProjectFilesResponse that includes information about the newly created file.
        """
        ...

    def CreateBacktest(self, projectId: int, compileId: str, backtestName: str) -> QuantConnect.Api.Backtest:
        """
        Create a new backtest request and get the id.
        
        :param projectId: Id for the project to backtest
        :param compileId: Compile id for the project
        :param backtestName: Name for the new backtest
        :returns: Backtestt.
        """
        ...

    def CreateCompile(self, projectId: int) -> QuantConnect.Api.Compile:
        """
        Create a new compile job request for this project id.
        
        :param projectId: Project id we wish to compile.
        :returns: Compile object result.
        """
        ...

    def CreateLiveAlgorithm(self, projectId: int, compileId: str, nodeId: str, baseLiveAlgorithmSettings: QuantConnect.Api.BaseLiveAlgorithmSettings, versionId: str = "-1") -> QuantConnect.Api.LiveAlgorithm:
        """
        Create a live algorithm.
        
        :param projectId: Id of the project on QuantConnect
        :param compileId: Id of the compilation on QuantConnect
        :param nodeId: Id of the node that will run the algorithm
        :param baseLiveAlgorithmSettings: Brokerage specific BaseLiveAlgorithmSettings.
        :param versionId: The version of the Lean used to run the algorithm.                         -1 is master, however, sometimes this can create problems with live deployments.                         If you experience problems using, try specifying the version of Lean you would like to use.
        :returns: Information regarding the new algorithm LiveAlgorithm.
        """
        ...

    def CreateNode(self, name: str, organizationId: str, sku: QuantConnect.Api.SKU) -> QuantConnect.Api.CreatedNode:
        """
        Create a new node in the organization, node configuration is defined by the
        SKU
        
        :param name: The name of the new node
        :param organizationId: ID of the organization
        :param sku: SKU Object representing configuration
        :returns: Returns CreatedNode which contains API response and Node.
        """
        ...

    def CreateOptimization(self, projectId: int, name: str, target: str, targetTo: str, targetValue: typing.Optional[float], strategy: str, compileId: str, parameters: System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter], constraints: System.Collections.Generic.IReadOnlyList[QuantConnect.Optimizer.Objectives.Constraint], estimatedCost: float, nodeType: str, parallelNodes: int) -> QuantConnect.Api.BaseOptimization:
        """
        Create an optimization with the specified parameters via QuantConnect.com API
        
        :param projectId: Project ID of the project the optimization belongs to
        :param name: Name of the optimization
        :param target: Target of the optimization, see examples in PortfolioStatistics
        :param targetTo: Target extremum of the optimization, for example "max" or "min"
        :param targetValue: Optimization target value
        :param strategy: Optimization strategy, GridSearchOptimizationStrategy
        :param compileId: Optimization compile ID
        :param parameters: Optimization parameters
        :param constraints: Optimization constraints
        :param estimatedCost: Estimated cost for optimization
        :param nodeType: Optimization node type OptimizationNodes
        :param parallelNodes: Number of parallel nodes for optimization
        :returns: BaseOptimization object from the API.
        """
        ...

    def CreateProject(self, name: str, language: QuantConnect.Language, organizationId: str = None) -> QuantConnect.Api.ProjectResponse:
        """
        Create a project with the specified name and language via QuantConnect.com API
        
        :param name: Project name
        :param language: Programming language to use
        :param organizationId: Optional param for specifying organization to create project under. If none provided web defaults to preferred.
        :returns: Project object from the API.
        """
        ...

    @staticmethod
    def CreateSecureHash(timestamp: int, token: str) -> str:
        """
        Generate a secure hash for the authorization headers.
        
        :returns: Time based hash of user token and timestamp.
        """
        ...

    def DeleteBacktest(self, projectId: int, backtestId: str) -> QuantConnect.Api.RestResponse:
        """
        Delete a backtest from the specified project and backtestId.
        
        :param projectId: Project for the backtest we want to delete
        :param backtestId: Backtest id we want to delete
        :returns: RestResponse.
        """
        ...

    def DeleteNode(self, nodeId: str, organizationId: str) -> QuantConnect.Api.RestResponse:
        """
        Delete a node from an organization, requires node ID.
        
        :param nodeId: The node ID of the node you want to delete
        :param organizationId: ID of the organization
        :returns: RestResponse containing success response and errors.
        """
        ...

    def DeleteOptimization(self, optimizationId: str) -> QuantConnect.Api.RestResponse:
        """
        Delete an optimization
        
        :param optimizationId: Optimization id for the optimization we want to delete
        :returns: RestResponse.
        """
        ...

    def DeleteProject(self, projectId: int) -> QuantConnect.Api.RestResponse:
        """
        Delete a project
        
        :param projectId: Project id we own and wish to delete
        :returns: RestResponse indicating success.
        """
        ...

    def DeleteProjectFile(self, projectId: int, name: str) -> QuantConnect.Api.RestResponse:
        """
        Delete a file in a project
        
        :param projectId: Project id to which the file belongs
        :param name: The name of the file that should be deleted
        :returns: ProjectFilesResponse that includes the information about all files in the project.
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def Download(self, address: str, headers: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[str, str]], userName: str, password: str) -> str:
        """
        Local implementation for downloading data to algorithms
        
        :param address: URL to download
        :param headers: KVP headers
        :param userName: Username for basic authentication
        :param password: Password for basic authentication
        """
        ...

    def DownloadData(self, filePath: str, organizationId: str) -> bool:
        """
        Method to purchase and download data from QuantConnect
        
        :param filePath: File path representing the data requested
        :param organizationId: Organization to buy the data with
        :returns: A bool indicating whether the data was successfully downloaded or not.
        """
        ...

    def EstimateOptimization(self, projectId: int, name: str, target: str, targetTo: str, targetValue: typing.Optional[float], strategy: str, compileId: str, parameters: System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter], constraints: System.Collections.Generic.IReadOnlyList[QuantConnect.Optimizer.Objectives.Constraint]) -> QuantConnect.Api.Estimate:
        """
        Estimate optimization with the specified parameters via QuantConnect.com API
        
        :param projectId: Project ID of the project the optimization belongs to
        :param name: Name of the optimization
        :param target: Target of the optimization, see examples in PortfolioStatistics
        :param targetTo: Target extremum of the optimization, for example "max" or "min"
        :param targetValue: Optimization target value
        :param strategy: Optimization strategy, GridSearchOptimizationStrategy
        :param compileId: Optimization compile ID
        :param parameters: Optimization parameters
        :param constraints: Optimization constraints
        :returns: Estimate object from the API.
        """
        ...

    @staticmethod
    def FormatPathForDataRequest(filePath: str, dataFolder: str = None) -> str:
        """
        Helper method to normalize path for api data requests
        
        :param filePath: Filepath to format
        :param dataFolder: The data folder to use
        :returns: Normalized path.
        """
        ...

    def GetAlgorithmStatus(self, algorithmId: str) -> QuantConnect.AlgorithmControl:
        """
        Get the algorithm status from the user with this algorithm id.
        
        :param algorithmId: String algorithm id we're searching for.
        :returns: Algorithm status enum.
        """
        ...

    def Initialize(self, userId: int, token: str, dataFolder: str) -> None:
        """Initialize the API with the given variables"""
        ...

    def LiquidateLiveAlgorithm(self, projectId: int) -> QuantConnect.Api.RestResponse:
        """
        Liquidate a live algorithm from the specified project and deployId.
        
        :param projectId: Project for the live instance we want to stop
        :returns: RestResponse.
        """
        ...

    def ListBacktests(self, projectId: int) -> QuantConnect.Api.BacktestList:
        """
        List all the backtests for a project
        
        :param projectId: Project id we'd like to get a list of backtest for
        :returns: BacktestList.
        """
        ...

    def ListLiveAlgorithms(self, status: typing.Optional[QuantConnect.AlgorithmStatus] = None, startTime: typing.Optional[datetime.datetime] = None, endTime: typing.Optional[datetime.datetime] = None) -> QuantConnect.Api.LiveList:
        """
        Get a list of live running algorithms for user
        
        :param status: Filter the statuses of the algorithms returned from the api
        :param startTime: Earliest launched time of the algorithms returned by the Api
        :param endTime: Latest launched time of the algorithms returned by the Api
        :returns: LiveList.
        """
        ...

    def ListOptimizations(self, projectId: int) -> System.Collections.Generic.List[QuantConnect.Api.BaseOptimization]:
        """
        List all the optimizations for a project
        
        :param projectId: Project id we'd like to get a list of optimizations for
        :returns: A list of BaseOptimization objects, BaseOptimization.
        """
        ...

    def ListOrganizations(self) -> System.Collections.Generic.List[QuantConnect.Api.Organization]:
        """Get a list of organizations tied to this account"""
        ...

    def ListProjects(self) -> QuantConnect.Api.ProjectResponse:
        """
        List details of all projects
        
        :returns: ProjectResponse that contains information regarding the project.
        """
        ...

    def ReadAccount(self, organizationId: str = None) -> QuantConnect.Api.Account:
        """
        Will read the organization account status
        
        :param organizationId: The target organization id, if null will return default organization
        """
        ...

    def ReadBacktest(self, projectId: int, backtestId: str, getCharts: bool = True) -> QuantConnect.Api.Backtest:
        """
        Read out a backtest in the project id specified.
        
        :param projectId: Project id to read
        :param backtestId: Specific backtest id to read
        :param getCharts: True will return backtest charts
        :returns: Backtest.
        """
        ...

    def ReadBacktestOrders(self, projectId: int, backtestId: str, start: int = 0, end: int = 100) -> System.Collections.Generic.List[QuantConnect.Orders.Order]:
        """
        Returns the orders of the specified backtest and project id.
        
        :param projectId: Id of the project from which to read the orders
        :param backtestId: Id of the backtest from which to read the orders
        :param start: Starting index of the orders to be fetched. Required if end > 100
        :param end: Last index of the orders to be fetched. Note that end - start must be less than 100
        :returns: The list of Order.
        """
        ...

    def ReadBacktestReport(self, projectId: int, backtestId: str) -> QuantConnect.Api.BacktestReport:
        """
        Read out the report of a backtest in the project id specified.
        
        :param projectId: Project id to read
        :param backtestId: Specific backtest id to read
        :returns: BacktestReport.
        """
        ...

    def ReadCompile(self, projectId: int, compileId: str) -> QuantConnect.Api.Compile:
        """
        Read a compile packet job result.
        
        :param projectId: Project id we sent for compile
        :param compileId: Compile id return from the creation request
        :returns: Compile.
        """
        ...

    def ReadDataDirectory(self, filePath: str) -> QuantConnect.Api.DataList:
        """Get valid data entries for a given filepath from data/list"""
        ...

    def ReadDataLink(self, filePath: str, organizationId: str) -> QuantConnect.Api.DataLink:
        """
        Gets the link to the downloadable data.
        
        :param filePath: File path representing the data requested
        :param organizationId: Organization to download from
        :returns: Link to the downloadable data.
        """
        ...

    def ReadDataPrices(self, organizationId: str) -> QuantConnect.Api.DataPricesList:
        """Gets data prices from data/prices"""
        ...

    def ReadLiveAlgorithm(self, projectId: int, deployId: str) -> QuantConnect.Api.LiveAlgorithmResults:
        """
        Read out a live algorithm in the project id specified.
        
        :param projectId: Project id to read
        :param deployId: Specific instance id to read
        :returns: LiveAlgorithmResults.
        """
        ...

    def ReadLiveLogs(self, projectId: int, algorithmId: str, startTime: typing.Optional[datetime.datetime] = None, endTime: typing.Optional[datetime.datetime] = None) -> QuantConnect.Api.LiveLog:
        """
        Gets the logs of a specific live algorithm
        
        :param projectId: Project Id of the live running algorithm
        :param algorithmId: Algorithm Id of the live running algorithm
        :param startTime: No logs will be returned before this time
        :param endTime: No logs will be returned after this time
        :returns: LiveLog List of strings that represent the logs of the algorithm.
        """
        ...

    def ReadLiveOrders(self, projectId: int, start: int = 0, end: int = 100) -> System.Collections.Generic.List[QuantConnect.Orders.Order]:
        """
        Returns the orders of the specified project id live algorithm.
        
        :param projectId: Id of the project from which to read the live orders
        :param start: Starting index of the orders to be fetched. Required if end > 100
        :param end: Last index of the orders to be fetched. Note that end - start must be less than 100
        :returns: The list of Order.
        """
        ...

    def ReadNodes(self, organizationId: str) -> QuantConnect.Api.NodeList:
        """
        Reads the nodes associated with the organization, creating a
        NodeList for the response
        
        :param organizationId: ID of the organization
        :returns: NodeList containing Backtest, Research, and Live Nodes.
        """
        ...

    def ReadOptimization(self, optimizationId: str) -> QuantConnect.Api.Optimization:
        """
        Read an optimization
        
        :param optimizationId: Optimization id for the optimization we want to read
        :returns: Optimization.
        """
        ...

    def ReadOrganization(self, organizationId: str = None) -> QuantConnect.Api.Organization:
        """Fetch organization data from web API"""
        ...

    def ReadProject(self, projectId: int) -> QuantConnect.Api.ProjectResponse:
        """
        Get details about a single project
        
        :param projectId: Id of the project
        :returns: ProjectResponse that contains information regarding the project.
        """
        ...

    def ReadProjectFile(self, projectId: int, fileName: str) -> QuantConnect.Api.ProjectFilesResponse:
        """
        Read a file in a project
        
        :param projectId: Project id to which the file belongs
        :param fileName: The name of the file
        :returns: ProjectFilesResponse that includes the file information.
        """
        ...

    def ReadProjectFiles(self, projectId: int) -> QuantConnect.Api.ProjectFilesResponse:
        """
        Read all files in a project
        
        :param projectId: Project id to which the file belongs
        :returns: ProjectFilesResponse that includes the information about all files in the project.
        """
        ...

    def SendNotification(self, notification: QuantConnect.Notifications.Notification) -> QuantConnect.Api.RestResponse:
        """
        Sends a notification
        
        :param notification: The notification to send
        :returns: RestResponse containing success response and errors.
        """
        ...

    def SendStatistics(self, algorithmId: str, unrealized: float, fees: float, netProfit: float, holdings: float, equity: float, netReturn: float, volume: float, trades: int, sharpe: float) -> None:
        """
        Send the statistics to storage for performance tracking.
        
        :param algorithmId: Identifier for algorithm
        :param unrealized: Unrealized gainloss
        :param fees: Total fees
        :param netProfit: Net profi
        :param holdings: Algorithm holdings
        :param equity: Total equity
        :param netReturn: Net return for the deployment
        :param volume: Volume traded
        :param trades: Total trades since inception
        :param sharpe: Sharpe ratio since inception
        """
        ...

    def SendUserEmail(self, algorithmId: str, subject: str, body: str) -> None:
        """
        Send an email to the user associated with the specified algorithm id
        
        :param algorithmId: The algorithm id
        :param subject: The email subject
        :param body: The email message body
        """
        ...

    def SetAlgorithmStatus(self, algorithmId: str, status: QuantConnect.AlgorithmStatus, message: str = ...) -> None:
        """
        Algorithm passes back its current status to the UX.
        
        :param algorithmId: String algorithm id we're setting.
        :param status: Status of the current algorithm
        :param message: Message for the algorithm status event
        :returns: Algorithm status enum.
        """
        ...

    def StopLiveAlgorithm(self, projectId: int) -> QuantConnect.Api.RestResponse:
        """
        Stop a live algorithm from the specified project and deployId.
        
        :param projectId: Project for the live instance we want to stop
        :returns: RestResponse.
        """
        ...

    def StopNode(self, nodeId: str, organizationId: str) -> QuantConnect.Api.RestResponse:
        """
        Stop a running node in a organization
        
        :param nodeId: The node ID of the node you want to stop
        :param organizationId: ID of the organization
        :returns: RestResponse containing success response and errors.
        """
        ...

    def UpdateBacktest(self, projectId: int, backtestId: str, name: str = ..., note: str = ...) -> QuantConnect.Api.RestResponse:
        """
        Update a backtest name
        
        :param projectId: Project for the backtest we want to update
        :param backtestId: Backtest id we want to update
        :param name: Name we'd like to assign to the backtest
        :param note: Note attached to the backtest
        :returns: RestResponse.
        """
        ...

    def UpdateNode(self, nodeId: str, newName: str, organizationId: str) -> QuantConnect.Api.RestResponse:
        """
        Update an organizations node with a new name
        
        :param nodeId: The node ID of the node you want to update
        :param newName: The new name for that node
        :param organizationId: ID of the organization
        :returns: RestResponse containing success response and errors.
        """
        ...

    def UpdateOptimization(self, optimizationId: str, name: str = None) -> QuantConnect.Api.RestResponse:
        """
        Update an optimization
        
        :param optimizationId: Optimization id we want to update
        :param name: Name we'd like to assign to the optimization
        :returns: RestResponse.
        """
        ...

    def UpdateProjectFileContent(self, projectId: int, fileName: str, newFileContents: str) -> QuantConnect.Api.RestResponse:
        """
        Update the contents of a file
        
        :param projectId: Project id to which the file belongs
        :param fileName: The name of the file that should be updated
        :param newFileContents: The new contents of the file
        :returns: RestResponse indicating success.
        """
        ...

    def UpdateProjectFileName(self, projectId: int, oldFileName: str, newFileName: str) -> QuantConnect.Api.RestResponse:
        """
        Update the name of a file
        
        :param projectId: Project id to which the file belongs
        :param oldFileName: The current name of the file
        :param newFileName: The new name for the file
        :returns: RestResponse indicating success.
        """
        ...


class EstimateResponseWrapper(QuantConnect.Api.RestResponse):
    """
    Wrapper class for Optimizations/* endpoints JSON response
    Currently used by Optimizations/Estimate
    """

    @property
    def Estimate(self) -> QuantConnect.Api.Estimate:
        """Estimate object"""
        ...

    @Estimate.setter
    def Estimate(self, value: QuantConnect.Api.Estimate):
        """Estimate object"""
        ...


class LiveAlgorithmResultsJsonConverter(JsonConverter):
    """Custom JsonConverter for LiveResults data for live algorithms"""

    @property
    def CanWrite(self) -> bool:
        """Gets a value indicating whether this Newtonsoft.Json.JsonConverter can write JSON."""
        ...

    def CanConvert(self, objectType: typing.Type) -> bool:
        """
        Determines whether this instance can convert the specified object type.
        
        :param objectType: Type of the object.
        :returns: true if this instance can convert the specified object type; otherwise, false.
        """
        ...

    def ReadJson(self, reader: typing.Any, objectType: typing.Type, existingValue: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Reads the JSON representation of the object.
        
        :param reader: The Newtonsoft.Json.JsonReader to read from.
        :param objectType: Type of the object.
        :param existingValue: The existing value of object being read.
        :param serializer: The calling serializer.
        :returns: The object value.
        """
        ...

    def WriteJson(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """
        Writes the JSON representation of the object.
        
        :param writer: The Newtonsoft.Json.JsonWriter to write to.
        :param value: The value.
        :param serializer: The calling serializer.
        """
        ...


class CompileState(System.Enum):
    """State of the compilation request"""

    InQueue = 0
    """Compile waiting in the queue to be processed."""

    BuildSuccess = 1
    """Compile was built successfully"""

    BuildError = 2
    """Build error, check logs for more information"""


class OptimizationResponseWrapper(QuantConnect.Api.RestResponse):
    """Wrapper class for Optimizations/Read endpoint JSON response"""

    @property
    def Optimization(self) -> QuantConnect.Api.Optimization:
        """Optimization object"""
        ...

    @Optimization.setter
    def Optimization(self, value: QuantConnect.Api.Optimization):
        """Optimization object"""
        ...


class OptimizationList(QuantConnect.Api.RestResponse):
    """Collection container for a list of summarized optimizations for a project"""

    @property
    def Optimizations(self) -> System.Collections.Generic.List[QuantConnect.Api.BaseOptimization]:
        """Collection of summarized optimization objects"""
        ...

    @Optimizations.setter
    def Optimizations(self, value: System.Collections.Generic.List[QuantConnect.Api.BaseOptimization]):
        """Collection of summarized optimization objects"""
        ...


class LiveAlgorithmApiSettingsWrapper(System.Object):
    """Helper class to put BaseLiveAlgorithmSettings in proper format."""

    @property
    def VersionId(self) -> str:
        """-1 is master"""
        ...

    @VersionId.setter
    def VersionId(self, value: str):
        """-1 is master"""
        ...

    @property
    def ProjectId(self) -> int:
        """Project id for the live instance"""
        ...

    @ProjectId.setter
    def ProjectId(self, value: int):
        """Project id for the live instance"""
        ...

    @property
    def CompileId(self) -> str:
        """Compile Id for the live algorithm"""
        ...

    @CompileId.setter
    def CompileId(self, value: str):
        """Compile Id for the live algorithm"""
        ...

    @property
    def NodeId(self) -> str:
        """Id of the node being used to run live algorithm"""
        ...

    @NodeId.setter
    def NodeId(self, value: str):
        """Id of the node being used to run live algorithm"""
        ...

    @property
    def Brokerage(self) -> QuantConnect.Api.BaseLiveAlgorithmSettings:
        """The API expects the settings as part of a brokerage object"""
        ...

    @Brokerage.setter
    def Brokerage(self, value: QuantConnect.Api.BaseLiveAlgorithmSettings):
        """The API expects the settings as part of a brokerage object"""
        ...

    def __init__(self, projectId: int, compileId: str, nodeId: str, settings: QuantConnect.Api.BaseLiveAlgorithmSettings, version: str = "-1") -> None:
        """
        Constructor for LiveAlgorithmApiSettingsWrapper
        
        :param projectId: Id of project from QuantConnect
        :param compileId: Id of compilation of project from QuantConnect
        :param nodeId: Server type to run live Algorithm
        :param settings: BaseLiveAlgorithmSettings  for a specific brokerage
        :param version: The version identifier
        """
        ...


class DefaultLiveAlgorithmSettings(QuantConnect.Api.BaseLiveAlgorithmSettings):
    """Default live algorithm settings"""

    def __init__(self, user: str, password: str, environment: QuantConnect.BrokerageEnvironment, account: str) -> None:
        """
        Constructor for default algorithms
        
        :param user: Username associated with brokerage
        :param password: Password associated with brokerage
        :param environment: 'live'/'paper'
        :param account: Account id for brokerage
        """
        ...


class FXCMLiveAlgorithmSettings(QuantConnect.Api.BaseLiveAlgorithmSettings):
    """Algorithm setting for trading with FXCM"""

    def __init__(self, user: str, password: str, environment: QuantConnect.BrokerageEnvironment, account: str) -> None:
        """
        Contructor for live trading with FXCM
        
        :param user: Username associated with brokerage
        :param password: Password associated with brokerage
        :param environment: 'live'/'paper'
        :param account: Account id for brokerage
        """
        ...


class InteractiveBrokersLiveAlgorithmSettings(QuantConnect.Api.BaseLiveAlgorithmSettings):
    """Live algorithm settings for trading with Interactive Brokers"""

    def __init__(self, user: str, password: str, account: str) -> None:
        """
        Contructor for live trading with IB.
        
        :param user: Username associated with brokerage
        :param password: Password of assciate brokerage
        :param account: Account id for brokerage
        """
        ...


class OandaLiveAlgorithmSettings(QuantConnect.Api.BaseLiveAlgorithmSettings):
    """Live algorithm settings for trading with Oanda"""

    @property
    def AccessToken(self) -> str:
        """Access token for Oanda"""
        ...

    @AccessToken.setter
    def AccessToken(self, value: str):
        """Access token for Oanda"""
        ...

    @property
    def DateIssued(self) -> str:
        """Date token was issued"""
        ...

    @DateIssued.setter
    def DateIssued(self, value: str):
        """Date token was issued"""
        ...

    def __init__(self, accessToken: str, environment: QuantConnect.BrokerageEnvironment, account: str) -> None:
        """
        Contructor for live trading with Oanda.
        
        :param accessToken: Access Token (specific for Oanda Brokerage)
        :param environment: 'live'/'paper'
        :param account: Account id for brokerage
        """
        ...


class TradierLiveAlgorithmSettings(QuantConnect.Api.BaseLiveAlgorithmSettings):
    """Live algorithm settings for trading with Tradier"""

    @property
    def AccessToken(self) -> str:
        """Access token for tradier brokerage"""
        ...

    @AccessToken.setter
    def AccessToken(self, value: str):
        """Access token for tradier brokerage"""
        ...

    @property
    def DateIssued(self) -> str:
        """Property specific to Tradier account.  See tradier account for more details."""
        ...

    @DateIssued.setter
    def DateIssued(self, value: str):
        """Property specific to Tradier account.  See tradier account for more details."""
        ...

    @property
    def RefreshToken(self) -> str:
        """Property specific to Tradier account.  See tradier account for more details."""
        ...

    @RefreshToken.setter
    def RefreshToken(self, value: str):
        """Property specific to Tradier account.  See tradier account for more details."""
        ...

    @property
    def Lifetime(self) -> str:
        """Property specific to Tradier account.  See tradier account for more details."""
        ...

    @Lifetime.setter
    def Lifetime(self, value: str):
        """Property specific to Tradier account.  See tradier account for more details."""
        ...

    def __init__(self, accessToken: str, dateIssued: str, refreshToken: str, account: str) -> None:
        """
        Contructor for live trading with Tradier.
        
        :param dateIssued: Specific for live trading with Tradier.  See Tradier account for more details.
        :param refreshToken: Specific for live trading with Tradier.  See Tradier account for more details.
        :param account: Account id for brokerage
        """
        ...


class BitfinexLiveAlgorithmSettings(QuantConnect.Api.BaseLiveAlgorithmSettings):
    """Live algorithm settings for trading with Bitfinex"""

    @property
    def Key(self) -> str:
        """Property specific to Bitfinex account. API Key"""
        ...

    @Key.setter
    def Key(self, value: str):
        """Property specific to Bitfinex account. API Key"""
        ...

    @property
    def Secret(self) -> str:
        """Property specific to Bitfinex account. API Secret Key"""
        ...

    @Secret.setter
    def Secret(self, value: str):
        """Property specific to Bitfinex account. API Secret Key"""
        ...

    def __init__(self, key: str, secret: str) -> None:
        """
        Constructor for live trading with Bitfinex
        
        :param key: Api key to Bitfinex account
        :param secret: Secret Api key to Bitfinex account
        """
        ...


class GDAXLiveAlgorithmSettings(QuantConnect.Api.BaseLiveAlgorithmSettings):
    """Live algorithm settings for trading with GDAX (Coinbase)"""

    @property
    def Key(self) -> str:
        """Property specific to GDAX account. API Key"""
        ...

    @Key.setter
    def Key(self, value: str):
        """Property specific to GDAX account. API Key"""
        ...

    @property
    def Secret(self) -> str:
        """Property specific to GDAX account. API Secret Key"""
        ...

    @Secret.setter
    def Secret(self, value: str):
        """Property specific to GDAX account. API Secret Key"""
        ...

    @property
    def Passphrase(self) -> str:
        """Property specific to GDAX account. API Passphrase"""
        ...

    @Passphrase.setter
    def Passphrase(self, value: str):
        """Property specific to GDAX account. API Passphrase"""
        ...

    def __init__(self, key: str, secret: str, passphrase: str) -> None:
        """
        Constructor for live trading with GDAX (Coinbase)
        
        :param key: Api key to GDAX account
        :param secret: Secret Api key to GDAX account
        :param passphrase: Passphrase to this API key
        """
        ...


class OrganizationResponseList(QuantConnect.Api.RestResponse):
    """
    Response wrapper for Organizations/List
    TODO: The response objects in the array do not contain all Organization Properties; do we need another wrapper object?
    """

    @property
    def List(self) -> System.Collections.Generic.List[QuantConnect.Api.Organization]:
        """List of organizations in the response"""
        ...

    @List.setter
    def List(self, value: System.Collections.Generic.List[QuantConnect.Api.Organization]):
        """List of organizations in the response"""
        ...


class OrganizationResponse(QuantConnect.Api.RestResponse):
    """Response wrapper for Organizations/Read"""

    @property
    def Organization(self) -> QuantConnect.Api.Organization:
        """Organization read from the response"""
        ...

    @Organization.setter
    def Organization(self, value: QuantConnect.Api.Organization):
        """Organization read from the response"""
        ...


class ProductType(System.Enum):
    """
    Product types offered by QuantConnect
    Used by Product class
    """

    ProfessionalSeats = 0
    """Professional Seats Subscriptions"""

    BacktestNode = 1
    """Backtest Nodes Subscriptions"""

    ResearchNode = 2
    """Research Nodes Subscriptions"""

    LiveNode = 3
    """Live Trading Nodes Subscriptions"""

    Support = 4
    """Support Subscriptions"""

    Data = 5
    """Data Subscriptions"""

    Modules = 6
    """Modules Subscriptions"""


class BacktestResponseWrapper(QuantConnect.Api.RestResponse):
    """
    Wrapper class for Backtest/* endpoints JSON response
    Currently used by Backtest/Read and Backtest/Create
    """

    @property
    def Backtest(self) -> QuantConnect.Api.Backtest:
        """Backtest Object"""
        ...

    @Backtest.setter
    def Backtest(self, value: QuantConnect.Api.Backtest):
        """Backtest Object"""
        ...


class OptimizationNodes(System.Object):
    """Supported optimization nodes"""

    O2_8: str
    """2 CPUs 8 GB ram"""

    O4_12: str
    """4 CPUs 12 GB ram"""

    O8_16: str
    """8 CPUs 16 GB ram"""


class OptimizationBacktestJsonConverter(JsonConverter):
    """Json converter for OptimizationBacktest which creates a light weight easy to consume serialized version"""

    def CanConvert(self, objectType: typing.Type) -> bool:
        """
        Determines whether this instance can convert the specified object type.
        
        :param objectType: Type of the object.
        :returns: true if this instance can convert the specified object type; otherwise, false.
        """
        ...

    def ReadJson(self, reader: typing.Any, objectType: typing.Type, existingValue: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Reads the JSON representation of the object.
        
        :param reader: The Newtonsoft.Json.JsonReader to read from.
        :param objectType: Type of the object.
        :param existingValue: The existing value of object being read.
        :param serializer: The calling serializer.
        :returns: The object value.
        """
        ...

    def WriteJson(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """
        Writes the JSON representation of the object.
        
        :param writer: The Newtonsoft.Json.JsonWriter to write to.
        :param value: The value.
        :param serializer: The calling serializer.
        """
        ...


class ParameterSetJsonConverter(JsonConverter):
    """Json converter for ParameterSet which creates a light weight easy to consume serialized version"""

    def CanConvert(self, objectType: typing.Type) -> bool:
        """
        Determines whether this instance can convert the specified object type.
        
        :param objectType: Type of the object.
        :returns: true if this instance can convert the specified object type; otherwise, false.
        """
        ...

    def ReadJson(self, reader: typing.Any, objectType: typing.Type, existingValue: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Reads the JSON representation of the object.
        
        :param reader: The Newtonsoft.Json.JsonReader to read from.
        :param objectType: Type of the object.
        :param existingValue: The existing value of object being read.
        :param serializer: The calling serializer.
        :returns: The object value.
        """
        ...

    def WriteJson(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        ...


class AuthenticationResponse(QuantConnect.Api.RestResponse):
    """Verify if the credentials are OK."""


class Split(System.Object):
    """Split returned from the api"""

    @property
    def Symbol(self) -> QuantConnect.Symbol:
        """The Symbol"""
        ...

    @property
    def SymbolID(self) -> str:
        """The requested symbol ID"""
        ...

    @SymbolID.setter
    def SymbolID(self, value: str):
        """The requested symbol ID"""
        ...

    @property
    def Date(self) -> datetime.datetime:
        """The date of the split"""
        ...

    @Date.setter
    def Date(self, value: datetime.datetime):
        """The date of the split"""
        ...

    @property
    def SplitFactor(self) -> float:
        """The split factor"""
        ...

    @SplitFactor.setter
    def SplitFactor(self, value: float):
        """The split factor"""
        ...

    @property
    def ReferencePrice(self) -> float:
        """The reference price for the split"""
        ...

    @ReferencePrice.setter
    def ReferencePrice(self, value: float):
        """The reference price for the split"""
        ...


class SplitList(QuantConnect.Api.RestResponse):
    """Collection container for a list of split objects"""

    @property
    def Splits(self) -> System.Collections.Generic.List[QuantConnect.Api.Split]:
        """The splits list"""
        ...

    @Splits.setter
    def Splits(self, value: System.Collections.Generic.List[QuantConnect.Api.Split]):
        """The splits list"""
        ...


class Dividend(System.Object):
    """Dividend returned from the api"""

    @property
    def Symbol(self) -> QuantConnect.Symbol:
        """The Symbol"""
        ...

    @property
    def SymbolID(self) -> str:
        """The requested symbol ID"""
        ...

    @SymbolID.setter
    def SymbolID(self, value: str):
        """The requested symbol ID"""
        ...

    @property
    def Date(self) -> datetime.datetime:
        """The date of the dividend"""
        ...

    @Date.setter
    def Date(self, value: datetime.datetime):
        """The date of the dividend"""
        ...

    @property
    def DividendPerShare(self) -> float:
        """The dividend distribution"""
        ...

    @DividendPerShare.setter
    def DividendPerShare(self, value: float):
        """The dividend distribution"""
        ...

    @property
    def ReferencePrice(self) -> float:
        """The reference price for the dividend"""
        ...

    @ReferencePrice.setter
    def ReferencePrice(self, value: float):
        """The reference price for the dividend"""
        ...


class DividendList(QuantConnect.Api.RestResponse):
    """Collection container for a list of dividend objects"""

    @property
    def Dividends(self) -> System.Collections.Generic.List[QuantConnect.Api.Dividend]:
        """The dividends list"""
        ...

    @Dividends.setter
    def Dividends(self, value: System.Collections.Generic.List[QuantConnect.Api.Dividend]):
        """The dividends list"""
        ...


