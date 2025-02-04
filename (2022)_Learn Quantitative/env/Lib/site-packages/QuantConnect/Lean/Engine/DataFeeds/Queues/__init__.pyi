from typing import overload
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Interfaces
import QuantConnect.Lean.Engine.DataFeeds.Queues
import QuantConnect.Packets
import System
import System.Collections.Generic


class FakeDataQueue(System.Object, QuantConnect.Interfaces.IDataQueueHandler, QuantConnect.Interfaces.IDataQueueUniverseProvider):
    """This is an implementation of IDataQueueHandler used for testing. FakeHistoryProvider"""

    @property
    def TimeProvider(self) -> QuantConnect.ITimeProvider:
        """
        Continuous UTC time provider
        
        This property is protected.
        """
        ...

    @property
    def IsConnected(self) -> bool:
        """Returns whether the data provider is connected"""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the FakeDataQueue class to randomly emit data for each symbol"""
        ...

    @overload
    def __init__(self, dataAggregator: QuantConnect.Data.IDataAggregator) -> None:
        """Initializes a new instance of the FakeDataQueue class to randomly emit data for each symbol"""
        ...

    def CanPerformSelection(self) -> bool:
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def LookupSymbols(self, symbol: typing.Union[QuantConnect.Symbol, str], includeExpired: bool, securityCurrency: str = None) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Method returns a collection of Symbols that are available at the data source.
        
        :param symbol: Symbol to lookup
        :param includeExpired: Include expired contracts
        :param securityCurrency: Expected security currency(if any)
        :returns: Enumerable of Symbols, that are associated with the provided Symbol.
        """
        ...

    def SetJob(self, job: QuantConnect.Packets.LiveNodePacket) -> None:
        """
        Sets the job we're subscribing for
        
        :param job: Job we're subscribing for
        """
        ...

    def Subscribe(self, dataConfig: QuantConnect.Data.SubscriptionDataConfig, newDataAvailableHandler: typing.Callable[[System.Object, System.EventArgs], None]) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """
        Subscribe to the specified configuration
        
        :param dataConfig: defines the parameters to subscribe to a data feed
        :param newDataAvailableHandler: handler to be fired on new data available
        :returns: The new enumerator for this subscription request.
        """
        ...

    def Unsubscribe(self, dataConfig: QuantConnect.Data.SubscriptionDataConfig) -> None:
        """
        Removes the specified configuration
        
        :param dataConfig: Subscription config to be removed
        """
        ...


class LiveDataQueue(System.Object, QuantConnect.Interfaces.IDataQueueHandler):
    """Live Data Queue is the cut out implementation of how to bind a custom live data source"""

    @property
    def IsConnected(self) -> bool:
        """Returns whether the data provider is connected"""
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def SetJob(self, job: QuantConnect.Packets.LiveNodePacket) -> None:
        """
        Sets the job we're subscribing for
        
        :param job: Job we're subscribing for
        """
        ...

    def Subscribe(self, dataConfig: QuantConnect.Data.SubscriptionDataConfig, newDataAvailableHandler: typing.Callable[[System.Object, System.EventArgs], None]) -> System.Collections.Generic.IEnumerator[QuantConnect.Data.BaseData]:
        """Desktop/Local doesn't support live data from this handler"""
        ...

    def Unsubscribe(self, dataConfig: QuantConnect.Data.SubscriptionDataConfig) -> None:
        """Desktop/Local doesn't support live data from this handler"""
        ...


