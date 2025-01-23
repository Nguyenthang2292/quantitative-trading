from typing import overload
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Brokerages
import QuantConnect.Data
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import QuantConnect.Lean.Engine.DataFeeds
import QuantConnect.Lean.Engine.DataFeeds.Enumerators
import QuantConnect.Lean.Engine.Results
import QuantConnect.Packets
import QuantConnect.Securities
import QuantConnect.Util
import System
import System.Collections
import System.Collections.Generic
import System.IO
import System.Threading

QuantConnect_Lean_Engine_DataFeeds_UpdateData_T = typing.TypeVar("QuantConnect_Lean_Engine_DataFeeds_UpdateData_T")
QuantConnect_Lean_Engine_DataFeeds__EventContainer_Callable = typing.TypeVar("QuantConnect_Lean_Engine_DataFeeds__EventContainer_Callable")
QuantConnect_Lean_Engine_DataFeeds__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Lean_Engine_DataFeeds__EventContainer_ReturnType")


class BaseDataExchange(System.Object):
    """Provides a means of distributing output from enumerators from a dedicated separate thread"""

    class EnumeratorHandler(System.Object):
        """Handler used to manage a single enumerator's move next/end of stream behavior"""

        @property
        def EnumeratorFinished(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.BaseDataExchange.EnumeratorHandler], None], None]:
            """Event fired when MoveNext returns false"""
            ...

        @EnumeratorFinished.setter
        def EnumeratorFinished(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.BaseDataExchange.EnumeratorHandler], None], None]):
            """Event fired when MoveNext returns false"""
            ...

        @property
        def Symbol(self) -> QuantConnect.Symbol:
            """A unique symbol used to identify this enumerator"""
            ...

        @property
        def Enumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
            """The enumerator this handler handles"""
            ...

        def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], shouldMoveNext: typing.Callable[[], bool] = None, handleData: typing.Callable[[QuantConnect.Data.BaseData], None] = None) -> None:
            """
            Initializes a new instance of the EnumeratorHandler class
            
            :param symbol: The symbol to identify this enumerator
            :param enumerator: The enumeator this handler handles
            :param shouldMoveNext: Predicate function used to determine if we should call move next on the symbol's enumerator
            :param handleData: Handler for data if HandlesData=true
            """
            ...

        def HandleData(self, data: QuantConnect.Data.BaseData) -> None:
            """
            Handles the specified data.
            
            :param data: The data to be handled
            """
            ...

        def OnEnumeratorFinished(self) -> None:
            """Event invocator for the EnumeratorFinished event"""
            ...

        def ShouldMoveNext(self) -> bool:
            """Returns true if this enumerator should move next"""
            ...

    @property
    def SleepInterval(self) -> int:
        """Gets or sets how long this thread will sleep when no data is available"""
        ...

    @SleepInterval.setter
    def SleepInterval(self, value: int):
        """Gets or sets how long this thread will sleep when no data is available"""
        ...

    @property
    def Name(self) -> str:
        """Gets a name for this exchange"""
        ...

    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the BaseDataExchange
        
        :param name: A name for this exchange
        """
        ...

    @overload
    def AddEnumerator(self, handler: QuantConnect.Lean.Engine.DataFeeds.BaseDataExchange.EnumeratorHandler) -> None:
        """
        Adds the enumerator to this exchange. If it has already been added
        then it will remain registered in the exchange only once
        
        :param handler: The handler to use when this symbol's data is encountered
        """
        ...

    @overload
    def AddEnumerator(self, symbol: typing.Union[QuantConnect.Symbol, str], enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], shouldMoveNext: typing.Callable[[], bool] = None, enumeratorFinished: typing.Callable[[QuantConnect.Lean.Engine.DataFeeds.BaseDataExchange.EnumeratorHandler], None] = None, handleData: typing.Callable[[QuantConnect.Data.BaseData], None] = None) -> None:
        """
        Adds the enumerator to this exchange. If it has already been added
        then it will remain registered in the exchange only once
        
        :param symbol: A unique symbol used to identify this enumerator
        :param enumerator: The enumerator to be added
        :param shouldMoveNext: Function used to determine if move next should be called on this enumerator, defaults to always returning true
        :param enumeratorFinished: Delegate called when the enumerator move next returns false
        :param handleData: Handler for data if HandlesData=true
        """
        ...

    def RemoveEnumerator(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Lean.Engine.DataFeeds.BaseDataExchange.EnumeratorHandler:
        """
        Removes and returns enumerator handler with the specified symbol.
        The removed handler is returned, null if not found
        """
        ...

    def SetErrorHandler(self, isFatalError: typing.Callable[[System.Exception], bool]) -> None:
        """
        Sets the specified function as the error handler. This function
        returns true if it is a fatal error and queue consumption should
        cease.
        
        :param isFatalError: The error handling function to use when an error is encountered during queue consumption. Returns true if queue consumption should be stopped, returns false if queue consumption should continue
        """
        ...

    def Start(self) -> None:
        """
        Begins consumption of the wrapped IDataQueueHandler on
        a separate thread
        """
        ...

    def Stop(self) -> None:
        """Ends consumption of the wrapped IDataQueueHandler"""
        ...


class SingleEntryDataCacheProvider(System.Object, QuantConnect.Interfaces.IDataCacheProvider):
    """
    Default implementation of the IDataCacheProvider
    Does not cache data.  If the data is a zip, the first entry is returned
    """

    @property
    def IsDataEphemeral(self) -> bool:
        """Property indicating the data is temporary in nature and should not be cached."""
        ...

    def __init__(self, dataProvider: QuantConnect.Interfaces.IDataProvider, isDataEphemeral: bool = True) -> None:
        """Constructor that takes the IDataProvider to be used to retrieve data"""
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def Fetch(self, key: str) -> System.IO.Stream:
        """
        Fetch data from the cache
        
        :param key: A string representing the key of the cached data
        :returns: An Stream of the cached data.
        """
        ...

    def GetZipEntries(self, zipFile: str) -> System.Collections.Generic.List[str]:
        """Returns a list of zip entries in a provided zip file"""
        ...

    def Store(self, key: str, data: typing.List[int]) -> None:
        """
        Not implemented
        
        :param key: The source of the data, used as a key to retrieve data in the cache
        :param data: The data to cache as a byte array
        """
        ...


class InternalSubscriptionManager(System.Object):
    """Class in charge of handling Leans internal subscriptions"""

    @property
    def Added(self) -> typing.Callable[[System.Object, QuantConnect.Data.UniverseSelection.SubscriptionRequest], None]:
        """Event fired when a new internal subscription request is to be added"""
        ...

    @Added.setter
    def Added(self, value: typing.Callable[[System.Object, QuantConnect.Data.UniverseSelection.SubscriptionRequest], None]):
        """Event fired when a new internal subscription request is to be added"""
        ...

    @property
    def Removed(self) -> typing.Callable[[System.Object, QuantConnect.Data.UniverseSelection.SubscriptionRequest], None]:
        """Event fired when an existing internal subscription should be removed"""
        ...

    @Removed.setter
    def Removed(self, value: typing.Callable[[System.Object, QuantConnect.Data.UniverseSelection.SubscriptionRequest], None]):
        """Event fired when an existing internal subscription should be removed"""
        ...

    def __init__(self, algorithm: QuantConnect.Interfaces.IAlgorithm, resolution: QuantConnect.Resolution) -> None:
        """
        Creates a new instances
        
        :param algorithm: The associated algorithm
        :param resolution: The resolution to use for the internal subscriptions
        """
        ...

    def AddedSubscriptionRequest(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest) -> None:
        """
        Notifies about a removed subscription request
        
        :param request: The removed subscription request
        """
        ...

    def RemovedSubscriptionRequest(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest) -> None:
        """
        Notifies about an added subscription request
        
        :param request: The added subscription request
        """
        ...


class InvalidSourceEventArgs(System.EventArgs):
    """Event arguments for the ISubscriptionDataSourceReader.InvalidSource event"""

    @property
    def Source(self) -> QuantConnect.Data.SubscriptionDataSource:
        """Gets the source that was considered invalid"""
        ...

    @Source.setter
    def Source(self, value: QuantConnect.Data.SubscriptionDataSource):
        """Gets the source that was considered invalid"""
        ...

    @property
    def Exception(self) -> System.Exception:
        """Gets the exception that was encountered"""
        ...

    @Exception.setter
    def Exception(self, value: System.Exception):
        """Gets the exception that was encountered"""
        ...

    def __init__(self, source: QuantConnect.Data.SubscriptionDataSource, exception: System.Exception) -> None:
        """
        Initializes a new instance of the InvalidSourceEventArgs class
        
        :param source: The source that was considered invalid
        :param exception: The exception that was encountered
        """
        ...


class ISubscriptionDataSourceReader(metaclass=abc.ABCMeta):
    """
    Represents a type responsible for accepting an input SubscriptionDataSource
    and returning an enumerable of the source's BaseData
    """

    @property
    @abc.abstractmethod
    def InvalidSource(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.InvalidSourceEventArgs], None], None]:
        """
        Event fired when the specified source is considered invalid, this may
        be from a missing file or failure to download a remote source
        """
        ...

    @InvalidSource.setter
    @abc.abstractmethod
    def InvalidSource(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.InvalidSourceEventArgs], None], None]):
        """
        Event fired when the specified source is considered invalid, this may
        be from a missing file or failure to download a remote source
        """
        ...

    def Read(self, source: QuantConnect.Data.SubscriptionDataSource) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]:
        """
        Reads the specified
        
        :param source: The source to be read
        :returns: An IEnumerable{BaseData} that contains the data in the source.
        """
        ...


class BaseSubscriptionDataSourceReader(System.Object, QuantConnect.Lean.Engine.DataFeeds.ISubscriptionDataSourceReader, metaclass=abc.ABCMeta):
    """A base class for implementations of the ISubscriptionDataSourceReader"""

    @property
    def IsLiveMode(self) -> bool:
        """
        True if we're in live mode, false for backtesting
        
        This property is protected.
        """
        ...

    @property
    def DataCacheProvider(self) -> QuantConnect.Interfaces.IDataCacheProvider:
        """
        The data cache provider to use
        
        This property is protected.
        """
        ...

    @property
    def InvalidSource(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.InvalidSourceEventArgs], None], None]:
        """
        Event fired when the specified source is considered invalid, this may
        be from a missing file or failure to download a remote source
        """
        ...

    @InvalidSource.setter
    def InvalidSource(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.InvalidSourceEventArgs], None], None]):
        """
        Event fired when the specified source is considered invalid, this may
        be from a missing file or failure to download a remote source
        """
        ...

    def __init__(self, dataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider, isLiveMode: bool) -> None:
        """
        Creates a new instance
        
        This method is protected.
        """
        ...

    def CreateStreamReader(self, subscriptionDataSource: QuantConnect.Data.SubscriptionDataSource) -> QuantConnect.Interfaces.IStreamReader:
        """
        Creates a new IStreamReader for the specified
        
        This method is protected.
        
        :param subscriptionDataSource: The source to produce an IStreamReader for
        :returns: A new instance of IStreamReader to read the source, or null if there was an error.
        """
        ...

    def OnInvalidSource(self, source: QuantConnect.Data.SubscriptionDataSource, exception: System.Exception) -> None:
        """
        Event invocator for the InvalidSource event
        
        This method is protected.
        
        :param source: The SubscriptionDataSource that was invalid
        :param exception: The exception if one was raised, otherwise null
        """
        ...

    def Read(self, source: QuantConnect.Data.SubscriptionDataSource) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]:
        """
        Reads the specified
        
        :param source: The source to be read
        :returns: An IEnumerable{BaseData} that contains the data in the source.
        """
        ...


class ReaderErrorEventArgs(System.EventArgs):
    """Event arguments for the TextSubscriptionDataSourceReader.ReaderError event."""

    @property
    def Line(self) -> str:
        """Gets the line that caused the error"""
        ...

    @Line.setter
    def Line(self, value: str):
        """Gets the line that caused the error"""
        ...

    @property
    def Exception(self) -> System.Exception:
        """Gets the exception that was caught"""
        ...

    @Exception.setter
    def Exception(self, value: System.Exception):
        """Gets the exception that was caught"""
        ...

    def __init__(self, line: str, exception: System.Exception) -> None:
        """
        Initializes a new instance of the ReaderErrorEventArgs class
        
        :param line: The line that caused the error
        :param exception: The exception that was caught during the read
        """
        ...


class CollectionSubscriptionDataSourceReader(QuantConnect.Lean.Engine.DataFeeds.BaseSubscriptionDataSourceReader):
    """
    Collection Subscription Factory takes a BaseDataCollection from BaseData factories
    and yields it one point at a time to the algorithm
    """

    @property
    def ReaderError(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.ReaderErrorEventArgs], None], None]:
        """
        Event fired when an exception is thrown during a call to
        BaseData.Reader(SubscriptionDataConfig, string, DateTime, bool)
        """
        ...

    @ReaderError.setter
    def ReaderError(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.ReaderErrorEventArgs], None], None]):
        """
        Event fired when an exception is thrown during a call to
        BaseData.Reader(SubscriptionDataConfig, string, DateTime, bool)
        """
        ...

    def __init__(self, dataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> None:
        """
        Initializes a new instance of the CollectionSubscriptionDataSourceReader class
        
        :param dataCacheProvider: Used to cache data for requested from the IDataProvider
        :param config: The subscription's configuration
        :param date: The date this factory was produced to read data for
        :param isLiveMode: True if we're in live mode, false for backtesting
        """
        ...

    def Read(self, source: QuantConnect.Data.SubscriptionDataSource) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]:
        """
        Reads the specified
        
        :param source: The source to be read
        :returns: An IEnumerable{BaseData} that contains the data in the source.
        """
        ...


class CreateStreamReaderErrorEventArgs(System.EventArgs):
    """Event arguments for the TextSubscriptionDataSourceReader's CreateStreamReader event"""

    @property
    def Date(self) -> datetime.datetime:
        """Gets the date of the source"""
        ...

    @Date.setter
    def Date(self, value: datetime.datetime):
        """Gets the date of the source"""
        ...

    @property
    def Source(self) -> QuantConnect.Data.SubscriptionDataSource:
        """Gets the source that caused the error"""
        ...

    @Source.setter
    def Source(self, value: QuantConnect.Data.SubscriptionDataSource):
        """Gets the source that caused the error"""
        ...

    def __init__(self, date: typing.Union[datetime.datetime, datetime.date], source: QuantConnect.Data.SubscriptionDataSource) -> None:
        """
        Initializes a new instance of the CreateStreamReaderErrorEventArgs class
        
        :param date: The date of the source
        :param source: The source that cause the error
        """
        ...


class DataQueueHandlerManager(System.Object, QuantConnect.Interfaces.IDataQueueHandler, QuantConnect.Interfaces.IDataQueueUniverseProvider):
    """This is an implementation of IDataQueueHandler used to handle multiple live datafeeds"""

    @property
    def DataHandlers(self) -> System.Collections.Generic.List[QuantConnect.Interfaces.IDataQueueHandler]:
        """
        Collection of data queue handles being used
        
        This property is protected.
        """
        ...

    @property
    def HasUniverseProvider(self) -> bool:
        """True if the composite queue handler has any IDataQueueUniverseProvider instance"""
        ...

    @property
    def IsConnected(self) -> bool:
        """Returns whether the data provider is connected"""
        ...

    def CanPerformSelection(self) -> bool:
        """
        Returns whether selection can take place or not.
        
        :returns: True if selection can take place.
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def InitializeFrontierTimeProvider(self) -> None:
        """
        Creates the frontier time provider instance
        
        This method is protected.
        """
        ...

    def LookupSymbols(self, symbol: typing.Union[QuantConnect.Symbol, str], includeExpired: bool, securityCurrency: str = None) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Method returns a collection of Symbols that are available at the data source.
        
        :param symbol: Symbol to lookup
        :param includeExpired: Include expired contracts
        :param securityCurrency: Expected security currency(if any)
        :returns: Enumerable of Symbols, that are associated with the provided Symbol.
        """
        ...

    def SetJob(self, job: QuantConnect.Packets.LiveNodePacket) -> None:
        """
        Sets the job we're subscribing for
        
        :param job: Job we're subscribing for
        """
        ...

    def Subscribe(self, dataConfig: QuantConnect.Data.SubscriptionDataConfig, newDataAvailableHandler: typing.Callable[[System.Object, System.EventArgs], None]) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Subscribe to the specified configuration
        
        :param dataConfig: defines the parameters to subscribe to a data feed
        :param newDataAvailableHandler: handler to be fired on new data available
        :returns: The new enumerator for this subscription request.
        """
        ...

    def Unsubscribe(self, dataConfig: QuantConnect.Data.SubscriptionDataConfig) -> None:
        """
        Removes the specified configuration
        
        :param dataConfig: Subscription config to be removed
        """
        ...


class DefaultDataProvider(System.Object, QuantConnect.Interfaces.IDataProvider, System.IDisposable):
    """Default file provider functionality that retrieves data from disc to be used in an algorithm"""

    @property
    def NewDataRequest(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Interfaces.DataProviderNewDataRequestEventArgs], None], None]:
        """Event raised each time data fetch is finished (successfully or not)"""
        ...

    @NewDataRequest.setter
    def NewDataRequest(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Interfaces.DataProviderNewDataRequestEventArgs], None], None]):
        """Event raised each time data fetch is finished (successfully or not)"""
        ...

    def Dispose(self) -> None:
        """
        The stream created by this type is passed up the stack to the IStreamReader
        The stream is closed when the StreamReader that wraps this stream is disposed
        """
        ...

    def Fetch(self, key: str) -> System.IO.Stream:
        """
        Retrieves data from disc to be used in an algorithm
        
        :param key: A string representing where the data is stored
        :returns: A Stream of the data requested.
        """
        ...

    def OnNewDataRequest(self, e: QuantConnect.Interfaces.DataProviderNewDataRequestEventArgs) -> None:
        """
        Event invocator for the NewDataRequest event
        
        This method is protected.
        """
        ...


class BaseDownloaderDataProvider(QuantConnect.Lean.Engine.DataFeeds.DefaultDataProvider, metaclass=abc.ABCMeta):
    """Base downloader implementation with some helper methods"""

    def DownloadOnce(self, key: str, download: typing.Callable[[str], None]) -> System.IO.Stream:
        """
        Helper method which guarantees each requested key is downloaded only once concurrently if required based on NeedToDownload
        
        This method is protected.
        
        :param key: A string representing where the data is stored
        :param download: The download operation we want to perform once concurrently per key
        :returns: A Stream of the data requested.
        """
        ...

    def NeedToDownload(self, filePath: str) -> bool:
        """
        Main filter to determine if this file needs to be downloaded
        
        This method is protected.
        
        :param filePath: File we are looking at
        :returns: True if should download.
        """
        ...


class IndexSubscriptionDataSourceReader(QuantConnect.Lean.Engine.DataFeeds.BaseSubscriptionDataSourceReader):
    """
    This ISubscriptionDataSourceReader implementation supports
    the FileFormat.Index and IndexedBaseData types.
    Handles the layer of indirection for the index data source and forwards
    the target source to the corresponding ISubscriptionDataSourceReader
    """

    def __init__(self, dataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool, dataProvider: QuantConnect.Interfaces.IDataProvider) -> None:
        """Creates a new instance of this ISubscriptionDataSourceReader"""
        ...

    def Read(self, source: QuantConnect.Data.SubscriptionDataSource) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]:
        """
        Reads the specified
        
        :param source: The source to be read
        :returns: An IEnumerable{BaseData} that contains the data in the source.
        """
        ...


class CompositeTimeProvider(System.Object, QuantConnect.ITimeProvider):
    """The composite time provider will source it's current time using the smallest time from the given providers"""

    def __init__(self, timeProviders: System.Collections.Generic.IEnumerable[QuantConnect.ITimeProvider]) -> None:
        """
        Creates a new instance
        
        :param timeProviders: The time providers to use. Will default to the real time provider if empty
        """
        ...

    def GetUtcNow(self) -> datetime.datetime:
        """
        Gets the current time in UTC
        
        :returns: The current time in UTC.
        """
        ...


class LiveTimeProvider(System.Object, QuantConnect.ITimeProvider):
    """Live time provide which supports an initial warmup period using the given time provider SubscriptionFrontierTimeProvider, used by the LiveSynchronizer"""

    def __init__(self, realTime: QuantConnect.ITimeProvider) -> None:
        """
        Creates a new instance
        
        :param realTime: Real time provider
        """
        ...

    def GetUtcNow(self) -> datetime.datetime:
        """
        Gets the current time in UTC
        
        :returns: The current time in UTC.
        """
        ...

    def Initialize(self, warmupTimeProvider: QuantConnect.ITimeProvider) -> None:
        """
        Fully initializes this instance providing the initial warmup time provider to use
        
        :param warmupTimeProvider: The warmup provider to use
        """
        ...


class TextSubscriptionDataSourceReader(QuantConnect.Lean.Engine.DataFeeds.BaseSubscriptionDataSourceReader):
    """
    Provides an implementations of ISubscriptionDataSourceReader that uses the
    BaseData.Reader(SubscriptionDataConfig,string,DateTime,bool)
    method to read lines of text from a SubscriptionDataSource
    """

    @property
    def ReaderError(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.ReaderErrorEventArgs], None], None]:
        """
        Event fired when an exception is thrown during a call to
        BaseData.Reader(SubscriptionDataConfig,string,DateTime,bool)
        """
        ...

    @ReaderError.setter
    def ReaderError(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.ReaderErrorEventArgs], None], None]):
        """
        Event fired when an exception is thrown during a call to
        BaseData.Reader(SubscriptionDataConfig,string,DateTime,bool)
        """
        ...

    def __init__(self, dataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> None:
        """
        Initializes a new instance of the TextSubscriptionDataSourceReader class
        
        :param dataCacheProvider: This provider caches files if needed
        :param config: The subscription's configuration
        :param date: The date this factory was produced to read data for
        :param isLiveMode: True if we're in live mode, false for backtesting
        """
        ...

    def Read(self, source: QuantConnect.Data.SubscriptionDataSource) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]:
        """
        Reads the specified
        
        :param source: The source to be read
        :returns: An IEnumerable{BaseData} that contains the data in the source.
        """
        ...

    @staticmethod
    def SetCacheSize(megaBytesToUse: int) -> None:
        """Set the cache size to use"""
        ...


class BaseDataCollectionAggregatorReader(QuantConnect.Lean.Engine.DataFeeds.TextSubscriptionDataSourceReader):
    """Data source reader that will aggregate data points into a base data collection"""

    def __init__(self, dataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> None:
        """
        Initializes a new instance of the TextSubscriptionDataSourceReader class
        
        :param dataCacheProvider: This provider caches files if needed
        :param config: The subscription's configuration
        :param date: The date this factory was produced to read data for
        :param isLiveMode: True if we're in live mode, false for backtesting
        """
        ...

    def Read(self, source: QuantConnect.Data.SubscriptionDataSource) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]:
        """
        Reads the specified
        
        :param source: The source to be read
        :returns: An IEnumerable{BaseData} that contains the data in the source.
        """
        ...


class SubscriptionData(System.Object):
    """Store data (either raw or adjusted) and the time at which it should be synchronized"""

    @property
    def _data(self) -> QuantConnect.Data.BaseData:
        """
        Data
        
        This field is protected.
        """
        ...

    @_data.setter
    def _data(self, value: QuantConnect.Data.BaseData):
        """
        Data
        
        This field is protected.
        """
        ...

    @property
    def Data(self) -> QuantConnect.Data.BaseData:
        """Gets the data"""
        ...

    @property
    def EmitTimeUtc(self) -> datetime.datetime:
        """Gets the UTC emit time for this data"""
        ...

    def __init__(self, data: QuantConnect.Data.BaseData, emitTimeUtc: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the SubscriptionData class
        
        :param data: The base data
        :param emitTimeUtc: The emit time for the data
        """
        ...

    @staticmethod
    def Create(configuration: QuantConnect.Data.SubscriptionDataConfig, exchangeHours: QuantConnect.Securities.SecurityExchangeHours, offsetProvider: QuantConnect.TimeZoneOffsetProvider, data: QuantConnect.Data.BaseData, normalizationMode: QuantConnect.DataNormalizationMode, factor: typing.Optional[float] = None) -> QuantConnect.Lean.Engine.DataFeeds.SubscriptionData:
        """
        Clones the data, computes the utc emit time and performs exchange round down behavior, storing the result in a new SubscriptionData instance
        
        :param configuration: The subscription's configuration
        :param exchangeHours: The exchange hours of the security
        :param offsetProvider: The subscription's offset provider
        :param data: The data being emitted
        :param normalizationMode: Specifies how data is normalized
        :param factor: price scale factor
        :returns: A new SubscriptionData containing the specified data.
        """
        ...


class Subscription(System.Object):
    """Represents the data required for a data feed to process a single subscription"""

    @property
    def NewDataAvailable(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Event fired when a new data point is available"""
        ...

    @NewDataAvailable.setter
    def NewDataAvailable(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]):
        """Event fired when a new data point is available"""
        ...

    @property
    def Universes(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.UniverseSelection.Universe]:
        """Gets the universe for this subscription"""
        ...

    @property
    def Security(self) -> QuantConnect.Interfaces.ISecurityPrice:
        """Gets the security this subscription points to"""
        ...

    @property
    def Configuration(self) -> QuantConnect.Data.SubscriptionDataConfig:
        """Gets the configuration for this subscritions"""
        ...

    @property
    def TimeZone(self) -> typing.Any:
        """Gets the exchange time zone associated with this subscription"""
        ...

    @property
    def OffsetProvider(self) -> QuantConnect.TimeZoneOffsetProvider:
        """Gets the offset provider for time zone conversions to and from the data's local time"""
        ...

    @property
    def RealtimePrice(self) -> float:
        """Gets the most current value from the subscription source"""
        ...

    @RealtimePrice.setter
    def RealtimePrice(self, value: float):
        """Gets the most current value from the subscription source"""
        ...

    @property
    def EndOfStream(self) -> bool:
        """Gets true if this subscription is finished, false otherwise"""
        ...

    @EndOfStream.setter
    def EndOfStream(self, value: bool):
        """Gets true if this subscription is finished, false otherwise"""
        ...

    @property
    def IsUniverseSelectionSubscription(self) -> bool:
        """Gets true if this subscription is used in universe selection"""
        ...

    @property
    def UtcStartTime(self) -> datetime.datetime:
        """Gets the start time of this subscription in UTC"""
        ...

    @property
    def UtcEndTime(self) -> datetime.datetime:
        """Gets the end time of this subscription in UTC"""
        ...

    @property
    def RemovedFromUniverse(self) -> QuantConnect.Util.IReadOnlyRef[bool]:
        """Gets whether or not this subscription has been removed from its parent universe"""
        ...

    @property
    def Current(self) -> QuantConnect.Lean.Engine.DataFeeds.SubscriptionData:
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    @Current.setter
    def Current(self, value: QuantConnect.Lean.Engine.DataFeeds.SubscriptionData):
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    def __init__(self, subscriptionRequest: QuantConnect.Data.UniverseSelection.SubscriptionRequest, enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Lean.Engine.DataFeeds.SubscriptionData], timeZoneOffsetProvider: QuantConnect.TimeZoneOffsetProvider) -> None:
        """
        Initializes a new instance of the Subscription class with a universe
        
        :param subscriptionRequest: Specified for universe subscriptions
        :param enumerator: The subscription's data source
        :param timeZoneOffsetProvider: The offset provider used to convert data local times to utc
        """
        ...

    def AddSubscriptionRequest(self, subscriptionRequest: QuantConnect.Data.UniverseSelection.SubscriptionRequest) -> bool:
        """
        Adds a SubscriptionRequest for this subscription
        
        :param subscriptionRequest: The SubscriptionRequest to add
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def Equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified object is equal to the current object.
        
        :param obj: The object to compare with the current object.
        :returns: true if the specified object  is equal to the current object; otherwise, false.
        """
        ...

    def GetHashCode(self) -> int:
        """
        Serves as a hash function for a particular type.
        
        :returns: A hash code for the current System.Object.
        """
        ...

    def MarkAsRemovedFromUniverse(self) -> None:
        """
        Mark this subscription as having been removed from the universe.
        Data for this time step will be discarded.
        """
        ...

    def MoveNext(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        ...

    def OnNewDataAvailable(self) -> None:
        """Event invocator for the NewDataAvailable event"""
        ...

    def RemoveSubscriptionRequest(self, universe: QuantConnect.Data.UniverseSelection.Universe = None) -> bool:
        """
        Removes one or all SubscriptionRequest from this subscription
        
        :param universe: Universe requesting to remove SubscriptionRequest. Default value, null, will remove all universes
        :returns: True, if the subscription is empty and ready to be removed.
        """
        ...

    def Reset(self) -> None:
        """Sets the enumerator to its initial position, which is before the first element in the collection."""
        ...

    def ToString(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class SubscriptionCollection(System.Object, typing.Iterable[QuantConnect.Lean.Engine.DataFeeds.Subscription]):
    """Provides a collection for holding subscriptions."""

    def __init__(self) -> None:
        """Initializes a new instance of the SubscriptionCollection class"""
        ...

    def Contains(self, configuration: QuantConnect.Data.SubscriptionDataConfig) -> bool:
        """
        Checks the collection for the specified subscription configuration
        
        :param configuration: The subscription configuration to check for
        :returns: True if a subscription with the specified configuration is found in this collection, false otherwise.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Lean.Engine.DataFeeds.Subscription]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: An enumerator that can be used to iterate through the collection.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        """
        Returns an enumerator that iterates through a collection.
        
        :returns: An System.Collections.IEnumerator object that can be used to iterate through the collection.
        """
        ...

    def TryAdd(self, subscription: QuantConnect.Lean.Engine.DataFeeds.Subscription) -> bool:
        """
        Attempts to add the specified subscription to the collection. If another subscription
        exists with the same configuration then it won't be added.
        
        :param subscription: The subscription to add
        :returns: True if the subscription is successfully added, false otherwise.
        """
        ...

    def TryGetValue(self, configuration: QuantConnect.Data.SubscriptionDataConfig, subscription: typing.Optional[QuantConnect.Lean.Engine.DataFeeds.Subscription]) -> typing.Union[bool, QuantConnect.Lean.Engine.DataFeeds.Subscription]:
        """
        Attempts to retrieve the subscription with the specified configuration
        
        :param configuration: The subscription's configuration
        :param subscription: The subscription matching the configuration, null if not found
        :returns: True if the subscription is successfully retrieved, false otherwise.
        """
        ...

    def TryRemove(self, configuration: QuantConnect.Data.SubscriptionDataConfig, subscription: typing.Optional[QuantConnect.Lean.Engine.DataFeeds.Subscription]) -> typing.Union[bool, QuantConnect.Lean.Engine.DataFeeds.Subscription]:
        """
        Attempts to remove the subscription with the specified configuraton from the collection.
        
        :param configuration: The configuration of the subscription to remove
        :param subscription: The removed subscription, null if not found.
        :returns: True if the subscription is successfully removed, false otherwise.
        """
        ...

    def UpdateAndGetFillForwardResolution(self, configuration: QuantConnect.Data.SubscriptionDataConfig = None) -> QuantConnect.Util.Ref[datetime.timedelta]:
        """
        Gets and updates the fill forward resolution by checking specified subscription configurations and
        selecting the smallest resoluton not equal to tick
        """
        ...


class IDataFeedSubscriptionManager(metaclass=abc.ABCMeta):
    """DataFeedSubscriptionManager interface will manage the subscriptions for the Data Feed"""

    @property
    @abc.abstractmethod
    def SubscriptionAdded(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], None], None]:
        """Event fired when a new subscription is added"""
        ...

    @SubscriptionAdded.setter
    @abc.abstractmethod
    def SubscriptionAdded(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], None], None]):
        """Event fired when a new subscription is added"""
        ...

    @property
    @abc.abstractmethod
    def SubscriptionRemoved(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], None], None]:
        """Event fired when an existing subscription is removed"""
        ...

    @SubscriptionRemoved.setter
    @abc.abstractmethod
    def SubscriptionRemoved(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], None], None]):
        """Event fired when an existing subscription is removed"""
        ...

    @property
    @abc.abstractmethod
    def DataFeedSubscriptions(self) -> QuantConnect.Lean.Engine.DataFeeds.SubscriptionCollection:
        """Gets the data feed subscription collection"""
        ...

    @property
    @abc.abstractmethod
    def UniverseSelection(self) -> QuantConnect.Lean.Engine.DataFeeds.UniverseSelection:
        """Get the universe selection instance"""
        ...

    def AddSubscription(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest) -> bool:
        """
        Adds a new Subscription to provide data for the specified security.
        
        :param request: Defines the SubscriptionRequest to be added
        :returns: True if the subscription was created and added successfully, false otherwise.
        """
        ...

    def RemoveSubscription(self, configuration: QuantConnect.Data.SubscriptionDataConfig, universe: QuantConnect.Data.UniverseSelection.Universe = None) -> bool:
        """
        Removes the Subscription, if it exists
        
        :param configuration: The SubscriptionDataConfig of the subscription to remove
        :param universe: Universe requesting to remove Subscription. Default value, null, will remove all universes
        :returns: True if the subscription was successfully removed, false otherwise.
        """
        ...


class UniverseSelection(System.Object):
    """Provides methods for apply the results of universe selection to an algorithm"""

    def __init__(self, algorithm: QuantConnect.Interfaces.IAlgorithm, securityService: QuantConnect.Interfaces.ISecurityService, dataPermissionManager: QuantConnect.Interfaces.IDataPermissionManager, dataProvider: QuantConnect.Interfaces.IDataProvider, internalConfigResolution: QuantConnect.Resolution = ...) -> None:
        """
        Initializes a new instance of the UniverseSelection class
        
        :param algorithm: The algorithm to add securities to
        :param securityService: The security service
        :param dataPermissionManager: The data permissions manager
        :param dataProvider: The data provider to use
        :param internalConfigResolution: The resolution to use for internal configuration
        """
        ...

    def AddPendingInternalDataFeeds(self, utcStart: typing.Union[datetime.datetime, datetime.date]) -> bool:
        """
        Will add any pending internal currency subscriptions
        
        :param utcStart: The current date time in utc
        :returns: Will return true if any subscription was added.
        """
        ...

    def ApplyUniverseSelection(self, universe: QuantConnect.Data.UniverseSelection.Universe, dateTimeUtc: typing.Union[datetime.datetime, datetime.date], universeData: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> QuantConnect.Data.UniverseSelection.SecurityChanges:
        """
        Applies universe selection the the data feed and algorithm
        
        :param universe: The universe to perform selection on
        :param dateTimeUtc: The current date time in utc
        :param universeData: The data provided to perform selection with
        """
        ...

    def EnsureCurrencyDataFeeds(self, securityChanges: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """Checks the current subscriptions and adds necessary currency pair feeds to provide real time conversion data"""
        ...

    def SetDataManager(self, dataManager: QuantConnect.Lean.Engine.DataFeeds.IDataFeedSubscriptionManager) -> None:
        """Sets the data manager"""
        ...


class DownloaderDataProvider(QuantConnect.Lean.Engine.DataFeeds.BaseDownloaderDataProvider):
    """Data provider which downloads data using an IDataDownloader or IBrokerage implementation"""

    def __init__(self) -> None:
        """Creates a new instance"""
        ...

    def Fetch(self, key: str) -> System.IO.Stream:
        """
        Determines if it should downloads new data and retrieves data from disc
        
        :param key: A string representing where the data is stored
        :returns: A Stream of the data requested.
        """
        ...

    def NeedToDownload(self, filePath: str) -> bool:
        """
        Main filter to determine if this file needs to be downloaded
        
        This method is protected.
        
        :param filePath: File we are looking at
        :returns: True if should download.
        """
        ...


class BacktestingChainProvider(System.Object, metaclass=abc.ABCMeta):
    """Base backtesting cache provider which will source symbols from local zip files"""

    @property
    def DataCacheProvider(self) -> QuantConnect.Interfaces.IDataCacheProvider:
        """
        The data cache instance to use
        
        This property is protected.
        """
        ...

    def __init__(self, dataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider) -> None:
        """
        Creates a new instance
        
        This method is protected.
        """
        ...

    def GetSymbols(self, canonicalSymbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Get the contract symbols associated with the given canonical symbol and date
        
        This method is protected.
        
        :param canonicalSymbol: The canonical symbol
        :param date: The date to search for
        """
        ...


class CachingOptionChainProvider(System.Object, QuantConnect.Interfaces.IOptionChainProvider):
    """An implementation of IOptionChainProvider that will cache by date option contracts returned by another option chain provider."""

    def __init__(self, optionChainProvider: QuantConnect.Interfaces.IOptionChainProvider) -> None:
        """Initializes a new instance of the CachingOptionChainProvider class"""
        ...

    def GetOptionContractList(self, symbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Gets the list of option contracts for a given underlying symbol
        
        :param symbol: The underlying symbol
        :param date: The date for which to request the option chain (only used in backtesting)
        :returns: The list of option contracts.
        """
        ...


class DataFeedPacket(System.Object):
    """Defines a container type to hold data produced by a data feed subscription"""

    @property
    def Security(self) -> QuantConnect.Interfaces.ISecurityPrice:
        """The security"""
        ...

    @Security.setter
    def Security(self, value: QuantConnect.Interfaces.ISecurityPrice):
        """The security"""
        ...

    @property
    def Configuration(self) -> QuantConnect.Data.SubscriptionDataConfig:
        """The subscription configuration that produced this data"""
        ...

    @Configuration.setter
    def Configuration(self, value: QuantConnect.Data.SubscriptionDataConfig):
        """The subscription configuration that produced this data"""
        ...

    @property
    def Count(self) -> int:
        """Gets the number of data points held within this packet"""
        ...

    @property
    def Data(self) -> System.Collections.Generic.List[QuantConnect.Data.BaseData]:
        """The data for the security"""
        ...

    @property
    def IsSubscriptionRemoved(self) -> bool:
        """Gets whether or not this packet should be filtered out due to the subscription being removed"""
        ...

    @overload
    def __init__(self, security: QuantConnect.Interfaces.ISecurityPrice, configuration: QuantConnect.Data.SubscriptionDataConfig, isSubscriptionRemoved: QuantConnect.Util.IReadOnlyRef[bool] = None) -> None:
        """
        Initializes a new instance of the DataFeedPacket class
        
        :param security: The security whose data is held in this packet
        :param configuration: The subscription configuration that produced this data
        :param isSubscriptionRemoved: Reference to whether or not the subscription has since been removed, defaults to false
        """
        ...

    @overload
    def __init__(self, security: QuantConnect.Interfaces.ISecurityPrice, configuration: QuantConnect.Data.SubscriptionDataConfig, data: System.Collections.Generic.List[QuantConnect.Data.BaseData], isSubscriptionRemoved: QuantConnect.Util.IReadOnlyRef[bool] = None) -> None:
        """
        Initializes a new instance of the DataFeedPacket class
        
        :param security: The security whose data is held in this packet
        :param configuration: The subscription configuration that produced this data
        :param data: The data to add to this packet. The list reference is reused internally and NOT copied.
        :param isSubscriptionRemoved: Reference to whether or not the subscription has since been removed, defaults to false
        """
        ...

    def Add(self, data: QuantConnect.Data.BaseData) -> None:
        """
        Adds the specified data to this packet
        
        :param data: The data to be added to this packet
        """
        ...


class UpdateData(typing.Generic[QuantConnect_Lean_Engine_DataFeeds_UpdateData_T], System.Object):
    """
    Transport type for algorithm update data. This is intended to provide a
    list of base data used to perform updates against the specified target
    """

    @property
    def ContainsFillForwardData(self) -> typing.Optional[bool]:
        """Flag indicating whether Data contains any fill forward bar or not"""
        ...

    @property
    def Target(self) -> QuantConnect_Lean_Engine_DataFeeds_UpdateData_T:
        """The target, such as a security or subscription data config"""
        ...

    @property
    def Data(self) -> System.Collections.Generic.IReadOnlyList[QuantConnect.Data.BaseData]:
        """The data used to update the target"""
        ...

    @property
    def DataType(self) -> typing.Type:
        """The type of data in the data list"""
        ...

    @property
    def IsInternalConfig(self) -> bool:
        """
        True if this update data corresponds to an internal subscription
        such as currency or security benchmark
        """
        ...

    def __init__(self, target: QuantConnect_Lean_Engine_DataFeeds_UpdateData_T, dataType: typing.Type, data: System.Collections.Generic.IReadOnlyList[QuantConnect.Data.BaseData], isInternalConfig: bool, containsFillForwardData: typing.Optional[bool] = None) -> None:
        """
        Initializes a new instance of the UpdateData{T} class
        
        :param target: The end consumer/user of the dat
        :param dataType: The type of data in the list
        :param data: The update data
        :param isInternalConfig: True if this update data corresponds to an internal subscription such as currency or security benchmark
        :param containsFillForwardData: True if this update data contains fill forward bars
        """
        ...


class TimeSlice(System.Object):
    """Represents a grouping of data emitted at a certain time."""

    @property
    def DataPointCount(self) -> int:
        """Gets the count of data points in this TimeSlice"""
        ...

    @property
    def Time(self) -> datetime.datetime:
        """Gets the UTC time this data was emitted"""
        ...

    @property
    def Data(self) -> System.Collections.Generic.List[QuantConnect.Lean.Engine.DataFeeds.DataFeedPacket]:
        """Gets the data in the time slice"""
        ...

    @property
    def Slice(self) -> QuantConnect.Data.Slice:
        """Gets the Slice that will be used as input for the algorithm"""
        ...

    @property
    def SecuritiesUpdateData(self) -> System.Collections.Generic.List[QuantConnect.Lean.Engine.DataFeeds.UpdateData[QuantConnect.Interfaces.ISecurityPrice]]:
        """Gets the data used to update securities"""
        ...

    @property
    def ConsolidatorUpdateData(self) -> System.Collections.Generic.List[QuantConnect.Lean.Engine.DataFeeds.UpdateData[QuantConnect.Data.SubscriptionDataConfig]]:
        """Gets the data used to update the consolidators"""
        ...

    @property
    def CustomData(self) -> System.Collections.Generic.List[QuantConnect.Lean.Engine.DataFeeds.UpdateData[QuantConnect.Interfaces.ISecurityPrice]]:
        """Gets all the custom data in this TimeSlice"""
        ...

    @property
    def SecurityChanges(self) -> QuantConnect.Data.UniverseSelection.SecurityChanges:
        """Gets the changes to the data subscriptions as a result of universe selection"""
        ...

    @property
    def UniverseData(self) -> System.Collections.Generic.Dictionary[QuantConnect.Data.UniverseSelection.Universe, QuantConnect.Data.UniverseSelection.BaseDataCollection]:
        """Gets the universe data generated this time step."""
        ...

    @property
    def IsTimePulse(self) -> bool:
        """True indicates this time slice is a time pulse for the algorithm containing no data"""
        ...

    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], dataPointCount: int, slice: QuantConnect.Data.Slice, data: System.Collections.Generic.List[QuantConnect.Lean.Engine.DataFeeds.DataFeedPacket], securitiesUpdateData: System.Collections.Generic.List[QuantConnect.Lean.Engine.DataFeeds.UpdateData[QuantConnect.Interfaces.ISecurityPrice]], consolidatorUpdateData: System.Collections.Generic.List[QuantConnect.Lean.Engine.DataFeeds.UpdateData[QuantConnect.Data.SubscriptionDataConfig]], customData: System.Collections.Generic.List[QuantConnect.Lean.Engine.DataFeeds.UpdateData[QuantConnect.Interfaces.ISecurityPrice]], securityChanges: QuantConnect.Data.UniverseSelection.SecurityChanges, universeData: System.Collections.Generic.Dictionary[QuantConnect.Data.UniverseSelection.Universe, QuantConnect.Data.UniverseSelection.BaseDataCollection], isTimePulse: bool = False) -> None:
        """Initializes a new TimeSlice containing the specified data"""
        ...


class TimeSliceFactory(System.Object):
    """Instance base class that will provide methods for creating new TimeSlice"""

    def __init__(self, timeZone: typing.Any) -> None:
        """
        Creates a new instance
        
        :param timeZone: The time zone required for computing algorithm and slice time
        """
        ...

    def Create(self, utcDateTime: typing.Union[datetime.datetime, datetime.date], data: System.Collections.Generic.List[QuantConnect.Lean.Engine.DataFeeds.DataFeedPacket], changes: QuantConnect.Data.UniverseSelection.SecurityChanges, universeData: System.Collections.Generic.Dictionary[QuantConnect.Data.UniverseSelection.Universe, QuantConnect.Data.UniverseSelection.BaseDataCollection]) -> QuantConnect.Lean.Engine.DataFeeds.TimeSlice:
        """
        Creates a new TimeSlice for the specified time using the specified data
        
        :param utcDateTime: The UTC frontier date time
        :param data: The data in this TimeSlice
        :param changes: The new changes that are seen in this time slice as a result of universe selection
        :returns: A new TimeSlice containing the specified data.
        """
        ...

    def CreateTimePulse(self, utcDateTime: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Lean.Engine.DataFeeds.TimeSlice:
        """
        Creates a new empty TimeSlice to be used as a time pulse
        
        :param utcDateTime: The UTC frontier date time
        :returns: A new TimeSlice time pulse.
        """
        ...


class IDataFeedTimeProvider(metaclass=abc.ABCMeta):
    """Reduced interface which exposes required ITimeProvider for IDataFeed implementations"""

    @property
    @abc.abstractmethod
    def TimeProvider(self) -> QuantConnect.ITimeProvider:
        """Continuous UTC time provider"""
        ...

    @property
    @abc.abstractmethod
    def FrontierTimeProvider(self) -> QuantConnect.ITimeProvider:
        """Time provider which returns current UTC frontier time"""
        ...


class IDataFeed(metaclass=abc.ABCMeta):
    """Datafeed interface for creating custom datafeed sources."""

    @property
    @abc.abstractmethod
    def IsActive(self) -> bool:
        """Public flag indicator that the thread is still busy."""
        ...

    def CreateSubscription(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest) -> QuantConnect.Lean.Engine.DataFeeds.Subscription:
        """
        Creates a new subscription to provide data for the specified security.
        
        :param request: Defines the subscription to be added, including start/end times the universe and security
        :returns: The created Subscription if successful, null otherwise.
        """
        ...

    def Exit(self) -> None:
        """External controller calls to signal a terminate of the thread."""
        ...

    def Initialize(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.AlgorithmNodePacket, resultHandler: QuantConnect.Lean.Engine.Results.IResultHandler, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider, factorFileProvider: QuantConnect.Interfaces.IFactorFileProvider, dataProvider: QuantConnect.Interfaces.IDataProvider, subscriptionManager: QuantConnect.Lean.Engine.DataFeeds.IDataFeedSubscriptionManager, dataFeedTimeProvider: QuantConnect.Lean.Engine.DataFeeds.IDataFeedTimeProvider, dataChannelProvider: QuantConnect.Interfaces.IDataChannelProvider) -> None:
        """Initializes the data feed for the specified job and algorithm"""
        ...

    def RemoveSubscription(self, subscription: QuantConnect.Lean.Engine.DataFeeds.Subscription) -> None:
        """
        Removes the subscription from the data feed, if it exists
        
        :param subscription: The subscription to remove
        """
        ...


class FileSystemDataFeed(System.Object, QuantConnect.Lean.Engine.DataFeeds.IDataFeed):
    """Historical datafeed stream reader for processing files on a local disk."""

    @property
    def IsActive(self) -> bool:
        """Flag indicating the hander thread is completely finished and ready to dispose."""
        ...

    @IsActive.setter
    def IsActive(self, value: bool):
        """Flag indicating the hander thread is completely finished and ready to dispose."""
        ...

    def ConfigureEnumerator(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, aggregate: bool, enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], fillForwardResolution: typing.Optional[QuantConnect.Resolution]) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Configure the enumerator with aggregation/fill-forward/filter behaviors. Returns new instance if re-configured
        
        This method is protected.
        """
        ...

    def CreateEnumerator(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, fillForwardResolution: typing.Optional[QuantConnect.Resolution] = None) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Creates a file based data enumerator for the given subscription request
        
        This method is protected.
        """
        ...

    def CreateSubscription(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest) -> QuantConnect.Lean.Engine.DataFeeds.Subscription:
        """
        Creates a new subscription to provide data for the specified security.
        
        :param request: Defines the subscription to be added, including start/end times the universe and security
        :returns: The created Subscription if successful, null otherwise.
        """
        ...

    def CreateUniverseEnumerator(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, createUnderlyingEnumerator: typing.Callable[[QuantConnect.Data.UniverseSelection.SubscriptionRequest, typing.Optional[QuantConnect.Resolution]], System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]], fillForwardResolution: typing.Optional[QuantConnect.Resolution] = None) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """This method is protected."""
        ...

    def Exit(self) -> None:
        """Send an exit signal to the thread."""
        ...

    def Initialize(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.AlgorithmNodePacket, resultHandler: QuantConnect.Lean.Engine.Results.IResultHandler, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider, factorFileProvider: QuantConnect.Interfaces.IFactorFileProvider, dataProvider: QuantConnect.Interfaces.IDataProvider, subscriptionManager: QuantConnect.Lean.Engine.DataFeeds.IDataFeedSubscriptionManager, dataFeedTimeProvider: QuantConnect.Lean.Engine.DataFeeds.IDataFeedTimeProvider, dataChannelProvider: QuantConnect.Interfaces.IDataChannelProvider) -> None:
        """Initializes the data feed for the specified job and algorithm"""
        ...

    def RemoveSubscription(self, subscription: QuantConnect.Lean.Engine.DataFeeds.Subscription) -> None:
        """
        Removes the subscription from the data feed, if it exists
        
        :param subscription: The subscription to remove
        """
        ...

    def TryAddFillForwardEnumerator(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], fillForward: bool, fillForwardResolution: typing.Optional[QuantConnect.Resolution]) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Will add a fill forward enumerator if requested
        
        This method is protected.
        """
        ...

    def TryAppendUnderlyingEnumerator(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, parent: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], createEnumerator: typing.Callable[[QuantConnect.Data.UniverseSelection.SubscriptionRequest, typing.Optional[QuantConnect.Resolution]], System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]], fillForwardResolution: typing.Optional[QuantConnect.Resolution]) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        If required will add a new enumerator for the underlying symbol
        
        This method is protected.
        """
        ...


class IDataManager(metaclass=abc.ABCMeta):
    """IDataManager is the engines view of the Data Manager."""

    @property
    @abc.abstractmethod
    def UniverseSelection(self) -> QuantConnect.Lean.Engine.DataFeeds.UniverseSelection:
        """Get the universe selection instance"""
        ...


class PrecalculatedSubscriptionData(QuantConnect.Lean.Engine.DataFeeds.SubscriptionData):
    """Store data both raw and adjusted and the time at which it should be synchronized"""

    @property
    def Data(self) -> QuantConnect.Data.BaseData:
        """Gets the data"""
        ...

    def __init__(self, configuration: QuantConnect.Data.SubscriptionDataConfig, rawData: QuantConnect.Data.BaseData, normalizedData: QuantConnect.Data.BaseData, normalizationMode: QuantConnect.DataNormalizationMode, emitTimeUtc: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the PrecalculatedSubscriptionData class
        
        :param configuration: The subscription's configuration
        :param rawData: The base data
        :param normalizedData: The normalized calculated based on raw data
        :param normalizationMode: Specifies how data is normalized
        :param emitTimeUtc: The emit time for the data
        """
        ...


class ApiDataProvider(QuantConnect.Lean.Engine.DataFeeds.BaseDownloaderDataProvider):
    """An instance of the IDataProvider that will download and update data files as needed via QC's Api."""

    def __init__(self) -> None:
        """Initialize a new instance of the ApiDataProvider"""
        ...

    def DownloadData(self, filePath: str) -> bool:
        """
        Attempt to download data using the Api for and return a FileStream of that data.
        
        This method is protected.
        
        :param filePath: The path to store the file
        :returns: A FileStream of the data.
        """
        ...

    def Fetch(self, key: str) -> System.IO.Stream:
        """
        Retrieves data to be used in an algorithm.
        If file does not exist, an attempt is made to download them from the api
        
        :param key: File path representing where the data requested
        :returns: A Stream of the data requested.
        """
        ...

    def NeedToDownload(self, filePath: str) -> bool:
        """
        Main filter to determine if this file needs to be downloaded
        
        This method is protected.
        
        :param filePath: File we are looking at
        :returns: True if should download.
        """
        ...


class SubscriptionFrontierTimeProvider(System.Object, QuantConnect.ITimeProvider):
    """A time provider which updates 'now' time based on the current data emit time of all subscriptions"""

    def __init__(self, utcNow: typing.Union[datetime.datetime, datetime.date], subscriptionManager: QuantConnect.Lean.Engine.DataFeeds.IDataFeedSubscriptionManager) -> None:
        """
        Creates a new instance of the SubscriptionFrontierTimeProvider
        
        :param utcNow: Initial UTC now time
        :param subscriptionManager: Subscription manager. Will be used to obtain current subscriptions
        """
        ...

    def GetUtcNow(self) -> datetime.datetime:
        """
        Gets the current time in UTC
        
        :returns: The current time in UTC.
        """
        ...


class BacktestingFutureChainProvider(QuantConnect.Lean.Engine.DataFeeds.BacktestingChainProvider, QuantConnect.Interfaces.IFutureChainProvider):
    """An implementation of IFutureChainProvider that reads the list of contracts from open interest zip data files"""

    def __init__(self, dataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider) -> None:
        """
        Creates a new instance
        
        :param dataCacheProvider: The data cache provider instance to use
        """
        ...

    def GetFutureContractList(self, symbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Gets the list of future contracts for a given underlying symbol
        
        :param symbol: The underlying symbol
        :param date: The date for which to request the future chain (only used in backtesting)
        :returns: The list of future contracts.
        """
        ...

    @staticmethod
    def GetSymbol(symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Symbol:
        """
        Helper method to get the symbol to use
        
        This method is protected.
        """
        ...


class ISubscriptionSynchronizer(metaclass=abc.ABCMeta):
    """Provides the ability to synchronize subscriptions into time slices"""

    @property
    @abc.abstractmethod
    def SubscriptionFinished(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], None], None]:
        """Event fired when a subscription is finished"""
        ...

    @SubscriptionFinished.setter
    @abc.abstractmethod
    def SubscriptionFinished(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], None], None]):
        """Event fired when a subscription is finished"""
        ...

    def Sync(self, subscriptions: System.Collections.Generic.IEnumerable[QuantConnect.Lean.Engine.DataFeeds.Subscription], cancellationToken: System.Threading.CancellationToken) -> System.Collections.Generic.IEnumerable[QuantConnect.Lean.Engine.DataFeeds.TimeSlice]:
        """
        Syncs the specified subscriptions. The frontier time used for synchronization is
        managed internally and dependent upon previous synchronization operations.
        
        :param subscriptions: The subscriptions to sync
        :param cancellationToken: The cancellation token to stop enumeration
        """
        ...


class SubscriptionSynchronizer(System.Object, QuantConnect.Lean.Engine.DataFeeds.ISubscriptionSynchronizer, QuantConnect.ITimeProvider):
    """Provides the ability to synchronize subscriptions into time slices"""

    @property
    def SubscriptionFinished(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], None], None]:
        """Event fired when a Subscription is finished"""
        ...

    @SubscriptionFinished.setter
    def SubscriptionFinished(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], None], None]):
        """Event fired when a Subscription is finished"""
        ...

    def __init__(self, universeSelection: QuantConnect.Lean.Engine.DataFeeds.UniverseSelection) -> None:
        """
        Initializes a new instance of the SubscriptionSynchronizer class
        
        :param universeSelection: The universe selection instance used to handle universe selection subscription output
        :returns: A time slice for the specified frontier time.
        """
        ...

    def GetUtcNow(self) -> datetime.datetime:
        """Returns the current UTC frontier time"""
        ...

    def OnSubscriptionFinished(self, subscription: QuantConnect.Lean.Engine.DataFeeds.Subscription) -> None:
        """
        Event invocator for the SubscriptionFinished event
        
        This method is protected.
        """
        ...

    def SetTimeProvider(self, timeProvider: QuantConnect.ITimeProvider) -> None:
        """
        Sets the time provider. If already set will throw.
        
        :param timeProvider: The time provider, used to obtain the current frontier UTC value
        """
        ...

    def SetTimeSliceFactory(self, timeSliceFactory: QuantConnect.Lean.Engine.DataFeeds.TimeSliceFactory) -> None:
        """
        Sets the TimeSliceFactory instance to use
        
        :param timeSliceFactory: Used to create the new TimeSlice
        """
        ...

    def Sync(self, subscriptions: System.Collections.Generic.IEnumerable[QuantConnect.Lean.Engine.DataFeeds.Subscription], cancellationToken: System.Threading.CancellationToken) -> System.Collections.Generic.IEnumerable[QuantConnect.Lean.Engine.DataFeeds.TimeSlice]:
        """
        Syncs the specified subscriptions. The frontier time used for synchronization is
        managed internally and dependent upon previous synchronization operations.
        
        :param subscriptions: The subscriptions to sync
        :param cancellationToken: The cancellation token to stop enumeration
        """
        ...


class SubscriptionDataReader(System.Object, QuantConnect.Lean.Engine.DataFeeds.Enumerators.ITradableDatesNotifier, QuantConnect.Interfaces.IDataProviderEvents):
    """Subscription data reader is a wrapper on the stream reader class to download, unpack and iterate over a data file."""

    @property
    def InvalidConfigurationDetected(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.InvalidConfigurationDetectedEventArgs], None], None]:
        """Event fired when an invalid configuration has been detected"""
        ...

    @InvalidConfigurationDetected.setter
    def InvalidConfigurationDetected(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.InvalidConfigurationDetectedEventArgs], None], None]):
        """Event fired when an invalid configuration has been detected"""
        ...

    @property
    def NumericalPrecisionLimited(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.NumericalPrecisionLimitedEventArgs], None], None]:
        """Event fired when the numerical precision in the factor file has been limited"""
        ...

    @NumericalPrecisionLimited.setter
    def NumericalPrecisionLimited(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.NumericalPrecisionLimitedEventArgs], None], None]):
        """Event fired when the numerical precision in the factor file has been limited"""
        ...

    @property
    def StartDateLimited(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.StartDateLimitedEventArgs], None], None]:
        """Event fired when the start date has been limited"""
        ...

    @StartDateLimited.setter
    def StartDateLimited(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.StartDateLimitedEventArgs], None], None]):
        """Event fired when the start date has been limited"""
        ...

    @property
    def DownloadFailed(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.DownloadFailedEventArgs], None], None]:
        """Event fired when there was an error downloading a remote file"""
        ...

    @DownloadFailed.setter
    def DownloadFailed(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.DownloadFailedEventArgs], None], None]):
        """Event fired when there was an error downloading a remote file"""
        ...

    @property
    def ReaderErrorDetected(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.ReaderErrorDetectedEventArgs], None], None]:
        """Event fired when there was an error reading the data"""
        ...

    @ReaderErrorDetected.setter
    def ReaderErrorDetected(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.ReaderErrorDetectedEventArgs], None], None]):
        """Event fired when there was an error reading the data"""
        ...

    @property
    def NewTradableDate(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.NewTradableDateEventArgs], None], None]:
        """Event fired when there is a new tradable date"""
        ...

    @NewTradableDate.setter
    def NewTradableDate(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.NewTradableDateEventArgs], None], None]):
        """Event fired when there is a new tradable date"""
        ...

    @property
    def Current(self) -> QuantConnect.Data.BaseData:
        """Last read BaseData object from this type and source"""
        ...

    @Current.setter
    def Current(self, value: QuantConnect.Data.BaseData):
        """Last read BaseData object from this type and source"""
        ...

    def __init__(self, config: QuantConnect.Data.SubscriptionDataConfig, dataRequest: QuantConnect.Data.BaseDataRequest, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider, factorFileProvider: QuantConnect.Interfaces.IFactorFileProvider, dataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider, dataProvider: QuantConnect.Interfaces.IDataProvider) -> None:
        """
        Subscription data reader takes a subscription request, loads the type, accepts the data source and enumerate on the results.
        
        :param config: Subscription configuration object
        :param dataRequest: The data request
        :param mapFileProvider: Used for resolving the correct map files
        :param factorFileProvider: Used for getting factor files
        :param dataCacheProvider: Used for caching files
        :param dataProvider: The data provider to use
        """
        ...

    def Dispose(self) -> None:
        """Dispose of the Stream Reader and close out the source stream and file connections."""
        ...

    def Initialize(self) -> None:
        """Initializes the SubscriptionDataReader instance"""
        ...

    def MoveNext(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        ...

    def OnDownloadFailed(self, e: QuantConnect.DownloadFailedEventArgs) -> None:
        """
        Event invocator for the DownloadFailed event
        
        This method is protected.
        
        :param e: Event arguments for the DownloadFailed event
        """
        ...

    def OnInvalidConfigurationDetected(self, e: QuantConnect.InvalidConfigurationDetectedEventArgs) -> None:
        """
        Event invocator for the InvalidConfigurationDetected event
        
        This method is protected.
        
        :param e: Event arguments for the InvalidConfigurationDetected event
        """
        ...

    def OnNewTradableDate(self, e: QuantConnect.NewTradableDateEventArgs) -> None:
        """
        Event invocator for the NewTradableDate event
        
        This method is protected.
        
        :param e: Event arguments for the NewTradableDate event
        """
        ...

    def OnNumericalPrecisionLimited(self, e: QuantConnect.NumericalPrecisionLimitedEventArgs) -> None:
        """
        Event invocator for the NumericalPrecisionLimited event
        
        This method is protected.
        
        :param e: Event arguments for the NumericalPrecisionLimited event
        """
        ...

    def OnReaderErrorDetected(self, e: QuantConnect.ReaderErrorDetectedEventArgs) -> None:
        """
        Event invocator for the ReaderErrorDetected event
        
        This method is protected.
        
        :param e: Event arguments for the ReaderErrorDetected event
        """
        ...

    def OnStartDateLimited(self, e: QuantConnect.StartDateLimitedEventArgs) -> None:
        """
        Event invocator for the StartDateLimited event
        
        This method is protected.
        
        :param e: Event arguments for the StartDateLimited event
        """
        ...

    def Reset(self) -> None:
        """Reset the IEnumeration"""
        ...


class DataManager(System.Object, QuantConnect.Interfaces.IAlgorithmSubscriptionManager, QuantConnect.Lean.Engine.DataFeeds.IDataFeedSubscriptionManager, QuantConnect.Lean.Engine.DataFeeds.IDataManager):
    """DataManager will manage the subscriptions for both the DataFeeds and the SubscriptionManager"""

    @property
    def SubscriptionAdded(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], None], None]:
        """Event fired when a new subscription is added"""
        ...

    @SubscriptionAdded.setter
    def SubscriptionAdded(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], None], None]):
        """Event fired when a new subscription is added"""
        ...

    @property
    def SubscriptionRemoved(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], None], None]:
        """Event fired when an existing subscription is removed"""
        ...

    @SubscriptionRemoved.setter
    def SubscriptionRemoved(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.Subscription], None], None]):
        """Event fired when an existing subscription is removed"""
        ...

    @property
    def DataFeedSubscriptions(self) -> QuantConnect.Lean.Engine.DataFeeds.SubscriptionCollection:
        ...

    @property
    def SubscriptionManagerSubscriptions(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.SubscriptionDataConfig]:
        ...

    @property
    def AvailableDataTypes(self) -> System.Collections.Generic.Dictionary[QuantConnect.SecurityType, System.Collections.Generic.List[QuantConnect.TickType]]:
        ...

    @property
    def UniverseSelection(self) -> QuantConnect.Lean.Engine.DataFeeds.UniverseSelection:
        ...

    def __init__(self, dataFeed: QuantConnect.Lean.Engine.DataFeeds.IDataFeed, universeSelection: QuantConnect.Lean.Engine.DataFeeds.UniverseSelection, algorithm: QuantConnect.Interfaces.IAlgorithm, timeKeeper: QuantConnect.Interfaces.ITimeKeeper, marketHoursDatabase: QuantConnect.Securities.MarketHoursDatabase, liveMode: bool, registeredTypesProvider: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, dataPermissionManager: QuantConnect.Interfaces.IDataPermissionManager) -> None:
        """Creates a new instance of the DataManager"""
        ...

    @overload
    def Add(self, dataType: typing.Type, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, fillForward: bool = True, extendedMarketHours: bool = False, isFilteredSubscription: bool = True, isInternalFeed: bool = False, isCustomData: bool = False, dataNormalizationMode: QuantConnect.DataNormalizationMode = ..., dataMappingMode: QuantConnect.DataMappingMode = ..., contractDepthOffset: int = 0) -> QuantConnect.Data.SubscriptionDataConfig:
        """
        Creates and adds a list of SubscriptionDataConfig for a given symbol and configuration.
        Can optionally pass in desired subscription data type to use.
        If the config already existed will return existing instance instead
        """
        ...

    @overload
    def Add(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, fillForward: bool = True, extendedMarketHours: bool = False, isFilteredSubscription: bool = True, isInternalFeed: bool = False, isCustomData: bool = False, subscriptionDataTypes: System.Collections.Generic.List[System.Tuple[typing.Type, QuantConnect.TickType]] = None, dataNormalizationMode: QuantConnect.DataNormalizationMode = ..., dataMappingMode: QuantConnect.DataMappingMode = ..., contractDepthOffset: int = 0) -> System.Collections.Generic.List[QuantConnect.Data.SubscriptionDataConfig]:
        """
        Creates and adds a list of SubscriptionDataConfig for a given symbol and configuration.
        Can optionally pass in desired subscription data types to use.
         If the config already existed will return existing instance instead
        """
        ...

    def AddSubscription(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest) -> bool:
        """
        Adds a new Subscription to provide data for the specified security.
        
        :param request: Defines the SubscriptionRequest to be added
        :returns: True if the subscription was created and added successfully, false otherwise.
        """
        ...

    def GetSubscriptionDataConfigs(self, symbol: typing.Union[QuantConnect.Symbol, str], includeInternalConfigs: bool = False) -> System.Collections.Generic.List[QuantConnect.Data.SubscriptionDataConfig]:
        """Gets a list of all registered SubscriptionDataConfig for a given Symbol"""
        ...

    def LookupSubscriptionConfigDataTypes(self, symbolSecurityType: QuantConnect.SecurityType, resolution: QuantConnect.Resolution, isCanonical: bool) -> System.Collections.Generic.List[System.Tuple[typing.Type, QuantConnect.TickType]]:
        """
        Get the data feed types for a given SecurityTypeResolution
        
        :param symbolSecurityType: The SecurityType used to determine the types
        :param resolution: The resolution of the data requested
        :param isCanonical: Indicates whether the security is Canonical (future and options)
        :returns: Types that should be added to the SubscriptionDataConfig.
        """
        ...

    def RemoveAllSubscriptions(self) -> None:
        """Will remove all current Subscription"""
        ...

    def RemoveSubscription(self, configuration: QuantConnect.Data.SubscriptionDataConfig, universe: QuantConnect.Data.UniverseSelection.Universe = None) -> bool:
        """
        Removes the Subscription, if it exists
        
        :param configuration: The SubscriptionDataConfig of the subscription to remove
        :param universe: Universe requesting to remove Subscription. Default value, null, will remove all universes
        :returns: True if the subscription was successfully removed, false otherwise.
        """
        ...

    def SubscriptionManagerCount(self) -> int:
        """Returns the amount of data config subscriptions processed for the SubscriptionManager"""
        ...

    def SubscriptionManagerGetOrAdd(self, newConfig: QuantConnect.Data.SubscriptionDataConfig) -> QuantConnect.Data.SubscriptionDataConfig:
        """
        Gets existing or adds new SubscriptionDataConfig
        
        :returns: Returns the SubscriptionDataConfig instance used.
        """
        ...


class ZipEntryNameSubscriptionDataSourceReader(System.Object, QuantConnect.Lean.Engine.DataFeeds.ISubscriptionDataSourceReader):
    """Provides an implementation of ISubscriptionDataSourceReader that reads zip entry names"""

    @property
    def InvalidSource(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.InvalidSourceEventArgs], None], None]:
        """
        Event fired when the specified source is considered invalid, this may
        be from a missing file or failure to download a remote source
        """
        ...

    @InvalidSource.setter
    def InvalidSource(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Lean.Engine.DataFeeds.InvalidSourceEventArgs], None], None]):
        """
        Event fired when the specified source is considered invalid, this may
        be from a missing file or failure to download a remote source
        """
        ...

    def __init__(self, dataProvider: QuantConnect.Interfaces.IDataCacheProvider, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> None:
        """
        Initializes a new instance of the ZipEntryNameSubscriptionDataSourceReader class
        
        :param dataProvider: Used to fetch data
        :param config: The subscription's configuration
        :param date: The date this factory was produced to read data for
        :param isLiveMode: True if we're in live mode, false for backtesting
        """
        ...

    def Read(self, source: QuantConnect.Data.SubscriptionDataSource) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]:
        """
        Reads the specified
        
        :param source: The source to be read
        :returns: An IEnumerable{BaseData} that contains the data in the source.
        """
        ...


class AggregationManager(System.Object, QuantConnect.Data.IDataAggregator):
    """
    Aggregates ticks and bars based on given subscriptions.
    Current implementation is based on IDataConsolidator that consolidates ticks and put them into enumerator.
    """

    @property
    def TimeProvider(self) -> QuantConnect.ITimeProvider:
        """
        Continuous UTC time provider
        
        This property is protected.
        """
        ...

    @TimeProvider.setter
    def TimeProvider(self, value: QuantConnect.ITimeProvider):
        """
        Continuous UTC time provider
        
        This property is protected.
        """
        ...

    def Add(self, dataConfig: QuantConnect.Data.SubscriptionDataConfig, newDataAvailableHandler: typing.Callable[[System.Object, System.EventArgs], None]) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Add new subscription to current IDataAggregator instance
        
        :param dataConfig: defines the parameters to subscribe to a data feed
        :param newDataAvailableHandler: handler to be fired on new data available
        :returns: The new enumerator for this subscription request.
        """
        ...

    def Dispose(self) -> None:
        """Dispose of the aggregation manager."""
        ...

    def Remove(self, dataConfig: QuantConnect.Data.SubscriptionDataConfig) -> bool:
        """
        Removes the handler with the specified identifier
        
        :param dataConfig: Subscription data configuration to be removed
        """
        ...

    def Update(self, input: QuantConnect.Data.BaseData) -> None:
        """
        Add new data to aggregator
        
        :param input: The new data
        """
        ...


class CurrencySubscriptionDataConfigManager(System.Object):
    """
    Helper class to keep track of required internal currency SubscriptionDataConfig.
    This class is used by the UniverseSelection
    """

    def __init__(self, cashBook: QuantConnect.Securities.CashBook, securityManager: QuantConnect.Securities.SecurityManager, subscriptionManager: QuantConnect.Data.SubscriptionManager, securityService: QuantConnect.Interfaces.ISecurityService, defaultResolution: QuantConnect.Resolution) -> None:
        """
        Creates a new instance
        
        :param cashBook: The cash book instance
        :param securityManager: The SecurityManager, required by the cash book for creating new securities
        :param subscriptionManager: The SubscriptionManager, required by the cash book for creating new subscription data configs
        :param securityService: The SecurityService, required by the cash book for creating new securities
        :param defaultResolution: The default resolution to use for the internal subscriptions
        """
        ...

    def EnsureCurrencySubscriptionDataConfigs(self, securityChanges: QuantConnect.Data.UniverseSelection.SecurityChanges, brokerageModel: QuantConnect.Brokerages.IBrokerageModel) -> None:
        """Checks the current SubscriptionDataConfig and adds new necessary currency pair feeds to provide real time conversion data"""
        ...

    def GetPendingSubscriptionDataConfigs(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.SubscriptionDataConfig]:
        """
        Will return any pending internal currency SubscriptionDataConfig and remove them as pending.
        
        :returns: Will return the SubscriptionDataConfig to be added.
        """
        ...

    def GetSubscriptionDataConfigToRemove(self, addedSymbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.SubscriptionDataConfig:
        """
        Will verify if there are any SubscriptionDataConfig to be removed
        for a given added Symbol.
        
        :param addedSymbol: The symbol that was added to the data feed system
        :returns: The SubscriptionDataConfig to be removed, null if none.
        """
        ...

    def UpdatePendingSubscriptionDataConfigs(self, brokerageModel: QuantConnect.Brokerages.IBrokerageModel) -> bool:
        """
        Will update pending currency SubscriptionDataConfig
        
        :returns: True when there are pending currency subscriptions GetPendingSubscriptionDataConfigs.
        """
        ...


class PredicateTimeProvider(System.Object, QuantConnect.ITimeProvider):
    """
    Will generate time steps around the desired ITimeProvider
    Provided step evaluator should return true when the next time step
    is valid and time can advance
    """

    def __init__(self, underlyingTimeProvider: QuantConnect.ITimeProvider, customStepEvaluator: typing.Callable[[datetime.datetime], bool]) -> None:
        """
        Creates a new instance
        
        :param underlyingTimeProvider: The timer provider instance to wrap
        :param customStepEvaluator: Function to evaluate whether or not to advance time. Should return true if provided DateTime is a valid new next time. False will avoid time advancing
        """
        ...

    def GetUtcNow(self) -> datetime.datetime:
        """Gets the current utc time step"""
        ...


class BacktestingOptionChainProvider(QuantConnect.Lean.Engine.DataFeeds.BacktestingChainProvider, QuantConnect.Interfaces.IOptionChainProvider):
    """An implementation of IOptionChainProvider that reads the list of contracts from open interest zip data files"""

    def __init__(self, dataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider) -> None:
        """
        Creates a new instance
        
        :param dataCacheProvider: The data cache provider instance to use
        :param mapFileProvider: The map file provider instance to use
        """
        ...

    def GetOptionContractList(self, symbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Gets the list of option contracts for a given underlying symbol
        
        :param symbol: The underlying symbol
        :param date: The date for which to request the option chain (only used in backtesting)
        :returns: The list of option contracts.
        """
        ...


class NullDataFeed(System.Object, QuantConnect.Lean.Engine.DataFeeds.IDataFeed):
    """Null data feed implementation."""

    @property
    def ShouldThrow(self) -> bool:
        """Allows specifying if this implementation should throw always or not"""
        ...

    @ShouldThrow.setter
    def ShouldThrow(self, value: bool):
        """Allows specifying if this implementation should throw always or not"""
        ...

    @property
    def IsActive(self) -> bool:
        ...

    def CreateSubscription(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest) -> QuantConnect.Lean.Engine.DataFeeds.Subscription:
        ...

    def Exit(self) -> None:
        ...

    def Initialize(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.AlgorithmNodePacket, resultHandler: QuantConnect.Lean.Engine.Results.IResultHandler, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider, factorFileProvider: QuantConnect.Interfaces.IFactorFileProvider, dataProvider: QuantConnect.Interfaces.IDataProvider, subscriptionManager: QuantConnect.Lean.Engine.DataFeeds.IDataFeedSubscriptionManager, dataFeedTimeProvider: QuantConnect.Lean.Engine.DataFeeds.IDataFeedTimeProvider, channelProvider: QuantConnect.Interfaces.IDataChannelProvider) -> None:
        ...

    def RemoveSubscription(self, subscription: QuantConnect.Lean.Engine.DataFeeds.Subscription) -> None:
        ...


class LiveFutureChainProvider(QuantConnect.Lean.Engine.DataFeeds.BacktestingFutureChainProvider):
    """
    An implementation of IFutureChainProvider that fetches the list of contracts
    from an external source
    """

    def __init__(self, dataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider) -> None:
        """
        Creates a new instance
        
        :param dataCacheProvider: The data cache provider instance to use
        """
        ...

    def GetFutureContractList(self, symbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Gets the list of future contracts for a given underlying symbol
        
        :param symbol: The underlying symbol
        :param date: The date for which to request the future chain (only used in backtesting)
        :returns: The list of future contracts.
        """
        ...


class ZipDataCacheProvider(System.Object, QuantConnect.Interfaces.IDataCacheProvider):
    """File provider implements optimized zip archives caching facility. Cache is thread safe."""

    @property
    def IsDataEphemeral(self) -> bool:
        """Property indicating the data is temporary in nature and should not be cached."""
        ...

    def __init__(self, dataProvider: QuantConnect.Interfaces.IDataProvider, isDataEphemeral: bool = True, cacheTimer: float = 10) -> None:
        """Constructor that sets the IDataProvider used to retrieve data"""
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def Fetch(self, key: str) -> System.IO.Stream:
        """Does not attempt to retrieve any data"""
        ...

    def GetZipEntries(self, zipFile: str) -> System.Collections.Generic.List[str]:
        """Returns a list of zip entries in a provided zip file"""
        ...

    def Store(self, key: str, data: typing.List[int]) -> None:
        """
        Store the data in the cache.
        
        :param key: The source of the data, used as a key to retrieve data in the cache
        :param data: The data as a byte array
        """
        ...


class SubscriptionDataSourceReader(System.Object):
    """Provides a factory method for creating ISubscriptionDataSourceReader instances"""

    @staticmethod
    def CheckRemoteFileCache() -> None:
        """Creates cache directory if not existing and deletes old files from the cache"""
        ...

    @staticmethod
    def ForSource(source: QuantConnect.Data.SubscriptionDataSource, dataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool, factory: QuantConnect.Data.BaseData, dataProvider: QuantConnect.Interfaces.IDataProvider) -> QuantConnect.Lean.Engine.DataFeeds.ISubscriptionDataSourceReader:
        """
        Creates a new ISubscriptionDataSourceReader capable of handling the specified
        
        :param source: The subscription data source to create a factory for
        :param dataCacheProvider: Used to cache data
        :param config: The configuration of the subscription
        :param date: The date to be processed
        :param isLiveMode: True for live mode, false otherwise
        :param factory: The base data instance factory
        :param dataProvider: The data provider to use
        :returns: A new ISubscriptionDataSourceReader that can read the specified.
        """
        ...


class ManualTimeProvider(System.Object, QuantConnect.ITimeProvider):
    """
    Provides an implementation of ITimeProvider that can be
    manually advanced through time
    """

    @overload
    def __init__(self, setCurrentTimeTimeZone: typing.Any = None) -> None:
        """
        Initializes a new instance of the ManualTimeProvider
        
        :param setCurrentTimeTimeZone: Specify to use this time zone when calling SetCurrentTime, leave null for the default of TimeZones.Utc
        """
        ...

    @overload
    def __init__(self, currentTime: typing.Union[datetime.datetime, datetime.date], setCurrentTimeTimeZone: typing.Any = None) -> None:
        """
        Initializes a new instance of the ManualTimeProvider class
        
        :param currentTime: The current time in the specified time zone, if the time zone is null then the time is interpreted as being in TimeZones.Utc
        :param setCurrentTimeTimeZone: Specify to use this time zone when calling SetCurrentTime, leave null for the default of TimeZones.Utc
        """
        ...

    def Advance(self, span: datetime.timedelta) -> None:
        """
        Advances the current time by the specified span
        
        :param span: The amount of time to advance the current time by
        """
        ...

    def AdvanceSeconds(self, seconds: float) -> None:
        """
        Advances the current time by the specified number of seconds
        
        :param seconds: The number of seconds to advance the current time by
        """
        ...

    def GetUtcNow(self) -> datetime.datetime:
        """
        Gets the current time in UTC
        
        :returns: The current time in UTC.
        """
        ...

    def SetCurrentTime(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Sets the current time interpeting the specified time as a local time
        using the time zone used at instatiation.
        
        :param time: The local time to set the current time time, will be converted into UTC
        """
        ...

    def SetCurrentTimeUtc(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Sets the current time interpreting the specified time as a UTC time
        
        :param time: The current time in UTC
        """
        ...


class ISynchronizer(metaclass=abc.ABCMeta):
    """Interface which provides the data to stream to the algorithm"""

    def StreamData(self, cancellationToken: System.Threading.CancellationToken) -> System.Collections.Generic.IEnumerable[QuantConnect.Lean.Engine.DataFeeds.TimeSlice]:
        """Returns an enumerable which provides the data to stream to the algorithm"""
        ...


class Synchronizer(System.Object, QuantConnect.Lean.Engine.DataFeeds.ISynchronizer, QuantConnect.Lean.Engine.DataFeeds.IDataFeedTimeProvider, System.IDisposable):
    """Implementation of the ISynchronizer interface which provides the mechanism to stream data to the algorithm"""

    @property
    def Algorithm(self) -> QuantConnect.Interfaces.IAlgorithm:
        """
        The algorithm instance
        
        This field is protected.
        """
        ...

    @Algorithm.setter
    def Algorithm(self, value: QuantConnect.Interfaces.IAlgorithm):
        """
        The algorithm instance
        
        This field is protected.
        """
        ...

    @property
    def SubscriptionManager(self) -> QuantConnect.Lean.Engine.DataFeeds.IDataFeedSubscriptionManager:
        """
        The subscription manager
        
        This field is protected.
        """
        ...

    @SubscriptionManager.setter
    def SubscriptionManager(self, value: QuantConnect.Lean.Engine.DataFeeds.IDataFeedSubscriptionManager):
        """
        The subscription manager
        
        This field is protected.
        """
        ...

    @property
    def SubscriptionSynchronizer(self) -> QuantConnect.Lean.Engine.DataFeeds.SubscriptionSynchronizer:
        """
        The subscription synchronizer
        
        This field is protected.
        """
        ...

    @SubscriptionSynchronizer.setter
    def SubscriptionSynchronizer(self, value: QuantConnect.Lean.Engine.DataFeeds.SubscriptionSynchronizer):
        """
        The subscription synchronizer
        
        This field is protected.
        """
        ...

    @property
    def TimeSliceFactory(self) -> QuantConnect.Lean.Engine.DataFeeds.TimeSliceFactory:
        """
        The time slice factory
        
        This field is protected.
        """
        ...

    @TimeSliceFactory.setter
    def TimeSliceFactory(self, value: QuantConnect.Lean.Engine.DataFeeds.TimeSliceFactory):
        """
        The time slice factory
        
        This field is protected.
        """
        ...

    @property
    def TimeProvider(self) -> QuantConnect.ITimeProvider:
        """Continuous UTC time provider, only valid for live trading see LiveSynchronizer"""
        ...

    @property
    def FrontierTimeProvider(self) -> QuantConnect.ITimeProvider:
        """Time provider which returns current UTC frontier time"""
        ...

    def Dispose(self) -> None:
        """Free resources"""
        ...

    def GetTimeProvider(self) -> QuantConnect.ITimeProvider:
        """
        Gets the ITimeProvider to use. By default this will load the
        RealTimeProvider for live mode, else SubscriptionFrontierTimeProvider
        
        This method is protected.
        
        :returns: The ITimeProvider to use.
        """
        ...

    def Initialize(self, algorithm: QuantConnect.Interfaces.IAlgorithm, dataFeedSubscriptionManager: QuantConnect.Lean.Engine.DataFeeds.IDataFeedSubscriptionManager) -> None:
        """Initializes the instance of the Synchronizer class"""
        ...

    def PostInitialize(self) -> None:
        """
        Performs additional initialization steps after algorithm initialization
        
        This method is protected.
        """
        ...

    def StreamData(self, cancellationToken: System.Threading.CancellationToken) -> System.Collections.Generic.IEnumerable[QuantConnect.Lean.Engine.DataFeeds.TimeSlice]:
        """Returns an enumerable which provides the data to stream to the algorithm"""
        ...


class SubscriptionUtils(System.Object):
    """Utilities related to data Subscription"""

    @staticmethod
    def Create(request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]) -> QuantConnect.Lean.Engine.DataFeeds.Subscription:
        """
        Creates a new Subscription which will directly consume the provided enumerator
        
        :param request: The subscription data request
        :param enumerator: The data enumerator stack
        :returns: A new subscription instance ready to consume.
        """
        ...

    @staticmethod
    def CreateAndScheduleWorker(request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], factorFileProvider: QuantConnect.Interfaces.IFactorFileProvider, enablePriceScale: bool) -> QuantConnect.Lean.Engine.DataFeeds.Subscription:
        """
        Setups a new Subscription which will consume a blocking EnqueueableEnumerator{T}
        that will be feed by a worker task
        
        :param request: The subscription data request
        :param enumerator: The data enumerator stack
        :param factorFileProvider: The factor file provider
        :param enablePriceScale: Enables price factoring
        :returns: A new subscription instance ready to consume.
        """
        ...


class DataPermissionManager(System.Object, QuantConnect.Interfaces.IDataPermissionManager):
    """Entity in charge of handling data permissions"""

    @property
    def DataChannelProvider(self) -> QuantConnect.Interfaces.IDataChannelProvider:
        """The data channel provider instance"""
        ...

    @DataChannelProvider.setter
    def DataChannelProvider(self, value: QuantConnect.Interfaces.IDataChannelProvider):
        """The data channel provider instance"""
        ...

    def AssertConfiguration(self, subscriptionDataConfig: QuantConnect.Data.SubscriptionDataConfig, startTimeLocal: typing.Union[datetime.datetime, datetime.date], endTimeLocal: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Will assert the requested configuration is valid for the current job
        
        :param subscriptionDataConfig: The data subscription configuration to assert
        :param startTimeLocal: The start time of this request
        :param endTimeLocal: The end time of this request
        """
        ...

    def Initialize(self, job: QuantConnect.Packets.AlgorithmNodePacket) -> None:
        """
        Initialize the data permission manager
        
        :param job: The job packet
        """
        ...


class PendingRemovalsManager(System.Object):
    """Helper class used to managed pending security removals UniverseSelection"""

    class RemovedMember(System.Object):
        """Helper class used to report removed universe members"""

        @property
        def Universe(self) -> QuantConnect.Data.UniverseSelection.Universe:
            """Universe the security was removed from"""
            ...

        @property
        def Security(self) -> QuantConnect.Securities.Security:
            """Security that is removed"""
            ...

        def __init__(self, universe: QuantConnect.Data.UniverseSelection.Universe, security: QuantConnect.Securities.Security) -> None:
            """
            Initialize a new instance of RemovedMember
            
            :param universe: Universe the security was removed from
            :param security: Security that is removed
            """
            ...

    @property
    def PendingRemovals(self) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.Data.UniverseSelection.Universe, System.Collections.Generic.List[QuantConnect.Securities.Security]]:
        """Current pending removals"""
        ...

    def __init__(self, orderProvider: QuantConnect.Securities.IOrderProvider) -> None:
        """
        Create a new instance
        
        :param orderProvider: The order provider used to determine if it is safe to remove a security
        """
        ...

    def CheckPendingRemovals(self, selectedSymbols: System.Collections.Generic.HashSet[QuantConnect.Symbol], currentUniverse: QuantConnect.Data.UniverseSelection.Universe) -> System.Collections.Generic.List[QuantConnect.Lean.Engine.DataFeeds.PendingRemovalsManager.RemovedMember]:
        """
        Will check pending security removals
        
        :param selectedSymbols: Currently selected symbols
        :param currentUniverse: Current universe
        :returns: The members to be removed.
        """
        ...

    def TryRemoveMember(self, member: QuantConnect.Securities.Security, universe: QuantConnect.Data.UniverseSelection.Universe) -> System.Collections.Generic.List[QuantConnect.Lean.Engine.DataFeeds.PendingRemovalsManager.RemovedMember]:
        """
        Will determine if the Security can be removed.
        If it can be removed will add it to PendingRemovals
        
        :param member: The security to remove
        :param universe: The universe which the security is a member of
        :returns: The member to remove.
        """
        ...


class LiveOptionChainProvider(QuantConnect.Lean.Engine.DataFeeds.BacktestingOptionChainProvider):
    """
    An implementation of IOptionChainProvider that fetches the list of contracts
    from the Options Clearing Corporation (OCC) website
    """

    def __init__(self, dataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider) -> None:
        """
        Creates a new instance
        
        :param dataCacheProvider: The data cache provider instance to use
        :param mapFileProvider: The map file provider instance to use
        """
        ...

    def GetOptionContractList(self, underlyingSymbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Gets the option chain associated with the underlying Symbol
        
        :param underlyingSymbol: Underlying symbol to get the option chain for
        :param date: Unused
        :returns: Option chain.
        """
        ...


class LiveTradingDataFeed(QuantConnect.Lean.Engine.DataFeeds.FileSystemDataFeed):
    """
    Provides an implementation of IDataFeed that is designed to deal with
    live, remote data sources
    """

    @property
    def IsActive(self) -> bool:
        """Public flag indicator that the thread is still busy."""
        ...

    @IsActive.setter
    def IsActive(self, value: bool):
        """Public flag indicator that the thread is still busy."""
        ...

    def CreateSubscription(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest) -> QuantConnect.Lean.Engine.DataFeeds.Subscription:
        """
        Creates a new subscription to provide data for the specified security.
        
        :param request: Defines the subscription to be added, including start/end times the universe and security
        :returns: The created Subscription if successful, null otherwise.
        """
        ...

    def Exit(self) -> None:
        """External controller calls to signal a terminate of the thread."""
        ...

    def GetBaseDataExchange(self) -> QuantConnect.Lean.Engine.DataFeeds.BaseDataExchange:
        """
        Gets the BaseDataExchange to use
        
        This method is protected.
        """
        ...

    def GetDataQueueHandler(self) -> QuantConnect.Interfaces.IDataQueueHandler:
        """
        Gets the IDataQueueHandler to use by default DataQueueHandlerManager
        
        This method is protected.
        
        :returns: The loaded IDataQueueHandler.
        """
        ...

    def Initialize(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.AlgorithmNodePacket, resultHandler: QuantConnect.Lean.Engine.Results.IResultHandler, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider, factorFileProvider: QuantConnect.Interfaces.IFactorFileProvider, dataProvider: QuantConnect.Interfaces.IDataProvider, subscriptionManager: QuantConnect.Lean.Engine.DataFeeds.IDataFeedSubscriptionManager, dataFeedTimeProvider: QuantConnect.Lean.Engine.DataFeeds.IDataFeedTimeProvider, dataChannelProvider: QuantConnect.Interfaces.IDataChannelProvider) -> None:
        """Initializes the data feed for the specified job and algorithm"""
        ...

    def RemoveSubscription(self, subscription: QuantConnect.Lean.Engine.DataFeeds.Subscription) -> None:
        """
        Removes the subscription from the data feed, if it exists
        
        :param subscription: The subscription to remove
        """
        ...


class RealTimeScheduleEventService(System.Object, System.IDisposable):
    """
    Allows to setup a real time scheduled event, internally using a Thread,
    that is guaranteed to trigger at or after the requested time, never before.
    """

    @property
    def NewEvent(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Event fired when the scheduled time is past"""
        ...

    @NewEvent.setter
    def NewEvent(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]):
        """Event fired when the scheduled time is past"""
        ...

    def __init__(self, timeProvider: QuantConnect.ITimeProvider) -> None:
        """
        Creates a new instance
        
        :param timeProvider: The time provider to use
        """
        ...

    def Dispose(self) -> None:
        """Disposes of the underlying Timer instance"""
        ...

    def ScheduleEvent(self, dueTime: datetime.timedelta, utcNow: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Schedules a new event
        
        :param dueTime: The desired due time
        :param utcNow: Current utc time
        """
        ...


class DataChannelProvider(System.Object, QuantConnect.Interfaces.IDataChannelProvider):
    """Specifies data channel settings"""

    def Initialize(self, packet: QuantConnect.Packets.AlgorithmNodePacket) -> None:
        """
        Initializes the instance with an algorithm node packet
        
        :param packet: Algorithm node packet
        """
        ...

    @staticmethod
    def IsStreamingType(configuration: QuantConnect.Data.SubscriptionDataConfig) -> bool:
        """
        Returns true if the data type for the given subscription configuration supports streaming
        
        This method is protected.
        """
        ...

    def ShouldStreamSubscription(self, config: QuantConnect.Data.SubscriptionDataConfig) -> bool:
        """True if this subscription request should be streamed"""
        ...


class CompositeDataProvider(System.Object, QuantConnect.Interfaces.IDataProvider):
    """This data provider will wrap and use multiple data providers internally in the provided order"""

    @property
    def NewDataRequest(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Interfaces.DataProviderNewDataRequestEventArgs], None], None]:
        """Event raised each time data fetch is finished (successfully or not)"""
        ...

    @NewDataRequest.setter
    def NewDataRequest(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Interfaces.DataProviderNewDataRequestEventArgs], None], None]):
        """Event raised each time data fetch is finished (successfully or not)"""
        ...

    def __init__(self) -> None:
        """Creates a new instance and initialize data providers used"""
        ...

    def Fetch(self, key: str) -> System.IO.Stream:
        """
        Retrieves data to be used in an algorithm
        
        :param key: A string representing where the data is stored
        :returns: A Stream of the data requested.
        """
        ...


class CachingFutureChainProvider(System.Object, QuantConnect.Interfaces.IFutureChainProvider):
    """An implementation of IFutureChainProvider that will cache by date future contracts returned by another future chain provider."""

    def __init__(self, futureChainProvider: QuantConnect.Interfaces.IFutureChainProvider) -> None:
        """Initializes a new instance of the CachingFutureChainProvider class"""
        ...

    def GetFutureContractList(self, symbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Gets the list of future contracts for a given underlying symbol
        
        :param symbol: The underlying symbol
        :param date: The date for which to request the future chain (only used in backtesting)
        :returns: The list of future contracts.
        """
        ...


class LiveSynchronizer(QuantConnect.Lean.Engine.DataFeeds.Synchronizer):
    """Implementation of the ISynchronizer interface which provides the mechanism to stream live data to the algorithm"""

    @property
    def TimeProvider(self) -> QuantConnect.ITimeProvider:
        """Continuous UTC time provider"""
        ...

    def Dispose(self) -> None:
        """Free resources"""
        ...

    def GetPulseDueTime(self, now: typing.Union[datetime.datetime, datetime.date]) -> int:
        """
        Will return the amount of milliseconds that are missing for the next time pulse
        
        This method is protected.
        """
        ...

    def GetTimeProvider(self) -> QuantConnect.ITimeProvider:
        """
        Gets the ITimeProvider to use. By default this will load the
        RealTimeProvider for live mode, else SubscriptionFrontierTimeProvider
        
        This method is protected.
        
        :returns: The ITimeProvider to use.
        """
        ...

    def Initialize(self, algorithm: QuantConnect.Interfaces.IAlgorithm, dataFeedSubscriptionManager: QuantConnect.Lean.Engine.DataFeeds.IDataFeedSubscriptionManager) -> None:
        """Initializes the instance of the Synchronizer class"""
        ...

    def OnSubscriptionNewDataAvailable(self, sender: typing.Any, args: System.EventArgs) -> None:
        """
        Trigger new data event
        
        This method is protected.
        
        :param sender: Sender of the event
        :param args: Event information
        """
        ...

    def PostInitialize(self) -> None:
        """
        Performs additional initialization steps after algorithm initialization
        
        This method is protected.
        """
        ...

    def StreamData(self, cancellationToken: System.Threading.CancellationToken) -> System.Collections.Generic.IEnumerable[QuantConnect.Lean.Engine.DataFeeds.TimeSlice]:
        """Returns an enumerable which provides the data to stream to the algorithm"""
        ...


class _EventContainer(typing.Generic[QuantConnect_Lean_Engine_DataFeeds__EventContainer_Callable, QuantConnect_Lean_Engine_DataFeeds__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Lean_Engine_DataFeeds__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Lean_Engine_DataFeeds__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Lean_Engine_DataFeeds__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


