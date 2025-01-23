from typing import overload
import datetime

import QuantConnect
import QuantConnect.Interfaces
import QuantConnect.Lean.Engine
import QuantConnect.Lean.Engine.Alpha
import QuantConnect.Lean.Engine.DataFeeds
import QuantConnect.Lean.Engine.RealTime
import QuantConnect.Lean.Engine.Results
import QuantConnect.Lean.Engine.Server
import QuantConnect.Lean.Engine.Setup
import QuantConnect.Lean.Engine.TransactionHandlers
import QuantConnect.Packets
import QuantConnect.Util
import QuantConnect.Util.RateLimit
import System
import System.Threading


class AlgorithmTimeLimitManager(System.Object, QuantConnect.IIsolatorLimitResultProvider):
    """
    Provides an implementation of IIsolatorLimitResultProvider that tracks the algorithm
    manager's time loops and enforces a maximum amount of time that each time loop may take to execute.
    The isolator uses the result provided by IsWithinLimit to determine if it should
    terminate the algorithm for violation of the imposed limits.
    """

    @property
    def AdditionalTimeBucket(self) -> QuantConnect.Util.RateLimit.ITokenBucket:
        """
        Gets the additional time bucket which is responsible for tracking additional time requested
        for processing via long-running scheduled events. In LEAN, we use the LeakyBucket
        """
        ...

    def __init__(self, additionalTimeBucket: QuantConnect.Util.RateLimit.ITokenBucket, timeLoopMaximum: datetime.timedelta) -> None:
        """
        Initializes a new instance of AlgorithmTimeLimitManager to manage the
        creation of IsolatorLimitResult instances as it pertains to the
        algorithm manager's time loop
        
        :param additionalTimeBucket: Provides a bucket of additional time that can be requested to be spent to give execution time for things such as training scheduled events
        :param timeLoopMaximum: Specifies the maximum amount of time the algorithm is permitted to spend in a single time loop. This value can be overriden if certain actions are taken by the algorithm, such as invoking the training methods.
        """
        ...

    def IsWithinLimit(self) -> QuantConnect.IsolatorLimitResult:
        """Determines whether or not the algorithm time loop is considered within the limits"""
        ...

    def RequestAdditionalTime(self, minutes: int) -> None:
        """
        Requests additional time to continue executing the current time step.
        At time of writing, this is intended to be used to provide training scheduled events
        additional time to allow complex training models time to execute while also preventing
        abuse by enforcing certain control parameters set via the job packet.
        
        Each time this method is invoked, this time limit manager will increase the allowable
        execution time by the specified number of whole minutes
        """
        ...

    def StartNewTimeStep(self) -> None:
        """
        Invoked by the algorithm at the start of each time loop. This resets the current time step
        elapsed time.
        """
        ...

    def TryRequestAdditionalTime(self, minutes: int) -> bool:
        """
        Attempts to requests additional time to continue executing the current time step.
        At time of writing, this is intended to be used to provide training scheduled events
        additional time to allow complex training models time to execute while also preventing
        abuse by enforcing certain control parameters set via the job packet.
        
        Each time this method is invoked, this time limit manager will increase the allowable
        execution time by the specified number of whole minutes
        """
        ...


class LeanEngineSystemHandlers(System.Object, System.IDisposable):
    """Provides a container for the system level handlers"""

    @property
    def Api(self) -> QuantConnect.Interfaces.IApi:
        """Gets the api instance used for communicating algorithm limits, status, and storing of log data"""
        ...

    @property
    def Notify(self) -> QuantConnect.Interfaces.IMessagingHandler:
        """
        Gets the messaging handler instance used for communicating various packets to listeners, including
        debug/log messages, email/sms/web messages, as well as results and run time errors
        """
        ...

    @property
    def JobQueue(self) -> QuantConnect.Interfaces.IJobQueueHandler:
        """Gets the job queue responsible for acquiring and acknowledging an algorithm job"""
        ...

    @property
    def LeanManager(self) -> QuantConnect.Lean.Engine.Server.ILeanManager:
        """Gets the ILeanManager implementation using to enhance the hosting environment"""
        ...

    def __init__(self, jobQueue: QuantConnect.Interfaces.IJobQueueHandler, api: QuantConnect.Interfaces.IApi, notify: QuantConnect.Interfaces.IMessagingHandler, leanManager: QuantConnect.Lean.Engine.Server.ILeanManager) -> None:
        """
        Initializes a new instance of the LeanEngineSystemHandlers class with the specified handles
        
        :param jobQueue: The job queue used to acquire algorithm jobs
        :param api: The api instance used for communicating limits and status
        :param notify: The messaging handler user for passing messages from the algorithm to listeners
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    @staticmethod
    def FromConfiguration(composer: QuantConnect.Util.Composer) -> QuantConnect.Lean.Engine.LeanEngineSystemHandlers:
        """
        Creates a new instance of the LeanEngineSystemHandlers class from the specified composer using type names from configuration
        
        :param composer: The composer instance to obtain implementations from
        :returns: A fully hydrates LeanEngineSystemHandlers instance.
        """
        ...

    def Initialize(self) -> None:
        """Initializes the Api, Messaging, and JobQueue components"""
        ...


class LeanEngineAlgorithmHandlers(System.Object, System.IDisposable):
    """Provides a container for the algorithm specific handlers"""

    @property
    def Results(self) -> QuantConnect.Lean.Engine.Results.IResultHandler:
        """Gets the result handler used to communicate results from the algorithm"""
        ...

    @property
    def Setup(self) -> QuantConnect.Lean.Engine.Setup.ISetupHandler:
        """Gets the setup handler used to initialize the algorithm state"""
        ...

    @property
    def DataFeed(self) -> QuantConnect.Lean.Engine.DataFeeds.IDataFeed:
        """Gets the data feed handler used to provide data to the algorithm"""
        ...

    @property
    def Transactions(self) -> QuantConnect.Lean.Engine.TransactionHandlers.ITransactionHandler:
        """Gets the transaction handler used to process orders from the algorithm"""
        ...

    @property
    def RealTime(self) -> QuantConnect.Lean.Engine.RealTime.IRealTimeHandler:
        """Gets the real time handler used to process real time events"""
        ...

    @property
    def MapFileProvider(self) -> QuantConnect.Interfaces.IMapFileProvider:
        """Gets the map file provider used as a map file source for the data feed"""
        ...

    @property
    def FactorFileProvider(self) -> QuantConnect.Interfaces.IFactorFileProvider:
        """Gets the map file provider used as a map file source for the data feed"""
        ...

    @property
    def DataProvider(self) -> QuantConnect.Interfaces.IDataProvider:
        """Gets the data file provider used to retrieve security data if it is not on the file system"""
        ...

    @property
    def DataCacheProvider(self) -> QuantConnect.Interfaces.IDataCacheProvider:
        """Gets the data file provider used to retrieve security data if it is not on the file system"""
        ...

    @property
    def Alphas(self) -> QuantConnect.Lean.Engine.Alpha.IAlphaHandler:
        """Gets the alpha handler used to process algorithm generated insights"""
        ...

    @property
    def ObjectStore(self) -> QuantConnect.Interfaces.IObjectStore:
        """Gets the object store used for persistence"""
        ...

    @property
    def DataPermissionsManager(self) -> QuantConnect.Interfaces.IDataPermissionManager:
        """Entity in charge of handling data permissions"""
        ...

    @property
    def DataMonitor(self) -> QuantConnect.Interfaces.IDataMonitor:
        """Monitors data requests and reports on missing data"""
        ...

    def __init__(self, results: QuantConnect.Lean.Engine.Results.IResultHandler, setup: QuantConnect.Lean.Engine.Setup.ISetupHandler, dataFeed: QuantConnect.Lean.Engine.DataFeeds.IDataFeed, transactions: QuantConnect.Lean.Engine.TransactionHandlers.ITransactionHandler, realTime: QuantConnect.Lean.Engine.RealTime.IRealTimeHandler, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider, factorFileProvider: QuantConnect.Interfaces.IFactorFileProvider, dataProvider: QuantConnect.Interfaces.IDataProvider, alphas: QuantConnect.Lean.Engine.Alpha.IAlphaHandler, objectStore: QuantConnect.Interfaces.IObjectStore, dataPermissionsManager: QuantConnect.Interfaces.IDataPermissionManager, liveMode: bool, researchMode: bool = False) -> None:
        """
        Initializes a new instance of the LeanEngineAlgorithmHandlers class from the specified handlers
        
        :param results: The result handler for communicating results from the algorithm
        :param setup: The setup handler used to initialize algorithm state
        :param dataFeed: The data feed handler used to pump data to the algorithm
        :param transactions: The transaction handler used to process orders from the algorithm
        :param realTime: The real time handler used to process real time events
        :param mapFileProvider: The map file provider used to retrieve map files for the data feed
        :param factorFileProvider: Map file provider used as a map file source for the data feed
        :param dataProvider: file provider used to retrieve security data if it is not on the file system
        :param alphas: The alpha handler used to process generated insights
        :param objectStore: The object store used for persistence
        :param dataPermissionsManager: The data permission manager to use
        :param liveMode: True for live mode, false otherwise
        :param researchMode: True for research mode, false otherwise. This has less priority than liveMode
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    @staticmethod
    def FromConfiguration(composer: QuantConnect.Util.Composer, researchMode: bool = False) -> QuantConnect.Lean.Engine.LeanEngineAlgorithmHandlers:
        """
        Creates a new instance of the LeanEngineAlgorithmHandlers class from the specified composer using type names from configuration
        
        :param composer: The composer instance to obtain implementations from
        :param researchMode: True for research mode, false otherwise
        :returns: A fully hydrates LeanEngineSystemHandlers instance.
        """
        ...


class AlgorithmManager(System.Object):
    """Algorithm manager class executes the algorithm and generates and passes through the algorithm events."""

    @property
    def State(self) -> int:
        """
        Publicly accessible algorithm status
        
        This property contains the int value of a member of the QuantConnect.AlgorithmStatus enum.
        """
        ...

    @property
    def AlgorithmId(self) -> str:
        """Public access to the currently running algorithm id."""
        ...

    @AlgorithmId.setter
    def AlgorithmId(self, value: str):
        """Public access to the currently running algorithm id."""
        ...

    @property
    def TimeLimit(self) -> QuantConnect.Lean.Engine.AlgorithmTimeLimitManager:
        """
        Provides the isolator with a function for verifying that we're not spending too much time in each
        algorithm manager time loop
        """
        ...

    @property
    def QuitState(self) -> bool:
        """Quit state flag for the running algorithm. When true the user has requested the backtest stops through a Quit() method."""
        ...

    @property
    def DataPoints(self) -> int:
        """Gets the number of data points processed per second"""
        ...

    @DataPoints.setter
    def DataPoints(self, value: int):
        """Gets the number of data points processed per second"""
        ...

    @property
    def AlgorithmHistoryDataPoints(self) -> int:
        """Gets the number of data points of algorithm history provider"""
        ...

    def __init__(self, liveMode: bool, job: QuantConnect.Packets.AlgorithmNodePacket = None) -> None:
        """
        Initializes a new instance of the AlgorithmManager class
        
        :param liveMode: True if we're running in live mode, false for backtest mode
        :param job: Provided by LEAN when creating a new algo manager. This is the job that the algo manager is about to execute. Research and other consumers can provide the default value of null
        """
        ...

    @staticmethod
    def HandleDividends(timeSlice: QuantConnect.Lean.Engine.DataFeeds.TimeSlice, algorithm: QuantConnect.Interfaces.IAlgorithm, liveMode: bool) -> None:
        """Helper method to apply a dividend to an algorithm instance"""
        ...

    @staticmethod
    def HandleSplits(timeSlice: QuantConnect.Lean.Engine.DataFeeds.TimeSlice, algorithm: QuantConnect.Interfaces.IAlgorithm, liveMode: bool) -> None:
        """Helper method to apply a split to an algorithm instance"""
        ...

    @staticmethod
    def ProcessVolatilityHistoryRequirements(algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """
        Helper method used to process securities volatility history requirements
        
        :param algorithm: The algorithm instance
        """
        ...

    def Run(self, job: QuantConnect.Packets.AlgorithmNodePacket, algorithm: QuantConnect.Interfaces.IAlgorithm, synchronizer: QuantConnect.Lean.Engine.DataFeeds.ISynchronizer, transactions: QuantConnect.Lean.Engine.TransactionHandlers.ITransactionHandler, results: QuantConnect.Lean.Engine.Results.IResultHandler, realtime: QuantConnect.Lean.Engine.RealTime.IRealTimeHandler, leanManager: QuantConnect.Lean.Engine.Server.ILeanManager, alphas: QuantConnect.Lean.Engine.Alpha.IAlphaHandler, token: System.Threading.CancellationToken) -> None:
        """
        Launch the algorithm manager to run this strategy
        
        :param job: Algorithm job
        :param algorithm: Algorithm instance
        :param synchronizer: Instance which implements ISynchronizer. Used to stream the data
        :param transactions: Transaction manager object
        :param results: Result handler object
        :param realtime: Realtime processing object
        :param leanManager: ILeanManager implementation that is updated periodically with the IAlgorithm instance
        :param alphas: Alpha handler used to process algorithm generated insights
        :param token: Cancellation token
        """
        ...

    def SetStatus(self, state: QuantConnect.AlgorithmStatus) -> None:
        """Set the quit state."""
        ...


class Engine(System.Object):
    """
    LEAN ALGORITHMIC TRADING ENGINE: ENTRY POINT.
    
    The engine loads new tasks, create the algorithms and threads, and sends them
    to Algorithm Manager to be executed. It is the primary operating loop.
    """

    @property
    def SystemHandlers(self) -> QuantConnect.Lean.Engine.LeanEngineSystemHandlers:
        """Gets the configured system handlers for this engine instance"""
        ...

    @property
    def AlgorithmHandlers(self) -> QuantConnect.Lean.Engine.LeanEngineAlgorithmHandlers:
        """Gets the configured algorithm handlers for this engine instance"""
        ...

    def __init__(self, systemHandlers: QuantConnect.Lean.Engine.LeanEngineSystemHandlers, algorithmHandlers: QuantConnect.Lean.Engine.LeanEngineAlgorithmHandlers, liveMode: bool) -> None:
        """
        Initializes a new instance of the Engine class using the specified handlers
        
        :param systemHandlers: The system handlers for controlling acquisition of jobs, messaging, and api calls
        :param algorithmHandlers: The algorithm handlers for managing algorithm initialization, data, results, transaction, and real time events
        :param liveMode: True when running in live mode, false otherwise
        """
        ...

    def Run(self, job: QuantConnect.Packets.AlgorithmNodePacket, manager: QuantConnect.Lean.Engine.AlgorithmManager, assemblyPath: str, workerThread: QuantConnect.Util.WorkerThread) -> None:
        """
        Runs a single backtest/live job from the job queue
        
        :param job: The algorithm job to be processed
        :param manager: The algorithm manager instance
        :param assemblyPath: The path to the algorithm's assembly
        :param workerThread: The worker thread instance
        """
        ...


class Initializer(System.Object):
    """Helper class to initialize a Lean engine"""

    @staticmethod
    def GetAlgorithmHandlers(researchMode: bool = False) -> QuantConnect.Lean.Engine.LeanEngineAlgorithmHandlers:
        """Get and initializes Algorithm Handler"""
        ...

    @staticmethod
    def GetSystemHandlers() -> QuantConnect.Lean.Engine.LeanEngineSystemHandlers:
        """Get and initializes System Handler"""
        ...

    @staticmethod
    def Start() -> None:
        """Basic common Lean initialization"""
        ...


