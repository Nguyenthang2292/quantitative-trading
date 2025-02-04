from typing import overload
import datetime
import typing

import QuantConnect
import QuantConnect.Interfaces
import QuantConnect.Orders
import QuantConnect.Statistics
import System
import System.Collections.Generic


class FillGroupingMethod(System.Enum):
    """The method used to group order fills into trades"""

    FillToFill = 0
    """A Trade is defined by a fill that establishes or increases a position and an offsetting fill that reduces the position size (0)"""

    FlatToFlat = 1
    """A Trade is defined by a sequence of fills, from a flat position to a non-zero position which may increase or decrease in quantity, and back to a flat position (1)"""

    FlatToReduced = 2
    """A Trade is defined by a sequence of fills, from a flat position to a non-zero position and an offsetting fill that reduces the position size (2)"""


class FillMatchingMethod(System.Enum):
    """The method used to match offsetting order fills"""

    FIFO = 0
    """First In First Out fill matching method (0)"""

    LIFO = 1
    """Last In Last Out fill matching method (1)"""


class Trade(System.Object):
    """Represents a closed trade"""

    @property
    def Symbol(self) -> QuantConnect.Symbol:
        """The symbol of the traded instrument"""
        ...

    @Symbol.setter
    def Symbol(self, value: QuantConnect.Symbol):
        """The symbol of the traded instrument"""
        ...

    @property
    def EntryTime(self) -> datetime.datetime:
        """The date and time the trade was opened"""
        ...

    @EntryTime.setter
    def EntryTime(self, value: datetime.datetime):
        """The date and time the trade was opened"""
        ...

    @property
    def EntryPrice(self) -> float:
        """The price at which the trade was opened (or the average price if multiple entries)"""
        ...

    @EntryPrice.setter
    def EntryPrice(self, value: float):
        """The price at which the trade was opened (or the average price if multiple entries)"""
        ...

    @property
    def Direction(self) -> int:
        """
        The direction of the trade (Long or Short)
        
        This property contains the int value of a member of the QuantConnect.Statistics.TradeDirection enum.
        """
        ...

    @Direction.setter
    def Direction(self, value: int):
        """
        The direction of the trade (Long or Short)
        
        This property contains the int value of a member of the QuantConnect.Statistics.TradeDirection enum.
        """
        ...

    @property
    def Quantity(self) -> float:
        """The total unsigned quantity of the trade"""
        ...

    @Quantity.setter
    def Quantity(self, value: float):
        """The total unsigned quantity of the trade"""
        ...

    @property
    def ExitTime(self) -> datetime.datetime:
        """The date and time the trade was closed"""
        ...

    @ExitTime.setter
    def ExitTime(self, value: datetime.datetime):
        """The date and time the trade was closed"""
        ...

    @property
    def ExitPrice(self) -> float:
        """The price at which the trade was closed (or the average price if multiple exits)"""
        ...

    @ExitPrice.setter
    def ExitPrice(self, value: float):
        """The price at which the trade was closed (or the average price if multiple exits)"""
        ...

    @property
    def ProfitLoss(self) -> float:
        """The gross profit/loss of the trade (as account currency)"""
        ...

    @ProfitLoss.setter
    def ProfitLoss(self, value: float):
        """The gross profit/loss of the trade (as account currency)"""
        ...

    @property
    def TotalFees(self) -> float:
        """The total fees associated with the trade (always positive value) (as account currency)"""
        ...

    @TotalFees.setter
    def TotalFees(self, value: float):
        """The total fees associated with the trade (always positive value) (as account currency)"""
        ...

    @property
    def MAE(self) -> float:
        """The Maximum Adverse Excursion (as account currency)"""
        ...

    @MAE.setter
    def MAE(self, value: float):
        """The Maximum Adverse Excursion (as account currency)"""
        ...

    @property
    def MFE(self) -> float:
        """The Maximum Favorable Excursion (as account currency)"""
        ...

    @MFE.setter
    def MFE(self, value: float):
        """The Maximum Favorable Excursion (as account currency)"""
        ...

    @property
    def Duration(self) -> datetime.timedelta:
        """Returns the duration of the trade"""
        ...

    @property
    def EndTradeDrawdown(self) -> float:
        """Returns the amount of profit given back before the trade was closed"""
        ...


class TradeBuilder(System.Object, QuantConnect.Interfaces.ITradeBuilder):
    """The TradeBuilder class generates trades from executions and market price updates"""

    @property
    def ClosedTrades(self) -> System.Collections.Generic.List[QuantConnect.Statistics.Trade]:
        """The list of closed trades"""
        ...

    def __init__(self, groupingMethod: QuantConnect.Statistics.FillGroupingMethod, matchingMethod: QuantConnect.Statistics.FillMatchingMethod) -> None:
        """Initializes a new instance of the TradeBuilder class"""
        ...

    def HasOpenPosition(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Returns true if there is an open position for the symbol
        
        :param symbol: The symbol
        :returns: true if there is an open position for the symbol.
        """
        ...

    def ProcessFill(self, fill: QuantConnect.Orders.OrderEvent, conversionRate: float, feeInAccountCurrency: float, multiplier: float = 1.0) -> None:
        """
        Processes a new fill, eventually creating new trades
        
        :param fill: The new fill order event
        :param conversionRate: The current security market conversion rate into the account currency
        :param feeInAccountCurrency: The current order fee in the account currency
        :param multiplier: The contract multiplier
        """
        ...

    def SetLiveMode(self, live: bool) -> None:
        """
        Sets the live mode flag
        
        :param live: The live mode flag
        """
        ...

    def SetMarketPrice(self, symbol: typing.Union[QuantConnect.Symbol, str], price: float) -> None:
        """Sets the current market price for the symbol"""
        ...


class TradeStatistics(System.Object):
    """The TradeStatistics class represents a set of statistics calculated from a list of closed trades"""

    @property
    def StartDateTime(self) -> typing.Optional[datetime.datetime]:
        """The entry date/time of the first trade"""
        ...

    @StartDateTime.setter
    def StartDateTime(self, value: typing.Optional[datetime.datetime]):
        """The entry date/time of the first trade"""
        ...

    @property
    def EndDateTime(self) -> typing.Optional[datetime.datetime]:
        """The exit date/time of the last trade"""
        ...

    @EndDateTime.setter
    def EndDateTime(self, value: typing.Optional[datetime.datetime]):
        """The exit date/time of the last trade"""
        ...

    @property
    def TotalNumberOfTrades(self) -> int:
        """The total number of trades"""
        ...

    @TotalNumberOfTrades.setter
    def TotalNumberOfTrades(self, value: int):
        """The total number of trades"""
        ...

    @property
    def NumberOfWinningTrades(self) -> int:
        """The total number of winning trades"""
        ...

    @NumberOfWinningTrades.setter
    def NumberOfWinningTrades(self, value: int):
        """The total number of winning trades"""
        ...

    @property
    def NumberOfLosingTrades(self) -> int:
        """The total number of losing trades"""
        ...

    @NumberOfLosingTrades.setter
    def NumberOfLosingTrades(self, value: int):
        """The total number of losing trades"""
        ...

    @property
    def TotalProfitLoss(self) -> float:
        """The total profit/loss for all trades (as symbol currency)"""
        ...

    @TotalProfitLoss.setter
    def TotalProfitLoss(self, value: float):
        """The total profit/loss for all trades (as symbol currency)"""
        ...

    @property
    def TotalProfit(self) -> float:
        """The total profit for all winning trades (as symbol currency)"""
        ...

    @TotalProfit.setter
    def TotalProfit(self, value: float):
        """The total profit for all winning trades (as symbol currency)"""
        ...

    @property
    def TotalLoss(self) -> float:
        """The total loss for all losing trades (as symbol currency)"""
        ...

    @TotalLoss.setter
    def TotalLoss(self, value: float):
        """The total loss for all losing trades (as symbol currency)"""
        ...

    @property
    def LargestProfit(self) -> float:
        """The largest profit in a single trade (as symbol currency)"""
        ...

    @LargestProfit.setter
    def LargestProfit(self, value: float):
        """The largest profit in a single trade (as symbol currency)"""
        ...

    @property
    def LargestLoss(self) -> float:
        """The largest loss in a single trade (as symbol currency)"""
        ...

    @LargestLoss.setter
    def LargestLoss(self, value: float):
        """The largest loss in a single trade (as symbol currency)"""
        ...

    @property
    def AverageProfitLoss(self) -> float:
        """The average profit/loss (a.k.a. Expectancy or Average Trade) for all trades (as symbol currency)"""
        ...

    @AverageProfitLoss.setter
    def AverageProfitLoss(self, value: float):
        """The average profit/loss (a.k.a. Expectancy or Average Trade) for all trades (as symbol currency)"""
        ...

    @property
    def AverageProfit(self) -> float:
        """The average profit for all winning trades (as symbol currency)"""
        ...

    @AverageProfit.setter
    def AverageProfit(self, value: float):
        """The average profit for all winning trades (as symbol currency)"""
        ...

    @property
    def AverageLoss(self) -> float:
        """The average loss for all winning trades (as symbol currency)"""
        ...

    @AverageLoss.setter
    def AverageLoss(self, value: float):
        """The average loss for all winning trades (as symbol currency)"""
        ...

    @property
    def AverageTradeDuration(self) -> datetime.timedelta:
        """The average duration for all trades"""
        ...

    @AverageTradeDuration.setter
    def AverageTradeDuration(self, value: datetime.timedelta):
        """The average duration for all trades"""
        ...

    @property
    def AverageWinningTradeDuration(self) -> datetime.timedelta:
        """The average duration for all winning trades"""
        ...

    @AverageWinningTradeDuration.setter
    def AverageWinningTradeDuration(self, value: datetime.timedelta):
        """The average duration for all winning trades"""
        ...

    @property
    def AverageLosingTradeDuration(self) -> datetime.timedelta:
        """The average duration for all losing trades"""
        ...

    @AverageLosingTradeDuration.setter
    def AverageLosingTradeDuration(self, value: datetime.timedelta):
        """The average duration for all losing trades"""
        ...

    @property
    def MedianTradeDuration(self) -> datetime.timedelta:
        """The median duration for all trades"""
        ...

    @MedianTradeDuration.setter
    def MedianTradeDuration(self, value: datetime.timedelta):
        """The median duration for all trades"""
        ...

    @property
    def MedianWinningTradeDuration(self) -> datetime.timedelta:
        """The median duration for all winning trades"""
        ...

    @MedianWinningTradeDuration.setter
    def MedianWinningTradeDuration(self, value: datetime.timedelta):
        """The median duration for all winning trades"""
        ...

    @property
    def MedianLosingTradeDuration(self) -> datetime.timedelta:
        """The median duration for all losing trades"""
        ...

    @MedianLosingTradeDuration.setter
    def MedianLosingTradeDuration(self, value: datetime.timedelta):
        """The median duration for all losing trades"""
        ...

    @property
    def MaxConsecutiveWinningTrades(self) -> int:
        """The maximum number of consecutive winning trades"""
        ...

    @MaxConsecutiveWinningTrades.setter
    def MaxConsecutiveWinningTrades(self, value: int):
        """The maximum number of consecutive winning trades"""
        ...

    @property
    def MaxConsecutiveLosingTrades(self) -> int:
        """The maximum number of consecutive losing trades"""
        ...

    @MaxConsecutiveLosingTrades.setter
    def MaxConsecutiveLosingTrades(self, value: int):
        """The maximum number of consecutive losing trades"""
        ...

    @property
    def ProfitLossRatio(self) -> float:
        """The ratio of the average profit per trade to the average loss per trade"""
        ...

    @ProfitLossRatio.setter
    def ProfitLossRatio(self, value: float):
        """The ratio of the average profit per trade to the average loss per trade"""
        ...

    @property
    def WinLossRatio(self) -> float:
        """The ratio of the number of winning trades to the number of losing trades"""
        ...

    @WinLossRatio.setter
    def WinLossRatio(self, value: float):
        """The ratio of the number of winning trades to the number of losing trades"""
        ...

    @property
    def WinRate(self) -> float:
        """The ratio of the number of winning trades to the total number of trades"""
        ...

    @WinRate.setter
    def WinRate(self, value: float):
        """The ratio of the number of winning trades to the total number of trades"""
        ...

    @property
    def LossRate(self) -> float:
        """The ratio of the number of losing trades to the total number of trades"""
        ...

    @LossRate.setter
    def LossRate(self, value: float):
        """The ratio of the number of losing trades to the total number of trades"""
        ...

    @property
    def AverageMAE(self) -> float:
        """The average Maximum Adverse Excursion for all trades"""
        ...

    @AverageMAE.setter
    def AverageMAE(self, value: float):
        """The average Maximum Adverse Excursion for all trades"""
        ...

    @property
    def AverageMFE(self) -> float:
        """The average Maximum Favorable Excursion for all trades"""
        ...

    @AverageMFE.setter
    def AverageMFE(self, value: float):
        """The average Maximum Favorable Excursion for all trades"""
        ...

    @property
    def LargestMAE(self) -> float:
        """The largest Maximum Adverse Excursion in a single trade (as symbol currency)"""
        ...

    @LargestMAE.setter
    def LargestMAE(self, value: float):
        """The largest Maximum Adverse Excursion in a single trade (as symbol currency)"""
        ...

    @property
    def LargestMFE(self) -> float:
        """The largest Maximum Favorable Excursion in a single trade (as symbol currency)"""
        ...

    @LargestMFE.setter
    def LargestMFE(self, value: float):
        """The largest Maximum Favorable Excursion in a single trade (as symbol currency)"""
        ...

    @property
    def MaximumClosedTradeDrawdown(self) -> float:
        """The maximum closed-trade drawdown for all trades (as symbol currency)"""
        ...

    @MaximumClosedTradeDrawdown.setter
    def MaximumClosedTradeDrawdown(self, value: float):
        """The maximum closed-trade drawdown for all trades (as symbol currency)"""
        ...

    @property
    def MaximumIntraTradeDrawdown(self) -> float:
        """The maximum intra-trade drawdown for all trades (as symbol currency)"""
        ...

    @MaximumIntraTradeDrawdown.setter
    def MaximumIntraTradeDrawdown(self, value: float):
        """The maximum intra-trade drawdown for all trades (as symbol currency)"""
        ...

    @property
    def ProfitLossStandardDeviation(self) -> float:
        """The standard deviation of the profits/losses for all trades (as symbol currency)"""
        ...

    @ProfitLossStandardDeviation.setter
    def ProfitLossStandardDeviation(self, value: float):
        """The standard deviation of the profits/losses for all trades (as symbol currency)"""
        ...

    @property
    def ProfitLossDownsideDeviation(self) -> float:
        """The downside deviation of the profits/losses for all trades (as symbol currency)"""
        ...

    @ProfitLossDownsideDeviation.setter
    def ProfitLossDownsideDeviation(self, value: float):
        """The downside deviation of the profits/losses for all trades (as symbol currency)"""
        ...

    @property
    def ProfitFactor(self) -> float:
        """The ratio of the total profit to the total loss"""
        ...

    @ProfitFactor.setter
    def ProfitFactor(self, value: float):
        """The ratio of the total profit to the total loss"""
        ...

    @property
    def SharpeRatio(self) -> float:
        """The ratio of the average profit/loss to the standard deviation"""
        ...

    @SharpeRatio.setter
    def SharpeRatio(self, value: float):
        """The ratio of the average profit/loss to the standard deviation"""
        ...

    @property
    def SortinoRatio(self) -> float:
        """The ratio of the average profit/loss to the downside deviation"""
        ...

    @SortinoRatio.setter
    def SortinoRatio(self, value: float):
        """The ratio of the average profit/loss to the downside deviation"""
        ...

    @property
    def ProfitToMaxDrawdownRatio(self) -> float:
        """The ratio of the total profit/loss to the maximum closed trade drawdown"""
        ...

    @ProfitToMaxDrawdownRatio.setter
    def ProfitToMaxDrawdownRatio(self, value: float):
        """The ratio of the total profit/loss to the maximum closed trade drawdown"""
        ...

    @property
    def MaximumEndTradeDrawdown(self) -> float:
        """The maximum amount of profit given back by a single trade before exit (as symbol currency)"""
        ...

    @MaximumEndTradeDrawdown.setter
    def MaximumEndTradeDrawdown(self, value: float):
        """The maximum amount of profit given back by a single trade before exit (as symbol currency)"""
        ...

    @property
    def AverageEndTradeDrawdown(self) -> float:
        """The average amount of profit given back by all trades before exit (as symbol currency)"""
        ...

    @AverageEndTradeDrawdown.setter
    def AverageEndTradeDrawdown(self, value: float):
        """The average amount of profit given back by all trades before exit (as symbol currency)"""
        ...

    @property
    def MaximumDrawdownDuration(self) -> datetime.timedelta:
        """The maximum amount of time to recover from a drawdown (longest time between new equity highs or peaks)"""
        ...

    @MaximumDrawdownDuration.setter
    def MaximumDrawdownDuration(self, value: datetime.timedelta):
        """The maximum amount of time to recover from a drawdown (longest time between new equity highs or peaks)"""
        ...

    @property
    def TotalFees(self) -> float:
        """The sum of fees for all trades"""
        ...

    @TotalFees.setter
    def TotalFees(self, value: float):
        """The sum of fees for all trades"""
        ...

    @overload
    def __init__(self, trades: System.Collections.Generic.IEnumerable[QuantConnect.Statistics.Trade]) -> None:
        """
        Initializes a new instance of the TradeStatistics class
        
        :param trades: The list of closed trades
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the TradeStatistics class"""
        ...


class PerformanceMetrics(System.Object):
    """PerformanceMetrics contains the names of the various performance metrics used for evaluation purposes."""

    Alpha: str = "Alpha"

    AnnualStandardDeviation: str = "Annual Standard Deviation"

    AnnualVariance: str = "Annual Variance"

    AverageLoss: str = "Average Loss"

    AverageWin: str = "Average Win"

    Beta: str = "Beta"

    CompoundingAnnualReturn: str = "Compounding Annual Return"

    Drawdown: str = "Drawdown"

    EstimatedStrategyCapacity: str = "Estimated Strategy Capacity"

    Expectancy: str = "Expectancy"

    InformationRatio: str = "Information Ratio"

    LossRate: str = "Loss Rate"

    NetProfit: str = "Net Profit"

    ProbabilisticSharpeRatio: str = "Probabilistic Sharpe Ratio"

    ProfitLossRatio: str = "Profit-Loss Ratio"

    SharpeRatio: str = "Sharpe Ratio"

    TotalFees: str = "Total Fees"

    TotalTrades: str = "Total Trades"

    TrackingError: str = "Tracking Error"

    TreynorRatio: str = "Treynor Ratio"

    WinRate: str = "Win Rate"

    LowestCapacityAsset: str = "Lowest Capacity Asset"


class PortfolioStatistics(System.Object):
    """The PortfolioStatistics class represents a set of statistics calculated from equity and benchmark samples"""

    @property
    def AverageWinRate(self) -> float:
        """The average rate of return for winning trades"""
        ...

    @AverageWinRate.setter
    def AverageWinRate(self, value: float):
        """The average rate of return for winning trades"""
        ...

    @property
    def AverageLossRate(self) -> float:
        """The average rate of return for losing trades"""
        ...

    @AverageLossRate.setter
    def AverageLossRate(self, value: float):
        """The average rate of return for losing trades"""
        ...

    @property
    def ProfitLossRatio(self) -> float:
        """The ratio of the average win rate to the average loss rate"""
        ...

    @ProfitLossRatio.setter
    def ProfitLossRatio(self, value: float):
        """The ratio of the average win rate to the average loss rate"""
        ...

    @property
    def WinRate(self) -> float:
        """The ratio of the number of winning trades to the total number of trades"""
        ...

    @WinRate.setter
    def WinRate(self, value: float):
        """The ratio of the number of winning trades to the total number of trades"""
        ...

    @property
    def LossRate(self) -> float:
        """The ratio of the number of losing trades to the total number of trades"""
        ...

    @LossRate.setter
    def LossRate(self, value: float):
        """The ratio of the number of losing trades to the total number of trades"""
        ...

    @property
    def Expectancy(self) -> float:
        """The expected value of the rate of return"""
        ...

    @Expectancy.setter
    def Expectancy(self, value: float):
        """The expected value of the rate of return"""
        ...

    @property
    def CompoundingAnnualReturn(self) -> float:
        """Annual compounded returns statistic based on the final-starting capital and years."""
        ...

    @CompoundingAnnualReturn.setter
    def CompoundingAnnualReturn(self, value: float):
        """Annual compounded returns statistic based on the final-starting capital and years."""
        ...

    @property
    def Drawdown(self) -> float:
        """Drawdown maximum percentage."""
        ...

    @Drawdown.setter
    def Drawdown(self, value: float):
        """Drawdown maximum percentage."""
        ...

    @property
    def TotalNetProfit(self) -> float:
        """The total net profit percentage."""
        ...

    @TotalNetProfit.setter
    def TotalNetProfit(self, value: float):
        """The total net profit percentage."""
        ...

    @property
    def SharpeRatio(self) -> float:
        """Sharpe ratio with respect to risk free rate: measures excess of return per unit of risk."""
        ...

    @SharpeRatio.setter
    def SharpeRatio(self, value: float):
        """Sharpe ratio with respect to risk free rate: measures excess of return per unit of risk."""
        ...

    @property
    def ProbabilisticSharpeRatio(self) -> float:
        """
        Probabilistic Sharpe Ratio is a probability measure associated with the Sharpe ratio.
        It informs us of the probability that the estimated Sharpe ratio is greater than a chosen benchmark
        """
        ...

    @ProbabilisticSharpeRatio.setter
    def ProbabilisticSharpeRatio(self, value: float):
        """
        Probabilistic Sharpe Ratio is a probability measure associated with the Sharpe ratio.
        It informs us of the probability that the estimated Sharpe ratio is greater than a chosen benchmark
        """
        ...

    @property
    def Alpha(self) -> float:
        """Algorithm "Alpha" statistic - abnormal returns over the risk free rate and the relationshio (beta) with the benchmark returns."""
        ...

    @Alpha.setter
    def Alpha(self, value: float):
        """Algorithm "Alpha" statistic - abnormal returns over the risk free rate and the relationshio (beta) with the benchmark returns."""
        ...

    @property
    def Beta(self) -> float:
        """Algorithm "beta" statistic - the covariance between the algorithm and benchmark performance, divided by benchmark's variance"""
        ...

    @Beta.setter
    def Beta(self, value: float):
        """Algorithm "beta" statistic - the covariance between the algorithm and benchmark performance, divided by benchmark's variance"""
        ...

    @property
    def AnnualStandardDeviation(self) -> float:
        """Annualized standard deviation"""
        ...

    @AnnualStandardDeviation.setter
    def AnnualStandardDeviation(self, value: float):
        """Annualized standard deviation"""
        ...

    @property
    def AnnualVariance(self) -> float:
        """Annualized variance statistic calculation using the daily performance variance and trading days per year."""
        ...

    @AnnualVariance.setter
    def AnnualVariance(self, value: float):
        """Annualized variance statistic calculation using the daily performance variance and trading days per year."""
        ...

    @property
    def InformationRatio(self) -> float:
        """Information ratio - risk adjusted return"""
        ...

    @InformationRatio.setter
    def InformationRatio(self, value: float):
        """Information ratio - risk adjusted return"""
        ...

    @property
    def TrackingError(self) -> float:
        """Tracking error volatility (TEV) statistic - a measure of how closely a portfolio follows the index to which it is benchmarked"""
        ...

    @TrackingError.setter
    def TrackingError(self, value: float):
        """Tracking error volatility (TEV) statistic - a measure of how closely a portfolio follows the index to which it is benchmarked"""
        ...

    @property
    def TreynorRatio(self) -> float:
        """Treynor ratio statistic is a measurement of the returns earned in excess of that which could have been earned on an investment that has no diversifiable risk"""
        ...

    @TreynorRatio.setter
    def TreynorRatio(self, value: float):
        """Treynor ratio statistic is a measurement of the returns earned in excess of that which could have been earned on an investment that has no diversifiable risk"""
        ...

    @overload
    def __init__(self, profitLoss: System.Collections.Generic.SortedDictionary[datetime.datetime, float], equity: System.Collections.Generic.SortedDictionary[datetime.datetime, float], listPerformance: System.Collections.Generic.List[float], listBenchmark: System.Collections.Generic.List[float], startingCapital: float, tradingDaysPerYear: int = 252) -> None:
        """
        Initializes a new instance of the PortfolioStatistics class
        
        :param profitLoss: Trade record of profits and losses
        :param equity: The list of daily equity values
        :param listPerformance: The list of algorithm performance values
        :param listBenchmark: The list of benchmark values
        :param startingCapital: The algorithm starting capital
        :param tradingDaysPerYear: The number of trading days per year
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the PortfolioStatistics class"""
        ...

    @staticmethod
    def GetRiskFreeRate() -> float:
        """Gets the current defined risk free annual return rate"""
        ...


class AlgorithmPerformance(System.Object):
    """The AlgorithmPerformance class is a wrapper for TradeStatistics and PortfolioStatistics"""

    @property
    def TradeStatistics(self) -> QuantConnect.Statistics.TradeStatistics:
        """The algorithm statistics on closed trades"""
        ...

    @TradeStatistics.setter
    def TradeStatistics(self, value: QuantConnect.Statistics.TradeStatistics):
        """The algorithm statistics on closed trades"""
        ...

    @property
    def PortfolioStatistics(self) -> QuantConnect.Statistics.PortfolioStatistics:
        """The algorithm statistics on portfolio"""
        ...

    @PortfolioStatistics.setter
    def PortfolioStatistics(self, value: QuantConnect.Statistics.PortfolioStatistics):
        """The algorithm statistics on portfolio"""
        ...

    @property
    def ClosedTrades(self) -> System.Collections.Generic.List[QuantConnect.Statistics.Trade]:
        """The list of closed trades"""
        ...

    @ClosedTrades.setter
    def ClosedTrades(self, value: System.Collections.Generic.List[QuantConnect.Statistics.Trade]):
        """The list of closed trades"""
        ...

    @overload
    def __init__(self, trades: System.Collections.Generic.List[QuantConnect.Statistics.Trade], profitLoss: System.Collections.Generic.SortedDictionary[datetime.datetime, float], equity: System.Collections.Generic.SortedDictionary[datetime.datetime, float], listPerformance: System.Collections.Generic.List[float], listBenchmark: System.Collections.Generic.List[float], startingCapital: float) -> None:
        """
        Initializes a new instance of the AlgorithmPerformance class
        
        :param trades: The list of closed trades
        :param profitLoss: Trade record of profits and losses
        :param equity: The list of daily equity values
        :param listPerformance: The list of algorithm performance values
        :param listBenchmark: The list of benchmark values
        :param startingCapital: The algorithm starting capital
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the AlgorithmPerformance class"""
        ...


class FitnessScoreManager(System.Object):
    """
    Implements a fitness score calculator needed to account for strategy volatility,
    returns, drawdown, and factor in the turnover to ensure the algorithm engagement
    is statistically significant
    """

    @property
    def FitnessScore(self) -> float:
        """Score of the strategy's performance, and suitability for the Alpha Stream Market"""
        ...

    @FitnessScore.setter
    def FitnessScore(self, value: float):
        """Score of the strategy's performance, and suitability for the Alpha Stream Market"""
        ...

    @property
    def PortfolioTurnover(self) -> float:
        """
        Measurement of the strategies trading activity with respect to the portfolio value.
        Calculated as the sales volume with respect to the average total portfolio value.
        """
        ...

    @PortfolioTurnover.setter
    def PortfolioTurnover(self, value: float):
        """
        Measurement of the strategies trading activity with respect to the portfolio value.
        Calculated as the sales volume with respect to the average total portfolio value.
        """
        ...

    @property
    def SortinoRatio(self) -> float:
        """
        Gives a relative picture of the strategy volatility.
        It is calculated by taking a portfolio's annualized rate of return and subtracting the risk free rate of return.
        """
        ...

    @SortinoRatio.setter
    def SortinoRatio(self, value: float):
        """
        Gives a relative picture of the strategy volatility.
        It is calculated by taking a portfolio's annualized rate of return and subtracting the risk free rate of return.
        """
        ...

    @property
    def ReturnOverMaxDrawdown(self) -> float:
        """
        Provides a risk adjusted way to factor in the returns and drawdown of the strategy.
        It is calculated by dividing the Portfolio Annualized Return by the Maximum Drawdown seen during the backtest.
        """
        ...

    @ReturnOverMaxDrawdown.setter
    def ReturnOverMaxDrawdown(self, value: float):
        """
        Provides a risk adjusted way to factor in the returns and drawdown of the strategy.
        It is calculated by dividing the Portfolio Annualized Return by the Maximum Drawdown seen during the backtest.
        """
        ...

    def Initialize(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """Initializes the fitness score instance and sets the initial portfolio value"""
        ...

    @staticmethod
    def SigmoidalScale(valueToScale: float) -> float:
        """Adjusts the input value to a range of 0 to 10 based on a sigmoidal scale"""
        ...

    def UpdateScores(self) -> None:
        """Gets the fitness score value for the algorithms current state"""
        ...


class StatisticsResults(System.Object):
    """The StatisticsResults class represents total and rolling statistics for an algorithm"""

    @property
    def TotalPerformance(self) -> QuantConnect.Statistics.AlgorithmPerformance:
        """The performance of the algorithm over the whole period"""
        ...

    @TotalPerformance.setter
    def TotalPerformance(self, value: QuantConnect.Statistics.AlgorithmPerformance):
        """The performance of the algorithm over the whole period"""
        ...

    @property
    def RollingPerformances(self) -> System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance]:
        """The rolling performance of the algorithm over 1, 3, 6, 12 month periods"""
        ...

    @RollingPerformances.setter
    def RollingPerformances(self, value: System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance]):
        """The rolling performance of the algorithm over 1, 3, 6, 12 month periods"""
        ...

    @property
    def Summary(self) -> System.Collections.Generic.Dictionary[str, str]:
        """Returns a summary of the algorithm performance as a dictionary"""
        ...

    @Summary.setter
    def Summary(self, value: System.Collections.Generic.Dictionary[str, str]):
        """Returns a summary of the algorithm performance as a dictionary"""
        ...

    @overload
    def __init__(self, totalPerformance: QuantConnect.Statistics.AlgorithmPerformance, rollingPerformances: System.Collections.Generic.Dictionary[str, QuantConnect.Statistics.AlgorithmPerformance], summary: System.Collections.Generic.Dictionary[str, str]) -> None:
        """
        Initializes a new instance of the StatisticsResults class
        
        :param totalPerformance: The algorithm total performance
        :param rollingPerformances: The algorithm rolling performances
        :param summary: The summary performance dictionary
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the StatisticsResults class"""
        ...


class StatisticsBuilder(System.Object):
    """The StatisticsBuilder class creates summary and rolling statistics from trades, equity and benchmark points"""

    @staticmethod
    def Generate(trades: System.Collections.Generic.List[QuantConnect.Statistics.Trade], profitLoss: System.Collections.Generic.SortedDictionary[datetime.datetime, float], pointsEquity: System.Collections.Generic.List[QuantConnect.ChartPoint], pointsPerformance: System.Collections.Generic.List[QuantConnect.ChartPoint], pointsBenchmark: System.Collections.Generic.List[QuantConnect.ChartPoint], startingCapital: float, totalFees: float, totalTransactions: int, estimatedStrategyCapacity: QuantConnect.CapacityEstimate, accountCurrencySymbol: str) -> QuantConnect.Statistics.StatisticsResults:
        """
        Generates the statistics and returns the results
        
        :param trades: The list of closed trades
        :param profitLoss: Trade record of profits and losses
        :param pointsEquity: The list of daily equity values
        :param pointsPerformance: The list of algorithm performance values
        :param pointsBenchmark: The list of benchmark values
        :param startingCapital: The algorithm starting capital
        :param totalFees: The total fees
        :param totalTransactions: The total number of transactions
        :param estimatedStrategyCapacity: The estimated capacity of this strategy
        :returns: Returns a StatisticsResults object.
        """
        ...


class Statistics(System.Object):
    """Calculate all the statistics required from the backtest, based on the equity curve and the profit loss statement."""

    YahooSPYBenchmark: System.Collections.Generic.SortedDictionary[datetime.datetime, float]
    """Retrieve a static S-P500 Benchmark for the statistics calculations. Update the benchmark once per day."""

    @staticmethod
    def Alpha(algoPerformance: System.Collections.Generic.List[float], benchmarkPerformance: System.Collections.Generic.List[float], riskFreeRate: float) -> float:
        """
        Algorithm "Alpha" statistic - abnormal returns over the risk free rate and the relationshio (beta) with the benchmark returns.
        
        :param algoPerformance: Collection of double algorithm daily performance values.
        :param benchmarkPerformance: Collection of double benchmark daily performance values.
        :param riskFreeRate: Risk free rate of return for the T-Bonds.
        :returns: Value for alpha.
        """
        ...

    @staticmethod
    def AnnualPerformance(performance: System.Collections.Generic.List[float], tradingDaysPerYear: float = 252) -> float:
        """
        Annualized return statistic calculated as an average of daily trading performance multiplied by the number of trading days per year.
        
        :param performance: Dictionary collection of double performance values
        :param tradingDaysPerYear: Trading days per year for the assets in portfolio
        :returns: Double annual performance percentage.
        """
        ...

    @staticmethod
    def AnnualStandardDeviation(performance: System.Collections.Generic.List[float], tradingDaysPerYear: float = 252) -> float:
        """
        Annualized standard deviation
        
        :param performance: Collection of double values for daily performance
        :param tradingDaysPerYear: Number of trading days for the assets in portfolio to get annualize standard deviation.
        :returns: Value for annual standard deviation.
        """
        ...

    @staticmethod
    def AnnualVariance(performance: System.Collections.Generic.List[float], tradingDaysPerYear: float = 252) -> float:
        """
        Annualized variance statistic calculation using the daily performance variance and trading days per year.
        
        :returns: Annual variance value.
        """
        ...

    @staticmethod
    def Beta(algoPerformance: System.Collections.Generic.List[float], benchmarkPerformance: System.Collections.Generic.List[float]) -> float:
        """
        Algorithm "beta" statistic - the covariance between the algorithm and benchmark performance, divided by benchmark's variance
        
        :param algoPerformance: Collection of double values for algorithm daily performance.
        :param benchmarkPerformance: Collection of double benchmark daily performance values.
        :returns: Value for beta.
        """
        ...

    @staticmethod
    def CompoundingAnnualPerformance(startingCapital: float, finalCapital: float, years: float) -> float:
        """
        Annual compounded returns statistic based on the final-starting capital and years.
        
        :param startingCapital: Algorithm starting capital
        :param finalCapital: Algorithm final capital
        :param years: Years trading
        :returns: Decimal fraction for annual compounding performance.
        """
        ...

    @staticmethod
    @overload
    def DrawdownPercent(equityOverTime: System.Collections.Generic.SortedDictionary[datetime.datetime, float], rounding: int = 2) -> float:
        """Drawdown maximum percentage."""
        ...

    @staticmethod
    @overload
    def DrawdownPercent(current: float, high: float, roundingDecimals: int = 2) -> float:
        """
        Calculate the drawdown between a high and current value
        
        :param current: Current value
        :param high: Latest maximum
        :param roundingDecimals: Digits to round the result too
        :returns: Drawdown percentage.
        """
        ...

    @staticmethod
    def DrawdownValue(equityOverTime: System.Collections.Generic.SortedDictionary[datetime.datetime, float], rounding: int = 2) -> float:
        """
        Drawdown maximum value
        
        :param equityOverTime: Array of portfolio value over time.
        :param rounding: Round the drawdown statistics.
        :returns: Draw down percentage over period.
        """
        ...

    @staticmethod
    def Generate(pointsEquity: System.Collections.Generic.IEnumerable[QuantConnect.ChartPoint], profitLoss: System.Collections.Generic.SortedDictionary[datetime.datetime, float], pointsPerformance: System.Collections.Generic.IEnumerable[QuantConnect.ChartPoint], unsortedBenchmark: System.Collections.Generic.Dictionary[datetime.datetime, float], startingCash: float, totalFees: float, totalTrades: float, tradingDaysPerYear: float = 252) -> System.Collections.Generic.Dictionary[str, str]:
        """
        Run a full set of orders and return a Dictionary of statistics.
        
        :param pointsEquity: Equity value over time.
        :param profitLoss: profit loss from trades
        :param pointsPerformance: Daily performance
        :param unsortedBenchmark: Benchmark data as dictionary. Data does not need to be ordered
        :param startingCash: Amount of starting cash in USD
        :param totalFees: The total fees incurred over the life time of the algorithm
        :param totalTrades: Total number of orders executed.
        :param tradingDaysPerYear: Number of trading days per year
        :returns: Statistics Array, Broken into Annual Periods.
        """
        ...

    @staticmethod
    def InformationRatio(algoPerformance: System.Collections.Generic.List[float], benchmarkPerformance: System.Collections.Generic.List[float]) -> float:
        """
        Information ratio - risk adjusted return
        
        :param algoPerformance: Collection of doubles for the daily algorithm daily performance
        :param benchmarkPerformance: Collection of doubles for the benchmark daily performance
        :returns: Value for information ratio.
        """
        ...

    @staticmethod
    def ObservedSharpeRatio(listPerformance: System.Collections.Generic.List[float]) -> float:
        """
        Calculates the observed sharpe ratio
        
        :param listPerformance: The performance samples to use
        :returns: The observed sharpe ratio.
        """
        ...

    @staticmethod
    def ProbabilisticSharpeRatio(listPerformance: System.Collections.Generic.List[float], benchmarkSharpeRatio: float) -> float:
        """
        Helper method to calculate the probabilistic sharpe ratio
        
        :param listPerformance: The list of algorithm performance values
        :param benchmarkSharpeRatio: The benchmark sharpe ratio to use
        :returns: Probabilistic Sharpe Ratio.
        """
        ...

    @staticmethod
    def ProfitLossRatio(averageWin: float, averageLoss: float) -> float:
        """Return profit loss ratio safely avoiding divide by zero errors."""
        ...

    @staticmethod
    def SharpeRatio(algoPerformance: System.Collections.Generic.List[float], riskFreeRate: float) -> float:
        """
        Sharpe ratio with respect to risk free rate: measures excess of return per unit of risk.
        
        :param algoPerformance: Collection of double values for the algorithm daily performance
        :returns: Value for sharpe ratio.
        """
        ...

    @staticmethod
    def TrackingError(algoPerformance: System.Collections.Generic.List[float], benchmarkPerformance: System.Collections.Generic.List[float], tradingDaysPerYear: float = 252) -> float:
        """
        Tracking error volatility (TEV) statistic - a measure of how closely a portfolio follows the index to which it is benchmarked
        
        :param algoPerformance: Double collection of algorithm daily performance values
        :param benchmarkPerformance: Double collection of benchmark daily performance values
        :param tradingDaysPerYear: Number of trading days per year
        :returns: Value for tracking error.
        """
        ...

    @staticmethod
    def TreynorRatio(algoPerformance: System.Collections.Generic.List[float], benchmarkPerformance: System.Collections.Generic.List[float], riskFreeRate: float) -> float:
        """
        Treynor ratio statistic is a measurement of the returns earned in excess of that which could have been earned on an investment that has no diversifiable risk
        
        :param algoPerformance: Collection of double algorithm daily performance values
        :param benchmarkPerformance: Collection of double benchmark daily performance values
        :param riskFreeRate: Risk free rate of return
        :returns: double Treynor ratio.
        """
        ...


class TradeDirection(System.Enum):
    """Direction of a trade"""

    Long = 0
    """Long direction (0)"""

    Short = 1
    """Short direction (1)"""


class KellyCriterionManager(System.Object):
    """
    Class in charge of calculating the Kelly Criterion values.
    Will use the sample values of the last year.
    """

    @property
    def KellyCriterionEstimate(self) -> float:
        """Score of the strategy's insights predictive power"""
        ...

    @KellyCriterionEstimate.setter
    def KellyCriterionEstimate(self, value: float):
        """Score of the strategy's insights predictive power"""
        ...

    @property
    def KellyCriterionProbabilityValue(self) -> float:
        """The p-value or probability value of the KellyCriterionEstimate"""
        ...

    @KellyCriterionProbabilityValue.setter
    def KellyCriterionProbabilityValue(self, value: float):
        """The p-value or probability value of the KellyCriterionEstimate"""
        ...

    def AddNewValue(self, newValue: float, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Adds a new value to the population.
        Will remove values older than an year compared with the provided time.
        For performance, will update the continuous average calculation
        
        :param newValue: The new value to add
        :param time: The new values time
        """
        ...

    def UpdateScores(self) -> None:
        """Updates the Kelly Criterion values"""
        ...


