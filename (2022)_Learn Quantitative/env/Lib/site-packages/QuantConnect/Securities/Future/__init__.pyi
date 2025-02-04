from typing import overload
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Interfaces
import QuantConnect.Securities
import QuantConnect.Securities.Future
import System
import System.Collections.Generic


class Future(QuantConnect.Securities.Security, QuantConnect.Securities.IDerivativeSecurity, QuantConnect.Securities.IContinuousSecurity):
    """Futures Security Object Implementation for Futures Assets"""

    @property
    def IsTradable(self) -> bool:
        """Gets or sets whether or not this security should be considered tradable"""
        ...

    @IsTradable.setter
    def IsTradable(self, value: bool):
        """Gets or sets whether or not this security should be considered tradable"""
        ...

    DefaultSettlementDays: int = 1
    """The default number of days required to settle a futures sale"""

    DefaultSettlementTime: datetime.timedelta = ...
    """The default time of day for settlement"""

    @property
    def IsFutureChain(self) -> bool:
        """Returns true if this is the future chain security, false if it is a specific future contract"""
        ...

    @property
    def IsFutureContract(self) -> bool:
        """Returns true if this is a specific future contract security, false if it is the future chain security"""
        ...

    @property
    def Expiry(self) -> datetime.datetime:
        """Gets the expiration date"""
        ...

    @property
    def SettlementType(self) -> int:
        """
        Specifies if futures contract has physical or cash settlement on settlement
        
        This property contains the int value of a member of the QuantConnect.SettlementType enum.
        """
        ...

    @SettlementType.setter
    def SettlementType(self, value: int):
        """
        Specifies if futures contract has physical or cash settlement on settlement
        
        This property contains the int value of a member of the QuantConnect.SettlementType enum.
        """
        ...

    @property
    def Underlying(self) -> QuantConnect.Securities.Security:
        """Gets or sets the underlying security object."""
        ...

    @Underlying.setter
    def Underlying(self, value: QuantConnect.Securities.Security):
        """Gets or sets the underlying security object."""
        ...

    @property
    def Mapped(self) -> QuantConnect.Symbol:
        """Gets or sets the currently mapped symbol for the security"""
        ...

    @Mapped.setter
    def Mapped(self, value: QuantConnect.Symbol):
        """Gets or sets the currently mapped symbol for the security"""
        ...

    @property
    def ContractFilter(self) -> QuantConnect.Securities.IDerivativeSecurityFilter:
        """Gets or sets the contract filter"""
        ...

    @ContractFilter.setter
    def ContractFilter(self, value: QuantConnect.Securities.IDerivativeSecurityFilter):
        """Gets or sets the contract filter"""
        ...

    @overload
    def __init__(self, exchangeHours: QuantConnect.Securities.SecurityExchangeHours, config: QuantConnect.Data.SubscriptionDataConfig, quoteCurrency: QuantConnect.Securities.Cash, symbolProperties: QuantConnect.Securities.SymbolProperties, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypes: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider) -> None:
        """
        Constructor for the Future security
        
        :param exchangeHours: Defines the hours this exchange is open
        :param config: The subscription configuration for this security
        :param quoteCurrency: The cash object that represent the quote currency
        :param symbolProperties: The symbol properties for this security
        :param currencyConverter: Currency converter used to convert CashAmount instances into units of the account currency
        :param registeredTypes: Provides all data types registered in the algorithm
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], exchangeHours: QuantConnect.Securities.SecurityExchangeHours, quoteCurrency: QuantConnect.Securities.Cash, symbolProperties: QuantConnect.Securities.SymbolProperties, currencyConverter: QuantConnect.Securities.ICurrencyConverter, registeredTypes: QuantConnect.Securities.IRegisteredSecurityDataTypesProvider, securityCache: QuantConnect.Securities.SecurityCache, underlying: QuantConnect.Securities.Security = None) -> None:
        """
        Constructor for the Future security
        
        :param symbol: The subscription security symbol
        :param exchangeHours: Defines the hours this exchange is open
        :param quoteCurrency: The cash object that represent the quote currency
        :param symbolProperties: The symbol properties for this security
        :param currencyConverter: Currency converter used to convert CashAmount     instances into units of the account currency
        :param registeredTypes: Provides all data types registered in the algorithm
        :param securityCache: Cache to store security information
        :param underlying: Future underlying security
        """
        ...

    @overload
    def SetFilter(self, minExpiry: datetime.timedelta, maxExpiry: datetime.timedelta) -> None:
        """
        Sets the ContractFilter to a new instance of the filter
        using the specified expiration range values
        
        :param minExpiry: The minimum time until expiry to include, for example, TimeSpan.FromDays(10) would exclude contracts expiring in more than 10 days
        :param maxExpiry: The maximum time until expiry to include, for example, TimeSpan.FromDays(10) would exclude contracts expiring in less than 10 days
        """
        ...

    @overload
    def SetFilter(self, minExpiryDays: int, maxExpiryDays: int) -> None:
        """
        Sets the ContractFilter to a new instance of the filter
        using the specified expiration range values
        
        :param minExpiryDays: The minimum time, expressed in days, until expiry to include, for example, 10 would exclude contracts expiring in more than 10 days
        :param maxExpiryDays: The maximum time, expressed in days, until expiry to include, for example, 10 would exclude contracts expiring in less than 10 days
        """
        ...

    @overload
    def SetFilter(self, universeFunc: typing.Callable[[QuantConnect.Securities.FutureFilterUniverse], QuantConnect.Securities.FutureFilterUniverse]) -> None:
        """
        Sets the ContractFilter to a new universe selection function
        
        :param universeFunc: new universe selection function
        """
        ...

    @overload
    def SetFilter(self, universeFunc: typing.Any) -> None:
        """
        Sets the ContractFilter to a new universe selection function
        
        :param universeFunc: new universe selection function
        """
        ...


class MarginRequirementsEntry(System.Object):
    """POCO class for modeling margin requirements at given date"""

    @property
    def Date(self) -> datetime.datetime:
        """Date of margin requirements change"""
        ...

    @Date.setter
    def Date(self, value: datetime.datetime):
        """Date of margin requirements change"""
        ...

    @property
    def InitialOvernight(self) -> float:
        """Initial overnight margin for the contract effective from the date of change"""
        ...

    @InitialOvernight.setter
    def InitialOvernight(self, value: float):
        """Initial overnight margin for the contract effective from the date of change"""
        ...

    @property
    def MaintenanceOvernight(self) -> float:
        """Maintenance overnight margin for the contract effective from the date of change"""
        ...

    @MaintenanceOvernight.setter
    def MaintenanceOvernight(self, value: float):
        """Maintenance overnight margin for the contract effective from the date of change"""
        ...

    @property
    def InitialIntraday(self) -> float:
        """Initial intraday margin for the contract effective from the date of change"""
        ...

    @InitialIntraday.setter
    def InitialIntraday(self, value: float):
        """Initial intraday margin for the contract effective from the date of change"""
        ...

    @property
    def MaintenanceIntraday(self) -> float:
        """Maintenance intraday margin for the contract effective from the date of change"""
        ...

    @MaintenanceIntraday.setter
    def MaintenanceIntraday(self, value: float):
        """Maintenance intraday margin for the contract effective from the date of change"""
        ...

    @staticmethod
    def Create(csvLine: str) -> QuantConnect.Securities.Future.MarginRequirementsEntry:
        """
        Creates a new instance of MarginRequirementsEntry from the specified csv line
        
        :param csvLine: The csv line to be parsed
        :returns: A new MarginRequirementsEntry for the specified csv line.
        """
        ...


class FutureCache(QuantConnect.Securities.SecurityCache):
    """Future specific caching support"""


class FutureHolding(QuantConnect.Securities.SecurityHolding):
    """Future holdings implementation of the base securities class"""

    def __init__(self, security: QuantConnect.Securities.Security, currencyConverter: QuantConnect.Securities.ICurrencyConverter) -> None:
        """
        Future Holding Class constructor
        
        :param security: The future security being held
        :param currencyConverter: A currency converter instance
        """
        ...


class FutureMarginModel(QuantConnect.Securities.SecurityMarginModel):
    """Represents a simple margin model for margin futures. Margin file contains Initial and Maintenance margins"""

    @property
    def EnableIntradayMargins(self) -> bool:
        """True will enable usage of intraday margins."""
        ...

    @EnableIntradayMargins.setter
    def EnableIntradayMargins(self, value: bool):
        """True will enable usage of intraday margins."""
        ...

    @property
    def InitialOvernightMarginRequirement(self) -> float:
        """Initial Overnight margin requirement for the contract effective from the date of change"""
        ...

    @property
    def MaintenanceOvernightMarginRequirement(self) -> float:
        """Maintenance Overnight margin requirement for the contract effective from the date of change"""
        ...

    @property
    def InitialIntradayMarginRequirement(self) -> float:
        """Initial Intraday margin for the contract effective from the date of change"""
        ...

    @property
    def MaintenanceIntradayMarginRequirement(self) -> float:
        """Maintenance Intraday margin requirement for the contract effective from the date of change"""
        ...

    def __init__(self, requiredFreeBuyingPowerPercent: float = 0, security: QuantConnect.Securities.Security = None) -> None:
        """
        Initializes a new instance of the FutureMarginModel
        
        :param requiredFreeBuyingPowerPercent: The percentage used to determine the required unused buying power for the account.
        :param security: The security that this model belongs to
        """
        ...

    def GetInitialMarginRequiredForOrder(self, parameters: QuantConnect.Securities.InitialMarginRequiredForOrderParameters) -> QuantConnect.Securities.InitialMargin:
        """
        Gets the total margin required to execute the specified order in units of the account currency including fees
        
        :param parameters: An object containing the portfolio, the security and the order
        :returns: The total margin in terms of the currency quoted in the order.
        """
        ...

    def GetInitialMarginRequirement(self, parameters: QuantConnect.Securities.InitialMarginParameters) -> QuantConnect.Securities.InitialMargin:
        """The margin that must be held in order to increase the position by the provided quantity"""
        ...

    def GetLeverage(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the current leverage of the security
        
        :param security: The security to get leverage for
        :returns: The current leverage in the security.
        """
        ...

    def GetMaintenanceMargin(self, parameters: QuantConnect.Securities.MaintenanceMarginParameters) -> QuantConnect.Securities.MaintenanceMargin:
        """
        Gets the margin currently allotted to the specified holding
        
        :param parameters: An object containing the security
        :returns: The maintenance margin required for the.
        """
        ...

    def GetMaximumOrderQuantityForTargetBuyingPower(self, parameters: QuantConnect.Securities.GetMaximumOrderQuantityForTargetBuyingPowerParameters) -> QuantConnect.Securities.GetMaximumOrderQuantityResult:
        """
        Get the maximum market order quantity to obtain a position with a given buying power percentage.
        Will not take into account free buying power.
        
        :param parameters: An object containing the portfolio, the security and the target signed buying power percentage
        :returns: Returns the maximum allowed market order quantity and if zero, also the reason.
        """
        ...

    def SetLeverage(self, security: QuantConnect.Securities.Security, leverage: float) -> None:
        """
        Sets the leverage for the applicable securities, i.e, futures
        
        :param leverage: The new leverage
        """
        ...


class FuturesListings(System.Object):
    """
    Helpers for getting the futures contracts that are trading on a given date.
    This is a substitute for the BacktestingFutureChainProvider, but
    does not outright replace it because of missing entries. This will resolve
    the listed contracts without having any data in place. We follow the listing rules
    set forth by the exchange to get the Symbols that are listed at a given date.
    """

    @staticmethod
    def ListedContracts(futureTicker: str, time: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.List[QuantConnect.Symbol]:
        """
        Gets the listed futures contracts on a given date
        
        :param futureTicker: Ticker of the future contract
        :param time: Contracts to look up that are listed at that time
        :returns: The currently trading contracts on the exchange.
        """
        ...


class EmptyFutureChainProvider(System.Object, QuantConnect.Interfaces.IFutureChainProvider):
    """An implementation of IFutureChainProvider that always returns an empty list of contracts"""

    def GetFutureContractList(self, symbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Gets the list of future contracts for a given underlying symbol
        
        :param symbol: The underlying symbol
        :param date: The date for which to request the future chain (only used in backtesting)
        :returns: The list of future contracts.
        """
        ...


class FuturesExpiryFunctions(System.Object):
    """Calculate the date of a futures expiry given an expiry month and year"""

    DairyReportDates: System.Collections.Generic.Dictionary[datetime.datetime, datetime.datetime] = ...
    """
    The USDA publishes a report containing contract prices for the contract month.
    You can see future publication dates at https://www.ams.usda.gov/rules-regulations/mmr/dmr (Advanced and Class Price Release Dates)
    These dates are erratic and requires maintenance of a separate list instead of using holiday entries in MHDB.
    """

    EnbridgeNoticeOfShipmentDates: System.Collections.Generic.Dictionary[datetime.datetime, datetime.datetime] = ...
    """Enbridge's Notice of Shipment report dates. Used to calculate the last trade date for CSW"""

    FuturesExpiryDictionary: System.Collections.Generic.Dictionary[QuantConnect.Symbol, typing.Callable[[datetime.datetime], datetime.datetime]] = ...
    """
    Dictionary of the Functions that calculates the expiry for a given year and month.
    It does not matter what the day and time of day are passed into the Functions.
    The Functions is responsible for calculating the day and time of day given a year and month
    """

    @staticmethod
    def FuturesExpiryFunction(symbol: typing.Union[QuantConnect.Symbol, str]) -> typing.Callable[[datetime.datetime], datetime.datetime]:
        """Method to retrieve the Function for a specific future symbol"""
        ...


class FutureExchange(QuantConnect.Securities.SecurityExchange):
    """Future exchange class - information and helper tools for future exchange properties"""

    @property
    def TradingDaysPerYear(self) -> int:
        """Number of trading days per year for this security, 252."""
        ...

    def __init__(self, exchangeHours: QuantConnect.Securities.SecurityExchangeHours) -> None:
        """
        Initializes a new instance of the FutureExchange class using the specified
        exchange hours to determine open/close times
        
        :param exchangeHours: Contains the weekly exchange schedule plus holidays
        """
        ...


class FuturesExpiryUtilityFunctions(System.Object):
    """Class to implement common functions used in FuturesExpiryFunctions"""

    @staticmethod
    def AddBusinessDays(time: typing.Union[datetime.datetime, datetime.date], n: int, useEquityHolidays: bool = True, holidayList: System.Collections.Generic.IEnumerable[datetime.datetime] = None) -> datetime.datetime:
        """
        Method to retrieve n^th succeeding/preceding business day for a given day
        
        :param time: The current Time
        :param n: Number of business days succeeding current time. Use negative value for preceding business days
        :param useEquityHolidays: Use LEAN's USHoliday definitions as holidays to exclude
        :param holidayList: Enumerable of holidays to exclude. These should be sourced from the MarketHoursDatabase
        :returns: The date-time after adding n business days.
        """
        ...

    @staticmethod
    def DairyLastTradeDate(time: typing.Union[datetime.datetime, datetime.date], lastTradeTime: typing.Optional[datetime.timedelta] = None) -> datetime.datetime:
        """
        Gets the last trade date corresponding to the contract month
        
        :param time: Contract month
        :param lastTradeTime: Time at which the dairy future contract stops trading (usually should be on 17:10:00 UTC)
        """
        ...

    @staticmethod
    def GetDatesFromDateTimeList(dateTimeList: System.Collections.Generic.IEnumerable[datetime.datetime]) -> System.Collections.Generic.List[datetime.datetime]:
        """
        Extracts Date portion of list of DateTimes
        
        :param dateTimeList: List of DateTimes (with optional time portion) to filter
        :returns: List of DateTimes with default time (00:00:00).
        """
        ...

    @staticmethod
    def GetDeltaBetweenContractMonthAndContractExpiry(underlying: str, futureExpiryDate: typing.Optional[datetime.datetime] = None) -> int:
        """
        Gets the number of months between the contract month and the expiry date.
        
        :param underlying: The future symbol ticker
        :param futureExpiryDate: Expiry date to use to look up contract month delta. Only used for dairy, since we need to lookup its contract month in a pre-defined table.
        :returns: The number of months between the contract month and the contract expiry.
        """
        ...

    @staticmethod
    def GetGoodFriday(year: int) -> datetime.datetime:
        """
        Calculates the date of Good Friday for a given year.
        
        :param year: Year to calculate Good Friday for
        :returns: Date of Good Friday.
        """
        ...

    @staticmethod
    def LastFriday(time: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """
        Method to retrieve the last Friday of any month
        
        :param time: Date from the given month
        :returns: Last Friday of the given month.
        """
        ...

    @staticmethod
    def LastThursday(time: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """
        Method to retrieve the last Thursday of any month
        
        :param time: Date from the given month
        :returns: Last Thursday of the given month.
        """
        ...

    @staticmethod
    def LastWeekday(time: typing.Union[datetime.datetime, datetime.date], dayOfWeek: System.DayOfWeek) -> datetime.datetime:
        """
        Method to retrieve the last weekday of any month
        
        :param time: Date from the given month
        :param dayOfWeek: the last weekday to be found
        :returns: Last day of the we.
        """
        ...

    @staticmethod
    def NotHoliday(time: typing.Union[datetime.datetime, datetime.date]) -> bool:
        """
        Method to check whether a given time is holiday or not
        
        :param time: The DateTime for consideration
        :returns: True if the time is not a holidays, otherwise returns false.
        """
        ...

    @staticmethod
    def NotPrecededByHoliday(thursday: typing.Union[datetime.datetime, datetime.date]) -> bool:
        """
        This function takes Thursday as input and returns true if four weekdays preceding it are not Holidays
        
        :param thursday: DateTime of a given Thursday
        :returns: False if DayOfWeek is not Thursday or is not preceded by four weekdays,Otherwise returns True.
        """
        ...

    @staticmethod
    def NthBusinessDay(time: typing.Union[datetime.datetime, datetime.date], nthBusinessDay: int, holidayList: System.Collections.Generic.IEnumerable[datetime.datetime] = None) -> datetime.datetime:
        """
        Calculates the n^th business day of the month (includes checking for holidays)
        
        :param time: Month to calculate business day for
        :param nthBusinessDay: n^th business day to get
        :param holidayList: Additional user provided holidays to not count as business days
        :returns: Nth business day of the month.
        """
        ...

    @staticmethod
    def NthFriday(time: typing.Union[datetime.datetime, datetime.date], n: int) -> datetime.datetime:
        """
        Method to retrieve the Nth Friday of the given month
        
        :param time: Date from the given month
        :param n: The order of the Friday in the period
        :returns: Nth Friday of given month.
        """
        ...

    @staticmethod
    def NthLastBusinessDay(time: typing.Union[datetime.datetime, datetime.date], n: int, holidayList: System.Collections.Generic.IEnumerable[datetime.datetime] = None) -> datetime.datetime:
        """
        Method to retrieve the n^th last business day of the delivery month.
        
        :param time: DateTime for delivery month
        :param n: Number of days
        :param holidayList: Additional holidays to use while calculating n^th business day. Useful for MHDB entries
        :returns: Nth Last Business day of the month.
        """
        ...

    @staticmethod
    def NthWeekday(time: typing.Union[datetime.datetime, datetime.date], n: int, dayOfWeek: System.DayOfWeek) -> datetime.datetime:
        """
        Method to retrieve the Nth Weekday of the given month
        
        :param time: Date from the given month
        :param n: The order of the Weekday in the period
        :param dayOfWeek: The day of the week
        :returns: Nth Weekday of given month.
        """
        ...

    @staticmethod
    def SecondFriday(time: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """
        Method to retrieve the 2nd Friday of the given month
        
        :param time: Date from the given month
        :returns: 2nd Friday of given month.
        """
        ...

    @staticmethod
    def ThirdFriday(time: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """
        Method to retrieve the 3rd Friday of the given month
        
        :param time: Date from the given month
        :returns: 3rd Friday of given month.
        """
        ...

    @staticmethod
    def ThirdWednesday(time: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """
        Method to retrieve third Wednesday of the given month (usually Monday).
        
        :param time: Date from the given month
        :returns: Third Wednesday of the given month.
        """
        ...


class FutureSymbol(System.Object):
    """Static class contains common utility methods specific to symbols representing the future contracts"""

    @staticmethod
    def IsStandard(symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Determine if a given Futures contract is a standard contract.
        
        :param symbol: Future symbol
        :returns: True if symbol expiration matches standard expiration.
        """
        ...

    @staticmethod
    def IsWeekly(symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Returns true if the future contract is a weekly contract
        
        :param symbol: Future symbol
        :returns: True if symbol is non-standard contract.
        """
        ...


class FuturesOptionsSymbolMappings(System.Object):
    """Provides conversions from a GLOBEX Futures ticker to a GLOBEX Futures Options ticker"""

    @staticmethod
    def Map(futureTicker: str) -> str:
        """
        Returns the futures options ticker for the given futures ticker.
        
        :param futureTicker: Future GLOBEX ticker to get Future Option GLOBEX ticker for
        :returns: Future option ticker. Defaults to future ticker provided if no entry is found.
        """
        ...

    @staticmethod
    def MapFromOption(futureOptionTicker: str) -> str:
        """
        Maps a futures options ticker to its underlying future's ticker
        
        :param futureOptionTicker: Future option ticker to map to the underlying
        :returns: Future ticker.
        """
        ...


