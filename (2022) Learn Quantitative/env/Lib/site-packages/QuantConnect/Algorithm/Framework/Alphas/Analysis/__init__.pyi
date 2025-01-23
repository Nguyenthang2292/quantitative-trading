from typing import overload
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Algorithm.Framework.Alphas
import QuantConnect.Algorithm.Framework.Alphas.Analysis
import QuantConnect.Securities
import System
import System.Collections.Generic

QuantConnect_Algorithm_Framework_Alphas_Analysis_InsightAnalysisContext_Get_T = typing.TypeVar("QuantConnect_Algorithm_Framework_Alphas_Analysis_InsightAnalysisContext_Get_T")


class SecurityValues(System.Object):
    """Contains security values required by insight analysis components"""

    @property
    def Symbol(self) -> QuantConnect.Symbol:
        """Gets the symbol these values are for"""
        ...

    @property
    def TimeUtc(self) -> datetime.datetime:
        """Gets the utc time these values were sampled"""
        ...

    @property
    def Price(self) -> float:
        """Gets the security price as of TimeUtc"""
        ...

    @property
    def Volatility(self) -> float:
        """Gets the security's volatility as of TimeUtc"""
        ...

    @property
    def Volume(self) -> float:
        """Gets the volume traded in the security during this time step"""
        ...

    @property
    def QuoteCurrencyConversionRate(self) -> float:
        """Gets the conversion rate for the quote currency of the security"""
        ...

    @property
    def ExchangeHours(self) -> QuantConnect.Securities.SecurityExchangeHours:
        """Gets the exchange hours for the security"""
        ...

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], timeUtc: typing.Union[datetime.datetime, datetime.date], exchangeHours: QuantConnect.Securities.SecurityExchangeHours, price: float, volatility: float, volume: float, quoteCurrencyConversionRate: float) -> None:
        """
        Initializes a new instance of the SecurityValues class
        
        :param symbol: The symbol of the security
        :param timeUtc: The time these values were sampled
        :param exchangeHours: The security's exchange hours
        :param price: The security price
        :param volatility: The security's volatility
        :param volume: The volume traded at this time step
        :param quoteCurrencyConversionRate: The conversion rate for the quote currency of the security
        """
        ...

    def Get(self, type: QuantConnect.Algorithm.Framework.Alphas.InsightType) -> float:
        """
        Gets the security value corresponding to the specified insight type
        
        :param type: The insight type
        :returns: The security value for the specified insight type.
        """
        ...


class ReadOnlySecurityValuesCollection(System.Object):
    """
    Defines the security values at a given instant. This is analagous
    to TimeSlice/Slice, but decoupled from the algorithm thread and is
    intended to contain all of the information necessary to score all
    insight at this particular time step
    """

    def __getitem__(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Algorithm.Framework.Alphas.Analysis.SecurityValues:
        """
        Symbol indexer into security values collection.
        
        :param symbol: The symbol
        :returns: The security values for the specified symbol.
        """
        ...

    @overload
    def __init__(self, securityValuesBySymbol: System.Collections.Generic.Dictionary[QuantConnect.Symbol, QuantConnect.Algorithm.Framework.Alphas.Analysis.SecurityValues]) -> None:
        """Initializes a new instance of the ReadOnlySecurityValuesCollection class"""
        ...

    @overload
    def __init__(self, securityValuesBySymbolFunc: typing.Callable[[QuantConnect.Symbol], QuantConnect.Algorithm.Framework.Alphas.Analysis.SecurityValues]) -> None:
        """
        Initializes a new instance of the ReadOnlySecurityValuesCollection class
        
        :param securityValuesBySymbolFunc: Function used to get the SecurityValues for a specified Symbol
        """
        ...


class ISecurityValuesProvider(metaclass=abc.ABCMeta):
    """
    Provides a simple abstraction that returns a security's current price and volatility.
    This facilitates testing by removing the dependency of IAlgorithm on the analysis components
    """

    def GetAllValues(self) -> QuantConnect.Algorithm.Framework.Alphas.Analysis.ReadOnlySecurityValuesCollection:
        """
        Gets the current values for all the algorithm securities (price/volatility)
        
        :returns: The insight target values for all the algorithm securities.
        """
        ...

    def GetValues(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Algorithm.Framework.Alphas.Analysis.SecurityValues:
        """
        Gets the current values for the specified symbol (price/volatility)
        
        :param symbol: The symbol to get price/volatility for
        :returns: The insight target values for the specified symbol.
        """
        ...


class SecurityValuesProviderExtensions(System.Object):
    """Provides extension methods for ISecurityValuesProvider"""

    @staticmethod
    def GetValues(securityValuesProvider: QuantConnect.Algorithm.Framework.Alphas.Analysis.ISecurityValuesProvider, symbols: System.Collections.Generic.ICollection[QuantConnect.Symbol]) -> QuantConnect.Algorithm.Framework.Alphas.Analysis.ReadOnlySecurityValuesCollection:
        """
        Creates a new instance of ReadOnlySecurityValuesCollection to hold all SecurityValues for
        the specified symbol at the current instant in time
        
        :param securityValuesProvider: Security values provider fetches security values for each symbol
        :param symbols: The symbols to get values for
        :returns: A collection of.
        """
        ...


class InsightAnalysisContext(System.Object):
    """Defines a context for performing analysis on a single insight"""

    @property
    def Id(self) -> System.Guid:
        """Gets the id of this context which is the same as the insight's id"""
        ...

    @property
    def Symbol(self) -> QuantConnect.Symbol:
        """Gets the symbol the insight is for"""
        ...

    @property
    def Insight(self) -> QuantConnect.Algorithm.Framework.Alphas.Insight:
        """Gets the insight being analyzed"""
        ...

    @property
    def Score(self) -> QuantConnect.Algorithm.Framework.Alphas.InsightScore:
        """Gets the insight's current score"""
        ...

    @property
    def AnalysisEndTimeUtc(self) -> datetime.datetime:
        """Gets ending time of the analysis period"""
        ...

    @AnalysisEndTimeUtc.setter
    def AnalysisEndTimeUtc(self, value: datetime.datetime):
        """Gets ending time of the analysis period"""
        ...

    @property
    def InitialValues(self) -> QuantConnect.Algorithm.Framework.Alphas.Analysis.SecurityValues:
        """Gets the initial values. These are values of price/volatility at the time the insight was generated"""
        ...

    @property
    def InsightPeriodClosed(self) -> bool:
        """Gets whether or not this insight's period has closed"""
        ...

    @InsightPeriodClosed.setter
    def InsightPeriodClosed(self, value: bool):
        """Gets whether or not this insight's period has closed"""
        ...

    @property
    def CurrentValues(self) -> QuantConnect.Algorithm.Framework.Alphas.Analysis.SecurityValues:
        """
        Gets the current values. These are values of price/volatility as of the current algorithm time.
        NOTE: Once the scoring has been finalized these values will no longer be updated and will be the
        values as of the last scoring which may not be the same as the prediction end time
        """
        ...

    @CurrentValues.setter
    def CurrentValues(self, value: QuantConnect.Algorithm.Framework.Alphas.Analysis.SecurityValues):
        """
        Gets the current values. These are values of price/volatility as of the current algorithm time.
        NOTE: Once the scoring has been finalized these values will no longer be updated and will be the
        values as of the last scoring which may not be the same as the prediction end time
        """
        ...

    @property
    def NormalizedTime(self) -> float:
        """Percentage through the analysis period"""
        ...

    @property
    def NormalizedTimeStep(self) -> float:
        """Percentage of the current time step w.r.t analysis period"""
        ...

    def __init__(self, insight: QuantConnect.Algorithm.Framework.Alphas.Insight, initialValues: QuantConnect.Algorithm.Framework.Alphas.Analysis.SecurityValues, analysisPeriod: datetime.timedelta) -> None:
        """
        Initializes a new instance of the InsightAnalysisContext class
        
        :param insight: The insight to be analyzed
        :param initialValues: The initial security values from when the insight was generated
        :param analysisPeriod: The period over which to perform analysis of the insight. This should be greater than or equal to Alphas.Insight.Period. Specify null for default, insight.Period
        """
        ...

    def Equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified object is equal to the current object.
        
        :param obj: The object to compare with the current object.
        :returns: true if the specified object  is equal to the current object; otherwise, false.
        """
        ...

    def Get(self, key: str) -> QuantConnect_Algorithm_Framework_Alphas_Analysis_InsightAnalysisContext_Get_T:
        """
        Gets a value from the context's generic storage.
        This is here to allow function to access contextual state without needing to track it themselves
        
        :param key: The key
        :returns: The value if in storage, otherwise default(T).
        """
        ...

    def GetHashCode(self) -> int:
        """
        Serves as the default hash function.
        
        :returns: A hash code for the current object.
        """
        ...

    def Set(self, key: str, value: typing.Any) -> None:
        """
        Sets the key/value in the context's generic storage
        
        :param key: The value's key
        :param value: The value to be stored
        """
        ...

    def ShouldAnalyze(self, scoreType: QuantConnect.Algorithm.Framework.Alphas.InsightScoreType) -> bool:
        """
        Determines whether or not this context/insight can be analyzed for the specified score type
        
        :param scoreType: The type of insight score
        :returns: True to proceed with analyzing this insight for the specified score type, false to skip analysis of the score type.
        """
        ...

    def ToString(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class IInsightScoreFunction(metaclass=abc.ABCMeta):
    """
    Defines a function used to determine how correct a particular insight is.
    The result of calling Evaluate is expected to be within the range [0, 1]
    where 0 is completely wrong and 1 is completely right
    """

    def Evaluate(self, context: QuantConnect.Algorithm.Framework.Alphas.Analysis.InsightAnalysisContext, scoreType: QuantConnect.Algorithm.Framework.Alphas.InsightScoreType) -> float:
        """
        Evaluates the score of the insight within the context
        
        :param context: The insight's analysis context
        :param scoreType: The score type to be evaluated
        :returns: The insight's current score.
        """
        ...


class IInsightManager(System.IDisposable, metaclass=abc.ABCMeta):
    """Encapsulates the storage and on-line scoring of insights."""

    @property
    @abc.abstractmethod
    def OpenInsights(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Algorithm.Framework.Alphas.Insight]:
        """Enumerable of insights still under analysis"""
        ...

    @property
    @abc.abstractmethod
    def ClosedInsights(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Algorithm.Framework.Alphas.Insight]:
        """Enumerable of insights who's analysis has been completed"""
        ...

    @property
    @abc.abstractmethod
    def AllInsights(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Algorithm.Framework.Alphas.Insight]:
        """Enumerable of all internally maintained insights"""
        ...

    def AddExtension(self, extension: QuantConnect.Algorithm.Framework.Alphas.IInsightManagerExtension) -> None:
        """
        Add an extension to this manager
        
        :param extension: The extension to be added
        """
        ...

    def InitializeExtensionsForRange(self, start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date], current: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes any extensions for the specified backtesting range
        
        :param start: The start date of the backtest (current time in live mode)
        :param end: The end date of the backtest (Time.EndOfTime in live mode)
        :param current: The algorithm's current utc time
        """
        ...

    def RemoveInsights(self, insightIds: System.Collections.Generic.IEnumerable[System.Guid]) -> None:
        """
        Removes insights from the manager with the specified ids
        
        :param insightIds: The insights ids to be removed
        """
        ...

    def Step(self, frontierTimeUtc: typing.Union[datetime.datetime, datetime.date], securityValuesCollection: QuantConnect.Algorithm.Framework.Alphas.Analysis.ReadOnlySecurityValuesCollection, generatedInsights: QuantConnect.Algorithm.Framework.Alphas.GeneratedInsightsCollection) -> None:
        """
        Steps the manager forward in time, accepting new state information and potentialy newly generated insights
        
        :param frontierTimeUtc: The frontier time of the insight analysis
        :param securityValuesCollection: Snap shot of the securities at the frontier time
        :param generatedInsights: Any insight generated by the algorithm at the frontier time
        """
        ...


class IInsightScoreFunctionProvider(metaclass=abc.ABCMeta):
    """Retrieves the registered scoring function for the specified insight/score type"""

    def GetScoreFunction(self, insightType: QuantConnect.Algorithm.Framework.Alphas.InsightType, scoreType: QuantConnect.Algorithm.Framework.Alphas.InsightScoreType) -> QuantConnect.Algorithm.Framework.Alphas.Analysis.IInsightScoreFunction:
        """
        Gets the insight scoring function for the specified insight type and score type
        
        :param insightType: The insight's type
        :param scoreType: The scoring type
        :returns: A function to be used to compute insight scores.
        """
        ...


class InsightManager(System.Object, QuantConnect.Algorithm.Framework.Alphas.Analysis.IInsightManager):
    """Encapsulates the storage and on-line scoring of insights."""

    ScoreTypes: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Algorithm.Framework.Alphas.InsightScoreType] = ...
    """Gets all insight score types"""

    @property
    def OpenInsights(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Algorithm.Framework.Alphas.Insight]:
        """Enumerable of insights still under analysis"""
        ...

    @property
    def ClosedInsights(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Algorithm.Framework.Alphas.Insight]:
        """Enumerable of insights who's analysis has been completed"""
        ...

    @property
    def AllInsights(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Algorithm.Framework.Alphas.Insight]:
        """Enumerable of all internally maintained insights"""
        ...

    def __init__(self, scoreFunctionProvider: QuantConnect.Algorithm.Framework.Alphas.Analysis.IInsightScoreFunctionProvider, extraAnalysisPeriodRatio: float, *extensions: QuantConnect.Algorithm.Framework.Alphas.IInsightManagerExtension) -> None:
        """
        Initializes a new instance of the InsightManager class
        
        :param scoreFunctionProvider: Provides scoring functions by insight type/score type
        :param extraAnalysisPeriodRatio: Ratio of the insight period to keep the analysis open
        :param extensions: Extensions used to perform tasks at certain events
        """
        ...

    def AddExtension(self, extension: QuantConnect.Algorithm.Framework.Alphas.IInsightManagerExtension) -> None:
        """
        Add an extension to this manager
        
        :param extension: The extension to be added
        """
        ...

    def ContextsOpenAt(self, frontierTimeUtc: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[QuantConnect.Algorithm.Framework.Alphas.Analysis.InsightAnalysisContext]:
        """Gets the unique set of symbols from analysis contexts that will"""
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def GetUpdatedContexts(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Algorithm.Framework.Alphas.Analysis.InsightAnalysisContext]:
        """
        Gets all insight analysis contexts that have been updated since this method's last invocation.
        Contexts are marked as not updated during the enumeration, so in order to remove a context from
        the updated set, the enumerable must be enumerated.
        """
        ...

    def InitializeExtensionsForRange(self, start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date], current: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes any extensions for the specified backtesting range
        
        :param start: The start date of the backtest (current time in live mode)
        :param end: The end date of the backtest (Time.EndOfTime in live mode)
        :param current: The algorithm's current utc time
        """
        ...

    def RemoveInsights(self, insightIds: System.Collections.Generic.IEnumerable[System.Guid]) -> None:
        """
        Removes insights from the manager with the specified ids
        
        :param insightIds: The insights ids to be removed
        """
        ...

    def Step(self, frontierTimeUtc: typing.Union[datetime.datetime, datetime.date], securityValuesCollection: QuantConnect.Algorithm.Framework.Alphas.Analysis.ReadOnlySecurityValuesCollection, generatedInsights: QuantConnect.Algorithm.Framework.Alphas.GeneratedInsightsCollection) -> None:
        """
        Steps the manager forward in time, accepting new state information and potentialy newly generated insights
        
        :param frontierTimeUtc: The frontier time of the insight analysis
        :param securityValuesCollection: Snap shot of the securities at the frontier time
        :param generatedInsights: Any insight generated by the algorithm at the frontier time
        """
        ...


