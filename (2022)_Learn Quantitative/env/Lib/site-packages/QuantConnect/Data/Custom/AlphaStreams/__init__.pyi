from typing import overload
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Custom.AlphaStreams
import QuantConnect.Orders
import QuantConnect.Securities
import QuantConnect.Securities.Positions
import System
import System.Collections.Generic


class AlphaStreamsOrderEvent(QuantConnect.Data.BaseData):
    """Snapshot of an algorithms portfolio state"""

    @property
    def AlphaId(self) -> str:
        """The deployed alpha id. This is the id generated upon submission to the alpha marketplace"""
        ...

    @AlphaId.setter
    def AlphaId(self, value: str):
        """The deployed alpha id. This is the id generated upon submission to the alpha marketplace"""
        ...

    @property
    def AlgorithmId(self) -> str:
        """The algorithm's unique deploy identifier"""
        ...

    @AlgorithmId.setter
    def AlgorithmId(self, value: str):
        """The algorithm's unique deploy identifier"""
        ...

    @property
    def Source(self) -> str:
        """The source of this data point, 'live trading' or in sample"""
        ...

    @Source.setter
    def Source(self, value: str):
        """The source of this data point, 'live trading' or in sample"""
        ...

    @property
    def OrderEvent(self) -> QuantConnect.Orders.OrderEvent:
        """The order event"""
        ...

    @OrderEvent.setter
    def OrderEvent(self, value: QuantConnect.Orders.OrderEvent):
        """The order event"""
        ...

    def Clone(self) -> QuantConnect.Data.BaseData:
        """Return a new instance clone of this object, used in fill forward"""
        ...

    def DataTimeZone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type
        
        :returns: The DateTimeZone of this data type.
        """
        ...

    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the Subscription Data Source
        
        :param config: Configuration object
        :param date: Date of this source file
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: Subscription Data Source.
        """
        ...

    def IsSparseData(self) -> bool:
        """Indicates that the data set is expected to be sparse"""
        ...

    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects.
        
        :param config: Subscription data config setup object
        :param line: Content of the source document
        :param date: Date of the requested data
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: New data point object.
        """
        ...


class PositionState(System.Object, QuantConnect.Securities.Positions.IPosition):
    """Snapshot of a position state"""

    @property
    def Symbol(self) -> QuantConnect.Symbol:
        """The symbol"""
        ...

    @Symbol.setter
    def Symbol(self, value: QuantConnect.Symbol):
        """The symbol"""
        ...

    @property
    def Quantity(self) -> float:
        """The quantity"""
        ...

    @Quantity.setter
    def Quantity(self, value: float):
        """The quantity"""
        ...

    @property
    def UnitQuantity(self) -> float:
        """
        The unit quantity. The unit quantities of a group define the group. For example, a covered
        call has 100 units of stock and -1 units of call contracts.
        """
        ...

    @UnitQuantity.setter
    def UnitQuantity(self, value: float):
        """
        The unit quantity. The unit quantities of a group define the group. For example, a covered
        call has 100 units of stock and -1 units of call contracts.
        """
        ...

    @staticmethod
    def Create(position: QuantConnect.Securities.Positions.IPosition) -> QuantConnect.Data.Custom.AlphaStreams.PositionState:
        """Creates a new instance"""
        ...


class PositionGroupState(System.Object):
    """Snapshot of a position group state"""

    @property
    def MarginUsed(self) -> float:
        """Currently margin used"""
        ...

    @MarginUsed.setter
    def MarginUsed(self, value: float):
        """Currently margin used"""
        ...

    @property
    def PortfolioValuePercentage(self) -> float:
        """The margin used by this position in relation to the total portfolio value"""
        ...

    @PortfolioValuePercentage.setter
    def PortfolioValuePercentage(self, value: float):
        """The margin used by this position in relation to the total portfolio value"""
        ...

    @property
    def Positions(self) -> System.Collections.Generic.List[QuantConnect.Data.Custom.AlphaStreams.PositionState]:
        """THe positions which compose this group"""
        ...

    @Positions.setter
    def Positions(self, value: System.Collections.Generic.List[QuantConnect.Data.Custom.AlphaStreams.PositionState]):
        """THe positions which compose this group"""
        ...


class AlphaStreamsPortfolioState(QuantConnect.Data.BaseData):
    """Snapshot of an algorithms portfolio state"""

    @property
    def AlphaId(self) -> str:
        """The deployed alpha id. This is the id generated upon submission to the alpha marketplace"""
        ...

    @AlphaId.setter
    def AlphaId(self, value: str):
        """The deployed alpha id. This is the id generated upon submission to the alpha marketplace"""
        ...

    @property
    def AlgorithmId(self) -> str:
        """The algorithm's unique deploy identifier"""
        ...

    @AlgorithmId.setter
    def AlgorithmId(self, value: str):
        """The algorithm's unique deploy identifier"""
        ...

    @property
    def Source(self) -> str:
        """The source of this data point, 'live trading' or in sample"""
        ...

    @Source.setter
    def Source(self, value: str):
        """The source of this data point, 'live trading' or in sample"""
        ...

    @property
    def Id(self) -> int:
        """Portfolio state id"""
        ...

    @Id.setter
    def Id(self, value: int):
        """Portfolio state id"""
        ...

    @property
    def AccountCurrency(self) -> str:
        """Algorithms account currency"""
        ...

    @AccountCurrency.setter
    def AccountCurrency(self, value: str):
        """Algorithms account currency"""
        ...

    @property
    def TotalPortfolioValue(self) -> float:
        """The current total portfolio value"""
        ...

    @TotalPortfolioValue.setter
    def TotalPortfolioValue(self, value: float):
        """The current total portfolio value"""
        ...

    @property
    def TotalMarginUsed(self) -> float:
        """The margin used"""
        ...

    @TotalMarginUsed.setter
    def TotalMarginUsed(self, value: float):
        """The margin used"""
        ...

    @property
    def PositionGroups(self) -> System.Collections.Generic.List[QuantConnect.Data.Custom.AlphaStreams.PositionGroupState]:
        """The different positions groups"""
        ...

    @PositionGroups.setter
    def PositionGroups(self, value: System.Collections.Generic.List[QuantConnect.Data.Custom.AlphaStreams.PositionGroupState]):
        """The different positions groups"""
        ...

    @property
    def CashBook(self) -> System.Collections.Generic.Dictionary[str, QuantConnect.Securities.Cash]:
        """Gets the cash book that keeps track of all currency holdings (only settled cash)"""
        ...

    @CashBook.setter
    def CashBook(self, value: System.Collections.Generic.Dictionary[str, QuantConnect.Securities.Cash]):
        """Gets the cash book that keeps track of all currency holdings (only settled cash)"""
        ...

    @property
    def UnsettledCashBook(self) -> System.Collections.Generic.Dictionary[str, QuantConnect.Securities.Cash]:
        """Gets the cash book that keeps track of all currency holdings (only unsettled cash)"""
        ...

    @UnsettledCashBook.setter
    def UnsettledCashBook(self, value: System.Collections.Generic.Dictionary[str, QuantConnect.Securities.Cash]):
        """Gets the cash book that keeps track of all currency holdings (only unsettled cash)"""
        ...

    def Clone(self) -> QuantConnect.Data.BaseData:
        """Return a new instance clone of this object, used in fill forward"""
        ...

    def DataTimeZone(self) -> typing.Any:
        """
        Specifies the data time zone for this data type
        
        :returns: The DateTimeZone of this data type.
        """
        ...

    def GetSource(self, config: QuantConnect.Data.SubscriptionDataConfig, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.SubscriptionDataSource:
        """
        Return the Subscription Data Source
        
        :param config: Configuration object
        :param date: Date of this source file
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: Subscription Data Source.
        """
        ...

    def IsSparseData(self) -> bool:
        """Indicates that the data set is expected to be sparse"""
        ...

    def Reader(self, config: QuantConnect.Data.SubscriptionDataConfig, line: str, date: typing.Union[datetime.datetime, datetime.date], isLiveMode: bool) -> QuantConnect.Data.BaseData:
        """
        Reader converts each line of the data source into BaseData objects.
        
        :param config: Subscription data config setup object
        :param line: Content of the source document
        :param date: Date of the requested data
        :param isLiveMode: true if we're in live mode, false for backtesting mode
        :returns: New data point object.
        """
        ...


