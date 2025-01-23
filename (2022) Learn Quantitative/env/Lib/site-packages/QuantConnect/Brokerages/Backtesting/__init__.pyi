from typing import overload
import abc
import typing

import QuantConnect
import QuantConnect.Brokerages
import QuantConnect.Brokerages.Backtesting
import QuantConnect.Data.Market
import QuantConnect.Interfaces
import QuantConnect.Orders
import QuantConnect.Packets
import QuantConnect.Securities
import QuantConnect.Securities.Option
import System
import System.Collections.Generic


class IBacktestingMarketSimulation(metaclass=abc.ABCMeta):
    """Backtesting Market Simulation interface, that must be implemented by all simulators of market conditions run during backtest"""

    def SimulateMarketConditions(self, brokerage: QuantConnect.Interfaces.IBrokerage, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """
        Method is called by backtesting brokerage to simulate market conditions.
        
        :param brokerage: Backtesting brokerage instance
        :param algorithm: Algorithm instance
        """
        ...


class BacktestingBrokerage(QuantConnect.Brokerages.Brokerage):
    """Represents a brokerage to be used during backtesting. This is intended to be only be used with the BacktestingTransactionHandler"""

    @property
    def Algorithm(self) -> QuantConnect.Interfaces.IAlgorithm:
        """
        This is the algorithm under test
        
        This field is protected.
        """
        ...

    @property
    def IsConnected(self) -> bool:
        """Gets the connection status"""
        ...

    @property
    def MarketSimulation(self) -> QuantConnect.Brokerages.Backtesting.IBacktestingMarketSimulation:
        """Market Simulation - simulates various market conditions in backtest"""
        ...

    @MarketSimulation.setter
    def MarketSimulation(self, value: QuantConnect.Brokerages.Backtesting.IBacktestingMarketSimulation):
        """Market Simulation - simulates various market conditions in backtest"""
        ...

    @overload
    def __init__(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """
        Creates a new BacktestingBrokerage for the specified algorithm
        
        :param algorithm: The algorithm instance
        """
        ...

    @overload
    def __init__(self, algorithm: QuantConnect.Interfaces.IAlgorithm, name: str) -> None:
        """
        Creates a new BacktestingBrokerage for the specified algorithm
        
        This method is protected.
        
        :param algorithm: The algorithm instance
        :param name: The name of the brokerage
        """
        ...

    @overload
    def __init__(self, algorithm: QuantConnect.Interfaces.IAlgorithm, marketSimulation: QuantConnect.Brokerages.Backtesting.IBacktestingMarketSimulation) -> None:
        """
        Creates a new BacktestingBrokerage for the specified algorithm. Adds market simulation to BacktestingBrokerage;
        
        :param algorithm: The algorithm instance
        :param marketSimulation: The backtesting market simulation instance
        """
        ...

    def ActivateOptionAssignment(self, option: QuantConnect.Securities.Option.Option, quantity: int) -> None:
        """
        This method is called by market simulator in order to launch an assignment event
        
        :param option: Option security to assign
        :param quantity: Quantity to assign
        """
        ...

    def CancelOrder(self, order: QuantConnect.Orders.Order) -> bool:
        """
        Cancels the order with the specified ID
        
        :param order: The order to cancel
        :returns: True if the request was made for the order to be canceled, false otherwise.
        """
        ...

    def Connect(self) -> None:
        """The BacktestingBrokerage is always connected. This is a no-op."""
        ...

    def Disconnect(self) -> None:
        """The BacktestingBrokerage is always connected. This is a no-op."""
        ...

    def GetAccountHoldings(self) -> System.Collections.Generic.List[QuantConnect.Holding]:
        """
        Gets all holdings for the account
        
        :returns: The current holdings from the account.
        """
        ...

    def GetCashBalance(self) -> System.Collections.Generic.List[QuantConnect.Securities.CashAmount]:
        """
        Gets the current cash balance for each currency held in the brokerage account
        
        :returns: The current cash balance for each currency available for trading.
        """
        ...

    def GetOpenOrders(self) -> System.Collections.Generic.List[QuantConnect.Orders.Order]:
        """
        Gets all open orders on the account
        
        :returns: The open orders returned from IB.
        """
        ...

    def OnOrderEvent(self, e: QuantConnect.Orders.OrderEvent) -> None:
        """
        Event invocator for the OrderFilled event
        
        This method is protected.
        
        :param e: The OrderEvent
        """
        ...

    def PlaceOrder(self, order: QuantConnect.Orders.Order) -> bool:
        """
        Places a new order and assigns a new broker ID to the order
        
        :param order: The order to be placed
        :returns: True if the request for a new order has been placed, false otherwise.
        """
        ...

    def ProcessDelistings(self, delistings: QuantConnect.Data.Market.Delistings) -> None:
        """
        Process delistings
        
        :param delistings: Delistings to process
        """
        ...

    def Scan(self) -> None:
        """Scans all the outstanding orders and applies the algorithm model fills to generate the order events"""
        ...

    def SimulateMarket(self) -> None:
        """Runs market simulation"""
        ...

    def UpdateOrder(self, order: QuantConnect.Orders.Order) -> bool:
        """
        Updates the order with the same ID
        
        :param order: The new order information
        :returns: True if the request was made for the order to be updated, false otherwise.
        """
        ...


class BacktestingBrokerageFactory(QuantConnect.Brokerages.BrokerageFactory):
    """Factory type for the BacktestingBrokerage"""

    @property
    def BrokerageData(self) -> System.Collections.Generic.Dictionary[str, str]:
        """Gets the brokerage data required to run the IB brokerage from configuration"""
        ...

    def __init__(self) -> None:
        """Initializes a new instance of the BacktestingBrokerageFactory class"""
        ...

    def CreateBrokerage(self, job: QuantConnect.Packets.LiveNodePacket, algorithm: QuantConnect.Interfaces.IAlgorithm) -> QuantConnect.Interfaces.IBrokerage:
        """
        Creates a new IBrokerage instance
        
        :param job: The job packet to create the brokerage for
        :param algorithm: The algorithm instance
        :returns: A new brokerage instance.
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def GetBrokerageModel(self, orderProvider: QuantConnect.Securities.IOrderProvider) -> QuantConnect.Brokerages.IBrokerageModel:
        """
        Gets a new instance of the InteractiveBrokersBrokerageModel
        
        :param orderProvider: The order provider
        """
        ...


class BasicOptionAssignmentSimulation(System.Object, QuantConnect.Brokerages.Backtesting.IBacktestingMarketSimulation):
    """
    This market conditions simulator emulates exercising of short option positions in the portfolio.
    Simulator implements basic no-arb argument: when time value of the option contract is close to zero
    it assigns short legs getting profit close to expiration dates in deep ITM positions. User algorithm then receives
    assignment event from LEAN. Simulator randomly scans for arbitrage opportunities every two hours or so.
    """

    def IsReadyToSimulate(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> bool:
        """We generate a list of time points when we would like to run our simulation. we then return true if the time is in the list."""
        ...

    def SimulateMarketConditions(self, brokerage: QuantConnect.Interfaces.IBrokerage, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """
        We simulate activity of market makers on expiration. Trying to get profit close to expiration dates in deep ITM positions.
        This version of the simulator exercises short positions in full.
        """
        ...


