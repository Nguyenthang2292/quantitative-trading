from typing import overload
import datetime
import typing

import QuantConnect
import QuantConnect.Algorithm.Framework.Alphas
import QuantConnect.Algorithm.Framework.Alphas.Analysis
import QuantConnect.Interfaces
import QuantConnect.Lean.Engine.Alpha
import QuantConnect.Lean.Engine.Alphas
import QuantConnect.Lean.Engine.TransactionHandlers
import QuantConnect.Packets
import System


class StatisticsInsightManagerExtension(System.Object, QuantConnect.Algorithm.Framework.Alphas.IInsightManagerExtension):
    """Manages alpha statistics responsbilities"""

    @property
    def Statistics(self) -> QuantConnect.AlphaRuntimeStatistics:
        """
        Gets the current statistics. The values are current as of the time specified
        in AlphaRuntimeStatistics.MeanPopulationScore and AlphaRuntimeStatistics.RollingAveragedPopulationScore
        """
        ...

    @property
    def RollingAverageIsReady(self) -> bool:
        """Gets whether or not the rolling average statistics is ready"""
        ...

    def __init__(self, accountCurrencyProvider: QuantConnect.Interfaces.IAccountCurrencyProvider, tradablePercentOfVolume: float = 0.01, period: int = 100, requireRollingAverageWarmup: bool = False) -> None:
        """
        Initializes a new instance of the StatisticsInsightManagerExtension class
        
        :param accountCurrencyProvider: The account currency provider
        :param tradablePercentOfVolume: Percent of volume of first bar used to estimate the maximum number of tradable shares. Defaults to 1%
        :param period: The period used for exponential smoothing of scores - this is a number of insights. Defaults to 100 insight predictions.
        :param requireRollingAverageWarmup: Specify true to force the population average scoring to warmup before plotting.
        """
        ...

    def InitializeForRange(self, algorithmStartDate: typing.Union[datetime.datetime, datetime.date], algorithmEndDate: typing.Union[datetime.datetime, datetime.date], algorithmUtcTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Allows the extension to initialize itself over the expected range
        
        :param algorithmStartDate: The start date of the algorithm
        :param algorithmEndDate: The end date of the algorithm
        :param algorithmUtcTime: The algorithm's current utc time
        """
        ...

    def OnInsightAnalysisCompleted(self, context: QuantConnect.Algorithm.Framework.Alphas.Analysis.InsightAnalysisContext) -> None:
        """
        Updates the specified statistics with the new scores
        
        :param context: Context whose insight has just completed analysis
        """
        ...

    def OnInsightClosed(self, context: QuantConnect.Algorithm.Framework.Alphas.Analysis.InsightAnalysisContext) -> None:
        """
        Computes an estimated value for the insight. This is intended to be invoked at the end of the
        insight period, i.e, when now == insight.GeneratedTimeUtc + insight.Period;
        
        :param context: Context whose insight has just closed
        """
        ...

    def OnInsightGenerated(self, context: QuantConnect.Algorithm.Framework.Alphas.Analysis.InsightAnalysisContext) -> None:
        """
        Handles the IAlgorithm.InsightsGenerated event
        Increments total, long and short counters. Updates long/short ratio
        
        :param context: The newly generated insight context
        """
        ...

    def Step(self, frontierTimeUtc: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Invokes the manager at the end of the time step.
        
        :param frontierTimeUtc: The current frontier time utc
        """
        ...


class DefaultAlphaHandler(System.Object, QuantConnect.Lean.Engine.Alpha.IAlphaHandler):
    """Default alpha handler that supports sending insights to the messaging handler, analyzing insights online"""

    class AlphaResultPacketSender(System.Object, QuantConnect.Algorithm.Framework.Alphas.IInsightManagerExtension, System.IDisposable):
        """
        Encapsulates routing finalized insights to the messaging handler
        
        This class is protected.
        """

        def __init__(self, job: QuantConnect.Packets.AlgorithmNodePacket, messagingHandler: QuantConnect.Interfaces.IMessagingHandler, interval: datetime.timedelta, maximumNumberOfInsightsPerPacket: int) -> None:
            """
            Initialize a new instance of AlphaResultPacketSender
            
            :param job: Algorithm job
            :param messagingHandler: Message handler to use
            :param interval: Timespan interval
            :param maximumNumberOfInsightsPerPacket: Limit on insights per packet
            """
            ...

        def Dispose(self) -> None:
            """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
            ...

        def InitializeForRange(self, algorithmStartDate: typing.Union[datetime.datetime, datetime.date], algorithmEndDate: typing.Union[datetime.datetime, datetime.date], algorithmUtcTime: typing.Union[datetime.datetime, datetime.date]) -> None:
            """No operation"""
            ...

        def OnInsightAnalysisCompleted(self, context: QuantConnect.Algorithm.Framework.Alphas.Analysis.InsightAnalysisContext) -> None:
            """Enqueue finalized insights to be sent via the messaging handler"""
            ...

        def OnInsightClosed(self, context: QuantConnect.Algorithm.Framework.Alphas.Analysis.InsightAnalysisContext) -> None:
            """No operation"""
            ...

        def OnInsightGenerated(self, context: QuantConnect.Algorithm.Framework.Alphas.Analysis.InsightAnalysisContext) -> None:
            """No operation"""
            ...

        def Step(self, frontierTimeUtc: typing.Union[datetime.datetime, datetime.date]) -> None:
            """No operation"""
            ...

    @property
    def IsActive(self) -> bool:
        """Gets a flag indicating if this handler's thread is still running and processing messages"""
        ...

    @IsActive.setter
    def IsActive(self, value: bool):
        """Gets a flag indicating if this handler's thread is still running and processing messages"""
        ...

    @property
    def RuntimeStatistics(self) -> QuantConnect.AlphaRuntimeStatistics:
        """Gets the current alpha runtime statistics"""
        ...

    @RuntimeStatistics.setter
    def RuntimeStatistics(self, value: QuantConnect.AlphaRuntimeStatistics):
        """Gets the current alpha runtime statistics"""
        ...

    @property
    def AlgorithmId(self) -> str:
        """
        Gets the algorithm's unique identifier
        
        This property is protected.
        """
        ...

    @property
    def LiveMode(self) -> bool:
        """
        Gets whether or not the job is a live job
        
        This property is protected.
        """
        ...

    @property
    def Job(self) -> QuantConnect.Packets.AlgorithmNodePacket:
        """
        Gets the algorithm job packet
        
        This property is protected.
        """
        ...

    @Job.setter
    def Job(self, value: QuantConnect.Packets.AlgorithmNodePacket):
        """
        Gets the algorithm job packet
        
        This property is protected.
        """
        ...

    @property
    def Algorithm(self) -> QuantConnect.Interfaces.IAlgorithm:
        """
        Gets the algorithm instance
        
        This property is protected.
        """
        ...

    @Algorithm.setter
    def Algorithm(self, value: QuantConnect.Interfaces.IAlgorithm):
        """
        Gets the algorithm instance
        
        This property is protected.
        """
        ...

    @property
    def MessagingHandler(self) -> QuantConnect.Interfaces.IMessagingHandler:
        """
        Gets the confgured messaging handler for sending packets
        
        This property is protected.
        """
        ...

    @MessagingHandler.setter
    def MessagingHandler(self, value: QuantConnect.Interfaces.IMessagingHandler):
        """
        Gets the confgured messaging handler for sending packets
        
        This property is protected.
        """
        ...

    @property
    def InsightManager(self) -> QuantConnect.Algorithm.Framework.Alphas.Analysis.IInsightManager:
        """
        Gets the insight manager instance used to manage the analysis of algorithm insights
        
        This property is protected.
        """
        ...

    @InsightManager.setter
    def InsightManager(self, value: QuantConnect.Algorithm.Framework.Alphas.Analysis.IInsightManager):
        """
        Gets the insight manager instance used to manage the analysis of algorithm insights
        
        This property is protected.
        """
        ...

    def AddInsightManagerCustomExtensions(self, statistics: QuantConnect.Lean.Engine.Alphas.StatisticsInsightManagerExtension) -> None:
        """
        Allows each alpha handler implementation to add there own optional extensions
        
        This method is protected.
        """
        ...

    def CreateInsightManager(self) -> QuantConnect.Algorithm.Framework.Alphas.Analysis.IInsightManager:
        """
        Creates the InsightManager to manage the analysis of generated insights
        
        This method is protected.
        
        :returns: A new insight manager instance.
        """
        ...

    def Exit(self) -> None:
        """Stops processing and stores insights"""
        ...

    def Initialize(self, job: QuantConnect.Packets.AlgorithmNodePacket, algorithm: QuantConnect.Interfaces.IAlgorithm, messagingHandler: QuantConnect.Interfaces.IMessagingHandler, api: QuantConnect.Interfaces.IApi, transactionHandler: QuantConnect.Lean.Engine.TransactionHandlers.ITransactionHandler) -> None:
        """
        Initializes this alpha handler to accept insights from the specified algorithm
        
        :param job: The algorithm job
        :param algorithm: The algorithm instance
        :param messagingHandler: Handler used for sending insights
        :param api: Api instance
        :param transactionHandler: Algorithms transaction handler
        """
        ...

    def OnAfterAlgorithmInitialized(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """
        Invoked after the algorithm's Initialize method was called allowing the alpha handler to check
        other things, such as sampling period for backtests
        
        :param algorithm: The algorithm instance
        """
        ...

    def ProcessSynchronousEvents(self) -> None:
        """Performs processing in sync with the algorithm's time loop to provide consisten reading of data"""
        ...

    def StoreInsights(self) -> None:
        """
        Save insight results to persistent storage
        
        This method is protected.
        """
        ...


class ChartingInsightManagerExtension(System.Object, QuantConnect.Algorithm.Framework.Alphas.IInsightManagerExtension):
    """Manages alpha charting responsibilities."""

    AlphaAssets: str = "Alpha Assets"
    """The string name used for the Alpha Assets chart"""

    @property
    def SampleInterval(self) -> datetime.timedelta:
        """
        Gets or sets the interval at which alpha charts are updated. This is in realtion to algorithm time.
        
        This property is protected.
        """
        ...

    @SampleInterval.setter
    def SampleInterval(self, value: datetime.timedelta):
        """
        Gets or sets the interval at which alpha charts are updated. This is in realtion to algorithm time.
        
        This property is protected.
        """
        ...

    def __init__(self, algorithm: QuantConnect.Interfaces.IAlgorithm, statisticsManager: QuantConnect.Lean.Engine.Alphas.StatisticsInsightManagerExtension) -> None:
        """
        Initializes a new instance of the ChartingInsightManagerExtension class
        
        :param algorithm: The algorithm instance. This is only used for adding the charts to the algorithm. We purposefully do not save a reference to avoid potentially inconsistent reads
        :param statisticsManager: Statistics manager used to access mean population scores for charting
        """
        ...

    def InitializeForRange(self, algorithmStartDate: typing.Union[datetime.datetime, datetime.date], algorithmEndDate: typing.Union[datetime.datetime, datetime.date], algorithmUtcTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Invoked after IAlgorithm.Initialize has been called.
        Determines chart sample interval and initial sample times
        
        :param algorithmStartDate: The start date of the algorithm
        :param algorithmEndDate: The end date of the algorithm
        :param algorithmUtcTime: The algorithm's current utc time
        """
        ...

    def OnInsightAnalysisCompleted(self, context: QuantConnect.Algorithm.Framework.Alphas.Analysis.InsightAnalysisContext) -> None:
        """
        NOP - Charting is more concerned with population vs individual insights
        
        :param context: Context whose insight has just completed analysis
        """
        ...

    def OnInsightClosed(self, context: QuantConnect.Algorithm.Framework.Alphas.Analysis.InsightAnalysisContext) -> None:
        """
        NOP - Charting is more concerned with population vs individual insights
        
        :param context: Context whose insight has just completed analysis
        """
        ...

    def OnInsightGenerated(self, context: QuantConnect.Algorithm.Framework.Alphas.Analysis.InsightAnalysisContext) -> None:
        """
        Handles the IAlgorithm.InsightsGenerated event.
        Keep daily and total count of insights by symbol
        
        :param context: The newly generated insight analysis context
        """
        ...

    def Step(self, frontierTimeUtc: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Invokes the manager at the end of the time step.
        Samples and plots insight counts and population score.
        
        :param frontierTimeUtc: The current frontier time utc
        """
        ...


