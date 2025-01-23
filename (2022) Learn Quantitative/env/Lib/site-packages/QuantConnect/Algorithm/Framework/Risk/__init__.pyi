from typing import overload
import abc
import typing

import QuantConnect.Algorithm
import QuantConnect.Algorithm.Framework
import QuantConnect.Algorithm.Framework.Portfolio
import QuantConnect.Algorithm.Framework.Risk
import QuantConnect.Data.UniverseSelection
import System
import System.Collections.Generic

PyObject = typing.Any


class IRiskManagementModel(QuantConnect.Algorithm.Framework.INotifiedSecurityChanges, metaclass=abc.ABCMeta):
    """Algorithm framework model that manages an algorithm's risk/downside"""

    def ManageRisk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> System.Collections.Generic.IEnumerable[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        """
        Manages the algorithm's risk at each time step
        
        :param algorithm: The algorithm instance
        :param targets: The current portfolio targets to be assessed for risk
        """
        ...


class RiskManagementModel(System.Object, QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel):
    """Provides a base class for risk management models"""

    def ManageRisk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> System.Collections.Generic.IEnumerable[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        """
        Manages the algorithm's risk at each time step
        
        :param algorithm: The algorithm instance
        :param targets: The current portfolio targets to be assessed for risk
        """
        ...

    def OnSecuritiesChanged(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """
        Event fired each time the we add/remove securities from the data feed
        
        :param algorithm: The algorithm instance that experienced the change in securities
        :param changes: The security additions and removals from the algorithm
        """
        ...


class MaximumUnrealizedProfitPercentPerSecurity(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel):
    """
    Provides an implementation of IRiskManagementModel that limits the unrealized profit
    per holding to the specified percentage
    """

    def __init__(self, maximumUnrealizedProfitPercent: float = 0.05) -> None:
        """
        Initializes a new instance of the MaximumUnrealizedProfitPercentPerSecurity class
        
        :param maximumUnrealizedProfitPercent: The maximum percentage unrealized profit allowed for any single security holding, defaults to 5% drawdown per security
        """
        ...

    def ManageRisk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> System.Collections.Generic.IEnumerable[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        """
        Manages the algorithm's risk at each time step
        
        :param algorithm: The algorithm instance
        :param targets: The current portfolio targets to be assessed for risk
        """
        ...


class MaximumSectorExposureRiskManagementModel(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel):
    """
    Provides an implementation of IRiskManagementModel that limits
    the sector exposure to the specified percentage
    """

    def __init__(self, maximumSectorExposure: float = 0.20) -> None:
        """
        Initializes a new instance of the MaximumSectorExposureRiskManagementModel class
        
        :param maximumSectorExposure: The maximum exposure for any sector, defaults to 20% sector exposure.
        """
        ...

    def ManageRisk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> System.Collections.Generic.IEnumerable[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        """
        Manages the algorithm's risk at each time step
        
        :param algorithm: The algorithm instance
        :param targets: The current portfolio targets to be assessed for risk
        """
        ...

    def OnSecuritiesChanged(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """
        Event fired each time the we add/remove securities from the data feed
        
        :param algorithm: The algorithm instance that experienced the change in securities
        :param changes: The security additions and removals from the algorithm
        """
        ...


class MaximumDrawdownPercentPerSecurity(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel):
    """
    Provides an implementation of IRiskManagementModel that limits the drawdown
    per holding to the specified percentage
    """

    def __init__(self, maximumDrawdownPercent: float = 0.05) -> None:
        """
        Initializes a new instance of the MaximumDrawdownPercentPerSecurity class
        
        :param maximumDrawdownPercent: The maximum percentage drawdown allowed for any single security holding, defaults to 5% drawdown per security
        """
        ...

    def ManageRisk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> System.Collections.Generic.IEnumerable[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        """
        Manages the algorithm's risk at each time step
        
        :param algorithm: The algorithm instance
        :param targets: The current portfolio targets to be assessed for risk
        """
        ...


class TrailingStopRiskManagementModel(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel):
    """
    Provides an implementation of IRiskManagementModel that limits the maximum possible loss
    measured from the highest unrealized profit
    """

    def __init__(self, maximumDrawdownPercent: float = 0.05) -> None:
        """
        Initializes a new instance of the TrailingStopRiskManagementModel class
        
        :param maximumDrawdownPercent: The maximum percentage relative drawdown allowed for algorithm portfolio compared with the highest unrealized profit, defaults to 5% drawdown per security
        """
        ...

    def ManageRisk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> System.Collections.Generic.IEnumerable[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        """
        Manages the algorithm's risk at each time step
        
        :param algorithm: The algorithm instance
        :param targets: The current portfolio targets to be assessed for risk
        """
        ...


class MaximumDrawdownPercentPortfolio(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel):
    """
    Provides an implementation of IRiskManagementModel that limits the drawdown of the portfolio
    to the specified percentage. Once this is triggered the algorithm will need to be manually restarted.
    """

    def __init__(self, maximumDrawdownPercent: float = 0.05, isTrailing: bool = False) -> None:
        """
        Initializes a new instance of the MaximumDrawdownPercentPortfolio class
        
        :param maximumDrawdownPercent: The maximum percentage drawdown allowed for algorithm portfolio compared with starting value, defaults to 5% drawdown
        :param isTrailing: If "false", the drawdown will be relative to the starting value of the portfolio. If "true", the drawdown will be relative the last maximum portfolio value
        """
        ...

    def ManageRisk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> System.Collections.Generic.IEnumerable[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        """
        Manages the algorithm's risk at each time step
        
        :param algorithm: The algorithm instance
        :param targets: The current portfolio targets to be assessed for risk
        """
        ...


class RiskManagementModelPythonWrapper(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel):
    """Provides an implementation of IRiskManagementModel that wraps a PyObject object"""

    def __init__(self, model: typing.Any) -> None:
        """
        Constructor for initialising the IRiskManagementModel class with wrapped PyObject object
        
        :param model: Model defining how risk is managed
        """
        ...

    def ManageRisk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> System.Collections.Generic.IEnumerable[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        """
        Manages the algorithm's risk at each time step
        
        :param algorithm: The algorithm instance
        :param targets: The current portfolio targets to be assessed for risk
        """
        ...

    def OnSecuritiesChanged(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """
        Event fired each time the we add/remove securities from the data feed
        
        :param algorithm: The algorithm instance that experienced the change in securities
        :param changes: The security additions and removals from the algorithm
        """
        ...


class NullRiskManagementModel(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel):
    """Provides an implementation of IRiskManagementModel that does nothing"""

    def ManageRisk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> System.Collections.Generic.IEnumerable[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        """
        Manages the algorithm's risk at each time step
        
        :param algorithm: The algorithm instance
        :param targets: The current portfolio targets to be assessed for risk
        """
        ...


class CompositeRiskManagementModel(QuantConnect.Algorithm.Framework.Risk.RiskManagementModel):
    """
    Provides an implementation of IRiskManagementModel that combines multiple risk
    models into a single risk management model and properly sets each insights 'SourceModel' property.
    """

    @overload
    def __init__(self, *riskManagementModels: QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel) -> None:
        """
        Initializes a new instance of the CompositeRiskManagementModel class
        
        :param riskManagementModels: The individual risk management models defining this composite model
        """
        ...

    @overload
    def __init__(self, riskManagementModels: System.Collections.Generic.IEnumerable[QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel]) -> None:
        """
        Initializes a new instance of the CompositeRiskManagementModel class
        
        :param riskManagementModels: The individual risk management models defining this composite model
        """
        ...

    @overload
    def __init__(self, *riskManagementModels: PyObject) -> None:
        """
        Initializes a new instance of the CompositeRiskManagementModel class
        
        :param riskManagementModels: The individual risk management models defining this composite model
        """
        ...

    @overload
    def __init__(self, riskManagementModel: typing.Any) -> None:
        """
        Initializes a new instance of the CompositeRiskManagementModel class
        
        :param riskManagementModel: The individual risk management model defining this composite model
        """
        ...

    @overload
    def AddRiskManagement(self, riskManagementModel: QuantConnect.Algorithm.Framework.Risk.IRiskManagementModel) -> None:
        """
        Adds a new IRiskManagementModel instance
        
        :param riskManagementModel: The risk management model to add
        """
        ...

    @overload
    def AddRiskManagement(self, pyRiskManagementModel: typing.Any) -> None:
        """
        Adds a new IRiskManagementModel instance
        
        :param pyRiskManagementModel: The risk management model to add
        """
        ...

    def ManageRisk(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, targets: typing.List[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]) -> System.Collections.Generic.IEnumerable[QuantConnect.Algorithm.Framework.Portfolio.IPortfolioTarget]:
        """
        Manages the algorithm's risk at each time step.
        This method patches this call through the each of the wrapped models.
        
        :param algorithm: The algorithm instance
        :param targets: The current portfolio targets to be assessed for risk
        :returns: The new portfolio targets.
        """
        ...

    def OnSecuritiesChanged(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """
        Event fired each time the we add/remove securities from the data feed.
        This method patches this call through the each of the wrapped models.
        
        :param algorithm: The algorithm instance that experienced the change in securities
        :param changes: The security additions and removals from the algorithm
        """
        ...


