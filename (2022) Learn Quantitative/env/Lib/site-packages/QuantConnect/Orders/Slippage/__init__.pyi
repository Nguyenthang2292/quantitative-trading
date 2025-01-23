from typing import overload
import abc

import QuantConnect.Orders
import QuantConnect.Orders.Slippage
import QuantConnect.Securities
import System


class ISlippageModel(metaclass=abc.ABCMeta):
    """Represents a model that simulates market order slippage"""

    def GetSlippageApproximation(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> float:
        """Slippage Model. Return a decimal cash slippage approximation on the order."""
        ...


class ConstantSlippageModel(System.Object, QuantConnect.Orders.Slippage.ISlippageModel):
    """Represents a slippage model that uses a constant percentage of slip"""

    def __init__(self, slippagePercent: float) -> None:
        """
        Initializes a new instance of the ConstantSlippageModel class
        
        :param slippagePercent: The slippage percent for each order. Percent is ranged 0 to 1.
        """
        ...

    def GetSlippageApproximation(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> float:
        """Slippage Model. Return a decimal cash slippage approximation on the order."""
        ...


class VolumeShareSlippageModel(System.Object, QuantConnect.Orders.Slippage.ISlippageModel):
    """
    Represents a slippage model that is calculated by multiplying the price impact constant
    by the square of the ratio of the order to the total volume.
    """

    def __init__(self, volumeLimit: float = 0.025, priceImpact: float = 0.1) -> None:
        """
        Initializes a new instance of the VolumeShareSlippageModel class
        
        :param priceImpact: Defines how large of an impact the order will have on the price calculation
        """
        ...

    def GetSlippageApproximation(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> float:
        """Slippage Model. Return a decimal cash slippage approximation on the order."""
        ...


class AlphaStreamsSlippageModel(System.Object, QuantConnect.Orders.Slippage.ISlippageModel):
    """Represents a slippage model that uses a constant percentage of slip"""

    def __init__(self) -> None:
        """Initializes a new instance of the AlphaStreamsSlippageModel class"""
        ...

    def GetSlippageApproximation(self, asset: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> float:
        """Return a decimal cash slippage approximation on the order."""
        ...


