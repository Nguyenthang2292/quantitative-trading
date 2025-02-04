from typing import overload
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Custom.Tiingo
import QuantConnect.Data.Market
import System
import System.Collections.Generic


class Tiingo(System.Object):
    """Helper class for Tiingo configuration"""

    AuthCode: str
    """Gets the Tiingo API token."""

    IsAuthCodeSet: bool
    """Returns true if the Tiingo API token has been set."""

    @staticmethod
    def SetAuthCode(authCode: str) -> None:
        """
        Sets the Tiingo API token.
        
        :param authCode: The Tiingo API token
        """
        ...


class TiingoPrice(QuantConnect.Data.Market.TradeBar):
    """
    Tiingo daily price data
    https://api.tiingo.com/docs/tiingo/daily
    """

    @property
    def EndTime(self) -> datetime.datetime:
        """
        The end time of this data. Some data covers spans (trade bars) and as such we want
        to know the entire time span covered
        """
        ...

    @EndTime.setter
    def EndTime(self, value: datetime.datetime):
        """
        The end time of this data. Some data covers spans (trade bars) and as such we want
        to know the entire time span covered
        """
        ...

    @property
    def Period(self) -> datetime.timedelta:
        """The period of this trade bar, (second, minute, daily, ect...)"""
        ...

    @Period.setter
    def Period(self, value: datetime.timedelta):
        """The period of this trade bar, (second, minute, daily, ect...)"""
        ...

    @property
    def Date(self) -> datetime.datetime:
        """The date this data pertains to"""
        ...

    @Date.setter
    def Date(self, value: datetime.datetime):
        """The date this data pertains to"""
        ...

    @property
    def Open(self) -> float:
        """The actual (not adjusted) open price of the asset on the specific date"""
        ...

    @Open.setter
    def Open(self, value: float):
        """The actual (not adjusted) open price of the asset on the specific date"""
        ...

    @property
    def High(self) -> float:
        """The actual (not adjusted) high price of the asset on the specific date"""
        ...

    @High.setter
    def High(self, value: float):
        """The actual (not adjusted) high price of the asset on the specific date"""
        ...

    @property
    def Low(self) -> float:
        """The actual (not adjusted) low price of the asset on the specific date"""
        ...

    @Low.setter
    def Low(self, value: float):
        """The actual (not adjusted) low price of the asset on the specific date"""
        ...

    @property
    def Close(self) -> float:
        """The actual (not adjusted) closing price of the asset on the specific date"""
        ...

    @Close.setter
    def Close(self, value: float):
        """The actual (not adjusted) closing price of the asset on the specific date"""
        ...

    @property
    def Volume(self) -> float:
        """The actual (not adjusted) number of shares traded during the day"""
        ...

    @Volume.setter
    def Volume(self, value: float):
        """The actual (not adjusted) number of shares traded during the day"""
        ...

    @property
    def AdjustedOpen(self) -> float:
        """The adjusted opening price of the asset on the specific date. Returns null if not available."""
        ...

    @AdjustedOpen.setter
    def AdjustedOpen(self, value: float):
        """The adjusted opening price of the asset on the specific date. Returns null if not available."""
        ...

    @property
    def AdjustedHigh(self) -> float:
        """The adjusted high price of the asset on the specific date. Returns null if not available."""
        ...

    @AdjustedHigh.setter
    def AdjustedHigh(self, value: float):
        """The adjusted high price of the asset on the specific date. Returns null if not available."""
        ...

    @property
    def AdjustedLow(self) -> float:
        """The adjusted low price of the asset on the specific date. Returns null if not available."""
        ...

    @AdjustedLow.setter
    def AdjustedLow(self, value: float):
        """The adjusted low price of the asset on the specific date. Returns null if not available."""
        ...

    @property
    def AdjustedClose(self) -> float:
        """The adjusted close price of the asset on the specific date. Returns null if not available."""
        ...

    @AdjustedClose.setter
    def AdjustedClose(self, value: float):
        """The adjusted close price of the asset on the specific date. Returns null if not available."""
        ...

    @property
    def AdjustedVolume(self) -> int:
        """The adjusted number of shares traded during the day - adjusted for splits. Returns null if not available"""
        ...

    @AdjustedVolume.setter
    def AdjustedVolume(self, value: int):
        """The adjusted number of shares traded during the day - adjusted for splits. Returns null if not available"""
        ...

    @property
    def Dividend(self) -> float:
        """The dividend paid out on "date" (note that "date" will be the "exDate" for the dividend)"""
        ...

    @Dividend.setter
    def Dividend(self, value: float):
        """The dividend paid out on "date" (note that "date" will be the "exDate" for the dividend)"""
        ...

    @property
    def SplitFactor(self) -> float:
        """
        A factor used when a company splits or reverse splits. On days where there is ONLY a split (no dividend payment),
        you can calculate the adjusted close as follows: adjClose = "Previous Close"/splitFactor
        """
        ...

    @SplitFactor.setter
    def SplitFactor(self, value: float):
        """
        A factor used when a company splits or reverse splits. On days where there is ONLY a split (no dividend payment),
        you can calculate the adjusted close as follows: adjClose = "Previous Close"/splitFactor
        """
        ...

    def __init__(self) -> None:
        """Initializes an instance of the TiingoPrice class."""
        ...

    def DataTimeZone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type. This is useful for custom data types
        
        :returns: The DateTimeZone of this data type.
        """
        ...

    def DefaultResolution(self) -> int:
        """
        Gets the default resolution for this data and security type
        
        :returns: This method returns the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the URL string source of the file. This will be converted to a stream
        
        :param config: Configuration object
        :param date: Date of this source file
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: String URL of source file.
        """
        ...

    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, content: str, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects. Each data type creates its own factory method,
            and returns a new instance of the object
            each time it is called. The returned object is assumed to be time stamped in the config.ExchangeTimeZone.
        
        :param config: Subscription data config setup object
        :param content: Content of the source document
        :param date: Date of the requested data
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: Instance of the T:BaseData object generated by this line of the CSV.
        """
        ...

    def RequiresMapping(self) -> bool:
        """
        Indicates if there is support for mapping
        
        :returns: True indicates mapping should be used.
        """
        ...

    def SupportedResolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """Gets the supported resolution for this data and security type"""
        ...


class TiingoSymbolMapper(System.Object):
    """Helper class to map a Lean format ticker to Tiingo format"""

    @staticmethod
    def GetLeanTicker(ticker: str) -> str:
        """Maps a given Tiingo ticker to Lean equivalent"""
        ...

    @staticmethod
    def GetTiingoTicker(symbol: typing.Union[QuantConnect.Symbol, str]) -> str:
        """Maps a given Symbol instance to it's Tiingo equivalent"""
        ...


class TiingoDailyData(QuantConnect.Data.Custom.Tiingo.TiingoPrice):
    """
    Tiingo daily price data
    https://api.tiingo.com/docs/tiingo/daily
    
    This is kept for backwards compatibility, please use TiingoPrice
    """


