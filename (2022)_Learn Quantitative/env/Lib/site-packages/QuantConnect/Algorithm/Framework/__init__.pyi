from typing import overload
import abc
import typing

import QuantConnect
import QuantConnect.Algorithm
import QuantConnect.Algorithm.Framework
import QuantConnect.Algorithm.Framework.Portfolio
import QuantConnect.Data.UniverseSelection
import QuantConnect.Securities
import System
import System.Collections.Generic

QuantConnect_Algorithm_Framework_NotifiedSecurityChanges_UpdateCollection_TValue = typing.TypeVar("QuantConnect_Algorithm_Framework_NotifiedSecurityChanges_UpdateCollection_TValue")
QuantConnect_Algorithm_Framework_NotifiedSecurityChanges_UpdateDictionary_TValue = typing.TypeVar("QuantConnect_Algorithm_Framework_NotifiedSecurityChanges_UpdateDictionary_TValue")
QuantConnect_Algorithm_Framework_NotifiedSecurityChanges_UpdateDictionary_TKey = typing.TypeVar("QuantConnect_Algorithm_Framework_NotifiedSecurityChanges_UpdateDictionary_TKey")


class CustomWeightingAlphaStreamsPortfolioConstructionModel(QuantConnect.Algorithm.Framework.Portfolio.EqualWeightingAlphaStreamsPortfolioConstructionModel):
    """
    Custom weighting alpha streams portfolio construction model that will generate aggregated security targets taking into account all the alphas positions
    and a custom weighting factor for each alpha, which is also factored by the relation of the alphas portfolio value and the current algorithms portfolio value
    """

    def GetAlphaWeight(self, alphaId: str) -> float:
        """
        Get's the weight for an alpha
        
        :param alphaId: The algorithm instance that experienced the change in securities
        :returns: The alphas weight.
        """
        ...

    def SetAlphaWeights(self, alphaWeights: System.Collections.Generic.Dictionary[str, float]) -> None:
        """
        Specify a custom set of alpha portfolio weights to use
        
        :param alphaWeights: The alpha portfolio weights
        """
        ...


class NotifiedSecurityChanges(System.Object):
    """Provides convenience methods for updating collections in responses to securities changed events"""

    @staticmethod
    def Update(changes: QuantConnect.Data.UniverseSelection.SecurityChanges, add: typing.Callable[[QuantConnect.Securities.Security], None], remove: typing.Callable[[QuantConnect.Securities.Security], None]) -> None:
        """
        Invokes the provided  and  functions for each
        
        :param changes: The security changes to process
        :param add: Function called for each added security
        :param remove: Function called for each removed security
        """
        ...

    @staticmethod
    @overload
    def UpdateCollection(securities: System.Collections.Generic.ICollection[QuantConnect.Securities.Security], changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """
        Adds and removes the security changes to/from the collection
        
        :param securities: The securities collection to be updated with the changes
        :param changes: The changes to be applied to the securities collection
        """
        ...

    @staticmethod
    @overload
    def UpdateCollection(securities: System.Collections.Generic.ICollection[QuantConnect_Algorithm_Framework_NotifiedSecurityChanges_UpdateCollection_TValue], changes: QuantConnect.Data.UniverseSelection.SecurityChanges, valueFactory: typing.Callable[[QuantConnect.Securities.Security], QuantConnect_Algorithm_Framework_NotifiedSecurityChanges_UpdateCollection_TValue]) -> None:
        """
        Adds and removes the security changes to/from the collection
        
        :param securities: The securities collection to be updated with the changes
        :param changes: The changes to be applied to the securities collection
        :param valueFactory: Delegate used to create instances of TValue from a Security object
        """
        ...

    @staticmethod
    @overload
    def UpdateDictionary(dictionary: System.Collections.Generic.IDictionary[QuantConnect.Securities.Security, QuantConnect_Algorithm_Framework_NotifiedSecurityChanges_UpdateDictionary_TValue], changes: QuantConnect.Data.UniverseSelection.SecurityChanges, valueFactory: typing.Callable[[QuantConnect.Securities.Security], QuantConnect_Algorithm_Framework_NotifiedSecurityChanges_UpdateDictionary_TValue]) -> None:
        """
        Adds and removes the security changes to/from the collection
        
        :param dictionary: The securities collection to be updated with the changes
        :param changes: The changes to be applied to the securities collection
        :param valueFactory: Factory for creating dictonary values for a key
        """
        ...

    @staticmethod
    @overload
    def UpdateDictionary(dictionary: System.Collections.Generic.IDictionary[QuantConnect.Symbol, QuantConnect_Algorithm_Framework_NotifiedSecurityChanges_UpdateDictionary_TValue], changes: QuantConnect.Data.UniverseSelection.SecurityChanges, valueFactory: typing.Callable[[QuantConnect.Securities.Security], QuantConnect_Algorithm_Framework_NotifiedSecurityChanges_UpdateDictionary_TValue]) -> None:
        """
        Adds and removes the security changes to/from the collection
        
        :param dictionary: The securities collection to be updated with the changes
        :param changes: The changes to be applied to the securities collection
        :param valueFactory: Factory for creating dictonary values for a key
        """
        ...

    @staticmethod
    @overload
    def UpdateDictionary(dictionary: System.Collections.Generic.IDictionary[QuantConnect_Algorithm_Framework_NotifiedSecurityChanges_UpdateDictionary_TKey, QuantConnect_Algorithm_Framework_NotifiedSecurityChanges_UpdateDictionary_TValue], changes: QuantConnect.Data.UniverseSelection.SecurityChanges, keyFactory: typing.Callable[[QuantConnect.Securities.Security], QuantConnect_Algorithm_Framework_NotifiedSecurityChanges_UpdateDictionary_TKey], valueFactory: typing.Callable[[QuantConnect.Securities.Security], QuantConnect_Algorithm_Framework_NotifiedSecurityChanges_UpdateDictionary_TValue]) -> None:
        """
        Most generic form of UpdateCollection
        
        :param dictionary: The dictionary to update
        :param changes: The  to apply to the dictionary
        :param keyFactory: Selector pulling TKey from a
        :param valueFactory: Selector pulling TValue from a
        """
        ...


class INotifiedSecurityChanges(metaclass=abc.ABCMeta):
    """Types implementing this interface will be called when the algorithm's set of securities changes"""

    def OnSecuritiesChanged(self, algorithm: QuantConnect.Algorithm.QCAlgorithm, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """
        Event fired each time the we add/remove securities from the data feed
        
        :param algorithm: The algorithm instance that experienced the change in securities
        :param changes: The security additions and removals from the algorithm
        """
        ...


