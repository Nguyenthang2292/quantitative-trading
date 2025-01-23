from typing import overload
import abc
import typing

import QuantConnect.Data.Market
import QuantConnect.Indicators
import QuantConnect.Indicators.CandlestickPatterns
import System


class CandleSettingType(System.Enum):
    """Types of candlestick settings"""

    BodyLong = 0
    """Real body is long when it's longer than the average of the 10 previous candles' real body (0)"""

    BodyVeryLong = 1
    """Real body is very long when it's longer than 3 times the average of the 10 previous candles' real body (1)"""

    BodyShort = 2
    """Real body is short when it's shorter than the average of the 10 previous candles' real bodies (2)"""

    BodyDoji = 3
    """Real body is like doji's body when it's shorter than 10% the average of the 10 previous candles' high-low range (3)"""

    ShadowLong = 4
    """Shadow is long when it's longer than the real body (4)"""

    ShadowVeryLong = 5
    """Shadow is very long when it's longer than 2 times the real body (5)"""

    ShadowShort = 6
    """Shadow is short when it's shorter than half the average of the 10 previous candles' sum of shadows (6)"""

    ShadowVeryShort = 7
    """Shadow is very short when it's shorter than 10% the average of the 10 previous candles' high-low range (7)"""

    Near = 8
    """
    When measuring distance between parts of candles or width of gaps
    "near" means "<= 20% of the average of the 5 previous candles' high-low range" (8)
    """

    Far = 9
    """
    When measuring distance between parts of candles or width of gaps
    "far" means ">= 60% of the average of the 5 previous candles' high-low range" (9)
    """

    Equal = 10
    """
    When measuring distance between parts of candles or width of gaps
    "equal" means "<= 5% of the average of the 5 previous candles' high-low range" (10)
    """


class CandlestickPattern(QuantConnect.Indicators.WindowIndicator[QuantConnect.Data.Market.IBaseDataBar], metaclass=abc.ABCMeta):
    """Abstract base class for a candlestick pattern indicator"""

    def __init__(self, name: str, period: int) -> None:
        """
        Creates a new CandlestickPattern with the specified name
        
        This method is protected.
        
        :param name: The name of this indicator
        :param period: The number of data points to hold in the window
        """
        ...

    @staticmethod
    def GetCandleAverage(type: QuantConnect.Indicators.CandlestickPatterns.CandleSettingType, sum: float, tradeBar: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Returns the average range of the previous candles
        
        This method is protected.
        
        :param type: The type of setting to use
        :param sum: The sum of the previous candles ranges
        :param tradeBar: The input candle
        """
        ...

    @staticmethod
    def GetCandleColor(tradeBar: QuantConnect.Data.Market.IBaseDataBar) -> int:
        """
        Returns the candle color of a candle
        
        This method is protected.
        
        :param tradeBar: The input candle
        :returns: This method returns the int value of a member of the QuantConnect.Indicators.CandlestickPatterns.CandleColor enum.
        """
        ...

    @staticmethod
    def GetCandleGapDown(tradeBar: QuantConnect.Data.Market.IBaseDataBar, previousBar: QuantConnect.Data.Market.IBaseDataBar) -> bool:
        """
        Returns true if the candle is lower than the previous one
        
        This method is protected.
        """
        ...

    @staticmethod
    def GetCandleGapUp(tradeBar: QuantConnect.Data.Market.IBaseDataBar, previousBar: QuantConnect.Data.Market.IBaseDataBar) -> bool:
        """
        Returns true if the candle is higher than the previous one
        
        This method is protected.
        """
        ...

    @staticmethod
    def GetCandleRange(type: QuantConnect.Indicators.CandlestickPatterns.CandleSettingType, tradeBar: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Returns the range of a candle
        
        This method is protected.
        
        :param type: The type of setting to use
        :param tradeBar: The input candle
        """
        ...

    @staticmethod
    def GetHighLowRange(tradeBar: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Returns the full range of the candle
        
        This method is protected.
        
        :param tradeBar: The input candle
        """
        ...

    @staticmethod
    def GetLowerShadow(tradeBar: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Returns the range of the candle's lower shadow
        
        This method is protected.
        
        :param tradeBar: The input candle
        """
        ...

    @staticmethod
    def GetRealBody(tradeBar: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Returns the distance between the close and the open of a candle
        
        This method is protected.
        
        :param tradeBar: The input candle
        """
        ...

    @staticmethod
    def GetRealBodyGapDown(tradeBar: QuantConnect.Data.Market.IBaseDataBar, previousBar: QuantConnect.Data.Market.IBaseDataBar) -> bool:
        """
        Returns true if the candle is lower than the previous one (with no body overlap)
        
        This method is protected.
        """
        ...

    @staticmethod
    def GetRealBodyGapUp(tradeBar: QuantConnect.Data.Market.IBaseDataBar, previousBar: QuantConnect.Data.Market.IBaseDataBar) -> bool:
        """
        Returns true if the candle is higher than the previous one (with no body overlap)
        
        This method is protected.
        """
        ...

    @staticmethod
    def GetUpperShadow(tradeBar: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Returns the range of the candle's upper shadow
        
        This method is protected.
        
        :param tradeBar: The input candle
        """
        ...


class Hammer(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Hammer candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the Hammer class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Hammer class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class GapSideBySideWhite(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Up/Down-gap side-by-side white lines candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the GapSideBySideWhite class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the GapSideBySideWhite class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class ThreeOutside(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Three Outside Up/Down candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the ThreeOutside class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the ThreeOutside class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...


class Doji(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Doji candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the Doji class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Doji class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class TwoCrows(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Two Crows candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the TwoCrows class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the TwoCrows class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class Hikkake(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Hikkake candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the Hikkake class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Hikkake class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class AbandonedBaby(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Abandoned Baby candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str, penetration: float = 0.3) -> None:
        """
        Initializes a new instance of the AbandonedBaby class using the specified name.
        
        :param name: The name of this indicator
        :param penetration: Percentage of penetration of a candle within another candle
        """
        ...

    @overload
    def __init__(self, penetration: float) -> None:
        """
        Initializes a new instance of the AbandonedBaby class.
        
        :param penetration: Percentage of penetration of a candle within another candle
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the AbandonedBaby class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class Marubozu(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Marubozu candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the Marubozu class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Marubozu class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class HighWaveCandle(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """High-Wave Candle candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the HighWaveCandle class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the HighWaveCandle class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class OnNeck(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """On-Neck candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the OnNeck class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the OnNeck class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class CandleRangeType(System.Enum):
    """Types of candlestick ranges"""

    RealBody = 0
    """The part of the candle between open and close (0)"""

    HighLow = 1
    """The complete range of the candle (1)"""

    Shadows = 2
    """The shadows (or tails) of the candle (2)"""


class CandleColor(System.Enum):
    """Colors of a candle"""

    White = 1
    """White is an up candle (close higher or equal than open) (1)"""

    Black = -1
    """Black is a down candle (close lower than open) (-1)"""


class HangingMan(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Hanging Man candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the HangingMan class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the HangingMan class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class Breakaway(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Breakaway candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the Breakaway class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Breakaway class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class EveningStar(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Evening Star candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str, penetration: float = 0.3) -> None:
        """
        Initializes a new instance of the EveningStar class using the specified name.
        
        :param name: The name of this indicator
        :param penetration: Percentage of penetration of a candle within another candle
        """
        ...

    @overload
    def __init__(self, penetration: float) -> None:
        """
        Initializes a new instance of the EveningStar class.
        
        :param penetration: Percentage of penetration of a candle within another candle
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the EveningStar class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class DragonflyDoji(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Dragonfly Doji candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the DragonflyDoji class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the DragonflyDoji class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class SeparatingLines(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Separating Lines candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the SeparatingLines class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the SeparatingLines class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class ConcealedBabySwallow(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Concealed Baby Swallow candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the ConcealedBabySwallow class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the ConcealedBabySwallow class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class DarkCloudCover(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Dark Cloud Cover candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str, penetration: float = 0.5) -> None:
        """
        Initializes a new instance of the DarkCloudCover class using the specified name.
        
        :param name: The name of this indicator
        :param penetration: Percentage of penetration of a candle within another candle
        """
        ...

    @overload
    def __init__(self, penetration: float) -> None:
        """
        Initializes a new instance of the DarkCloudCover class.
        
        :param penetration: Percentage of penetration of a candle within another candle
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the DarkCloudCover class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class IdenticalThreeCrows(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Identical Three Crows candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the IdenticalThreeCrows class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the IdenticalThreeCrows class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class UpsideGapTwoCrows(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Upside Gap Two Crows candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the UpsideGapTwoCrows class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the UpsideGapTwoCrows class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class HikkakeModified(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Hikkake Modified candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the HikkakeModified class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the HikkakeModified class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class UniqueThreeRiver(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Unique Three River candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the UniqueThreeRiver class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the UniqueThreeRiver class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class HaramiCross(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Harami Cross candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the HaramiCross class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the HaramiCross class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class LongLineCandle(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Long Line Candle candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the LongLineCandle class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the LongLineCandle class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class Piercing(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Piercing candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the Piercing class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Piercing class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class ThreeStarsInSouth(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Three Stars In The South candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the ThreeStarsInSouth class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the ThreeStarsInSouth class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class ThreeLineStrike(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Three Line Strike candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the ThreeLineStrike class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the ThreeLineStrike class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class ThreeInside(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Three Inside Up/Down candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the ThreeInside class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the ThreeInside class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class Thrusting(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Thrusting candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the Thrusting class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Thrusting class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class UpDownGapThreeMethods(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Up/Down Gap Three Methods candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the UpDownGapThreeMethods class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the UpDownGapThreeMethods class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...


class Tristar(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Tristar candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the Tristar class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Tristar class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class KickingByLength(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Kicking (bull/bear determined by the longer marubozu) candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the KickingByLength class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the KickingByLength class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class TasukiGap(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Tasuki Gap candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the TasukiGap class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the TasukiGap class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class Harami(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Harami candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the Harami class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Harami class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class DojiStar(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Doji Star candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the DojiStar class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the DojiStar class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class InNeck(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """In-Neck candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the InNeck class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the InNeck class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class ThreeWhiteSoldiers(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Three Advancing White Soldiers candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the ThreeWhiteSoldiers class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the ThreeWhiteSoldiers class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class ThreeBlackCrows(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Three Black Crows candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the ThreeBlackCrows class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the ThreeBlackCrows class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class AdvanceBlock(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Advance Block candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the AdvanceBlock class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the AdvanceBlock class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class ShortLineCandle(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Short Line Candle candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the ShortLineCandle class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the ShortLineCandle class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class RickshawMan(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Rickshaw Man candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the RickshawMan class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the RickshawMan class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class MatHold(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Mat Hold candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str, penetration: float = 0.5) -> None:
        """
        Initializes a new instance of the MatHold class using the specified name.
        
        :param name: The name of this indicator
        :param penetration: Percentage of penetration of a candle within another candle
        """
        ...

    @overload
    def __init__(self, penetration: float) -> None:
        """
        Initializes a new instance of the MatHold class.
        
        :param penetration: Percentage of penetration of a candle within another candle
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the MatHold class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class ShootingStar(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Shooting Star candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the ShootingStar class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the ShootingStar class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class HomingPigeon(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Homing Pigeon candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the HomingPigeon class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the HomingPigeon class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class Kicking(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Kicking candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the Kicking class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Kicking class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class Counterattack(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Counterattack candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the Counterattack class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Counterattack class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class LadderBottom(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Ladder Bottom candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the LadderBottom class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the LadderBottom class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class Engulfing(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Engulfing candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the Engulfing class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Engulfing class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...


class InvertedHammer(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Inverted Hammer candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the InvertedHammer class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the InvertedHammer class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class GravestoneDoji(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Gravestone Doji candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the GravestoneDoji class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the GravestoneDoji class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class Takuri(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Takuri (Dragonfly Doji with very long lower shadow) candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the Takuri class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Takuri class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class MorningStar(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Morning Star candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str, penetration: float = 0.3) -> None:
        """
        Initializes a new instance of the MorningStar class using the specified name.
        
        :param name: The name of this indicator
        :param penetration: Percentage of penetration of a candle within another candle
        """
        ...

    @overload
    def __init__(self, penetration: float) -> None:
        """
        Initializes a new instance of the MorningStar class.
        
        :param penetration: Percentage of penetration of a candle within another candle
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the MorningStar class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class EveningDojiStar(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Evening Doji Star candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str, penetration: float = 0.3) -> None:
        """
        Initializes a new instance of the EveningDojiStar class using the specified name.
        
        :param name: The name of this indicator
        :param penetration: Percentage of penetration of a candle within another candle
        """
        ...

    @overload
    def __init__(self, penetration: float) -> None:
        """
        Initializes a new instance of the EveningDojiStar class.
        
        :param penetration: Percentage of penetration of a candle within another candle
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the EveningDojiStar class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class SpinningTop(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Spinning Top candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the SpinningTop class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the SpinningTop class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class RiseFallThreeMethods(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Rising/Falling Three Methods candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the RiseFallThreeMethods class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the RiseFallThreeMethods class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class StalledPattern(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Stalled Pattern candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the StalledPattern class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the StalledPattern class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class MatchingLow(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Matching Low candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the MatchingLow class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the MatchingLow class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class MorningDojiStar(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Morning Doji Star candlestick pattern"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str, penetration: float = 0.3) -> None:
        """
        Initializes a new instance of the MorningDojiStar class using the specified name.
        
        :param name: The name of this indicator
        :param penetration: Percentage of penetration of a candle within another candle
        """
        ...

    @overload
    def __init__(self, penetration: float) -> None:
        """
        Initializes a new instance of the MorningDojiStar class.
        
        :param penetration: Percentage of penetration of a candle within another candle
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the MorningDojiStar class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class CandleSetting(System.Object):
    """Represents a candle setting"""

    @property
    def RangeType(self) -> int:
        """
        The candle range type
        
        This property contains the int value of a member of the QuantConnect.Indicators.CandlestickPatterns.CandleRangeType enum.
        """
        ...

    @RangeType.setter
    def RangeType(self, value: int):
        """
        The candle range type
        
        This property contains the int value of a member of the QuantConnect.Indicators.CandlestickPatterns.CandleRangeType enum.
        """
        ...

    @property
    def AveragePeriod(self) -> int:
        """The number of previous candles to average"""
        ...

    @AveragePeriod.setter
    def AveragePeriod(self, value: int):
        """The number of previous candles to average"""
        ...

    @property
    def Factor(self) -> float:
        """A multiplier to calculate candle ranges"""
        ...

    @Factor.setter
    def Factor(self, value: float):
        """A multiplier to calculate candle ranges"""
        ...

    def __init__(self, rangeType: QuantConnect.Indicators.CandlestickPatterns.CandleRangeType, averagePeriod: int, factor: float) -> None:
        """
        Creates an instance of the CandleSetting class
        
        :param rangeType: The range type
        :param averagePeriod: The average period
        :param factor: The factor
        """
        ...


class CandleSettings(System.Object):
    """Candle settings for all candlestick patterns"""

    @staticmethod
    def Get(type: QuantConnect.Indicators.CandlestickPatterns.CandleSettingType) -> QuantConnect.Indicators.CandlestickPatterns.CandleSetting:
        """
        Returns the candle setting for the requested type
        
        :param type: The candle setting type
        """
        ...

    @staticmethod
    def Set(type: QuantConnect.Indicators.CandlestickPatterns.CandleSettingType, setting: QuantConnect.Indicators.CandlestickPatterns.CandleSetting) -> None:
        """
        Changes the default candle setting for the requested type
        
        :param type: The candle setting type
        :param setting: The candle setting
        """
        ...


class LongLeggedDoji(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Long Legged Doji candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the LongLeggedDoji class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the LongLeggedDoji class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class StickSandwich(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Stick Sandwich candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the StickSandwich class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the StickSandwich class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class BeltHold(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Belt-hold candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the BeltHold class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the BeltHold class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


class ClosingMarubozu(QuantConnect.Indicators.CandlestickPatterns.CandlestickPattern):
    """Closing Marubozu candlestick pattern indicator"""

    @property
    def IsReady(self) -> bool:
        """Gets a flag indicating when this indicator is ready and fully initialized"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the ClosingMarubozu class using the specified name.
        
        :param name: The name of this indicator
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the ClosingMarubozu class."""
        ...

    def ComputeNextValue(self, window: QuantConnect.Indicators.IReadOnlyWindow[QuantConnect.Data.Market.IBaseDataBar], input: QuantConnect.Data.Market.IBaseDataBar) -> float:
        """
        Computes the next value of this indicator from the given state
        
        This method is protected.
        
        :param window: The window of data held in this indicator
        :param input: The input given to the indicator
        :returns: A new value for this indicator.
        """
        ...

    def Reset(self) -> None:
        """Resets this indicator to its initial state"""
        ...


