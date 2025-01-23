from typing import overload
import QuantConnect.Algorithm.Framework.Alphas
import QuantConnect.Algorithm.Framework.Alphas.Analysis
import QuantConnect.Algorithm.Framework.Alphas.Analysis.Functions
import System


class BinaryInsightScoreFunction(System.Object, QuantConnect.Algorithm.Framework.Alphas.Analysis.IInsightScoreFunction):
    """
    Defines a scoring function that always returns 1 or 0.
    You're either right or you're wrong with this one :)
    """

    def Evaluate(self, context: QuantConnect.Algorithm.Framework.Alphas.Analysis.InsightAnalysisContext, scoreType: QuantConnect.Algorithm.Framework.Alphas.InsightScoreType) -> float:
        ...


