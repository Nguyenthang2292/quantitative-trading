from typing import overload
import QuantConnect
import QuantConnect.Brokerages
import QuantConnect.Brokerages.Backtesting
import QuantConnect.Brokerages.Paper
import QuantConnect.Interfaces
import QuantConnect.Packets
import QuantConnect.Securities
import System.Collections.Generic


class PaperBrokerage(QuantConnect.Brokerages.Backtesting.BacktestingBrokerage):
    """Paper Trading Brokerage"""

    def __init__(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.LiveNodePacket) -> None:
        """
        Creates a new PaperBrokerage
        
        :param algorithm: The algorithm under analysis
        :param job: The job packet
        """
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

    def Scan(self) -> None:
        """
        Scans all the outstanding orders and applies the algorithm model fills to generate the order events.
        This override adds dividend detection and application
        """
        ...


class PaperBrokerageFactory(QuantConnect.Brokerages.BrokerageFactory):
    """The factory type for the PaperBrokerage"""

    @property
    def BrokerageData(self) -> System.Collections.Generic.Dictionary[str, str]:
        """Gets the brokerage data required to run the IB brokerage from configuration"""
        ...

    def __init__(self) -> None:
        """Initializes a new instance of the PaperBrokerageFactory class"""
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


