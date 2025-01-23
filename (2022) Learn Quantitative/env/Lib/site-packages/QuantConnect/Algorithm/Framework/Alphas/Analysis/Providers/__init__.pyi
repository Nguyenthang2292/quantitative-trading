from typing import overload
import typing

import QuantConnect
import QuantConnect.Algorithm.Framework.Alphas
import QuantConnect.Algorithm.Framework.Alphas.Analysis
import QuantConnect.Algorithm.Framework.Alphas.Analysis.Providers
import QuantConnect.Interfaces
import System


class DefaultInsightScoreFunctionProvider(System.Object, QuantConnect.Algorithm.Framework.Alphas.Analysis.IInsightScoreFunctionProvider):
    """Default implementation of IInsightScoreFunctionProvider always returns the BinaryInsightScoreFunction"""

    def GetScoreFunction(self, insightType: QuantConnect.Algorithm.Framework.Alphas.InsightType, scoreType: QuantConnect.Algorithm.Framework.Alphas.InsightScoreType) -> QuantConnect.Algorithm.Framework.Alphas.Analysis.IInsightScoreFunction:
        ...


class AlgorithmSecurityValuesProvider(System.Object, QuantConnect.Algorithm.Framework.Alphas.Analysis.ISecurityValuesProvider):
    """
    Provides an implementation of ISecurityProvider that uses the SecurityManager
    to get the price for the specified symbols
    """

    def __init__(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """
        Initializes a new instance of the AlgorithmSecurityValuesProvider class
        
        :param algorithm: The wrapped algorithm instance
        """
        ...

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


