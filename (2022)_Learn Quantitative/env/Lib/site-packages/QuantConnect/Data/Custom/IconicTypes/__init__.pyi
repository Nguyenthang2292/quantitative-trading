from typing import overload
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Custom.IconicTypes
import QuantConnect.Data.Market
import System.Collections.Generic


class UnlinkedData(QuantConnect.Data.BaseData):
    """Data source that is unlinked (no mapping) and takes any ticker when calling AddData"""

    AnyTicker: bool
    """If true, we accept any ticker from the AddData call"""

    @property
    def Ticker(self) -> str:
        """Example data"""
        ...

    @Ticker.setter
    def Ticker(self, value: str):
        """Example data"""
        ...

    def DataTimeZone(self) -> typing.Any:
        """
        Set the data time zone to UTC
        
        :returns: Time zone as UTC.
        """
        ...

    def DefaultResolution(self) -> int:
        """
        Sets the default resolution to Second
        
        :returns: Resolution.Second. This method returns the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        ...

    def IsSparseData(self) -> bool:
        """
        Indicates whether the data source is sparse.
        If false, it will disable missing file logging.
        
        :returns: true.
        """
        ...

    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        ...

    def RequiresMapping(self) -> bool:
        """
        Indicates whether the data source can undergo
        rename events/is tied to equities.
        
        :returns: true.
        """
        ...

    def SupportedResolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """
        Gets a list of all the supported Resolutions
        
        :returns: All resolutions.
        """
        ...


class UnlinkedDataTradeBar(QuantConnect.Data.Market.TradeBar):
    """Data source that is unlinked (no mapping) and takes any ticker when calling AddData"""

    AnyTicker: bool
    """If true, we accept any ticker from the AddData call"""

    def __init__(self) -> None:
        ...

    def DataTimeZone(self) -> typing.Any:
        """
        Set the data time zone to UTC
        
        :returns: Time zone as UTC.
        """
        ...

    def DefaultResolution(self) -> int:
        """
        Sets the default resolution to Second
        
        :returns: Resolution.Second. This method returns the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        ...

    def IsSparseData(self) -> bool:
        """
        Indicates whether the data source is sparse.
        If false, it will disable missing file logging.
        
        :returns: true.
        """
        ...

    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        ...

    def RequiresMapping(self) -> bool:
        """
        Indicates whether the data source can undergo
        rename events/is tied to equities.
        
        :returns: true.
        """
        ...

    def SupportedResolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """
        Gets a list of all the supported Resolutions
        
        :returns: All resolutions.
        """
        ...


class IndexedLinkedData2(QuantConnect.Data.IndexedBaseData):
    """
    Data type that is indexed, i.e. a file that points to another file containing the contents
    we're looking for in a Symbol.
    """

    @property
    def Count(self) -> int:
        """Example data property"""
        ...

    @Count.setter
    def Count(self, value: int):
        """Example data property"""
        ...

    def DataTimeZone(self) -> typing.Any:
        """
        Set the data time zone to UTC
        
        :returns: Time zone as UTC.
        """
        ...

    def DefaultResolution(self) -> int:
        """
        Sets the default resolution to Second
        
        :returns: Resolution.Second. This method returns the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Gets the source of the index file
        
        :param config: Configuration object
        :param date: Date of this source file
        :param isLiveMode: Is live mode
        :returns: SubscriptionDataSource indicating where data is located and how it's stored.
        """
        ...

    def GetSourceForAnIndex(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], index: str, isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Determines the actual source from an index contained within a ticker folder
        
        :param config: Subscription configuration
        :param date: Date
        :param index: File to load data from
        :param isLiveMode: Is live mode
        :returns: SubscriptionDataSource pointing to the article.
        """
        ...

    def IsSparseData(self) -> bool:
        """
        Indicates whether the data source is sparse.
        If false, it will disable missing file logging.
        
        :returns: true.
        """
        ...

    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        """
        Creates an instance from a line of JSON containing article information read from the `content` directory
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param isLiveMode: Is live mode
        """
        ...

    def RequiresMapping(self) -> bool:
        """
        Indicates whether the data source can undergo
        rename events/is tied to equities.
        
        :returns: true.
        """
        ...

    def SupportedResolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """
        Gets a list of all the supported Resolutions
        
        :returns: All resolutions.
        """
        ...


class IndexedLinkedData(QuantConnect.Data.IndexedBaseData):
    """
    Data type that is indexed, i.e. a file that points to another file containing the contents
    we're looking for in a Symbol.
    """

    @property
    def Count(self) -> int:
        """Example data property"""
        ...

    @Count.setter
    def Count(self, value: int):
        """Example data property"""
        ...

    def DataTimeZone(self) -> typing.Any:
        """
        Set the data time zone to UTC
        
        :returns: Time zone as UTC.
        """
        ...

    def DefaultResolution(self) -> int:
        """
        Sets the default resolution to Second
        
        :returns: Resolution.Second. This method returns the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Gets the source of the index file
        
        :param config: Configuration object
        :param date: Date of this source file
        :param isLiveMode: Is live mode
        :returns: SubscriptionDataSource indicating where data is located and how it's stored.
        """
        ...

    def GetSourceForAnIndex(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], index: str, isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Determines the actual source from an index contained within a ticker folder
        
        :param config: Subscription configuration
        :param date: Date
        :param index: File to load data from
        :param isLiveMode: Is live mode
        :returns: SubscriptionDataSource pointing to the article.
        """
        ...

    def IsSparseData(self) -> bool:
        """
        Indicates whether the data source is sparse.
        If false, it will disable missing file logging.
        
        :returns: true.
        """
        ...

    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        """
        Creates an instance from a line of JSON containing article information read from the `content` directory
        
        :param config: Subscription configuration
        :param line: Line of data
        :param date: Date
        :param isLiveMode: Is live mode
        """
        ...

    def RequiresMapping(self) -> bool:
        """
        Indicates whether the data source can undergo
        rename events/is tied to equities.
        
        :returns: true.
        """
        ...

    def SupportedResolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """
        Gets a list of all the supported Resolutions
        
        :returns: All resolutions.
        """
        ...


class LinkedData(QuantConnect.Data.BaseData):
    """Data source that is linked (tickers that can have renames or be delisted)"""

    @property
    def Count(self) -> int:
        """Example data"""
        ...

    @Count.setter
    def Count(self, value: int):
        """Example data"""
        ...

    def DataTimeZone(self) -> typing.Any:
        """
        Set the data time zone to UTC
        
        :returns: Time zone as UTC.
        """
        ...

    def DefaultResolution(self) -> int:
        """
        Sets the default resolution to Second
        
        :returns: Resolution.Second. This method returns the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        ...

    def IsSparseData(self) -> bool:
        """
        Indicates whether the data source is sparse.
        If false, it will disable missing file logging.
        
        :returns: true.
        """
        ...

    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        ...

    def RequiresMapping(self) -> bool:
        """
        Indicates whether the data source can undergo
        rename events/is tied to equities.
        
        :returns: true.
        """
        ...

    def SupportedResolutions(self) -> System.Collections.Generic.List[QuantConnect.Resolution]:
        """
        Gets a list of all the supported Resolutions
        
        :returns: All resolutions.
        """
        ...


