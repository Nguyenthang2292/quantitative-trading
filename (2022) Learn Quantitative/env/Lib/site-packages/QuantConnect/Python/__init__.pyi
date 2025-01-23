from typing import overload
import datetime
import typing

import QuantConnect
import QuantConnect.Benchmarks
import QuantConnect.Brokerages
import QuantConnect.Data
import QuantConnect.Data.Consolidators
import QuantConnect.Data.Market
import QuantConnect.DataSource
import QuantConnect.Indicators
import QuantConnect.Interfaces
import QuantConnect.Orders
import QuantConnect.Orders.Fees
import QuantConnect.Orders.Fills
import QuantConnect.Orders.Slippage
import QuantConnect.Python
import QuantConnect.Securities
import QuantConnect.Securities.Volatility
import System
import System.Collections.Generic
import pandas

QuantConnect_Python_PandasConverter_GetDataFrame_T = typing.TypeVar("QuantConnect_Python_PandasConverter_GetDataFrame_T")
QuantConnect_Python__EventContainer_Callable = typing.TypeVar("QuantConnect_Python__EventContainer_Callable")
QuantConnect_Python__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Python__EventContainer_ReturnType")


class PythonSlice(QuantConnect.Data.Slice):
    """Provides a data structure for all of an algorithm's data at a single time step"""

    @property
    def Count(self) -> int:
        """Gets the number of symbols held in this slice"""
        ...

    @property
    def Keys(self) -> System.Collections.Generic.IReadOnlyList[QuantConnect.Symbol]:
        """Gets all the symbols in this slice"""
        ...

    @property
    def Values(self) -> System.Collections.Generic.IReadOnlyList[QuantConnect.Data.BaseData]:
        """Gets a list of all the data in this slice"""
        ...

    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> typing.Any:
        """
        Gets the data corresponding to the specified symbol. If the requested data
        is of MarketDataType.Tick, then a List{Tick} will
        be returned, otherwise, it will be the subscribed type, for example, TradeBar
        or event UnlinkedData for custom data.
        
        :param symbol: The data's symbols
        :returns: The data for the specified symbol.
        """
        ...

    def __init__(self, slice: QuantConnect.Data.Slice) -> None:
        """
        Initializes a new instance of the PythonSlice class
        
        :param slice: slice object to wrap
        """
        ...

    def __setitem__(self, symbol: typing.Union[QuantConnect.Symbol, str], value: typing.Any) -> None:
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
    def Get(self, type: typing.Any, symbol: typing.Union[QuantConnect.Symbol, str]) -> typing.Any:
        """
        Gets the data of the specified symbol and type.
        
        :param type: The type of data we seek
        :param symbol: The specific symbol was seek
        :returns: The data for the requested symbol.
        """
        ...

    @overload
    def Get(self, type: typing.Any) -> typing.Any:
        """
        Gets the data of the specified symbol and type.
        
        :param type: The type of data we seek
        :returns: The data for the requested symbol.
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


class PythonInitializer(System.Object):
    """Helper class for Python initialization"""

    @staticmethod
    def ActivatePythonVirtualEnvironment(pathToVirtualEnv: str) -> bool:
        """
        "Activate" a virtual Python environment by prepending its library storage to Pythons
        path. This allows the libraries in this venv to be selected prior to our base install.
        Requires PYTHONNET_PYDLL to be set to base install.
        """
        ...

    @staticmethod
    def AddAlgorithmLocationPath(algorithmLocation: str) -> None:
        """
        Adds the algorithm location to the python path.
        This will make sure that AddPythonPaths keeps the algorithm location path
        at the beginning of the pythonpath.
        """
        ...

    @staticmethod
    def AddPythonPaths(paths: System.Collections.Generic.IEnumerable[str]) -> bool:
        """Adds directories to the python path at runtime"""
        ...

    @staticmethod
    def Initialize(beginAllowThreads: bool = True) -> None:
        """
        Initialize python.
        
        In some cases, we might not need to call BeginAllowThreads, like when we're running
        in a python or non-threaded environment.
        In those cases, we can set the beginAllowThreads parameter to false.
        """
        ...

    @staticmethod
    def ResetAlgorithmLocationPath() -> None:
        """Resets the algorithm location path so another can be set"""
        ...

    @staticmethod
    def Shutdown() -> None:
        """Shutdown python"""
        ...


class BuyingPowerModelPythonWrapper(System.Object, QuantConnect.Securities.IBuyingPowerModel):
    """Wraps a PyObject object that represents a security's model of buying power"""

    def __init__(self, model: typing.Any) -> None:
        """
        Constructor for initializing the BuyingPowerModelPythonWrapper class with wrapped PyObject object
        
        :param model: Represents a security's model of buying power
        """
        ...

    def GetBuyingPower(self, parameters: QuantConnect.Securities.BuyingPowerParameters) -> QuantConnect.Securities.BuyingPower:
        """
        Gets the buying power available for a trade
        
        :param parameters: A parameters object containing the algorithm's potrfolio, security, and order direction
        :returns: The buying power available for the trade.
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
        """
        The margin that must be held in order to increase the position by the provided quantity
        
        :param parameters: An object containing the security and quantity
        :returns: The initial margin required for the provided security and quantity.
        """
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
        Gets the margin currently allocated to the specified holding
        
        :param parameters: An object containing the security
        :returns: The maintenance margin required for the provided holdings quantity/cost/value.
        """
        ...

    def GetMaximumOrderQuantityForDeltaBuyingPower(self, parameters: QuantConnect.Securities.GetMaximumOrderQuantityForDeltaBuyingPowerParameters) -> QuantConnect.Securities.GetMaximumOrderQuantityResult:
        """
        Get the maximum market order quantity to obtain a delta in the buying power used by a security.
        The deltas sign defines the position side to apply it to, positive long, negative short.
        
        :param parameters: An object containing the portfolio, the security and the delta buying power
        :returns: Returns the maximum allowed market order quantity and if zero, also the reason.
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

    def GetReservedBuyingPowerForPosition(self, parameters: QuantConnect.Securities.ReservedBuyingPowerForPositionParameters) -> QuantConnect.Securities.ReservedBuyingPowerForPosition:
        """
        Gets the amount of buying power reserved to maintain the specified position
        
        :param parameters: A parameters object containing the security
        :returns: The reserved buying power in account currency.
        """
        ...

    def HasSufficientBuyingPowerForOrder(self, parameters: QuantConnect.Securities.HasSufficientBuyingPowerForOrderParameters) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """
        Check if there is sufficient buying power to execute this order.
        
        :param parameters: An object containing the portfolio, the security and the order
        :returns: Returns buying power information for an order.
        """
        ...

    def SetLeverage(self, security: QuantConnect.Securities.Security, leverage: float) -> None:
        """
        Sets the leverage for the applicable securities, i.e, equities
        
        :param security: The security to set leverage for
        :param leverage: The new leverage
        """
        ...


class PythonWrapper(System.Object):
    """Provides extension methods for managing python wrapper classes"""

    @staticmethod
    def ValidateImplementationOf(model: typing.Any) -> typing.Any:
        """
        Validates that the specified PyObject completely implements the provided interface type
        
        :param model: The model implementing the interface type
        """
        ...


class PandasConverter(System.Object):
    """Collection of methods that converts lists of objects in pandas.DataFrame"""

    def __init__(self) -> None:
        """Creates an instance of PandasConverter."""
        ...

    @overload
    def GetDataFrame(self, data: System.Collections.Generic.IEnumerable[QuantConnect.Data.Slice], dataType: typing.Type = None) -> pandas.DataFrame:
        """
        Converts an enumerable of Slice in a pandas.DataFrame
        
        :param data: Enumerable of Slice
        :param dataType: Optional type of bars to add to the data frame
        :returns: PyObject containing a pandas.DataFrame.
        """
        ...

    @overload
    def GetDataFrame(self, data: System.Collections.Generic.IEnumerable[QuantConnect_Python_PandasConverter_GetDataFrame_T]) -> pandas.DataFrame:
        """
        Converts an enumerable of IBaseData in a pandas.DataFrame
        
        :param data: Enumerable of Slice
        :returns: PyObject containing a pandas.DataFrame.
        """
        ...

    @overload
    def GetIndicatorDataFrame(self, data: System.Collections.Generic.IDictionary[str, System.Collections.Generic.List[QuantConnect.Indicators.IndicatorDataPoint]]) -> pandas.DataFrame:
        """
        Converts a dictionary with a list of IndicatorDataPoint in a pandas.DataFrame
        
        :param data: Dictionary with a list of IndicatorDataPoint
        :returns: PyObject containing a pandas.DataFrame.
        """
        ...

    @overload
    def GetIndicatorDataFrame(self, data: typing.Any) -> pandas.DataFrame:
        """
        Converts a dictionary with a list of IndicatorDataPoint in a pandas.DataFrame
        
        :param data: PyObject that should be a dictionary (convertible to PyDict) of string to list of IndicatorDataPoint
        :returns: PyObject containing a pandas.DataFrame.
        """
        ...

    def ToString(self) -> str:
        """Returns a string that represent the current object"""
        ...


class SlippageModelPythonWrapper(System.Object, QuantConnect.Orders.Slippage.ISlippageModel):
    """Wraps a PyObject object that represents a model that simulates market order slippage"""

    def __init__(self, model: typing.Any) -> None:
        """
        Constructor for initialising the SlippageModelPythonWrapper class with wrapped PyObject object
        
        :param model: Represents a model that simulates market order slippage
        """
        ...

    def GetSlippageApproximation(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> float:
        """
        Slippage Model. Return a decimal cash slippage approximation on the order.
        
        :param asset: The security matching the order
        :param order: The order to compute slippage for
        :returns: The slippage of the order in units of the account currency.
        """
        ...


class MarginCallModelPythonWrapper(System.Object, QuantConnect.Securities.IMarginCallModel):
    """Provides a margin call model that wraps a PyObject object that represents the model responsible for picking which orders should be executed during a margin call"""

    def __init__(self, model: typing.Any) -> None:
        """
        Constructor for initialising the MarginCallModelPythonWrapper class with wrapped PyObject object
        
        :param model: Represents the model responsible for picking which orders should be executed during a margin call
        """
        ...

    def ExecuteMarginCall(self, generatedMarginCallOrders: System.Collections.Generic.IEnumerable[QuantConnect.Orders.SubmitOrderRequest]) -> System.Collections.Generic.List[QuantConnect.Orders.OrderTicket]:
        """
        Executes synchronous orders to bring the account within margin requirements.
        
        :param generatedMarginCallOrders: These are the margin call orders that were generated by individual security margin models.
        :returns: The list of orders that were actually executed.
        """
        ...

    def GetMarginCallOrders(self, issueMarginCallWarning: typing.Optional[bool]) -> typing.Union[System.Collections.Generic.List[QuantConnect.Orders.SubmitOrderRequest], bool]:
        """
        Scan the portfolio and the updated data for a potential margin call situation which may get the holdings below zero!
        If there is a margin call, liquidate the portfolio immediately before the portfolio gets sub zero.
        
        :param issueMarginCallWarning: Set to true if a warning should be issued to the algorithm
        :returns: True for a margin call on the holdings.
        """
        ...


class PythonData(QuantConnect.Data.DynamicData):
    """
    Dynamic data class for Python algorithms.
    Stores properties of python instances in DynamicData dictionary
    """

    @property
    def EndTime(self) -> datetime.datetime:
        """
        The end time of this data. Some data covers spans (trade bars)
        and as such we want to know the entire time span covered
        """
        ...

    @EndTime.setter
    def EndTime(self, value: datetime.datetime):
        """
        The end time of this data. Some data covers spans (trade bars)
        and as such we want to know the entire time span covered
        """
        ...

    def __getitem__(self, index: str) -> typing.Any:
        """
        Indexes into this PythonData, where index is key to the dynamic property
        
        :param index: the index
        :returns: Dynamic property of a given index.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Constructor for initializing the PythonData class"""
        ...

    @overload
    def __init__(self, pythonData: typing.Any) -> None:
        """Constructor for initializing the PythonData class with wrapped PyObject"""
        ...

    def __setitem__(self, index: str, value: typing.Any) -> None:
        """
        Indexes into this PythonData, where index is key to the dynamic property
        
        :param index: the index
        :returns: Dynamic property of a given index.
        """
        ...

    def DefaultResolution(self) -> int:
        """
        Gets the default resolution for this data and security type
        
        :returns: This method returns the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Source Locator for algorithm written in Python.
        
        :param config: Subscription configuration object
        :param date: Date of the data file we're looking for
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: STRING API Url.
        """
        ...

    def IsOfType(self, type: typing.Type) -> bool:
        """
        Helper method to determine if the current instance is of the provided type
        
        :param type: Target type to check against
        :returns: True if this instance is of the provided type.
        """
        ...

    def IsSparseData(self) -> bool:
        """
        Indicates that the data set is expected to be sparse
        
        :returns: True if the data set represented by this type is expected to be sparse.
        """
        ...

    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        """
        Generic Reader Implementation for Python Custom Data.
        
        :param config: Subscription configuration
        :param line: CSV line of data from the source
        :param date: Date of the requested line
        :param isLiveMode: true if we're in live mode, false for backtesting mode
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


class DataConsolidatorPythonWrapper(System.Object, QuantConnect.Data.Consolidators.IDataConsolidator):
    """Provides an Data Consolidator that wraps a PyObject object that represents a custom Python consolidator"""

    @property
    def Consolidated(self) -> QuantConnect.Data.IBaseData:
        """
        Gets the most recently consolidated piece of data. This will be null if this consolidator
        has not produced any data yet.
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

    def __init__(self, consolidator: typing.Any) -> None:
        """
        Constructor for initialising the DataConsolidatorPythonWrapper class with wrapped PyObject object
        
        :param consolidator: Represents a custom python consolidator
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

    def Update(self, data: QuantConnect.Data.IBaseData) -> None:
        """
        Updates this consolidator with the specified data
        
        :param data: The new data for the consolidator
        """
        ...


class BrokerageMessageHandlerPythonWrapper(System.Object, QuantConnect.Brokerages.IBrokerageMessageHandler):
    """Provides a wrapper for IBrokerageMessageHandler implementations written in python"""

    def __init__(self, model: typing.Any) -> None:
        """
        Initializes a new instance of the BrokerageMessageHandlerPythonWrapper class
        
        :param model: The python implementation of IBrokerageMessageHandler
        """
        ...

    def Handle(self, message: QuantConnect.Brokerages.BrokerageMessageEvent) -> None:
        """
        Handles the message
        
        :param message: The message to be handled
        """
        ...


class SecurityInitializerPythonWrapper(System.Object, QuantConnect.Securities.ISecurityInitializer):
    """Wraps a PyObject object that represents a type capable of initializing a new security"""

    def __init__(self, model: typing.Any) -> None:
        """
        Constructor for initialising the SecurityInitializerPythonWrapper class with wrapped PyObject object
        
        :param model: Represents a type capable of initializing a new security
        """
        ...

    def Initialize(self, security: QuantConnect.Securities.Security) -> None:
        """
        Initializes the specified security
        
        :param security: The security to be initialized
        """
        ...


class VolatilityModelPythonWrapper(QuantConnect.Securities.Volatility.BaseVolatilityModel):
    """Provides a volatility model that wraps a PyObject object that represents a model that computes the volatility of a security"""

    @property
    def Volatility(self) -> float:
        """Gets the volatility of the security as a percentage"""
        ...

    def __init__(self, model: typing.Any) -> None:
        """
        Constructor for initialising the VolatilityModelPythonWrapper class with wrapped PyObject object
        
        :param model: Represents a model that computes the volatility of a security
        """
        ...

    def GetHistoryRequirements(self, security: QuantConnect.Securities.Security, utcTime: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.HistoryRequest]:
        """
        Returns history requirements for the volatility model expressed in the form of history request
        
        :param security: The security of the request
        :param utcTime: The date/time of the request
        :returns: History request object list, or empty if no requirements.
        """
        ...

    def SetSubscriptionDataConfigProvider(self, subscriptionDataConfigProvider: QuantConnect.Interfaces.ISubscriptionDataConfigProvider) -> None:
        """
        Sets the ISubscriptionDataConfigProvider instance to use.
        
        :param subscriptionDataConfigProvider: Provides access to registered SubscriptionDataConfig
        """
        ...

    def Update(self, security: QuantConnect.Securities.Security, data: QuantConnect.Data.BaseData) -> None:
        """
        Updates this model using the new price information in
        the specified security instance
        
        :param security: The security to calculate volatility for
        :param data: The new data used to update the model
        """
        ...


class PythonConsolidator(System.Object):
    """Provides a base class for python consolidators, necessary to use event handler."""

    @property
    def DataConsolidated(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.IBaseData], None], None]:
        """Event handler that fires when a new piece of data is produced"""
        ...

    @DataConsolidated.setter
    def DataConsolidated(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Data.IBaseData], None], None]):
        """Event handler that fires when a new piece of data is produced"""
        ...

    def OnDataConsolidated(self, consolidator: typing.Any, data: QuantConnect.Data.IBaseData) -> None:
        """
        Function to invoke the event handler
        
        :param consolidator: Reference to the consolidator itself
        :param data: The finished data from the consolidator
        """
        ...


class FeeModelPythonWrapper(QuantConnect.Orders.Fees.FeeModel):
    """Provides an order fee model that wraps a PyObject object that represents a model that simulates order fees"""

    def __init__(self, model: typing.Any) -> None:
        """
        Constructor for initialising the FeeModelPythonWrapper class with wrapped PyObject object
        
        :param model: Represents a model that simulates order fees
        """
        ...

    def GetOrderFee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in units of the account currency.
        """
        ...


class PythonActivator(System.Object):
    """Provides methods for creating new instances of python custom data objects"""

    @property
    def Type(self) -> typing.Type:
        """System.Type of the object we wish to create"""
        ...

    @property
    def Factory(self) -> typing.Callable[[typing.List[System.Object]], System.Object]:
        """Method to return an instance of object"""
        ...

    def __init__(self, type: typing.Type, value: typing.Any) -> None:
        """
        Creates a new instance of PythonActivator
        
        :param type: System.Type of the object we wish to create
        :param value: PyObject that contains the python type
        """
        ...


class FillModelPythonWrapper(QuantConnect.Orders.Fills.FillModel):
    """Wraps a PyObject object that represents a model that simulates order fill events"""

    def __init__(self, model: typing.Any) -> None:
        """
        Constructor for initialising the FillModelPythonWrapper class with wrapped PyObject object
        
        :param model: Represents a model that simulates order fill events
        """
        ...

    def Fill(self, parameters: QuantConnect.Orders.Fills.FillModelParameters) -> QuantConnect.Orders.Fills.Fill:
        """
        Return an order event with the fill details
        
        :param parameters: A parameters object containing the security and order
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...

    def GetPrices(self, asset: QuantConnect.Securities.Security, direction: QuantConnect.Orders.OrderDirection) -> QuantConnect.Orders.Fills.Prices:
        """
        Get the minimum and maximum price for this security in the last bar:
        
        This method is protected.
        
        :param asset: Security asset we're checking
        :param direction: The order direction, decides whether to pick bid or ask
        """
        ...

    def LimitFill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.LimitOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Limit Fill Model. Return an order event with the fill details.
        
        :param asset: Stock Object to use to help model limit fill
        :param order: Order to fill. Alter the values directly if filled.
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...

    def LimitIfTouchedFill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.LimitIfTouchedOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Limit if Touched Fill Model. Return an order event with the fill details.
        
        :param asset: Asset we're trading this order
        :param order: LimitIfTouchedOrder Order to Check, return filled if true
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...

    def MarketFill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.MarketOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Model the slippage on a market order: fixed percentage of order price
        
        :param asset: Asset we're trading this order
        :param order: Order to update
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...

    def MarketOnCloseFill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.MarketOnCloseOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Market on Close Fill Model. Return an order event with the fill details
        
        :param asset: Asset we're trading with this order
        :param order: Order to be filled
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...

    def MarketOnOpenFill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.MarketOnOpenOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Market on Open Fill Model. Return an order event with the fill details
        
        :param asset: Asset we're trading with this order
        :param order: Order to be filled
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...

    def StopLimitFill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.StopLimitOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Stop Limit Fill Model. Return an order event with the fill details.
        
        :param asset: Asset we're trading this order
        :param order: Stop Limit Order to Check, return filled if true
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...

    def StopMarketFill(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.StopMarketOrder) -> QuantConnect.Orders.OrderEvent:
        """
        Stop Market Fill Model. Return an order event with the fill details.
        
        :param asset: Asset we're trading this order
        :param order: Stop Order to Check, return filled if true
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...


class BrokerageModelPythonWrapper(System.Object, QuantConnect.Brokerages.IBrokerageModel):
    """Provides an implementation of IBrokerageModel that wraps a PyObject object"""

    @property
    def AccountType(self) -> int:
        """
        Gets or sets the account type used by this model
        
        This property contains the int value of a member of the QuantConnect.AccountType enum.
        """
        ...

    @property
    def RequiredFreeBuyingPowerPercent(self) -> float:
        """
        Gets the brokerages model percentage factor used to determine the required unused buying power for the account.
        From 1 to 0. Example: 0 means no unused buying power is required. 0.5 means 50% of the buying power should be left unused.
        """
        ...

    @property
    def DefaultMarkets(self) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect.SecurityType, str]:
        """Gets a map of the default markets to be used for each security type"""
        ...

    def __init__(self, model: typing.Any) -> None:
        """
        Constructor for initialising the BrokerageModelPythonWrapper class with wrapped PyObject object
        
        :param model: Models brokerage transactions, fees, and order
        """
        ...

    def ApplySplit(self, tickets: System.Collections.Generic.List[QuantConnect.Orders.OrderTicket], split: QuantConnect.Data.Market.Split) -> None:
        """
        Applies the split to the specified order ticket
        
        :param tickets: The open tickets matching the split event
        :param split: The split event data
        """
        ...

    def CanExecuteOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> bool:
        """
        Returns true if the brokerage would be able to execute this order at this time assuming
        market prices are sufficient for the fill to take place. This is used to emulate the
        brokerage fills in backtesting and paper trading. For example some brokerages may not perform
        executions during extended market hours. This is not intended to be checking whether or not
        the exchange is open, that is handled in the Security.Exchange property.
        
        :param security: The security being ordered
        :param order: The order to test for execution
        :returns: True if the brokerage would be able to perform the execution, false otherwise.
        """
        ...

    def CanSubmitOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage could accept this order. This takes into account
        order type, security type, and order size limits.
        
        :param security: The security being ordered
        :param order: The order to be processed
        :param message: If this function returns false, a brokerage message detailing why the order may not be submitted
        :returns: True if the brokerage could process the order, false otherwise.
        """
        ...

    def CanUpdateOrder(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order, request: QuantConnect.Orders.UpdateOrderRequest, message: typing.Optional[QuantConnect.Brokerages.BrokerageMessageEvent]) -> typing.Union[bool, QuantConnect.Brokerages.BrokerageMessageEvent]:
        """
        Returns true if the brokerage would allow updating the order as specified by the request
        
        :param security: The security of the order
        :param order: The order to be updated
        :param request: The requested updated to be made to the order
        :param message: If this function returns false, a brokerage message detailing why the order may not be updated
        :returns: True if the brokerage would allow updating the order, false otherwise.
        """
        ...

    def GetBenchmark(self, securities: QuantConnect.Securities.SecurityManager) -> QuantConnect.Benchmarks.IBenchmark:
        """
        Get the benchmark for this model
        
        :param securities: SecurityService to create the security with if needed
        :returns: The benchmark for this brokerage.
        """
        ...

    @overload
    def GetBuyingPowerModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.IBuyingPowerModel:
        """
        Gets a new buying power model for the security, returning the default model with the security's configured leverage.
        For cash accounts, leverage = 1 is used.
        
        :param security: The security to get a buying power model for
        :returns: The buying power model for this brokerage/security.
        """
        ...

    @overload
    def GetBuyingPowerModel(self, security: QuantConnect.Securities.Security, accountType: QuantConnect.AccountType) -> QuantConnect.Securities.IBuyingPowerModel:
        """
        Gets a new buying power model for the security
        
        Flagged deprecated and will remove December 1st 2018
        
        :param security: The security to get a buying power model for
        :param accountType: The account type
        :returns: The buying power model for this brokerage/security.
        """
        ...

    def GetFeeModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fees.IFeeModel:
        """
        Gets a new fee model that represents this brokerage's fee structure
        
        :param security: The security to get a fee model for
        :returns: The new fee model for this brokerage.
        """
        ...

    def GetFillModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Fills.IFillModel:
        """
        Gets a new fill model that represents this brokerage's fill behavior
        
        :param security: The security to get fill model for
        :returns: The new fill model for this brokerage.
        """
        ...

    def GetLeverage(self, security: QuantConnect.Securities.Security) -> float:
        """
        Gets the brokerage's leverage for the specified security
        
        :param security: The security's whose leverage we seek
        :returns: The leverage for the specified security.
        """
        ...

    def GetModel(self) -> QuantConnect.Brokerages.IBrokerageModel:
        """
        Convenience method to get the underlying IBrokerageModel object from the wrapper.
        
        :returns: Underlying IBrokerageModel object.
        """
        ...

    @overload
    def GetSettlementModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.ISettlementModel:
        """
        Gets a new settlement model for the security
        
        :param security: The security to get a settlement model for
        :returns: The settlement model for this brokerage.
        """
        ...

    @overload
    def GetSettlementModel(self, security: QuantConnect.Securities.Security, accountType: QuantConnect.AccountType) -> QuantConnect.Securities.ISettlementModel:
        """
        Gets a new settlement model for the security
        
        Flagged deprecated and will remove December 1st 2018
        
        :param security: The security to get a settlement model for
        :param accountType: The account type
        :returns: The settlement model for this brokerage.
        """
        ...

    def GetShortableProvider(self) -> QuantConnect.Interfaces.IShortableProvider:
        """
        Gets the shortable provider
        
        :returns: Shortable provider.
        """
        ...

    def GetSlippageModel(self, security: QuantConnect.Securities.Security) -> QuantConnect.Orders.Slippage.ISlippageModel:
        """
        Gets a new slippage model that represents this brokerage's fill slippage behavior
        
        :param security: The security to get a slippage model for
        :returns: The new slippage model for this brokerage.
        """
        ...

    def Shortable(self, algorithm: QuantConnect.Interfaces.IAlgorithm, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float) -> bool:
        """
        Determine if this symbol is shortable
        
        :param algorithm: The algorithm running
        :param symbol: The symbol to short
        :param quantity: The amount to short
        """
        ...


class PandasData(System.Object):
    """Organizes a list of data to create pandas.DataFrames"""

    @property
    def IsCustomData(self) -> bool:
        """Gets true if this is a custom data request, false for normal QC data"""
        ...

    @property
    def Levels(self) -> int:
        """Implied levels of a multi index pandas.Series (depends on the security type)"""
        ...

    def __init__(self, data: typing.Any) -> None:
        """Initializes an instance of PandasData"""
        ...

    @overload
    def Add(self, baseData: typing.Any) -> None:
        """
        Adds security data object to the end of the lists
        
        :param baseData: IBaseData object that contains security data
        """
        ...

    @overload
    def Add(self, ticks: System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.Tick], tradeBar: QuantConnect.Data.Market.TradeBar, quoteBar: QuantConnect.Data.Market.QuoteBar) -> None:
        """
        Adds Lean data objects to the end of the lists
        
        :param ticks: List of Tick object that contains tick information of the security
        :param tradeBar: TradeBar object that contains trade bar information of the security
        :param quoteBar: QuoteBar object that contains quote bar information of the security
        """
        ...

    def ToPandasDataFrame(self, levels: int = 2) -> pandas.DataFrame:
        """
        Get the pandas.DataFrame of the current PandasData state
        
        :param levels: Number of levels of the multi index
        :returns: pandas.DataFrame object.
        """
        ...


class PythonQuandl(QuantConnect.DataSource.NasdaqDataLink):
    """Dynamic data class for Python algorithms."""

    def __init__(self) -> None:
        """Constructor for initialising the PythonQuandl class"""
        ...


class _EventContainer(typing.Generic[QuantConnect_Python__EventContainer_Callable, QuantConnect_Python__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Python__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Python__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Python__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


