from typing import overload
import abc
import datetime
import typing
import warnings

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Market
import QuantConnect.Interfaces
import QuantConnect.Orders
import System
import System.Collections
import System.Collections.Generic
import System.IO

QuantConnect_Data_Market_DataDictionary_T = typing.TypeVar("QuantConnect_Data_Market_DataDictionary_T")
QuantConnect_Data_Market_DataDictionaryExtensions_Add_T = typing.TypeVar("QuantConnect_Data_Market_DataDictionaryExtensions_Add_T")
QuantConnect_Data_Market_OptionChain_GetAux_T = typing.TypeVar("QuantConnect_Data_Market_OptionChain_GetAux_T")
QuantConnect_Data_Market_OptionChain_GetAuxList_T = typing.TypeVar("QuantConnect_Data_Market_OptionChain_GetAuxList_T")
QuantConnect_Data_Market_TradeBar_ParseEquity_T = typing.TypeVar("QuantConnect_Data_Market_TradeBar_ParseEquity_T")
QuantConnect_Data_Market_TradeBar_ParseForex_T = typing.TypeVar("QuantConnect_Data_Market_TradeBar_ParseForex_T")
QuantConnect_Data_Market_TradeBar_ParseCrypto_T = typing.TypeVar("QuantConnect_Data_Market_TradeBar_ParseCrypto_T")
QuantConnect_Data_Market_TradeBar_ParseCfd_T = typing.TypeVar("QuantConnect_Data_Market_TradeBar_ParseCfd_T")
QuantConnect_Data_Market_TradeBar_ParseOption_T = typing.TypeVar("QuantConnect_Data_Market_TradeBar_ParseOption_T")
QuantConnect_Data_Market_TradeBar_ParseFuture_T = typing.TypeVar("QuantConnect_Data_Market_TradeBar_ParseFuture_T")
QuantConnect_Data_Market_FuturesChain_GetAux_T = typing.TypeVar("QuantConnect_Data_Market_FuturesChain_GetAux_T")
QuantConnect_Data_Market_FuturesChain_GetAuxList_T = typing.TypeVar("QuantConnect_Data_Market_FuturesChain_GetAuxList_T")


class IBar(metaclass=abc.ABCMeta):
    """Generic bar interface with Open, High, Low and Close."""

    @property
    @abc.abstractmethod
    def Open(self) -> float:
        """Opening price of the bar: Defined as the price at the start of the time period."""
        ...

    @property
    @abc.abstractmethod
    def High(self) -> float:
        """High price of the bar during the time period."""
        ...

    @property
    @abc.abstractmethod
    def Low(self) -> float:
        """Low price of the bar during the time period."""
        ...

    @property
    @abc.abstractmethod
    def Close(self) -> float:
        """Closing price of the bar. Defined as the price at Start Time + TimeSpan."""
        ...


class Bar(System.Object, QuantConnect.Data.Market.IBar):
    """Base Bar Class: Open, High, Low, Close and Period."""

    @property
    def Open(self) -> float:
        """Opening price of the bar: Defined as the price at the start of the time period."""
        ...

    @Open.setter
    def Open(self, value: float):
        """Opening price of the bar: Defined as the price at the start of the time period."""
        ...

    @property
    def High(self) -> float:
        """High price of the bar during the time period."""
        ...

    @High.setter
    def High(self, value: float):
        """High price of the bar during the time period."""
        ...

    @property
    def Low(self) -> float:
        """Low price of the bar during the time period."""
        ...

    @Low.setter
    def Low(self, value: float):
        """Low price of the bar during the time period."""
        ...

    @property
    def Close(self) -> float:
        """Closing price of the bar. Defined as the price at Start Time + TimeSpan."""
        ...

    @Close.setter
    def Close(self, value: float):
        """Closing price of the bar. Defined as the price at Start Time + TimeSpan."""
        ...

    @overload
    def __init__(self) -> None:
        """Default initializer to setup an empty bar."""
        ...

    @overload
    def __init__(self, open: float, high: float, low: float, close: float) -> None:
        """
        Initializer to setup a bar with a given information.
        
        :param open: Decimal Opening Price
        :param high: Decimal High Price of this bar
        :param low: Decimal Low Price of this bar
        :param close: Decimal Close price of this bar
        """
        ...

    def Clone(self) -> QuantConnect.Data.Market.Bar:
        """Returns a clone of this bar"""
        ...

    def ToString(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...

    @overload
    def Update(self, value: float) -> None:
        """
        Updates the bar with a new value. This will aggregate the OHLC bar
        
        :param value: The new value
        """
        ...

    @overload
    def Update(self, value: float) -> None:
        """
        Updates the bar with a new value. This will aggregate the OHLC bar
        
        :param value: The new value
        """
        ...


class DataDictionary(typing.Generic[QuantConnect_Data_Market_DataDictionary_T], QuantConnect.ExtendedDictionary[QuantConnect_Data_Market_DataDictionary_T], System.Collections.Generic.IDictionary[QuantConnect.Symbol, QuantConnect_Data_Market_DataDictionary_T], typing.Iterable[System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect_Data_Market_DataDictionary_T]]):
    """Provides a base class for types holding base data instances keyed by symbol"""

    @property
    def Time(self) -> datetime.datetime:
        """
        Gets or sets the time associated with this collection of data
        
        The DataDictionary<T> Time property is now obsolete. All algorithms should use algorithm.Time instead.
        """
        warnings.warn("The DataDictionary<T> Time property is now obsolete. All algorithms should use algorithm.Time instead.", DeprecationWarning)

    @Time.setter
    def Time(self, value: datetime.datetime):
        """
        Gets or sets the time associated with this collection of data
        
        The DataDictionary<T> Time property is now obsolete. All algorithms should use algorithm.Time instead.
        """
        warnings.warn("The DataDictionary<T> Time property is now obsolete. All algorithms should use algorithm.Time instead.", DeprecationWarning)

    @property
    def Count(self) -> int:
        """Gets the number of elements contained in the System.Collections.Generic.ICollection`1."""
        ...

    @property
    def IsReadOnly(self) -> bool:
        """Gets a value indicating whether the System.Collections.Generic.ICollection`1 is read-only."""
        ...

    @property
    def Keys(self) -> System.Collections.Generic.ICollection[QuantConnect.Symbol]:
        """Gets an System.Collections.Generic.ICollection`1 containing the keys of the System.Collections.Generic.IDictionary`2."""
        ...

    @property
    def Values(self) -> System.Collections.Generic.ICollection[QuantConnect_Data_Market_DataDictionary_T]:
        """Gets an System.Collections.Generic.ICollection`1 containing the values in the System.Collections.Generic.IDictionary`2."""
        ...

    @property
    def GetKeys(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Gets an System.Collections.Generic.ICollection`1 containing the Symbol objects of the System.Collections.Generic.IDictionary`2.
        
        This property is protected.
        """
        ...

    @property
    def GetValues(self) -> System.Collections.Generic.IEnumerable[QuantConnect_Data_Market_DataDictionary_T]:
        """
        Gets an System.Collections.Generic.ICollection`1 containing the values in the System.Collections.Generic.IDictionary`2.
        
        This property is protected.
        """
        ...

    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect_Data_Market_DataDictionary_T:
        """
        Gets or sets the element with the specified key.
        
        :param symbol: The key of the element to get or set.
        :returns: The element with the specified key.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the QuantConnect.Data.Market.DataDictionary{T} class."""
        ...

    @overload
    def __init__(self, data: System.Collections.Generic.IEnumerable[QuantConnect_Data_Market_DataDictionary_T], keySelector: typing.Callable[[QuantConnect_Data_Market_DataDictionary_T], QuantConnect.Symbol]) -> None:
        """
        Initializes a new instance of the QuantConnect.Data.Market.DataDictionary{T} class
        using the specified  as a data source
        
        :param data: The data source for this data dictionary
        :param keySelector: Delegate used to select a key from the value
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the QuantConnect.Data.Market.DataDictionary{T} class.
        
        :param time: The time this data was emitted.
        """
        ...

    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect_Data_Market_DataDictionary_T) -> None:
        """
        Gets or sets the element with the specified key.
        
        :param symbol: The key of the element to get or set.
        :returns: The element with the specified key.
        """
        ...

    @overload
    def Add(self, item: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect_Data_Market_DataDictionary_T]) -> None:
        """
        Adds an item to the System.Collections.Generic.ICollection`1.
        
        :param item: The object to add to the System.Collections.Generic.ICollection`1.
        """
        ...

    @overload
    def Add(self, key: typing.Union[QuantConnect.Symbol, str], value: QuantConnect_Data_Market_DataDictionary_T) -> None:
        """
        Adds an element with the provided key and value to the System.Collections.Generic.IDictionary`2.
        
        :param key: The object to use as the key of the element to add.
        :param value: The object to use as the value of the element to add.
        """
        ...

    def Clear(self) -> None:
        """Removes all items from the System.Collections.Generic.ICollection`1."""
        ...

    def Contains(self, item: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect_Data_Market_DataDictionary_T]) -> bool:
        """
        Determines whether the System.Collections.Generic.ICollection`1 contains a specific value.
        
        :param item: The object to locate in the System.Collections.Generic.ICollection`1.
        :returns: true if  is found in the System.Collections.Generic.ICollection`1; otherwise, false.
        """
        ...

    def ContainsKey(self, key: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Determines whether the System.Collections.Generic.IDictionary`2 contains an element with the specified key.
        
        :param key: The key to locate in the System.Collections.Generic.IDictionary`2.
        :returns: true if the System.Collections.Generic.IDictionary`2 contains an element with the key; otherwise, false.
        """
        ...

    def CopyTo(self, array: typing.List[System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect_Data_Market_DataDictionary_T]], arrayIndex: int) -> None:
        """
        Copies the elements of the System.Collections.Generic.ICollection`1 to an System.Array, starting at a particular System.Array index.
        
        :param array: The one-dimensional System.Array that is the destination of the elements copied from System.Collections.Generic.ICollection`1. The System.Array must have zero-based indexing.
        :param arrayIndex: The zero-based index in  at which copying begins.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect_Data_Market_DataDictionary_T]]:
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

    def GetValue(self, key: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect_Data_Market_DataDictionary_T:
        """
        Gets the value associated with the specified key.
        
        :param key: The key whose value to get.
        :returns: The value associated with the specified key, if the key is found; otherwise, the default value for the type of the T parameter.
        """
        ...

    @overload
    def Remove(self, item: System.Collections.Generic.KeyValuePair[QuantConnect.Symbol, QuantConnect_Data_Market_DataDictionary_T]) -> bool:
        """
        Removes the first occurrence of a specific object from the System.Collections.Generic.ICollection`1.
        
        :param item: The object to remove from the System.Collections.Generic.ICollection`1.
        :returns: true if  was successfully removed from the System.Collections.Generic.ICollection`1; otherwise, false. This method also returns false if  is not found in the original System.Collections.Generic.ICollection`1.
        """
        ...

    @overload
    def Remove(self, key: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Removes the element with the specified key from the System.Collections.Generic.IDictionary`2.
        
        :param key: The key of the element to remove.
        :returns: true if the element is successfully removed; otherwise, false.  This method also returns false if  was not found in the original System.Collections.Generic.IDictionary`2.
        """
        ...

    def TryGetValue(self, key: typing.Union[QuantConnect.Symbol, str], value: typing.Optional[QuantConnect_Data_Market_DataDictionary_T]) -> typing.Union[bool, QuantConnect_Data_Market_DataDictionary_T]:
        """
        Gets the value associated with the specified key.
        
        :param key: The key whose value to get.
        :param value: When this method returns, the value associated with the specified key, if the key is found; otherwise, the default value for the type of the  parameter. This parameter is passed uninitialized.
        :returns: true if the object that implements System.Collections.Generic.IDictionary`2 contains an element with the specified key; otherwise, false.
        """
        ...


class FuturesContract(System.Object):
    """Defines a single futures contract at a specific expiration"""

    @property
    def Symbol(self) -> QuantConnect.Symbol:
        """Gets the futures contract's symbol"""
        ...

    @Symbol.setter
    def Symbol(self, value: QuantConnect.Symbol):
        """Gets the futures contract's symbol"""
        ...

    @property
    def UnderlyingSymbol(self) -> QuantConnect.Symbol:
        """Gets the underlying security's symbol"""
        ...

    @UnderlyingSymbol.setter
    def UnderlyingSymbol(self, value: QuantConnect.Symbol):
        """Gets the underlying security's symbol"""
        ...

    @property
    def Expiry(self) -> datetime.datetime:
        """Gets the expiration date"""
        ...

    @property
    def Time(self) -> datetime.datetime:
        """Gets the local date time this contract's data was last updated"""
        ...

    @Time.setter
    def Time(self, value: datetime.datetime):
        """Gets the local date time this contract's data was last updated"""
        ...

    @property
    def OpenInterest(self) -> float:
        """Gets the open interest"""
        ...

    @OpenInterest.setter
    def OpenInterest(self, value: float):
        """Gets the open interest"""
        ...

    @property
    def LastPrice(self) -> float:
        """Gets the last price this contract traded at"""
        ...

    @LastPrice.setter
    def LastPrice(self, value: float):
        """Gets the last price this contract traded at"""
        ...

    @property
    def Volume(self) -> int:
        """Gets the last volume this contract traded at"""
        ...

    @Volume.setter
    def Volume(self, value: int):
        """Gets the last volume this contract traded at"""
        ...

    @property
    def BidPrice(self) -> float:
        """Gets the current bid price"""
        ...

    @BidPrice.setter
    def BidPrice(self, value: float):
        """Gets the current bid price"""
        ...

    @property
    def BidSize(self) -> int:
        """Get the current bid size"""
        ...

    @BidSize.setter
    def BidSize(self, value: int):
        """Get the current bid size"""
        ...

    @property
    def AskPrice(self) -> float:
        """Gets the ask price"""
        ...

    @AskPrice.setter
    def AskPrice(self, value: float):
        """Gets the ask price"""
        ...

    @property
    def AskSize(self) -> int:
        """Gets the current ask size"""
        ...

    @AskSize.setter
    def AskSize(self, value: int):
        """Gets the current ask size"""
        ...

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], underlyingSymbol: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Initializes a new instance of the FuturesContract class
        
        :param symbol: The futures contract symbol
        :param underlyingSymbol: The symbol of the underlying security
        """
        ...

    def ToString(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class FuturesContracts(QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.FuturesContract]):
    """Collection of FuturesContract keyed by futures symbol"""

    @overload
    def __getitem__(self, ticker: str) -> QuantConnect.Data.Market.FuturesContract:
        """
        Gets or sets the FuturesContract with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The FuturesContract with the specified ticker.
        """
        ...

    @overload
    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Market.FuturesContract:
        """
        Gets or sets the FuturesContract with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The FuturesContract with the specified Symbol.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new instance of the FuturesContracts dictionary"""
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """Creates a new instance of the FuturesContracts dictionary"""
        ...

    @overload
    def __setitem__(self, ticker: str, value: QuantConnect.Data.Market.FuturesContract) -> None:
        """
        Gets or sets the FuturesContract with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The FuturesContract with the specified ticker.
        """
        ...

    @overload
    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Data.Market.FuturesContract) -> None:
        """
        Gets or sets the FuturesContract with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The FuturesContract with the specified Symbol.
        """
        ...


class Tick(QuantConnect.Data.BaseData):
    """
    Tick class is the base representation for tick data. It is grouped into a Ticks object
    which implements IDictionary and passed into an OnData event handler.
    """

    @property
    def TickType(self) -> QuantConnect.TickType:
        """Type of the Tick: Trade or Quote."""
        ...

    @TickType.setter
    def TickType(self, value: QuantConnect.TickType):
        """Type of the Tick: Trade or Quote."""
        ...

    @property
    def Quantity(self) -> float:
        """Quantity exchanged in a trade."""
        ...

    @Quantity.setter
    def Quantity(self, value: float):
        """Quantity exchanged in a trade."""
        ...

    @property
    def ExchangeCode(self) -> str:
        """Exchange code this tick came from Exchanges"""
        ...

    @ExchangeCode.setter
    def ExchangeCode(self, value: str):
        """Exchange code this tick came from Exchanges"""
        ...

    @property
    def Exchange(self) -> str:
        """Exchange name this tick came from Exchanges"""
        ...

    @Exchange.setter
    def Exchange(self, value: str):
        """Exchange name this tick came from Exchanges"""
        ...

    @property
    def SaleCondition(self) -> str:
        """Sale condition for the tick."""
        ...

    @SaleCondition.setter
    def SaleCondition(self, value: str):
        """Sale condition for the tick."""
        ...

    @property
    def ParsedSaleCondition(self) -> int:
        """For performance parsed sale condition for the tick."""
        ...

    @ParsedSaleCondition.setter
    def ParsedSaleCondition(self, value: int):
        """For performance parsed sale condition for the tick."""
        ...

    @property
    def Suspicious(self) -> bool:
        """Bool whether this is a suspicious tick"""
        ...

    @Suspicious.setter
    def Suspicious(self, value: bool):
        """Bool whether this is a suspicious tick"""
        ...

    @property
    def BidPrice(self) -> float:
        """Bid Price for Tick"""
        ...

    @BidPrice.setter
    def BidPrice(self, value: float):
        """Bid Price for Tick"""
        ...

    @property
    def AskPrice(self) -> float:
        """Asking price for the Tick quote."""
        ...

    @AskPrice.setter
    def AskPrice(self, value: float):
        """Asking price for the Tick quote."""
        ...

    @property
    def LastPrice(self) -> float:
        """Alias for "Value" - the last sale for this asset."""
        ...

    @property
    def BidSize(self) -> float:
        """Size of bid quote."""
        ...

    @BidSize.setter
    def BidSize(self, value: float):
        """Size of bid quote."""
        ...

    @property
    def AskSize(self) -> float:
        """Size of ask quote."""
        ...

    @AskSize.setter
    def AskSize(self, value: float):
        """Size of ask quote."""
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, original: QuantConnect.Data.Market.Tick) -> None:
        """
        Cloner constructor for fill forward engine implementation. Clone the original tick into this new tick:
        
        :param original: Original tick we're cloning
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str], bid: float, ask: float) -> None:
        """
        Constructor for a FOREX tick where there is no last sale price. The volume in FX is so high its rare to find FX trade data.
        To fake this the tick contains bid-ask prices and the last price is the midpoint.
        
        :param time: Full date and time
        :param symbol: Underlying currency pair we're trading
        :param bid: FX tick bid value
        :param ask: FX tick ask value
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str], last: float, bid: float, ask: float) -> None:
        """
        Initializer for a last-trade equity tick with bid or ask prices.
        
        :param time: Full date and time
        :param symbol: Underlying equity security symbol
        :param last: Last trade price
        :param bid: Bid value
        :param ask: Ask value
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str], saleCondition: str, exchange: str, quantity: float, price: float) -> None:
        """
        Trade tick type constructor
        
        :param time: Full date and time
        :param symbol: Underlying equity security symbol
        :param saleCondition: The ticks sale condition
        :param exchange: The ticks exchange
        :param quantity: The quantity traded
        :param price: The price of the trade
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str], saleCondition: str, exchange: str, bidSize: float, bidPrice: float, askSize: float, askPrice: float) -> None:
        """
        Quote tick type constructor
        
        :param time: Full date and time
        :param symbol: Underlying equity security symbol
        :param saleCondition: The ticks sale condition
        :param exchange: The ticks exchange
        :param bidSize: The bid size
        :param bidPrice: The bid price
        :param askSize: The ask size
        :param askPrice: The ask price
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], line: str) -> None:
        """
        Constructor for QuantConnect FXCM Data source:
        
        :param symbol: Symbol for underlying asset
        :param line: CSV line of data from FXCM
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], line: str, baseDate: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Constructor for QuantConnect tick data
        
        :param symbol: Symbol for underlying asset
        :param line: CSV line of data from QC tick csv
        :param baseDate: The base date of the tick
        """
        ...

    @overload
    def __init__(self, config: QuantConnect.Data.SubscriptionDataConfig, reader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Parse a tick data line from quantconnect zip source files.
        
        :param config: Subscription configuration object
        :param reader: The source stream reader
        :param date: Base date for the tick (ticks date is stored as int milliseconds since midnight)
        """
        ...

    @overload
    def __init__(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Parse a tick data line from quantconnect zip source files.
        
        :param config: Subscription configuration object
        :param line: CSV source line of the compressed source
        :param date: Base date for the tick (ticks date is stored as int milliseconds since midnight)
        """
        ...

    def Clone(self) -> QuantConnect.Data.BaseData:
        """
        Clone implementation for tick class:
        
        :returns: New tick object clone of the current class values.
        """
        ...

    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Get source for tick data feed - not used with QuantConnect data sources implementation.
        
        :param config: Configuration object
        :param date: Date of this source request if source spread across multiple files
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: String source location of the file to be opened with a stream.
        """
        ...

    def IsValid(self) -> bool:
        """Check if tick contains valid data (either a trade, or a bid or ask)"""
        ...

    @overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        """
        Tick implementation of reader method: read a line of data from the source and convert it to a tick object.
        
        :param config: Subscription configuration object for algorithm
        :param line: Line from the datafeed source
        :param date: Date of this reader request
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: New Initialized tick.
        """
        ...

    @overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, reader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        """
        Tick implementation of reader method: read a line of data from the source and convert it to a tick object.
        
        :param config: Subscription configuration object for algorithm
        :param reader: The source stream reader
        :param date: Date of this reader request
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: New Initialized tick.
        """
        ...

    def SetValue(self) -> None:
        """Sets the tick Value based on ask and bid price"""
        ...

    def ToString(self) -> str:
        """
        Formats a string with the symbol and value.
        
        :returns: string - a string formatted as SPY: 167.753.
        """
        ...

    def Update(self, lastTrade: float, bidPrice: float, askPrice: float, volume: float, bidSize: float, askSize: float) -> None:
        """
        Update the tick price information - not used.
        
        :param lastTrade: This trade price
        :param bidPrice: Current bid price
        :param askPrice: Current asking price
        :param volume: Volume of this trade
        :param bidSize: The size of the current bid, if available
        :param askSize: The size of the current ask, if available
        """
        ...


class OpenInterest(QuantConnect.Data.Market.Tick):
    """Defines a data type that represents open interest for given security"""

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the OpenInterest class"""
        ...

    @overload
    def __init__(self, original: QuantConnect.Data.Market.OpenInterest) -> None:
        """
        Cloner constructor for fill forward engine implementation. Clone the original OI into this new one:
        
        :param original: Original OI we're cloning
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str], openInterest: float) -> None:
        """
        Initializes a new instance of the OpenInterest class with data
        
        :param time: Full date and time
        :param symbol: Underlying equity security symbol
        :param openInterest: Open Interest value
        """
        ...

    @overload
    def __init__(self, config: QuantConnect.Data.SubscriptionDataConfig, symbol: typing.Union[QuantConnect.Symbol, str], line: str, baseDate: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Constructor for QuantConnect open interest data
        
        :param config: Subscription configuration
        :param symbol: Symbol for underlying asset
        :param line: CSV line of data from QC OI csv
        :param baseDate: The base date of the OI
        """
        ...

    @overload
    def __init__(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Parse an open interest data line from quantconnect zip source files.
        
        :param config: Subscription configuration object
        :param line: CSV source line of the compressed source
        :param date: Base date for the open interest (date is stored as int milliseconds since midnight)
        """
        ...

    def Clone(self) -> QuantConnect.Data.BaseData:
        """
        Clone implementation for open interest class:
        
        :returns: New tick object clone of the current class values.
        """
        ...

    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Get source for OI data feed - not used with QuantConnect data sources implementation.
        
        :param config: Configuration object
        :param date: Date of this source request if source spread across multiple files
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: String source location of the file to be opened with a stream.
        """
        ...

    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        """
        Tick implementation of reader method: read a line of data from the source and convert it to an open interest object.
        
        :param config: Subscription configuration object for algorithm
        :param line: Line from the datafeed source
        :param date: Date of this reader request
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: New initialized open interest object.
        """
        ...


class Ticks(QuantConnect.Data.Market.DataDictionary[System.Collections.Generic.List[QuantConnect.Data.Market.Tick]]):
    """Ticks collection which implements an IDictionary-string-list of ticks. This way users can iterate over the string indexed ticks of the requested symbol."""

    @overload
    def __getitem__(self, ticker: str) -> System.Collections.Generic.List[QuantConnect.Data.Market.Tick]:
        """
        Gets or sets the list of Tick with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The list of Tick with the specified ticker.
        """
        ...

    @overload
    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> System.Collections.Generic.List[QuantConnect.Data.Market.Tick]:
        """
        Gets or sets the list of Tick with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The list of Tick with the specified Symbol.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Ticks dictionary"""
        ...

    @overload
    def __init__(self, frontier: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the Ticks dictionary
        
        :param frontier: The time associated with the data in this dictionary
        """
        ...

    @overload
    def __setitem__(self, ticker: str, value: System.Collections.Generic.List[QuantConnect.Data.Market.Tick]) -> None:
        """
        Gets or sets the list of Tick with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The list of Tick with the specified ticker.
        """
        ...

    @overload
    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: System.Collections.Generic.List[QuantConnect.Data.Market.Tick]) -> None:
        """
        Gets or sets the list of Tick with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The list of Tick with the specified Symbol.
        """
        ...


class IBaseDataBar(QuantConnect.Data.IBaseData, QuantConnect.Data.Market.IBar, metaclass=abc.ABCMeta):
    """Represents a type that is both a bar and base data"""


class TradeBar(QuantConnect.Data.BaseData, QuantConnect.Data.Market.IBaseDataBar):
    """
    TradeBar class for second and minute resolution data:
    An OHLC implementation of the QuantConnect BaseData class with parameters for candles.
    """

    @property
    def Volume(self) -> float:
        """Volume:"""
        ...

    @Volume.setter
    def Volume(self, value: float):
        """Volume:"""
        ...

    @property
    def Open(self) -> float:
        """Opening price of the bar: Defined as the price at the start of the time period."""
        ...

    @Open.setter
    def Open(self, value: float):
        """Opening price of the bar: Defined as the price at the start of the time period."""
        ...

    @property
    def High(self) -> float:
        """High price of the TradeBar during the time period."""
        ...

    @High.setter
    def High(self, value: float):
        """High price of the TradeBar during the time period."""
        ...

    @property
    def Low(self) -> float:
        """Low price of the TradeBar during the time period."""
        ...

    @Low.setter
    def Low(self, value: float):
        """Low price of the TradeBar during the time period."""
        ...

    @property
    def Close(self) -> float:
        """Closing price of the TradeBar. Defined as the price at Start Time + TimeSpan."""
        ...

    @Close.setter
    def Close(self, value: float):
        """Closing price of the TradeBar. Defined as the price at Start Time + TimeSpan."""
        ...

    @property
    def EndTime(self) -> datetime.datetime:
        """The closing time of this bar, computed via the Time and Period"""
        ...

    @EndTime.setter
    def EndTime(self, value: datetime.datetime):
        """The closing time of this bar, computed via the Time and Period"""
        ...

    @property
    def Period(self) -> datetime.timedelta:
        """The period of this trade bar, (second, minute, daily, ect...)"""
        ...

    @Period.setter
    def Period(self, value: datetime.timedelta):
        """The period of this trade bar, (second, minute, daily, ect...)"""
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, original: QuantConnect.Data.Market.TradeBar) -> None:
        """
        Cloner constructor for implementing fill forward.
        Return a new instance with the same values as this original.
        
        :param original: Original tradebar object we seek to clone
        """
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str], open: float, high: float, low: float, close: float, volume: float, period: typing.Optional[datetime.timedelta] = None) -> None:
        """
        Initialize Trade Bar with OHLC Values:
        
        :param time: DateTime Timestamp of the bar
        :param symbol: Market MarketType Symbol
        :param open: Decimal Opening Price
        :param high: Decimal High Price of this bar
        :param low: Decimal Low Price of this bar
        :param close: Decimal Close price of this bar
        :param volume: Volume sum over day
        :param period: The period of this bar, specify null for default of 1 minute
        """
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
        """Return a new instance clone of this object"""
        ...

    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Get Source for Custom Data File
        >> What source file location would you prefer for each type of usage:
        
        :param config: Configuration object
        :param date: Date of this source request if source spread across multiple files
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: String source location of the file.
        """
        ...

    @staticmethod
    def Parse(config: QuantConnect.Data.SubscriptionDataConfig, line: str, baseDate: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """Parses the trade bar data line assuming QC data formats"""
        ...

    @staticmethod
    @overload
    def ParseCfd(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect_Data_Market_TradeBar_ParseCfd_T:
        """
        Parses CFD trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def ParseCfd(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses CFD trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def ParseCfd(config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses CFD trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param streamReader: The data stream of the requested file
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def ParseCrypto(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect_Data_Market_TradeBar_ParseCrypto_T:
        """
        Parses crypto trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def ParseCrypto(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses crypto trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def ParseCrypto(config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses crypto trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param streamReader: The data stream of the requested file
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def ParseEquity(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect_Data_Market_TradeBar_ParseEquity_T:
        """
        Parses equity trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: Date of this reader request
        """
        ...

    @staticmethod
    @overload
    def ParseEquity(config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses equity trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param streamReader: The data stream of the requested file
        :param date: Date of this reader request
        """
        ...

    @staticmethod
    @overload
    def ParseEquity(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses equity trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: Date of this reader request
        """
        ...

    @staticmethod
    @overload
    def ParseForex(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect_Data_Market_TradeBar_ParseForex_T:
        """
        Parses forex trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def ParseForex(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses forex trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def ParseForex(config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses forex trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param streamReader: The data stream of the requested file
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def ParseFuture(config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect_Data_Market_TradeBar_ParseFuture_T:
        """
        Parses Future trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param streamReader: The data stream of the requested file
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def ParseFuture(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect_Data_Market_TradeBar_ParseFuture_T:
        """
        Parses Future trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def ParseFuture(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses Future trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def ParseFuture(config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses Future trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param streamReader: The data stream of the requested file
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def ParseIndex(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """Parse an index bar from the LEAN disk format"""
        ...

    @staticmethod
    @overload
    def ParseIndex(config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """Parse an index bar from the LEAN disk format"""
        ...

    @staticmethod
    @overload
    def ParseOption(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect_Data_Market_TradeBar_ParseOption_T:
        """
        Parses Option trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def ParseOption(config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect_Data_Market_TradeBar_ParseOption_T:
        """
        Parses Option trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param streamReader: The data stream of the requested file
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def ParseOption(config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses Option trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @staticmethod
    @overload
    def ParseOption(config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.TradeBar:
        """
        Parses Option trade bar data into the specified tradebar type, useful for custom types with OHLCV data deriving from TradeBar
        
        :param config: Symbols, Resolution, DataType,
        :param streamReader: The data stream of the requested file
        :param date: The base data used to compute the time of the bar since the line specifies a milliseconds since midnight
        """
        ...

    @overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        """
        TradeBar Reader: Fetch the data from the QC storage and feed it line by line into the engine.
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: Date of this reader request
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: Enumerable iterator for returning each line of the required data.
        """
        ...

    @overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, stream: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        """
        TradeBar Reader: Fetch the data from the QC storage and feed it directly from the stream into the engine.
        
        :param config: Symbols, Resolution, DataType,
        :param stream: The file data stream
        :param date: Date of this reader request
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: Enumerable iterator for returning each line of the required data.
        """
        ...

    def ToString(self) -> str:
        """
        Formats a string with the symbol and value.
        
        :returns: string - a string formatted as SPY: 167.753.
        """
        ...

    def Update(self, lastTrade: float, bidPrice: float, askPrice: float, volume: float, bidSize: float, askSize: float) -> None:
        """
        Update the tradebar - build the bar from this pricing information:
        
        :param lastTrade: This trade price
        :param bidPrice: Current bid price (not used)
        :param askPrice: Current asking price (not used)
        :param volume: Volume of this trade
        :param bidSize: The size of the current bid, if available
        :param askSize: The size of the current ask, if available
        """
        ...


class TradeBars(QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.TradeBar]):
    """Collection of TradeBars to create a data type for generic data handler:"""

    @overload
    def __getitem__(self, ticker: str) -> QuantConnect.Data.Market.TradeBar:
        """
        Gets or sets the TradeBar with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The TradeBar with the specified ticker.
        """
        ...

    @overload
    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Market.TradeBar:
        """
        Gets or sets the TradeBar with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The TradeBar with the specified Symbol.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new instance of the TradeBars dictionary"""
        ...

    @overload
    def __init__(self, frontier: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Creates a new instance of the TradeBars dictionary
        
        :param frontier: The time associated with the data in this dictionary
        """
        ...

    @overload
    def __setitem__(self, ticker: str, value: QuantConnect.Data.Market.TradeBar) -> None:
        """
        Gets or sets the TradeBar with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The TradeBar with the specified ticker.
        """
        ...

    @overload
    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Data.Market.TradeBar) -> None:
        """
        Gets or sets the TradeBar with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The TradeBar with the specified Symbol.
        """
        ...


class Greeks(System.Object):
    """Defines the greeks"""

    @property
    def Delta(self) -> float:
        """
        Gets the delta.
        
        Delta measures the rate of change of the option value with respect to changes in
        the underlying asset'sprice. (∂V/∂S)
        """
        ...

    @Delta.setter
    def Delta(self, value: float):
        """
        Gets the delta.
        
        Delta measures the rate of change of the option value with respect to changes in
        the underlying asset'sprice. (∂V/∂S)
        """
        ...

    @property
    def Gamma(self) -> float:
        """
        Gets the gamma.
        
        Gamma measures the rate of change of Delta with respect to changes in
        the underlying asset'sprice. (∂²V/∂S²)
        """
        ...

    @Gamma.setter
    def Gamma(self, value: float):
        """
        Gets the gamma.
        
        Gamma measures the rate of change of Delta with respect to changes in
        the underlying asset'sprice. (∂²V/∂S²)
        """
        ...

    @property
    def Vega(self) -> float:
        """
        Gets the vega.
        
        Vega measures the rate of change of the option value with respect to changes in
        the underlying's volatility. (∂V/∂σ)
        """
        ...

    @Vega.setter
    def Vega(self, value: float):
        """
        Gets the vega.
        
        Vega measures the rate of change of the option value with respect to changes in
        the underlying's volatility. (∂V/∂σ)
        """
        ...

    @property
    def Theta(self) -> float:
        """
        Gets the theta.
        
        Theta measures the rate of change of the option value with respect to changes in
        time. This is commonly known as the 'time decay.' (∂V/∂τ)
        """
        ...

    @Theta.setter
    def Theta(self, value: float):
        """
        Gets the theta.
        
        Theta measures the rate of change of the option value with respect to changes in
        time. This is commonly known as the 'time decay.' (∂V/∂τ)
        """
        ...

    @property
    def Rho(self) -> float:
        """
        Gets the rho.
        
        Rho measures the rate of change of the option value with respect to changes in
        the risk free interest rate. (∂V/∂r)
        """
        ...

    @Rho.setter
    def Rho(self, value: float):
        """
        Gets the rho.
        
        Rho measures the rate of change of the option value with respect to changes in
        the risk free interest rate. (∂V/∂r)
        """
        ...

    @property
    def Lambda(self) -> float:
        """
        Gets the lambda.
        
        Lambda is the percentage change in option value per percentage change in the
        underlying's price, a measure of leverage. Sometimes referred to as gearing.
        (∂V/∂S ✕ S/V)
        """
        ...

    @Lambda.setter
    def Lambda(self, value: float):
        """
        Gets the lambda.
        
        Lambda is the percentage change in option value per percentage change in the
        underlying's price, a measure of leverage. Sometimes referred to as gearing.
        (∂V/∂S ✕ S/V)
        """
        ...

    @property
    def ThetaPerDay(self) -> float:
        """
        Gets the theta per day.
        
        Theta measures the rate of change of the option value with respect to changes in
        time. This is commonly known as the 'time decay.' (∂V/∂τ)
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new default instance of the Greeks class"""
        ...

    @overload
    def __init__(self, delta: float, gamma: float, vega: float, theta: float, rho: float, _lambda: float) -> None:
        """Initializes a new instance of the Greeks class"""
        ...

    @overload
    def __init__(self, delta: typing.Callable[[], float], gamma: typing.Callable[[], float], vega: typing.Callable[[], float], theta: typing.Callable[[], float], rho: typing.Callable[[], float], _lambda: typing.Callable[[], float]) -> None:
        """Initializes a new instance of the Greeks class"""
        ...

    @overload
    def __init__(self, deltaGamma: typing.Callable[[], System.Tuple[float, float]], vega: typing.Callable[[], float], theta: typing.Callable[[], float], rho: typing.Callable[[], float], _lambda: typing.Callable[[], float]) -> None:
        """Initializes a new instance of the Greeks class"""
        ...


class OptionContract(System.Object):
    """Defines a single option contract at a specific expiration and strike price"""

    @property
    def Symbol(self) -> QuantConnect.Symbol:
        """Gets the option contract's symbol"""
        ...

    @Symbol.setter
    def Symbol(self, value: QuantConnect.Symbol):
        """Gets the option contract's symbol"""
        ...

    @property
    def UnderlyingSymbol(self) -> QuantConnect.Symbol:
        """Gets the underlying security's symbol"""
        ...

    @UnderlyingSymbol.setter
    def UnderlyingSymbol(self, value: QuantConnect.Symbol):
        """Gets the underlying security's symbol"""
        ...

    @property
    def Strike(self) -> float:
        """Gets the strike price"""
        ...

    @property
    def Expiry(self) -> datetime.datetime:
        """Gets the expiration date"""
        ...

    @property
    def Right(self) -> int:
        """
        Gets the right being purchased (call [right to buy] or put [right to sell])
        
        This property contains the int value of a member of the QuantConnect.OptionRight enum.
        """
        ...

    @property
    def Style(self) -> int:
        """
        Gets the option style
        
        This property contains the int value of a member of the QuantConnect.OptionStyle enum.
        """
        ...

    @property
    def TheoreticalPrice(self) -> float:
        """Gets the theoretical price of this option contract as computed by the IOptionPriceModel"""
        ...

    @property
    def ImpliedVolatility(self) -> float:
        """Gets the implied volatility of the option contract as computed by the IOptionPriceModel"""
        ...

    @property
    def Greeks(self) -> QuantConnect.Data.Market.Greeks:
        """Gets the greeks for this contract"""
        ...

    @property
    def Time(self) -> datetime.datetime:
        """Gets the local date time this contract's data was last updated"""
        ...

    @Time.setter
    def Time(self, value: datetime.datetime):
        """Gets the local date time this contract's data was last updated"""
        ...

    @property
    def OpenInterest(self) -> float:
        """Gets the open interest"""
        ...

    @OpenInterest.setter
    def OpenInterest(self, value: float):
        """Gets the open interest"""
        ...

    @property
    def LastPrice(self) -> float:
        """Gets the last price this contract traded at"""
        ...

    @LastPrice.setter
    def LastPrice(self, value: float):
        """Gets the last price this contract traded at"""
        ...

    @property
    def Volume(self) -> int:
        """Gets the last volume this contract traded at"""
        ...

    @Volume.setter
    def Volume(self, value: int):
        """Gets the last volume this contract traded at"""
        ...

    @property
    def BidPrice(self) -> float:
        """Gets the current bid price"""
        ...

    @BidPrice.setter
    def BidPrice(self, value: float):
        """Gets the current bid price"""
        ...

    @property
    def BidSize(self) -> int:
        """Get the current bid size"""
        ...

    @BidSize.setter
    def BidSize(self, value: int):
        """Get the current bid size"""
        ...

    @property
    def AskPrice(self) -> float:
        """Gets the ask price"""
        ...

    @AskPrice.setter
    def AskPrice(self, value: float):
        """Gets the ask price"""
        ...

    @property
    def AskSize(self) -> int:
        """Gets the current ask size"""
        ...

    @AskSize.setter
    def AskSize(self, value: int):
        """Gets the current ask size"""
        ...

    @property
    def UnderlyingLastPrice(self) -> float:
        """Gets the last price the underlying security traded at"""
        ...

    @UnderlyingLastPrice.setter
    def UnderlyingLastPrice(self, value: float):
        """Gets the last price the underlying security traded at"""
        ...

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], underlyingSymbol: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        Initializes a new instance of the OptionContract class
        
        :param symbol: The option contract symbol
        :param underlyingSymbol: The symbol of the underlying security
        """
        ...

    @staticmethod
    @overload
    def Create(baseData: QuantConnect.Data.BaseData, security: QuantConnect.Interfaces.ISecurityPrice, underlyingLastPrice: float) -> QuantConnect.Data.Market.OptionContract:
        """
        Creates a OptionContract
        
        :param security: provides price properties for a Security
        :param underlyingLastPrice: last price the underlying security traded at
        :returns: Option contract.
        """
        ...

    @staticmethod
    @overload
    def Create(symbol: typing.Union[QuantConnect.Symbol, str], underlyingSymbol: typing.Union[QuantConnect.Symbol, str], endTime: typing.Union[datetime.datetime, datetime.date], security: QuantConnect.Interfaces.ISecurityPrice, underlyingLastPrice: float) -> QuantConnect.Data.Market.OptionContract:
        """
        Creates a OptionContract
        
        :param symbol: The option contract symbol
        :param underlyingSymbol: The symbol of the underlying security
        :param endTime: local date time this contract's data was last updated
        :param security: provides price properties for a Security
        :param underlyingLastPrice: last price the underlying security traded at
        :returns: Option contract.
        """
        ...

    def ToString(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class QuoteBar(QuantConnect.Data.BaseData, QuantConnect.Data.Market.IBaseDataBar):
    """
    QuoteBar class for second and minute resolution data:
    An OHLC implementation of the QuantConnect BaseData class with parameters for candles.
    """

    @property
    def LastBidSize(self) -> float:
        """Average bid size"""
        ...

    @LastBidSize.setter
    def LastBidSize(self, value: float):
        """Average bid size"""
        ...

    @property
    def LastAskSize(self) -> float:
        """Average ask size"""
        ...

    @LastAskSize.setter
    def LastAskSize(self, value: float):
        """Average ask size"""
        ...

    @property
    def Bid(self) -> QuantConnect.Data.Market.Bar:
        """Bid OHLC"""
        ...

    @Bid.setter
    def Bid(self, value: QuantConnect.Data.Market.Bar):
        """Bid OHLC"""
        ...

    @property
    def Ask(self) -> QuantConnect.Data.Market.Bar:
        """Ask OHLC"""
        ...

    @Ask.setter
    def Ask(self, value: QuantConnect.Data.Market.Bar):
        """Ask OHLC"""
        ...

    @property
    def Open(self) -> float:
        """Opening price of the bar: Defined as the price at the start of the time period."""
        ...

    @property
    def High(self) -> float:
        """High price of the QuoteBar during the time period."""
        ...

    @property
    def Low(self) -> float:
        """Low price of the QuoteBar during the time period."""
        ...

    @property
    def Close(self) -> float:
        """Closing price of the QuoteBar. Defined as the price at Start Time + TimeSpan."""
        ...

    @property
    def EndTime(self) -> datetime.datetime:
        """The closing time of this bar, computed via the Time and Period"""
        ...

    @EndTime.setter
    def EndTime(self, value: datetime.datetime):
        """The closing time of this bar, computed via the Time and Period"""
        ...

    @property
    def Period(self) -> datetime.timedelta:
        """The period of this quote bar, (second, minute, daily, ect...)"""
        ...

    @Period.setter
    def Period(self, value: datetime.timedelta):
        """The period of this quote bar, (second, minute, daily, ect...)"""
        ...

    @overload
    def __init__(self) -> None:
        """Default initializer to setup an empty quotebar."""
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date], symbol: typing.Union[QuantConnect.Symbol, str], bid: QuantConnect.Data.Market.IBar, lastBidSize: float, ask: QuantConnect.Data.Market.IBar, lastAskSize: float, period: typing.Optional[datetime.timedelta] = None) -> None:
        """
        Initialize Quote Bar with Bid(OHLC) and Ask(OHLC) Values:
        
        :param time: DateTime Timestamp of the bar
        :param symbol: Market MarketType Symbol
        :param bid: Bid OLHC bar
        :param lastBidSize: Average bid size over period
        :param ask: Ask OLHC bar
        :param lastAskSize: Average ask size over period
        :param period: The period of this bar, specify null for default of 1 minute
        """
        ...

    def Clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this quote bar, used in fill forward
        
        :returns: A clone of the current quote bar.
        """
        ...

    def Collapse(self) -> QuantConnect.Data.Market.TradeBar:
        """
        Collapses QuoteBars into TradeBars object when
         algorithm requires FX data, but calls OnData(TradeBars)
        TODO: (2017) Remove this method in favor of using OnData(Slice)
        
        :returns: TradeBars.
        """
        ...

    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Get Source for Custom Data File
        >> What source file location would you prefer for each type of usage:
        
        :param config: Configuration object
        :param date: Date of this source request if source spread across multiple files
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: String source location of the file.
        """
        ...

    @overload
    def ParseCfd(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.QuoteBar:
        """
        Parse a quotebar representing a cfd without a scaling factor
        
        :param config: Symbols, Resolution, DataType
        :param line: Line from the data file requested
        :param date: Date of this reader request
        :returns: QuoteBar with the bid/ask set to same values.
        """
        ...

    @overload
    def ParseCfd(self, config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.QuoteBar:
        """
        Parse a quotebar representing a cfd without a scaling factor
        
        :param config: Symbols, Resolution, DataType
        :param streamReader: The data stream of the requested file
        :param date: Date of this reader request
        :returns: QuoteBar with the bid/ask set to same values.
        """
        ...

    @overload
    def ParseEquity(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.QuoteBar:
        """
        Parse a quotebar representing an equity with a scaling factor
        
        :param config: Symbols, Resolution, DataType
        :param line: Line from the data file requested
        :param date: Date of this reader request
        :returns: QuoteBar with the bid/ask set to same values.
        """
        ...

    @overload
    def ParseEquity(self, config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.QuoteBar:
        """
        Parse a quotebar representing an equity with a scaling factor
        
        :param config: Symbols, Resolution, DataType
        :param streamReader: The data stream of the requested file
        :param date: Date of this reader request
        :returns: QuoteBar with the bid/ask set to same values.
        """
        ...

    @overload
    def ParseForex(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.QuoteBar:
        """
        Parse a quotebar representing a forex without a scaling factor
        
        :param config: Symbols, Resolution, DataType
        :param line: Line from the data file requested
        :param date: Date of this reader request
        :returns: QuoteBar with the bid/ask set to same values.
        """
        ...

    @overload
    def ParseForex(self, config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.QuoteBar:
        """
        Parse a quotebar representing a forex without a scaling factor
        
        :param config: Symbols, Resolution, DataType
        :param streamReader: The data stream of the requested file
        :param date: Date of this reader request
        :returns: QuoteBar with the bid/ask set to same values.
        """
        ...

    @overload
    def ParseFuture(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.QuoteBar:
        """
        Parse a quotebar representing a future with a scaling factor
        
        :param config: Symbols, Resolution, DataType
        :param line: Line from the data file requested
        :param date: Date of this reader request
        :returns: QuoteBar with the bid/ask set to same values.
        """
        ...

    @overload
    def ParseFuture(self, config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.QuoteBar:
        """
        Parse a quotebar representing a future with a scaling factor
        
        :param config: Symbols, Resolution, DataType
        :param streamReader: The data stream of the requested file
        :param date: Date of this reader request
        :returns: QuoteBar with the bid/ask set to same values.
        """
        ...

    @overload
    def ParseOption(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.QuoteBar:
        """
        Parse a quotebar representing an option with a scaling factor
        
        :param config: Symbols, Resolution, DataType
        :param line: Line from the data file requested
        :param date: Date of this reader request
        :returns: QuoteBar with the bid/ask set to same values.
        """
        ...

    @overload
    def ParseOption(self, config: QuantConnect.Data.SubscriptionDataConfig, streamReader: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Data.Market.QuoteBar:
        """
        Parse a quotebar representing an option with a scaling factor
        
        :param config: Symbols, Resolution, DataType
        :param streamReader: The data stream of the requested file
        :param date: Date of this reader request
        :returns: QuoteBar with the bid/ask set to same values.
        """
        ...

    @overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, stream: System.IO.StreamReader, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        """
        QuoteBar Reader: Fetch the data from the QC storage and feed it line by line into the engine.
        
        :param config: Symbols, Resolution, DataType,
        :param stream: The file data stream
        :param date: Date of this reader request
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: Enumerable iterator for returning each line of the required data.
        """
        ...

    @overload
    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        """
        QuoteBar Reader: Fetch the data from the QC storage and feed it line by line into the engine.
        
        :param config: Symbols, Resolution, DataType,
        :param line: Line from the data file requested
        :param date: Date of this reader request
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: Enumerable iterator for returning each line of the required data.
        """
        ...

    def ToString(self) -> str:
        """
        Convert this QuoteBar to string form.
        
        :returns: String representation of the QuoteBar.
        """
        ...

    def Update(self, lastTrade: float, bidPrice: float, askPrice: float, volume: float, bidSize: float, askSize: float) -> None:
        """
        Update the quotebar - build the bar from this pricing information:
        
        :param lastTrade: The last trade price
        :param bidPrice: Current bid price
        :param askPrice: Current asking price
        :param volume: Volume of this trade
        :param bidSize: The size of the current bid, if available, if not, pass 0
        :param askSize: The size of the current ask, if available, if not, pass 0
        """
        ...


class QuoteBars(QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.QuoteBar]):
    """Collection of QuoteBar keyed by symbol"""

    @overload
    def __getitem__(self, ticker: str) -> QuantConnect.Data.Market.QuoteBar:
        """
        Gets or sets the QuoteBar with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The QuoteBar with the specified ticker.
        """
        ...

    @overload
    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Market.QuoteBar:
        """
        Gets or sets the QuoteBar with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The QuoteBar with the specified Symbol.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new instance of the QuoteBars dictionary"""
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """Creates a new instance of the QuoteBars dictionary"""
        ...

    @overload
    def __setitem__(self, ticker: str, value: QuantConnect.Data.Market.QuoteBar) -> None:
        """
        Gets or sets the QuoteBar with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The QuoteBar with the specified ticker.
        """
        ...

    @overload
    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Data.Market.QuoteBar) -> None:
        """
        Gets or sets the QuoteBar with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The QuoteBar with the specified Symbol.
        """
        ...


class FuturesChain(QuantConnect.Data.BaseData, typing.Iterable[QuantConnect.Data.Market.FuturesContract]):
    """
    Represents an entire chain of futures contracts for a single underlying
    This type is IEnumerable{FuturesContract}
    """

    @property
    def Underlying(self) -> QuantConnect.Data.BaseData:
        """
        Gets the most recent trade information for the underlying. This may
        be a Tick or a TradeBar
        """
        ...

    @Underlying.setter
    def Underlying(self, value: QuantConnect.Data.BaseData):
        """
        Gets the most recent trade information for the underlying. This may
        be a Tick or a TradeBar
        """
        ...

    @property
    def Ticks(self) -> QuantConnect.Data.Market.Ticks:
        """Gets all ticks for every futures contract in this chain, keyed by symbol"""
        ...

    @Ticks.setter
    def Ticks(self, value: QuantConnect.Data.Market.Ticks):
        """Gets all ticks for every futures contract in this chain, keyed by symbol"""
        ...

    @property
    def TradeBars(self) -> QuantConnect.Data.Market.TradeBars:
        """Gets all trade bars for every futures contract in this chain, keyed by symbol"""
        ...

    @TradeBars.setter
    def TradeBars(self, value: QuantConnect.Data.Market.TradeBars):
        """Gets all trade bars for every futures contract in this chain, keyed by symbol"""
        ...

    @property
    def QuoteBars(self) -> QuantConnect.Data.Market.QuoteBars:
        """Gets all quote bars for every futures contract in this chain, keyed by symbol"""
        ...

    @QuoteBars.setter
    def QuoteBars(self, value: QuantConnect.Data.Market.QuoteBars):
        """Gets all quote bars for every futures contract in this chain, keyed by symbol"""
        ...

    @property
    def Contracts(self) -> QuantConnect.Data.Market.FuturesContracts:
        """Gets all contracts in the chain, keyed by symbol"""
        ...

    @Contracts.setter
    def Contracts(self, value: QuantConnect.Data.Market.FuturesContracts):
        """Gets all contracts in the chain, keyed by symbol"""
        ...

    @property
    def FilteredContracts(self) -> System.Collections.Generic.HashSet[QuantConnect.Symbol]:
        """Gets the set of symbols that passed the Future.ContractFilter"""
        ...

    @FilteredContracts.setter
    def FilteredContracts(self, value: System.Collections.Generic.HashSet[QuantConnect.Symbol]):
        """Gets the set of symbols that passed the Future.ContractFilter"""
        ...

    @overload
    def __init__(self, canonicalFutureSymbol: typing.Union[QuantConnect.Symbol, str], time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the FuturesChain class
        
        :param canonicalFutureSymbol: The symbol for this chain.
        :param time: The time of this chain
        """
        ...

    @overload
    def __init__(self, canonicalFutureSymbol: typing.Union[QuantConnect.Symbol, str], time: typing.Union[datetime.datetime, datetime.date], trades: System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData], quotes: System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData], contracts: System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.FuturesContract], filteredContracts: System.Collections.Generic.IEnumerable[QuantConnect.Symbol]) -> None:
        """
        Initializes a new instance of the FuturesChain class
        
        :param canonicalFutureSymbol: The symbol for this chain.
        :param time: The time of this chain
        :param trades: All trade data for the entire futures chain
        :param quotes: All quote data for the entire futures chain
        :param contracts: All contracts for this futures chain
        :param filteredContracts: The filtered list of contracts for this futures chain
        """
        ...

    def Clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :returns: A clone of the current object.
        """
        ...

    @overload
    def GetAux(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect_Data_Market_FuturesChain_GetAux_T:
        """
        Gets the auxiliary data with the specified type and symbol
        
        :param symbol: The symbol of the auxiliary data
        :returns: The last auxiliary data with the specified type and symbol.
        """
        ...

    @overload
    def GetAux(self) -> QuantConnect.Data.Market.DataDictionary[QuantConnect_Data_Market_FuturesChain_GetAux_T]:
        """
        Gets all auxiliary data of the specified type as a dictionary keyed by symbol
        
        :returns: A dictionary containing all auxiliary data of the specified type.
        """
        ...

    @overload
    def GetAuxList(self) -> System.Collections.Generic.Dictionary[QuantConnect.Symbol, System.Collections.Generic.List[QuantConnect.Data.BaseData]]:
        """
        Gets all auxiliary data of the specified type as a dictionary keyed by symbol
        
        :returns: A dictionary containing all auxiliary data of the specified type.
        """
        ...

    @overload
    def GetAuxList(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> System.Collections.Generic.List[QuantConnect_Data_Market_FuturesChain_GetAuxList_T]:
        """
        Gets a list of auxiliary data with the specified type and symbol
        
        :param symbol: The symbol of the auxiliary data
        :returns: The list of auxiliary data with the specified type and symbol.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.Market.FuturesContract]:
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


class FuturesChains(QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.FuturesChain]):
    """Collection of FuturesChain keyed by canonical futures symbol"""

    @overload
    def __getitem__(self, ticker: str) -> QuantConnect.Data.Market.FuturesChain:
        """
        Gets or sets the FuturesChain with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The FuturesChain with the specified ticker.
        """
        ...

    @overload
    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Market.FuturesChain:
        """
        Gets or sets the FuturesChain with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The FuturesChain with the specified Symbol.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new instance of the FuturesChains dictionary"""
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """Creates a new instance of the FuturesChains dictionary"""
        ...

    @overload
    def __setitem__(self, ticker: str, value: QuantConnect.Data.Market.FuturesChain) -> None:
        """
        Gets or sets the FuturesChain with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The FuturesChain with the specified ticker.
        """
        ...

    @overload
    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Data.Market.FuturesChain) -> None:
        """
        Gets or sets the FuturesChain with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The FuturesChain with the specified Symbol.
        """
        ...


class BarDirection(System.Enum):
    """Enum for Bar Direction"""

    Rising = 0
    """Rising bar (0)"""

    NoDelta = 1
    """No change (1)"""

    Falling = 2
    """Falling bar (2)"""


class SymbolChangedEvent(QuantConnect.Data.BaseData):
    """
    Symbol changed event of a security. This is generated when a symbol is remapped for a given
    security, for example, at EOD 2014.04.02 GOOG turned into GOOGL, but are the same
    """

    @property
    def OldSymbol(self) -> str:
        """Gets the symbol before the change"""
        ...

    @OldSymbol.setter
    def OldSymbol(self, value: str):
        """Gets the symbol before the change"""
        ...

    @property
    def NewSymbol(self) -> str:
        """Gets the symbol after the change"""
        ...

    @NewSymbol.setter
    def NewSymbol(self, value: str):
        """Gets the symbol after the change"""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new default instance of the SymbolChangedEvent class"""
        ...

    @overload
    def __init__(self, requestedSymbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date], oldSymbol: str, newSymbol: str) -> None:
        """
        Initializes a new instance of the SymbolChangedEvent
        
        :param requestedSymbol: The symbol that was originally requested
        :param date: The date/time this symbol remapping took place
        :param oldSymbol: The old symbol mapping
        :param newSymbol: The new symbol mapping
        """
        ...

    def Clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :returns: A clone of the current object.
        """
        ...

    def ToString(self) -> str:
        """Friendly string representation of this symbol changed event"""
        ...


class SymbolChangedEvents(QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.SymbolChangedEvent]):
    """Collection of SymbolChangedEvent keyed by the original, requested symbol"""

    @overload
    def __getitem__(self, ticker: str) -> QuantConnect.Data.Market.SymbolChangedEvent:
        """
        Gets or sets the SymbolChangedEvent with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The SymbolChangedEvent with the specified ticker.
        """
        ...

    @overload
    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Market.SymbolChangedEvent:
        """
        Gets or sets the SymbolChangedEvent with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The SymbolChangedEvent with the specified Symbol.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the SymbolChangedEvent dictionary"""
        ...

    @overload
    def __init__(self, frontier: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the SymbolChangedEvent dictionary
        
        :param frontier: The time associated with the data in this dictionary
        """
        ...

    @overload
    def __setitem__(self, ticker: str, value: QuantConnect.Data.Market.SymbolChangedEvent) -> None:
        """
        Gets or sets the SymbolChangedEvent with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The SymbolChangedEvent with the specified ticker.
        """
        ...

    @overload
    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Data.Market.SymbolChangedEvent) -> None:
        """
        Gets or sets the SymbolChangedEvent with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The SymbolChangedEvent with the specified Symbol.
        """
        ...


class OptionContracts(QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.OptionContract]):
    """Collection of OptionContract keyed by option symbol"""

    @overload
    def __getitem__(self, ticker: str) -> QuantConnect.Data.Market.OptionContract:
        """
        Gets or sets the OptionContract with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The OptionContract with the specified ticker.
        """
        ...

    @overload
    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Market.OptionContract:
        """
        Gets or sets the OptionContract with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The OptionContract with the specified Symbol.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new instance of the OptionContracts dictionary"""
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """Creates a new instance of the OptionContracts dictionary"""
        ...

    @overload
    def __setitem__(self, ticker: str, value: QuantConnect.Data.Market.OptionContract) -> None:
        """
        Gets or sets the OptionContract with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The OptionContract with the specified ticker.
        """
        ...

    @overload
    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Data.Market.OptionContract) -> None:
        """
        Gets or sets the OptionContract with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The OptionContract with the specified Symbol.
        """
        ...


class OptionChain(QuantConnect.Data.BaseData, typing.Iterable[QuantConnect.Data.Market.OptionContract]):
    """
    Represents an entire chain of option contracts for a single underying security.
    This type is IEnumerable{OptionContract}
    """

    @property
    def Underlying(self) -> QuantConnect.Data.BaseData:
        """
        Gets the most recent trade information for the underlying. This may
        be a Tick or a TradeBar
        """
        ...

    @Underlying.setter
    def Underlying(self, value: QuantConnect.Data.BaseData):
        """
        Gets the most recent trade information for the underlying. This may
        be a Tick or a TradeBar
        """
        ...

    @property
    def Ticks(self) -> QuantConnect.Data.Market.Ticks:
        """Gets all ticks for every option contract in this chain, keyed by option symbol"""
        ...

    @Ticks.setter
    def Ticks(self, value: QuantConnect.Data.Market.Ticks):
        """Gets all ticks for every option contract in this chain, keyed by option symbol"""
        ...

    @property
    def TradeBars(self) -> QuantConnect.Data.Market.TradeBars:
        """Gets all trade bars for every option contract in this chain, keyed by option symbol"""
        ...

    @TradeBars.setter
    def TradeBars(self, value: QuantConnect.Data.Market.TradeBars):
        """Gets all trade bars for every option contract in this chain, keyed by option symbol"""
        ...

    @property
    def QuoteBars(self) -> QuantConnect.Data.Market.QuoteBars:
        """Gets all quote bars for every option contract in this chain, keyed by option symbol"""
        ...

    @QuoteBars.setter
    def QuoteBars(self, value: QuantConnect.Data.Market.QuoteBars):
        """Gets all quote bars for every option contract in this chain, keyed by option symbol"""
        ...

    @property
    def Contracts(self) -> QuantConnect.Data.Market.OptionContracts:
        """Gets all contracts in the chain, keyed by option symbol"""
        ...

    @Contracts.setter
    def Contracts(self, value: QuantConnect.Data.Market.OptionContracts):
        """Gets all contracts in the chain, keyed by option symbol"""
        ...

    @property
    def FilteredContracts(self) -> System.Collections.Generic.HashSet[QuantConnect.Symbol]:
        """Gets the set of symbols that passed the Option.ContractFilter"""
        ...

    @FilteredContracts.setter
    def FilteredContracts(self, value: System.Collections.Generic.HashSet[QuantConnect.Symbol]):
        """Gets the set of symbols that passed the Option.ContractFilter"""
        ...

    @overload
    def __init__(self, canonicalOptionSymbol: typing.Union[QuantConnect.Symbol, str], time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the OptionChain class
        
        :param canonicalOptionSymbol: The symbol for this chain.
        :param time: The time of this chain
        """
        ...

    @overload
    def __init__(self, canonicalOptionSymbol: typing.Union[QuantConnect.Symbol, str], time: typing.Union[datetime.datetime, datetime.date], underlying: QuantConnect.Data.BaseData, trades: System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData], quotes: System.Collections.Generic.IEnumerable[QuantConnect.Data.BaseData], contracts: System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.OptionContract], filteredContracts: System.Collections.Generic.IEnumerable[QuantConnect.Symbol]) -> None:
        """
        Initializes a new instance of the OptionChain class
        
        :param canonicalOptionSymbol: The symbol for this chain.
        :param time: The time of this chain
        :param underlying: The most recent underlying trade data
        :param trades: All trade data for the entire option chain
        :param quotes: All quote data for the entire option chain
        :param contracts: All contracts for this option chain
        :param filteredContracts: The filtered list of contracts for this option chain
        """
        ...

    def Clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :returns: A clone of the current object.
        """
        ...

    @overload
    def GetAux(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect_Data_Market_OptionChain_GetAux_T:
        """
        Gets the auxiliary data with the specified type and symbol
        
        :param symbol: The symbol of the auxiliary data
        :returns: The last auxiliary data with the specified type and symbol.
        """
        ...

    @overload
    def GetAux(self) -> QuantConnect.Data.Market.DataDictionary[QuantConnect_Data_Market_OptionChain_GetAux_T]:
        """
        Gets all auxiliary data of the specified type as a dictionary keyed by symbol
        
        :returns: A dictionary containing all auxiliary data of the specified type.
        """
        ...

    @overload
    def GetAuxList(self) -> System.Collections.Generic.Dictionary[QuantConnect.Symbol, System.Collections.Generic.List[QuantConnect.Data.BaseData]]:
        """
        Gets all auxiliary data of the specified type as a dictionary keyed by symbol
        
        :returns: A dictionary containing all auxiliary data of the specified type.
        """
        ...

    @overload
    def GetAuxList(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> System.Collections.Generic.List[QuantConnect_Data_Market_OptionChain_GetAuxList_T]:
        """
        Gets a list of auxiliary data with the specified type and symbol
        
        :param symbol: The symbol of the auxiliary data
        :returns: The list of auxiliary data with the specified type and symbol.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.Market.OptionContract]:
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


class OptionChains(QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.OptionChain]):
    """Collection of OptionChain keyed by canonical option symbol"""

    @overload
    def __getitem__(self, ticker: str) -> QuantConnect.Data.Market.OptionChain:
        """
        Gets or sets the OptionChain with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The OptionChain with the specified ticker.
        """
        ...

    @overload
    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Market.OptionChain:
        """
        Gets or sets the OptionChain with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The OptionChain with the specified Symbol.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new instance of the OptionChains dictionary"""
        ...

    @overload
    def __init__(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """Creates a new instance of the OptionChains dictionary"""
        ...

    @overload
    def __setitem__(self, ticker: str, value: QuantConnect.Data.Market.OptionChain) -> None:
        """
        Gets or sets the OptionChain with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The OptionChain with the specified ticker.
        """
        ...

    @overload
    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Data.Market.OptionChain) -> None:
        """
        Gets or sets the OptionChain with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The OptionChain with the specified Symbol.
        """
        ...


class RenkoBar(QuantConnect.Data.BaseData, QuantConnect.Data.Market.IBaseDataBar):
    """Represents a bar sectioned not by time, but by some amount of movement in a value (for example, Closing price moving in $10 bar sizes)"""

    @property
    def Type(self) -> int:
        """
        Gets the kind of the bar
        
        This property contains the int value of a member of the QuantConnect.Data.Market.RenkoType enum.
        """
        ...

    @Type.setter
    def Type(self, value: int):
        """
        Gets the kind of the bar
        
        This property contains the int value of a member of the QuantConnect.Data.Market.RenkoType enum.
        """
        ...

    @property
    def BrickSize(self) -> float:
        """Gets the height of the bar"""
        ...

    @BrickSize.setter
    def BrickSize(self, value: float):
        """Gets the height of the bar"""
        ...

    @property
    def Open(self) -> float:
        """Gets the opening value that started this bar."""
        ...

    @Open.setter
    def Open(self, value: float):
        """Gets the opening value that started this bar."""
        ...

    @property
    def Close(self) -> float:
        """Gets the closing value or the current value if the bar has not yet closed."""
        ...

    @Close.setter
    def Close(self, value: float):
        """Gets the closing value or the current value if the bar has not yet closed."""
        ...

    @property
    def High(self) -> float:
        """Gets the highest value encountered during this bar"""
        ...

    @High.setter
    def High(self, value: float):
        """Gets the highest value encountered during this bar"""
        ...

    @property
    def Low(self) -> float:
        """Gets the lowest value encountered during this bar"""
        ...

    @Low.setter
    def Low(self, value: float):
        """Gets the lowest value encountered during this bar"""
        ...

    @property
    def Volume(self) -> float:
        """Gets the volume of trades during the bar."""
        ...

    @Volume.setter
    def Volume(self, value: float):
        """Gets the volume of trades during the bar."""
        ...

    @property
    def EndTime(self) -> datetime.datetime:
        """Gets the end time of this renko bar or the most recent update time if it IsClosed"""
        ...

    @EndTime.setter
    def EndTime(self, value: datetime.datetime):
        """Gets the end time of this renko bar or the most recent update time if it IsClosed"""
        ...

    @property
    def End(self) -> datetime.datetime:
        """
        Gets the end time of this renko bar or the most recent update time if it IsClosed
        
        RenkoBar.End is obsolete. Please use RenkoBar.EndTime property instead.
        """
        warnings.warn("RenkoBar.End is obsolete. Please use RenkoBar.EndTime property instead.", DeprecationWarning)

    @End.setter
    def End(self, value: datetime.datetime):
        """
        Gets the end time of this renko bar or the most recent update time if it IsClosed
        
        RenkoBar.End is obsolete. Please use RenkoBar.EndTime property instead.
        """
        warnings.warn("RenkoBar.End is obsolete. Please use RenkoBar.EndTime property instead.", DeprecationWarning)

    @property
    def Start(self) -> datetime.datetime:
        """Gets the time this bar started"""
        ...

    @Start.setter
    def Start(self, value: datetime.datetime):
        """Gets the time this bar started"""
        ...

    @property
    def IsClosed(self) -> bool:
        """Gets whether or not this bar is considered closed."""
        ...

    @IsClosed.setter
    def IsClosed(self, value: bool):
        """Gets whether or not this bar is considered closed."""
        ...

    @property
    def Direction(self) -> int:
        """
        The trend of the bar (i.e. Rising, Falling or NoDelta)
        
        This property contains the int value of a member of the QuantConnect.Data.Market.BarDirection enum.
        """
        ...

    @property
    def Spread(self) -> float:
        """The "spread" of the bar"""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new default instance of the RenkoBar class."""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], time: typing.Union[datetime.datetime, datetime.date], brickSize: float, open: float, volume: float) -> None:
        """
        Initializes a new instance of the RenkoBar class with the specified values
        
        :param symbol: The symbol of this data
        :param time: The start time of the bar
        :param brickSize: The size of each renko brick
        :param open: The opening price for the new bar
        :param volume: Any initial volume associated with the data
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], start: typing.Union[datetime.datetime, datetime.date], endTime: typing.Union[datetime.datetime, datetime.date], brickSize: float, open: float, high: float, low: float, close: float) -> None:
        """
        Initializes a new instance of the RenkoBar class with the specified values
        
        :param symbol: The symbol of this data
        :param start: The start time of the bar
        :param endTime: The end time of the bar
        :param brickSize: The size of each wicko brick
        :param open: The opening price for the new bar
        :param high: The high price for the new bar
        :param low: The low price for the new bar
        :param close: The closing price for the new bar
        """
        ...

    def Clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :returns: A clone of the current object.
        """
        ...

    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the URL string source of the file. This will be converted to a stream
        
        :param config: Configuration object
        :param date: Date of this source file
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: String URL of source file.
        """
        ...

    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader Method :: using set of arguements we specify read out type. Enumerate
        until the end of the data stream or file. E.g. Read CSV file line by line and convert
        into data types.
        
        :param config: Config.
        :param line: Line.
        :param date: Date.
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: BaseData type set by Subscription Method.
        """
        ...

    def Update(self, time: typing.Union[datetime.datetime, datetime.date], currentValue: float, volumeSinceLastUpdate: float) -> bool:
        """
        Updates this RenkoBar with the specified values and returns whether or not this bar is closed
        
        :param time: The current time
        :param currentValue: The current value
        :param volumeSinceLastUpdate: The volume since the last update called on this instance
        :returns: True if this bar IsClosed.
        """
        ...


class RenkoType(System.Enum):
    """
    The type of the RenkoBar being created.
    Used by RenkoConsolidator and ClassicRenkoConsolidator
    """

    Classic = 0
    """
    Indicates that the RenkoConsolidator works in its
    original implementation; Specifically:
    - It only returns a single bar, at most, irrespective of tick movement
    - It will emit consecutive bars side by side
    - By default even bars are created
    (0)
    """

    Wicked = 1
    """
    Indicates that the RenkoConsolidator works properly;
    Specifically:
    - returns zero or more bars per tick, as appropriate.
    - Will not emit consecutive bars side by side
    - Creates
    (1)
    """


class Split(QuantConnect.Data.BaseData):
    """Split event from a security"""

    @property
    def Type(self) -> int:
        """
        Gets the type of split event, warning or split.
        
        This property contains the int value of a member of the QuantConnect.SplitType enum.
        """
        ...

    @Type.setter
    def Type(self, value: int):
        """
        Gets the type of split event, warning or split.
        
        This property contains the int value of a member of the QuantConnect.SplitType enum.
        """
        ...

    @property
    def SplitFactor(self) -> float:
        """Gets the split factor"""
        ...

    @SplitFactor.setter
    def SplitFactor(self, value: float):
        """Gets the split factor"""
        ...

    @property
    def ReferencePrice(self) -> float:
        """
        Gets the price at which the split occurred
        This is typically the previous day's closing price
        """
        ...

    @ReferencePrice.setter
    def ReferencePrice(self, value: float):
        """
        Gets the price at which the split occurred
        This is typically the previous day's closing price
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Split class"""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date], price: float, splitFactor: float, type: QuantConnect.SplitType) -> None:
        """
        Initializes a new instance of the Split class
        
        :param symbol: The symbol
        :param date: The date
        :param price: The price at the time of the split
        :param splitFactor: The split factor to be applied to current holdings
        :param type: The type of split event, warning or split occurred
        """
        ...

    def Clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :returns: A clone of the current object.
        """
        ...

    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the URL string source of the file. This will be converted to a stream
        
        :param config: Configuration object
        :param date: Date of this source file
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: String URL of source file.
        """
        ...

    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects. Each data type creates its own factory method, and returns a new instance of the object
        each time it is called.
        
        :param config: Subscription data config setup object
        :param line: Line of the source document
        :param date: Date of the requested data
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: Instance of the T:BaseData object generated by this line of the CSV.
        """
        ...

    def ToString(self) -> str:
        """
        Formats a string with the symbol and value.
        
        :returns: string - a string formatted as SPY: 167.753.
        """
        ...


class Splits(QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.Split]):
    """Collection of splits keyed by Symbol"""

    @overload
    def __getitem__(self, ticker: str) -> QuantConnect.Data.Market.Split:
        """
        Gets or sets the Split with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The Split with the specified ticker.
        """
        ...

    @overload
    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Market.Split:
        """
        Gets or sets the Split with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The Split with the specified Symbol.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Splits dictionary"""
        ...

    @overload
    def __init__(self, frontier: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the Splits dictionary
        
        :param frontier: The time associated with the data in this dictionary
        """
        ...

    @overload
    def __setitem__(self, ticker: str, value: QuantConnect.Data.Market.Split) -> None:
        """
        Gets or sets the Split with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The Split with the specified ticker.
        """
        ...

    @overload
    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Data.Market.Split) -> None:
        """
        Gets or sets the Split with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The Split with the specified Symbol.
        """
        ...


class Dividend(QuantConnect.Data.BaseData):
    """Dividend event from a security"""

    @property
    def Distribution(self) -> float:
        """Gets the dividend payment"""
        ...

    @Distribution.setter
    def Distribution(self, value: float):
        """Gets the dividend payment"""
        ...

    @property
    def ReferencePrice(self) -> float:
        """
        Gets the price at which the dividend occurred.
        This is typically the previous day's closing price
        """
        ...

    @ReferencePrice.setter
    def ReferencePrice(self, value: float):
        """
        Gets the price at which the dividend occurred.
        This is typically the previous day's closing price
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Dividend class"""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date], distribution: float, referencePrice: float) -> None:
        """
        Initializes a new instance of the Dividend class
        
        :param symbol: The symbol
        :param date: The date
        :param distribution: The dividend amount
        :param referencePrice: The previous day's closing price
        """
        ...

    def Clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :returns: A clone of the current object.
        """
        ...

    @staticmethod
    def ComputeDistribution(close: float, priceFactorRatio: float, decimalPlaces: int) -> float:
        """
        Computes the price factor ratio given the previous day's closing price and the p
        
        :param close: Previous day's closing price
        :param priceFactorRatio: Price factor ratio pf_i/pf_i+1
        :param decimalPlaces: The number of decimal places to round the result to, defaulting to 2
        :returns: The distribution rounded to the specified number of decimal places, defaulting to 2.
        """
        ...

    @staticmethod
    def Create(symbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date], referencePrice: float, priceFactorRatio: float, decimalPlaces: int = 2) -> QuantConnect.Data.Market.Dividend:
        """
        Initializes a new instance of the Dividend class
        
        :param symbol: The symbol
        :param date: The date
        :param referencePrice: The previous day's closing price
        :param priceFactorRatio: The ratio of the price factors, pf_i/pf_i+1
        :param decimalPlaces: The number of decimal places to round the dividend's distribution to, defaulting to 2
        """
        ...

    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the URL string source of the file. This will be converted to a stream
        
        :param config: Configuration object
        :param date: Date of this source file
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: String URL of source file.
        """
        ...

    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects. Each data type creates its own factory method, and returns a new instance of the object
        each time it is called.
        
        :param config: Subscription data config setup object
        :param line: Line of the source document
        :param date: Date of the requested data
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: Instance of the T:BaseData object generated by this line of the CSV.
        """
        ...

    def ToString(self) -> str:
        """
        Formats a string with the symbol and value.
        
        :returns: string - a string formatted as SPY: 167.753.
        """
        ...


class DataDictionaryExtensions(System.Object):
    """Provides extension methods for the DataDictionary class"""

    @staticmethod
    def Add(dictionary: QuantConnect.Data.Market.DataDictionary[QuantConnect_Data_Market_DataDictionaryExtensions_Add_T], data: QuantConnect_Data_Market_DataDictionaryExtensions_Add_T) -> None:
        """Provides a convenience method for adding a base data instance to our data dictionary"""
        ...


class Delisting(QuantConnect.Data.BaseData):
    """Delisting event of a security"""

    @property
    def Type(self) -> int:
        """
        Gets the type of delisting, warning or delisted
        A DelistingType.Warning is sent
        
        This property contains the int value of a member of the QuantConnect.DelistingType enum.
        """
        ...

    @Type.setter
    def Type(self, value: int):
        """
        Gets the type of delisting, warning or delisted
        A DelistingType.Warning is sent
        
        This property contains the int value of a member of the QuantConnect.DelistingType enum.
        """
        ...

    @property
    def Ticket(self) -> QuantConnect.Orders.OrderTicket:
        """Gets the OrderTicket that was submitted to liquidate this position"""
        ...

    @Ticket.setter
    def Ticket(self, value: QuantConnect.Orders.OrderTicket):
        """Gets the OrderTicket that was submitted to liquidate this position"""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Delisting class"""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date], price: float, type: QuantConnect.DelistingType) -> None:
        """
        Initializes a new instance of the Delisting class
        
        :param symbol: The delisted symbol
        :param date: The date the symbol was delisted
        :param price: The final price before delisting
        :param type: The type of delisting event
        """
        ...

    def Clone(self) -> QuantConnect.Data.BaseData:
        """
        Return a new instance clone of this object, used in fill forward
        
        :returns: A clone of the current object.
        """
        ...

    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the URL string source of the file. This will be converted to a stream
        
        :param config: Configuration object
        :param date: Date of this source file
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: String URL of source file.
        """
        ...

    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects. Each data type creates its own factory method, and returns a new instance of the object
        each time it is called.
        
        :param config: Subscription data config setup object
        :param line: Line of the source document
        :param date: Date of the requested data
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: Instance of the T:BaseData object generated by this line of the CSV.
        """
        ...

    def SetOrderTicket(self, ticket: QuantConnect.Orders.OrderTicket) -> None:
        """
        Sets the OrderTicket used to liquidate this position
        
        :param ticket: The ticket that represents the order to liquidate this position
        """
        ...

    def ToString(self) -> str:
        """
        Formats a string with the symbol and value.
        
        :returns: string - a string formatted as SPY: 167.753.
        """
        ...


class Delistings(QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.Delisting]):
    """Collections of Delisting keyed by Symbol"""

    @overload
    def __getitem__(self, ticker: str) -> QuantConnect.Data.Market.Delisting:
        """
        Gets or sets the Delisting with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The Delisting with the specified ticker.
        """
        ...

    @overload
    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Market.Delisting:
        """
        Gets or sets the Delisting with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The Delisting with the specified Symbol.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Delistings dictionary"""
        ...

    @overload
    def __init__(self, frontier: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the Delistings dictionary
        
        :param frontier: The time associated with the data in this dictionary
        """
        ...

    @overload
    def __setitem__(self, ticker: str, value: QuantConnect.Data.Market.Delisting) -> None:
        """
        Gets or sets the Delisting with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The Delisting with the specified ticker.
        """
        ...

    @overload
    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Data.Market.Delisting) -> None:
        """
        Gets or sets the Delisting with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The Delisting with the specified Symbol.
        """
        ...


class Dividends(QuantConnect.Data.Market.DataDictionary[QuantConnect.Data.Market.Dividend]):
    """Collection of dividends keyed by Symbol"""

    @overload
    def __getitem__(self, ticker: str) -> QuantConnect.Data.Market.Dividend:
        """
        Gets or sets the Dividend with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The Dividend with the specified ticker.
        """
        ...

    @overload
    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Data.Market.Dividend:
        """
        Gets or sets the Dividend with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The Dividend with the specified Symbol.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Dividends dictionary"""
        ...

    @overload
    def __init__(self, frontier: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the Dividends dictionary
        
        :param frontier: The time associated with the data in this dictionary
        """
        ...

    @overload
    def __setitem__(self, ticker: str, value: QuantConnect.Data.Market.Dividend) -> None:
        """
        Gets or sets the Dividend with the specified ticker.
        
        :param ticker: The ticker of the element to get or set.
        :returns: The Dividend with the specified ticker.
        """
        ...

    @overload
    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: QuantConnect.Data.Market.Dividend) -> None:
        """
        Gets or sets the Dividend with the specified Symbol.
        
        :param symbol: The Symbol of the element to get or set.
        :returns: The Dividend with the specified Symbol.
        """
        ...


