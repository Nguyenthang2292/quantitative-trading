from typing import overload
import datetime
import typing

import QuantConnect
import QuantConnect.Algorithm
import QuantConnect.Algorithm.Framework.Selection
import QuantConnect.Algorithm.Selection
import QuantConnect.Data
import QuantConnect.Data.UniverseSelection
import QuantConnect.Securities
import System.Collections.Generic
import System.Collections.Specialized


class OptionContractUniverse(QuantConnect.Data.UniverseSelection.UserDefinedUniverse):
    """This universe will hold single option contracts and their underlying, managing removals and additions"""

    def __init__(self, configuration: QuantConnect.Data.SubscriptionDataConfig, universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings) -> None:
        """
        Creates a new empty instance
        
        :param configuration: The universe configuration to use
        :param universeSettings: The universe settings to use
        """
        ...

    @staticmethod
    def CreateSymbol(market: str, securityType: QuantConnect.SecurityType) -> QuantConnect.Symbol:
        """
        Creates a user defined universe symbol
        
        :param market: The market
        :param securityType: The underlying option security type
        :returns: A symbol for user defined universe of the specified security type and market.
        """
        ...

    def OnCollectionChanged(self, args: System.Collections.Specialized.NotifyCollectionChangedEventArgs) -> None:
        """
        Event invocator for the UserDefinedUniverse.CollectionChanged event
        
        This method is protected.
        
        :param args: The notify collection changed event arguments
        """
        ...

    def SelectSymbols(self, utcTime: typing.Union[datetime.datetime, datetime.date], data: QuantConnect.Data.UniverseSelection.BaseDataCollection) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Returns the symbols defined by the user for this universe
        
        :param utcTime: The current utc time
        :param data: The symbols to remain in the universe
        :returns: The data that passes the filter.
        """
        ...


class OptionChainedUniverseSelectionModel(QuantConnect.Algorithm.Framework.Selection.UniverseSelectionModel):
    """
    This universe selection model will chain to the security changes of a given Universe selection
    output and create a new OptionChainUniverse for each of them
    """

    def __init__(self, universe: QuantConnect.Data.UniverseSelection.Universe, optionFilter: typing.Callable[[QuantConnect.Securities.OptionFilterUniverse], QuantConnect.Securities.OptionFilterUniverse], universeSettings: QuantConnect.Data.UniverseSelection.UniverseSettings = None) -> None:
        """
        Creates a new instance of OptionChainedUniverseSelectionModel
        
        :param universe: The universe we want to chain to
        :param optionFilter: The option filter universe to use
        :param universeSettings: Universe settings define attributes of created subscriptions, such as their resolution and the minimum time in universe before they can be removed
        """
        ...

    def CreateUniverses(self, algorithm: QuantConnect.Algorithm.QCAlgorithm) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.UniverseSelection.Universe]:
        """
        Creates the universes for this algorithm. Called once after IAlgorithm.Initialize
        
        :param algorithm: The algorithm instance to create universes for
        :returns: The universes to be used by the algorithm.
        """
        ...

    def GetNextRefreshTimeUtc(self) -> datetime.datetime:
        """Gets the next time the framework should invoke the `CreateUniverses` method to refresh the set of universes."""
        ...


