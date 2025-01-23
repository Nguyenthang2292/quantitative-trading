from typing import overload
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Securities
import QuantConnect.Securities.Option
import QuantConnect.Securities.Option.StrategyMatcher
import QuantConnect.Securities.Positions
import System
import System.Collections
import System.Collections.Generic
import System.Collections.Immutable

QuantConnect_Securities_Option_StrategyMatcher_OptionStrategyLegDefinitionMatch = typing.Any
Expression = typing.Any
QuantConnect_Securities_Option_StrategyMatcher_OptionPosition = typing.Any
QuantConnect_Securities_Option_StrategyMatcher_OptionStrategyDefinitionMatch = typing.Any

QuantConnect_Securities_Option_StrategyMatcher_ConstantOptionStrategyLegPredicateReferenceValue_T = typing.TypeVar("QuantConnect_Securities_Option_StrategyMatcher_ConstantOptionStrategyLegPredicateReferenceValue_T")


class OptionPosition(System.IEquatable[QuantConnect_Securities_Option_StrategyMatcher_OptionPosition]):
    """
    Defines a lightweight structure representing a position in an option contract or underlying.
    This type is heavily utilized by the options strategy matcher and is the parameter type of
    option strategy definition predicates. Underlying quantities should be represented in lot sizes,
    which is equal to the quantity of shares divided by the contract's multiplier and then rounded
    down towards zero (truncate)
    """

    @property
    def HasQuantity(self) -> bool:
        """Determines whether or not this position has any quantity"""
        ...

    @property
    def IsUnderlying(self) -> bool:
        """Determines whether or not this position is for the underlying symbol"""
        ...

    @property
    def Quantity(self) -> int:
        """Number of contracts held, can be positive or negative"""
        ...

    @property
    def Symbol(self) -> QuantConnect.Symbol:
        """Option contract symbol"""
        ...

    @property
    def Underlying(self) -> QuantConnect.Symbol:
        """
        Gets the underlying symbol. If this position represents the underlying,
        then this property is the same as the Symbol property
        """
        ...

    @property
    def Expiration(self) -> datetime.datetime:
        """Option contract expiration date"""
        ...

    @property
    def Strike(self) -> float:
        """Option contract strike price"""
        ...

    @property
    def Right(self) -> int:
        """
        Option contract right (put/call)
        
        This property contains the int value of a member of the QuantConnect.OptionRight enum.
        """
        ...

    @property
    def Side(self) -> int:
        """
        Gets whether this position is short/long/none
        
        This property contains the int value of a member of the QuantConnect.PositionSide enum.
        """
        ...

    def __init__(self, symbol: typing.Union[QuantConnect.Symbol, str], quantity: int) -> None:
        """
        Initializes a new instance of the OptionPosition structure
        
        :param symbol: The option contract symbol
        :param quantity: The number of contracts held
        """
        ...

    @staticmethod
    def Empty(symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Securities.Option.StrategyMatcher.OptionPosition:
        """Gets a new OptionPosition with zero Quantity"""
        ...

    @overload
    def Equals(self, other: QuantConnect.Securities.Option.StrategyMatcher.OptionPosition) -> bool:
        """
        Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the  parameter; otherwise, false.
        """
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        """
        Indicates whether this instance and a specified object are equal.
        
        :param obj: The object to compare with the current instance.
        :returns: true if  and this instance are the same type and represent the same value; otherwise, false.
        """
        ...

    def GetHashCode(self) -> int:
        """
        Returns the hash code for this instance.
        
        :returns: A 32-bit signed integer that is the hash code for this instance.
        """
        ...

    def Negate(self) -> QuantConnect.Securities.Option.StrategyMatcher.OptionPosition:
        """Creates a new OptionPosition instance with negative Quantity"""
        ...

    def ToString(self) -> str:
        """
        Returns the fully qualified type name of this instance.
        
        :returns: The fully qualified type name.
        """
        ...

    def WithQuantity(self, quantity: int) -> QuantConnect.Securities.Option.StrategyMatcher.OptionPosition:
        """
        Creates a new OptionPosition with this position's Symbol
        and the provided
        """
        ...


class OptionStrategyLegDefinitionMatch(System.IEquatable[QuantConnect_Securities_Option_StrategyMatcher_OptionStrategyLegDefinitionMatch]):
    """
    Defines the item result type of OptionStrategyLegDefinition.Match, containing the number of
    times the leg definition matched the position (Multiplier) and applicable portion of the position.
    """

    @property
    def Multiplier(self) -> int:
        """
        The number of times the definition is able to match the position. For example,
        if the definition requires +2 contracts and the algorithm's position has +5
        contracts, then this multiplier would equal 2.
        """
        ...

    @property
    def Position(self) -> QuantConnect.Securities.Option.StrategyMatcher.OptionPosition:
        """
        The position that was successfully matched with the total quantity matched. For example,
        if the definition requires +2 contracts and this multiplier equals 2, then this position
        would have a quantity of 4. This may be different than the remaining/total quantity
        available in the positions collection.
        """
        ...

    def __init__(self, multiplier: int, position: QuantConnect.Securities.Option.StrategyMatcher.OptionPosition) -> None:
        """
        Initializes a new instance of the OptionStrategyLegDefinitionMatch struct
        
        :param multiplier: The number of times the positions matched the leg definition
        :param position: The position that matched the leg definition
        """
        ...

    def CreateOptionPosition(self, multiplier: int) -> QuantConnect.Securities.Option.StrategyMatcher.OptionPosition:
        """
        Creates the appropriate OptionPosition for this matched position
        
        :param multiplier: The multiplier to use for creating the OptionPosition. This multiplier will be the minimum multiplier of all legs within a strategy definition match. Each leg defines its own multiplier which is the max matches for that leg and the strategy definition's multiplier is the min of the individual legs.
        """
        ...

    def CreateOptionStrategyLeg(self, multiplier: int) -> QuantConnect.Securities.Option.OptionStrategy.LegData:
        """
        Creates the appropriate type of OptionStrategy.LegData for this matched position
        
        :param multiplier: The multiplier to use for creating the leg data. This multiplier will be the minimum multiplier of all legs within a strategy definition match. Each leg defines its own multiplier which is the max matches for that leg and the strategy definition's multiplier is the min of the individual legs.
        """
        ...

    @overload
    def Equals(self, other: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyLegDefinitionMatch) -> bool:
        """
        Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the  parameter; otherwise, false.
        """
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        """
        Indicates whether this instance and a specified object are equal.
        
        :param obj: The object to compare with the current instance.
        :returns: true if  and this instance are the same type and represent the same value; otherwise, false.
        """
        ...

    def GetHashCode(self) -> int:
        """
        Returns the hash code for this instance.
        
        :returns: A 32-bit signed integer that is the hash code for this instance.
        """
        ...

    def ToString(self) -> str:
        """
        Returns the fully qualified type name of this instance.
        
        :returns: The fully qualified type name.
        """
        ...


class OptionPositionCollection(System.Object, typing.Iterable[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition]):
    """Provides indexing of option contracts"""

    Empty: QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection
    """Gets an empty instance of OptionPositionCollection"""

    @property
    def Underlying(self) -> QuantConnect.Symbol:
        """Gets the underlying security's symbol"""
        ...

    @property
    def Count(self) -> int:
        """Gets the total count of unique positions, including the underlying"""
        ...

    @property
    def IsEmpty(self) -> bool:
        """Gets whether or not there's any positions in this collection."""
        ...

    @property
    def UnderlyingQuantity(self) -> int:
        """
        Gets the quantity of underlying shares held
        TODO : Change to UnderlyingLots
        """
        ...

    @property
    def UniquePuts(self) -> int:
        """Gets the number of unique put contracts held (long or short)"""
        ...

    @property
    def UniqueExpirations(self) -> int:
        """Gets the unique number of expirations"""
        ...

    @property
    def UniqueCalls(self) -> int:
        """Gets the number of unique call contracts held (long or short)"""
        ...

    @property
    def HasUnderlying(self) -> bool:
        """Determines if this collection contains a position in the underlying"""
        ...

    @property
    def UnderlyingPosition(self) -> QuantConnect.Securities.Option.StrategyMatcher.OptionPosition:
        """Gets the Underlying position"""
        ...

    @property
    def Strikes(self) -> System.Collections.Generic.IEnumerable[float]:
        """Gets all unique strike prices in the collection, in ascending order."""
        ...

    @property
    def Expirations(self) -> System.Collections.Generic.IEnumerable[datetime.datetime]:
        """Gets all unique expiration dates in the collection, in chronological order."""
        ...

    def __init__(self, positions: System.Collections.Immutable.ImmutableDictionary[QuantConnect.Symbol, QuantConnect.Securities.Option.StrategyMatcher.OptionPosition], rights: System.Collections.Immutable.ImmutableDictionary[QuantConnect.OptionRight, System.Collections.Immutable.ImmutableHashSet[QuantConnect.Symbol]], sides: System.Collections.Immutable.ImmutableDictionary[QuantConnect.PositionSide, System.Collections.Immutable.ImmutableHashSet[QuantConnect.Symbol]], strikes: System.Collections.Immutable.ImmutableSortedDictionary[float, System.Collections.Immutable.ImmutableHashSet[QuantConnect.Symbol]], expirations: System.Collections.Immutable.ImmutableSortedDictionary[datetime.datetime, System.Collections.Immutable.ImmutableHashSet[QuantConnect.Symbol]]) -> None:
        """
        Initializes a new instance of the OptionPositionCollection class
        
        :param positions: All positions
        :param rights: Index of position symbols by option right
        :param sides: Index of position symbols by position side (short/long/none)
        :param strikes: Index of position symbols by strike price
        :param expirations: Index of position symbols by expiration
        """
        ...

    def Add(self, position: QuantConnect.Securities.Option.StrategyMatcher.OptionPosition) -> QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection:
        """Creates a new collection that is the result of adding the specified  to this collection."""
        ...

    @overload
    def AddRange(self, *positions: QuantConnect.Securities.Option.StrategyMatcher.OptionPosition) -> QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection:
        """Creates a new collection that is the result of adding the specified  to this collection."""
        ...

    @overload
    def AddRange(self, positions: System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition]) -> QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection:
        """Creates a new collection that is the result of adding the specified  to this collection."""
        ...

    @staticmethod
    def Create(underlying: typing.Union[QuantConnect.Symbol, str], contractMultiplier: float, holdings: System.Collections.Generic.IEnumerable[QuantConnect.Securities.SecurityHolding]) -> QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection:
        """
        Creates a new OptionPositionCollection from the specified ,
        filtering based on the
        """
        ...

    def ForExpiration(self, expiration: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition]:
        """Returns the set of OptionPosition with the specified"""
        ...

    def ForRight(self, right: QuantConnect.OptionRight) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition]:
        """Returns the set of OptionPosition with the specified"""
        ...

    def ForSide(self, side: QuantConnect.PositionSide) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition]:
        """Returns the set of OptionPosition with the specified"""
        ...

    def ForStrike(self, strike: float) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition]:
        """Returns the set of OptionPosition with the specified"""
        ...

    def ForSymbols(self, symbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol]) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition]:
        """Returns the set of OptionPosition with the specified"""
        ...

    @staticmethod
    @overload
    def FromPositions(positions: System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition]) -> QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection:
        """Creates a new OptionPositionCollection from the specified enumerable of"""
        ...

    @staticmethod
    @overload
    def FromPositions(positions: System.Collections.Generic.IEnumerable[QuantConnect.Securities.Positions.IPosition], contractMultiplier: float) -> QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection:
        """Creates a new OptionPositionCollection from the specified enumerable of"""
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: An enumerator that can be used to iterate through the collection.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        ...

    def HasPosition(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """Determines if a position is held in the specified"""
        ...

    def Remove(self, position: QuantConnect.Securities.Option.StrategyMatcher.OptionPosition) -> QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection:
        """Creates a new collection that is the result of removing the specified"""
        ...

    def RemoveRange(self, positions: System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition]) -> QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection:
        """Creates a new collection that is the result of removing the specified"""
        ...

    @overload
    def Slice(self, right: QuantConnect.OptionRight, includeUnderlying: bool = True) -> QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection:
        """
        Slices this collection, returning a new collection containing only
        positions with the specified
        """
        ...

    @overload
    def Slice(self, side: QuantConnect.PositionSide, includeUnderlying: bool = True) -> QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection:
        """
        Slices this collection, returning a new collection containing only
        positions with the specified
        """
        ...

    @overload
    def Slice(self, comparison: QuantConnect.BinaryComparison, strike: float, includeUnderlying: bool = True) -> QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection:
        """
        Slices this collection, returning a new collection containing only
        positions matching the specified  and
        """
        ...

    @overload
    def Slice(self, comparison: QuantConnect.BinaryComparison, expiration: typing.Union[datetime.datetime, datetime.date], includeUnderlying: bool = True) -> QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection:
        """
        Slices this collection, returning a new collection containing only
        positions matching the specified  and
        """
        ...

    def ToString(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...

    def TryGetPosition(self, symbol: typing.Union[QuantConnect.Symbol, str], position: typing.Optional[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition]) -> typing.Union[bool, QuantConnect.Securities.Option.StrategyMatcher.OptionPosition]:
        """
        Retrieves the OptionPosition for the specified 
        if one exists in this collection.
        """
        ...


class IOptionPositionCollectionEnumerator(metaclass=abc.ABCMeta):
    """
    Enumerates an OptionPositionCollection. The intent is to evaluate positions that
    may be more important sooner. Positions appearing earlier in the enumeration are evaluated before
    positions showing later. This effectively prioritizes individual positions. This should not be
    used filter filtering, but it could also be used to split a position, for example a position with
    10 could be changed to two 5s and they don't need to be enumerated back to-back either. In this
    way you could prioritize the first 5 and then delay matching of the final 5.
    """

    def Enumerate(self, positions: QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition]:
        """
        Enumerates the provided . Positions enumerated first are more
        likely to be matched than those appearing later in the enumeration.
        """
        ...


class AbsoluteRiskOptionPositionCollectionEnumerator(System.Object, QuantConnect.Securities.Option.StrategyMatcher.IOptionPositionCollectionEnumerator):
    """
    Stub class providing an idea towards an optimal IOptionPositionCollectionEnumerator implementation
    that still needs to be implemented.
    """

    def __init__(self, marketPriceProvider: typing.Callable[[QuantConnect.Symbol], float]) -> None:
        """
        Intializes a new instance of the AbsoluteRiskOptionPositionCollectionEnumerator class
        
        :param marketPriceProvider: Function providing the current market price for a provided symbol
        """
        ...

    def Enumerate(self, positions: QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition]:
        """
        Enumerates the provided . Positions enumerated first are more
        likely to be matched than those appearing later in the enumeration.
        """
        ...


class IOptionStrategyLegPredicateReferenceValue(metaclass=abc.ABCMeta):
    """
    When decoding leg predicates, we extract the value we're comparing against
    If we're comparing against another leg's value (such as legs[0].Strike), then
    we'll create a OptionStrategyLegPredicateReferenceValue. If we're comparing against a literal/constant value,
    then we'll create a ConstantOptionStrategyLegPredicateReferenceValue. These reference values are used to slice
    the OptionPositionCollection to only include positions matching the
    predicate.
    """

    @property
    @abc.abstractmethod
    def Target(self) -> int:
        """
        Gets the target of this value
        
        This property contains the int value of a member of the QuantConnect.Securities.Option.StrategyMatcher.PredicateTargetValue enum.
        """
        ...

    def Resolve(self, legs: System.Collections.Generic.IReadOnlyList[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition]) -> System.Object:
        """
        Resolves the value of the comparand specified in an OptionStrategyLegPredicate.
        For example, the predicate may include ... > legs[0].Strike, and upon evaluation, we need to
        be able to extract leg[0].Strike for the currently contemplated set of legs adhering to a
        strategy's definition.
        """
        ...


class OptionStrategyMatch(System.Object):
    """
    Defines a complete result from running the matcher on a collection of positions.
    The matching process will return one these matches for every potential combination
    of strategies conforming to the search settings and the positions provided.
    """

    @property
    def Strategies(self) -> System.Collections.Generic.List[QuantConnect.Securities.Option.OptionStrategy]:
        """The strategies that were matched"""
        ...

    def __init__(self, strategies: System.Collections.Generic.List[QuantConnect.Securities.Option.OptionStrategy]) -> None:
        """Initializes a new instance of the OptionStrategyMatch class"""
        ...


class IOptionStrategyMatchObjectiveFunction(metaclass=abc.ABCMeta):
    """Evaluates the provided match to assign an objective score. Higher scores are better."""

    def ComputeScore(self, input: QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection, match: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyMatch, unmatched: QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection) -> float:
        """
        Evaluates the objective function for the provided match solution. Solution with the highest score will be selected
        as the solution. NOTE: This part of the match has not been implemented as of 2020-11-06 as it's only evaluating the
        first solution match (MatchOnce).
        """
        ...


class IOptionStrategyDefinitionEnumerator(metaclass=abc.ABCMeta):
    """
    Enumerates OptionStrategyDefinition for the purposes of providing a bias towards definitions
    that are more favorable to be matched before matching less favorable definitions.
    """

    def Enumerate(self, definitions: System.Collections.Generic.IReadOnlyList[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition]) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition]:
        """Enumerates the  according to the implementation's own concept of favorability."""
        ...


class OptionStrategyMatcherOptions(System.Object):
    """Defines options that influence how the matcher operates."""

    @property
    def MaximumDuration(self) -> datetime.timedelta:
        """The maximum amount of time spent trying to find an optimal solution."""
        ...

    @property
    def MaximumSolutionCount(self) -> int:
        """The maximum number of matches to evaluate for the entire portfolio."""
        ...

    @property
    def MaximumCountPerLeg(self) -> System.Collections.Generic.IReadOnlyList[int]:
        """
        Indexed by leg index, defines the max matches to evaluate per leg.
        For example, MaximumCountPerLeg[1] is the max matches to evaluate
        for the second leg (index=1).
        """
        ...

    @property
    def Definitions(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition]:
        """The definitions to be used for matching."""
        ...

    @property
    def ObjectiveFunction(self) -> QuantConnect.Securities.Option.StrategyMatcher.IOptionStrategyMatchObjectiveFunction:
        """Objective function used to compare different match solutions for a given set of positions/definitions"""
        ...

    def __init__(self, definitions: System.Collections.Generic.IReadOnlyList[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition], maximumCountPerLeg: System.Collections.Generic.IReadOnlyList[int], maximumDuration: datetime.timedelta = ..., maximumSolutionCount: int = 100, definitionEnumerator: QuantConnect.Securities.Option.StrategyMatcher.IOptionStrategyDefinitionEnumerator = None, objectiveFunction: QuantConnect.Securities.Option.StrategyMatcher.IOptionStrategyMatchObjectiveFunction = None, positionEnumerator: QuantConnect.Securities.Option.StrategyMatcher.IOptionPositionCollectionEnumerator = None) -> None:
        """
        Initializes a new instance of the OptionStrategyMatcherOptions class, providing
        options that control the behavior of the OptionStrategyMatcher
        """
        ...

    def Enumerate(self, positions: QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition]:
        """
        Enumerates the specified  according to the configured
        IOptionPositionCollectionEnumerator
        """
        ...

    @staticmethod
    @overload
    def ForDefinitions(*definitions: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition) -> QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyMatcherOptions:
        """
        Creates a new OptionStrategyMatcherOptions with the specified ,
        with no limits of maximum matches per leg and default values for the remaining options
        """
        ...

    @staticmethod
    @overload
    def ForDefinitions(definitions: System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition]) -> QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyMatcherOptions:
        """
        Creates a new OptionStrategyMatcherOptions with the specified ,
        with no limits of maximum matches per leg and default values for the remaining options
        """
        ...

    def GetMaximumLegMatches(self, legIndex: int) -> int:
        """
        Gets the maximum number of leg matches to be evaluated. This is to limit evaluating exponential
        numbers of potential matches as a result of large numbers of unique option positions for the same
        underlying security.
        """
        ...

    def WithDefinitionEnumerator(self, enumerator: QuantConnect.Securities.Option.StrategyMatcher.IOptionStrategyDefinitionEnumerator) -> QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyMatcherOptions:
        """
        Specifies the order in which definitions are evaluated. Definitions evaluated sooner are more likely to
        find matches than ones evaluated later.
        """
        ...

    def WithMaximumCountPerLeg(self, counts: System.Collections.Generic.IReadOnlyList[int]) -> QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyMatcherOptions:
        """
        Specifies the maximum number of solutions per leg index in a solution. Matching is a recursive
        process, for example, we'll find a very large number of positions to match the first leg. Matching
        the second leg we'll see less, and third still even less. This is because each subsequent leg must
        abide by all the previous legs. This parameter defines how many potential matches to evaluate at
        each leg. For the first leg, we'll evaluate counts[0] matches. For the second leg we'll evaluate
        counts[1] matches and so on. By decreasing this parameter we can evaluate more total, complete
        solutions for the entire portfolio rather than evaluation every single permutation of matches for
        a particular strategy definition, which grows in absurd exponential fashion as the portfolio grows.
        """
        ...

    def WithMaximumDuration(self, duration: datetime.timedelta) -> QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyMatcherOptions:
        """Specifies the maximum time provided for obtaining an optimal solution."""
        ...

    def WithMaximumSolutionCount(self, count: int) -> QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyMatcherOptions:
        """Specifies the maximum number of solutions to evaluate via the objective function."""
        ...

    def WithObjectiveFunction(self, function: QuantConnect.Securities.Option.StrategyMatcher.IOptionStrategyMatchObjectiveFunction) -> QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyMatcherOptions:
        """
        Specifies a function used to evaluate how desirable a particular solution is. A good implementation for
        this would be to minimize the total margin required to hold all of the positions.
        """
        ...

    def WithPositionEnumerator(self, enumerator: QuantConnect.Securities.Option.StrategyMatcher.IOptionPositionCollectionEnumerator) -> QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyMatcherOptions:
        """
        Specifies the order in which positions are evaluated. Positions evaluated sooner are more likely to
        find matches than ones evaluated later. A good implementation for this is its stand-alone margin required,
        which would encourage the algorithm to match higher margin positions before matching lower margin positiosn.
        """
        ...


class OptionStrategyLegPredicate(System.Object):
    """
    Defines a condition under which a particular OptionPosition can be combined with
    a preceding list of leg (also of type OptionPosition) to achieve a particular
    option strategy.
    """

    @property
    def IsIndexed(self) -> bool:
        """Determines whether or not this predicate is able to utilize OptionPositionCollection indexes."""
        ...

    def __init__(self, comparison: QuantConnect.BinaryComparison, reference: QuantConnect.Securities.Option.StrategyMatcher.IOptionStrategyLegPredicateReferenceValue, predicate: typing.Callable[[System.Collections.Generic.IReadOnlyList[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition], QuantConnect.Securities.Option.StrategyMatcher.OptionPosition], bool], expression: typing.Any) -> None:
        """
        Initializes a new instance of the OptionStrategyLegPredicate class
        
        :param comparison: The BinaryComparison invoked
        :param reference: The reference value, such as a strike price, encapsulated within the IOptionStrategyLegPredicateReferenceValue to enable resolving the value from different potential sets.
        :param predicate: The compiled predicate expression
        :param expression: The predicate expression, from which, all other values were derived.
        """
        ...

    @staticmethod
    def Create(expression: typing.Any) -> QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyLegPredicate:
        """Creates a new OptionStrategyLegPredicate from the specified predicate"""
        ...

    def Filter(self, legs: System.Collections.Generic.IReadOnlyList[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition], positions: QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection, includeUnderlying: bool) -> QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection:
        """Filters the specified  by applying this predicate based on the referenced legs."""
        ...

    def GetReferenceValue(self) -> QuantConnect.Securities.Option.StrategyMatcher.IOptionStrategyLegPredicateReferenceValue:
        """Gets the underlying IOptionStrategyLegPredicateReferenceValue value used by this predicate."""
        ...

    def Matches(self, legs: System.Collections.Generic.IReadOnlyList[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition], position: QuantConnect.Securities.Option.StrategyMatcher.OptionPosition) -> bool:
        """
        Determines whether or not the provided combination of preceding 
        and current  adhere to this predicate's requirements.
        """
        ...

    def ToString(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class OptionStrategyLegDefinition(System.Object, typing.Iterable[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyLegPredicate]):
    """
    Defines a single option leg in an option strategy. This definition supports direct
    match (does position X match the definition) and position collection filtering (filter
    collection to include matches)
    """

    @property
    def Quantity(self) -> int:
        """Gets the unit quantity"""
        ...

    @property
    def Right(self) -> int:
        """
        Gets the contract right
        
        This property contains the int value of a member of the QuantConnect.OptionRight enum.
        """
        ...

    def __init__(self, right: QuantConnect.OptionRight, quantity: int, predicates: System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyLegPredicate]) -> None:
        """
        Initializes a new instance of the OptionStrategyLegDefinition class
        
        :param right: The leg's contract right
        :param quantity: The leg's unit quantity
        :param predicates: The conditions a position must meet in order to match this definition
        """
        ...

    @staticmethod
    def Create(right: QuantConnect.OptionRight, quantity: int, predicates: System.Collections.Generic.IEnumerable[Expression]) -> QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyLegDefinition:
        """Creates a new OptionStrategyLegDefinition matching the specified parameters"""
        ...

    @overload
    def CreateLegData(self, match: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyLegDefinitionMatch) -> QuantConnect.Securities.Option.OptionStrategy.LegData:
        """Creates the appropriate OptionStrategy.LegData for the specified"""
        ...

    @staticmethod
    @overload
    def CreateLegData(symbol: typing.Union[QuantConnect.Symbol, str], quantity: int) -> QuantConnect.Securities.Option.OptionStrategy.LegData:
        """Creates the appropriate OptionStrategy.LegData with the specified"""
        ...

    def Filter(self, legs: System.Collections.Generic.IReadOnlyList[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition], positions: QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection, includeUnderlying: bool = True) -> QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection:
        """
        Filters the provided  collection such that any remaining positions are all
        valid options that match this leg definition instance.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyLegPredicate]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: An enumerator that can be used to iterate through the collection.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        ...

    def Match(self, options: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyMatcherOptions, legs: System.Collections.Generic.IReadOnlyList[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition], positions: QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyLegDefinitionMatch]:
        """
        Yields all possible matches for this leg definition held within the collection of
        
        :param options: Strategy matcher options guiding matching behaviors
        :param legs: The preceding legs already matched for the parent strategy definition
        :param positions: The remaining, unmatched positions available to be matched against
        :returns: An enumerable of potential matches.
        """
        ...

    def TryMatch(self, position: QuantConnect.Securities.Option.StrategyMatcher.OptionPosition, leg: typing.Optional[QuantConnect.Securities.Option.OptionStrategy.LegData]) -> typing.Union[bool, QuantConnect.Securities.Option.OptionStrategy.LegData]:
        """
        Determines whether or not this leg definition matches the specified ,
        and if so, what the resulting quantity of the OptionStrategy.OptionLegData should be.
        """
        ...


class OptionStrategyDefinitionMatch(System.Object, System.IEquatable[QuantConnect_Securities_Option_StrategyMatcher_OptionStrategyDefinitionMatch]):
    """Defines a match of OptionPosition to a OptionStrategyDefinition"""

    @property
    def Definition(self) -> QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition:
        """The OptionStrategyDefinition matched"""
        ...

    @property
    def Multiplier(self) -> int:
        """
        The number of times the definition is able to match the available positions.
        Since definitions are formed at the 'unit' level, such as having 1 contract,
        the multiplier defines how many times the definition matched. This multiplier
        is used to scale the quantity defined in each leg definition when creating the
        OptionStrategy objects.
        """
        ...

    @property
    def Legs(self) -> System.Collections.Generic.IReadOnlyList[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyLegDefinitionMatch]:
        """The OptionStrategyLegDefinitionMatch instances matched to the definition."""
        ...

    def __init__(self, definition: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition, legs: System.Collections.Generic.IReadOnlyList[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyLegDefinitionMatch], multiplier: int) -> None:
        """Initializes a new instance of the OptionStrategyDefinitionMatch class"""
        ...

    def CreateStrategy(self) -> QuantConnect.Securities.Option.OptionStrategy:
        """Creates the OptionStrategy instance this match represents"""
        ...

    @overload
    def Equals(self, other: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinitionMatch) -> bool:
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

    def RemoveFrom(self, positions: QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection) -> QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection:
        """Deducts the matched positions from the specified  taking into account the multiplier"""
        ...

    def ToString(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class OptionStrategyDefinition(System.Object, typing.Iterable[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyLegDefinition]):
    """
    Provides a definitional object for an OptionStrategy. This definition is used to 'match' option
    positions via OptionPositionCollection. The OptionStrategyMatcher utilizes a full
    collection of these definitional objects in order to match an algorithm's option position holdings to the
    set of strategies in an effort to reduce the total margin required for holding the positions.
    """

    class Builder(System.Object):
        """Builder class supporting fluent syntax in constructing OptionStrategyDefinition."""

        def __init__(self, name: str) -> None:
            """Initializes a new instance of the Builder class"""
            ...

        def Build(self) -> QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition:
            """Builds the OptionStrategyDefinition"""
            ...

        def WithCall(self, quantity: int, *predicates: Expression) -> QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition.Builder:
            """Adds a call leg"""
            ...

        def WithPut(self, quantity: int, *predicates: Expression) -> QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition.Builder:
            """Adds a put leg"""
            ...

        def WithUnderlyingLots(self, lots: int) -> QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition.Builder:
            """Sets the required number of underlying lots"""
            ...

    @property
    def Name(self) -> str:
        """Gets the definition's name"""
        ...

    @property
    def UnderlyingLots(self) -> int:
        """
        Gets the number of underlying lots required to match this definition. A lot size
        is equal to the contract's multiplier and is usually equal to 100.
        """
        ...

    @property
    def Legs(self) -> System.Collections.Generic.IReadOnlyList[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyLegDefinition]:
        """
        Gets the option leg definitions. This list does NOT contain a definition for the
        required underlying lots, due to its simplicity. Instead the required underlying
        lots are defined via the UnderlyingLots property of the definition.
        """
        ...

    @property
    def LegCount(self) -> int:
        """
        Gets the total number of legs, INCLUDING the underlying leg if applicable. This
        is used to perform a coarse filter as the minimum number of unique positions in
        the positions collection.
        """
        ...

    def __init__(self, name: str, underlyingLots: int, legs: System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyLegDefinition]) -> None:
        """
        Initializes a new instance of the OptionStrategyDefinition class
        
        :param name: The definition's name
        :param underlyingLots: The required number of underlying lots
        :param legs: Definitions for each option leg
        """
        ...

    @staticmethod
    def CallLeg(quantity: int, *predicates: Expression) -> QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyLegDefinition:
        """Factory function for creating a call leg definition"""
        ...

    @staticmethod
    @overload
    def Create(name: str, underlyingLots: int, *legs: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyLegDefinition) -> QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition:
        """Factory function for creating definitions"""
        ...

    @staticmethod
    @overload
    def Create(name: str, *legs: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyLegDefinition) -> QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition:
        """Factory function for creating definitions"""
        ...

    @staticmethod
    @overload
    def Create(name: str, *predicates: typing.Callable[[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition.Builder], QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition.Builder]) -> QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition:
        """Factory function for creating definitions"""
        ...

    def CreateStrategy(self, legs: System.Collections.Generic.IReadOnlyList[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyLegDefinitionMatch]) -> QuantConnect.Securities.Option.OptionStrategy:
        """Creates the OptionStrategy instance using this definition and the provided leg matches"""
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyLegDefinition]:
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

    @overload
    def Match(self, positions: QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinitionMatch]:
        """
        Determines all possible matches for this definition using the provided .
        This includes OVERLAPPING matches. It's up to the actual matcher to make decisions based on which
        matches to accept. This allows the matcher to prioritize matching certain positions over others.
        """
        ...

    @overload
    def Match(self, options: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyMatcherOptions, positions: QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinitionMatch]:
        """
        Determines all possible matches for this definition using the provided .
        This includes OVERLAPPING matches. It's up to the actual matcher to make decisions based on which
        matches to accept. This allows the matcher to prioritize matching certain positions over others.
        """
        ...

    @staticmethod
    def PutLeg(quantity: int, *predicates: Expression) -> QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyLegDefinition:
        """Factory function for creating a put leg definition"""
        ...

    def ToString(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...

    def TryMatchOnce(self, options: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyMatcherOptions, positions: QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection, match: typing.Optional[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinitionMatch]) -> typing.Union[bool, QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinitionMatch]:
        """
        Attempts to match the positions to this definition exactly once, by evaluating the enumerable and
        taking the first entry matched. If not match is found, then false is returned and 
        will be null.
        """
        ...


class PredicateTargetValue(System.Enum):
    """
    Specifies the type of value being compared against in a OptionStrategyLegPredicate.
    These values define the limits of what can be filtered and must match available slice methods in
    OptionPositionCollection
    """

    Right = 0
    """Predicate matches on OptionPosition.Right (0)"""

    Quantity = 1
    """Predicate match on OptionPosition.Quantity (1)"""

    Strike = 2
    """Predicate matches on OptionPosition.Strike (2)"""

    Expiration = 3
    """Predicate matches on OptionPosition.Expiration (3)"""


class OptionStrategyLegPredicateReferenceValue(System.Object, QuantConnect.Securities.Option.StrategyMatcher.IOptionStrategyLegPredicateReferenceValue):
    """
    Provides an implementation of IOptionStrategyLegPredicateReferenceValue that references an option
    leg from the list of already matched legs by index. The property referenced is defined by PredicateTargetValue
    """

    @property
    def Target(self) -> int:
        """
        Gets the target of this value
        
        This property contains the int value of a member of the QuantConnect.Securities.Option.StrategyMatcher.PredicateTargetValue enum.
        """
        ...

    def __init__(self, index: int, target: QuantConnect.Securities.Option.StrategyMatcher.PredicateTargetValue) -> None:
        """
        Initializes a new instance of the IOptionStrategyLegPredicateReferenceValue class
        
        :param index: The legs list index
        :param target: The property value being referenced
        """
        ...

    def Resolve(self, legs: System.Collections.Generic.IReadOnlyList[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition]) -> System.Object:
        """
        Resolves the value of the comparand specified in an OptionStrategyLegPredicate.
        For example, the predicate may include ... > legs[0].Strike, and upon evaluation, we need to
        be able to extract leg[0].Strike for the currently contemplated set of legs adhering to a
        strategy's definition.
        """
        ...


class UnmatchedPositionCountOptionStrategyMatchObjectiveFunction(System.Object, QuantConnect.Securities.Option.StrategyMatcher.IOptionStrategyMatchObjectiveFunction):
    """
    Provides an implementation of IOptionStrategyMatchObjectiveFunction that evaluates the number of unmatched
    positions, in number of contracts, giving precedence to solutions that have fewer unmatched contracts.
    """

    def ComputeScore(self, input: QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection, match: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyMatch, unmatched: QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection) -> float:
        """Computes the delta in matched vs unmatched positions, which gives precedence to solutions that match more contracts."""
        ...


class OptionStrategyDefinitions(System.Object):
    """
    Provides a listing of pre-defined OptionStrategyDefinition
    These definitions are blueprints for OptionStrategy instances.
    Factory functions for those can be found at OptionStrategies
    """

    AllDefinitions: System.Collections.Immutable.ImmutableList[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition]
    """Collection of all OptionStrategyDefinitions"""

    CoveredCall: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition
    """Hold 1 lot of the underlying and sell 1 call contract"""

    CoveredPut: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition
    """Hold -1 lot of the underlying and sell 1 put contract"""

    BearCallSpread: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition
    """
    Bear Call Spread strategy consists of two calls with the same expiration but different strikes.
    The strike price of the short call is below the strike of the long call. This is a credit spread.
    """

    BearPutSpread: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition
    """
    Bear Put Spread strategy consists of two puts with the same expiration but different strikes.
    The strike price of the short put is below the strike of the long put. This is a debit spread.
    """

    BullCallSpread: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition
    """
    Bull Call Spread strategy consists of two calls with the same expiration but different strikes.
    The strike price of the short call is higher than the strike of the long call. This is a debit spread.
    """

    BullPutSpread: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition
    """
    Method creates new Bull Put Spread strategy, that consists of two puts with the same expiration but
    different strikes. The strike price of the short put is above the strike of the long put. This is a
    credit spread.
    """

    Straddle: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition
    """
    Straddle strategy is a combination of buying a call and buying a put, both with the same strike price
    and expiration.
    """

    Strangle: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition
    """
    Strangle strategy consists of buying a call option and a put option with the same expiration date.
    The strike price of the call is above the strike of the put.
    """

    ButterflyCall: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition
    """
    Short Butterfly Call strategy consists of two short calls at a middle strike, and one long call each at a lower
    and upper strike. The upper and lower strikes must both be equidistant from the middle strike.
    """

    ShortButterflyCall: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition
    """
    Butterfly Call strategy consists of two long calls at a middle strike, and one short call each at a lower
    and upper strike. The upper and lower strikes must both be equidistant from the middle strike.
    """

    ButterflyPut: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition
    """
    Butterfly Put strategy consists of two short puts at a middle strike, and one long put each at a lower and
    upper strike. The upper and lower strikes must both be equidistant from the middle strike.
    """

    ShortButterflyPut: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition
    """
    Short Butterfly Put strategy consists of two long puts at a middle strike, and one short put each at a lower and
    upper strike. The upper and lower strikes must both be equidistant from the middle strike.
    """

    CallCalendarSpread: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition
    """
    Call Calendar Spread strategy is a short one call option and long a second call option with a more distant
    expiration.
    """

    PutCalendarSpread: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition
    """
    Put Calendar Spread strategy is a short one put option and long a second put option with a more distant
    expiration.
    """

    IronCondor: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition
    """
    Iron Condor strategy is buying a put, selling a put with a higher strike price, selling a call and buying a call with a higher strike price.
    All at the same expiration date
    """


class OptionStrategyMatcher(System.Object):
    """
    Matches OptionPositionCollection against a collection of OptionStrategyDefinition
    according to the OptionStrategyMatcherOptions provided.
    """

    @property
    def Options(self) -> QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyMatcherOptions:
        """Specifies options controlling how the matcher operates"""
        ...

    def __init__(self, options: QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyMatcherOptions) -> None:
        """
        Initializes a new instance of the OptionStrategyMatcher class
        
        :param options: Specifies definitions and other options controlling the matcher
        """
        ...

    def MatchOnce(self, positions: QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection) -> QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyMatch:
        ...


class ConstantOptionStrategyLegPredicateReferenceValue(typing.Generic[QuantConnect_Securities_Option_StrategyMatcher_ConstantOptionStrategyLegPredicateReferenceValue_T], System.Object, QuantConnect.Securities.Option.StrategyMatcher.IOptionStrategyLegPredicateReferenceValue):
    """Provides an implementation of IOptionStrategyLegPredicateReferenceValue that represents a constant value."""

    @property
    def Target(self) -> int:
        """
        Gets the target of this value
        
        This property contains the int value of a member of the QuantConnect.Securities.Option.StrategyMatcher.PredicateTargetValue enum.
        """
        ...

    def __init__(self, value: QuantConnect_Securities_Option_StrategyMatcher_ConstantOptionStrategyLegPredicateReferenceValue_T, target: QuantConnect.Securities.Option.StrategyMatcher.PredicateTargetValue) -> None:
        """
        Initializes a new instance of the ConstantOptionStrategyLegPredicateReferenceValue{T} class
        
        :param value: The constant reference value
        :param target: The value target in relation to the OptionPosition
        """
        ...

    def Resolve(self, legs: System.Collections.Generic.IReadOnlyList[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition]) -> System.Object:
        """Returns the constant value provided at initialization"""
        ...


class ConstantOptionStrategyLegReferenceValue(System.Object):
    """Provides methods for easily creating instances of ConstantOptionStrategyLegPredicateReferenceValue{T}"""

    @staticmethod
    def Create(value: typing.Any) -> QuantConnect.Securities.Option.StrategyMatcher.IOptionStrategyLegPredicateReferenceValue:
        """
        Creates a new instance of the ConstantOptionStrategyLegPredicateReferenceValue{T} class for
        the specified
        """
        ...


class DefaultOptionPositionCollectionEnumerator(System.Object, QuantConnect.Securities.Option.StrategyMatcher.IOptionPositionCollectionEnumerator):
    """Provides a default implementation of the IOptionPositionCollectionEnumerator abstraction."""

    def Enumerate(self, positions: QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition]:
        """Enumerates  according to its default enumerator implementation."""
        ...


class IdentityOptionStrategyDefinitionEnumerator(System.Object, QuantConnect.Securities.Option.StrategyMatcher.IOptionStrategyDefinitionEnumerator):
    """
    Provides a default implementation of IOptionStrategyDefinitionEnumerator that enumerates
    definitions according to the order that they were provided to OptionStrategyMatcherOptions
    """

    def Enumerate(self, definitions: System.Collections.Generic.IReadOnlyList[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition]) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition]:
        """Enumerates the  in the same order as provided."""
        ...


class DescendingByLegCountOptionStrategyDefinitionEnumerator(System.Object, QuantConnect.Securities.Option.StrategyMatcher.IOptionStrategyDefinitionEnumerator):
    """
    Provides an implementation of IOptionStrategyDefinitionEnumerator that enumerates definitions
    requiring more leg matches first. This ensures more complex definitions are evaluated before simpler definitions.
    """

    def Enumerate(self, definitions: System.Collections.Generic.IReadOnlyList[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition]) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionStrategyDefinition]:
        """Enumerates definitions in descending order of OptionStrategyDefinition.LegCount"""
        ...


class FunctionalOptionPositionCollectionEnumerator(System.Object, QuantConnect.Securities.Option.StrategyMatcher.IOptionPositionCollectionEnumerator):
    """Provides a functional implementation of IOptionPositionCollectionEnumerator"""

    def __init__(self, enumerate: typing.Callable[[QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection], System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition]]) -> None:
        """Initializes a new instance of the FunctionalOptionPositionCollectionEnumerator class"""
        ...

    def Enumerate(self, positions: QuantConnect.Securities.Option.StrategyMatcher.OptionPositionCollection) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Option.StrategyMatcher.OptionPosition]:
        """
        Enumerate the Option Positions Collection
        
        :param positions: The positions to enumerate on
        :returns: Enumerable of Option Positions.
        """
        ...


