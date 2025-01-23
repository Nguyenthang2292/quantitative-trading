from typing import overload
import abc
import datetime
import typing

import QuantConnect.Optimizer
import QuantConnect.Optimizer.Objectives
import QuantConnect.Optimizer.Parameters
import QuantConnect.Optimizer.Strategies
import System
import System.Collections.Generic

QuantConnect_Optimizer_Strategies__EventContainer_Callable = typing.TypeVar("QuantConnect_Optimizer_Strategies__EventContainer_Callable")
QuantConnect_Optimizer_Strategies__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Optimizer_Strategies__EventContainer_ReturnType")


class OptimizationStrategySettings(System.Object):
    """Defines the specific optimization strategy settings"""

    @property
    def MaxRuntime(self) -> datetime.timedelta:
        """TODO: implement"""
        ...

    @MaxRuntime.setter
    def MaxRuntime(self, value: datetime.timedelta):
        """TODO: implement"""
        ...


class StepBaseOptimizationStrategySettings(QuantConnect.Optimizer.Strategies.OptimizationStrategySettings):
    """Defines the specific optimization strategy settings"""

    @property
    def DefaultSegmentAmount(self) -> int:
        """Defines the default number of segments for the next step"""
        ...

    @DefaultSegmentAmount.setter
    def DefaultSegmentAmount(self, value: int):
        """Defines the default number of segments for the next step"""
        ...


class IOptimizationStrategy(metaclass=abc.ABCMeta):
    """Defines the optimization settings, direction, solution and exit, i.e. optimization strategy"""

    @property
    @abc.abstractmethod
    def NewParameterSet(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Optimizer.Parameters.ParameterSet], None], None]:
        """Fires when new parameter set is retrieved"""
        ...

    @NewParameterSet.setter
    @abc.abstractmethod
    def NewParameterSet(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Optimizer.Parameters.ParameterSet], None], None]):
        """Fires when new parameter set is retrieved"""
        ...

    @property
    @abc.abstractmethod
    def Solution(self) -> QuantConnect.Optimizer.OptimizationResult:
        """Best found solution, its value and parameter set"""
        ...

    def GetTotalBacktestEstimate(self) -> int:
        """Estimates amount of parameter sets that can be run"""
        ...

    def Initialize(self, target: QuantConnect.Optimizer.Objectives.Target, constraints: System.Collections.Generic.IReadOnlyList[QuantConnect.Optimizer.Objectives.Constraint], parameters: System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter], settings: QuantConnect.Optimizer.Strategies.OptimizationStrategySettings) -> None:
        """
        Initializes the strategy using generator, extremum settings and optimization parameters
        
        :param target: The optimization target
        :param constraints: The optimization constraints to apply on backtest results
        :param parameters: optimization parameters
        :param settings: optimization strategy advanced settings
        """
        ...

    def PushNewResults(self, result: QuantConnect.Optimizer.OptimizationResult) -> None:
        """
        Callback when lean compute job completed.
        
        :param result: Lean compute job result and corresponding parameter set
        """
        ...


class StepBaseOptimizationStrategy(System.Object, QuantConnect.Optimizer.Strategies.IOptimizationStrategy, typing.Iterable[str], metaclass=abc.ABCMeta):
    """Base class for any optimization built on top of brute force optimization method"""

    @property
    def Initialized(self) -> bool:
        """
        Indicates was strategy initialized or no
        
        This field is protected.
        """
        ...

    @Initialized.setter
    def Initialized(self, value: bool):
        """
        Indicates was strategy initialized or no
        
        This field is protected.
        """
        ...

    @property
    def OptimizationParameters(self) -> System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter]:
        """
        Optimization parameters
        
        This field is protected.
        """
        ...

    @OptimizationParameters.setter
    def OptimizationParameters(self, value: System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter]):
        """
        Optimization parameters
        
        This field is protected.
        """
        ...

    @property
    def Target(self) -> QuantConnect.Optimizer.Objectives.Target:
        """
        Optimization target, i.e. maximize or minimize
        
        This field is protected.
        """
        ...

    @Target.setter
    def Target(self, value: QuantConnect.Optimizer.Objectives.Target):
        """
        Optimization target, i.e. maximize or minimize
        
        This field is protected.
        """
        ...

    @property
    def Constraints(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Optimizer.Objectives.Constraint]:
        """
        Optimization constraints; if it doesn't comply just drop the backtest
        
        This field is protected.
        """
        ...

    @Constraints.setter
    def Constraints(self, value: System.Collections.Generic.IEnumerable[QuantConnect.Optimizer.Objectives.Constraint]):
        """
        Optimization constraints; if it doesn't comply just drop the backtest
        
        This field is protected.
        """
        ...

    @property
    def Solution(self) -> QuantConnect.Optimizer.OptimizationResult:
        """Keep the best found solution - lean computed job result and corresponding  parameter set"""
        ...

    @Solution.setter
    def Solution(self, value: QuantConnect.Optimizer.OptimizationResult):
        """Keep the best found solution - lean computed job result and corresponding  parameter set"""
        ...

    @property
    def Settings(self) -> QuantConnect.Optimizer.Strategies.OptimizationStrategySettings:
        """Advanced strategy settings"""
        ...

    @Settings.setter
    def Settings(self, value: QuantConnect.Optimizer.Strategies.OptimizationStrategySettings):
        """Advanced strategy settings"""
        ...

    @property
    def NewParameterSet(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Optimizer.Parameters.ParameterSet], None], None]:
        """Fires when new parameter set is generated"""
        ...

    @NewParameterSet.setter
    def NewParameterSet(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Optimizer.Parameters.ParameterSet], None], None]):
        """Fires when new parameter set is generated"""
        ...

    def GetTotalBacktestEstimate(self) -> int:
        """
        Calculate number of parameter sets within grid
        
        :returns: Number of parameter sets for given optimization parameters.
        """
        ...

    def Initialize(self, target: QuantConnect.Optimizer.Objectives.Target, constraints: System.Collections.Generic.IReadOnlyList[QuantConnect.Optimizer.Objectives.Constraint], parameters: System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter], settings: QuantConnect.Optimizer.Strategies.OptimizationStrategySettings) -> None:
        """
        Initializes the strategy using generator, extremum settings and optimization parameters
        
        :param target: The optimization target
        :param constraints: The optimization constraints to apply on backtest results
        :param parameters: Optimization parameters
        :param settings: Optimization strategy settings
        """
        ...

    def OnNewParameterSet(self, parameterSet: QuantConnect.Optimizer.Parameters.ParameterSet) -> None:
        """
        Handles new parameter set
        
        This method is protected.
        
        :param parameterSet: New parameter set
        """
        ...

    def ProcessNewResult(self, result: QuantConnect.Optimizer.OptimizationResult) -> None:
        """This method is protected."""
        ...

    def PushNewResults(self, result: QuantConnect.Optimizer.OptimizationResult) -> None:
        """
        Checks whether new lean compute job better than previous and run new iteration if necessary.
        
        :param result: Lean compute job result and corresponding parameter set
        """
        ...

    def Step(self, args: System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter]) -> System.Collections.Generic.IEnumerable[QuantConnect.Optimizer.Parameters.ParameterSet]:
        """
        Enumerate all possible arrangements
        
        This method is protected.
        
        :returns: Collection of possible combinations for given optimization parameters settings.
        """
        ...


class GridSearchOptimizationStrategy(QuantConnect.Optimizer.Strategies.StepBaseOptimizationStrategy):
    """Find the best solution in first generation"""

    def PushNewResults(self, result: QuantConnect.Optimizer.OptimizationResult) -> None:
        """
        Checks whether new lean compute job better than previous and run new iteration if necessary.
        
        :param result: Lean compute job result and corresponding parameter set
        """
        ...


class EulerSearchOptimizationStrategy(QuantConnect.Optimizer.Strategies.StepBaseOptimizationStrategy):
    """Advanced brute-force strategy with search in-depth for best solution on previous step"""

    def Initialize(self, target: QuantConnect.Optimizer.Objectives.Target, constraints: System.Collections.Generic.IReadOnlyList[QuantConnect.Optimizer.Objectives.Constraint], parameters: System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter], settings: QuantConnect.Optimizer.Strategies.OptimizationStrategySettings) -> None:
        """
        Initializes the strategy using generator, extremum settings and optimization parameters
        
        :param target: The optimization target
        :param constraints: The optimization constraints to apply on backtest results
        :param parameters: Optimization parameters
        :param settings: Optimization strategy settings
        """
        ...

    def OnNewParameterSet(self, parameterSet: QuantConnect.Optimizer.Parameters.ParameterSet) -> None:
        """
        Handles new parameter set
        
        This method is protected.
        
        :param parameterSet: New parameter set
        """
        ...

    def PushNewResults(self, result: QuantConnect.Optimizer.OptimizationResult) -> None:
        """
        Checks whether new lean compute job better than previous and run new iteration if necessary.
        
        :param result: Lean compute job result and corresponding parameter set
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Optimizer_Strategies__EventContainer_Callable, QuantConnect_Optimizer_Strategies__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Optimizer_Strategies__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Optimizer_Strategies__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Optimizer_Strategies__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


