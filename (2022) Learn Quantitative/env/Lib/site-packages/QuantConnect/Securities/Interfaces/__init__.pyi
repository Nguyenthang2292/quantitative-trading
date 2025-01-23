from typing import overload
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Securities
import QuantConnect.Securities.Interfaces
import System
import System.Collections.Generic


class ISecurityDataFilter(metaclass=abc.ABCMeta):
    """Security data filter interface. Defines pattern for the user defined data filter techniques."""

    def Filter(self, vehicle: QuantConnect.Securities.Security, data: QuantConnect.Data.BaseData) -> bool:
        """
        Filter out a tick from this security, with this new data:
        
        :param vehicle: Security of this filter.
        :param data: New data packet we're checking
        """
        ...


class AdjustmentType(System.Enum):
    """Enum defines types of possible price adjustments in continuous contract modeling."""

    ForwardAdjusted = 0

    BackAdjusted = 1


class IContinuousContractModel(metaclass=abc.ABCMeta):
    """
    Continuous contract model interface. Interfaces is implemented by different classes
    realizing various methods for modeling continuous security series. Primarily, modeling of continuous futures.
    Continuous contracts are used in backtesting of otherwise expiring derivative contracts.
    Continuous contracts are not traded, and are not products traded on exchanges.
    """

    @property
    @abc.abstractmethod
    def AdjustmentType(self) -> int:
        """
        Adjustment type, implemented by the model
        
        This property contains the int value of a member of the QuantConnect.Securities.Interfaces.AdjustmentType enum.
        """
        ...

    @AdjustmentType.setter
    @abc.abstractmethod
    def AdjustmentType(self, value: int):
        """
        Adjustment type, implemented by the model
        
        This property contains the int value of a member of the QuantConnect.Securities.Interfaces.AdjustmentType enum.
        """
        ...

    @property
    @abc.abstractmethod
    def InputSeries(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        List of current and historical data series for one root symbol.
        e.g. 6BH16, 6BM16, 6BU16, 6BZ16
        """
        ...

    @InputSeries.setter
    @abc.abstractmethod
    def InputSeries(self, value: System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]):
        """
        List of current and historical data series for one root symbol.
        e.g. 6BH16, 6BM16, 6BU16, 6BZ16
        """
        ...

    def GetContinuousData(self, dateTime: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Method returns continuous prices from the list of current and historical data series for one root symbol.
        It returns enumerator of stitched continuous quotes, produced by the model.
        e.g. 6BH15, 6BM15, 6BU15, 6BZ15 will result in one 6B continuous historical series for 2015
        
        :returns: Continuous prices.
        """
        ...

    def GetCurrentSymbol(self, dateTime: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Symbol:
        """
        Returns current symbol name that corresponds to the current continuous model,
        or null if none.
        
        :returns: Current symbol name.
        """
        ...

    def GetRollDates(self) -> System.Collections.Generic.IEnumerator[datetime.datetime]:
        """
        Returns the list of roll dates for the contract.
        
        :returns: The list of roll dates.
        """
        ...


