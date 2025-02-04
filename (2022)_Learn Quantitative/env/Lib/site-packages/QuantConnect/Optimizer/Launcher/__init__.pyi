from typing import overload
import QuantConnect.Optimizer
import QuantConnect.Optimizer.Launcher
import QuantConnect.Optimizer.Parameters
import System


class Program(System.Object):
    """This class has no documentation."""

    @staticmethod
    def Main() -> None:
        ...


class ConsoleLeanOptimizer(QuantConnect.Optimizer.LeanOptimizer):
    """Optimizer implementation that launches Lean as a local process"""

    def __init__(self, nodePacket: QuantConnect.Optimizer.OptimizationNodePacket) -> None:
        """
        Creates a new instance
        
        :param nodePacket: The optimization node packet to handle
        """
        ...

    def AbortLean(self, backtestId: str) -> None:
        """
        Stops lean process
        
        This method is protected.
        
        :param backtestId: Specified backtest id
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


