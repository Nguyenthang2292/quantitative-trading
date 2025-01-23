from typing import overload
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Securities
import QuantConnect.Securities.Index
import System


class IndexDataFilter(QuantConnect.Securities.SecurityDataFilter):
    """Index packet by packet data filtering mechanism for dynamically detecting bad ticks."""


class IndexSymbol(System.Object):
    """Helper methods for Index Symbols"""

    @staticmethod
    def GetIndexExchange(symbol: typing.Union[QuantConnect.Symbol, str]) -> str:
        """
        Gets the actual exchange the index lives on
        
        :returns: The market of the index.
        """
        ...


class IndexCache(QuantConnect.Securities.SecurityCache):
    """INDEX specific caching support"""


class Index(QuantConnect.Securities.Security):
    """INDEX Security Object Implementation for INDEX Assets"""

    @property
    def IsTradable(self) -> bool:
        """Gets or sets whether or not this security should be considered tradable"""
        ...

    @IsTradable.setter
    def IsTradable(self, value: bool):
        """Gets or sets whether or not this security should be considered tradable"""
        ...

    @overload
    def __init__(self, exchangeHours: QuantConnect.Securities.SecurityExchangeHours, quoteCurrency: QuantConnect.Securities.Cash, config: QuantConnect.Data.SubscriptionDataConfig, symbolProperties: QuantConnect.Securities.SymbolProperties, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypes: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider) -> None:
        """
        Constructor for the INDEX security
        
        :param exchangeHours: Defines the hours this exchange is open
        :param quoteCurrency: The cash object that represent the quote currency
        :param config: The subscription configuration for this security
        :param symbolProperties: The symbol properties for this security
        :param currencyConverter: Currency converter used to convert CashAmount instances into units of the account currency
        :param registeredTypes: Provides all data types registered in the algorithm
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], exchangeHours: QuantConnect.Securities.SecurityExchangeHours, quoteCurrency: QuantConnect.Securities.Cash, symbolProperties: QuantConnect.Securities.SymbolProperties, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypes: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, securityCache: QuantConnect.Securities.SecurityCache) -> None:
        """
        Constructor for the INDEX security
        
        :param symbol: The security's symbol
        :param exchangeHours: Defines the hours this exchange is open
        :param quoteCurrency: The cash object that represent the quote currency
        :param symbolProperties: The symbol properties for this security
        :param currencyConverter: Currency converter used to convert CashAmount instances into units of the account currency
        :param registeredTypes: Provides all data types registered in the algorithm
        :param securityCache: Cache to store security information
        """
        ...


class IndexHolding(QuantConnect.Securities.SecurityHolding):
    """Index holdings implementation of the base securities class"""

    def __init__(self, security: QuantConnect.Securities.Index.Index, currencyConverter: QuantConnect.Securities.ICurrencyConverter) -> None:
        """
        INDEX Holding Class constructor
        
        :param security: The INDEX security being held
        :param currencyConverter: A currency converter instance
        """
        ...


class IndexExchange(QuantConnect.Securities.SecurityExchange):
    """INDEX exchange class - information and helper tools for Index exchange properties"""

    @property
    def TradingDaysPerYear(self) -> int:
        """Number of trading days per year for this security, used for performance statistics."""
        ...

    def __init__(self, exchangeHours: QuantConnect.Securities.SecurityExchangeHours) -> None:
        """
        Initializes a new instance of the IndexExchange class using the specified
        exchange hours to determine open/close times
        
        :param exchangeHours: Contains the weekly exchange schedule plus holidays
        """
        ...


