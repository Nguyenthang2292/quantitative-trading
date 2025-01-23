from typing import overload
import datetime
import typing

import QuantConnect
import QuantConnect.Data.Shortable
import QuantConnect.Interfaces
import System
import System.Collections.Generic


class LocalDiskShortableProvider(System.Object, QuantConnect.Interfaces.IShortableProvider):
    """Sources easy-to-borrow (ETB) data from the local disk for the given brokerage"""

    def __init__(self, securityType: QuantConnect.SecurityType, brokerage: str, market: str) -> None:
        """
        Creates an instance of the class. Establishes the directory to read from.
        
        :param securityType: SecurityType to read data
        :param brokerage: Brokerage to read ETB data
        :param market: Market to read ETB data
        """
        ...

    def AllShortableSymbols(self, localTime: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.Dictionary[QuantConnect.Symbol, int]:
        """
        Gets a list of all shortable Symbols, including the quantity shortable as a Dictionary.
        
        :param localTime: The algorithm's local time
        :returns: Symbol/quantity shortable as a Dictionary. Returns null if no entry data exists for this date or brokerage.
        """
        ...

    def ShortableQuantity(self, symbol: typing.Union[QuantConnect.Symbol, str], localTime: typing.Union[datetime.datetime, datetime.date]) -> typing.Optional[int]:
        """
        Gets the quantity shortable for the Symbol at the given date.
        
        :param symbol: Symbol to lookup shortable quantity
        :param localTime: Time of the algorithm
        :returns: Quantity shortable. Null if the data for the brokerage/date does not exist.
        """
        ...


class AtreyuShortableProvider(QuantConnect.Data.Shortable.LocalDiskShortableProvider):
    """Defines the default Atreyu Shortable Provider"""

    def __init__(self, securityType: QuantConnect.SecurityType, market: str) -> None:
        """
        Initialize an instance of AtreyuShortableProvider
        
        :param securityType: SecurityType to read data
        :param market: Market to read ETB data
        """
        ...


class NullShortableProvider(System.Object, QuantConnect.Interfaces.IShortableProvider):
    """
    Defines the default shortable provider in the case that no local data exists.
    This will allow for all assets to be infinitely shortable, with no restrictions.
    """

    def AllShortableSymbols(self, localTime: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.Dictionary[QuantConnect.Symbol, int]:
        """
        Gets all shortable Symbols
        
        :param localTime: Time of the algorithm
        :returns: null indicating that all Symbols are shortable.
        """
        ...

    def ShortableQuantity(self, symbol: typing.Union[QuantConnect.Symbol, str], localTime: typing.Union[datetime.datetime, datetime.date]) -> typing.Optional[int]:
        """
        Gets the quantity shortable for the Symbol at the given time.
        
        :param symbol: Symbol to check
        :param localTime: Local time of the algorithm
        :returns: null, indicating that it is infinitely shortable.
        """
        ...


