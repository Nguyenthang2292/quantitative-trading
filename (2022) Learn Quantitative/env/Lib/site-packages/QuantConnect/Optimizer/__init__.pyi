from typing import overload
import abc
import typing

import QuantConnect.Optimizer
import QuantConnect.Optimizer.Objectives
import QuantConnect.Optimizer.Parameters
import QuantConnect.Optimizer.Strategies
import QuantConnect.Packets
import System
import System.Collections.Concurrent
import System.Collections.Generic

QuantConnect_Optimizer__EventContainer_Callable = typing.TypeVar("QuantConnect_Optimizer__EventContainer_Callable")
QuantConnect_Optimizer__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Optimizer__EventContainer_ReturnType")


class OptimizationResult(System.Object):
    """Defines the result of Lean compute job"""

    Initial: QuantConnect.Optimizer.OptimizationResult = ...
    """Corresponds to initial result to drive the optimization strategy"""

    @property
    def BacktestId(self) -> str:
        """The backtest id that generated this result"""
        ...

    @property
    def Id(self) -> int:
        """Parameter set Id"""
        ...

    @property
    def JsonBacktestResult(self) -> str:
        """Json Backtest result"""
        ...

    @property
    def ParameterSet(self) -> QuantConnect.Optimizer.Parameters.ParameterSet:
        """The parameter set at which the result was achieved"""
        ...

    def __init__(self, jsonBacktestResult: str, parameterSet: QuantConnect.Optimizer.Parameters.ParameterSet, backtestId: str) -> None:
        """
        Create an instance of OptimizationResult
        
        :param jsonBacktestResult: Optimization target value for this backtest
        :param parameterSet: Parameter set used in compute job
        :param backtestId: The backtest id that generated this result
        """
        ...


class OptimizationNodePacket(QuantConnect.Packets.Packet):
    """Provide a packet type containing information on the optimization compute job."""

    @property
    def UserId(self) -> int:
        """User Id placing request"""
        ...

    @UserId.setter
    def UserId(self, value: int):
        """User Id placing request"""
        ...

    @property
    def UserToken(self) -> str:
        ...

    @UserToken.setter
    def UserToken(self, value: str):
        ...

    @property
    def ProjectId(self) -> int:
        """Project Id of the request"""
        ...

    @ProjectId.setter
    def ProjectId(self, value: int):
        """Project Id of the request"""
        ...

    @property
    def CompileId(self) -> str:
        """Unique compile id of this optimization"""
        ...

    @CompileId.setter
    def CompileId(self, value: str):
        """Unique compile id of this optimization"""
        ...

    @property
    def OptimizationId(self) -> str:
        """The unique optimization Id of the request"""
        ...

    @OptimizationId.setter
    def OptimizationId(self, value: str):
        """The unique optimization Id of the request"""
        ...

    @property
    def OrganizationId(self) -> str:
        """Organization Id of the request"""
        ...

    @OrganizationId.setter
    def OrganizationId(self, value: str):
        """Organization Id of the request"""
        ...

    @property
    def MaximumConcurrentBacktests(self) -> int:
        """Limit for the amount of concurrent backtests being run"""
        ...

    @MaximumConcurrentBacktests.setter
    def MaximumConcurrentBacktests(self, value: int):
        """Limit for the amount of concurrent backtests being run"""
        ...

    @property
    def OptimizationStrategy(self) -> str:
        """Optimization strategy name"""
        ...

    @OptimizationStrategy.setter
    def OptimizationStrategy(self, value: str):
        """Optimization strategy name"""
        ...

    @property
    def Criterion(self) -> QuantConnect.Optimizer.Objectives.Target:
        """Objective settings"""
        ...

    @Criterion.setter
    def Criterion(self, value: QuantConnect.Optimizer.Objectives.Target):
        """Objective settings"""
        ...

    @property
    def Constraints(self) -> System.Collections.Generic.IReadOnlyList[QuantConnect.Optimizer.Objectives.Constraint]:
        """Optimization constraints"""
        ...

    @Constraints.setter
    def Constraints(self, value: System.Collections.Generic.IReadOnlyList[QuantConnect.Optimizer.Objectives.Constraint]):
        """Optimization constraints"""
        ...

    @property
    def OptimizationParameters(self) -> System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter]:
        """The user optimization parameters"""
        ...

    @OptimizationParameters.setter
    def OptimizationParameters(self, value: System.Collections.Generic.HashSet[QuantConnect.Optimizer.Parameters.OptimizationParameter]):
        """The user optimization parameters"""
        ...

    @property
    def OptimizationStrategySettings(self) -> QuantConnect.Optimizer.Strategies.OptimizationStrategySettings:
        """The user optimization parameters"""
        ...

    @OptimizationStrategySettings.setter
    def OptimizationStrategySettings(self, value: QuantConnect.Optimizer.Strategies.OptimizationStrategySettings):
        """The user optimization parameters"""
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new instance"""
        ...

    @overload
    def __init__(self, packetType: QuantConnect.Packets.PacketType) -> None:
        """
        Creates a new instance
        
        This method is protected.
        """
        ...


class OptimizationStatus(System.Enum):
    """The different optimization status"""

    New = 0
    """Just created and not running optimization (0)"""

    Aborted = 1
    """We failed or we were aborted (1)"""

    Running = 2
    """We are running (2)"""

    Completed = 3
    """Optimization job has completed (3)"""


class LeanOptimizer(System.Object, System.IDisposable, metaclass=abc.ABCMeta):
    """Base Lean optimizer class in charge of handling an optimization job packet"""

    @property
    def CompletedBacktests(self) -> int:
        """
        The total completed backtests count
        
        This property is protected.
        """
        ...

    @property
    def Status(self) -> int:
        """
        The current optimization status
        
        This property contains the int value of a member of the QuantConnect.Optimizer.OptimizationStatus enum.
        
        This property is protected.
        """
        ...

    @Status.setter
    def Status(self, value: int):
        """
        The current optimization status
        
        This property contains the int value of a member of the QuantConnect.Optimizer.OptimizationStatus enum.
        
        This property is protected.
        """
        ...

    @property
    def OptimizationTarget(self) -> QuantConnect.Optimizer.Objectives.Target:
        """
        The optimization target
        
        This field is protected.
        """
        ...

    @property
    def RunningParameterSetForBacktest(self) -> System.Collections.Concurrent.ConcurrentDictionary[str, QuantConnect.Optimizer.Parameters.ParameterSet]:
        """
        Collection holding ParameterSet for each backtest id we are waiting to finish
        
        This field is protected.
        """
        ...

    @property
    def PendingParameterSet(self) -> System.Collections.Concurrent.ConcurrentQueue[QuantConnect.Optimizer.Parameters.ParameterSet]:
        """
        Collection holding ParameterSet for each backtest id we are waiting to launch
        
        This field is protected.
        """
        ...

    @property
    def Strategy(self) -> QuantConnect.Optimizer.Strategies.IOptimizationStrategy:
        """
        The optimization strategy being used
        
        This field is protected.
        """
        ...

    @property
    def NodePacket(self) -> QuantConnect.Optimizer.OptimizationNodePacket:
        """
        The optimization packet
        
        This field is protected.
        """
        ...

    @property
    def Disposed(self) -> bool:
        """
        Indicates whether optimizer was disposed
        
        This property is protected.
        """
        ...

    @property
    def Ended(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Optimizer.OptimizationResult], None], None]:
        """Event triggered when the optimization work ended"""
        ...

    @Ended.setter
    def Ended(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Optimizer.OptimizationResult], None], None]):
        """Event triggered when the optimization work ended"""
        ...

    def __init__(self, nodePacket: QuantConnect.Optimizer.OptimizationNodePacket) -> None:
        """
        Creates a new instance
        
        This method is protected.
        
        :param nodePacket: The optimization node packet to handle
        """
        ...

    def AbortLean(self, backtestId: str) -> None:
        """
        Handles stopping Lean process
        
        This method is protected.
        
        :param backtestId: Specified backtest id
        """
        ...

    def Dispose(self) -> None:
        """Disposes of any resources"""
        ...

    def GetCurrentEstimate(self) -> int:
        """Returns the current optimization status and strategy estimates"""
        ...

    def GetLogDetails(self) -> str:
        """
        Helper method to have pretty more informative logs
        
        This method is protected.
        """
        ...

    def GetRuntimeStatistics(self) -> System.Collections.Generic.Dictionary[str, str]:
        """Get the current runtime statistics"""
        ...

    def NewResult(self, jsonBacktestResult: str, backtestId: str) -> None:
        """
        Handles a new backtest json result matching a requested backtest id
        
        This method is protected.
        
        :param jsonBacktestResult: The backtest json result
        :param backtestId: The associated backtest id
        """
        ...

    def RunLean(self, parameterSet: QuantConnect.Optimizer.Parameters.ParameterSet) -> str:
        """
        Handles starting Lean for a given parameter set
        
        This method is protected.
        
        :param parameterSet: The parameter set for the backtest to run
        :returns: The new unique backtest id.
        """
        ...

    def SendUpdate(self) -> None:
        """
        Sends an update of the current optimization status to the user
        
        This method is protected.
        """
        ...

    def SetOptimizationStatus(self, optimizationStatus: QuantConnect.Optimizer.OptimizationStatus) -> None:
        """
        Sets the current optimization status
        
        This method is protected.
        
        :param optimizationStatus: The new optimization status
        """
        ...

    def Start(self) -> None:
        """Starts the optimization"""
        ...

    def TriggerOnEndEvent(self) -> None:
        """
        Triggers the optimization job end event
        
        This method is protected.
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Optimizer__EventContainer_Callable, QuantConnect_Optimizer__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Optimizer__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Optimizer__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Optimizer__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


