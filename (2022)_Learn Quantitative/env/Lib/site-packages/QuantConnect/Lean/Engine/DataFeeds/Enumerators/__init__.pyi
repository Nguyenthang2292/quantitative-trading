from typing import overload
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Auxiliary
import QuantConnect.Data.Consolidators
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import QuantConnect.Lean.Engine.DataFeeds.Enumerators
import QuantConnect.Lean.Engine.Results
import QuantConnect.Python
import QuantConnect.Securities
import QuantConnect.Util
import System
import System.Collections
import System.Collections.Generic

QuantConnect_Lean_Engine_DataFeeds_Enumerators_RefreshEnumerator_T = typing.TypeVar("QuantConnect_Lean_Engine_DataFeeds_Enumerators_RefreshEnumerator_T")
QuantConnect_Lean_Engine_DataFeeds_Enumerators_RateLimitEnumerator_T = typing.TypeVar("QuantConnect_Lean_Engine_DataFeeds_Enumerators_RateLimitEnumerator_T")
QuantConnect_Lean_Engine_DataFeeds_Enumerators_SynchronizingEnumerator_T = typing.TypeVar("QuantConnect_Lean_Engine_DataFeeds_Enumerators_SynchronizingEnumerator_T")
QuantConnect_Lean_Engine_DataFeeds_Enumerators_FilterEnumerator_T = typing.TypeVar("QuantConnect_Lean_Engine_DataFeeds_Enumerators_FilterEnumerator_T")
QuantConnect_Lean_Engine_DataFeeds_Enumerators_ScannableEnumerator_T = typing.TypeVar("QuantConnect_Lean_Engine_DataFeeds_Enumerators_ScannableEnumerator_T")
QuantConnect_Lean_Engine_DataFeeds_Enumerators_EnqueueableEnumerator_T = typing.TypeVar("QuantConnect_Lean_Engine_DataFeeds_Enumerators_EnqueueableEnumerator_T")
QuantConnect_Lean_Engine_DataFeeds_Enumerators__EventContainer_Callable = typing.TypeVar("QuantConnect_Lean_Engine_DataFeeds_Enumerators__EventContainer_Callable")
QuantConnect_Lean_Engine_DataFeeds_Enumerators__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Lean_Engine_DataFeeds_Enumerators__EventContainer_ReturnType")


class DataQueueOptionChainUniverseDataCollectionEnumerator(System.Object):
    """Enumerates live options symbol universe data into OptionChainUniverseDataCollection instances"""

    @property
    def Underlying(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """Gets the enumerator for the underlying asset"""
        ...

    @property
    def Current(self) -> QuantConnect.Data.UniverseSelection.BaseDataCollection:
        """Returns current option chain enumerator position"""
        ...

    @Current.setter
    def Current(self, value: QuantConnect.Data.UniverseSelection.BaseDataCollection):
        """Returns current option chain enumerator position"""
        ...

    def __init__(self, subscriptionRequest: QuantConnect.Data.UniverseSelection.SubscriptionRequest, underlying: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], universeProvider: QuantConnect.Interfaces.IDataQueueUniverseProvider, timeProvider: QuantConnect.ITimeProvider) -> None:
        """
        Initializes a new instance of the DataQueueOptionChainUniverseDataCollectionEnumerator class.
        
        :param subscriptionRequest: The subscription request to be used
        :param underlying: Underlying enumerator
        :param universeProvider: Symbol universe provider of the data queue
        :param timeProvider: The time provider to be used
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def MoveNext(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        ...

    def Reset(self) -> None:
        """Sets the enumerator to its initial position, which is before the first element in the collection."""
        ...


class LiveAuxiliaryDataSynchronizingEnumerator(System.Object):
    """
    Represents an enumerator capable of synchronizing live equity data enumerators in time.
    This assumes that all enumerators have data time stamped in the same time zone.
    """

    @property
    def Current(self) -> QuantConnect.Data.BaseData:
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    @Current.setter
    def Current(self, value: QuantConnect.Data.BaseData):
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    def __init__(self, timeProvider: QuantConnect.ITimeProvider, exchangeTimeZone: typing.Any, tradeBarAggregator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], auxDataEnumerators: System.Collections.Generic.List[System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]]) -> None:
        """
        Initializes a new instance of the LiveAuxiliaryDataSynchronizingEnumerator class
        
        :param timeProvider: The source of time used to gauge when this enumerator should emit extra bars when null data is returned from the source enumerator
        :param exchangeTimeZone: The time zone the raw data is time stamped in
        :param tradeBarAggregator: The trade bar aggregator enumerator
        :param auxDataEnumerators: The auxiliary data enumerators
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def MoveNext(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        ...

    def Reset(self) -> None:
        """Sets the enumerator to its initial position, which is before the first element in the collection."""
        ...


class BaseDataCollectionAggregatorEnumerator(System.Object):
    """
    Provides an implementation of IEnumerator{BaseDataCollection}
    that aggregates an underlying IEnumerator{BaseData} into a single
    data packet
    """

    @property
    def Current(self) -> QuantConnect.Data.UniverseSelection.BaseDataCollection:
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    @Current.setter
    def Current(self, value: QuantConnect.Data.UniverseSelection.BaseDataCollection):
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    def __init__(self, enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], symbol: typing.Union[QuantConnect.Symbol, str], liveMode: bool = False) -> None:
        """
        Initializes a new instance of the BaseDataCollectionAggregatorEnumerator class
        This will aggregate instances emitted from the underlying enumerator and tag them with the
        specified symbol
        
        :param enumerator: The underlying enumerator to aggregate
        :param symbol: The symbol to place on the aggregated collection
        :param liveMode: True if running in live mode
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def MoveNext(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        ...

    def Reset(self) -> None:
        """Sets the enumerator to its initial position, which is before the first element in the collection."""
        ...


class RefreshEnumerator(typing.Generic[QuantConnect_Lean_Engine_DataFeeds_Enumerators_RefreshEnumerator_T], System.Object):
    """
    Provides an implementation of IEnumerator{T} that will
    always return true via MoveNext.
    """

    @property
    def Current(self) -> QuantConnect_Lean_Engine_DataFeeds_Enumerators_RefreshEnumerator_T:
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    def __init__(self, enumeratorFactory: typing.Callable[[], System.Collections.Generic.IEnumerator[QuantConnect_Lean_Engine_DataFeeds_Enumerators_RefreshEnumerator_T]]) -> None:
        """
        Initializes a new instance of the RefreshEnumerator{T} class
        
        :param enumeratorFactory: Enumerator factory used to regenerate the underlying enumerator when it ends
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def MoveNext(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        ...

    def Reset(self) -> None:
        """Sets the enumerator to its initial position, which is before the first element in the collection."""
        ...


class SubscriptionDataEnumerator(System.Object):
    """An IEnumerator{SubscriptionData} which wraps an existing IEnumerator{BaseData}."""

    @property
    def Current(self) -> System.Object:
        ...

    def __init__(self, configuration: QuantConnect.Data.SubscriptionDataConfig, exchangeHours: QuantConnect.Securities.SecurityExchangeHours, offsetProvider: QuantConnect.TimeZoneOffsetProvider, enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], isUniverse: bool) -> None:
        """
        Creates a new instance
        
        :param configuration: The subscription's configuration
        :param exchangeHours: The security's exchange hours
        :param offsetProvider: The subscription's time zone offset provider
        :param enumerator: The underlying data enumerator
        :param isUniverse: The subscription is a universe subscription
        :returns: A subscription data enumerator.
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def MoveNext(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: True if the enumerator was successfully advanced to the next element; False if the enumerator has passed the end of the collection.
        """
        ...

    def Reset(self) -> None:
        """Sets the enumerator to its initial position, which is before the first element in the collection."""
        ...


class FastForwardEnumerator(System.Object):
    """Provides the ability to fast forward an enumerator based on the age of the data"""

    @property
    def Current(self) -> QuantConnect.Data.BaseData:
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    def __init__(self, enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], timeProvider: QuantConnect.ITimeProvider, timeZone: typing.Any, maximumDataAge: datetime.timedelta) -> None:
        """
        Initializes a new instance of the FastForwardEnumerator class
        
        :param enumerator: The source enumerator
        :param timeProvider: A time provider used to determine age of data
        :param timeZone: The data's time zone
        :param maximumDataAge: The maximum age of data allowed
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def MoveNext(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        ...

    def Reset(self) -> None:
        """Sets the enumerator to its initial position, which is before the first element in the collection."""
        ...


class ITradableDateEventProvider(metaclass=abc.ABCMeta):
    """Interface for event providers for new tradable dates"""

    def GetEvents(self, eventArgs: QuantConnect.NewTradableDateEventArgs) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]:
        """
        Called each time there is a new tradable day
        
        :param eventArgs: The new tradable day event arguments
        :returns: New corporate event if any.
        """
        ...

    def Initialize(self, config: QuantConnect.Data.SubscriptionDataConfig, factorFileProvider: QuantConnect.Interfaces.IFactorFileProvider, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider, startTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes the event provider instance
        
        :param config: The SubscriptionDataConfig
        :param factorFileProvider: The factor file provider to use
        :param mapFileProvider: The MapFile provider to use
        :param startTime: Start date for the data request
        """
        ...


class MappingEventProvider(System.Object, QuantConnect.Lean.Engine.DataFeeds.Enumerators.ITradableDateEventProvider):
    """Event provider who will emit SymbolChangedEvent events"""

    @property
    def Config(self) -> QuantConnect.Data.SubscriptionDataConfig:
        """
        The associated configuration
        
        This property is protected.
        """
        ...

    @Config.setter
    def Config(self, value: QuantConnect.Data.SubscriptionDataConfig):
        """
        The associated configuration
        
        This property is protected.
        """
        ...

    @property
    def MapFile(self) -> QuantConnect.Data.Auxiliary.MapFile:
        """
        The current instance being used
        
        This property is protected.
        """
        ...

    @MapFile.setter
    def MapFile(self, value: QuantConnect.Data.Auxiliary.MapFile):
        """
        The current instance being used
        
        This property is protected.
        """
        ...

    def GetEvents(self, eventArgs: QuantConnect.NewTradableDateEventArgs) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]:
        """
        Check for new mappings
        
        :param eventArgs: The new tradable day event arguments
        :returns: New mapping event if any.
        """
        ...

    def Initialize(self, config: QuantConnect.Data.SubscriptionDataConfig, factorFileProvider: QuantConnect.Interfaces.IFactorFileProvider, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider, startTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes this instance
        
        :param config: The SubscriptionDataConfig
        :param factorFileProvider: The factor file provider to use
        :param mapFileProvider: The Data.Auxiliary.MapFile provider to use
        :param startTime: Start date for the data request
        """
        ...

    def InitializeMapFile(self) -> None:
        """
        Initializes the map file to use
        
        This method is protected.
        """
        ...


class RateLimitEnumerator(typing.Generic[QuantConnect_Lean_Engine_DataFeeds_Enumerators_RateLimitEnumerator_T], System.Object):
    """
    Provides augmentation of how often an enumerator can be called. Time is measured using
    an ITimeProvider instance and calls to the underlying enumerator are limited
    to a minimum time between each call.
    """

    @property
    def Current(self) -> QuantConnect_Lean_Engine_DataFeeds_Enumerators_RateLimitEnumerator_T:
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    def __init__(self, enumerator: System.Collections.Generic.IEnumerator[QuantConnect_Lean_Engine_DataFeeds_Enumerators_RateLimitEnumerator_T], timeProvider: QuantConnect.ITimeProvider, minimumTimeBetweenCalls: datetime.timedelta) -> None:
        """
        Initializes a new instance of the RateLimitEnumerator{T} class
        
        :param enumerator: The underlying enumerator to place rate limits on
        :param timeProvider: Time provider used for determing the time between calls
        :param minimumTimeBetweenCalls: The minimum time allowed between calls to the underlying enumerator
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def MoveNext(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        ...

    def Reset(self) -> None:
        """Sets the enumerator to its initial position, which is before the first element in the collection."""
        ...


class ITradableDatesNotifier(metaclass=abc.ABCMeta):
    """
    Interface which will provide an event handler
    who will be fired with each new tradable day
    """

    @property
    @abc.abstractmethod
    def NewTradableDate(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.NewTradableDateEventArgs], None], None]:
        """Event fired when there is a new tradable date"""
        ...

    @NewTradableDate.setter
    @abc.abstractmethod
    def NewTradableDate(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.NewTradableDateEventArgs], None], None]):
        """Event fired when there is a new tradable date"""
        ...


class SplitEventProvider(System.Object, QuantConnect.Lean.Engine.DataFeeds.Enumerators.ITradableDateEventProvider):
    """Event provider who will emit Split events"""

    def GetEvents(self, eventArgs: QuantConnect.NewTradableDateEventArgs) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]:
        """
        Check for new splits
        
        :param eventArgs: The new tradable day event arguments
        :returns: New split event if any.
        """
        ...

    def Initialize(self, config: QuantConnect.Data.SubscriptionDataConfig, factorFileProvider: QuantConnect.Interfaces.IFactorFileProvider, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider, startTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes this instance
        
        :param config: The SubscriptionDataConfig
        :param factorFileProvider: The factor file provider to use
        :param mapFileProvider: The Data.Auxiliary.MapFile provider to use
        :param startTime: Start date for the data request
        """
        ...


class NewDataAvailableEventArgs(System.EventArgs):
    """Event args for when a new data point is ready to be emitted"""

    @property
    def DataPoint(self) -> QuantConnect.Data.IBaseData:
        """The new data point"""
        ...

    @DataPoint.setter
    def DataPoint(self, value: QuantConnect.Data.IBaseData):
        """The new data point"""
        ...


class DelistingEventProvider(System.Object, QuantConnect.Lean.Engine.DataFeeds.Enumerators.ITradableDateEventProvider):
    """Event provider who will emit Delisting events"""

    @property
    def DelistingDate(self) -> QuantConnect.Util.ReferenceWrapper[datetime.datetime]:
        """
        The delisting date
        
        This property is protected.
        """
        ...

    @DelistingDate.setter
    def DelistingDate(self, value: QuantConnect.Util.ReferenceWrapper[datetime.datetime]):
        """
        The delisting date
        
        This property is protected.
        """
        ...

    def GetEvents(self, eventArgs: QuantConnect.NewTradableDateEventArgs) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]:
        """
        Check for delistings
        
        :param eventArgs: The new tradable day event arguments
        :returns: New delisting event if any.
        """
        ...

    def Initialize(self, config: QuantConnect.Data.SubscriptionDataConfig, factorFileProvider: QuantConnect.Interfaces.IFactorFileProvider, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider, startTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes this instance
        
        :param config: The SubscriptionDataConfig
        :param factorFileProvider: The factor file provider to use
        :param mapFileProvider: The Data.Auxiliary.MapFile provider to use
        :param startTime: Start date for the data request
        """
        ...


class LiveDataBasedDelistingEventProvider(QuantConnect.Lean.Engine.DataFeeds.Enumerators.DelistingEventProvider, System.IDisposable):
    """Delisting event provider implementation which will source the delisting date based on the incoming data point"""

    def __init__(self, dataConfig: QuantConnect.Data.SubscriptionDataConfig, dataQueueHandler: QuantConnect.Interfaces.IDataQueueHandler) -> None:
        """Creates a new instance"""
        ...

    def Dispose(self) -> None:
        """Clean up"""
        ...

    def Initialize(self, config: QuantConnect.Data.SubscriptionDataConfig, factorFileProvider: QuantConnect.Interfaces.IFactorFileProvider, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider, startTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes this instance
        
        :param config: The SubscriptionDataConfig
        :param factorFileProvider: The factor file provider to use
        :param mapFileProvider: The Data.Auxiliary.MapFile provider to use
        :param startTime: Start date for the data request
        """
        ...


class SynchronizingEnumerator(typing.Generic[QuantConnect_Lean_Engine_DataFeeds_Enumerators_SynchronizingEnumerator_T], System.Object, metaclass=abc.ABCMeta):
    """
    Represents an enumerator capable of synchronizing other enumerators of type T in time.
    This assumes that all enumerators have data time stamped in the same time zone
    """

    @property
    def Current(self) -> QuantConnect_Lean_Engine_DataFeeds_Enumerators_SynchronizingEnumerator_T:
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    @Current.setter
    def Current(self, value: QuantConnect_Lean_Engine_DataFeeds_Enumerators_SynchronizingEnumerator_T):
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    @overload
    def __init__(self, *enumerators: System.Collections.Generic.IEnumerator[QuantConnect_Lean_Engine_DataFeeds_Enumerators_SynchronizingEnumerator_T]) -> None:
        """
        Initializes a new instance of the SynchronizingEnumerator{T} class
        
        This method is protected.
        
        :param enumerators: The enumerators to be synchronized. NOTE: Assumes the same time zone for all data
        """
        ...

    @overload
    def __init__(self, enumerators: System.Collections.Generic.IEnumerable[System.Collections.Generic.IEnumerator[QuantConnect_Lean_Engine_DataFeeds_Enumerators_SynchronizingEnumerator_T]]) -> None:
        """
        Initializes a new instance of the SynchronizingEnumerator{T} class
        
        This method is protected.
        
        :param enumerators: The enumerators to be synchronized. NOTE: Assumes the same time zone for all data
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def GetInstanceTime(self, instance: QuantConnect_Lean_Engine_DataFeeds_Enumerators_SynchronizingEnumerator_T) -> datetime.datetime:
        """
        Gets the Timestamp for the data
        
        This method is protected.
        """
        ...

    def MoveNext(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        ...

    def Reset(self) -> None:
        """Sets the enumerator to its initial position, which is before the first element in the collection."""
        ...


class PriceScaleFactorEnumerator(System.Object):
    """
    This enumerator will update the SubscriptionDataConfig.PriceScaleFactor when required
    and adjust the raw BaseData prices based on the provided SubscriptionDataConfig.
    Assumes the prices of the provided IEnumerator are in raw mode.
    """

    @property
    def Current(self) -> System.Object:
        """Explicit interface implementation for Current"""
        ...

    def __init__(self, rawDataEnumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], config: QuantConnect.Data.SubscriptionDataConfig, factorFileProvider: QuantConnect.Interfaces.IFactorFileProvider, liveMode: bool = False) -> None:
        """
        Creates a new instance of the PriceScaleFactorEnumerator.
        
        :param rawDataEnumerator: The underlying raw data enumerator
        :param config: The SubscriptionDataConfig to enumerate for. Will determine the DataNormalizationMode to use.
        :param factorFileProvider: The IFactorFileProvider instance to use
        :param liveMode: True, is this is a live mode data stream
        """
        ...

    def Dispose(self) -> None:
        """Dispose of the underlying enumerator."""
        ...

    def MoveNext(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: True if the enumerator was successfully advanced to the next element; False if the enumerator has passed the end of the collection.
        """
        ...

    def Reset(self) -> None:
        """Reset the IEnumeration"""
        ...


class ConcatEnumerator(System.Object):
    """Enumerator that will concatenate enumerators together sequentially enumerating them in the provided order"""

    @property
    def Current(self) -> QuantConnect.Data.BaseData:
        """The current BaseData object"""
        ...

    @Current.setter
    def Current(self, value: QuantConnect.Data.BaseData):
        """The current BaseData object"""
        ...

    @property
    def CanEmitNull(self) -> bool:
        """True if emitting a null data point is expected"""
        ...

    @CanEmitNull.setter
    def CanEmitNull(self, value: bool):
        """True if emitting a null data point is expected"""
        ...

    def __init__(self, skipDuplicateEndTimes: bool, *enumerators: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]) -> None:
        """
        Creates a new instance
        
        :param skipDuplicateEndTimes: True will skip data points from enumerators if before or at the last end time
        :param enumerators: The sequence of enumerators to concatenate. Note that the order here matters, it will consume enumerators and dispose of them, even if they return true and their current is null, except for the last which will be kept!
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def MoveNext(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: True if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        ...

    def Reset(self) -> None:
        """Sets the enumerator to its initial position, which is before the first element in the collection."""
        ...


class SubscriptionFilterEnumerator(System.Object):
    """Implements a wrapper around a base data enumerator to provide a final filtering step"""

    @property
    def DataFilterError(self) -> _EventContainer[typing.Callable[[System.Object, System.Exception], None], None]:
        """Fired when there's an error executing a user's data filter"""
        ...

    @DataFilterError.setter
    def DataFilterError(self, value: _EventContainer[typing.Callable[[System.Object, System.Exception], None], None]):
        """Fired when there's an error executing a user's data filter"""
        ...

    @property
    def Current(self) -> QuantConnect.Data.BaseData:
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    @Current.setter
    def Current(self, value: QuantConnect.Data.BaseData):
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    def __init__(self, enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], security: QuantConnect.Securities.Security, endTime: typing.Union[datetime.datetime, datetime.date], extendedMarketHours: bool, liveMode: bool, securityExchangeHours: QuantConnect.Securities.SecurityExchangeHours) -> None:
        """
        Initializes a new instance of the SubscriptionFilterEnumerator class
        
        :param enumerator: The source enumerator to be wrapped
        :param security: The security containing an exchange and data filter
        :param endTime: The end time of the subscription
        :param extendedMarketHours: True if extended market hours are enabled
        :param liveMode: True if live mode
        :param securityExchangeHours: The security exchange hours instance to use
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def MoveNext(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        ...

    def Reset(self) -> None:
        """Sets the enumerator to its initial position, which is before the first element in the collection."""
        ...

    @staticmethod
    def WrapForDataFeed(resultHandler: QuantConnect.Lean.Engine.Results.IResultHandler, enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], security: QuantConnect.Securities.Security, endTime: typing.Union[datetime.datetime, datetime.date], extendedMarketHours: bool, liveMode: bool, securityExchangeHours: QuantConnect.Securities.SecurityExchangeHours) -> QuantConnect.Lean.Engine.DataFeeds.Enumerators.SubscriptionFilterEnumerator:
        """
        Convenience method to wrap the enumerator and attach the data filter event to log and alery users of errors
        
        :param resultHandler: Result handler reference used to send errors
        :param enumerator: The source enumerator to be wrapped
        :param security: The security who's data is being enumerated
        :param endTime: The end time of the subscription
        :param extendedMarketHours: True if extended market hours are enabled
        :param liveMode: True if live mode
        :param securityExchangeHours: The security exchange hours instance to use
        :returns: A new instance of the SubscriptionFilterEnumerator class that has had it's DataFilterError event subscribed to to send errors to the result handler.
        """
        ...


class SynchronizingSliceEnumerator(QuantConnect.Lean.Engine.DataFeeds.Enumerators.SynchronizingEnumerator[QuantConnect.Data.Slice]):
    """
    Represents an enumerator capable of synchronizing other slice enumerators in time.
    This assumes that all enumerators have data time stamped in the same time zone
    """

    @overload
    def __init__(self, *enumerators: System.Collections.Generic.IEnumerator[QuantConnect.Data.Slice]) -> None:
        """
        Initializes a new instance of the SynchronizingSliceEnumerator class
        
        :param enumerators: The enumerators to be synchronized. NOTE: Assumes the same time zone for all data
        """
        ...

    @overload
    def __init__(self, enumerators: System.Collections.Generic.IEnumerable[System.Collections.IEnumerator]) -> None:
        """
        Initializes a new instance of the SynchronizingSliceEnumerator class
        
        :param enumerators: The enumerators to be synchronized. NOTE: Assumes the same time zone for all data
        """
        ...

    def GetInstanceTime(self, instance: QuantConnect.Data.Slice) -> datetime.datetime:
        """
        Gets the Timestamp for the data
        
        This method is protected.
        """
        ...


class SynchronizingBaseDataEnumerator(QuantConnect.Lean.Engine.DataFeeds.Enumerators.SynchronizingEnumerator[QuantConnect.Data.BaseData]):
    """
    Represents an enumerator capable of synchronizing other base data enumerators in time.
    This assumes that all enumerators have data time stamped in the same time zone
    """

    @overload
    def __init__(self, *enumerators: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]) -> None:
        """
        Initializes a new instance of the SynchronizingBaseDataEnumerator class
        
        :param enumerators: The enumerators to be synchronized. NOTE: Assumes the same time zone for all data
        """
        ...

    @overload
    def __init__(self, enumerators: System.Collections.Generic.IEnumerable[System.Collections.IEnumerator]) -> None:
        """
        Initializes a new instance of the SynchronizingBaseDataEnumerator class
        
        :param enumerators: The enumerators to be synchronized. NOTE: Assumes the same time zone for all data
        """
        ...

    def GetInstanceTime(self, instance: QuantConnect.Data.BaseData) -> datetime.datetime:
        """
        Gets the Timestamp for the data
        
        This method is protected.
        """
        ...


class FilterEnumerator(typing.Generic[QuantConnect_Lean_Engine_DataFeeds_Enumerators_FilterEnumerator_T], System.Object):
    """Enumerator that allow applying a filtering function"""

    @property
    def Current(self) -> QuantConnect_Lean_Engine_DataFeeds_Enumerators_FilterEnumerator_T:
        ...

    def __init__(self, enumerator: System.Collections.Generic.IEnumerator[QuantConnect_Lean_Engine_DataFeeds_Enumerators_FilterEnumerator_T], filter: typing.Callable[[QuantConnect_Lean_Engine_DataFeeds_Enumerators_FilterEnumerator_T], bool]) -> None:
        """
        Creates a new instance
        
        :param enumerator: The underlying enumerator to filter on
        :param filter: The filter to apply
        """
        ...

    def Dispose(self) -> None:
        ...

    def MoveNext(self) -> bool:
        ...

    def Reset(self) -> None:
        ...


class DataQueueFuturesChainUniverseDataCollectionEnumerator(System.Object):
    """Enumerates live futures symbol universe data into BaseDataCollection instances"""

    @property
    def Current(self) -> QuantConnect.Data.UniverseSelection.BaseDataCollection:
        """Returns current futures chain enumerator position"""
        ...

    @Current.setter
    def Current(self, value: QuantConnect.Data.UniverseSelection.BaseDataCollection):
        """Returns current futures chain enumerator position"""
        ...

    def __init__(self, subscriptionRequest: QuantConnect.Data.UniverseSelection.SubscriptionRequest, universeProvider: QuantConnect.Interfaces.IDataQueueUniverseProvider, timeProvider: QuantConnect.ITimeProvider) -> None:
        """
        Initializes a new instance of the DataQueueFuturesChainUniverseDataCollectionEnumerator class.
        
        :param subscriptionRequest: The subscription request to be used
        :param universeProvider: Symbol universe provider of the data queue
        :param timeProvider: The time provider to be used
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def MoveNext(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        ...

    def Reset(self) -> None:
        """Sets the enumerator to its initial position, which is before the first element in the collection."""
        ...


class FillForwardEnumerator(System.Object):
    """
    The FillForwardEnumerator wraps an existing base data enumerator and inserts extra 'base data' instances
    on a specified fill forward resolution
    """

    @property
    def Exchange(self) -> QuantConnect.Securities.SecurityExchange:
        """
        The exchange used to determine when to insert fill forward data
        
        This field is protected.
        """
        ...

    @property
    def Current(self) -> QuantConnect.Data.BaseData:
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    @Current.setter
    def Current(self, value: QuantConnect.Data.BaseData):
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    def __init__(self, enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], exchange: QuantConnect.Securities.SecurityExchange, fillForwardResolution: QuantConnect.Util.IReadOnlyRef[datetime.timedelta], isExtendedMarketHours: bool, subscriptionEndTime: typing.Union[datetime.datetime, datetime.date], dataResolution: datetime.timedelta, dataTimeZone: typing.Any) -> None:
        """
        Initializes a new instance of the FillForwardEnumerator class that accepts
        a reference to the fill forward resolution, useful if the fill forward resolution is dynamic
        and changing as the enumeration progresses
        
        :param enumerator: The source enumerator to be filled forward
        :param exchange: The exchange used to determine when to insert fill forward data
        :param fillForwardResolution: The resolution we'd like to receive data on
        :param isExtendedMarketHours: True to use the exchange's extended market hours, false to use the regular market hours
        :param subscriptionEndTime: The end time of the subscrition, once passing this date the enumerator will stop
        :param dataResolution: The source enumerator's data resolution
        :param dataTimeZone: The time zone of the underlying source data. This is used for rounding calculations and is NOT the time zone on the BaseData instances (unless of course data time zone equals the exchange time zone)
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def MoveNext(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        ...

    def RequiresFillForwardData(self, fillForwardResolution: datetime.timedelta, previous: QuantConnect.Data.BaseData, next: QuantConnect.Data.BaseData, fillForward: typing.Optional[QuantConnect.Data.BaseData]) -> typing.Union[bool, QuantConnect.Data.BaseData]:
        """
        Determines whether or not fill forward is required, and if true, will produce the new fill forward data
        
        This method is protected.
        
        :param previous: The last piece of data emitted by this enumerator
        :param next: The next piece of data on the source enumerator
        :param fillForward: When this function returns true, this will have a non-null value, null when the function returns false
        :returns: True when a new fill forward piece of data was produced and should be emitted by this enumerator.
        """
        ...

    def Reset(self) -> None:
        """Sets the enumerator to its initial position, which is before the first element in the collection."""
        ...


class LiveFillForwardEnumerator(QuantConnect.Lean.Engine.DataFeeds.Enumerators.FillForwardEnumerator):
    """
    An implementation of the FillForwardEnumerator that uses an ITimeProvider
    to determine if a fill forward bar needs to be emitted
    """

    def __init__(self, timeProvider: QuantConnect.ITimeProvider, enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], exchange: QuantConnect.Securities.SecurityExchange, fillForwardResolution: QuantConnect.Util.IReadOnlyRef[datetime.timedelta], isExtendedMarketHours: bool, subscriptionEndTime: typing.Union[datetime.datetime, datetime.date], dataResolution: datetime.timedelta, dataTimeZone: typing.Any) -> None:
        """
        Initializes a new instance of the LiveFillForwardEnumerator class that accepts
        a reference to the fill forward resolution, useful if the fill forward resolution is dynamic
        and changing as the enumeration progresses
        
        :param timeProvider: The source of time used to gauage when this enumerator should emit extra bars when null data is returned from the source enumerator
        :param enumerator: The source enumerator to be filled forward
        :param exchange: The exchange used to determine when to insert fill forward data
        :param fillForwardResolution: The resolution we'd like to receive data on
        :param isExtendedMarketHours: True to use the exchange's extended market hours, false to use the regular market hours
        :param subscriptionEndTime: The end time of the subscription, once passing this date the enumerator will stop
        :param dataResolution: The source enumerator's data resolution
        :param dataTimeZone: Time zone of the underlying source data
        """
        ...

    def RequiresFillForwardData(self, fillForwardResolution: datetime.timedelta, previous: QuantConnect.Data.BaseData, next: QuantConnect.Data.BaseData, fillForward: typing.Optional[QuantConnect.Data.BaseData]) -> typing.Union[bool, QuantConnect.Data.BaseData]:
        """
        Determines whether or not fill forward is required, and if true, will produce the new fill forward data
        
        This method is protected.
        
        :param previous: The last piece of data emitted by this enumerator
        :param next: The next piece of data on the source enumerator, this may be null
        :param fillForward: When this function returns true, this will have a non-null value, null when the function returns false
        :returns: True when a new fill forward piece of data was produced and should be emitted by this enumerator.
        """
        ...


class ScannableEnumerator(typing.Generic[QuantConnect_Lean_Engine_DataFeeds_Enumerators_ScannableEnumerator_T], System.Object):
    """An implementation of IEnumerator{T} that relies on "consolidated" data"""

    @property
    def Current(self) -> QuantConnect_Lean_Engine_DataFeeds_Enumerators_ScannableEnumerator_T:
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    def __init__(self, consolidator: typing.Union[QuantConnect.Data.Consolidators.IDataConsolidator, QuantConnect.Python.PythonConsolidator, datetime.timedelta], timeZone: typing.Any, timeProvider: QuantConnect.ITimeProvider, newDataAvailableHandler: typing.Callable[[System.Object, System.EventArgs], None], isPeriodBased: bool = True) -> None:
        """
        Initializes a new instance of the ScannableEnumerator{T} class
        
        :param consolidator: Consolidator taking BaseData updates and firing events containing new 'consolidated' data
        :param timeZone: The time zone the raw data is time stamped in
        :param timeProvider: The time provider instance used to determine when bars are completed and can be emitted
        :param newDataAvailableHandler: The event handler for a new available data point
        :param isPeriodBased: The consolidator is period based, this will enable scanning on MoveNext
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def MoveNext(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        ...

    def Reset(self) -> None:
        """Sets the enumerator to its initial position, which is before the first element in the collection."""
        ...

    def Update(self, data: QuantConnect_Lean_Engine_DataFeeds_Enumerators_ScannableEnumerator_T) -> None:
        """
        Updates the consolidator
        
        :param data: The data to consolidate
        """
        ...


class LiveSubscriptionEnumerator(System.Object):
    """Enumerator that will subscribe through the provided data queue handler and refresh the subscription if any mapping occurs"""

    @property
    def Current(self) -> QuantConnect.Data.BaseData:
        """The current data object instance"""
        ...

    def __init__(self, dataConfig: QuantConnect.Data.SubscriptionDataConfig, dataQueueHandler: QuantConnect.Interfaces.IDataQueueHandler, handler: typing.Callable[[System.Object, System.EventArgs], None]) -> None:
        """Creates a new instance"""
        ...

    def Dispose(self) -> None:
        """Disposes of the used enumerators"""
        ...

    def MoveNext(self) -> bool:
        """Advances the enumerator to the next element."""
        ...

    def Reset(self) -> None:
        """Reset the IEnumeration"""
        ...


class FrontierAwareEnumerator(System.Object):
    """
    Provides an implementation of IEnumerator{BaseData} that will not emit
    data ahead of the frontier as specified by an instance of ITimeProvider.
    An instance of TimeZoneOffsetProvider is used to convert between UTC
    and the data's native time zone
    """

    @property
    def Current(self) -> QuantConnect.Data.BaseData:
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    def __init__(self, enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData], timeProvider: QuantConnect.ITimeProvider, offsetProvider: QuantConnect.TimeZoneOffsetProvider) -> None:
        """
        Initializes a new instance of the FrontierAwareEnumerator class
        
        :param enumerator: The underlying enumerator to make frontier aware
        :param timeProvider: The time provider used for resolving the current frontier time
        :param offsetProvider: An offset provider used for converting the frontier UTC time into the data's native time zone
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def MoveNext(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        ...

    def Reset(self) -> None:
        """Sets the enumerator to its initial position, which is before the first element in the collection."""
        ...


class EnqueueableEnumerator(typing.Generic[QuantConnect_Lean_Engine_DataFeeds_Enumerators_EnqueueableEnumerator_T], System.Object):
    """
    An implementation of IEnumerator{T} that relies on the
    Enqueue method being called and only ends when Stop
    is called
    """

    @property
    def Count(self) -> int:
        """Gets the current number of items held in the internal queue"""
        ...

    @property
    def LastEnqueued(self) -> QuantConnect_Lean_Engine_DataFeeds_Enumerators_EnqueueableEnumerator_T:
        """Gets the last item that was enqueued"""
        ...

    @property
    def HasFinished(self) -> bool:
        """Returns true if the enumerator has finished and will not accept any more data"""
        ...

    @property
    def Current(self) -> QuantConnect_Lean_Engine_DataFeeds_Enumerators_EnqueueableEnumerator_T:
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    def __init__(self, blocking: bool = False) -> None:
        """
        Initializes a new instance of the EnqueueableEnumerator{T} class
        
        :param blocking: Specifies whether or not to use the blocking behavior
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def Enqueue(self, data: QuantConnect_Lean_Engine_DataFeeds_Enumerators_EnqueueableEnumerator_T) -> None:
        """
        Enqueues the new data into this enumerator
        
        :param data: The data to be enqueued
        """
        ...

    def MoveNext(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        ...

    def Reset(self) -> None:
        """Sets the enumerator to its initial position, which is before the first element in the collection."""
        ...

    def Stop(self) -> None:
        """
        Signals the enumerator to stop enumerating when the items currently
        held inside are gone. No more items will be added to this enumerator.
        """
        ...


class AuxiliaryDataEnumerator(System.Object):
    """
    Auxiliary data enumerator that will, initialize and call the ITradableDateEventProvider.GetEvents
    implementation each time there is a new tradable day for every ITradableDateEventProvider
    provided.
    """

    @property
    def Config(self) -> QuantConnect.Data.SubscriptionDataConfig:
        """
        The associated data configuration
        
        This property is protected.
        """
        ...

    @property
    def Current(self) -> System.Object:
        ...

    def __init__(self, config: QuantConnect.Data.SubscriptionDataConfig, factorFileProvider: QuantConnect.Interfaces.IFactorFileProvider, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider, tradableDateEventProviders: typing.List[QuantConnect.Lean.Engine.DataFeeds.Enumerators.ITradableDateEventProvider], tradableDayNotifier: QuantConnect.Lean.Engine.DataFeeds.Enumerators.ITradableDatesNotifier, startTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Creates a new instance
        
        :param config: The SubscriptionDataConfig
        :param factorFileProvider: The factor file provider to use
        :param mapFileProvider: The MapFile provider to use
        :param tradableDateEventProviders: The tradable dates event providers
        :param tradableDayNotifier: Tradable dates provider
        :param startTime: Start date for the data request
        """
        ...

    def Dispose(self) -> None:
        """Dispose of the Stream Reader and close out the source stream and file connections."""
        ...

    def Initialize(self) -> None:
        """
        Initializes the underlying tradable data event providers
        
        This method is protected.
        """
        ...

    def MoveNext(self) -> bool:
        """
        Advances the enumerator to the next element.
        
        :returns: Always true.
        """
        ...

    def NewTradableDate(self, sender: typing.Any, eventArgs: QuantConnect.NewTradableDateEventArgs) -> None:
        """
        Handle a new tradable date, drives the ITradableDateEventProvider instances
        
        This method is protected.
        """
        ...

    def Reset(self) -> None:
        """Reset the IEnumeration"""
        ...


class LiveMappingEventProvider(QuantConnect.Lean.Engine.DataFeeds.Enumerators.MappingEventProvider):
    """Event provider who will emit SymbolChangedEvent events"""

    def GetEvents(self, eventArgs: QuantConnect.NewTradableDateEventArgs) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]:
        ...


class QuoteBarFillForwardEnumerator(System.Object):
    """
    The QuoteBarFillForwardEnumerator wraps an existing base data enumerator
    If the current QuoteBar has null Bid and/or Ask bars, it copies them from the previous QuoteBar
    """

    @property
    def Current(self) -> QuantConnect.Data.BaseData:
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    @Current.setter
    def Current(self, value: QuantConnect.Data.BaseData):
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    def __init__(self, enumerator: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]) -> None:
        """Initializes a new instance of the FillForwardEnumerator class"""
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def MoveNext(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        ...

    def Reset(self) -> None:
        """Sets the enumerator to its initial position, which is before the first element in the collection."""
        ...


class LiveAuxiliaryDataEnumerator(QuantConnect.Lean.Engine.DataFeeds.Enumerators.AuxiliaryDataEnumerator):
    """Auxiliary data enumerator that will trigger new tradable dates event accordingly"""

    def __init__(self, config: QuantConnect.Data.SubscriptionDataConfig, factorFileProvider: QuantConnect.Interfaces.IFactorFileProvider, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider, tradableDateEventProviders: typing.List[QuantConnect.Lean.Engine.DataFeeds.Enumerators.ITradableDateEventProvider], startTime: typing.Union[datetime.datetime, datetime.date], timeProvider: QuantConnect.ITimeProvider, securityCache: QuantConnect.Securities.SecurityCache) -> None:
        """
        Creates a new instance
        
        :param config: The SubscriptionDataConfig
        :param factorFileProvider: The factor file provider to use
        :param mapFileProvider: The MapFile provider to use
        :param tradableDateEventProviders: The tradable dates event providers
        :param startTime: Start date for the data request
        :param timeProvider: The time provider to use
        :param securityCache: The security cache
        """
        ...

    def MoveNext(self) -> bool:
        ...

    @staticmethod
    def TryCreate(dataConfig: QuantConnect.Data.SubscriptionDataConfig, timeProvider: QuantConnect.ITimeProvider, dataQueueHandler: QuantConnect.Interfaces.IDataQueueHandler, securityCache: QuantConnect.Securities.SecurityCache, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider, fileProvider: QuantConnect.Interfaces.IFactorFileProvider, startTime: typing.Union[datetime.datetime, datetime.date], enumerator: typing.Optional[System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]]) -> typing.Union[bool, System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]]:
        """
        Helper method to create a new instance.
        Knows which security types should create one and determines the appropriate delisting event provider to use
        """
        ...


class DividendEventProvider(System.Object, QuantConnect.Lean.Engine.DataFeeds.Enumerators.ITradableDateEventProvider):
    """Event provider who will emit Dividend events"""

    def GetEvents(self, eventArgs: QuantConnect.NewTradableDateEventArgs) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]:
        """
        Check for dividends and returns them
        
        :param eventArgs: The new tradable day event arguments
        :returns: New Dividend event if any.
        """
        ...

    def Initialize(self, config: QuantConnect.Data.SubscriptionDataConfig, factorFileProvider: QuantConnect.Interfaces.IFactorFileProvider, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider, startTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes this instance
        
        :param config: The SubscriptionDataConfig
        :param factorFileProvider: The factor file provider to use
        :param mapFileProvider: The Data.Auxiliary.MapFile provider to use
        :param startTime: Start date for the data request
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Lean_Engine_DataFeeds_Enumerators__EventContainer_Callable, QuantConnect_Lean_Engine_DataFeeds_Enumerators__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Lean_Engine_DataFeeds_Enumerators__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Lean_Engine_DataFeeds_Enumerators__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Lean_Engine_DataFeeds_Enumerators__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


