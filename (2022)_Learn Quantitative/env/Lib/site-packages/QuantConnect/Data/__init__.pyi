from typing import overload
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Consolidators
import QuantConnect.Data.Market
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import QuantConnect.Packets
import QuantConnect.Python
import QuantConnect.Securities
import System
import System.Collections
import System.Collections.Concurrent
import System.Collections.Generic
import System.IO
import System.Reflection

IDynamicMetaObjectProvider = typing.Any
QuantConnect_Data_SubscriptionDataSource = typing.Any
QuantConnect_Data_SubscriptionDataConfig = typing.Any
DynamicMetaObject = typing.Any

QuantConnect_Data_Slice_Get_T = typing.TypeVar("QuantConnect_Data_Slice_Get_T")
QuantConnect_Data_SliceExtensions_Get_T = typing.TypeVar("QuantConnect_Data_SliceExtensions_Get_T")
QuantConnect_Data__EventContainer_Callable = typing.TypeVar("QuantConnect_Data__EventContainer_Callable")
QuantConnect_Data__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Data__EventContainer_ReturnType")


class SubscriptionDataConfig(System.Object, System.IEquatable[QuantConnect_Data_SubscriptionDataConfig]):
    """Subscription data required including the type of data."""

    class NewSymbolEventArgs(System.EventArgs):
        """This class has no documentation."""

        @property
        def Old(self) -> QuantConnect.Symbol:
            """The old symbol instance"""
            ...

        @property
        def New(self) -> QuantConnect.Symbol:
            """The new symbol instance"""
            ...

        def __init__(self, new: typing.Union[QuantConnect.Symbol, str], old: typing.Union[QuantConnect.Symbol, str]) -> None:
            ...

    @property
    def NewSymbol(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.SubscriptionDataConfig.NewSymbolEventArgs], None], None]:
        """Event fired when there is a new symbol due to mapping"""
        ...

    @NewSymbol.setter
    def NewSymbol(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.SubscriptionDataConfig.NewSymbolEventArgs], None], None]):
        """Event fired when there is a new symbol due to mapping"""
        ...

    @property
    def Type(self) -> typing.Type:
        """Type of data"""
        ...

    @property
    def SecurityType(self) -> int:
        """
        Security type of this data subscription
        
        This property contains the int value of a member of the QuantConnect.SecurityType enum.
        """
        ...

    @property
    def Symbol(self) -> QuantConnect.Symbol:
        """Symbol of the asset we're requesting: this is really a perm tick!!"""
        ...

    @Symbol.setter
    def Symbol(self, value: QuantConnect.Symbol):
        """Symbol of the asset we're requesting: this is really a perm tick!!"""
        ...

    @property
    def TickType(self) -> int:
        """
        Trade, quote or open interest data
        
        This property contains the int value of a member of the QuantConnect.TickType enum.
        """
        ...

    @property
    def Resolution(self) -> int:
        """
        Resolution of the asset we're requesting, second minute or tick
        
        This property contains the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    @property
    def Increment(self) -> datetime.timedelta:
        """Timespan increment between triggers of this data:"""
        ...

    @property
    def FillDataForward(self) -> bool:
        """True if wish to send old data when time gaps in data feed."""
        ...

    @property
    def ExtendedMarketHours(self) -> bool:
        """Boolean Send Data from between 4am - 8am (Equities Setting Only)"""
        ...

    @property
    def IsInternalFeed(self) -> bool:
        """True if this subscription was added for the sole purpose of providing currency conversion rates via CashBook.EnsureCurrencyDataFeeds"""
        ...

    @property
    def IsCustomData(self) -> bool:
        """True if this subscription is for custom user data, false for QC data"""
        ...

    @property
    def SumOfDividends(self) -> float:
        """The sum of dividends accrued in this subscription, used for scaling total return prices"""
        ...

    @SumOfDividends.setter
    def SumOfDividends(self, value: float):
        """The sum of dividends accrued in this subscription, used for scaling total return prices"""
        ...

    @property
    def DataNormalizationMode(self) -> int:
        """
        Gets the normalization mode used for this subscription
        
        This property contains the int value of a member of the QuantConnect.DataNormalizationMode enum.
        """
        ...

    @DataNormalizationMode.setter
    def DataNormalizationMode(self, value: int):
        """
        Gets the normalization mode used for this subscription
        
        This property contains the int value of a member of the QuantConnect.DataNormalizationMode enum.
        """
        ...

    @property
    def DataMappingMode(self) -> int:
        """
        Gets the securities mapping mode used for this subscription
        
        This property contains the int value of a member of the QuantConnect.DataMappingMode enum.
        """
        ...

    @property
    def ContractDepthOffset(self) -> int:
        """
        The continuous contract desired offset from the current front month.
        For example, 0 (default) will use the front month, 1 will use the back month contract
        """
        ...

    @property
    def PriceScaleFactor(self) -> float:
        """Price Scaling Factor:"""
        ...

    @PriceScaleFactor.setter
    def PriceScaleFactor(self, value: float):
        """Price Scaling Factor:"""
        ...

    @property
    def MappedSymbol(self) -> str:
        """Symbol Mapping: When symbols change over time (e.g. CHASE-> JPM) need to update the symbol requested."""
        ...

    @MappedSymbol.setter
    def MappedSymbol(self, value: str):
        """Symbol Mapping: When symbols change over time (e.g. CHASE-> JPM) need to update the symbol requested."""
        ...

    @property
    def Market(self) -> str:
        """Gets the market / scope of the symbol"""
        ...

    @property
    def DataTimeZone(self) -> typing.Any:
        """Gets the data time zone for this subscription"""
        ...

    @property
    def ExchangeTimeZone(self) -> typing.Any:
        """Gets the exchange time zone for this subscription"""
        ...

    @property
    def Consolidators(self) -> System.Collections.Generic.ISet[QuantConnect.Data.Consolidators.IDataConsolidator]:
        """Consolidators that are registred with this subscription"""
        ...

    @property
    def IsFilteredSubscription(self) -> bool:
        """Gets whether or not this subscription should have filters applied to it (market hours/user filters from security)"""
        ...

    @overload
    def __init__(self, objectType: typing.Type, symbol: typing.Union[QuantConnect.Symbol, str], resolution: QuantConnect.Resolution, dataTimeZone: typing.Any, exchangeTimeZone: typing.Any, fillForward: bool, extendedHours: bool, isInternalFeed: bool, isCustom: bool = False, tickType: typing.Optional[QuantConnect.TickType] = None, isFilteredSubscription: bool = True, dataNormalizationMode: QuantConnect.DataNormalizationMode = ..., dataMappingMode: QuantConnect.DataMappingMode = ..., contractDepthOffset: int = 0, mappedConfig: bool = False) -> None:
        """
        Constructor for Data Subscriptions
        
        :param objectType: Type of the data objects.
        :param symbol: Symbol of the asset we're requesting
        :param resolution: Resolution of the asset we're requesting
        :param dataTimeZone: The time zone the raw data is time stamped in
        :param exchangeTimeZone: Specifies the time zone of the exchange for the security this subscription is for. This is this output time zone, that is, the time zone that will be used on BaseData instances
        :param fillForward: Fill in gaps with historical data
        :param extendedHours: Equities only - send in data from 4am - 8pm
        :param isInternalFeed: Set to true if this subscription is added for the sole purpose of providing currency conversion rates, setting this flag to true will prevent the data from being sent into the algorithm's OnData methods
        :param isCustom: True if this is user supplied custom data, false for normal QC data
        :param tickType: Specifies if trade or quote data is subscribed
        :param isFilteredSubscription: True if this subscription should have filters applied to it (market hours/user filters from security), false otherwise
        :param dataNormalizationMode: Specifies normalization mode used for this subscription
        :param dataMappingMode: The contract mapping mode to use for the security
        :param contractDepthOffset: The continuous contract desired offset from the current front month. For example, 0 (default) will use the front month, 1 will use the back month contract
        """
        ...

    @overload
    def __init__(self, config: QuantConnect.Data.SubscriptionDataConfig, objectType: typing.Type = None, symbol: typing.Union[QuantConnect.Symbol, str] = None, resolution: typing.Optional[QuantConnect.Resolution] = None, dataTimeZone: typing.Any = None, exchangeTimeZone: typing.Any = None, fillForward: typing.Optional[bool] = None, extendedHours: typing.Optional[bool] = None, isInternalFeed: typing.Optional[bool] = None, isCustom: typing.Optional[bool] = None, tickType: typing.Optional[QuantConnect.TickType] = None, isFilteredSubscription: typing.Optional[bool] = None, dataNormalizationMode: typing.Optional[QuantConnect.DataNormalizationMode] = None, dataMappingMode: typing.Optional[QuantConnect.DataMappingMode] = None, contractDepthOffset: typing.Optional[int] = None, mappedConfig: typing.Optional[bool] = None) -> None:
        """
        Copy constructor with overrides
        
        :param config: The config to copy, then overrides are applied and all option
        :param objectType: Type of the data objects.
        :param symbol: Symbol of the asset we're requesting
        :param resolution: Resolution of the asset we're requesting
        :param dataTimeZone: The time zone the raw data is time stamped in
        :param exchangeTimeZone: Specifies the time zone of the exchange for the security this subscription is for. This is this output time zone, that is, the time zone that will be used on BaseData instances
        :param fillForward: Fill in gaps with historical data
        :param extendedHours: Equities only - send in data from 4am - 8pm
        :param isInternalFeed: Set to true if this subscription is added for the sole purpose of providing currency conversion rates, setting this flag to true will prevent the data from being sent into the algorithm's OnData methods
        :param isCustom: True if this is user supplied custom data, false for normal QC data
        :param tickType: Specifies if trade or quote data is subscribed
        :param isFilteredSubscription: True if this subscription should have filters applied to it (market hours/user filters from security), false otherwise
        :param dataNormalizationMode: Specifies normalization mode used for this subscription
        :param dataMappingMode: The contract mapping mode to use for the security
        :param contractDepthOffset: The continuous contract desired offset from the current front month. For example, 0 (default) will use the front month, 1 will use the back month contract
        :param mappedConfig: True if this is created as a mapped config. This is useful for continuous contract at live trading where we subscribe to the mapped symbol but want to preserve uniqueness
        """
        ...

    @overload
    def Equals(self, other: QuantConnect.Data.SubscriptionDataConfig) -> bool:
        """
        Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the  parameter; otherwise, false.
        """
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified object is equal to the current object.
        
        :param obj: The object to compare with the current object.
        :returns: true if the specified object  is equal to the current object; otherwise, false.
        """
        ...

    def GetHashCode(self) -> int:
        """
        Serves as the default hash function.
        
        :returns: A hash code for the current object.
        """
        ...

    def ToString(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class IBaseData(metaclass=abc.ABCMeta):
    """Base Data Class: Type, Timestamp, Key -- Base Features."""

    @property
    @abc.abstractmethod
    def DataType(self) -> int:
        """
        Market Data Type of this data - does it come in individual price packets or is it grouped into OHLC.
        
        This property contains the int value of a member of the QuantConnect.MarketDataType enum.
        """
        ...

    @DataType.setter
    @abc.abstractmethod
    def DataType(self, value: int):
        """
        Market Data Type of this data - does it come in individual price packets or is it grouped into OHLC.
        
        This property contains the int value of a member of the QuantConnect.MarketDataType enum.
        """
        ...

    @property
    @abc.abstractmethod
    def Time(self) -> datetime.datetime:
        """Time keeper of data -- all data is timeseries based."""
        ...

    @Time.setter
    @abc.abstractmethod
    def Time(self, value: datetime.datetime):
        """Time keeper of data -- all data is timeseries based."""
        ...

    @property
    @abc.abstractmethod
    def EndTime(self) -> datetime.datetime:
        """End time of data"""
        ...

    @EndTime.setter
    @abc.abstractmethod
    def EndTime(self, value: datetime.datetime):
        """End time of data"""
        ...

    @property
    @abc.abstractmethod
    def Symbol(self) -> QuantConnect.Symbol:
        """Symbol for underlying Security"""
        ...

    @Symbol.setter
    @abc.abstractmethod
    def Symbol(self, value: QuantConnect.Symbol):
        """Symbol for underlying Security"""
        ...

    @property
    @abc.abstractmethod
    def Value(self) -> float:
        """All timeseries data is a time-value pair:"""
        ...

    @Value.setter
    @abc.abstractmethod
    def Value(self, value: float):
        """All timeseries data is a time-value pair:"""
        ...

    @property
    @abc.abstractmethod
    def Price(self) -> float:
        """Alias of Value."""
        ...

    def Clone(self) -> QuantConnect.Data.BaseData:
        """Return a new instance clone of this object"""
        ...

    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], datafeed: QuantConnect.DataFeedEndpoint) -> str:
        """
        Return the URL string source of the file. This will be converted to a stream
        
        :param config: Configuration object
        :param date: Date of this source file
        :param datafeed: Type of datafeed we're reqesting - backtest or live
        :returns: String URL of source file.
        """
        ...

    @overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects. Each data type creates its own factory method, and returns a new instance of the object
        each time it is called. The returned object is assumed to be time stamped in the config.ExchangeTimeZone.
        
        :param config: Subscription data config setup object
        :param line: Line of the source document
        :param date: Date of the requested data
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: Instance of the T:BaseData object generated by this line of the CSV.
        """
        ...

    @overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, stream: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects. Each data type creates its own factory method, and returns a new instance of the object
        each time it is called. The returned object is assumed to be time stamped in the config.ExchangeTimeZone.
        
        :param config: Subscription data config setup object
        :param stream: The data stream
        :param date: Date of the requested data
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: Instance of the T:BaseData object generated by this line of the CSV.
        """
        ...

    @overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], dataFeed: QuantConnect.DataFeedEndpoint) -> QuantConnect.Data.BaseData:
        """
        Reader Method :: using set of arguements we specify read out type. Enumerate
        until the end of the data stream or file. E.g. Read CSV file line by line and convert
        into data types.
        
        Reader(SubscriptionDataConfig, string, DateTime, DataFeedEndpoint) method has been made obsolete, use Reader(SubscriptionDataConfig, string, DateTime, bool) instead.
        
        :returns: BaseData type set by Subscription Method.
        """
        ...

    def RequiresMapping(self) -> bool:
        """
        Indicates if there is support for mapping
        
        :returns: True indicates mapping should be used.
        """
        ...


class FileFormat(System.Enum):
    """Specifies the format of data in a subscription"""

    Csv = 0
    """Comma separated values (0)"""

    Binary = 1
    """Binary file data (1)"""

    ZipEntryName = 2
    """Only the zip entry names are read in as symbols (2)"""

    UnfoldingCollection = 3
    """Reader returns a BaseDataCollection object (3)"""

    Index = 4
    """Data stored using an intermediate index source (4)"""

    FoldingCollection = 5
    """
    Data type inherits from BaseDataCollection.
    Reader method can return a non BaseDataCollection type which will be folded, based on unique time,
    into an instance of the data type (5)
    """


class SubscriptionDataSource(System.Object, System.IEquatable[QuantConnect_Data_SubscriptionDataSource]):
    """Represents the source location and transport medium for a subscription"""

    @property
    def Source(self) -> str:
        """Identifies where to get the subscription's data from"""
        ...

    @property
    def Format(self) -> QuantConnect.Data.FileFormat:
        """Identifies the format of the data within the source"""
        ...

    @property
    def TransportMedium(self) -> QuantConnect.SubscriptionTransportMedium:
        """Identifies the transport medium used to access the data, such as a local or remote file, or a polling rest API"""
        ...

    @property
    def Headers(self) -> System.Collections.Generic.IReadOnlyList[System.Collections.Generic.KeyValuePair[str, str]]:
        """Gets the header values to be used in the web request."""
        ...

    @overload
    def __init__(self, source: str, transportMedium: QuantConnect.SubscriptionTransportMedium) -> None:
        """
        Initializes a new instance of the SubscriptionDataSource class.
        
        :param source: The subscription's data source location
        :param transportMedium: The transport medium to be used to retrieve the subscription's data from the source
        """
        ...

    @overload
    def __init__(self, source: str, transportMedium: QuantConnect.SubscriptionTransportMedium, format: QuantConnect.Data.FileFormat) -> None:
        """
        Initializes a new instance of the SubscriptionDataSource class.
        
        :param source: The subscription's data source location
        :param transportMedium: The transport medium to be used to retrieve the subscription's data from the source
        :param format: The format of the data within the source
        """
        ...

    @overload
    def __init__(self, source: str, transportMedium: QuantConnect.SubscriptionTransportMedium, format: QuantConnect.Data.FileFormat, headers: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[str, str]]) -> None:
        """
        Initializes a new instance of the SubscriptionDataSource class with SubscriptionTransportMedium.Rest
        including the specified header values
        
        :param source: The subscription's data source location
        :param transportMedium: The transport medium to be used to retrieve the subscription's data from the source
        :param format: The format of the data within the source
        :param headers: The headers to be used for this source
        """
        ...

    @overload
    def Equals(self, other: QuantConnect.Data.SubscriptionDataSource) -> bool:
        """
        Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the  parameter; otherwise, false.
        """
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified instance is equal to the current instance.
        
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

    def ToString(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class BaseData(System.Object, QuantConnect.Data.IBaseData, metaclass=abc.ABCMeta):
    """
    Abstract base data class of QuantConnect. It is intended to be extended to define
    generic user customizable data types while at the same time implementing the basics of data where possible
    """

    AllResolutions: System.Collections.Generic.List[QuantConnect.Resolution] = ...
    """
    A list of all Resolution
    
    This field is protected.
    """

    DailyResolution: System.Collections.Generic.List[QuantConnect.Resolution] = ...
    """
    A list of Resolution.Daily
    
    This field is protected.
    """

    MinuteResolution: System.Collections.Generic.List[QuantConnect.Resolution] = ...
    """
    A list of Resolution.Minute
    
    This field is protected.
    """

    HighResolution: System.Collections.Generic.List[QuantConnect.Resolution] = ...
    """
    A list of high Resolution, including minute, second, and tick.
    
    This field is protected.
    """

    OptionResolutions: System.Collections.Generic.List[QuantConnect.Resolution] = ...
    """
    A list of resolutions support by Options
    
    This field is protected.
    """

    @property
    def DataType(self) -> int:
        """
        Market Data Type of this data - does it come in individual price packets or is it grouped into OHLC.
        
        This property contains the int value of a member of the QuantConnect.MarketDataType enum.
        """
        ...

    @DataType.setter
    def DataType(self, value: int):
        """
        Market Data Type of this data - does it come in individual price packets or is it grouped into OHLC.
        
        This property contains the int value of a member of the QuantConnect.MarketDataType enum.
        """
        ...

    @property
    def IsFillForward(self) -> bool:
        """True if this is a fill forward piece of data"""
        ...

    @IsFillForward.setter
    def IsFillForward(self, value: bool):
        """True if this is a fill forward piece of data"""
        ...

    @property
    def Time(self) -> datetime.datetime:
        """Current time marker of this data packet."""
        ...

    @Time.setter
    def Time(self, value: datetime.datetime):
        """Current time marker of this data packet."""
        ...

    @property
    def EndTime(self) -> datetime.datetime:
        """
        The end time of this data. Some data covers spans (trade bars) and as such we want
        to know the entire time span covered
        """
        ...

    @EndTime.setter
    def EndTime(self, value: datetime.datetime):
        """
        The end time of this data. Some data covers spans (trade bars) and as such we want
        to know the entire time span covered
        """
        ...

    @property
    def Symbol(self) -> QuantConnect.Symbol:
        """Symbol representation for underlying Security"""
        ...

    @Symbol.setter
    def Symbol(self, value: QuantConnect.Symbol):
        """Symbol representation for underlying Security"""
        ...

    @property
    def Value(self) -> float:
        """
        Value representation of this data packet. All data requires a representative value for this moment in time.
        For streams of data this is the price now, for OHLC packets this is the closing price.
        """
        ...

    @Value.setter
    def Value(self, value: float):
        """
        Value representation of this data packet. All data requires a representative value for this moment in time.
        For streams of data this is the price now, for OHLC packets this is the closing price.
        """
        ...

    @property
    def Price(self) -> float:
        """As this is a backtesting platform we'll provide an alias of value as price."""
        ...

    def __init__(self) -> None:
        """Constructor for initialising the dase data class"""
        ...

    @overload
    def Clone(self, fillForward: bool) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :param fillForward: True if this is a fill forward clone
        :returns: A clone of the current object.
        """
        ...

    @overload
    def Clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :returns: A clone of the current object.
        """
        ...

    def DataTimeZone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The DateTimeZone of this data type.
        """
        ...

    def DefaultResolution(self) -> int:
        """
        Gets the default resolution for this data and security type
        
        :returns: This method returns the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    @staticmethod
    def DeserializeMessage(serialized: str) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]:
        """
        Deserialize the message from the data server
        
        :param serialized: The data server's message
        :returns: An enumerable of base data, if unsuccessful, returns an empty enumerable.
        """
        ...

    @overload
    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the URL string source of the file. This will be converted to a stream
        
        :param config: Configuration object
        :param date: Date of this source file
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: String URL of source file.
        """
        ...

    @overload
    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], datafeed: QuantConnect.DataFeedEndpoint) -> str:
        """
        Return the URL string source of the file. This will be converted to a stream
        
        GetSource(SubscriptionDataConfig, DateTime, DataFeedEndpoint) method has been made obsolete, use GetSource(SubscriptionDataConfig, DateTime, bool) instead.
        
        :param config: Configuration object
        :param date: Date of this source file
        :param datafeed: Type of datafeed we're reqesting - backtest or live
        :returns: String URL of source file.
        """
        ...

    def IsSparseData(self) -> bool:
        """
        Indicates that the data set is expected to be sparse
        
        :returns: True if the data set represented by this type is expected to be sparse.
        """
        ...

    @overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects. Each data type creates its own factory method, and returns a new instance of the object
        each time it is called. The returned object is assumed to be time stamped in the config.ExchangeTimeZone.
        
        :param config: Subscription data config setup object
        :param line: Line of the source document
        :param date: Date of the requested data
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: Instance of the T:BaseData object generated by this line of the CSV.
        """
        ...

    @overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, stream: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects. Each data type creates its own factory method, and returns a new instance of the object
        each time it is called. The returned object is assumed to be time stamped in the config.ExchangeTimeZone.
        
        :param config: Subscription data config setup object
        :param stream: The data stream
        :param date: Date of the requested data
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: Instance of the T:BaseData object generated by this line of the CSV.
        """
        ...

    @overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], datafeed: QuantConnect.DataFeedEndpoint) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects. Each data type creates its own factory method, and returns a new instance of the object
        each time it is called.
        
        Reader(SubscriptionDataConfig, string, DateTime, DataFeedEndpoint) method has been made obsolete, use Reader(SubscriptionDataConfig, string, DateTime, bool) instead.
        
        :param config: Subscription data config setup object
        :param line: Line of the source document
        :param date: Date of the requested data
        :param datafeed: Type of datafeed we're requesting - a live or backtest feed.
        :returns: Instance of the T:BaseData object generated by this line of the CSV.
        """
        ...

    def RequiresMapping(self) -> bool:
        """
        Indicates if there is support for mapping
        
        :returns: True indicates mapping should be used.
        """
        ...

    def SupportedResolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...

    def ToString(self) -> str:
        """
        Formats a string with the symbol and value.
        
        :returns: string - a string formatted as SPY: 167.753.
        """
        ...

    def Update(self, lastTrade: float, bidPrice: float, askPrice: float, volume: float, bidSize: float, askSize: float) -> None:
        """
        Update routine to build a bar/tick from a data update.
        
        :param lastTrade: The last trade price
        :param bidPrice: Current bid price
        :param askPrice: Current asking price
        :param volume: Volume of this trade
        :param bidSize: The size of the current bid, if available
        :param askSize: The size of the current ask, if available
        """
        ...

    def UpdateAsk(self, askPrice: float, askSize: float) -> None:
        """
        Updates this base data with the new quote ask information
        
        :param askPrice: The current ask price
        :param askSize: The current ask size
        """
        ...

    def UpdateBid(self, bidPrice: float, bidSize: float) -> None:
        """
        Updates this base data with the new quote bid information
        
        :param bidPrice: The current bid price
        :param bidSize: The current bid size
        """
        ...

    def UpdateQuote(self, bidPrice: float, bidSize: float, askPrice: float, askSize: float) -> None:
        """
        Updates this base data with new quote information
        
        :param bidPrice: The current bid price
        :param bidSize: The current bid size
        :param askPrice: The current ask price
        :param askSize: The current ask size
        """
        ...

    def UpdateTrade(self, lastTrade: float, tradeSize: float) -> None:
        """
        Updates this base data with a new trade
        
        :param lastTrade: The price of the last trade
        :param tradeSize: The quantity traded
        """
        ...


class DynamicData(QuantConnect.Data.BaseData, IDynamicMetaObjectProvider, metaclass=abc.ABCMeta):
    """Dynamic Data Class: Accept flexible data, adapting to the columns provided by source."""

    def Clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :returns: A clone of the current object.
        """
        ...

    def GetMetaObject(self, parameter: typing.Any) -> typing.Any:
        """Get the metaObject required for Dynamism."""
        ...

    def GetProperty(self, name: str) -> System.Object:
        """
        Gets the property's value with the specified name. This is a case-insensitve search.
        
        :param name: The property name to access
        :returns: object value of BaseData.
        """
        ...

    def GetStorageDictionary(self) -> System.Collections.Generic.IDictionary[str, System.Object]:
        """
        Gets the storage dictionary
        Python algorithms need this information since DynamicMetaObject does not work
        
        :returns: Dictionary that stores the paramenters names and values.
        """
        ...

    def HasProperty(self, name: str) -> bool:
        """
        Gets whether or not this dynamic data instance has a property with the specified name.
        This is a case-insensitve search.
        
        :param name: The property name to check for
        :returns: True if the property exists, false otherwise.
        """
        ...

    def SetProperty(self, name: str, value: typing.Any) -> System.Object:
        """
        Sets the property with the specified name to the value. This is a case-insensitve search.
        
        :param name: The property name to set
        :param value: The new property value
        :returns: Returns the input value back to the caller.
        """
        ...


class Slice(QuantConnect.ExtendedDictionary[typing.Any], typing.Iterable[System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Data.BaseData]]):
    """Provides a data structure for all of an algorithm's data at a single time step"""

    @property
    def Time(self) -> datetime.datetime:
        """Gets the timestamp for this slice of data"""
        ...

    @Time.setter
    def Time(self, value: datetime.datetime):
        """Gets the timestamp for this slice of data"""
        ...

    @property
    def UtcTime(self) -> datetime.datetime:
        """Gets the timestamp for this slice of data in UTC"""
        ...

    @UtcTime.setter
    def UtcTime(self, value: datetime.datetime):
        """Gets the timestamp for this slice of data in UTC"""
        ...

    @property
    def HasData(self) -> bool:
        """Gets whether or not this slice has data"""
        ...

    @HasData.setter
    def HasData(self, value: bool):
        """Gets whether or not this slice has data"""
        ...

    @property
    def Bars(self) -> QuantConnect.Data.Market.TradeBars:
        """Gets the TradeBars for this slice of data"""
        ...

    @property
    def QuoteBars(self) -> QuantConnect.Data.Market.QuoteBars:
        """Gets the QuoteBars for this slice of data"""
        ...

    @property
    def Ticks(self) -> QuantConnect.Data.Market.Ticks:
        """Gets the Ticks for this slice of data"""
        ...

    @property
    def OptionChains(self) -> QuantConnect.Data.Market.OptionChains:
        """Gets the OptionChains for this slice of data"""
        ...

    @property
    def FuturesChains(self) -> QuantConnect.Data.Market.FuturesChains:
        """Gets the FuturesChains for this slice of data"""
        ...

    @property
    def FutureChains(self) -> QuantConnect.Data.Market.FuturesChains:
        """Gets the FuturesChains for this slice of data"""
        ...

    @property
    def Splits(self) -> QuantConnect.Data.Market.Splits:
        """Gets the Splits for this slice of data"""
        ...

    @property
    def Dividends(self) -> QuantConnect.Data.Market.Dividends:
        """Gets the Dividends for this slice of data"""
        ...

    @property
    def Delistings(self) -> QuantConnect.Data.Market.Delistings:
        """Gets the Delistings for this slice of data"""
        ...

    @property
    def SymbolChangedEvents(self) -> QuantConnect.Data.Market.SymbolChangedEvents:
        """Gets the QuantConnect.Data.Market.SymbolChangedEvents for this slice of data"""
        ...

    @property
    def Count(self) -> int:
        """Gets the number of symbols held in this slice"""
        ...

    @property
    def Keys(self) -> System.Collections.Generic.IReadOnlyList[QuantConnect.Symbol]:
        """Gets all the symbols in this slice"""
        ...

    @property
    def GetKeys(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Gets an System.Collections.Generic.ICollection`1 containing the Symbol objects of the System.Collections.Generic.IDictionary`2.
        
        This property is protected.
        """
        ...

    @property
    def GetValues(self) -> System.Collections.Generic.IEnumerable[typing.Any]:
        """
        Gets an System.Collections.Generic.ICollection`1 containing the values in the System.Collections.Generic.IDictionary`2.
        
        This property is protected.
        """
        ...

    @property
    def Values(self) -> System.Collections.Generic.IReadOnlyList[QuantConnect.Data.BaseData]:
        """Gets a list of all the data in this slice"""
        ...

    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> typing.Union[QuantConnect.Data.Market.TradeBar, QuantConnect.Data.Market.QuoteBar, System.Collections.Generic.List[QuantConnect.Data.Market.Tick], typing.Any]:
        """
        Gets the data corresponding to the specified symbol. If the requested data
        is of MarketDataType.Tick, then a List{Tick} will
        be returned, otherwise, it will be the subscribed type, for example, TradeBar
        or event UnlinkedData for custom data.
        
        :param symbol: The data's symbols
        :returns: The data for the specified symbol.
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], data: System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData], utcTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the Slice class, lazily
        instantiating the Slice.Bars and Slice.Ticks
        collections on demand
        
        :param time: The timestamp for this slice of data
        :param data: The raw data in this slice
        :param utcTime: The timestamp for this slice of data in UTC
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], data: System.Collections.Generic.List[QuantConnect.Data.BaseData], utcTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the Slice class, lazily
        instantiating the Slice.Bars and Slice.Ticks
        collections on demand
        
        :param time: The timestamp for this slice of data
        :param data: The raw data in this slice
        :param utcTime: The timestamp for this slice of data in UTC
        """
        ...

    @overload
    def __init__(self, slice: QuantConnect.Data.Slice) -> None:
        """
        Initializes a new instance used by the PythonSlice
        
        This method is protected.
        
        :param slice: slice object to wrap
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], data: System.Collections.Generic.List[QuantConnect.Data.BaseData], tradeBars: QuantConnect.Data.Market.TradeBars, quoteBars: QuantConnect.Data.Market.QuoteBars, ticks: QuantConnect.Data.Market.Ticks, optionChains: QuantConnect.Data.Market.OptionChains, futuresChains: QuantConnect.Data.Market.FuturesChains, splits: QuantConnect.Data.Market.Splits, dividends: QuantConnect.Data.Market.Dividends, delistings: QuantConnect.Data.Market.Delistings, symbolChanges: QuantConnect.Data.Market.SymbolChangedEvents, utcTime: typing.Union[datetime.datetime, datetime.date], hasData: typing.Optional[bool] = None) -> None:
        """
        Initializes a new instance of the Slice class
        
        :param time: The timestamp for this slice of data
        :param data: The raw data in this slice
        :param tradeBars: The trade bars for this slice
        :param quoteBars: The quote bars for this slice
        :param ticks: This ticks for this slice
        :param optionChains: The option chains for this slice
        :param futuresChains: The futures chains for this slice
        :param splits: The splits for this slice
        :param dividends: The dividends for this slice
        :param delistings: The delistings for this slice
        :param symbolChanges: The symbol changed events for this slice
        :param utcTime: The timestamp for this slice of data in UTC
        :param hasData: true if this slice contains data
        """
        ...

    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: typing.Union[QuantConnect.Data.Market.TradeBar, QuantConnect.Data.Market.QuoteBar, System.Collections.Generic.List[QuantConnect.Data.Market.Tick], typing.Any]) -> None:
        """
        Gets the data corresponding to the specified symbol. If the requested data
        is of MarketDataType.Tick, then a List{Tick} will
        be returned, otherwise, it will be the subscribed type, for example, TradeBar
        or event UnlinkedData for custom data.
        
        :param symbol: The data's symbols
        :returns: The data for the specified symbol.
        """
        ...

    def ContainsKey(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Determines whether this instance contains data for the specified symbol
        
        :param symbol: The symbol we seek data for
        :returns: True if this instance contains data for the symbol, false otherwise.
        """
        ...

    @overload
    def Get(self, type: QuantConnect_Data_Slice_Get_T) -> QuantConnect.Data.Market.DataDictionary[QuantConnect_Data_Slice_Get_T]:
        """
        Gets the data of the specified type.
        
        :param type: The type of data we seek
        :returns: The DataDictionary{T} instance for the requested type.
        """
        ...

    @overload
    def Get(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect_Data_Slice_Get_T:
        """
        Gets the data of the specified symbol and type.
        
        :param symbol: The specific symbol was seek
        :returns: The data for the requested symbol.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect.Data.BaseData]]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: A System.Collections.Generic.IEnumerator`1 that can be used to iterate through the collection.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        """
        Returns an enumerator that iterates through a collection.
        
        :returns: An System.Collections.IEnumerator object that can be used to iterate through the collection.
        """
        ...

    @staticmethod
    def GetImpl(type: typing.Type, instance: QuantConnect.Data.Slice) -> typing.Any:
        """
        Gets the data of the specified type.
        
        This method is protected.
        """
        ...

    def MergeSlice(self, inputSlice: QuantConnect.Data.Slice) -> None:
        """
        Merge two slice with same Time
        
        :param inputSlice: slice instance
        """
        ...

    def TryGetValue(self, symbol: typing.Union[QuantConnect.Symbol, str], data: typing.Optional[typing.Any]) -> typing.Union[bool, typing.Any]:
        """
        Gets the data associated with the specified symbol
        
        :param symbol: The symbol we want data for
        :param data: The data for the specifed symbol, or null if no data was found
        :returns: True if data was found, false otherwise.
        """
        ...


class Channel(System.Object):
    """Represents a subscription channel"""

    Single: str = "common"
    """Represents an internal channel name for all brokerage channels in case we don't differentiate them"""

    @property
    def Name(self) -> str:
        """The name of the channel"""
        ...

    @Name.setter
    def Name(self, value: str):
        """The name of the channel"""
        ...

    @property
    def Symbol(self) -> QuantConnect.Symbol:
        """The ticker symbol of the channel"""
        ...

    @Symbol.setter
    def Symbol(self, value: QuantConnect.Symbol):
        """The ticker symbol of the channel"""
        ...

    def __init__(self, channelName: str, symbol: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Creates an instance of subscription channel
        
        :param channelName: Socket channel name
        :param symbol: Associated symbol
        """
        ...

    @overload
    def Equals(self, other: QuantConnect.Data.Channel) -> bool:
        """
        Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the  parameter; otherwise, false.
        """
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified object is equal to the current object.
        
        :param obj: The object to compare with the current object.
        :returns: true if the specified object  is equal to the current object; otherwise, false.
        """
        ...

    def GetHashCode(self) -> int:
        """
        Serves as the default hash function.
        
        :returns: A hash code for the current object.
        """
        ...


class SubscriptionManager(System.Object):
    """Enumerable Subscription Management Class"""

    @property
    def SubscriptionDataConfigService(self) -> QuantConnect.Interfaces.ISubscriptionDataConfigService:
        """Instance that implements ISubscriptionDataConfigService"""
        ...

    @property
    def Subscriptions(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.SubscriptionDataConfig]:
        """Returns an IEnumerable of Subscriptions"""
        ...

    @property
    def AvailableDataTypes(self) -> System.Collections.Generic.Dictionary[QuantConnect.SecurityType, System.Collections.Generic.List[QuantConnect.TickType]]:
        """The different TickType each SecurityType supports"""
        ...

    @property
    def Count(self) -> int:
        """Get the count of assets:"""
        ...

    @overload
    def Add(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: QuantConnect.Resolution, timeZone: typing.Any, exchangeTimeZone: typing.Any, isCustomData: bool = False, fillDataForward: bool = True, extendedMarketHours: bool = False) -> QuantConnect.Data.SubscriptionDataConfig:
        """
        Add Market Data Required (Overloaded method for backwards compatibility).
        
        :param symbol: Symbol of the asset we're like
        :param resolution: Resolution of Asset Required
        :param timeZone: The time zone the subscription's data is time stamped in
        :param exchangeTimeZone: Specifies the time zone of the exchange for the security this subscription is for. This     is this output time zone, that is, the time zone that will be used on BaseData instances
        :param isCustomData: True if this is custom user supplied data, false for normal QC data
        :param fillDataForward: when there is no data pass the last tradebar forward
        :param extendedMarketHours: Request premarket data as well when true
        :returns: The newly created SubscriptionDataConfig or existing instance if it already existed.
        """
        ...

    @overload
    def Add(self, dataType: typing.Type, tickType: QuantConnect.TickType, symbol: typing.Union[QuantConnect.Symbol, str], resolution: QuantConnect.Resolution, dataTimeZone: typing.Any, exchangeTimeZone: typing.Any, isCustomData: bool, fillDataForward: bool = True, extendedMarketHours: bool = False, isInternalFeed: bool = False, isFilteredSubscription: bool = True, dataNormalizationMode: QuantConnect.DataNormalizationMode = ...) -> QuantConnect.Data.SubscriptionDataConfig:
        """
        Add Market Data Required - generic data typing support as long as Type implements BaseData.
        
        :param dataType: Set the type of the data we're subscribing to.
        :param tickType: Tick type for the subscription.
        :param symbol: Symbol of the asset we're like
        :param resolution: Resolution of Asset Required
        :param dataTimeZone: The time zone the subscription's data is time stamped in
        :param exchangeTimeZone: Specifies the time zone of the exchange for the security this subscription is for. This     is this output time zone, that is, the time zone that will be used on BaseData instances
        :param isCustomData: True if this is custom user supplied data, false for normal QC data
        :param fillDataForward: when there is no data pass the last tradebar forward
        :param extendedMarketHours: Request premarket data as well when true
        :param isInternalFeed: Set to true to prevent data from this subscription from being sent into the algorithm's     OnData events
        :param isFilteredSubscription: True if this subscription should have filters applied to it (market hours/user     filters from security), false otherwise
        :param dataNormalizationMode: Define how data is normalized
        :returns: The newly created SubscriptionDataConfig or existing instance if it already existed.
        """
        ...

    @overload
    def AddConsolidator(self, symbol: typing.Union[QuantConnect.Symbol, str], consolidator: typing.Union[QuantConnect.Data.Consolidators.IDataConsolidator, QuantConnect.Python.PythonConsolidator, datetime.timedelta]) -> None:
        """
        Add a consolidator for the symbol
        
        :param symbol: Symbol of the asset to consolidate
        :param consolidator: The consolidator
        """
        ...

    @overload
    def AddConsolidator(self, symbol: typing.Union[QuantConnect.Symbol, str], pyConsolidator: typing.Any) -> None:
        """
        Add a custom python consolidator for the symbol
        
        :param symbol: Symbol of the asset to consolidate
        :param pyConsolidator: The custom python consolidator
        """
        ...

    @staticmethod
    def DefaultDataTypes() -> System.Collections.Generic.Dictionary[QuantConnect.SecurityType, System.Collections.Generic.List[QuantConnect.TickType]]:
        """Hard code the set of default available data feeds"""
        ...

    def GetDataTypesForSecurity(self, securityType: QuantConnect.SecurityType) -> System.Collections.Generic.IReadOnlyList[QuantConnect.TickType]:
        """Get the available data types for a security"""
        ...

    @staticmethod
    def IsSubscriptionValidForConsolidator(subscription: QuantConnect.Data.SubscriptionDataConfig, consolidator: typing.Union[QuantConnect.Data.Consolidators.IDataConsolidator, QuantConnect.Python.PythonConsolidator, datetime.timedelta]) -> bool:
        """
        Checks if the subscription is valid for the consolidator
        
        :param subscription: The subscription configuration
        :param consolidator: The consolidator
        :returns: true if the subscription is valid for the consolidator.
        """
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

    def RemoveConsolidator(self, symbol: typing.Union[QuantConnect.Symbol, str], consolidator: typing.Union[QuantConnect.Data.Consolidators.IDataConsolidator, QuantConnect.Python.PythonConsolidator, datetime.timedelta]) -> None:
        """
        Removes the specified consolidator for the symbol
        
        :param symbol: The symbol the consolidator is receiving data from
        :param consolidator: The consolidator instance to be removed
        """
        ...

    def SetDataManager(self, subscriptionManager: QuantConnect.Interfaces.IAlgorithmSubscriptionManager) -> None:
        """Sets the Subscription Manager"""
        ...


class ISubscriptionEnumeratorFactory(metaclass=abc.ABCMeta):
    """Create an IEnumerator{BaseData}"""

    def CreateEnumerator(self, request: QuantConnect.Data.UniverseSelection.SubscriptionRequest, dataProvider: QuantConnect.Interfaces.IDataProvider) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Creates an enumerator to read the specified request
        
        :param request: The subscription request to be read
        :param dataProvider: Provider used to get data when it is not present on disk
        :returns: An enumerator reading the subscription request.
        """
        ...


class DataMonitor(System.Object, QuantConnect.Interfaces.IDataMonitor):
    """Monitors data requests and reports on missing data"""

    def __init__(self) -> None:
        """Initializes a new instance of the DataMonitor class"""
        ...

    def Dispose(self) -> None:
        ...

    def Exit(self) -> None:
        """Terminates the data monitor generating a final report"""
        ...

    def OnNewDataRequest(self, sender: typing.Any, e: QuantConnect.Interfaces.DataProviderNewDataRequestEventArgs) -> None:
        """Event handler for the IDataProvider.NewDataRequest event"""
        ...

    def StripDataFolder(self, path: str) -> str:
        """This method is protected."""
        ...


class LeanDataWriter(System.Object):
    """Data writer for saving an IEnumerable of BaseData into the LEAN data directory."""

    @overload
    def __init__(self, resolution: QuantConnect.Resolution, symbol: typing.Union[QuantConnect.Symbol, str], dataDirectory: str, tickType: QuantConnect.TickType = ..., dataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider = None, writePolicy: typing.Optional[QuantConnect.WritePolicy] = None) -> None:
        """
        Create a new lean data writer to this base data directory.
        
        :param resolution: Resolution of the desired output data
        :param symbol: Symbol string
        :param dataDirectory: Base data directory
        :param tickType: The tick type
        :param dataCacheProvider: The data cache provider to use
        :param writePolicy: The file write policy to use
        """
        ...

    @overload
    def __init__(self, dataDirectory: str, resolution: QuantConnect.Resolution, securityType: QuantConnect.SecurityType, tickType: QuantConnect.TickType, dataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider = None, writePolicy: typing.Optional[QuantConnect.WritePolicy] = None) -> None:
        """
        Create a new lean data writer to this base data directory.
        
        :param dataDirectory: Base data directory
        :param resolution: Resolution of the desired output data
        :param securityType: The security type
        :param tickType: The tick type
        :param dataCacheProvider: The data cache provider to use
        :param writePolicy: The file write policy to use
        """
        ...

    def DownloadAndSave(self, brokerage: QuantConnect.Interfaces.IBrokerage, symbols: System.Collections.Generic.List[QuantConnect.Symbol], startTimeUtc: typing.Union[datetime.datetime, datetime.date], endTimeUtc: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Downloads historical data from the brokerage and saves it in LEAN format.
        
        :param brokerage: The brokerage from where to fetch the data
        :param symbols: The list of symbols
        :param startTimeUtc: The starting date/time (UTC)
        :param endTimeUtc: The ending date/time (UTC)
        """
        ...

    def Write(self, source: System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData]) -> None:
        """
        Given the constructor parameters, write out the data in LEAN format.
        
        :param source: IEnumerable source of the data: sorted from oldest to newest.
        """
        ...


class SubscriptionDataConfigList(System.Collections.Generic.List[QuantConnect.Data.SubscriptionDataConfig]):
    """Provides convenient methods for holding several SubscriptionDataConfig"""

    @property
    def Symbol(self) -> QuantConnect.Symbol:
        """Symbol for which this class holds SubscriptionDataConfig"""
        ...

    @Symbol.setter
    def Symbol(self, value: QuantConnect.Symbol):
        """Symbol for which this class holds SubscriptionDataConfig"""
        ...

    @property
    def IsInternalFeed(self) -> bool:
        """Assume that the InternalDataFeed is the same for both SubscriptionDataConfig"""
        ...

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> None:
        """Default constructor that specifies the Symbol that the SubscriptionDataConfig represent"""
        ...

    def SetDataNormalizationMode(self, normalizationMode: QuantConnect.DataNormalizationMode) -> None:
        """Sets the DataNormalizationMode for all SubscriptionDataConfig contained in the list"""
        ...


class GetSetPropertyDynamicMetaObject(DynamicMetaObject):
    """
    Provides an implementation of DynamicMetaObject that uses get/set methods to update
    values in the dynamic object.
    """

    def __init__(self, expression: typing.Any, value: typing.Any, setPropertyMethodInfo: System.Reflection.MethodInfo, getPropertyMethodInfo: System.Reflection.MethodInfo) -> None:
        """
        Initializes a new instance of the QuantConnect.Data.GetSetPropertyDynamicMetaObject class.
        
        :param expression: The expression representing this System.Dynamic.DynamicMetaObject
        :param value: The value represented by the System.Dynamic.DynamicMetaObject
        :param setPropertyMethodInfo: The set method to use for updating this dynamic object
        :param getPropertyMethodInfo: The get method to use for updating this dynamic object
        """
        ...

    def BindGetMember(self, binder: typing.Any) -> typing.Any:
        """
        Performs the binding of the dynamic get member operation.
        
        :param binder: An instance of the System.Dynamic.GetMemberBinder that represents the details of the dynamic operation.
        :returns: The new System.Dynamic.DynamicMetaObject representing the result of the binding.
        """
        ...

    def BindSetMember(self, binder: typing.Any, value: typing.Any) -> typing.Any:
        """
        Performs the binding of the dynamic set member operation.
        
        :param binder: An instance of the System.Dynamic.SetMemberBinder that represents the details of the dynamic operation.
        :param value: The System.Dynamic.DynamicMetaObject representing the value for the set member operation.
        :returns: The new System.Dynamic.DynamicMetaObject representing the result of the binding.
        """
        ...


class BaseDataRequest(System.Object, metaclass=abc.ABCMeta):
    """Abstract sharing logic for data requests"""

    @property
    def StartTimeUtc(self) -> datetime.datetime:
        """Gets the beginning of the requested time interval in UTC"""
        ...

    @StartTimeUtc.setter
    def StartTimeUtc(self, value: datetime.datetime):
        """Gets the beginning of the requested time interval in UTC"""
        ...

    @property
    def EndTimeUtc(self) -> datetime.datetime:
        """Gets the end of the requested time interval in UTC"""
        ...

    @EndTimeUtc.setter
    def EndTimeUtc(self, value: datetime.datetime):
        """Gets the end of the requested time interval in UTC"""
        ...

    @property
    def StartTimeLocal(self) -> datetime.datetime:
        """Gets the StartTimeUtc in the security's exchange time zone"""
        ...

    @property
    def EndTimeLocal(self) -> datetime.datetime:
        """Gets the EndTimeUtc in the security's exchange time zone"""
        ...

    @property
    def ExchangeHours(self) -> QuantConnect.Securities.SecurityExchangeHours:
        """Gets the exchange hours used for processing fill forward requests"""
        ...

    @property
    @abc.abstractmethod
    def TradableDays(self) -> System.Collections.Generic.IEnumerable[datetime.datetime]:
        """Gets the tradable days specified by this request, in the security's data time zone"""
        ...

    def __init__(self, startTimeUtc: typing.Union[datetime.datetime, datetime.date], endTimeUtc: typing.Union[datetime.datetime, datetime.date], exchangeHours: QuantConnect.Securities.SecurityExchangeHours, tickType: QuantConnect.TickType) -> None:
        """
        Initializes the base data request
        
        This method is protected.
        
        :param startTimeUtc: The start time for this request,
        :param endTimeUtc: The start time for this request
        :param exchangeHours: The exchange hours for this request
        :param tickType: The tick type of this request
        """
        ...


class SliceExtensions(System.Object):
    """Provides extension methods to slice enumerables"""

    @staticmethod
    @overload
    def Get(slices: System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice], symbol: typing.Union[QuantConnect.Symbol, str]) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.TradeBar]:
        """
        Gets an enumerable of TradeBar for the given symbol. This method does not verify
        that the specified symbol points to a TradeBar
        
        :param slices: The enumerable of slice
        :param symbol: The symbol to retrieve
        :returns: An enumerable of TradeBar for the matching symbol, of no TradeBar found for symbol, empty enumerable is returned.
        """
        ...

    @staticmethod
    @overload
    def Get(dataDictionaries: System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.DataDictionary[QuantConnect_Data_SliceExtensions_Get_T]], symbol: typing.Union[QuantConnect.Symbol, str]) -> System.Collections.Generic.IEnumerable[QuantConnect_Data_SliceExtensions_Get_T]:
        """
        Gets an enumerable of T for the given symbol. This method does not vify
        that the specified symbol points to a T
        
        :param dataDictionaries: The data dictionary enumerable to access
        :param symbol: The symbol to retrieve
        :returns: An enumerable of T for the matching symbol, if no T is found for symbol, empty enumerable is returned.
        """
        ...

    @staticmethod
    @overload
    def Get(dataDictionaries: System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.DataDictionary[QuantConnect_Data_SliceExtensions_Get_T]], symbol: typing.Union[QuantConnect.Symbol, str], field: str) -> System.Collections.Generic.IEnumerable[float]:
        """
        Gets an enumerable of decimals by accessing the specified field on data for the symbol
        
        :param dataDictionaries: An enumerable of data dictionaries
        :param symbol: The symbol to retrieve
        :param field: The field to access
        :returns: An enumerable of decimals.
        """
        ...

    @staticmethod
    @overload
    def Get(slices: System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice]) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.DataDictionary[QuantConnect_Data_SliceExtensions_Get_T]]:
        """
        Gets the data dictionaries of the requested type in each slice
        
        :param slices: The enumerable of slice
        :returns: An enumerable of data dictionary of the requested type.
        """
        ...

    @staticmethod
    @overload
    def Get(slices: System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice], symbol: typing.Union[QuantConnect.Symbol, str]) -> System.Collections.Generic.IEnumerable[QuantConnect_Data_SliceExtensions_Get_T]:
        """
        Gets an enumerable of T by accessing the slices for the requested symbol
        
        :param slices: The enumerable of slice
        :param symbol: The symbol to retrieve
        :returns: An enumerable of T by accessing each slice for the requested symbol.
        """
        ...

    @staticmethod
    @overload
    def Get(slices: System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice], symbol: typing.Union[QuantConnect.Symbol, str], field: typing.Callable[[QuantConnect.Data.BaseData], float]) -> System.Collections.Generic.IEnumerable[float]:
        """
        Gets an enumerable of decimal by accessing the slice for the symbol and then retrieving the specified
        field on each piece of data
        
        :param slices: The enumerable of slice
        :param symbol: The symbol to retrieve
        :param field: The field selector used to access the dats
        :returns: An enumerable of decimal.
        """
        ...

    @staticmethod
    def PushThrough(slices: System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice], handler: typing.Callable[[QuantConnect.Data.BaseData], None]) -> None:
        """
        Loops through the specified slices and pushes the data into the consolidators. This can be used to
        easily warm up indicators from a history call that returns slice objects.
        
        :param slices: The data to send into the consolidators, likely result of a history request
        :param handler: Delegate handles each data piece from the slice
        """
        ...

    @staticmethod
    @overload
    def PushThroughConsolidators(slices: System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice], consolidatorsBySymbol: System.Collections.Generic.Dictionary[QuantConnect.Symbol, QuantConnect.Data.Consolidators.IDataConsolidator]) -> None:
        """
        Loops through the specified slices and pushes the data into the consolidators. This can be used to
        easily warm up indicators from a history call that returns slice objects.
        
        :param slices: The data to send into the consolidators, likely result of a history request
        :param consolidatorsBySymbol: Dictionary of consolidators keyed by symbol
        """
        ...

    @staticmethod
    @overload
    def PushThroughConsolidators(slices: System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice], consolidatorsProvider: typing.Callable[[QuantConnect.Symbol], QuantConnect.Data.Consolidators.IDataConsolidator]) -> None:
        """
        Loops through the specified slices and pushes the data into the consolidators. This can be used to
        easily warm up indicators from a history call that returns slice objects.
        
        :param slices: The data to send into the consolidators, likely result of a history request
        :param consolidatorsProvider: Delegate that fetches the consolidators by a symbol
        """
        ...

    @staticmethod
    def Ticks(slices: System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice]) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.Ticks]:
        """
        Selects into the slice and returns the Ticks that have data in order
        
        :param slices: The enumerable of slice
        :returns: An enumerable of Ticks.
        """
        ...

    @staticmethod
    def ToDoubleArray(decimals: System.Collections.Generic.IEnumerable[float]) -> typing.List[float]:
        """
        Converts the specified enumerable of decimals into a double array
        
        :param decimals: The enumerable of decimal
        :returns: Double array representing the enumerable of decimal.
        """
        ...

    @staticmethod
    def TradeBars(slices: System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice]) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.TradeBars]:
        """
        Selects into the slice and returns the TradeBars that have data in order
        
        :param slices: The enumerable of slice
        :returns: An enumerable of TradeBars.
        """
        ...


class DiskDataCacheProvider(System.Object, QuantConnect.Interfaces.IDataCacheProvider):
    """
    Simple data cache provider, writes and reads directly from disk
    Used as default for LeanDataWriter
    """

    @property
    def IsDataEphemeral(self) -> bool:
        """Property indicating the data is temporary in nature and should not be cached."""
        ...

    def Dispose(self) -> None:
        """Dispose for this class"""
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
        Store the data in the cache. Not implemented in this instance of the IDataCacheProvider
        
        :param key: The source of the data, used as a key to retrieve data in the cache
        :param data: The data as a byte array
        """
        ...


class HistoryProviderInitializeParameters(System.Object):
    """Represents the set of parameters for the IHistoryProvider.Initialize method"""

    @property
    def Job(self) -> QuantConnect.Packets.AlgorithmNodePacket:
        """The job"""
        ...

    @property
    def Api(self) -> QuantConnect.Interfaces.IApi:
        """The API instance"""
        ...

    @property
    def DataProvider(self) -> QuantConnect.Interfaces.IDataProvider:
        """The provider used to get data when it is not present on disk"""
        ...

    @property
    def DataCacheProvider(self) -> QuantConnect.Interfaces.IDataCacheProvider:
        """The provider used to cache history data files"""
        ...

    @property
    def MapFileProvider(self) -> QuantConnect.Interfaces.IMapFileProvider:
        """The provider used to get a map file resolver to handle equity mapping"""
        ...

    @property
    def FactorFileProvider(self) -> QuantConnect.Interfaces.IFactorFileProvider:
        """The provider used to get factor files to handle equity price scaling"""
        ...

    @property
    def StatusUpdateAction(self) -> typing.Callable[[int], None]:
        """A function used to send status updates"""
        ...

    @property
    def ParallelHistoryRequestsEnabled(self) -> bool:
        """True if parallel history requests are enabled"""
        ...

    @property
    def DataPermissionManager(self) -> QuantConnect.Interfaces.IDataPermissionManager:
        """The data permission manager"""
        ...

    def __init__(self, job: QuantConnect.Packets.AlgorithmNodePacket, api: QuantConnect.Interfaces.IApi, dataProvider: QuantConnect.Interfaces.IDataProvider, dataCacheProvider: QuantConnect.Interfaces.IDataCacheProvider, mapFileProvider: QuantConnect.Interfaces.IMapFileProvider, factorFileProvider: QuantConnect.Interfaces.IFactorFileProvider, statusUpdateAction: typing.Callable[[int], None], parallelHistoryRequestsEnabled: bool, dataPermissionManager: QuantConnect.Interfaces.IDataPermissionManager) -> None:
        """
        Initializes a new instance of the HistoryProviderInitializeParameters class from the specified parameters
        
        :param job: The job
        :param api: The API instance
        :param dataProvider: Provider used to get data when it is not present on disk
        :param dataCacheProvider: Provider used to cache history data files
        :param mapFileProvider: Provider used to get a map file resolver to handle equity mapping
        :param factorFileProvider: Provider used to get factor files to handle equity price scaling
        :param statusUpdateAction: Function used to send status updates
        :param parallelHistoryRequestsEnabled: True if parallel history requests are enabled
        :param dataPermissionManager: The data permission manager to use
        """
        ...


class IndexedBaseData(QuantConnect.Data.BaseData, metaclass=abc.ABCMeta):
    """
    Abstract indexed base data class of QuantConnect.
    It is intended to be extended to define customizable data types which are stored
    using an intermediate index source
    """

    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Returns the index source for a date
        
        :param config: Configuration object
        :param date: Date of this source file
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: The SubscriptionDataSource instance to use.
        """
        ...

    def GetSourceForAnIndex(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], index: str, isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Returns the source for a given index value
        
        :param config: Configuration object
        :param date: Date of this source file
        :param index: The index value for which we want to fetch the source
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: The SubscriptionDataSource instance to use.
        """
        ...


class HistoryRequest(QuantConnect.Data.BaseDataRequest):
    """Represents a request for historical data"""

    @property
    def Symbol(self) -> QuantConnect.Symbol:
        """Gets the symbol to request data for"""
        ...

    @Symbol.setter
    def Symbol(self, value: QuantConnect.Symbol):
        """Gets the symbol to request data for"""
        ...

    @property
    def Resolution(self) -> int:
        """
        Gets the requested data resolution
        
        This property contains the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    @Resolution.setter
    def Resolution(self, value: int):
        """
        Gets the requested data resolution
        
        This property contains the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    @property
    def FillForwardResolution(self) -> typing.Optional[QuantConnect.Resolution]:
        """
        Gets the requested fill forward resolution, set to null for no fill forward behavior.
        Will always return null when Resolution is set to Tick.
        """
        ...

    @FillForwardResolution.setter
    def FillForwardResolution(self, value: typing.Optional[QuantConnect.Resolution]):
        """
        Gets the requested fill forward resolution, set to null for no fill forward behavior.
        Will always return null when Resolution is set to Tick.
        """
        ...

    @property
    def IncludeExtendedMarketHours(self) -> bool:
        """Gets whether or not to include extended market hours data, set to false for only normal market hours"""
        ...

    @IncludeExtendedMarketHours.setter
    def IncludeExtendedMarketHours(self, value: bool):
        """Gets whether or not to include extended market hours data, set to false for only normal market hours"""
        ...

    @property
    def DataType(self) -> typing.Type:
        """Gets the data type used to process the subscription request, this type must derive from BaseData"""
        ...

    @DataType.setter
    def DataType(self, value: typing.Type):
        """Gets the data type used to process the subscription request, this type must derive from BaseData"""
        ...

    @property
    def DataTimeZone(self) -> typing.Any:
        """Gets the time zone of the time stamps on the raw input data"""
        ...

    @DataTimeZone.setter
    def DataTimeZone(self, value: typing.Any):
        """Gets the time zone of the time stamps on the raw input data"""
        ...

    @property
    def TickType(self) -> int:
        """
        TickType of the history request
        
        This property contains the int value of a member of the QuantConnect.TickType enum.
        """
        ...

    @TickType.setter
    def TickType(self, value: int):
        """
        TickType of the history request
        
        This property contains the int value of a member of the QuantConnect.TickType enum.
        """
        ...

    @property
    def IsCustomData(self) -> bool:
        """Gets true if this is a custom data request, false for normal QC data"""
        ...

    @IsCustomData.setter
    def IsCustomData(self, value: bool):
        """Gets true if this is a custom data request, false for normal QC data"""
        ...

    @property
    def DataNormalizationMode(self) -> int:
        """
        Gets the normalization mode used for this subscription
        
        This property contains the int value of a member of the QuantConnect.DataNormalizationMode enum.
        """
        ...

    @DataNormalizationMode.setter
    def DataNormalizationMode(self, value: int):
        """
        Gets the normalization mode used for this subscription
        
        This property contains the int value of a member of the QuantConnect.DataNormalizationMode enum.
        """
        ...

    @property
    def DataMappingMode(self) -> int:
        """
        Gets the data mapping mode used for this subscription
        
        This property contains the int value of a member of the QuantConnect.DataMappingMode enum.
        """
        ...

    @DataMappingMode.setter
    def DataMappingMode(self, value: int):
        """
        Gets the data mapping mode used for this subscription
        
        This property contains the int value of a member of the QuantConnect.DataMappingMode enum.
        """
        ...

    @property
    def ContractDepthOffset(self) -> int:
        """
        The continuous contract desired offset from the current front month.
        For example, 0 (default) will use the front month, 1 will use the back month contract
        """
        ...

    @ContractDepthOffset.setter
    def ContractDepthOffset(self, value: int):
        """
        The continuous contract desired offset from the current front month.
        For example, 0 (default) will use the front month, 1 will use the back month contract
        """
        ...

    @property
    def TradableDays(self) -> System.Collections.Generic.IEnumerable[datetime.datetime]:
        """Gets the tradable days specified by this request, in the security's data time zone"""
        ...

    @overload
    def __init__(self, startTimeUtc: typing.Union[datetime.datetime, datetime.date], endTimeUtc: typing.Union[datetime.datetime, datetime.date], dataType: typing.Type, symbol: typing.Union[QuantConnect.Symbol, str], resolution: QuantConnect.Resolution, exchangeHours: QuantConnect.Securities.SecurityExchangeHours, dataTimeZone: typing.Any, fillForwardResolution: typing.Optional[QuantConnect.Resolution], includeExtendedMarketHours: bool, isCustomData: bool, dataNormalizationMode: QuantConnect.DataNormalizationMode, tickType: QuantConnect.TickType, dataMappingMode: QuantConnect.DataMappingMode = ..., contractDepthOffset: int = 0) -> None:
        """
        Initializes a new instance of the HistoryRequest class from the specified parameters
        
        :param startTimeUtc: The start time for this request,
        :param endTimeUtc: The start time for this request
        :param dataType: The data type of the output data
        :param symbol: The symbol to request data for
        :param resolution: The requested data resolution
        :param exchangeHours: The exchange hours used in fill forward processing
        :param dataTimeZone: The time zone of the data
        :param fillForwardResolution: The requested fill forward resolution for this request
        :param includeExtendedMarketHours: True to include data from pre/post market hours
        :param isCustomData: True for custom user data, false for normal QC data
        :param dataNormalizationMode: Specifies normalization mode used for this subscription
        :param tickType: The tick type used to created the SubscriptionDataConfig for the retrieval of history data
        :param dataMappingMode: The contract mapping mode to use for the security
        :param contractDepthOffset: The continuous contract desired offset from the current front month. For example, 0 (default) will use the front month, 1 will use the back month contract
        """
        ...

    @overload
    def __init__(self, config: QuantConnect.Data.SubscriptionDataConfig, hours: QuantConnect.Securities.SecurityExchangeHours, startTimeUtc: typing.Union[datetime.datetime, datetime.date], endTimeUtc: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the HistoryRequest class from the specified config and exchange hours
        
        :param config: The subscription data config used to initialize this request
        :param hours: The exchange hours used for fill forward processing
        :param startTimeUtc: The start time for this request,
        :param endTimeUtc: The start time for this request
        """
        ...


class HistoryProviderBase(System.Object, QuantConnect.Interfaces.IHistoryProvider, metaclass=abc.ABCMeta):
    """Provides a base type for all history providers"""

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
    @abc.abstractmethod
    def DataPointCount(self) -> int:
        """Gets the total number of data points emitted by this history provider"""
        ...

    def GetHistory(self, requests: System.Collections.Generic.IEnumerable[QuantConnect.Data.HistoryRequest], sliceTimeZone: typing.Any) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice]:
        """
        Gets the history for the requested securities
        
        :param requests: The historical data requests
        :param sliceTimeZone: The time zone used when time stamping the slice instances
        :returns: An enumerable of the slices of data covering the span specified in each request.
        """
        ...

    def Initialize(self, parameters: QuantConnect.Data.HistoryProviderInitializeParameters) -> None:
        """
        Initializes this history provider to work for the specified job
        
        :param parameters: The initialization parameters
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


class InterestRateProvider(System.Object):
    """Fed US Primary Credit Rate at given date"""

    DefaultRiskFreeRate: float
    """Default Risk Free Rate of 1%"""

    def __init__(self) -> None:
        """Create class instance of interest rate provider"""
        ...

    @staticmethod
    def FromCsvFile(file: str, firstInterestRate: typing.Optional[float]) -> typing.Union[System.Collections.Generic.Dictionary[datetime.datetime, float], float]:
        """
        Reads Fed primary credit rate file and returns a dictionary of historical rate changes
        
        :param file: The csv file to be read
        :param firstInterestRate: The first interest rate on file
        :returns: Dictionary of historical credit rate change events.
        """
        ...

    def GetInterestRate(self, dateTime: typing.Union[datetime.datetime, datetime.date]) -> float:
        """
        Get interest rate by a given datetime
        
        :returns: interest rate of the given date.
        """
        ...

    def LoadInterestRateProvider(self) -> None:
        """
        Generate the daily historical US primary credit rate
        
        This method is protected.
        """
        ...

    @staticmethod
    def TryParse(csvLine: str, date: typing.Optional[typing.Union[datetime.datetime, datetime.date]], interestRate: typing.Optional[float]) -> typing.Union[bool, typing.Union[datetime.datetime, datetime.date], float]:
        """
        Parse the string into the interest rate date and value
        
        :param csvLine: The csv line to be parsed
        :param date: Parsed interest rate date
        :param interestRate: Parsed interest rate value
        """
        ...


class DataQueueHandlerSubscriptionManager(System.Object, System.IDisposable, metaclass=abc.ABCMeta):
    """Count number of subscribers for each channel (Symbol, Socket) pair"""

    @property
    def SubscribersByChannel(self) -> System.Collections.Concurrent.ConcurrentDictionary[QuantConnect.Data.Channel, int]:
        """
        Counter
        
        This field is protected.
        """
        ...

    @SubscribersByChannel.setter
    def SubscribersByChannel(self, value: System.Collections.Concurrent.ConcurrentDictionary[QuantConnect.Data.Channel, int]):
        """
        Counter
        
        This field is protected.
        """
        ...

    def ChannelNameFromTickType(self, tickType: QuantConnect.TickType) -> str:
        """
        Brokerage maps TickType to real socket/api channel
        
        This method is protected.
        
        :param tickType: Type of tick data
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def GetSubscribedSymbols(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Returns subscribed symbols
        
        :returns: list of Symbol currently subscribed.
        """
        ...

    def IsSubscribed(self, symbol: typing.Union[QuantConnect.Symbol, str], tickType: QuantConnect.TickType) -> bool:
        """
        Checks if there is existing subscriber for current channel
        
        :param symbol: Symbol
        :param tickType: Type of tick data
        :returns: return true if there is one subscriber at least; otherwise false.
        """
        ...

    @overload
    def Subscribe(self, dataConfig: QuantConnect.Data.SubscriptionDataConfig) -> None:
        """
        Increment number of subscribers for current TickType
        
        :param dataConfig: defines the subscription configuration data.
        """
        ...

    @overload
    def Subscribe(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], tickType: QuantConnect.TickType) -> bool:
        """
        Describes the way IDataQueueHandler implements subscription
        
        This method is protected.
        
        :param symbols: Symbols to subscribe
        :param tickType: Type of tick data
        :returns: Returns true if subsribed; otherwise false.
        """
        ...

    @overload
    def Unsubscribe(self, dataConfig: QuantConnect.Data.SubscriptionDataConfig) -> None:
        """
        Decrement number of subscribers for current TickType
        
        :param dataConfig: defines the subscription configuration data.
        """
        ...

    @overload
    def Unsubscribe(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], tickType: QuantConnect.TickType) -> bool:
        """
        Describes the way IDataQueueHandler implements unsubscription
        
        This method is protected.
        
        :param symbols: Symbols to unsubscribe
        :param tickType: Type of tick data
        :returns: Returns true if unsubsribed; otherwise false.
        """
        ...


class EventBasedDataQueueHandlerSubscriptionManager(QuantConnect.Data.DataQueueHandlerSubscriptionManager):
    """Overrides DataQueueHandlerSubscriptionManager methods using events"""

    @property
    def SubscribeImpl(self) -> typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Symbol], QuantConnect.TickType], bool]:
        """Subscription method implementation"""
        ...

    @SubscribeImpl.setter
    def SubscribeImpl(self, value: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Symbol], QuantConnect.TickType], bool]):
        """Subscription method implementation"""
        ...

    @property
    def UnsubscribeImpl(self) -> typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Symbol], QuantConnect.TickType], bool]:
        """Unsubscription method implementation"""
        ...

    @UnsubscribeImpl.setter
    def UnsubscribeImpl(self, value: typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Symbol], QuantConnect.TickType], bool]):
        """Unsubscription method implementation"""
        ...

    @overload
    def __init__(self) -> None:
        """Creates an instance of EventBasedDataQueueHandlerSubscriptionManager with a single channel name"""
        ...

    @overload
    def __init__(self, getChannelName: typing.Callable[[QuantConnect.TickType], str]) -> None:
        """
        Creates an instance of EventBasedDataQueueHandlerSubscriptionManager
        
        :param getChannelName: Convert TickType into string
        """
        ...

    def ChannelNameFromTickType(self, tickType: QuantConnect.TickType) -> str:
        """
        Channel name
        
        This method is protected.
        
        :param tickType: Type of tick data
        :returns: Returns Socket channel name corresponding.
        """
        ...

    def Subscribe(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], tickType: QuantConnect.TickType) -> bool:
        """
        The way Brokerage subscribes to symbol tickers
        
        This method is protected.
        
        :param symbols: Symbols to subscribe
        :param tickType: Type of tick data
        """
        ...

    def Unsubscribe(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], tickType: QuantConnect.TickType) -> bool:
        """
        The way Brokerage unsubscribes from symbol tickers
        
        This method is protected.
        
        :param symbols: Symbols to unsubscribe
        :param tickType: Type of tick data
        """
        ...


class HistoryRequestFactory(System.Object):
    """Helper class used to create new HistoryRequest"""

    def __init__(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """
        Creates a new instance
        
        :param algorithm: The algorithm instance to use
        """
        ...

    def CreateHistoryRequest(self, subscription: QuantConnect.Data.SubscriptionDataConfig, startAlgoTz: typing.Union[datetime.datetime, datetime.date], endAlgoTz: typing.Union[datetime.datetime, datetime.date], exchangeHours: QuantConnect.Securities.SecurityExchangeHours, resolution: typing.Optional[QuantConnect.Resolution], dataMappingMode: typing.Optional[QuantConnect.DataMappingMode] = None, dataNormalizationMode: typing.Optional[QuantConnect.DataNormalizationMode] = None, contractDepthOffset: typing.Optional[int] = None) -> QuantConnect.Data.HistoryRequest:
        """
        Creates a new history request
        
        :param subscription: The config
        :param startAlgoTz: History request start time in algorithm time zone
        :param endAlgoTz: History request end time in algorithm time zone
        :param exchangeHours: Security exchange hours
        :param resolution: The resolution to use. If null will use SubscriptionDataConfig.Resolution
        :param dataMappingMode: The contract mapping mode to use for the security history request
        :param dataNormalizationMode: The price scaling mode to use for the securities history
        :param contractDepthOffset: The continuous contract desired offset from the current front month. For example, 0 (default) will use the front month, 1 will use the back month contract
        :returns: The new HistoryRequest.
        """
        ...

    def GetStartTimeAlgoTz(self, symbol: typing.Union[QuantConnect.Symbol, str], periods: int, resolution: QuantConnect.Resolution, exchange: QuantConnect.Securities.SecurityExchangeHours, dataTimeZone: typing.Any) -> datetime.datetime:
        """
        Gets the start time required for the specified bar count in terms of the algorithm's time zone
        
        :param symbol: The symbol to select proper SubscriptionDataConfig config
        :param periods: The number of bars requested
        :param resolution: The length of each bar
        :param exchange: The exchange hours used for market open hours
        :param dataTimeZone: The time zone in which data are stored
        :returns: The start time that would provide the specified number of bars ending at the algorithm's current time.
        """
        ...


class IDataAggregator(System.IDisposable, metaclass=abc.ABCMeta):
    """Aggregates ticks and bars based on given subscriptions."""

    def Add(self, dataConfig: QuantConnect.Data.SubscriptionDataConfig, newDataAvailableHandler: typing.Callable[[System.Object, System.EventArgs], None]) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Add new subscription to current IDataAggregator instance
        
        :param dataConfig: defines the parameters to subscribe to a data feed
        :param newDataAvailableHandler: handler to be fired on new data available
        :returns: The new enumerator for this subscription request.
        """
        ...

    def Remove(self, dataConfig: QuantConnect.Data.SubscriptionDataConfig) -> bool:
        """
        Remove the given subscription
        
        :param dataConfig: defines the subscription configuration data.
        :returns: Returns true if given SubscriptionDataConfig was found and succesfully removed; otherwise false.
        """
        ...

    def Update(self, input: QuantConnect.Data.BaseData) -> None:
        """
        Adds new BaseData input into aggregator.
        
        :param input: The new data
        """
        ...


class SubscriptionDataConfigExtensions(System.Object):
    """
    Helper methods used to determine different configurations properties
    for a given set of SubscriptionDataConfig
    """

    @staticmethod
    def DataNormalizationMode(subscriptionDataConfigs: System.Collections.Generic.IEnumerable[QuantConnect.Data.SubscriptionDataConfig]) -> int:
        """
        Extension method used to determine what QuantConnect.DataNormalizationMode
        to use for a given set of SubscriptionDataConfig
        
        :returns: The first DataNormalizationMode, DataNormalizationMode.Adjusted if there  are no subscriptions. This method returns the int value of a member of the QuantConnect.DataNormalizationMode enum.
        """
        ...

    @staticmethod
    def EmitSplitsAndDividends(config: QuantConnect.Data.SubscriptionDataConfig) -> bool:
        """
        Will determine if splits and dividends should be used for this subscription configuration
        
        :param config: The subscription data configuration we are processing
        :returns: True if this configuration requires split and divided handling.
        """
        ...

    @staticmethod
    def GetBaseDataInstance(config: QuantConnect.Data.SubscriptionDataConfig) -> QuantConnect.Data.BaseData:
        """Initializes a new instance of the BaseData type defined in  with the symbol properly set"""
        ...

    @staticmethod
    def GetHighestResolution(subscriptionDataConfigs: System.Collections.Generic.IEnumerable[QuantConnect.Data.SubscriptionDataConfig]) -> int:
        """
        Extension method used to obtain the highest Resolution
        for a given set of SubscriptionDataConfig
        
        :returns: The highest resolution, Resolution.Daily if there are no subscriptions. This method returns the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    @staticmethod
    def IsCustomData(subscriptionDataConfigs: System.Collections.Generic.IEnumerable[QuantConnect.Data.SubscriptionDataConfig]) -> bool:
        """
        Extension method used to determine if it is custom data
        for a given set of SubscriptionDataConfig
        
        :returns: True, at least one subscription is custom data.
        """
        ...

    @staticmethod
    def IsExtendedMarketHours(subscriptionDataConfigs: System.Collections.Generic.IEnumerable[QuantConnect.Data.SubscriptionDataConfig]) -> bool:
        """
        Extension method used to determine if ExtendedMarketHours is enabled
        for a given set of SubscriptionDataConfig
        
        :returns: True, at least one subscription has it enabled.
        """
        ...

    @staticmethod
    def IsFillForward(subscriptionDataConfigs: System.Collections.Generic.IEnumerable[QuantConnect.Data.SubscriptionDataConfig]) -> bool:
        """
        Extension method used to determine if FillForward is enabled
        for a given set of SubscriptionDataConfig
        
        :returns: True, at least one subscription has it enabled.
        """
        ...

    @staticmethod
    def PricesShouldBeScaled(config: QuantConnect.Data.SubscriptionDataConfig, liveMode: bool = False) -> bool:
        """
        Will determine if price scaling should be used for this subscription configuration
        
        :param config: The subscription data configuration we are processing
        :param liveMode: True, is this is a live mode data stream
        :returns: True if ticker prices should be scaled.
        """
        ...

    @staticmethod
    def SetDataNormalizationMode(subscriptionDataConfigs: System.Collections.Generic.IEnumerable[QuantConnect.Data.SubscriptionDataConfig], mode: QuantConnect.DataNormalizationMode) -> None:
        """
        Sets the data normalization mode to be used by
        this set of SubscriptionDataConfig
        """
        ...

    @staticmethod
    def TickerShouldBeMapped(config: QuantConnect.Data.SubscriptionDataConfig) -> bool:
        """
        Will determine if mapping should be used for this subscription configuration
        
        :param config: The subscription data configuration we are processing
        :returns: True if ticker should be mapped.
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Data__EventContainer_Callable, QuantConnect_Data__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Data__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Data__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Data__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


