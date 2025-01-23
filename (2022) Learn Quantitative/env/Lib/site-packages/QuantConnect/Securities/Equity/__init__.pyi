from typing import overload
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Securities
import QuantConnect.Securities.Equity


class EquityHolding(QuantConnect.Securities.SecurityHolding):
    """Holdings class for equities securities: no specific properties here but it is a placeholder for future equities specific behaviours."""

    def __init__(self, security: QuantConnect.Securities.Security, currencyConverter: QuantConnect.Securities.ICurrencyConverter) -> None:
        """
        Constructor for equities holdings.
        
        :param security: The security being held
        :param currencyConverter: A currency converter instance
        """
        ...


class EquityDataFilter(QuantConnect.Securities.SecurityDataFilter):
    """Equity security type data filter"""

    def __init__(self) -> None:
        """Initialize Data Filter Class:"""
        ...

    def Filter(self, vehicle: QuantConnect.Securities.Security, data: QuantConnect.Data.BaseData) -> bool:
        """
        Equity filter the data: true - accept, false - fail.
        
        :param vehicle: Security asset
        :param data: Data class
        """
        ...


class EquityCache(QuantConnect.Securities.SecurityCache):
    """Equity cache override."""

    def __init__(self) -> None:
        """Start a new Cache for the set Index Code"""
        ...


class EquityExchange(QuantConnect.Securities.SecurityExchange):
    """Equity exchange information"""

    @property
    def TradingDaysPerYear(self) -> int:
        """Number of trading days in an equity calendar year - 252"""
        ...

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the EquityExchange class using market hours
        derived from the market-hours-database for the USA Equity market
        """
        ...

    @overload
    def __init__(self, exchangeHours: QuantConnect.Securities.SecurityExchangeHours) -> None:
        """
        Initializes a new instance of the EquityExchange class using the specified
        exchange hours to determine open/close times
        
        :param exchangeHours: Contains the weekly exchange schedule plus holidays
        """
        ...


class Equity(QuantConnect.Securities.Security):
    """Equity Security Type : Extension of the underlying Security class for equity specific behaviours."""

    DefaultSettlementDays: int = 3
    """The default number of days required to settle an equity sale"""

    DefaultSettlementTime: datetime.timedelta = ...
    """The default time of day for settlement"""

    @property
    def Shortable(self) -> bool:
        """
        Checks if the equity is a shortable asset. Note that this does not
        take into account any open orders or existing holdings. To check if the asset
        is currently shortable, use QCAlgorithm's ShortableQuantity property instead.
        """
        ...

    @property
    def TotalShortableQuantity(self) -> typing.Optional[int]:
        """
        Gets the total quantity shortable for this security. This does not take into account
        any open orders or existing holdings. To check the asset's currently shortable quantity,
        use QCAlgorithm's ShortableQuantity property instead.
        """
        ...

    @property
    def PrimaryExchange(self) -> QuantConnect.Exchange:
        """Equity primary exchange."""
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], exchangeHours: QuantConnect.Securities.SecurityExchangeHours, quoteCurrency: QuantConnect.Securities.Cash, symbolProperties: QuantConnect.Securities.SymbolProperties, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypes: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, securityCache: QuantConnect.Securities.SecurityCache, primaryExchange: QuantConnect.Exchange = None) -> None:
        """Construct the Equity Object"""
        ...

    @overload
    def __init__(self, exchangeHours: QuantConnect.Securities.SecurityExchangeHours, config: QuantConnect.Data.SubscriptionDataConfig, quoteCurrency: QuantConnect.Securities.Cash, symbolProperties: QuantConnect.Securities.SymbolProperties, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypes: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, primaryExchange: QuantConnect.Exchange = None) -> None:
        """Construct the Equity Object"""
        ...

    def SetDataNormalizationMode(self, mode: QuantConnect.DataNormalizationMode) -> None:
        """Sets the data normalization mode to be used by this security"""
        ...


