from typing import overload
import datetime
import typing

import QuantConnect
import QuantConnect.Algorithm.Framework.Alphas
import QuantConnect.AlgorithmFactory.Python.Wrappers
import QuantConnect.Benchmarks
import QuantConnect.Brokerages
import QuantConnect.Data
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import QuantConnect.Notifications
import QuantConnect.Orders
import QuantConnect.Scheduling
import QuantConnect.Securities
import QuantConnect.Securities.Future
import QuantConnect.Securities.Option
import QuantConnect.Storage
import System
import System.Collections.Concurrent
import System.Collections.Generic

QuantConnect_AlgorithmFactory_Python_Wrappers__EventContainer_Callable = typing.TypeVar("QuantConnect_AlgorithmFactory_Python_Wrappers__EventContainer_Callable")
QuantConnect_AlgorithmFactory_Python_Wrappers__EventContainer_ReturnType = typing.TypeVar("QuantConnect_AlgorithmFactory_Python_Wrappers__EventContainer_ReturnType")


class AlgorithmPythonWrapper(System.Object, QuantConnect.Interfaces.IAlgorithm):
    """Creates and wraps the algorithm written in python."""

    @property
    def IsOnEndOfDayImplemented(self) -> bool:
        """True if the underlying python algorithm implements "OnEndOfDay\""""
        ...

    @property
    def IsOnEndOfDaySymbolImplemented(self) -> bool:
        """True if the underlying python algorithm implements "OnEndOfDay(symbol)\""""
        ...

    @property
    def AlgorithmId(self) -> str:
        """AlgorithmId for the backtest"""
        ...

    @property
    def Benchmark(self) -> QuantConnect.Benchmarks.IBenchmark:
        """
        Gets the function used to define the benchmark. This function will return
        the value of the benchmark at a requested date/time
        """
        ...

    @property
    def BrokerageMessageHandler(self) -> QuantConnect.Brokerages.IBrokerageMessageHandler:
        """
        Gets the brokerage message handler used to decide what to do
        with each message sent from the brokerage
        """
        ...

    @BrokerageMessageHandler.setter
    def BrokerageMessageHandler(self, value: QuantConnect.Brokerages.IBrokerageMessageHandler):
        """
        Gets the brokerage message handler used to decide what to do
        with each message sent from the brokerage
        """
        ...

    @property
    def BrokerageModel(self) -> QuantConnect.Brokerages.IBrokerageModel:
        """Gets the brokerage model used to emulate a real brokerage"""
        ...

    @property
    def DebugMessages(self) -> System.Collections.Concurrent.ConcurrentQueue[str]:
        """Debug messages from the strategy:"""
        ...

    @property
    def EndDate(self) -> datetime.datetime:
        """Get Requested Backtest End Date"""
        ...

    @property
    def ErrorMessages(self) -> System.Collections.Concurrent.ConcurrentQueue[str]:
        """Error messages from the strategy:"""
        ...

    @property
    def HistoryProvider(self) -> QuantConnect.Interfaces.IHistoryProvider:
        """Gets or sets the history provider for the algorithm"""
        ...

    @HistoryProvider.setter
    def HistoryProvider(self, value: QuantConnect.Interfaces.IHistoryProvider):
        """Gets or sets the history provider for the algorithm"""
        ...

    @property
    def IsWarmingUp(self) -> bool:
        """Gets whether or not this algorithm is still warming up"""
        ...

    @property
    def LiveMode(self) -> bool:
        """Algorithm is running on a live server."""
        ...

    @property
    def LogMessages(self) -> System.Collections.Concurrent.ConcurrentQueue[str]:
        """Log messages from the strategy:"""
        ...

    @property
    def Name(self) -> str:
        """Public name for the algorithm."""
        ...

    @Name.setter
    def Name(self, value: str):
        """Public name for the algorithm."""
        ...

    @property
    def Notify(self) -> QuantConnect.Notifications.NotificationManager:
        """Notification manager for storing and processing live event messages"""
        ...

    @property
    def Portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """
        Security portfolio management class provides wrapper and helper methods for the Security.Holdings class such as
        IsLong, IsShort, TotalProfit
        """
        ...

    @property
    def RunTimeError(self) -> System.Exception:
        """Gets the run time error from the algorithm, or null if none was encountered."""
        ...

    @RunTimeError.setter
    def RunTimeError(self, value: System.Exception):
        """Gets the run time error from the algorithm, or null if none was encountered."""
        ...

    @property
    def RuntimeStatistics(self) -> System.Collections.Concurrent.ConcurrentDictionary[str, str]:
        """Customizable dynamic statistics displayed during live trading:"""
        ...

    @property
    def Schedule(self) -> QuantConnect.Scheduling.ScheduleManager:
        """Gets schedule manager for adding/removing scheduled events"""
        ...

    @property
    def Securities(self) -> QuantConnect.Securities.SecurityManager:
        """
        Security object collection class stores an array of objects representing representing each security/asset
        we have a subscription for.
        """
        ...

    @property
    def SecurityInitializer(self) -> QuantConnect.Securities.ISecurityInitializer:
        """Gets an instance that is to be used to initialize newly created securities."""
        ...

    @property
    def TradeBuilder(self) -> QuantConnect.Interfaces.ITradeBuilder:
        """Gets the Trade Builder to generate trades from executions"""
        ...

    @property
    def Settings(self) -> QuantConnect.Interfaces.IAlgorithmSettings:
        """Gets the user settings for the algorithm"""
        ...

    @property
    def OptionChainProvider(self) -> QuantConnect.Interfaces.IOptionChainProvider:
        """Gets the option chain provider, used to get the list of option contracts for an underlying symbol"""
        ...

    @property
    def FutureChainProvider(self) -> QuantConnect.Interfaces.IFutureChainProvider:
        """Gets the future chain provider, used to get the list of future contracts for an underlying symbol"""
        ...

    @property
    def ObjectStore(self) -> QuantConnect.Storage.ObjectStore:
        """Gets the object store, used for persistence"""
        ...

    @property
    def CurrentSlice(self) -> QuantConnect.Data.Slice:
        """Returns the current Slice object"""
        ...

    @property
    def StartDate(self) -> datetime.datetime:
        """Algorithm start date for backtesting, set by the SetStartDate methods."""
        ...

    @property
    def Status(self) -> int:
        """
        Gets or sets the current status of the algorithm
        
        This property contains the int value of a member of the QuantConnect.AlgorithmStatus enum.
        """
        ...

    @Status.setter
    def Status(self, value: int):
        """
        Gets or sets the current status of the algorithm
        
        This property contains the int value of a member of the QuantConnect.AlgorithmStatus enum.
        """
        ...

    @property
    def InsightsGenerated(self) -> _EventContainer[typing.Callable[[QuantConnect.Interfaces.IAlgorithm, QuantConnect.Algorithm.Framework.Alphas.GeneratedInsightsCollection], None], None]:
        """Event fired when an algorithm generates a insight"""
        ...

    @InsightsGenerated.setter
    def InsightsGenerated(self, value: _EventContainer[typing.Callable[[QuantConnect.Interfaces.IAlgorithm, QuantConnect.Algorithm.Framework.Alphas.GeneratedInsightsCollection], None], None]):
        """Event fired when an algorithm generates a insight"""
        ...

    @property
    def TimeKeeper(self) -> QuantConnect.Interfaces.ITimeKeeper:
        """Gets the time keeper instance"""
        ...

    @property
    def SubscriptionManager(self) -> QuantConnect.Data.SubscriptionManager:
        """
        Data subscription manager controls the information and subscriptions the algorithms recieves.
        Subscription configurations can be added through the Subscription Manager.
        """
        ...

    @property
    def ProjectId(self) -> int:
        """The project id associated with this algorithm if any"""
        ...

    @ProjectId.setter
    def ProjectId(self, value: int):
        """The project id associated with this algorithm if any"""
        ...

    @property
    def Time(self) -> datetime.datetime:
        """Current date/time in the algorithm's local time zone"""
        ...

    @property
    def TimeZone(self) -> typing.Any:
        """Gets the time zone of the algorithm"""
        ...

    @property
    def Transactions(self) -> QuantConnect.Securities.SecurityTransactionManager:
        """Security transaction manager class controls the store and processing of orders."""
        ...

    @property
    def UniverseManager(self) -> QuantConnect.Securities.UniverseManager:
        """Gets the collection of universes for the algorithm"""
        ...

    @property
    def UniverseSettings(self) -> QuantConnect.Data.UniverseSelection.UniverseSettings:
        """Gets the subscription settings to be used when adding securities via universe selection"""
        ...

    @property
    def UtcTime(self) -> datetime.datetime:
        """Current date/time in UTC."""
        ...

    @property
    def AccountCurrency(self) -> str:
        """Gets the account currency"""
        ...

    def __init__(self, moduleName: str) -> None:
        """
        AlgorithmPythonWrapper constructor.
        Creates and wraps the algorithm written in python.
        
        :param moduleName: Name of the module that can be found in the PYTHONPATH
        """
        ...

    def AddChart(self, chart: QuantConnect.Chart) -> None:
        """
        Add a Chart object to algorithm collection
        
        :param chart: Chart object to add to collection.
        """
        ...

    def AddFutureContract(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, fillDataForward: bool = True, leverage: float = 0, extendedMarketHours: bool = False) -> QuantConnect.Securities.Future.Future:
        """
        Creates and adds a new single Future contract to the algorithm
        
        :param symbol: The futures contract symbol
        :param resolution: The Resolution of market data, Tick, Second, Minute, Hour, or Daily. Default is Resolution.Minute
        :param fillDataForward: If true, returns the last available data even if none in that timeslice. Default is true
        :param leverage: The requested leverage for this equity. Default is set by SecurityInitializer
        :param extendedMarketHours: Use extended market hours data
        :returns: The new Future security.
        """
        ...

    def AddOptionContract(self, symbol: typing.Union[QuantConnect.Symbol, str], resolution: typing.Optional[QuantConnect.Resolution] = None, fillDataForward: bool = True, leverage: float = 0, extendedMarketHours: bool = False) -> QuantConnect.Securities.Option.Option:
        """
        Creates and adds a new single Option contract to the algorithm
        
        :param symbol: The option contract symbol
        :param resolution: The Resolution of market data, Tick, Second, Minute, Hour, or Daily. Default is Resolution.Minute
        :param fillDataForward: If true, returns the last available data even if none in that timeslice. Default is true
        :param leverage: The requested leverage for this equity. Default is set by SecurityInitializer
        :param extendedMarketHours: Use extended market hours data
        :returns: The new Option security.
        """
        ...

    def AddSecurity(self, securityType: QuantConnect.SecurityType, symbol: str, resolution: typing.Optional[QuantConnect.Resolution], market: str, fillDataForward: bool, leverage: float, extendedMarketHours: bool, dataMappingMode: typing.Optional[QuantConnect.DataMappingMode] = None, dataNormalizationMode: typing.Optional[QuantConnect.DataNormalizationMode] = None) -> QuantConnect.Securities.Security:
        """
        Set a required SecurityType-symbol and resolution for algorithm
        
        :param securityType: SecurityType Enum: Equity, Commodity, FOREX or Future
        :param symbol: Symbol Representation of the MarketType, e.g. AAPL
        :param resolution: The Resolution of market data, Tick, Second, Minute, Hour, or Daily.
        :param market: The market the requested security belongs to, such as 'usa' or 'fxcm'
        :param fillDataForward: If true, returns the last available data even if none in that timeslice.
        :param leverage: leverage for this security
        :param extendedMarketHours: Use extended market hours data
        :param dataMappingMode: The contract mapping mode to use for the security
        :param dataNormalizationMode: The price scaling mode to use for the security
        """
        ...

    def Debug(self, message: str) -> None:
        """
        Send debug message
        
        :param message: String message
        """
        ...

    def Error(self, message: str) -> None:
        """
        Send an error message for the algorithm
        
        :param message: String message
        """
        ...

    def GetChartUpdates(self, clearChartData: bool = False) -> System.Collections.Generic.List[QuantConnect.Chart]:
        """
        Get the chart updates since the last request:
        
        :returns: List of Chart Updates.
        """
        ...

    def GetLastKnownPrice(self, security: QuantConnect.Securities.Security) -> QuantConnect.Data.BaseData:
        """
        Get the last known price using the history provider.
        Useful for seeding securities with the correct price
        
        :param security: Security object for which to retrieve historical data
        :returns: A single BaseData object with the last known price.
        """
        ...

    def GetLocked(self) -> bool:
        """Gets whether or not this algorithm has been locked and fully initialized"""
        ...

    @overload
    def GetParameter(self, name: str, defaultValue: str = None) -> str:
        """
        Gets the parameter with the specified name. If a parameter with the specified name does not exist,
        the given default value is returned if any, else null
        
        :param name: The name of the parameter to get
        :param defaultValue: The default value to return
        :returns: The value of the specified parameter, or defaultValue if not found or null if there's no default value.
        """
        ...

    @overload
    def GetParameter(self, name: str, defaultValue: int) -> int:
        """
        Gets the parameter with the specified name parsed as an integer. If a parameter with the specified name does not exist,
        or the conversion is not possible, the given default value is returned
        
        :param name: The name of the parameter to get
        :param defaultValue: The default value to return
        :returns: The value of the specified parameter, or defaultValue if not found or null if there's no default value.
        """
        ...

    @overload
    def GetParameter(self, name: str, defaultValue: float) -> float:
        """
        Gets the parameter with the specified name parsed as a double. If a parameter with the specified name does not exist,
        or the conversion is not possible, the given default value is returned
        
        :param name: The name of the parameter to get
        :param defaultValue: The default value to return
        :returns: The value of the specified parameter, or defaultValue if not found or null if there's no default value.
        """
        ...

    @overload
    def GetParameter(self, name: str, defaultValue: float) -> float:
        """
        Gets the parameter with the specified name parsed as a decimal. If a parameter with the specified name does not exist,
        or the conversion is not possible, the given default value is returned
        
        :param name: The name of the parameter to get
        :param defaultValue: The default value to return
        :returns: The value of the specified parameter, or defaultValue if not found or null if there's no default value.
        """
        ...

    def Initialize(self) -> None:
        """Initialise the Algorithm and Prepare Required Data:"""
        ...

    def Liquidate(self, symbolToLiquidate: typing.Union[QuantConnect.Symbol, str] = None, tag: str = "Liquidated") -> System.Collections.Generic.List[int]:
        """
        Liquidate your portfolio holdings:
        
        :param symbolToLiquidate: Specific asset to liquidate, defaults to all.
        :param tag: Custom tag to know who is calling this.
        :returns: list of order ids.
        """
        ...

    def Log(self, message: str) -> None:
        """
        Save entry to the Log
        
        :param message: String message
        """
        ...

    def OnAssignmentOrderEvent(self, assignmentEvent: QuantConnect.Orders.OrderEvent) -> None:
        """
        Option assignment event handler. On an option assignment event for short legs the resulting information is passed to this method.
        
        :param assignmentEvent: Option exercise event details containing details of the assignment
        """
        ...

    def OnBrokerageDisconnect(self) -> None:
        """Brokerage disconnected event handler. This method is called when the brokerage connection is lost."""
        ...

    def OnBrokerageMessage(self, messageEvent: QuantConnect.Brokerages.BrokerageMessageEvent) -> None:
        """Brokerage message event handler. This method is called for all types of brokerage messages."""
        ...

    def OnBrokerageReconnect(self) -> None:
        """Brokerage reconnected event handler. This method is called when the brokerage connection is restored after a disconnection."""
        ...

    def OnData(self, slice: QuantConnect.Data.Slice) -> None:
        """
        v3.0 Handler for all data types
        
        :param slice: The current slice of data
        """
        ...

    def OnEndOfAlgorithm(self) -> None:
        """Call this event at the end of the algorithm running."""
        ...

    @overload
    def OnEndOfDay(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> None:
        """
        End of a trading day event handler. This method is called at the end of the algorithm day (or multiple times if trading multiple assets).
        
        :param symbol: Asset symbol for this end of day event. Forex and equities have different closing hours.
        """
        ...

    @overload
    def OnEndOfDay(self) -> None:
        """
        End of a trading day event handler. This method is called at the end of the algorithm day (or multiple times if trading multiple assets).
        
        This method is deprecated. Please use this overload: OnEndOfDay(Symbol symbol)
        """
        ...

    def OnEndOfTimeStep(self) -> None:
        """
        Invoked at the end of every time step. This allows the algorithm
        to process events before advancing to the next time step.
        """
        ...

    def OnFrameworkData(self, slice: QuantConnect.Data.Slice) -> None:
        """
        Used to send data updates to algorithm framework models
        
        :param slice: The current data slice
        """
        ...

    def OnFrameworkSecuritiesChanged(self, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """
        Used to send security changes to algorithm framework models
        
        :param changes: Security additions/removals for this time step
        """
        ...

    def OnMarginCall(self, requests: System.Collections.Generic.List[QuantConnect.Orders.SubmitOrderRequest]) -> None:
        """
        Margin call event handler. This method is called right before the margin call orders are placed in the market.
        
        :param requests: The orders to be executed to bring this algorithm within margin limits
        """
        ...

    def OnMarginCallWarning(self) -> None:
        """Margin call warning event handler. This method is called when Portfolio.MarginRemaining is under 5% of your Portfolio.TotalPortfolioValue"""
        ...

    def OnOrderEvent(self, newEvent: QuantConnect.Orders.OrderEvent) -> None:
        """
        EXPERTS ONLY:: [-!-Async Code-!-]
        New order event handler: on order status changes (filled, partially filled, cancelled etc).
        
        :param newEvent: Event information
        """
        ...

    def OnSecuritiesChanged(self, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """
        Event fired each time the we add/remove securities from the data feed
        
        :param changes: Security additions/removals for this time step
        """
        ...

    def OnWarmupFinished(self) -> None:
        """Called when the algorithm has completed initialization and warm up."""
        ...

    def PostInitialize(self) -> None:
        """
        Called by setup handlers after Initialize and allows the algorithm a chance to organize
        the data gather in the Initialize method
        """
        ...

    def RemoveSecurity(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Removes the security with the specified symbol. This will cancel all
        open orders and then liquidate any existing holdings
        
        :param symbol: The symbol of the security to be removed
        """
        ...

    def SetAccountCurrency(self, accountCurrency: str) -> None:
        """
        Sets the account currency cash symbol this algorithm is to manage.
        
        :param accountCurrency: The account currency cash symbol to set
        """
        ...

    def SetAlgorithmId(self, algorithmId: str) -> None:
        """
        Set the algorithm Id for this backtest or live run. This can be used to identify the order and equity records.
        
        :param algorithmId: unique 32 character identifier for backtest or live server
        """
        ...

    def SetApi(self, api: QuantConnect.Interfaces.IApi) -> None:
        """
        Provide the API for the algorithm.
        
        :param api: Initiated API
        """
        ...

    def SetAvailableDataTypes(self, availableDataTypes: System.Collections.Generic.Dictionary[QuantConnect.SecurityType, System.Collections.Generic.List[QuantConnect.TickType]]) -> None:
        """
        Set the available TickType supported by each SecurityType in SecurityManager
        
        :param availableDataTypes: >The different TickType each Security supports
        """
        ...

    def SetBrokerageMessageHandler(self, handler: QuantConnect.Brokerages.IBrokerageMessageHandler) -> None:
        """
        Sets the implementation used to handle messages from the brokerage.
        The default implementation will forward messages to debug or error
        and when a BrokerageMessageType.Error occurs, the algorithm
        is stopped.
        
        :param handler: The message handler to use
        """
        ...

    def SetBrokerageModel(self, brokerageModel: QuantConnect.Brokerages.IBrokerageModel) -> None:
        """
        Sets the brokerage model used to resolve transaction models, settlement models,
        and brokerage specified ordering behaviors.
        
        :param brokerageModel: The brokerage model used to emulate the real brokerage
        """
        ...

    @overload
    def SetCash(self, startingCash: float) -> None:
        """
        Set the starting capital for the strategy
        
        :param startingCash: decimal starting capital, default $100,000
        """
        ...

    @overload
    def SetCash(self, symbol: str, startingCash: float, conversionRate: float = 0) -> None:
        """
        Set the cash for the specified symbol
        
        :param symbol: The cash symbol to set
        :param startingCash: Decimal cash value of portfolio
        :param conversionRate: The current conversion rate for the
        """
        ...

    def SetCurrentSlice(self, slice: QuantConnect.Data.Slice) -> None:
        """
        Sets the current slice
        
        :param slice: The Slice object
        """
        ...

    def SetDateTime(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """Set the DateTime Frontier: This is the master time and is"""
        ...

    def SetEndDate(self, end: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Set the end date for a backtest.
        
        :param end: Datetime value for end date
        """
        ...

    def SetFinishedWarmingUp(self) -> None:
        """Sets IsWarmingUp to false to indicate this algorithm has finished its warm up"""
        ...

    def SetFutureChainProvider(self, futureChainProvider: QuantConnect.Interfaces.IFutureChainProvider) -> None:
        """
        Sets the future chain provider, used to get the list of future contracts for an underlying symbol
        
        :param futureChainProvider: The future chain provider
        """
        ...

    def SetHistoryProvider(self, historyProvider: QuantConnect.Interfaces.IHistoryProvider) -> None:
        """
        Set the historical data provider
        
        :param historyProvider: Historical data provider
        """
        ...

    def SetLiveMode(self, live: bool) -> None:
        """
        Set live mode state of the algorithm run: Public setter for the algorithm property LiveMode.
        
        :param live: Bool live mode flag
        """
        ...

    def SetLocked(self) -> None:
        """Set the algorithm as initialized and locked. No more cash or security changes."""
        ...

    def SetMaximumOrders(self, max: int) -> None:
        """
        Set the maximum number of orders the algorithm is allowed to process.
        
        :param max: Maximum order count int
        """
        ...

    def SetObjectStore(self, objectStore: QuantConnect.Interfaces.IObjectStore) -> None:
        """
        Sets the object store
        
        :param objectStore: The object store
        """
        ...

    def SetOptionChainProvider(self, optionChainProvider: QuantConnect.Interfaces.IOptionChainProvider) -> None:
        """
        Sets the option chain provider, used to get the list of option contracts for an underlying symbol
        
        :param optionChainProvider: The option chain provider
        """
        ...

    def SetParameters(self, parameters: System.Collections.Generic.Dictionary[str, str]) -> None:
        """
        Sets the parameters from the dictionary
        
        :param parameters: Dictionary containing the parameter names to values
        """
        ...

    def SetRunTimeError(self, exception: System.Exception) -> None:
        """
        Set the runtime error
        
        :param exception: Represents error that occur during execution
        """
        ...

    def SetStartDate(self, start: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Set the start date for the backtest
        
        :param start: Datetime Start date for backtest
        """
        ...

    def SetStatus(self, status: QuantConnect.AlgorithmStatus) -> None:
        """
        Set the state of a live deployment
        
        :param status: Live deployment status
        """
        ...

    def Shortable(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float) -> bool:
        """
        Checks if the asset is shortable at the brokerage
        
        :param symbol: Symbol to check if it is shortable
        :param quantity: Quantity to short
        :returns: True if shortable at the brokerage.
        """
        ...

    def SubmitOrderRequest(self, request: QuantConnect.Orders.SubmitOrderRequest) -> QuantConnect.Orders.OrderTicket:
        """
        Will submit an order request to the algorithm
        
        :param request: The request to submit
        :returns: The order ticket.
        """
        ...

    def ToString(self) -> str:
        """Returns a string that represents the current AlgorithmPythonWrapper object."""
        ...


class _EventContainer(typing.Generic[QuantConnect_AlgorithmFactory_Python_Wrappers__EventContainer_Callable, QuantConnect_AlgorithmFactory_Python_Wrappers__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_AlgorithmFactory_Python_Wrappers__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_AlgorithmFactory_Python_Wrappers__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_AlgorithmFactory_Python_Wrappers__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


