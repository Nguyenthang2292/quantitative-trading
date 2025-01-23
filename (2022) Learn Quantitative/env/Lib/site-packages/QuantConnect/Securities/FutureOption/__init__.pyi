from typing import overload
import datetime
import typing

import QuantConnect
import QuantConnect.Securities
import QuantConnect.Securities.FutureOption
import QuantConnect.Securities.Option
import System


class FutureOptionSymbol(System.Object):
    """Static helper methods to resolve Futures Options Symbol-related tasks."""

    @staticmethod
    def GetLastDayOfTrading(symbol: typing.Union[QuantConnect.Symbol, str]) -> datetime.datetime:
        """
        Gets the last day of trading, aliased to be the Futures options' expiry
        
        :param symbol: Futures Options Symbol
        :returns: Last day of trading date.
        """
        ...

    @staticmethod
    def IsStandard(_: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Detects if the future option contract is standard, i.e. not weekly, not short-term, not mid-sized, etc.
        
        :param _: Symbol
        :returns: true.
        """
        ...


class FutureOption(QuantConnect.Securities.Option.Option):
    """Futures Options security"""

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], exchangeHours: QuantConnect.Securities.SecurityExchangeHours, quoteCurrency: QuantConnect.Securities.Cash, symbolProperties: QuantConnect.Securities.Option.OptionSymbolProperties, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypes: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, securityCache: QuantConnect.Securities.SecurityCache, underlying: QuantConnect.Securities.Security) -> None:
        """
        Constructor for the future option security
        
        :param symbol: Symbol of the future option
        :param exchangeHours: Exchange hours of the future option
        :param quoteCurrency: Quoted currency of the future option
        :param symbolProperties: Symbol properties of the future option
        :param currencyConverter: Currency converter
        :param registeredTypes: Provides all data types registered to the algorithm
        :param securityCache: Cache of security objects
        :param underlying: Future underlying security
        """
        ...


class FuturesOptionsUnderlyingMapper(System.Object):
    """Creates the underlying Symbol that corresponds to a futures options contract"""

    @staticmethod
    def GetUnderlyingFutureFromFutureOption(futureOptionTicker: str, market: str, futureOptionExpiration: typing.Union[datetime.datetime, datetime.date], date: typing.Optional[datetime.datetime] = None) -> QuantConnect.Symbol:
        """
        Gets the FOP's underlying Future. The underlying Future's contract month might not match
        the contract month of the Future Option when providing CBOT or COMEX based FOPs contracts to this method.
        
        :param futureOptionTicker: Future option ticker
        :param market: Market of the Future Option
        :param futureOptionExpiration: Expiration date of the future option
        :param date: Date to search the future chain provider with. Optional, but required for CBOT based contracts
        :returns: Symbol if there is an underlying for the FOP, null if there's no underlying found for the Future Option.
        """
        ...


class FuturesOptionsExpiryFunctions(System.Object):
    """Futures options expiry lookup utility class"""

    @staticmethod
    def FuturesOptionExpiry(canonicalFutureOptionSymbol: typing.Union[QuantConnect.Symbol, str], futureContractMonth: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """
        Gets the Futures Options' expiry for the given contract month.
        
        :param canonicalFutureOptionSymbol: Canonical Futures Options Symbol. Will be made canonical if not provided a canonical
        :param futureContractMonth: Contract month of the underlying Future
        :returns: Expiry date/time.
        """
        ...

    @staticmethod
    def GetFutureOptionExpiryFromFutureExpiry(futureSymbol: typing.Union[QuantConnect.Symbol, str], canonicalFutureOption: typing.Union[QuantConnect.Symbol, str] = None) -> datetime.datetime:
        """
        Gets the Future Option's expiry from the Future Symbol provided
        
        :param futureSymbol: Future (non-canonical) Symbol
        :param canonicalFutureOption: The canonical Future Option Symbol
        :returns: Future Option Expiry for the Future with the same contract month.
        """
        ...


class CMEStrikePriceScalingFactors(System.Object):
    """Provides a means to get the scaling factor for CME's quotes API"""

    @staticmethod
    def GetScaleFactor(underlyingFuture: typing.Union[QuantConnect.Symbol, str]) -> float:
        """
        Gets the option chain strike price scaling factor for the quote response from CME
        
        :param underlyingFuture: Underlying future Symbol to normalize
        :returns: Scaling factor for the strike price.
        """
        ...


