from typing import overload
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Consolidators
import QuantConnect.Data.Market
import QuantConnect.Python
import System

QuantConnect_Data_Consolidators_ClassicRenkoConsolidator = typing.Any
QuantConnect_Data_Consolidators_RenkoConsolidator = typing.Any

QuantConnect_Data_Consolidators_FilteredIdentityDataConsolidator_T = typing.TypeVar("QuantConnect_Data_Consolidators_FilteredIdentityDataConsolidator_T")
QuantConnect_Data_Consolidators_IdentityDataConsolidator_T = typing.TypeVar("QuantConnect_Data_Consolidators_IdentityDataConsolidator_T")
QuantConnect_Data_Consolidators_ClassicRenkoConsolidator_TInput = typing.TypeVar("QuantConnect_Data_Consolidators_ClassicRenkoConsolidator_TInput")
QuantConnect_Data_Consolidators_DataConsolidator_TInput = typing.TypeVar("QuantConnect_Data_Consolidators_DataConsolidator_TInput")
QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_T = typing.TypeVar("QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_T")
QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_TConsolidated = typing.TypeVar("QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_TConsolidated")
QuantConnect_Data_Consolidators_RenkoConsolidator_TInput = typing.TypeVar("QuantConnect_Data_Consolidators_RenkoConsolidator_TInput")
QuantConnect_Data_Consolidators_WickedRenkoConsolidator_T = typing.TypeVar("QuantConnect_Data_Consolidators_WickedRenkoConsolidator_T")
QuantConnect_Data_Consolidators_TradeBarConsolidatorBase_T = typing.TypeVar("QuantConnect_Data_Consolidators_TradeBarConsolidatorBase_T")
QuantConnect_Data_Consolidators__EventContainer_Callable = typing.TypeVar("QuantConnect_Data_Consolidators__EventContainer_Callable")
QuantConnect_Data_Consolidators__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Data_Consolidators__EventContainer_ReturnType")


class IDataConsolidator(System.IDisposable, metaclass=abc.ABCMeta):
    """
    Represents a type capable of taking BaseData updates and firing events containing new
    'consolidated' data. These types can be used to produce larger bars, or even be used to
    transform the data before being sent to another component. The most common usage of these
    types is with indicators.
    """

    @property
    @abc.abstractmethod
    def Consolidated(self) -> QuantConnect.Data.IBaseData:
        """
        Gets the most recently consolidated piece of data. This will be null if this consolidator
        has not produced any data yet.
        """
        ...

    @property
    @abc.abstractmethod
    def WorkingData(self) -> QuantConnect.Data.IBaseData:
        """Gets a clone of the data being currently consolidated"""
        ...

    @property
    @abc.abstractmethod
    def InputType(self) -> typing.Type:
        """Gets the type consumed by this consolidator"""
        ...

    @property
    @abc.abstractmethod
    def OutputType(self) -> typing.Type:
        """Gets the type produced by this consolidator"""
        ...

    @property
    @abc.abstractmethod
    def DataConsolidated(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.IBaseData], None], None]:
        """Event handler that fires when a new piece of data is produced"""
        ...

    @DataConsolidated.setter
    @abc.abstractmethod
    def DataConsolidated(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.IBaseData], None], None]):
        """Event handler that fires when a new piece of data is produced"""
        ...

    def Scan(self, currentLocalTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scans this consolidator to see if it should emit a bar due to time passing
        
        :param currentLocalTime: The current time in the local time zone (same as BaseData.Time)
        """
        ...

    def Update(self, data: QuantConnect.Data.IBaseData) -> None:
        """
        Updates this consolidator with the specified data
        
        :param data: The new data for the consolidator
        """
        ...


class DataConsolidator(typing.Generic[QuantConnect_Data_Consolidators_DataConsolidator_TInput], System.Object, QuantConnect.Data.Consolidators.IDataConsolidator, metaclass=abc.ABCMeta):
    """
    Represents a type that consumes BaseData instances and fires an event with consolidated
    and/or aggregated data.
    """

    @property
    def DataConsolidated(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.IBaseData], None], None]:
        """Event handler that fires when a new piece of data is produced"""
        ...

    @DataConsolidated.setter
    def DataConsolidated(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.IBaseData], None], None]):
        """Event handler that fires when a new piece of data is produced"""
        ...

    @property
    def Consolidated(self) -> QuantConnect.Data.IBaseData:
        """
        Gets the most recently consolidated piece of data. This will be null if this consolidator
        has not produced any data yet.
        """
        ...

    @Consolidated.setter
    def Consolidated(self, value: QuantConnect.Data.IBaseData):
        """
        Gets the most recently consolidated piece of data. This will be null if this consolidator
        has not produced any data yet.
        """
        ...

    @property
    @abc.abstractmethod
    def WorkingData(self) -> QuantConnect.Data.IBaseData:
        """Gets a clone of the data being currently consolidated"""
        ...

    @property
    def InputType(self) -> typing.Type:
        """Gets the type consumed by this consolidator"""
        ...

    @property
    @abc.abstractmethod
    def OutputType(self) -> typing.Type:
        """Gets the type produced by this consolidator"""
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def OnDataConsolidated(self, consolidated: QuantConnect.Data.IBaseData) -> None:
        """
        Event invocator for the DataConsolidated event. This should be invoked
        by derived classes when they have consolidated a new piece of data.
        
        This method is protected.
        
        :param consolidated: The newly consolidated data
        """
        ...

    def Scan(self, currentLocalTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scans this consolidator to see if it should emit a bar due to time passing
        
        :param currentLocalTime: The current time in the local time zone (same as BaseData.Time)
        """
        ...

    @overload
    def Update(self, data: QuantConnect.Data.IBaseData) -> None:
        """
        Updates this consolidator with the specified data
        
        :param data: The new data for the consolidator
        """
        ...

    @overload
    def Update(self, data: QuantConnect_Data_Consolidators_DataConsolidator_TInput) -> None:
        """
        Updates this consolidator with the specified data. This method is
        responsible for raising the DataConsolidated event
        
        :param data: The new data for the consolidator
        """
        ...


class CalendarInfo:
    """Calendar Info for storing information related to the start and period of a consolidator"""

    @property
    def Start(self) -> datetime.datetime:
        """Calendar Start"""
        ...

    @property
    def Period(self) -> datetime.timedelta:
        """Consolidation Period"""
        ...

    def __init__(self, start: typing.Union[datetime.datetime, datetime.date], period: datetime.timedelta) -> None:
        """
        Constructor for CalendarInfo; used for consolidation calendar
        
        :param start: Calendar Start
        :param period: Consolidation Period
        """
        ...


class PeriodCountConsolidatorBase(typing.Generic[QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_T, QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_TConsolidated], QuantConnect.Data.Consolidators.DataConsolidator[QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_T], metaclass=abc.ABCMeta):
    """
    Provides a base class for consolidators that emit data based on the passing of a period of time
    or after seeing a max count of data points.
    """

    @property
    def OutputType(self) -> typing.Type:
        """Gets the type produced by this consolidator"""
        ...

    @property
    def WorkingData(self) -> QuantConnect.Data.IBaseData:
        """Gets a clone of the data being currently consolidated"""
        ...

    @property
    def DataConsolidated(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_TConsolidated], None], None]:
        """
        Event handler that fires when a new piece of data is produced. We define this as a 'new'
        event so we can expose it as a TConsolidated instead of a BaseData instance
        """
        ...

    @DataConsolidated.setter
    def DataConsolidated(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_TConsolidated], None], None]):
        """
        Event handler that fires when a new piece of data is produced. We define this as a 'new'
        event so we can expose it as a TConsolidated instead of a BaseData instance
        """
        ...

    @property
    def IsTimeBased(self) -> bool:
        """
        Returns true if this consolidator is time-based, false otherwise
        
        This property is protected.
        """
        ...

    @property
    def Period(self) -> typing.Optional[datetime.timedelta]:
        """
        Gets the time period for this consolidator
        
        This property is protected.
        """
        ...

    @overload
    def __init__(self, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new TConsolidated instance representing the period
        
        This method is protected.
        
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, maxCount: int) -> None:
        """
        Creates a consolidator to produce a new TConsolidated instance representing the last count pieces of data
        
        This method is protected.
        
        :param maxCount: The number of pieces to accept before emiting a consolidated bar
        """
        ...

    @overload
    def __init__(self, maxCount: int, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new TConsolidated instance representing the last count pieces of data or the period, whichever comes first
        
        This method is protected.
        
        :param maxCount: The number of pieces to accept before emiting a consolidated bar
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, func: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]) -> None:
        """
        Creates a consolidator to produce a new TConsolidated instance representing the last count pieces of data or the period, whichever comes first
        
        This method is protected.
        
        :param func: Func that defines the start time of a consolidated data
        """
        ...

    @overload
    def __init__(self, pyObject: typing.Any) -> None:
        """
        Creates a consolidator to produce a new TConsolidated instance representing the last count pieces of data or the period, whichever comes first
        
        This method is protected.
        
        :param pyObject: Python object that defines either a function object that defines the start time of a consolidated data or a timespan
        """
        ...

    def AggregateBar(self, workingBar: QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_TConsolidated, data: QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_T) -> None:
        """
        Aggregates the new 'data' into the 'workingBar'. The 'workingBar' will be
        null following the event firing
        
        This method is protected.
        
        :param workingBar: The bar we're building, null if the event was just fired and we're starting a new consolidated bar
        :param data: The new data
        """
        ...

    @overload
    def GetRoundedBarTime(self, time: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """
        Gets a rounded-down bar time. Called by AggregateBar in derived classes.
        
        This method is protected.
        
        :param time: The bar time to be rounded down
        :returns: The rounded bar time.
        """
        ...

    @overload
    def GetRoundedBarTime(self, inputData: QuantConnect.Data.IBaseData) -> datetime.datetime:
        """
        Gets a rounded-down bar start time. Called by AggregateBar in derived classes.
        
        This method is protected.
        
        :param inputData: The input data point
        :returns: The rounded bar start time.
        """
        ...

    def OnDataConsolidated(self, e: QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_TConsolidated) -> None:
        """
        Event invocator for the DataConsolidated event
        
        This method is protected.
        
        :param e: The consolidated data
        """
        ...

    def Scan(self, currentLocalTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scans this consolidator to see if it should emit a bar due to time passing
        
        :param currentLocalTime: The current time in the local time zone (same as BaseData.Time)
        """
        ...

    def ShouldProcess(self, data: QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_T) -> bool:
        """
        Determines whether or not the specified data should be processed
        
        This method is protected.
        
        :param data: The data to check
        :returns: True if the consolidator should process this data, false otherwise.
        """
        ...

    def Update(self, data: QuantConnect_Data_Consolidators_PeriodCountConsolidatorBase_T) -> None:
        """
        Updates this consolidator with the specified data. This method is
        responsible for raising the DataConsolidated event
        In time span mode, the bar range is closed on the left and open on the right: [T, T+TimeSpan).
        For example, if time span is 1 minute, we have [10:00, 10:01): so data at 10:01 is not
        included in the bar starting at 10:00.
        
        :param data: The new data for the consolidator
        """
        ...


class TradeBarConsolidatorBase(typing.Generic[QuantConnect_Data_Consolidators_TradeBarConsolidatorBase_T], QuantConnect.Data.Consolidators.PeriodCountConsolidatorBase[QuantConnect_Data_Consolidators_TradeBarConsolidatorBase_T, QuantConnect.Data.Market.TradeBar], metaclass=abc.ABCMeta):
    """
    A data consolidator that can make bigger bars from any base data
    
    This type acts as the base for other consolidators that produce bars on a given time step or for a count of data.
    """

    @property
    def WorkingBar(self) -> QuantConnect.Data.Market.TradeBar:
        """Gets a copy of the current 'workingBar'."""
        ...

    @overload
    def __init__(self, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the period
        
        This method is protected.
        
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, maxCount: int) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data
        
        This method is protected.
        
        :param maxCount: The number of pieces to accept before emiting a consolidated bar
        """
        ...

    @overload
    def __init__(self, maxCount: int, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data or the period, whichever comes first
        
        This method is protected.
        
        :param maxCount: The number of pieces to accept before emiting a consolidated bar
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, func: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data or the period, whichever comes first
        
        This method is protected.
        
        :param func: Func that defines the start time of a consolidated data
        """
        ...

    @overload
    def __init__(self, pyfuncobj: typing.Any) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data or the period, whichever comes first
        
        This method is protected.
        
        :param pyfuncobj: Python function object that defines the start time of a consolidated data
        """
        ...


class TickConsolidator(QuantConnect.Data.Consolidators.TradeBarConsolidatorBase[QuantConnect.Data.Market.Tick]):
    """
    A data consolidator that can make bigger bars from ticks over a given
    time span or a count of pieces of data.
    """

    @overload
    def __init__(self, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the period
        
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, maxCount: int) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data
        
        :param maxCount: The number of pieces to accept before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, maxCount: int, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data or the period, whichever comes first
        
        :param maxCount: The number of pieces to accept before emitting a consolidated bar
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, func: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]) -> None:
        """
        Initializes a new instance of the TickQuoteBarConsolidator class
        
        :param func: Func that defines the start time of a consolidated data
        """
        ...

    @overload
    def __init__(self, pyfuncobj: typing.Any) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data or the period, whichever comes first
        
        :param pyfuncobj: Python function object that defines the start time of a consolidated data
        """
        ...

    def AggregateBar(self, workingBar: QuantConnect.Data.Market.TradeBar, data: QuantConnect.Data.Market.Tick) -> None:
        """
        Aggregates the new 'data' into the 'workingBar'. The 'workingBar' will be
        null following the event firing
        
        This method is protected.
        
        :param workingBar: The bar we're building
        :param data: The new data
        """
        ...

    def ShouldProcess(self, data: QuantConnect.Data.Market.Tick) -> bool:
        """
        Determines whether or not the specified data should be processed
        
        This method is protected.
        
        :param data: The data to check
        :returns: True if the consolidator should process this data, false otherwise.
        """
        ...


class IdentityDataConsolidator(typing.Generic[QuantConnect_Data_Consolidators_IdentityDataConsolidator_T], QuantConnect.Data.Consolidators.DataConsolidator[QuantConnect_Data_Consolidators_IdentityDataConsolidator_T]):
    """
    Represents the simplest DataConsolidator implementation, one that is defined
    by a straight pass through of the data. No projection or aggregation is performed.
    """

    @property
    def WorkingData(self) -> QuantConnect.Data.IBaseData:
        """Gets a clone of the data being currently consolidated"""
        ...

    @property
    def OutputType(self) -> typing.Type:
        """Gets the type produced by this consolidator"""
        ...

    def Scan(self, currentLocalTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scans this consolidator to see if it should emit a bar due to time passing
        
        :param currentLocalTime: The current time in the local time zone (same as BaseData.Time)
        """
        ...

    def Update(self, data: QuantConnect_Data_Consolidators_IdentityDataConsolidator_T) -> None:
        """
        Updates this consolidator with the specified data
        
        :param data: The new data for the consolidator
        """
        ...


class FilteredIdentityDataConsolidator(typing.Generic[QuantConnect_Data_Consolidators_FilteredIdentityDataConsolidator_T], QuantConnect.Data.Consolidators.IdentityDataConsolidator[QuantConnect_Data_Consolidators_FilteredIdentityDataConsolidator_T]):
    """
    Provides an implementation of IDataConsolidator that preserve the input
    data unmodified. The input data is filtering by the specified predicate function
    """

    def __init__(self, predicate: typing.Callable[[QuantConnect_Data_Consolidators_FilteredIdentityDataConsolidator_T], bool]) -> None:
        """
        Initializes a new instance of the FilteredIdentityDataConsolidator{T} class
        
        :param predicate: The predicate function, returning true to accept data and false to reject data
        """
        ...

    @staticmethod
    def ForTickType(tickType: QuantConnect.TickType) -> QuantConnect.Data.Consolidators.FilteredIdentityDataConsolidator[QuantConnect.Data.Market.Tick]:
        """
        Creates a new instance of FilteredIdentityDataConsolidator{T} that filters ticks
        based on the specified TickType
        
        :param tickType: The tick type of data to accept
        :returns: A new FilteredIdentityDataConsolidator{T} that filters based on the provided tick type.
        """
        ...

    def Update(self, data: QuantConnect_Data_Consolidators_FilteredIdentityDataConsolidator_T) -> None:
        """
        Updates this consolidator with the specified data
        
        :param data: The new data for the consolidator
        """
        ...


class TradeBarConsolidator(QuantConnect.Data.Consolidators.TradeBarConsolidatorBase[QuantConnect.Data.Market.TradeBar]):
    """
    A data consolidator that can make bigger bars from smaller ones over a given
    time span or a count of pieces of data.
    
    Use this consolidator to turn data of a lower resolution into data of a higher resolution,
    for example, if you subscribe to minute data but want to have a 15 minute bar.
    """

    @overload
    def __init__(self, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the period
        
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, maxCount: int) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data
        
        :param maxCount: The number of pieces to accept before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, maxCount: int, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data or the period, whichever comes first
        
        :param maxCount: The number of pieces to accept before emitting a consolidated bar
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, func: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data or the period, whichever comes first
        
        :param func: Func that defines the start time of a consolidated data
        """
        ...

    @overload
    def __init__(self, pyfuncobj: typing.Any) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data or the period, whichever comes first
        
        :param pyfuncobj: Python function object that defines the start time of a consolidated data
        """
        ...

    def AggregateBar(self, workingBar: QuantConnect.Data.Market.TradeBar, data: QuantConnect.Data.Market.TradeBar) -> None:
        """
        Aggregates the new 'data' into the 'workingBar'. The 'workingBar' will be
        null following the event firing
        
        This method is protected.
        
        :param workingBar: The bar we're building, null if the event was just fired and we're starting a new trade bar
        :param data: The new data
        """
        ...

    @staticmethod
    def FromResolution(resolution: QuantConnect.Resolution) -> QuantConnect.Data.Consolidators.TradeBarConsolidator:
        """
        Create a new TradeBarConsolidator for the desired resolution
        
        :param resolution: The resolution desired
        :returns: A consolidator that produces data on the resolution interval.
        """
        ...


class ClassicRenkoConsolidator(typing.Generic[QuantConnect_Data_Consolidators_ClassicRenkoConsolidator_TInput], QuantConnect_Data_Consolidators_ClassicRenkoConsolidator):
    """Provides a type safe wrapper on the RenkoConsolidator class. This just allows us to define our selector functions with the real type they'll be receiving"""

    @property
    def Type(self) -> int:
        """
        Gets the kind of the bar
        
        This property contains the int value of a member of the QuantConnect.Data.Market.RenkoType enum.
        """
        ...

    @property
    def WorkingData(self) -> QuantConnect.Data.IBaseData:
        """Gets a clone of the data being currently consolidated"""
        ...

    @property
    def InputType(self) -> typing.Type:
        """Gets the type consumed by this consolidator"""
        ...

    @property
    def OutputType(self) -> typing.Type:
        """Gets RenkoBar which is the type emitted in the IDataConsolidator.DataConsolidated event."""
        ...

    @property
    def Consolidated(self) -> QuantConnect.Data.IBaseData:
        """
        Gets the most recently consolidated piece of data. This will be null if this consolidator
        has not produced any data yet.
        """
        ...

    @Consolidated.setter
    def Consolidated(self, value: QuantConnect.Data.IBaseData):
        """
        Gets the most recently consolidated piece of data. This will be null if this consolidator
        has not produced any data yet.
        """
        ...

    @property
    def DataConsolidated(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.Market.RenkoBar], None], None]:
        """Event handler that fires when a new piece of data is produced"""
        ...

    @DataConsolidated.setter
    def DataConsolidated(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.Market.RenkoBar], None], None]):
        """Event handler that fires when a new piece of data is produced"""
        ...

    @overload
    def __init__(self, barSize: float, evenBars: bool = True) -> None:
        """
        Initializes a new instance of the ClassicRenkoConsolidator class using the specified .
        The value selector will by default select IBaseData.Value
        The volume selector will by default select zero.
        
        :param barSize: The constant value size of each bar
        :param evenBars: When true bar open/close will be a multiple of the barSize
        """
        ...

    @overload
    def __init__(self, barSize: float, selector: typing.Callable[[QuantConnect.Data.IBaseData], float], volumeSelector: typing.Callable[[QuantConnect.Data.IBaseData], float] = None, evenBars: bool = True) -> None:
        """
        Initializes a new instance of the ClassicRenkoConsolidator class.
        
        :param barSize: The size of each bar in units of the value produced by
        :param selector: Extracts the value from a data instance to be formed into a RenkoBar. The default value is (x => x.Value) the IBaseData.Value property on IBaseData
        :param volumeSelector: Extracts the volume from a data instance. The default value is null which does not aggregate volume per bar.
        :param evenBars: When true bar open/close will be a multiple of the barSize
        """
        ...

    @overload
    def __init__(self, barSize: float, selector: typing.Any, volumeSelector: typing.Any = None, evenBars: bool = True) -> None:
        """
        Initializes a new instance of the ClassicRenkoConsolidator class.
        
        :param barSize: The size of each bar in units of the value produced by
        :param selector: Extracts the value from a data instance to be formed into a RenkoBar. The default value is (x => x.Value) the IBaseData.Value property on IBaseData
        :param volumeSelector: Extracts the volume from a data instance. The default value is null which does not aggregate volume per bar.
        :param evenBars: When true bar open/close will be a multiple of the barSize
        """
        ...

    @overload
    def __init__(self, barSize: float, selector: typing.Callable[[QuantConnect_Data_Consolidators_ClassicRenkoConsolidator_TInput], float], volumeSelector: typing.Callable[[QuantConnect_Data_Consolidators_ClassicRenkoConsolidator_TInput], float] = None, evenBars: bool = True) -> None:
        """
        Initializes a new instance of the ClassicRenkoConsolidator class.
        
        :param barSize: The size of each bar in units of the value produced by
        :param selector: Extracts the value from a data instance to be formed into a RenkoBar. The default value is (x => x.Value) the IBaseData.Value property on IBaseData
        :param volumeSelector: Extracts the volume from a data instance. The default value is null which does not aggregate volume per bar.
        :param evenBars: When true bar open/close will be a multiple of the barSize
        """
        ...

    @overload
    def __init__(self, barSize: float, evenBars: bool = True) -> None:
        """
        Initializes a new instance of the ClassicRenkoConsolidator class using the specified .
        The value selector will by default select IBaseData.Value
        The volume selector will by default select zero.
        
        :param barSize: The constant value size of each bar
        :param evenBars: When true bar open/close will be a multiple of the barSize
        """
        ...

    @overload
    def __init__(self, barSize: float, type: QuantConnect.Data.Market.RenkoType) -> None:
        """
        Initializes a new instance of the ClassicRenkoConsolidator class.
        
        Please use the new RenkoConsolidator if RenkoType is not Classic
        
        :param barSize: The constant value size of each bar
        :param type: The RenkoType of the bar
        """
        ...

    @overload
    def __init__(self, barSize: float, type: QuantConnect.Data.Market.RenkoType) -> None:
        """
        Initializes a new instance of the ClassicRenkoConsolidator class using the specified .
        The value selector will by default select IBaseData.Value
        The volume selector will by default select zero.
        
        Please use the WickedRenkoConsolidator if RenkoType is not Classic
        
        :param barSize: The constant value size of each bar
        :param type: The RenkoType of the bar
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def Scan(self, currentLocalTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scans this consolidator to see if it should emit a bar due to time passing
        
        :param currentLocalTime: The current time in the local time zone (same as BaseData.Time)
        """
        ...

    @overload
    def Update(self, data: QuantConnect.Data.IBaseData) -> None:
        """
        Updates this consolidator with the specified data
        
        :param data: The new data for the consolidator
        """
        ...

    @overload
    def Update(self, data: QuantConnect_Data_Consolidators_ClassicRenkoConsolidator_TInput) -> None:
        """
        Updates this consolidator with the specified data.
        
        :param data: The new data for the consolidator
        """
        ...


class OpenInterestConsolidator(QuantConnect.Data.Consolidators.PeriodCountConsolidatorBase[QuantConnect.Data.Market.Tick, QuantConnect.Data.Market.OpenInterest]):
    """Type capable of consolidating open interest"""

    @overload
    def __init__(self, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new 'OpenInterest' representing the period
        
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, maxCount: int) -> None:
        """
        Creates a consolidator to produce a new 'OpenInterest' representing the last count pieces of data
        
        :param maxCount: The number of pieces to accept before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, maxCount: int, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new 'OpenInterest' representing the last count pieces of data or the period, whichever comes first
        
        :param maxCount: The number of pieces to accept before emitting a consolidated bar
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, func: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]) -> None:
        """
        Creates a consolidator to produce a new 'OpenInterest'
        
        :param func: Func that defines the start time of a consolidated data
        """
        ...

    @overload
    def __init__(self, pyfuncobj: typing.Any) -> None:
        """
        Creates a consolidator to produce a new 'OpenInterest'
        
        :param pyfuncobj: Python function object that defines the start time of a consolidated data
        """
        ...

    def AggregateBar(self, workingBar: QuantConnect.Data.Market.OpenInterest, tick: QuantConnect.Data.Market.Tick) -> None:
        """
        Aggregates the new 'data' into the 'workingBar'. The 'workingBar' will be
        null following the event firing
        
        This method is protected.
        
        :param workingBar: The bar we're building, null if the event was just fired and we're starting a new OI bar
        :param tick: The new data
        """
        ...

    @staticmethod
    def FromResolution(resolution: QuantConnect.Resolution) -> QuantConnect.Data.Consolidators.OpenInterestConsolidator:
        """
        Create a new OpenInterestConsolidator for the desired resolution
        
        :param resolution: The resolution desired
        :returns: A consolidator that produces data on the resolution interval.
        """
        ...

    def ShouldProcess(self, tick: QuantConnect.Data.Market.Tick) -> bool:
        """
        Determines whether or not the specified data should be processed
        
        This method is protected.
        
        :param tick: The data to check
        :returns: True if the consolidator should process this data, false otherwise.
        """
        ...


class SequentialConsolidator(System.Object, QuantConnect.Data.Consolidators.IDataConsolidator):
    """
    This consolidator wires up the events on its First and Second consolidators
    such that data flows from the First to Second consolidator. It's output comes
    from the Second.
    """

    @property
    def First(self) -> QuantConnect.Data.Consolidators.IDataConsolidator:
        """Gets the first consolidator to receive data"""
        ...

    @First.setter
    def First(self, value: QuantConnect.Data.Consolidators.IDataConsolidator):
        """Gets the first consolidator to receive data"""
        ...

    @property
    def Second(self) -> QuantConnect.Data.Consolidators.IDataConsolidator:
        """
        Gets the second consolidator that ends up receiving data produced
        by the first
        """
        ...

    @Second.setter
    def Second(self, value: QuantConnect.Data.Consolidators.IDataConsolidator):
        """
        Gets the second consolidator that ends up receiving data produced
        by the first
        """
        ...

    @property
    def Consolidated(self) -> QuantConnect.Data.IBaseData:
        """
        Gets the most recently consolidated piece of data. This will be null if this consolidator
        has not produced any data yet.
        
        For a SequentialConsolidator, this is the output from the 'Second' consolidator.
        """
        ...

    @property
    def WorkingData(self) -> QuantConnect.Data.IBaseData:
        """Gets a clone of the data being currently consolidated"""
        ...

    @property
    def InputType(self) -> typing.Type:
        """Gets the type consumed by this consolidator"""
        ...

    @property
    def OutputType(self) -> typing.Type:
        """Gets the type produced by this consolidator"""
        ...

    @property
    def DataConsolidated(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.IBaseData], None], None]:
        """Event handler that fires when a new piece of data is produced"""
        ...

    @DataConsolidated.setter
    def DataConsolidated(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.IBaseData], None], None]):
        """Event handler that fires when a new piece of data is produced"""
        ...

    def __init__(self, first: typing.Union[QuantConnect.Data.Consolidators.IDataConsolidator, QuantConnect.Python.PythonConsolidator, datetime.timedelta], second: typing.Union[QuantConnect.Data.Consolidators.IDataConsolidator, QuantConnect.Python.PythonConsolidator, datetime.timedelta]) -> None:
        """
        Creates a new consolidator that will pump date through the first, and then the output
        of the first into the second. This enables 'wrapping' or 'composing' of consolidators
        
        :param first: The first consolidator to receive data
        :param second: The consolidator to receive first's output
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def OnDataConsolidated(self, consolidated: QuantConnect.Data.IBaseData) -> None:
        """
        Event invocator for the DataConsolidated event. This should be invoked
        by derived classes when they have consolidated a new piece of data.
        
        This method is protected.
        
        :param consolidated: The newly consolidated data
        """
        ...

    def Scan(self, currentLocalTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scans this consolidator to see if it should emit a bar due to time passing
        
        :param currentLocalTime: The current time in the local time zone (same as BaseData.Time)
        """
        ...

    def Update(self, data: QuantConnect.Data.IBaseData) -> None:
        """
        Updates this consolidator with the specified data
        
        :param data: The new data for the consolidator
        """
        ...


class CalendarType(System.Object):
    """
    Calendar Type Class; now obsolete routes functions to Calendar
    
    CalendarType is obsolete, please use Calendar instead
    """

    Weekly: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]
    """Computes the start of week (previous Monday) of given date/time"""

    Monthly: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]
    """Computes the start of month (1st of the current month) of given date/time"""


class RenkoConsolidator(typing.Generic[QuantConnect_Data_Consolidators_RenkoConsolidator_TInput], QuantConnect_Data_Consolidators_RenkoConsolidator):
    """Provides a type safe wrapper on the RenkoConsolidator class. This just allows us to define our selector functions with the real type they'll be receiving"""

    @property
    def CloseOn(self) -> datetime.datetime:
        """
        Time of consolidated close.
        
        This field is protected.
        """
        ...

    @CloseOn.setter
    def CloseOn(self, value: datetime.datetime):
        """
        Time of consolidated close.
        
        This field is protected.
        """
        ...

    @property
    def CloseRate(self) -> float:
        """
        Value of consolidated close.
        
        This field is protected.
        """
        ...

    @CloseRate.setter
    def CloseRate(self, value: float):
        """
        Value of consolidated close.
        
        This field is protected.
        """
        ...

    @property
    def HighRate(self) -> float:
        """
        Value of consolidated high.
        
        This field is protected.
        """
        ...

    @HighRate.setter
    def HighRate(self, value: float):
        """
        Value of consolidated high.
        
        This field is protected.
        """
        ...

    @property
    def LowRate(self) -> float:
        """
        Value of consolidated low.
        
        This field is protected.
        """
        ...

    @LowRate.setter
    def LowRate(self, value: float):
        """
        Value of consolidated low.
        
        This field is protected.
        """
        ...

    @property
    def OpenOn(self) -> datetime.datetime:
        """
        Time of consolidated open.
        
        This field is protected.
        """
        ...

    @OpenOn.setter
    def OpenOn(self, value: datetime.datetime):
        """
        Time of consolidated open.
        
        This field is protected.
        """
        ...

    @property
    def OpenRate(self) -> float:
        """
        Value of consolidate open.
        
        This field is protected.
        """
        ...

    @OpenRate.setter
    def OpenRate(self, value: float):
        """
        Value of consolidate open.
        
        This field is protected.
        """
        ...

    @property
    def BarSize(self) -> float:
        """
        Size of the consolidated bar.
        
        This field is protected.
        """
        ...

    @BarSize.setter
    def BarSize(self, value: float):
        """
        Size of the consolidated bar.
        
        This field is protected.
        """
        ...

    @property
    def Type(self) -> int:
        """
        Gets the kind of the bar
        
        This property contains the int value of a member of the QuantConnect.Data.Market.RenkoType enum.
        """
        ...

    @property
    def WorkingData(self) -> QuantConnect.Data.IBaseData:
        """Gets a clone of the data being currently consolidated"""
        ...

    @property
    def InputType(self) -> typing.Type:
        """Gets the type consumed by this consolidator"""
        ...

    @property
    def OutputType(self) -> typing.Type:
        """Gets RenkoBar which is the type emitted in the IDataConsolidator.DataConsolidated event."""
        ...

    @property
    def Consolidated(self) -> QuantConnect.Data.IBaseData:
        """
        Gets the most recently consolidated piece of data. This will be null if this consolidator
        has not produced any data yet.
        """
        ...

    @Consolidated.setter
    def Consolidated(self, value: QuantConnect.Data.IBaseData):
        """
        Gets the most recently consolidated piece of data. This will be null if this consolidator
        has not produced any data yet.
        """
        ...

    @property
    def DataConsolidated(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.Market.RenkoBar], None], None]:
        """Event handler that fires when a new piece of data is produced"""
        ...

    @DataConsolidated.setter
    def DataConsolidated(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.Market.RenkoBar], None], None]):
        """Event handler that fires when a new piece of data is produced"""
        ...

    @overload
    def __init__(self, barSize: float) -> None:
        """
        Initializes a new instance of the RenkoConsolidator class using the specified .
        
        :param barSize: The constant value size of each bar
        """
        ...

    @overload
    def __init__(self, barSize: float) -> None:
        """
        Initializes a new instance of the RenkoConsolidator class using the specified .
        
        :param barSize: The constant value size of each bar
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def OnDataConsolidated(self, consolidated: QuantConnect.Data.Market.RenkoBar) -> None:
        """
        Event invocator for the DataConsolidated event. This should be invoked
        by derived classes when they have consolidated a new piece of data.
        
        This method is protected.
        
        :param consolidated: The newly consolidated data
        """
        ...

    def Scan(self, currentLocalTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scans this consolidator to see if it should emit a bar due to time passing
        
        :param currentLocalTime: The current time in the local time zone (same as BaseData.Time)
        """
        ...

    @overload
    def Update(self, data: QuantConnect.Data.IBaseData) -> None:
        """
        Updates this consolidator with the specified data
        
        :param data: The new data for the consolidator
        """
        ...

    @overload
    def Update(self, data: QuantConnect_Data_Consolidators_RenkoConsolidator_TInput) -> None:
        """
        Updates this consolidator with the specified data.
        
        :param data: The new data for the consolidator
        """
        ...


class WickedRenkoConsolidator(typing.Generic[QuantConnect_Data_Consolidators_WickedRenkoConsolidator_T], QuantConnect.Data.Consolidators.RenkoConsolidator[QuantConnect_Data_Consolidators_WickedRenkoConsolidator_T]):
    """
    This consolidator can transform a stream of BaseData instances into a stream of RenkoBar
    with Renko type RenkoType.Wicked.
    Provides a type safe wrapper on the WickedRenkoConsolidator class. This just allows us to define our selector functions with the real type they'll be receiving
    ///
    """

    @overload
    def __init__(self, barSize: float) -> None:
        """
        Initializes a new instance of the RenkoConsolidator class using the specified .
        
        :param barSize: The constant value size of each bar
        """
        ...

    @overload
    def __init__(self, barSize: float) -> None:
        """
        Initializes a new instance of the RenkoConsolidator class using the specified .
        
        :param barSize: The constant value size of each bar
        """
        ...


class DynamicDataConsolidator(QuantConnect.Data.Consolidators.TradeBarConsolidatorBase[QuantConnect.Data.DynamicData]):
    """
    A data csolidator that can make trade bars from DynamicData derived types. This is useful for
    aggregating Quandl and other highly flexible dynamic custom data types.
    """

    @overload
    def __init__(self, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the period.
        
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, maxCount: int) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data.
        
        :param maxCount: The number of pieces to accept before emiting a consolidated bar
        """
        ...

    @overload
    def __init__(self, maxCount: int, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data or the period, whichever comes first.
        
        :param maxCount: The number of pieces to accept before emiting a consolidated bar
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, func: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data or the period, whichever comes first.
        
        :param func: Func that defines the start time of a consolidated data
        """
        ...

    def AggregateBar(self, workingBar: QuantConnect.Data.Market.TradeBar, data: QuantConnect.Data.DynamicData) -> None:
        """
        Aggregates the new 'data' into the 'workingBar'. The 'workingBar' will be
        null following the event firing
        
        This method is protected.
        
        :param workingBar: The bar we're building, null if the event was just fired and we're starting a new trade bar
        :param data: The new data
        """
        ...


class BaseDataConsolidator(QuantConnect.Data.Consolidators.TradeBarConsolidatorBase[QuantConnect.Data.BaseData]):
    """Type capable of consolidating trade bars from any base data instance"""

    @overload
    def __init__(self, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the period
        
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, maxCount: int) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data
        
        :param maxCount: The number of pieces to accept before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, maxCount: int, period: datetime.timedelta) -> None:
        """
        Creates a consolidator to produce a new 'TradeBar' representing the last count pieces of data or the period, whichever comes first
        
        :param maxCount: The number of pieces to accept before emitting a consolidated bar
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, func: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]) -> None:
        """
        Initializes a new instance of the BaseDataConsolidator class
        
        :param func: Func that defines the start time of a consolidated data
        """
        ...

    @overload
    def __init__(self, pyfuncobj: typing.Any) -> None:
        """
        Initializes a new instance of the BaseDataConsolidator class
        
        :param pyfuncobj: Func that defines the start time of a consolidated data
        """
        ...

    def AggregateBar(self, workingBar: QuantConnect.Data.Market.TradeBar, data: QuantConnect.Data.BaseData) -> None:
        """
        Aggregates the new 'data' into the 'workingBar'. The 'workingBar' will be
        null following the event firing
        
        This method is protected.
        
        :param workingBar: The bar we're building, null if the event was just fired and we're starting a new trade bar
        :param data: The new data
        """
        ...

    @staticmethod
    def FromResolution(resolution: QuantConnect.Resolution) -> QuantConnect.Data.Consolidators.BaseDataConsolidator:
        """
        Create a new TickConsolidator for the desired resolution
        
        :param resolution: The resolution desired
        :returns: A consolidator that produces data on the resolution interval.
        """
        ...


class Calendar(System.Object):
    """Helper class that provides Func{DateTime,CalendarInfo} used to define consolidation calendar"""

    Weekly: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]
    """Computes the start of week (previous Monday) of given date/time"""

    Monthly: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]
    """Computes the start of month (1st of the current month) of given date/time"""

    Quarterly: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]
    """Computes the start of quarter (1st of the starting month of current quarter) of given date/time"""

    Yearly: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]
    """Computes the start of year (1st of the current year) of given date/time"""


class QuoteBarConsolidator(QuantConnect.Data.Consolidators.PeriodCountConsolidatorBase[QuantConnect.Data.Market.QuoteBar, QuantConnect.Data.Market.QuoteBar]):
    """Consolidates QuoteBars into larger QuoteBars"""

    @overload
    def __init__(self, period: datetime.timedelta) -> None:
        """
        Initializes a new instance of the TickQuoteBarConsolidator class
        
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, maxCount: int) -> None:
        """
        Initializes a new instance of the TickQuoteBarConsolidator class
        
        :param maxCount: The number of pieces to accept before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, maxCount: int, period: datetime.timedelta) -> None:
        """
        Initializes a new instance of the TickQuoteBarConsolidator class
        
        :param maxCount: The number of pieces to accept before emitting a consolidated bar
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, func: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]) -> None:
        """
        Creates a consolidator to produce a new 'QuoteBar' representing the last count pieces of data or the period, whichever comes first
        
        :param func: Func that defines the start time of a consolidated data
        """
        ...

    @overload
    def __init__(self, pyfuncobj: typing.Any) -> None:
        """
        Creates a consolidator to produce a new 'QuoteBar' representing the last count pieces of data or the period, whichever comes first
        
        :param pyfuncobj: Python function object that defines the start time of a consolidated data
        """
        ...

    def AggregateBar(self, workingBar: QuantConnect.Data.Market.QuoteBar, data: QuantConnect.Data.Market.QuoteBar) -> None:
        """
        Aggregates the new 'data' into the 'workingBar'. The 'workingBar' will be
        null following the event firing
        
        This method is protected.
        
        :param workingBar: The bar we're building, null if the event was just fired and we're starting a new consolidated bar
        :param data: The new data
        """
        ...


class TickQuoteBarConsolidator(QuantConnect.Data.Consolidators.PeriodCountConsolidatorBase[QuantConnect.Data.Market.Tick, QuantConnect.Data.Market.QuoteBar]):
    """Consolidates ticks into quote bars. This consolidator ignores trade ticks"""

    @overload
    def __init__(self, period: datetime.timedelta) -> None:
        """
        Initializes a new instance of the TickQuoteBarConsolidator class
        
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, maxCount: int) -> None:
        """
        Initializes a new instance of the TickQuoteBarConsolidator class
        
        :param maxCount: The number of pieces to accept before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, maxCount: int, period: datetime.timedelta) -> None:
        """
        Initializes a new instance of the TickQuoteBarConsolidator class
        
        :param maxCount: The number of pieces to accept before emitting a consolidated bar
        :param period: The minimum span of time before emitting a consolidated bar
        """
        ...

    @overload
    def __init__(self, func: typing.Callable[[datetime.datetime], QuantConnect.Data.Consolidators.CalendarInfo]) -> None:
        """
        Initializes a new instance of the TickQuoteBarConsolidator class
        
        :param func: Func that defines the start time of a consolidated data
        """
        ...

    @overload
    def __init__(self, pyfuncobj: typing.Any) -> None:
        """
        Initializes a new instance of the TickQuoteBarConsolidator class
        
        :param pyfuncobj: Python function object that defines the start time of a consolidated data
        """
        ...

    def AggregateBar(self, workingBar: QuantConnect.Data.Market.QuoteBar, data: QuantConnect.Data.Market.Tick) -> None:
        """
        Aggregates the new 'data' into the 'workingBar'. The 'workingBar' will be
        null following the event firing
        
        This method is protected.
        
        :param workingBar: The bar we're building, null if the event was just fired and we're starting a new consolidated bar
        :param data: The new data
        """
        ...

    def ShouldProcess(self, data: QuantConnect.Data.Market.Tick) -> bool:
        """
        Determines whether or not the specified data should be processed
        
        This method is protected.
        
        :param data: The data to check
        :returns: True if the consolidator should process this data, false otherwise.
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Data_Consolidators__EventContainer_Callable, QuantConnect_Data_Consolidators__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Data_Consolidators__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Data_Consolidators__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Data_Consolidators__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


