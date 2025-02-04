from typing import overload
import abc
import typing

import QuantConnect
import QuantConnect.Orders
import QuantConnect.Securities
import QuantConnect.Securities.Option.StrategyMatcher
import QuantConnect.Securities.Positions
import System
import System.Collections
import System.Collections.Generic
import System.Collections.Immutable

QuantConnect_Securities_Positions_PositionGroupKey = typing.Any
QuantConnect_Securities_Positions_IPositionGroupBuyingPowerModel = typing.Any


class ReservedBuyingPowerForPositionGroup(System.Object):
    """Defines the result for IBuyingPowerModel.GetReservedBuyingPowerForPosition"""

    @property
    def AbsoluteUsedBuyingPower(self) -> float:
        """Gets the reserved buying power"""
        ...

    def __init__(self, reservedBuyingPowerForPosition: float) -> None:
        """
        Initializes a new instance of the ReservedBuyingPowerForPosition class
        
        :param reservedBuyingPowerForPosition: The reserved buying power for the security's holdings
        """
        ...


class GetMaximumLotsResult(System.Object):
    """
    Result type for IPositionGroupBuyingPowerModel.GetMaximumLotsForDeltaBuyingPower
    and IPositionGroupBuyingPowerModel.GetMaximumLotsForTargetBuyingPower
    """

    @property
    def NumberOfLots(self) -> float:
        """
        Returns the maximum number of lots of the position group that can be
        ordered. This is a whole number and is the IPositionGroup.Quantity
        """
        ...

    @property
    def Reason(self) -> str:
        """Returns the reason for which the maximum order quantity is zero"""
        ...

    @property
    def IsError(self) -> bool:
        """Returns true if the zero order quantity is an error condition and will be shown to the user."""
        ...

    @overload
    def __init__(self, numberOfLots: float, reason: str = None) -> None:
        """
        Initializes a new instance of the GetMaximumOrderQuantityResult class
        
        :param numberOfLots: Returns the maximum number of lots of the position group that can be ordered
        :param reason: The reason for which the maximum order quantity is zero
        """
        ...

    @overload
    def __init__(self, numberOfLots: float, reason: str, isError: bool = True) -> None:
        """
        Initializes a new instance of the GetMaximumOrderQuantityResult class
        
        :param numberOfLots: Returns the maximum number of lots of the position group that can be ordered
        :param reason: The reason for which the maximum order quantity is zero
        :param isError: True if the zero order quantity is an error condition
        """
        ...


class PositionGroupBuyingPower(System.Object):
    """Defines the result for IPositionGroupBuyingPowerModel.GetPositionGroupBuyingPower"""

    @property
    def Value(self) -> float:
        """Gets the buying power"""
        ...

    def __init__(self, buyingPower: float) -> None:
        """
        Initializes a new instance of the PositionGroupBuyingPower class
        
        :param buyingPower: The buying power
        """
        ...


class IPositionGroupBuyingPowerModel(System.IEquatable[QuantConnect_Securities_Positions_IPositionGroupBuyingPowerModel], metaclass=abc.ABCMeta):
    """Represents a position group's model of buying power"""

    def GetInitialMarginRequiredForOrder(self, parameters: QuantConnect.Securities.Positions.PositionGroupInitialMarginForOrderParameters) -> QuantConnect.Securities.InitialMargin:
        """
        Gets the total margin required to execute the specified order in units of the account currency including fees
        
        :param parameters: An object containing the portfolio, the security and the order
        :returns: The total margin in terms of the currency quoted in the order.
        """
        ...

    def GetInitialMarginRequirement(self, parameters: QuantConnect.Securities.Positions.PositionGroupInitialMarginParameters) -> QuantConnect.Securities.InitialMargin:
        """
        The margin that must be held in order to increase the position by the provided quantity
        
        :param parameters: An object containing the security and quantity
        """
        ...

    def GetMaintenanceMargin(self, parameters: QuantConnect.Securities.Positions.PositionGroupMaintenanceMarginParameters) -> QuantConnect.Securities.MaintenanceMargin:
        """
        Gets the margin currently allocated to the specified holding
        
        :param parameters: An object containing the security
        :returns: The maintenance margin required for the.
        """
        ...

    def GetMaximumLotsForDeltaBuyingPower(self, parameters: QuantConnect.Securities.Positions.GetMaximumLotsForDeltaBuyingPowerParameters) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """
        Get the maximum market position group order quantity to obtain a delta in the buying power used by a position group.
        The deltas sign defines the position side to apply it to, positive long, negative short.
        
        :param parameters: An object containing the portfolio, the position group and the delta buying power
        :returns: Returns the maximum allowed market order quantity and if zero, also the reason.
        """
        ...

    def GetMaximumLotsForTargetBuyingPower(self, parameters: QuantConnect.Securities.Positions.GetMaximumLotsForTargetBuyingPowerParameters) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """
        Get the maximum position group order quantity to obtain a position with a given buying power
        percentage. Will not take into account free buying power.
        
        :param parameters: An object containing the portfolio, the position group and the target     signed buying power percentage
        :returns: Returns the maximum allowed market order quantity and if zero, also the reason.
        """
        ...

    def GetPositionGroupBuyingPower(self, parameters: QuantConnect.Securities.Positions.PositionGroupBuyingPowerParameters) -> QuantConnect.Securities.Positions.PositionGroupBuyingPower:
        """
        Gets the buying power available for a position group trade
        
        :param parameters: A parameters object containing the algorithm's portfolio, security, and order direction
        :returns: The buying power available for the trade.
        """
        ...

    def GetReservedBuyingPowerForPositionGroup(self, parameters: QuantConnect.Securities.Positions.ReservedBuyingPowerForPositionGroupParameters) -> QuantConnect.Securities.Positions.ReservedBuyingPowerForPositionGroup:
        """Computes the amount of buying power reserved by the provided position group"""
        ...

    def GetReservedBuyingPowerImpact(self, parameters: QuantConnect.Securities.Positions.ReservedBuyingPowerImpactParameters) -> QuantConnect.Securities.Positions.ReservedBuyingPowerImpact:
        """
        Computes the impact on the portfolio's buying power from adding the position group to the portfolio. This is
        a 'what if' analysis to determine what the state of the portfolio would be if these changes were applied. The
        delta (before - after) is the margin requirement for adding the positions and if the margin used after the changes
        are applied is less than the total portfolio value, this indicates sufficient capital.
        
        :param parameters: An object containing the portfolio and a position group containing the contemplated changes to the portfolio
        :returns: Returns the portfolio's total portfolio value and margin used before and after the position changes are applied.
        """
        ...

    def HasSufficientBuyingPowerForOrder(self, parameters: QuantConnect.Securities.Positions.HasSufficientPositionGroupBuyingPowerForOrderParameters) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """
        Check if there is sufficient buying power for the position group to execute this order.
        
        :param parameters: An object containing the portfolio, the position group and the order
        :returns: Returns buying power information for an order against a position group.
        """
        ...


class IPosition(metaclass=abc.ABCMeta):
    """Defines a position for inclusion in a group"""

    @property
    @abc.abstractmethod
    def Symbol(self) -> QuantConnect.Symbol:
        """The symbol"""
        ...

    @property
    @abc.abstractmethod
    def Quantity(self) -> float:
        """The quantity"""
        ...

    @property
    @abc.abstractmethod
    def UnitQuantity(self) -> float:
        """
        The unit quantity. The unit quantities of a group define the group. For example, a covered
        call has 100 units of stock and -1 units of call contracts.
        """
        ...


class IPositionGroup(System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition], metaclass=abc.ABCMeta):
    """Defines a group of positions allowing for more efficient use of portfolio margin"""

    @property
    @abc.abstractmethod
    def Key(self) -> QuantConnect.Securities.Positions.PositionGroupKey:
        """Gets the key identifying this group"""
        ...

    @property
    @abc.abstractmethod
    def Quantity(self) -> float:
        """Gets the whole number of units in this position group"""
        ...

    @property
    @abc.abstractmethod
    def Positions(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPosition]:
        """Gets the positions in this group"""
        ...

    @property
    @abc.abstractmethod
    def BuyingPowerModel(self) -> QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel:
        """Gets the buying power model defining how margin works in this group"""
        ...

    def TryGetPosition(self, symbol: typing.Union[QuantConnect.Symbol, str], position: typing.Optional[QuantConnect.Securities.Positions.IPosition]) -> typing.Union[bool, QuantConnect.Securities.Positions.IPosition]:
        """
        Attempts to retrieve the position with the specified symbol
        
        :param symbol: The symbol
        :param position: The position, if found
        :returns: True if the position was found, otherwise false.
        """
        ...


class PositionGroupKey(System.Object, System.IEquatable[QuantConnect_Securities_Positions_PositionGroupKey]):
    """Defines a unique and deterministic key for IPositionGroup"""

    @property
    def IsDefaultGroup(self) -> bool:
        """Gets whether or not this key defines a default group"""
        ...

    @property
    def BuyingPowerModel(self) -> QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel:
        """Gets the IPositionGroupBuyingPowerModel being used by the group"""
        ...

    @property
    def UnitQuantities(self) -> System.Collections.Generic.IReadOnlyList[System.Tuple[QuantConnect.Symbol, float]]:
        """Gets the unit quantities defining the ratio between position quantities in the group"""
        ...

    @overload
    def __init__(self, buyingPowerModel: QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel, security: QuantConnect.Securities.Security) -> None:
        """
        Initializes a new instance of the PositionGroupKey class for groups with a single security
        
        :param buyingPowerModel: The group's buying power model
        :param security: The security
        """
        ...

    @overload
    def __init__(self, buyingPowerModel: QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel, positions: System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPosition]) -> None:
        """
        Initializes a new instance of the PositionGroupKey class
        
        :param buyingPowerModel: The group's buying power model
        :param positions: The positions comprising the group
        """
        ...

    def CreateEmptyPositions(self) -> typing.List[QuantConnect.Securities.Positions.IPosition]:
        """Creates a new array of empty positions with unit quantities according to this key"""
        ...

    def CreateUnitGroup(self) -> QuantConnect.Securities.Positions.IPositionGroup:
        """
        Creates a new IPositionGroup with each position's quantity equaling it's unit quantity
        
        :returns: A new position group with quantity equal to 1.
        """
        ...

    def CreateUnitPositions(self) -> typing.List[QuantConnect.Securities.Positions.IPosition]:
        """Creates a new array of positions with each position quantity equaling its unit quantity"""
        ...

    @overload
    def Equals(self, other: QuantConnect.Securities.Positions.PositionGroupKey) -> bool:
        """
        Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the  parameter; otherwise, false.
        """
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified object is equal to the current object.
        
        :param obj: The object to compare with the current object.
        :returns: true if the specified object  is equal to the current object; otherwise, false.
        """
        ...

    def GetHashCode(self) -> int:
        """
        Serves as the default hash function.
        
        :returns: A hash code for the current object.
        """
        ...

    def ToString(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class PositionGroupCollection(System.Object, System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPositionGroup], typing.Iterable[QuantConnect.Securities.Positions.IPositionGroup]):
    """Provides a collection type for IPositionGroup"""

    Empty: QuantConnect.Securities.Positions.PositionGroupCollection
    """Gets an empty instance of the PositionGroupCollection class"""

    @property
    def Count(self) -> int:
        """Gets the number of positions in this group"""
        ...

    @property
    def IsOnlyDefaultGroups(self) -> bool:
        """Gets whether or not this collection contains only default position groups"""
        ...

    def __getitem__(self, key: QuantConnect.Securities.Positions.PositionGroupKey) -> QuantConnect.Securities.Positions.IPositionGroup:
        """
        Gets the IPositionGroup matching the specified key. If one does not exist, then an empty
        group is returned matching the unit quantities defined in the
        
        :param key: The position group key to search for
        :returns: The position group matching the specified key, or a new empty group if no matching group is found.
        """
        ...

    @overload
    def __init__(self, groups: System.Collections.Immutable.ImmutableDictionary[QuantConnect.Securities.Positions.PositionGroupKey, QuantConnect.Securities.Positions.IPositionGroup], groupsBySymbol: System.Collections.Immutable.ImmutableDictionary[QuantConnect.Symbol, System.Collections.Immutable.ImmutableHashSet[QuantConnect.Securities.Positions.IPositionGroup]]) -> None:
        """
        Initializes a new instance of the PositionGroupCollection class
        
        :param groups: The position groups keyed by their group key
        :param groupsBySymbol: The position groups keyed by the symbol of each position
        """
        ...

    @overload
    def __init__(self, groups: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPositionGroup]) -> None:
        """
        Initializes a new instance of the PositionGroupCollection class
        
        :param groups: The position groups
        """
        ...

    def Add(self, group: QuantConnect.Securities.Positions.IPositionGroup) -> QuantConnect.Securities.Positions.PositionGroupCollection:
        """
        Creates a new PositionGroupCollection that contains all of the position groups
        in this collection in addition to the specified . If a group with the
        same key already exists then it is overwritten.
        """
        ...

    def CombineWith(self, other: QuantConnect.Securities.Positions.PositionGroupCollection) -> QuantConnect.Securities.Positions.PositionGroupCollection:
        """Merges this position group collection with the provided  collection."""
        ...

    def Contains(self, key: QuantConnect.Securities.Positions.PositionGroupKey) -> bool:
        """
        Determines whether or not a group with the specified key exists in this collection
        
        :param key: The group key to search for
        :returns: True if a group with the specified key was found, false otherwise.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Securities.Positions.IPositionGroup]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: An enumerator that can be used to iterate through the collection.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        """
        Returns an enumerator that iterates through a collection.
        
        :returns: An System.Collections.IEnumerator object that can be used to iterate through the collection.
        """
        ...

    def TryGetGroup(self, key: QuantConnect.Securities.Positions.PositionGroupKey, group: typing.Optional[QuantConnect.Securities.Positions.IPositionGroup]) -> typing.Union[bool, QuantConnect.Securities.Positions.IPositionGroup]:
        """
        Attempts to retrieve the group with the specified key
        
        :param key: The group key to search for
        :param group: The position group
        :returns: True if group with key found, otherwise false.
        """
        ...

    def TryGetGroups(self, symbol: typing.Union[QuantConnect.Symbol, str], groups: typing.Optional[System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPositionGroup]]) -> typing.Union[bool, System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPositionGroup]]:
        """
        Attempts to retrieve all groups that contain the provided symbol
        
        :param symbol: The symbol
        :param groups: The groups if any were found, otherwise null
        :returns: True if groups were found for the specified symbol, otherwise false.
        """
        ...


class PositionGroupMaintenanceMarginParameters(System.Object):
    """Defines parameters for IPositionGroupBuyingPowerModel.GetMaintenanceMargin"""

    @property
    def Portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """Gets the algorithm's portfolio manager"""
        ...

    @property
    def PositionGroup(self) -> QuantConnect.Securities.Positions.IPositionGroup:
        """Gets the position group"""
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, positionGroup: QuantConnect.Securities.Positions.IPositionGroup) -> None:
        """
        Initializes a new instance of the PositionGroupMaintenanceMarginParameters class
        
        :param portfolio: The algorithm's portfolio manager
        :param positionGroup: The position group
        """
        ...


class PositionGroupInitialMarginParameters(System.Object):
    """Defines parameters for IPositionGroupBuyingPowerModel.GetInitialMarginRequirement"""

    @property
    def Portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """Gets the algorithm's portfolio manager"""
        ...

    @property
    def PositionGroup(self) -> QuantConnect.Securities.Positions.IPositionGroup:
        """Gets the position group"""
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, positionGroup: QuantConnect.Securities.Positions.IPositionGroup) -> None:
        """
        Initializes a new instance of the PositionGroupInitialMarginParameters class
        
        :param portfolio: The algorithm's portfolio manager
        :param positionGroup: The position group
        """
        ...


class PositionGroupInitialMarginForOrderParameters(System.Object):
    """Defines parameters for IPositionGroupBuyingPowerModel.GetInitialMarginRequiredForOrder"""

    @property
    def Portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """Gets the algorithm's portfolio manager"""
        ...

    @property
    def PositionGroup(self) -> QuantConnect.Securities.Positions.IPositionGroup:
        """Gets the position group"""
        ...

    @property
    def Order(self) -> QuantConnect.Orders.Order:
        """Gets the order"""
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, positionGroup: QuantConnect.Securities.Positions.IPositionGroup, order: QuantConnect.Orders.Order) -> None:
        """
        Initializes a new instance of the PositionGroupInitialMarginForOrderParameters class
        
        :param portfolio: The algorithm's portfolio manager
        :param positionGroup: The position group
        :param order: The order
        """
        ...


class ReservedBuyingPowerImpact(System.Object):
    """
    Specifies the impact on buying power from changing security holdings that affects current IPositionGroup,
    including the current reserved buying power, without the change, and a contemplate reserved buying power, which takes
    into account a contemplated change to the algorithm's positions that impacts current position groups.
    """

    @property
    def Current(self) -> float:
        """Gets the current reserved buying power for the impacted groups"""
        ...

    @property
    def Contemplated(self) -> float:
        """Gets the reserved buying power for groups resolved after applying a contemplated change to the impacted groups"""
        ...

    @property
    def Delta(self) -> float:
        """Gets the change in reserved buying power, Current minus Contemplated"""
        ...

    @property
    def ImpactedGroups(self) -> System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPositionGroup]:
        """Gets the impacted groups used as the basis for these reserved buying power numbers"""
        ...

    @property
    def ContemplatedChanges(self) -> System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition]:
        """Gets the position changes being contemplated"""
        ...

    @property
    def ContemplatedGroups(self) -> System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPositionGroup]:
        """Gets the newly resolved groups resulting from applying the contemplated changes to the impacted groups"""
        ...

    def __init__(self, current: float, contemplated: float, impactedGroups: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPositionGroup], contemplatedChanges: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition], contemplatedGroups: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPositionGroup]) -> None:
        """
        Initializes a new instance of the ReservedBuyingPowerImpact class
        
        :param current: The current reserved buying power for impacted groups
        :param contemplated: The reserved buying power for impacted groups after applying the contemplated changes
        :param impactedGroups: The groups impacted by the contemplated changes
        :param contemplatedChanges: The position changes being contemplated
        :param contemplatedGroups: The groups resulting from applying the contemplated changes
        """
        ...


class ReservedBuyingPowerImpactParameters(System.Object):
    """Parameters for the IPositionGroupBuyingPowerModel.GetReservedBuyingPowerImpact"""

    @property
    def ContemplatedChanges(self) -> QuantConnect.Securities.Positions.IPositionGroup:
        """Gets the position changes being contemplated"""
        ...

    @property
    def Portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """Gets the algorithm's portfolio manager"""
        ...

    @property
    def Order(self) -> QuantConnect.Orders.Order:
        """The order associated with this request"""
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, contemplatedChanges: QuantConnect.Securities.Positions.IPositionGroup, order: QuantConnect.Orders.Order) -> None:
        """
        Initializes a new instance of the ReservedBuyingPowerImpactParameters class
        
        :param portfolio: The algorithm's portfolio manager
        :param contemplatedChanges: The position changes being contemplated
        :param order: The order associated with this request
        """
        ...


class HasSufficientPositionGroupBuyingPowerForOrderParameters(System.Object):
    """Defines the parameters for IPositionGroupBuyingPowerModel.HasSufficientBuyingPowerForOrder"""

    @property
    def Order(self) -> QuantConnect.Orders.Order:
        """Gets the order"""
        ...

    @property
    def PositionGroup(self) -> QuantConnect.Securities.Positions.IPositionGroup:
        """Gets the position group representing the holdings changes contemplated by the order"""
        ...

    @property
    def Portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """Gets the algorithm's portfolio manager"""
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, positionGroup: QuantConnect.Securities.Positions.IPositionGroup, order: QuantConnect.Orders.Order) -> None:
        """
        Initializes a new instance of the HasSufficientPositionGroupBuyingPowerForOrderParameters class
        
        :param portfolio: The algorithm's portfolio manager
        :param positionGroup: The position group
        :param order: The order
        """
        ...

    def Error(self, reason: str) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """Creates a new result indicating that there was an error"""
        ...

    def Insufficient(self, reason: str) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """Creates a new result indicating that there is insufficient buying power for the contemplated order"""
        ...

    def Sufficient(self) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """Creates a new result indicating that there is sufficient buying power for the contemplated order"""
        ...


class ReservedBuyingPowerForPositionGroupParameters(System.Object):
    """Defines the parameters for IBuyingPowerModel.GetReservedBuyingPowerForPosition"""

    @property
    def PositionGroup(self) -> QuantConnect.Securities.Positions.IPositionGroup:
        """Gets the IPositionGroup"""
        ...

    @property
    def Portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """Gets the algorithm's portfolio manager"""
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, positionGroup: QuantConnect.Securities.Positions.IPositionGroup) -> None:
        """
        Initializes a new instance of the ReservedBuyingPowerForPositionGroupParameters class
        
        :param portfolio: The algorithm's portfolio manager
        :param positionGroup: The position group
        """
        ...


class GetMaximumLotsForTargetBuyingPowerParameters(System.Object):
    """Defines the parameters for IPositionGroupBuyingPowerModel.GetMaximumLotsForTargetBuyingPower"""

    @property
    def Portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """Gets the algorithm's portfolio manager"""
        ...

    @property
    def PositionGroup(self) -> QuantConnect.Securities.Positions.IPositionGroup:
        """Gets the position group"""
        ...

    @property
    def TargetBuyingPower(self) -> float:
        """The target buying power."""
        ...

    @property
    def SilenceNonErrorReasons(self) -> bool:
        """
        True enables the IBuyingPowerModel to skip setting GetMaximumLotsResult.Reason
        for non error situations, for performance
        """
        ...

    @property
    def MinimumOrderMarginPortfolioPercentage(self) -> float:
        """Configurable minimum order margin portfolio percentage to ignore bad orders, orders with unrealistic small sizes"""
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, positionGroup: QuantConnect.Securities.Positions.IPositionGroup, targetBuyingPower: float, minimumOrderMarginPortfolioPercentage: float, silenceNonErrorReasons: bool = False) -> None:
        """
        Initializes a new instance of the GetMaximumLotsForTargetBuyingPowerParameters class
        
        :param portfolio: The algorithm's portfolio manager
        :param positionGroup: The position group
        :param targetBuyingPower: The target buying power
        :param minimumOrderMarginPortfolioPercentage: Configurable minimum order margin portfolio percentage to ignore orders with unrealistic small sizes
        :param silenceNonErrorReasons: True will not return GetMaximumLotsResult.Reason set for non error situation, this is for performance
        """
        ...

    def Error(self, reason: str) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """Creates a new GetMaximumLotsResult with zero quantity and an error message."""
        ...

    def Result(self, quantity: float) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """Creates a new GetMaximumLotsResult for the specified quantity and no message."""
        ...

    @overload
    def Zero(self) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """Creates a new GetMaximumLotsResult with zero quantity and no message."""
        ...

    @overload
    def Zero(self, reason: str) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """Creates a new GetMaximumLotsResult with zero quantity and an info message."""
        ...


class GetMaximumLotsForDeltaBuyingPowerParameters(System.Object):
    """Defines the parameters for IPositionGroupBuyingPowerModel.GetMaximumLotsForDeltaBuyingPower"""

    @property
    def Portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """Gets the algorithm's portfolio manager"""
        ...

    @property
    def PositionGroup(self) -> QuantConnect.Securities.Positions.IPositionGroup:
        """Gets the position group"""
        ...

    @property
    def DeltaBuyingPower(self) -> float:
        """The delta buying power."""
        ...

    @property
    def SilenceNonErrorReasons(self) -> bool:
        """
        True enables the IBuyingPowerModel to skip setting GetMaximumLotsResult.Reason
        for non error situations, for performance
        """
        ...

    @property
    def MinimumOrderMarginPortfolioPercentage(self) -> float:
        """Configurable minimum order margin portfolio percentage to ignore bad orders, orders with unrealistic small sizes"""
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, positionGroup: QuantConnect.Securities.Positions.IPositionGroup, deltaBuyingPower: float, minimumOrderMarginPortfolioPercentage: float, silenceNonErrorReasons: bool = False) -> None:
        """
        Initializes a new instance of the GetMaximumLotsForDeltaBuyingPowerParameters class
        
        :param portfolio: The algorithm's portfolio manager
        :param positionGroup: The position group
        :param deltaBuyingPower: The delta buying power to apply. Sign defines the position side to apply the delta
        :param minimumOrderMarginPortfolioPercentage: Configurable minimum order margin portfolio percentage to ignore orders with unrealistic small sizes
        :param silenceNonErrorReasons: True will not return GetMaximumLotsResult.Reason set for non error situation, this is for performance
        """
        ...

    def Error(self, reason: str) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """Creates a new GetMaximumLotsResult with zero quantity and an error message."""
        ...

    def Result(self, quantity: float) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """Creates a new GetMaximumLotsResult for the specified quantity and no message."""
        ...

    @overload
    def Zero(self) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """Creates a new GetMaximumLotsResult with zero quantity and no message."""
        ...

    @overload
    def Zero(self, reason: str) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """Creates a new GetMaximumLotsResult with zero quantity and an info message."""
        ...


class PositionGroupBuyingPowerParameters(System.Object):
    """Defines the parameters for IPositionGroupBuyingPowerModel.GetPositionGroupBuyingPower"""

    @property
    def PositionGroup(self) -> QuantConnect.Securities.Positions.IPositionGroup:
        """Gets the position group"""
        ...

    @property
    def Portfolio(self) -> QuantConnect.Securities.SecurityPortfolioManager:
        """Gets the algorithm's portfolio manager"""
        ...

    @property
    def Direction(self) -> int:
        """
        Gets the direction in which buying power is to be computed
        
        This property contains the int value of a member of the QuantConnect.Orders.OrderDirection enum.
        """
        ...

    def __init__(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, positionGroup: QuantConnect.Securities.Positions.IPositionGroup, direction: QuantConnect.Orders.OrderDirection) -> None:
        """
        Initializes a new instance of the PositionGroupBuyingPowerParameters class
        
        :param portfolio: The algorithm's portfolio manager
        :param positionGroup: The position group
        :param direction: The direction to compute buying power in
        """
        ...


class PositionGroupBuyingPowerModel(System.Object, QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel, metaclass=abc.ABCMeta):
    """Provides a base class for implementations of IPositionGroupBuyingPowerModel"""

    @property
    def RequiredFreeBuyingPowerPercent(self) -> float:
        """
        Gets the percentage of portfolio buying power to leave as a buffer
        
        This property is protected.
        """
        ...

    def __init__(self, requiredFreeBuyingPowerPercent: float = 0) -> None:
        """
        Initializes a new instance of the PositionGroupBuyingPowerModel class
        
        This method is protected.
        
        :param requiredFreeBuyingPowerPercent: The percentage of portfolio buying power to leave as a buffer
        """
        ...

    @overload
    def Equals(self, other: QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel) -> bool:
        """
        Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the  parameter; otherwise, false.
        """
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified object is equal to the current object.
        
        :param obj: The object to compare with the current object.
        :returns: true if the specified object  is equal to the current object; otherwise, false.
        """
        ...

    def GetHashCode(self) -> int:
        """
        Serves as the default hash function.
        
        :returns: A hash code for the current object.
        """
        ...

    def GetInitialMarginRequiredForOrder(self, parameters: QuantConnect.Securities.Positions.PositionGroupInitialMarginForOrderParameters) -> QuantConnect.Securities.InitialMargin:
        """
        Gets the total margin required to execute the specified order in units of the account currency including fees
        
        :param parameters: An object containing the portfolio, the security and the order
        :returns: The total margin in terms of the currency quoted in the order.
        """
        ...

    def GetInitialMarginRequirement(self, parameters: QuantConnect.Securities.Positions.PositionGroupInitialMarginParameters) -> QuantConnect.Securities.InitialMargin:
        """
        The margin that must be held in order to increase the position by the provided quantity
        
        :param parameters: An object containing the security and quantity
        """
        ...

    def GetMaintenanceMargin(self, parameters: QuantConnect.Securities.Positions.PositionGroupMaintenanceMarginParameters) -> QuantConnect.Securities.MaintenanceMargin:
        """
        Gets the margin currently allocated to the specified holding
        
        :param parameters: An object containing the security
        :returns: The maintenance margin required for the.
        """
        ...

    def GetMaximumLotsForDeltaBuyingPower(self, parameters: QuantConnect.Securities.Positions.GetMaximumLotsForDeltaBuyingPowerParameters) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """
        Get the maximum market position group order quantity to obtain a delta in the buying power used by a position group.
        The deltas sign defines the position side to apply it to, positive long, negative short.
        
        :param parameters: An object containing the portfolio, the position group and the delta buying power
        :returns: Returns the maximum allowed market order quantity and if zero, also the reason.
        """
        ...

    def GetMaximumLotsForTargetBuyingPower(self, parameters: QuantConnect.Securities.Positions.GetMaximumLotsForTargetBuyingPowerParameters) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """
        Get the maximum position group order quantity to obtain a position with a given buying power
        percentage. Will not take into account free buying power.
        
        :param parameters: An object containing the portfolio, the position group and the target     signed buying power percentage
        :returns: Returns the maximum allowed market order quantity and if zero, also the reason.
        """
        ...

    def GetOrderFeeInAccountCurrency(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, positionGroup: QuantConnect.Securities.Positions.IPositionGroup) -> float:
        """
        Helper function to compute the order fees associated with executing market orders for the specified
        
        This method is protected.
        """
        ...

    def GetPositionGroupBuyingPower(self, parameters: QuantConnect.Securities.Positions.PositionGroupBuyingPowerParameters) -> QuantConnect.Securities.Positions.PositionGroupBuyingPower:
        """
        Gets the buying power available for a position group trade
        
        :param parameters: A parameters object containing the algorithm's portfolio, security, and order direction
        :returns: The buying power available for the trade.
        """
        ...

    def GetReservedBuyingPowerForPositionGroup(self, parameters: QuantConnect.Securities.Positions.ReservedBuyingPowerForPositionGroupParameters) -> QuantConnect.Securities.Positions.ReservedBuyingPowerForPositionGroup:
        """Computes the amount of buying power reserved by the provided position group"""
        ...

    def GetReservedBuyingPowerImpact(self, parameters: QuantConnect.Securities.Positions.ReservedBuyingPowerImpactParameters) -> QuantConnect.Securities.Positions.ReservedBuyingPowerImpact:
        """
        Computes the impact on the portfolio's buying power from adding the position group to the portfolio. This is
        a 'what if' analysis to determine what the state of the portfolio would be if these changes were applied. The
        delta (before - after) is the margin requirement for adding the positions and if the margin used after the changes
        are applied is less than the total portfolio value, this indicates sufficient capital.
        
        :param parameters: An object containing the portfolio and a position group containing the contemplated changes to the portfolio
        :returns: Returns the portfolio's total portfolio value and margin used before and after the position changes are applied.
        """
        ...

    def HasSufficientBuyingPowerForOrder(self, parameters: QuantConnect.Securities.Positions.HasSufficientPositionGroupBuyingPowerForOrderParameters) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """
        Check if there is sufficient buying power for the position group to execute this order.
        
        :param parameters: An object containing the portfolio, the position group and the order
        :returns: Returns buying power information for an order against a position group.
        """
        ...

    def PassesPositionGroupSpecificBuyingPowerForOrderChecks(self, parameters: QuantConnect.Securities.Positions.HasSufficientPositionGroupBuyingPowerForOrderParameters, availableBuyingPower: float) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """
        Provides a mechanism for derived types to add their own buying power for order checks without needing to
        recompute the available buying power. Implementations should return null if all checks pass and should
        return an instance of HasSufficientBuyingPowerForOrderResult with IsSufficient=false if it
        fails.
        
        This method is protected.
        """
        ...

    def ToAccountCurrency(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, cash: QuantConnect.Securities.CashAmount) -> float:
        """
        Helper function to convert a CashAmount to the account currency
        
        This method is protected.
        """
        ...

    @staticmethod
    def UnableToConverge(lastOrderQuantity: float, positionGroupQuantity: float, groupUnit: QuantConnect.Securities.Positions.IPositionGroup, portfolio: QuantConnect.Securities.SecurityPortfolioManager, target: float, orderMargin: float, absUnitMargin: float, orderFees: float, error: typing.Optional[System.ArgumentException]) -> typing.Union[bool, System.ArgumentException]:
        """
        Checks if  equals  indicating we got the same result on this iteration
        meaning we're unable to converge through iteration. This function was split out to support derived types using the same error message as well
        as removing the added noise of the check and message creation.
        
        This method is protected.
        """
        ...


class SecurityPositionGroupBuyingPowerModel(QuantConnect.Securities.Positions.PositionGroupBuyingPowerModel):
    """Provides an implementation of IPositionGroupBuyingPowerModel for groups containing exactly one security"""

    def GetInitialMarginRequiredForOrder(self, parameters: QuantConnect.Securities.Positions.PositionGroupInitialMarginForOrderParameters) -> QuantConnect.Securities.InitialMargin:
        """
        Gets the total margin required to execute the specified order in units of the account currency including fees
        
        :param parameters: An object containing the portfolio, the security and the order
        :returns: The total margin in terms of the currency quoted in the order.
        """
        ...

    def GetInitialMarginRequirement(self, parameters: QuantConnect.Securities.Positions.PositionGroupInitialMarginParameters) -> QuantConnect.Securities.InitialMargin:
        """
        The margin that must be held in order to increase the position by the provided quantity
        
        :param parameters: An object containing the security and quantity
        """
        ...

    def GetMaintenanceMargin(self, parameters: QuantConnect.Securities.Positions.PositionGroupMaintenanceMarginParameters) -> QuantConnect.Securities.MaintenanceMargin:
        """
        Gets the margin currently allocated to the specified holding
        
        :param parameters: An object containing the security
        :returns: The maintenance margin required for the.
        """
        ...

    def GetMaximumLotsForDeltaBuyingPower(self, parameters: QuantConnect.Securities.Positions.GetMaximumLotsForDeltaBuyingPowerParameters) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """
        Get the maximum market position group order quantity to obtain a delta in the buying power used by a position group.
        The deltas sign defines the position side to apply it to, positive long, negative short.
        
        :param parameters: An object containing the portfolio, the position group and the delta buying power
        :returns: Returns the maximum allowed market order quantity and if zero, also the reason.
        """
        ...

    def GetMaximumLotsForTargetBuyingPower(self, parameters: QuantConnect.Securities.Positions.GetMaximumLotsForTargetBuyingPowerParameters) -> QuantConnect.Securities.Positions.GetMaximumLotsResult:
        """
        Get the maximum position group order quantity to obtain a position with a given buying power
        percentage. Will not take into account free buying power.
        
        :param parameters: An object containing the portfolio, the position group and the target     signed buying power percentage
        :returns: Returns the maximum allowed market order quantity and if zero, also the reason.
        """
        ...

    def HasSufficientBuyingPowerForOrder(self, parameters: QuantConnect.Securities.Positions.HasSufficientPositionGroupBuyingPowerForOrderParameters) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """
        Check if there is sufficient buying power for the position group to execute this order.
        
        :param parameters: An object containing the portfolio, the position group and the order
        :returns: Returns buying power information for an order against a position group.
        """
        ...

    def PassesPositionGroupSpecificBuyingPowerForOrderChecks(self, parameters: QuantConnect.Securities.Positions.HasSufficientPositionGroupBuyingPowerForOrderParameters, availableBuyingPower: float) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """
        Additionally check initial margin requirements if the algorithm only has default position groups
        
        This method is protected.
        """
        ...


class PositionCollection(System.Object, typing.Iterable[QuantConnect.Securities.Positions.IPosition]):
    """
    Provides a collection type for IPosition aimed at providing indexing for
    common operations required by the resolver implementations.
    """

    @property
    def Count(self) -> int:
        """Gets the number of elements in the collection."""
        ...

    @overload
    def __init__(self, positions: System.Collections.Immutable.ImmutableDictionary[QuantConnect.Symbol, QuantConnect.Securities.Positions.IPosition]) -> None:
        """
        Initializes a new instance of the PositionCollection class
        
        :param positions: The positions to include in this collection
        """
        ...

    @overload
    def __init__(self, positions: System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPosition]) -> None:
        """
        Initializes a new instance of the PositionCollection class
        
        :param positions: The positions to include in this collection
        """
        ...

    def Clear(self) -> None:
        """Clears this collection of all positions"""
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Securities.Positions.IPosition]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: An enumerator that can be used to iterate through the collection.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        """
        Returns an enumerator that iterates through a collection.
        
        :returns: An System.Collections.IEnumerator object that can be used to iterate through the collection.
        """
        ...

    def Remove(self, groups: System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPositionGroup]) -> None:
        """
        Removes the quantities in the provided groups from this position collection.
        This should be called following IPositionGroupResolver has resolved
        position groups in order to update the collection of positions for the next resolver,
        if one exists.
        
        :param groups: The resolved position groups
        """
        ...

    def TryGetPosition(self, symbol: typing.Union[QuantConnect.Symbol, str], position: typing.Optional[QuantConnect.Securities.Positions.IPosition]) -> typing.Union[bool, QuantConnect.Securities.Positions.IPosition]:
        """
        Attempts to retrieve the position with the specified symbol from this collection
        
        :param symbol: The symbol
        :param position: The position
        :returns: True if the position is found, otherwise false.
        """
        ...


class IPositionGroupResolver(metaclass=abc.ABCMeta):
    """Resolves position groups from a collection of positions."""

    def GetImpactedGroups(self, groups: QuantConnect.Securities.Positions.PositionGroupCollection, positions: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition]) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPositionGroup]:
        """
        Determines the position groups that would be evaluated for grouping of the specified
        positions were passed into the Resolve method.
        
        :param groups: The existing position groups
        :param positions: The positions being changed
        :returns: An enumerable containing the position groups that could be impacted by the specified position changes.
        """
        ...

    def Resolve(self, positions: QuantConnect.Securities.Positions.PositionCollection) -> QuantConnect.Securities.Positions.PositionGroupCollection:
        """
        Resolves the position groups that exist within the specified collection of positions.
        
        :param positions: The collection of positions
        :returns: An enumerable of position groups.
        """
        ...

    def TryGroup(self, newPositions: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition], currentPositions: QuantConnect.Securities.Positions.PositionGroupCollection, group: typing.Optional[QuantConnect.Securities.Positions.IPositionGroup]) -> typing.Union[bool, QuantConnect.Securities.Positions.IPositionGroup]:
        """
        Attempts to group the specified positions into a new IPositionGroup using an
        appropriate IPositionGroupBuyingPowerModel for position groups created via this
        resolver.
        
        :param newPositions: The positions to be grouped
        :param currentPositions: The currently grouped positions
        :param group: The grouped positions when this resolver is able to, otherwise null
        :returns: True if this resolver can group the specified positions, otherwise false.
        """
        ...


class CompositePositionGroupResolver(System.Object, QuantConnect.Securities.Positions.IPositionGroupResolver):
    """
    Provides an implementation of IPositionGroupResolver that invokes multiple wrapped implementations
    in succession. Each successive call to IPositionGroupResolver.Resolve will receive
    the remaining positions that have yet to be grouped. Any non-grouped positions are placed into identity groups.
    """

    @property
    def Count(self) -> int:
        """Gets the count of registered resolvers"""
        ...

    @overload
    def __init__(self, *resolvers: QuantConnect.Securities.Positions.IPositionGroupResolver) -> None:
        """
        Initializes a new instance of the CompositePositionGroupResolver class
        
        :param resolvers: The position group resolvers to be invoked in order
        """
        ...

    @overload
    def __init__(self, resolvers: System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPositionGroupResolver]) -> None:
        """
        Initializes a new instance of the CompositePositionGroupResolver class
        
        :param resolvers: The position group resolvers to be invoked in order
        """
        ...

    @overload
    def Add(self, resolver: QuantConnect.Securities.Positions.IPositionGroupResolver) -> None:
        """
        Adds the specified  to the end of the list of resolvers. This resolver will run last.
        
        :param resolver: The resolver to be added
        """
        ...

    @overload
    def Add(self, resolver: QuantConnect.Securities.Positions.IPositionGroupResolver, index: int) -> None:
        """
        Inserts the specified  into the list of resolvers at the specified index.
        
        :param resolver: The resolver to be inserted
        :param index: The zero based index indicating where to insert the resolver, zero inserts to the beginning of the list making this resolver un first and Count inserts the resolver to the end of the list making this resolver run last
        """
        ...

    def GetImpactedGroups(self, groups: QuantConnect.Securities.Positions.PositionGroupCollection, positions: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition]) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPositionGroup]:
        """
        Determines the position groups that would be evaluated for grouping of the specified
        positions were passed into the Resolve method.
        
        :param groups: The existing position groups
        :param positions: The positions being changed
        :returns: An enumerable containing the position groups that could be impacted by the specified position changes.
        """
        ...

    def Remove(self, resolver: QuantConnect.Securities.Positions.IPositionGroupResolver) -> bool:
        """
        Removes the specified  from the list of resolvers
        
        :param resolver: The resolver to be removed
        :returns: True if the resolver was removed, false if it wasn't found in the list.
        """
        ...

    def Resolve(self, positions: QuantConnect.Securities.Positions.PositionCollection) -> QuantConnect.Securities.Positions.PositionGroupCollection:
        """
        Resolves the optimal set of IPositionGroup from the provided .
        Implementations are required to deduct grouped positions from the  collection.
        """
        ...

    def TryGroup(self, newPositions: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition], currentPositions: QuantConnect.Securities.Positions.PositionGroupCollection, group: typing.Optional[QuantConnect.Securities.Positions.IPositionGroup]) -> typing.Union[bool, QuantConnect.Securities.Positions.IPositionGroup]:
        """
        Attempts to group the specified positions into a new IPositionGroup using an
        appropriate IPositionGroupBuyingPowerModel for position groups created via this
        resolver.
        
        :param newPositions: The positions to be grouped
        :param currentPositions: The currently grouped positions
        :param group: The grouped positions when this resolver is able to, otherwise null
        :returns: True if this resolver can group the specified positions, otherwise false.
        """
        ...


class PositionGroupExtensions(System.Object):
    """Provides extension methods for IPositionGroup"""

    @staticmethod
    def GetPosition(group: QuantConnect.Securities.Positions.IPositionGroup, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Securities.Positions.IPosition:
        """Gets the position in the  matching the provided"""
        ...

    @staticmethod
    def GetPositionSide(group: QuantConnect.Securities.Positions.IPositionGroup) -> int:
        """
        Gets the position side (long/short/none) of the specified
        
        :returns: This method returns the int value of a member of the QuantConnect.PositionSide enum.
        """
        ...

    @staticmethod
    def GetUserFriendlyName(group: QuantConnect.Securities.Positions.IPositionGroup) -> str:
        """Gets a user friendly name for the provided"""
        ...

    @staticmethod
    def WithQuantity(template: QuantConnect.Securities.Positions.IPositionGroup, groupQuantity: float) -> QuantConnect.Securities.Positions.IPositionGroup:
        """
        Creates a new IPositionGroup with the specified .
        If the quantity provided equals the template's quantity then the template is returned.
        
        :param template: The group template
        :param groupQuantity: The quantity of the new group
        :returns: A position group with the same position ratios as the template but with the specified group quantity.
        """
        ...


class Position(System.Object, QuantConnect.Securities.Positions.IPosition):
    """Defines a quantity of a security's holdings for inclusion in a position group"""

    @property
    def Symbol(self) -> QuantConnect.Symbol:
        """The symbol"""
        ...

    @property
    def Quantity(self) -> float:
        """The quantity"""
        ...

    @property
    def UnitQuantity(self) -> float:
        """
        The unit quantity. The unit quantities of a group define the group. For example, a covered
        call has 100 units of stock and -1 units of call contracts.
        """
        ...

    @overload
    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: float, unitQuantity: float) -> None:
        """
        Initializes a new instance of the Position class
        
        :param symbol: The symbol
        :param quantity: The quantity
        :param unitQuantity: The position's unit quantity within its group
        """
        ...

    @overload
    def __init__(self, security: QuantConnect.Securities.Security, quantity: typing.Optional[float] = None) -> None:
        """
        Initializes a new instance of the Position class using the security's lot size
        as it's unit quantity. If quantity is null, then the security's holdings quantity is used.
        
        :param security: The security
        :param quantity: The quantity, if null, the security's holdings quantity is used
        """
        ...

    def ToString(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class SecurityPositionGroupResolver(System.Object, QuantConnect.Securities.Positions.IPositionGroupResolver):
    """Provides an implementation of IPositionGroupResolver that places all positions into a default group of one security."""

    def __init__(self, buyingPowerModel: QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel) -> None:
        """
        Initializes a new instance of the SecurityPositionGroupResolver class
        
        :param buyingPowerModel: The buying power model to use for created groups
        """
        ...

    def GetImpactedGroups(self, groups: QuantConnect.Securities.Positions.PositionGroupCollection, positions: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition]) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPositionGroup]:
        """
        Determines the position groups that would be evaluated for grouping of the specified
        positions were passed into the IPositionGroupResolver.Resolve method.
        
        :param groups: The existing position groups
        :param positions: The positions being changed
        :returns: An enumerable containing the position groups that could be impacted by the specified position changes.
        """
        ...

    def Resolve(self, positions: QuantConnect.Securities.Positions.PositionCollection) -> QuantConnect.Securities.Positions.PositionGroupCollection:
        """
        Resolves the position groups that exist within the specified collection of positions.
        
        :param positions: The collection of positions
        :returns: An enumerable of position groups.
        """
        ...

    def TryGroup(self, newPositions: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition], currentPositions: QuantConnect.Securities.Positions.PositionGroupCollection, group: typing.Optional[QuantConnect.Securities.Positions.IPositionGroup]) -> typing.Union[bool, QuantConnect.Securities.Positions.IPositionGroup]:
        """
        Attempts to group the specified positions into a new IPositionGroup using an
        appropriate IPositionGroupBuyingPowerModel for position groups created via this
        resolver.
        
        :param newPositions: The positions to be grouped
        :param currentPositions: The currently grouped positions
        :param group: The grouped positions when this resolver is able to, otherwise null
        :returns: True if this resolver can group the specified positions, otherwise false.
        """
        ...


class PositionManager(System.Object):
    """Responsible for managing the resolution of position groups for an algorithm"""

    @property
    def Groups(self) -> QuantConnect.Securities.Positions.PositionGroupCollection:
        """Gets the set of currently resolved position groups"""
        ...

    @Groups.setter
    def Groups(self, value: QuantConnect.Securities.Positions.PositionGroupCollection):
        """Gets the set of currently resolved position groups"""
        ...

    @property
    def IsOnlyDefaultGroups(self) -> bool:
        """Gets whether or not the algorithm is using only default position groups"""
        ...

    def __getitem__(self, key: QuantConnect.Securities.Positions.PositionGroupKey) -> QuantConnect.Securities.Positions.IPositionGroup:
        """
        Gets the IPositionGroup matching the specified . If one is not found,
        then a new empty position group is returned.
        """
        ...

    def __init__(self, securities: QuantConnect.Securities.SecurityManager) -> None:
        """
        Initializes a new instance of the PositionManager class
        
        :param securities: The algorithm's security manager
        """
        ...

    def CreateDefaultKey(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.Positions.PositionGroupKey:
        """Creates a PositionGroupKey for the security's default position group"""
        ...

    def CreatePositionGroup(self, order: QuantConnect.Orders.Order) -> QuantConnect.Securities.Positions.IPositionGroup:
        """
        Creates a position group for the specified order, pulling
        
        :param order: The order
        :returns: A new position group matching the provided order.
        """
        ...

    def GetImpactedGroups(self, positions: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition]) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPositionGroup]:
        """
        Determines which position groups could be impacted by changes in the specified positions
        
        :param positions: The positions to be changed
        :returns: All position groups that need to be re-evaluated due to changes in the positions.
        """
        ...

    def GetOrCreateDefaultGroup(self, security: QuantConnect.Securities.Security) -> QuantConnect.Securities.Positions.IPositionGroup:
        """Gets or creates the default position group for the specified"""
        ...

    def ResolvePositionGroups(self, positions: QuantConnect.Securities.Positions.PositionCollection) -> QuantConnect.Securities.Positions.PositionGroupCollection:
        """
        Resolves position groups using the specified collection of positions
        
        :param positions: The positions to be grouped
        :returns: A collection of position groups containing all of the provided positions.
        """
        ...


class PositionGroupBuyingPowerModelExtensions(System.Object):
    """
    Provides methods aimed at reducing the noise introduced from having result/parameter types for each method.
    These methods aim to accept raw arguments and return the desired value type directly.
    """

    @staticmethod
    def GetInitialMarginRequiredForOrder(model: QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel, portfolio: QuantConnect.Securities.SecurityPortfolioManager, positionGroup: QuantConnect.Securities.Positions.IPositionGroup, order: QuantConnect.Orders.Order) -> float:
        """Gets the total margin required to execute the specified order in units of the account currency including fees"""
        ...

    @staticmethod
    def GetInitialMarginRequirement(model: QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel, portfolio: QuantConnect.Securities.SecurityPortfolioManager, positionGroup: QuantConnect.Securities.Positions.IPositionGroup) -> float:
        """The margin that must be held in order to change positions by the changes defined by the provided position group"""
        ...

    @staticmethod
    def GetMaintenanceMargin(model: QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel, portfolio: QuantConnect.Securities.SecurityPortfolioManager, positionGroup: QuantConnect.Securities.Positions.IPositionGroup) -> float:
        """Gets the margin currently allocated to the specified position group"""
        ...

    @staticmethod
    def GetPositionGroupBuyingPower(model: QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel, portfolio: QuantConnect.Securities.SecurityPortfolioManager, positionGroup: QuantConnect.Securities.Positions.IPositionGroup, direction: QuantConnect.Orders.OrderDirection) -> QuantConnect.Securities.Positions.PositionGroupBuyingPower:
        """Gets the buying power available for a position group trade"""
        ...

    @staticmethod
    def GetReservedBuyingPowerForPositionGroup(model: QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel, portfolio: QuantConnect.Securities.SecurityPortfolioManager, positionGroup: QuantConnect.Securities.Positions.IPositionGroup) -> float:
        """Computes the amount of buying power reserved by the provided position group"""
        ...

    @staticmethod
    def HasSufficientBuyingPowerForOrder(model: QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel, portfolio: QuantConnect.Securities.SecurityPortfolioManager, positionGroup: QuantConnect.Securities.Positions.IPositionGroup, order: QuantConnect.Orders.Order) -> QuantConnect.Securities.HasSufficientBuyingPowerForOrderResult:
        """Check if there is sufficient buying power for the position group to execute this order."""
        ...


class OptionStrategyPositionGroupResolver(System.Object, QuantConnect.Securities.Positions.IPositionGroupResolver):
    """Class in charge of resolving option strategy groups which will use the OptionStrategyPositionGroupBuyingPowerModel"""

    @overload
    def __init__(self, securities: QuantConnect.Securities.SecurityManager) -> None:
        """Creates the default option strategy group resolver for OptionStrategyDefinitions.AllDefinitions"""
        ...

    @overload
    def __init__(self, securities: QuantConnect.Securities.SecurityManager, strategyMatcherOptions: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyMatcherOptions) -> None:
        """
        Creates a custom option strategy group resolver
        
        :param securities: The algorithms securities
        :param strategyMatcherOptions: The option strategy matcher options instance to use
        """
        ...

    def GetImpactedGroups(self, groups: QuantConnect.Securities.Positions.PositionGroupCollection, positions: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition]) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPositionGroup]:
        """
        Determines the position groups that would be evaluated for grouping of the specified
        positions were passed into the Resolve method.
        
        :param groups: The existing position groups
        :param positions: The positions being changed
        :returns: An enumerable containing the position groups that could be impacted by the specified position changes.
        """
        ...

    def Resolve(self, positions: QuantConnect.Securities.Positions.PositionCollection) -> QuantConnect.Securities.Positions.PositionGroupCollection:
        """
        Resolves the position groups that exist within the specified collection of positions.
        
        :param positions: The collection of positions
        :returns: An enumerable of position groups.
        """
        ...

    def TryGroup(self, newPositions: System.Collections.Generic.IReadOnlyCollection[QuantConnect.Securities.Positions.IPosition], currentPositions: QuantConnect.Securities.Positions.PositionGroupCollection, group: typing.Optional[QuantConnect.Securities.Positions.IPositionGroup]) -> typing.Union[bool, QuantConnect.Securities.Positions.IPositionGroup]:
        """
        Attempts to group the specified positions into a new IPositionGroup using an
        appropriate IPositionGroupBuyingPowerModel for position groups created via this
        resolver.
        
        :param newPositions: The positions to be grouped
        :param currentPositions: The currently grouped positions
        :returns: True if this resolver can group the specified positions, otherwise false.
        """
        ...


class PositionExtensions(System.Object):
    """Provides extension methods for IPosition"""

    @staticmethod
    def Combine(position: QuantConnect.Securities.Positions.IPosition, other: QuantConnect.Securities.Positions.IPosition) -> QuantConnect.Securities.Positions.IPosition:
        """
        Combines the provided positions into a single position with the quantities added and the minimum unit quantity.
        
        :param position: The position
        :param other: The other position to add
        :returns: The combined position.
        """
        ...

    @staticmethod
    def Consolidate(positions: System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPosition]) -> System.Collections.Generic.Dictionary[QuantConnect.Symbol, QuantConnect.Securities.Positions.IPosition]:
        """
        Consolidates the provided  into a dictionary
        
        :param positions: The positions to be consolidated
        :returns: A dictionary containing the consolidated positions.
        """
        ...

    @staticmethod
    def Deduct(position: QuantConnect.Securities.Positions.IPosition, quantityToDeduct: float) -> QuantConnect.Securities.Positions.IPosition:
        """
        Deducts the specified  from the specified
        
        :param position: The source position
        :param quantityToDeduct: The quantity to deduct
        :returns: A new position with the same properties but quantity reduced by the specified amount.
        """
        ...

    @staticmethod
    def WithLots(position: QuantConnect.Securities.Positions.IPosition, numberOfLots: float) -> QuantConnect.Securities.Positions.IPosition:
        """
        Creates a new IPosition with quantity equal to  times its unit quantity
        
        :param position: The position
        :param numberOfLots: The number of lots for the new position
        :returns: A new position with the specified number of lots.
        """
        ...


class PositionGroup(System.Object, QuantConnect.Securities.Positions.IPositionGroup, typing.Iterable[QuantConnect.Securities.Positions.IPosition]):
    """Provides a default implementation of IPositionGroup"""

    @property
    def Count(self) -> int:
        """Gets the number of positions in the group"""
        ...

    @property
    def Key(self) -> QuantConnect.Securities.Positions.PositionGroupKey:
        """Gets the key identifying this group"""
        ...

    @property
    def Quantity(self) -> float:
        """Gets the whole number of units in this position group"""
        ...

    @property
    def Positions(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPosition]:
        """Gets the positions in this group"""
        ...

    @property
    def BuyingPowerModel(self) -> QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel:
        """Gets the buying power model defining how margin works in this group"""
        ...

    @overload
    def __init__(self, buyingPowerModel: QuantConnect.Securities.Positions.IPositionGroupBuyingPowerModel, *positions: QuantConnect.Securities.Positions.IPosition) -> None:
        """
        Initializes a new instance of the PositionGroup class
        
        :param buyingPowerModel: The buying power model to use for this group
        :param positions: The positions comprising this group
        """
        ...

    @overload
    def __init__(self, key: QuantConnect.Securities.Positions.PositionGroupKey, *positions: QuantConnect.Securities.Positions.IPosition) -> None:
        """
        Initializes a new instance of the PositionGroup class
        
        :param key: The deterministic key for this group
        :param positions: The positions comprising this group
        """
        ...

    @overload
    def __init__(self, key: QuantConnect.Securities.Positions.PositionGroupKey, positions: System.Collections.Generic.Dictionary[QuantConnect.Symbol, QuantConnect.Securities.Positions.IPosition]) -> None:
        """
        Initializes a new instance of the PositionGroup class
        
        :param key: The deterministic key for this group
        :param positions: The positions comprising this group
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Securities.Positions.IPosition]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: An enumerator that can be used to iterate through the collection.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        """
        Returns an enumerator that iterates through a collection.
        
        :returns: An System.Collections.IEnumerator object that can be used to iterate through the collection.
        """
        ...

    def ToString(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...

    def TryGetPosition(self, symbol: typing.Union[QuantConnect.Symbol, str], position: typing.Optional[QuantConnect.Securities.Positions.IPosition]) -> typing.Union[bool, QuantConnect.Securities.Positions.IPosition]:
        """
        Attempts to retrieve the position with the specified symbol
        
        :param symbol: The symbol
        :param position: The position, if found
        :returns: True if the position was found, otherwise false.
        """
        ...


