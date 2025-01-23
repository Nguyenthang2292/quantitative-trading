from typing import overload
import abc
import typing

import System
import System.Collections
import System.Collections.Generic
import System.Collections.Immutable
import System.Linq

System_Linq_ImmutableArrayExtensions_Aggregate_T = typing.TypeVar("System_Linq_ImmutableArrayExtensions_Aggregate_T")
System_Linq_ImmutableArrayExtensions_Aggregate_TAccumulate = typing.TypeVar("System_Linq_ImmutableArrayExtensions_Aggregate_TAccumulate")
System_Linq_ImmutableArrayExtensions_Aggregate_TResult = typing.TypeVar("System_Linq_ImmutableArrayExtensions_Aggregate_TResult")
System_Linq_ImmutableArrayExtensions_ElementAt_T = typing.TypeVar("System_Linq_ImmutableArrayExtensions_ElementAt_T")
System_Linq_ImmutableArrayExtensions_ElementAtOrDefault_T = typing.TypeVar("System_Linq_ImmutableArrayExtensions_ElementAtOrDefault_T")
System_Linq_ImmutableArrayExtensions_First_T = typing.TypeVar("System_Linq_ImmutableArrayExtensions_First_T")
System_Linq_ImmutableArrayExtensions_FirstOrDefault_T = typing.TypeVar("System_Linq_ImmutableArrayExtensions_FirstOrDefault_T")
System_Linq_ImmutableArrayExtensions_Last_T = typing.TypeVar("System_Linq_ImmutableArrayExtensions_Last_T")
System_Linq_ImmutableArrayExtensions_LastOrDefault_T = typing.TypeVar("System_Linq_ImmutableArrayExtensions_LastOrDefault_T")
System_Linq_ImmutableArrayExtensions_Single_T = typing.TypeVar("System_Linq_ImmutableArrayExtensions_Single_T")
System_Linq_ImmutableArrayExtensions_SingleOrDefault_T = typing.TypeVar("System_Linq_ImmutableArrayExtensions_SingleOrDefault_T")
System_Linq_ImmutableArrayExtensions_Select_TResult = typing.TypeVar("System_Linq_ImmutableArrayExtensions_Select_TResult")
System_Linq_ImmutableArrayExtensions_Select_T = typing.TypeVar("System_Linq_ImmutableArrayExtensions_Select_T")
System_Linq_ImmutableArrayExtensions_SelectMany_TResult = typing.TypeVar("System_Linq_ImmutableArrayExtensions_SelectMany_TResult")
System_Linq_ImmutableArrayExtensions_SelectMany_TSource = typing.TypeVar("System_Linq_ImmutableArrayExtensions_SelectMany_TSource")
System_Linq_ImmutableArrayExtensions_SelectMany_TCollection = typing.TypeVar("System_Linq_ImmutableArrayExtensions_SelectMany_TCollection")
System_Linq_ImmutableArrayExtensions_Where_T = typing.TypeVar("System_Linq_ImmutableArrayExtensions_Where_T")
System_Linq_ImmutableArrayExtensions_Any_T = typing.TypeVar("System_Linq_ImmutableArrayExtensions_Any_T")
System_Linq_ImmutableArrayExtensions_All_T = typing.TypeVar("System_Linq_ImmutableArrayExtensions_All_T")
System_Linq_ImmutableArrayExtensions_SequenceEqual_TBase = typing.TypeVar("System_Linq_ImmutableArrayExtensions_SequenceEqual_TBase")
System_Linq_ImmutableArrayExtensions_SequenceEqual_TDerived = typing.TypeVar("System_Linq_ImmutableArrayExtensions_SequenceEqual_TDerived")
System_Linq_ImmutableArrayExtensions_ToDictionary_TKey = typing.TypeVar("System_Linq_ImmutableArrayExtensions_ToDictionary_TKey")
System_Linq_ImmutableArrayExtensions_ToDictionary_T = typing.TypeVar("System_Linq_ImmutableArrayExtensions_ToDictionary_T")
System_Linq_ImmutableArrayExtensions_ToDictionary_TElement = typing.TypeVar("System_Linq_ImmutableArrayExtensions_ToDictionary_TElement")
System_Linq_ImmutableArrayExtensions_ToArray_T = typing.TypeVar("System_Linq_ImmutableArrayExtensions_ToArray_T")
System_Linq_Enumerable_DefaultIfEmpty_TSource = typing.TypeVar("System_Linq_Enumerable_DefaultIfEmpty_TSource")
System_Linq_Enumerable_Append_TSource = typing.TypeVar("System_Linq_Enumerable_Append_TSource")
System_Linq_Enumerable_Prepend_TSource = typing.TypeVar("System_Linq_Enumerable_Prepend_TSource")
System_Linq_Enumerable_First_TSource = typing.TypeVar("System_Linq_Enumerable_First_TSource")
System_Linq_Enumerable_FirstOrDefault_TSource = typing.TypeVar("System_Linq_Enumerable_FirstOrDefault_TSource")
System_Linq_Enumerable_Repeat_TResult = typing.TypeVar("System_Linq_Enumerable_Repeat_TResult")
System_Linq_Enumerable_Last_TSource = typing.TypeVar("System_Linq_Enumerable_Last_TSource")
System_Linq_Enumerable_LastOrDefault_TSource = typing.TypeVar("System_Linq_Enumerable_LastOrDefault_TSource")
System_Linq_Enumerable_Single_TSource = typing.TypeVar("System_Linq_Enumerable_Single_TSource")
System_Linq_Enumerable_SingleOrDefault_TSource = typing.TypeVar("System_Linq_Enumerable_SingleOrDefault_TSource")
System_Linq_Enumerable_Contains_TSource = typing.TypeVar("System_Linq_Enumerable_Contains_TSource")
System_Linq_Enumerable_Max_TSource = typing.TypeVar("System_Linq_Enumerable_Max_TSource")
System_Linq_Enumerable_MaxBy_TSource = typing.TypeVar("System_Linq_Enumerable_MaxBy_TSource")
System_Linq_Enumerable_Max_TResult = typing.TypeVar("System_Linq_Enumerable_Max_TResult")
System_Linq_Enumerable_Min_TSource = typing.TypeVar("System_Linq_Enumerable_Min_TSource")
System_Linq_Enumerable_MinBy_TSource = typing.TypeVar("System_Linq_Enumerable_MinBy_TSource")
System_Linq_Enumerable_Min_TResult = typing.TypeVar("System_Linq_Enumerable_Min_TResult")
System_Linq_Enumerable_Aggregate_TSource = typing.TypeVar("System_Linq_Enumerable_Aggregate_TSource")
System_Linq_Enumerable_Aggregate_TAccumulate = typing.TypeVar("System_Linq_Enumerable_Aggregate_TAccumulate")
System_Linq_Enumerable_Aggregate_TResult = typing.TypeVar("System_Linq_Enumerable_Aggregate_TResult")
System_Linq_Enumerable_ElementAt_TSource = typing.TypeVar("System_Linq_Enumerable_ElementAt_TSource")
System_Linq_Enumerable_ElementAtOrDefault_TSource = typing.TypeVar("System_Linq_Enumerable_ElementAtOrDefault_TSource")
System_Linq_Enumerable_Concat_TSource = typing.TypeVar("System_Linq_Enumerable_Concat_TSource")
System_Linq_Enumerable_SelectMany_TResult = typing.TypeVar("System_Linq_Enumerable_SelectMany_TResult")
System_Linq_Enumerable_SelectMany_TSource = typing.TypeVar("System_Linq_Enumerable_SelectMany_TSource")
System_Linq_Enumerable_SelectMany_TCollection = typing.TypeVar("System_Linq_Enumerable_SelectMany_TCollection")
System_Linq_Enumerable_CreateSelectIPartitionIterator_TSource = typing.TypeVar("System_Linq_Enumerable_CreateSelectIPartitionIterator_TSource")
System_Linq_Enumerable_CreateSelectIPartitionIterator_TResult = typing.TypeVar("System_Linq_Enumerable_CreateSelectIPartitionIterator_TResult")
System_Linq_Enumerable_Skip_TSource = typing.TypeVar("System_Linq_Enumerable_Skip_TSource")
System_Linq_Enumerable_SkipWhile_TSource = typing.TypeVar("System_Linq_Enumerable_SkipWhile_TSource")
System_Linq_Enumerable_SkipLast_TSource = typing.TypeVar("System_Linq_Enumerable_SkipLast_TSource")
System_Linq_Enumerable_Take_TSource = typing.TypeVar("System_Linq_Enumerable_Take_TSource")
System_Linq_Enumerable_TakeWhile_TSource = typing.TypeVar("System_Linq_Enumerable_TakeWhile_TSource")
System_Linq_Enumerable_TakeLast_TSource = typing.TypeVar("System_Linq_Enumerable_TakeLast_TSource")
System_Linq_Enumerable_Except_TSource = typing.TypeVar("System_Linq_Enumerable_Except_TSource")
System_Linq_Enumerable_ExceptBy_TSource = typing.TypeVar("System_Linq_Enumerable_ExceptBy_TSource")
System_Linq_Enumerable_ExceptBy_TKey = typing.TypeVar("System_Linq_Enumerable_ExceptBy_TKey")
System_Linq_Enumerable_AsEnumerable_TSource = typing.TypeVar("System_Linq_Enumerable_AsEnumerable_TSource")
System_Linq_Enumerable_Count_TSource = typing.TypeVar("System_Linq_Enumerable_Count_TSource")
System_Linq_Enumerable_TryGetNonEnumeratedCount_TSource = typing.TypeVar("System_Linq_Enumerable_TryGetNonEnumeratedCount_TSource")
System_Linq_Enumerable_LongCount_TSource = typing.TypeVar("System_Linq_Enumerable_LongCount_TSource")
System_Linq_Enumerable_Empty_TResult = typing.TypeVar("System_Linq_Enumerable_Empty_TResult")
System_Linq_Enumerable_Reverse_TSource = typing.TypeVar("System_Linq_Enumerable_Reverse_TSource")
System_Linq_Enumerable_Distinct_TSource = typing.TypeVar("System_Linq_Enumerable_Distinct_TSource")
System_Linq_Enumerable_DistinctBy_TSource = typing.TypeVar("System_Linq_Enumerable_DistinctBy_TSource")
System_Linq_Enumerable_DistinctBy_TKey = typing.TypeVar("System_Linq_Enumerable_DistinctBy_TKey")
System_Linq_Enumerable_Intersect_TSource = typing.TypeVar("System_Linq_Enumerable_Intersect_TSource")
System_Linq_Enumerable_IntersectBy_TSource = typing.TypeVar("System_Linq_Enumerable_IntersectBy_TSource")
System_Linq_Enumerable_IntersectBy_TKey = typing.TypeVar("System_Linq_Enumerable_IntersectBy_TKey")
System_Linq_Enumerable_MaxBy_TKey = typing.TypeVar("System_Linq_Enumerable_MaxBy_TKey")
System_Linq_Enumerable_GroupJoin_TResult = typing.TypeVar("System_Linq_Enumerable_GroupJoin_TResult")
System_Linq_Enumerable_GroupJoin_TOuter = typing.TypeVar("System_Linq_Enumerable_GroupJoin_TOuter")
System_Linq_Enumerable_GroupJoin_TInner = typing.TypeVar("System_Linq_Enumerable_GroupJoin_TInner")
System_Linq_Enumerable_GroupJoin_TKey = typing.TypeVar("System_Linq_Enumerable_GroupJoin_TKey")
System_Linq_Enumerable_Where_TSource = typing.TypeVar("System_Linq_Enumerable_Where_TSource")
System_Linq_Enumerable_ToLookup_TKey = typing.TypeVar("System_Linq_Enumerable_ToLookup_TKey")
System_Linq_Enumerable_ToLookup_TSource = typing.TypeVar("System_Linq_Enumerable_ToLookup_TSource")
System_Linq_Enumerable_ToLookup_TElement = typing.TypeVar("System_Linq_Enumerable_ToLookup_TElement")
System_Linq_Enumerable_Chunk_TSource = typing.TypeVar("System_Linq_Enumerable_Chunk_TSource")
System_Linq_Enumerable_Order_T = typing.TypeVar("System_Linq_Enumerable_Order_T")
System_Linq_Enumerable_OrderBy_TSource = typing.TypeVar("System_Linq_Enumerable_OrderBy_TSource")
System_Linq_Enumerable_OrderBy_TKey = typing.TypeVar("System_Linq_Enumerable_OrderBy_TKey")
System_Linq_Enumerable_OrderDescending_T = typing.TypeVar("System_Linq_Enumerable_OrderDescending_T")
System_Linq_Enumerable_OrderByDescending_TSource = typing.TypeVar("System_Linq_Enumerable_OrderByDescending_TSource")
System_Linq_Enumerable_OrderByDescending_TKey = typing.TypeVar("System_Linq_Enumerable_OrderByDescending_TKey")
System_Linq_Enumerable_ThenBy_TSource = typing.TypeVar("System_Linq_Enumerable_ThenBy_TSource")
System_Linq_Enumerable_ThenBy_TKey = typing.TypeVar("System_Linq_Enumerable_ThenBy_TKey")
System_Linq_Enumerable_ThenByDescending_TSource = typing.TypeVar("System_Linq_Enumerable_ThenByDescending_TSource")
System_Linq_Enumerable_ThenByDescending_TKey = typing.TypeVar("System_Linq_Enumerable_ThenByDescending_TKey")
System_Linq_Enumerable_MinBy_TKey = typing.TypeVar("System_Linq_Enumerable_MinBy_TKey")
System_Linq_Enumerable_OfType_TResult = typing.TypeVar("System_Linq_Enumerable_OfType_TResult")
System_Linq_Enumerable_Cast_TResult = typing.TypeVar("System_Linq_Enumerable_Cast_TResult")
System_Linq_Enumerable_Average_TSource = typing.TypeVar("System_Linq_Enumerable_Average_TSource")
System_Linq_Enumerable_Sum_TSource = typing.TypeVar("System_Linq_Enumerable_Sum_TSource")
System_Linq_Enumerable_Join_TResult = typing.TypeVar("System_Linq_Enumerable_Join_TResult")
System_Linq_Enumerable_Join_TOuter = typing.TypeVar("System_Linq_Enumerable_Join_TOuter")
System_Linq_Enumerable_Join_TInner = typing.TypeVar("System_Linq_Enumerable_Join_TInner")
System_Linq_Enumerable_Join_TKey = typing.TypeVar("System_Linq_Enumerable_Join_TKey")
System_Linq_Enumerable_Any_TSource = typing.TypeVar("System_Linq_Enumerable_Any_TSource")
System_Linq_Enumerable_All_TSource = typing.TypeVar("System_Linq_Enumerable_All_TSource")
System_Linq_Enumerable_Zip_TResult = typing.TypeVar("System_Linq_Enumerable_Zip_TResult")
System_Linq_Enumerable_Zip_TFirst = typing.TypeVar("System_Linq_Enumerable_Zip_TFirst")
System_Linq_Enumerable_Zip_TSecond = typing.TypeVar("System_Linq_Enumerable_Zip_TSecond")
System_Linq_Enumerable_Zip_TThird = typing.TypeVar("System_Linq_Enumerable_Zip_TThird")
System_Linq_Enumerable_Select_TResult = typing.TypeVar("System_Linq_Enumerable_Select_TResult")
System_Linq_Enumerable_Select_TSource = typing.TypeVar("System_Linq_Enumerable_Select_TSource")
System_Linq_Enumerable_GroupBy_TSource = typing.TypeVar("System_Linq_Enumerable_GroupBy_TSource")
System_Linq_Enumerable_GroupBy_TKey = typing.TypeVar("System_Linq_Enumerable_GroupBy_TKey")
System_Linq_Enumerable_GroupBy_TElement = typing.TypeVar("System_Linq_Enumerable_GroupBy_TElement")
System_Linq_Enumerable_GroupBy_TResult = typing.TypeVar("System_Linq_Enumerable_GroupBy_TResult")
System_Linq_Enumerable_Union_TSource = typing.TypeVar("System_Linq_Enumerable_Union_TSource")
System_Linq_Enumerable_UnionBy_TSource = typing.TypeVar("System_Linq_Enumerable_UnionBy_TSource")
System_Linq_Enumerable_UnionBy_TKey = typing.TypeVar("System_Linq_Enumerable_UnionBy_TKey")
System_Linq_Enumerable_ToArray_TSource = typing.TypeVar("System_Linq_Enumerable_ToArray_TSource")
System_Linq_Enumerable_ToList_TSource = typing.TypeVar("System_Linq_Enumerable_ToList_TSource")
System_Linq_Enumerable_ToDictionary_TKey = typing.TypeVar("System_Linq_Enumerable_ToDictionary_TKey")
System_Linq_Enumerable_ToDictionary_TSource = typing.TypeVar("System_Linq_Enumerable_ToDictionary_TSource")
System_Linq_Enumerable_ToDictionary_TElement = typing.TypeVar("System_Linq_Enumerable_ToDictionary_TElement")
System_Linq_Enumerable_ToHashSet_TSource = typing.TypeVar("System_Linq_Enumerable_ToHashSet_TSource")
System_Linq_Enumerable_SequenceEqual_TSource = typing.TypeVar("System_Linq_Enumerable_SequenceEqual_TSource")
System_Linq_Lookup_TKey = typing.TypeVar("System_Linq_Lookup_TKey")
System_Linq_Lookup_TElement = typing.TypeVar("System_Linq_Lookup_TElement")
System_Linq_Lookup_ApplyResultSelector_TResult = typing.TypeVar("System_Linq_Lookup_ApplyResultSelector_TResult")
System_Linq_ILookup_TKey = typing.TypeVar("System_Linq_ILookup_TKey")
System_Linq_ILookup_TElement = typing.TypeVar("System_Linq_ILookup_TElement")
System_Linq_IOrderedEnumerable_TElement = typing.TypeVar("System_Linq_IOrderedEnumerable_TElement")
System_Linq_IOrderedEnumerable_CreateOrderedEnumerable_TKey = typing.TypeVar("System_Linq_IOrderedEnumerable_CreateOrderedEnumerable_TKey")
System_Linq_IGrouping_TKey = typing.TypeVar("System_Linq_IGrouping_TKey")
System_Linq_IGrouping_TElement = typing.TypeVar("System_Linq_IGrouping_TElement")
System_Linq_Grouping_TKey = typing.TypeVar("System_Linq_Grouping_TKey")
System_Linq_Grouping_TElement = typing.TypeVar("System_Linq_Grouping_TElement")


class ImmutableArrayExtensions(System.Object):
    """LINQ extension method overrides that offer greater efficiency for ImmutableArray{T} than the standard LINQ methods"""

    @staticmethod
    @overload
    def Aggregate(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_Aggregate_T], func: typing.Callable[[System_Linq_ImmutableArrayExtensions_Aggregate_T, System_Linq_ImmutableArrayExtensions_Aggregate_T], System_Linq_ImmutableArrayExtensions_Aggregate_T]) -> System_Linq_ImmutableArrayExtensions_Aggregate_T:
        """Applies an accumulator function over a sequence."""
        ...

    @staticmethod
    @overload
    def Aggregate(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_Aggregate_T], seed: System_Linq_ImmutableArrayExtensions_Aggregate_TAccumulate, func: typing.Callable[[System_Linq_ImmutableArrayExtensions_Aggregate_TAccumulate, System_Linq_ImmutableArrayExtensions_Aggregate_T], System_Linq_ImmutableArrayExtensions_Aggregate_TAccumulate]) -> System_Linq_ImmutableArrayExtensions_Aggregate_TAccumulate:
        """Applies an accumulator function over a sequence."""
        ...

    @staticmethod
    @overload
    def Aggregate(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_Aggregate_T], seed: System_Linq_ImmutableArrayExtensions_Aggregate_TAccumulate, func: typing.Callable[[System_Linq_ImmutableArrayExtensions_Aggregate_TAccumulate, System_Linq_ImmutableArrayExtensions_Aggregate_T], System_Linq_ImmutableArrayExtensions_Aggregate_TAccumulate], resultSelector: typing.Callable[[System_Linq_ImmutableArrayExtensions_Aggregate_TAccumulate], System_Linq_ImmutableArrayExtensions_Aggregate_TResult]) -> System_Linq_ImmutableArrayExtensions_Aggregate_TResult:
        """
        Applies an accumulator function over a sequence.
        
        :param immutableArray: An immutable array to aggregate over.
        :param seed: The initial accumulator value.
        :param func: An accumulator function to be invoked on each element.
        :param resultSelector: A function to transform the final accumulator value into the result type.
        """
        ...

    @staticmethod
    def All(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_All_T], predicate: typing.Callable[[System_Linq_ImmutableArrayExtensions_All_T], bool]) -> bool:
        """
        Gets a value indicating whether all elements in this collection
        match a given condition.
        
        :param predicate: The predicate.
        :returns: true if every element of the source sequence passes the test in the specified predicate, or if the sequence is empty; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def Any(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_Any_T]) -> bool:
        """Gets a value indicating whether any elements are in this collection."""
        ...

    @staticmethod
    @overload
    def Any(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_Any_T], predicate: typing.Callable[[System_Linq_ImmutableArrayExtensions_Any_T], bool]) -> bool:
        """
        Gets a value indicating whether any elements are in this collection
        that match a given condition.
        
        :param predicate: The predicate.
        """
        ...

    @staticmethod
    @overload
    def Any(builder: System.Collections.Immutable.ImmutableArray.Builder) -> bool:
        """Returns a value indicating whether this collection contains any elements."""
        ...

    @staticmethod
    def ElementAt(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_ElementAt_T], index: int) -> System_Linq_ImmutableArrayExtensions_ElementAt_T:
        """Returns the element at a specified index in a sequence."""
        ...

    @staticmethod
    def ElementAtOrDefault(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_ElementAtOrDefault_T], index: int) -> System_Linq_ImmutableArrayExtensions_ElementAtOrDefault_T:
        """Returns the element at a specified index in a sequence or a default value if the index is out of range."""
        ...

    @staticmethod
    @overload
    def First(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_First_T], predicate: typing.Callable[[System_Linq_ImmutableArrayExtensions_First_T], bool]) -> System_Linq_ImmutableArrayExtensions_First_T:
        """Returns the first element in a sequence that satisfies a specified condition."""
        ...

    @staticmethod
    @overload
    def First(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_First_T]) -> System_Linq_ImmutableArrayExtensions_First_T:
        """Returns the first element in a sequence that satisfies a specified condition."""
        ...

    @staticmethod
    @overload
    def First(builder: System.Collections.Immutable.ImmutableArray.Builder) -> System_Linq_ImmutableArrayExtensions_First_T:
        ...

    @staticmethod
    @overload
    def FirstOrDefault(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_FirstOrDefault_T]) -> System_Linq_ImmutableArrayExtensions_FirstOrDefault_T:
        """Returns the first element of a sequence, or a default value if the sequence contains no elements."""
        ...

    @staticmethod
    @overload
    def FirstOrDefault(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_FirstOrDefault_T], predicate: typing.Callable[[System_Linq_ImmutableArrayExtensions_FirstOrDefault_T], bool]) -> System_Linq_ImmutableArrayExtensions_FirstOrDefault_T:
        """Returns the first element of the sequence that satisfies a condition or a default value if no such element is found."""
        ...

    @staticmethod
    @overload
    def FirstOrDefault(builder: System.Collections.Immutable.ImmutableArray.Builder) -> System_Linq_ImmutableArrayExtensions_FirstOrDefault_T:
        """Returns the first element in the collection, or the default value if the collection is empty."""
        ...

    @staticmethod
    @overload
    def Last(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_Last_T]) -> System_Linq_ImmutableArrayExtensions_Last_T:
        """Returns the last element of a sequence."""
        ...

    @staticmethod
    @overload
    def Last(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_Last_T], predicate: typing.Callable[[System_Linq_ImmutableArrayExtensions_Last_T], bool]) -> System_Linq_ImmutableArrayExtensions_Last_T:
        """Returns the last element of a sequence that satisfies a specified condition."""
        ...

    @staticmethod
    @overload
    def Last(builder: System.Collections.Immutable.ImmutableArray.Builder) -> System_Linq_ImmutableArrayExtensions_Last_T:
        """Returns the last element in the collection."""
        ...

    @staticmethod
    @overload
    def LastOrDefault(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_LastOrDefault_T]) -> System_Linq_ImmutableArrayExtensions_LastOrDefault_T:
        """Returns the last element of a sequence, or a default value if the sequence contains no elements."""
        ...

    @staticmethod
    @overload
    def LastOrDefault(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_LastOrDefault_T], predicate: typing.Callable[[System_Linq_ImmutableArrayExtensions_LastOrDefault_T], bool]) -> System_Linq_ImmutableArrayExtensions_LastOrDefault_T:
        """Returns the last element of a sequence that satisfies a condition or a default value if no such element is found."""
        ...

    @staticmethod
    @overload
    def LastOrDefault(builder: System.Collections.Immutable.ImmutableArray.Builder) -> System_Linq_ImmutableArrayExtensions_LastOrDefault_T:
        """Returns the last element in the collection, or the default value if the collection is empty."""
        ...

    @staticmethod
    def Select(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_Select_T], selector: typing.Callable[[System_Linq_ImmutableArrayExtensions_Select_T], System_Linq_ImmutableArrayExtensions_Select_TResult]) -> System.Collections.Generic.IEnumerable[System_Linq_ImmutableArrayExtensions_Select_TResult]:
        ...

    @staticmethod
    def SelectMany(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_SelectMany_TSource], collectionSelector: typing.Callable[[System_Linq_ImmutableArrayExtensions_SelectMany_TSource], System.Collections.Generic.IEnumerable[System_Linq_ImmutableArrayExtensions_SelectMany_TCollection]], resultSelector: typing.Callable[[System_Linq_ImmutableArrayExtensions_SelectMany_TSource, System_Linq_ImmutableArrayExtensions_SelectMany_TCollection], System_Linq_ImmutableArrayExtensions_SelectMany_TResult]) -> System.Collections.Generic.IEnumerable[System_Linq_ImmutableArrayExtensions_SelectMany_TResult]:
        """
        Projects each element of a sequence to an IEnumerable{T},
        flattens the resulting sequences into one sequence, and invokes a result
        selector function on each element therein.
        
        :param immutableArray: The immutable array.
        :param collectionSelector: A transform function to apply to each element of the input sequence.
        :param resultSelector: A transform function to apply to each element of the intermediate sequence.
        :returns: An IEnumerable{T} whose elements are the result of invoking the one-to-many transform function  on each element of  and then mapping each of those sequence elements and their corresponding source element to a result element.
        """
        ...

    @staticmethod
    @overload
    def SequenceEqual(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_SequenceEqual_TBase], items: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_SequenceEqual_TDerived], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_ImmutableArrayExtensions_SequenceEqual_TBase] = None) -> bool:
        """Determines whether two sequences are equal according to an equality comparer."""
        ...

    @staticmethod
    @overload
    def SequenceEqual(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_SequenceEqual_TBase], items: System.Collections.Generic.IEnumerable[System_Linq_ImmutableArrayExtensions_SequenceEqual_TDerived], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_ImmutableArrayExtensions_SequenceEqual_TBase] = None) -> bool:
        """Determines whether two sequences are equal according to an equality comparer."""
        ...

    @staticmethod
    @overload
    def SequenceEqual(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_SequenceEqual_TBase], items: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_SequenceEqual_TDerived], predicate: typing.Callable[[System_Linq_ImmutableArrayExtensions_SequenceEqual_TBase, System_Linq_ImmutableArrayExtensions_SequenceEqual_TBase], bool]) -> bool:
        """Determines whether two sequences are equal according to an equality comparer."""
        ...

    @staticmethod
    @overload
    def Single(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_Single_T]) -> System_Linq_ImmutableArrayExtensions_Single_T:
        """Returns the only element of a sequence, and throws an exception if there is not exactly one element in the sequence."""
        ...

    @staticmethod
    @overload
    def Single(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_Single_T], predicate: typing.Callable[[System_Linq_ImmutableArrayExtensions_Single_T], bool]) -> System_Linq_ImmutableArrayExtensions_Single_T:
        """
        Returns the only element of a sequence that satisfies a specified condition, and throws an exception if more than one such element exists.
        
        :param immutableArray: The immutable array to return a single element from.
        :param predicate: The function to test whether an element should be returned.
        """
        ...

    @staticmethod
    @overload
    def SingleOrDefault(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_SingleOrDefault_T]) -> System_Linq_ImmutableArrayExtensions_SingleOrDefault_T:
        """Returns the only element of a sequence, or a default value if the sequence is empty; this method throws an exception if there is more than one element in the sequence."""
        ...

    @staticmethod
    @overload
    def SingleOrDefault(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_SingleOrDefault_T], predicate: typing.Callable[[System_Linq_ImmutableArrayExtensions_SingleOrDefault_T], bool]) -> System_Linq_ImmutableArrayExtensions_SingleOrDefault_T:
        """Returns the only element of a sequence that satisfies a specified condition or a default value if no such element exists; this method throws an exception if more than one element satisfies the condition."""
        ...

    @staticmethod
    def ToArray(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_ToArray_T]) -> typing.List[System_Linq_ImmutableArrayExtensions_ToArray_T]:
        """
        Copies the contents of this array to a mutable array.
        
        :param immutableArray: The immutable array to copy into a mutable one.
        :returns: The newly instantiated array.
        """
        ...

    @staticmethod
    @overload
    def ToDictionary(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_ToDictionary_T], keySelector: typing.Callable[[System_Linq_ImmutableArrayExtensions_ToDictionary_T], System_Linq_ImmutableArrayExtensions_ToDictionary_TKey]) -> System.Collections.Generic.Dictionary[System_Linq_ImmutableArrayExtensions_ToDictionary_TKey, System_Linq_ImmutableArrayExtensions_ToDictionary_T]:
        """
        Creates a dictionary based on the contents of this array.
        
        :param keySelector: The key selector.
        :returns: The newly initialized dictionary.
        """
        ...

    @staticmethod
    @overload
    def ToDictionary(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_ToDictionary_T], keySelector: typing.Callable[[System_Linq_ImmutableArrayExtensions_ToDictionary_T], System_Linq_ImmutableArrayExtensions_ToDictionary_TKey], elementSelector: typing.Callable[[System_Linq_ImmutableArrayExtensions_ToDictionary_T], System_Linq_ImmutableArrayExtensions_ToDictionary_TElement]) -> System.Collections.Generic.Dictionary[System_Linq_ImmutableArrayExtensions_ToDictionary_TKey, System_Linq_ImmutableArrayExtensions_ToDictionary_TElement]:
        """
        Creates a dictionary based on the contents of this array.
        
        :param keySelector: The key selector.
        :param elementSelector: The element selector.
        :returns: The newly initialized dictionary.
        """
        ...

    @staticmethod
    @overload
    def ToDictionary(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_ToDictionary_T], keySelector: typing.Callable[[System_Linq_ImmutableArrayExtensions_ToDictionary_T], System_Linq_ImmutableArrayExtensions_ToDictionary_TKey], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_ImmutableArrayExtensions_ToDictionary_TKey]) -> System.Collections.Generic.Dictionary[System_Linq_ImmutableArrayExtensions_ToDictionary_TKey, System_Linq_ImmutableArrayExtensions_ToDictionary_T]:
        """
        Creates a dictionary based on the contents of this array.
        
        :param keySelector: The key selector.
        :param comparer: The comparer to initialize the dictionary with.
        :returns: The newly initialized dictionary.
        """
        ...

    @staticmethod
    @overload
    def ToDictionary(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_ToDictionary_T], keySelector: typing.Callable[[System_Linq_ImmutableArrayExtensions_ToDictionary_T], System_Linq_ImmutableArrayExtensions_ToDictionary_TKey], elementSelector: typing.Callable[[System_Linq_ImmutableArrayExtensions_ToDictionary_T], System_Linq_ImmutableArrayExtensions_ToDictionary_TElement], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_ImmutableArrayExtensions_ToDictionary_TKey]) -> System.Collections.Generic.Dictionary[System_Linq_ImmutableArrayExtensions_ToDictionary_TKey, System_Linq_ImmutableArrayExtensions_ToDictionary_TElement]:
        """
        Creates a dictionary based on the contents of this array.
        
        :param keySelector: The key selector.
        :param elementSelector: The element selector.
        :param comparer: The comparer to initialize the dictionary with.
        :returns: The newly initialized dictionary.
        """
        ...

    @staticmethod
    def Where(immutableArray: System.Collections.Immutable.ImmutableArray[System_Linq_ImmutableArrayExtensions_Where_T], predicate: typing.Callable[[System_Linq_ImmutableArrayExtensions_Where_T], bool]) -> System.Collections.Generic.IEnumerable[System_Linq_ImmutableArrayExtensions_Where_T]:
        """Filters a sequence of values based on a predicate."""
        ...


class ILookup(typing.Generic[System_Linq_ILookup_TKey, System_Linq_ILookup_TElement], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def Count(self) -> int:
        ...

    def __getitem__(self, key: System_Linq_ILookup_TKey) -> System.Collections.Generic.IEnumerable[System_Linq_ILookup_TElement]:
        ...

    def Contains(self, key: System_Linq_ILookup_TKey) -> bool:
        ...


class IOrderedEnumerable(typing.Generic[System_Linq_IOrderedEnumerable_TElement], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def CreateOrderedEnumerable(self, keySelector: typing.Callable[[System_Linq_IOrderedEnumerable_TElement], System_Linq_IOrderedEnumerable_CreateOrderedEnumerable_TKey], comparer: System.Collections.Generic.IComparer[System_Linq_IOrderedEnumerable_CreateOrderedEnumerable_TKey], descending: bool) -> System.Linq.IOrderedEnumerable[System_Linq_IOrderedEnumerable_TElement]:
        ...


class IGrouping(typing.Generic[System_Linq_IGrouping_TKey, System_Linq_IGrouping_TElement], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def Key(self) -> System_Linq_IGrouping_TKey:
        ...


class Enumerable(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def Aggregate(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Aggregate_TSource], func: typing.Callable[[System_Linq_Enumerable_Aggregate_TSource, System_Linq_Enumerable_Aggregate_TSource], System_Linq_Enumerable_Aggregate_TSource]) -> System_Linq_Enumerable_Aggregate_TSource:
        ...

    @staticmethod
    @overload
    def Aggregate(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Aggregate_TSource], seed: System_Linq_Enumerable_Aggregate_TAccumulate, func: typing.Callable[[System_Linq_Enumerable_Aggregate_TAccumulate, System_Linq_Enumerable_Aggregate_TSource], System_Linq_Enumerable_Aggregate_TAccumulate]) -> System_Linq_Enumerable_Aggregate_TAccumulate:
        ...

    @staticmethod
    @overload
    def Aggregate(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Aggregate_TSource], seed: System_Linq_Enumerable_Aggregate_TAccumulate, func: typing.Callable[[System_Linq_Enumerable_Aggregate_TAccumulate, System_Linq_Enumerable_Aggregate_TSource], System_Linq_Enumerable_Aggregate_TAccumulate], resultSelector: typing.Callable[[System_Linq_Enumerable_Aggregate_TAccumulate], System_Linq_Enumerable_Aggregate_TResult]) -> System_Linq_Enumerable_Aggregate_TResult:
        ...

    @staticmethod
    def All(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_All_TSource], predicate: typing.Callable[[System_Linq_Enumerable_All_TSource], bool]) -> bool:
        ...

    @staticmethod
    @overload
    def Any(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Any_TSource]) -> bool:
        ...

    @staticmethod
    @overload
    def Any(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Any_TSource], predicate: typing.Callable[[System_Linq_Enumerable_Any_TSource], bool]) -> bool:
        ...

    @staticmethod
    def Append(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Append_TSource], element: System_Linq_Enumerable_Append_TSource) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Append_TSource]:
        ...

    @staticmethod
    def AsEnumerable(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_AsEnumerable_TSource]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_AsEnumerable_TSource]:
        ...

    @staticmethod
    @overload
    def Average(source: System.Collections.Generic.IEnumerable[int]) -> float:
        ...

    @staticmethod
    @overload
    def Average(source: System.Collections.Generic.IEnumerable[int]) -> float:
        ...

    @staticmethod
    @overload
    def Average(source: System.Collections.Generic.IEnumerable[float]) -> float:
        ...

    @staticmethod
    @overload
    def Average(source: System.Collections.Generic.IEnumerable[float]) -> float:
        ...

    @staticmethod
    @overload
    def Average(source: System.Collections.Generic.IEnumerable[float]) -> float:
        ...

    @staticmethod
    @overload
    def Average(source: System.Collections.Generic.IEnumerable[typing.Optional[int]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Average(source: System.Collections.Generic.IEnumerable[typing.Optional[int]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Average(source: System.Collections.Generic.IEnumerable[typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Average(source: System.Collections.Generic.IEnumerable[typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Average(source: System.Collections.Generic.IEnumerable[typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Average(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Average_TSource], selector: typing.Callable[[System_Linq_Enumerable_Average_TSource], int]) -> float:
        ...

    @staticmethod
    @overload
    def Average(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Average_TSource], selector: typing.Callable[[System_Linq_Enumerable_Average_TSource], int]) -> float:
        ...

    @staticmethod
    @overload
    def Average(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Average_TSource], selector: typing.Callable[[System_Linq_Enumerable_Average_TSource], float]) -> float:
        ...

    @staticmethod
    @overload
    def Average(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Average_TSource], selector: typing.Callable[[System_Linq_Enumerable_Average_TSource], float]) -> float:
        ...

    @staticmethod
    @overload
    def Average(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Average_TSource], selector: typing.Callable[[System_Linq_Enumerable_Average_TSource], float]) -> float:
        ...

    @staticmethod
    @overload
    def Average(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Average_TSource], selector: typing.Callable[[System_Linq_Enumerable_Average_TSource], typing.Optional[int]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Average(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Average_TSource], selector: typing.Callable[[System_Linq_Enumerable_Average_TSource], typing.Optional[int]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Average(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Average_TSource], selector: typing.Callable[[System_Linq_Enumerable_Average_TSource], typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Average(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Average_TSource], selector: typing.Callable[[System_Linq_Enumerable_Average_TSource], typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Average(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Average_TSource], selector: typing.Callable[[System_Linq_Enumerable_Average_TSource], typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    def Cast(source: System.Collections.IEnumerable) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Cast_TResult]:
        ...

    @staticmethod
    def Chunk(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Chunk_TSource], size: int) -> System.Collections.Generic.IEnumerable[typing.List[System_Linq_Enumerable_Chunk_TSource]]:
        """
        Split the elements of a sequence into chunks of size at most .
        
        :param source: An IEnumerable{T} whose elements to chunk.
        :param size: Maximum size of each chunk.
        :returns: An IEnumerable{T} that contains the elements the input sequence split into chunks of size .
        """
        ...

    @staticmethod
    def Concat(first: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Concat_TSource], second: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Concat_TSource]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Concat_TSource]:
        ...

    @staticmethod
    @overload
    def Contains(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Contains_TSource], value: System_Linq_Enumerable_Contains_TSource) -> bool:
        ...

    @staticmethod
    @overload
    def Contains(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Contains_TSource], value: System_Linq_Enumerable_Contains_TSource, comparer: System.Collections.Generic.IEqualityComparer[System_Linq_Enumerable_Contains_TSource]) -> bool:
        ...

    @staticmethod
    @overload
    def Count(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Count_TSource]) -> int:
        ...

    @staticmethod
    @overload
    def Count(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Count_TSource], predicate: typing.Callable[[System_Linq_Enumerable_Count_TSource], bool]) -> int:
        ...

    @staticmethod
    @overload
    def CreateSelectIPartitionIterator(selector: typing.Callable[[System_Linq_Enumerable_CreateSelectIPartitionIterator_TSource], System_Linq_Enumerable_CreateSelectIPartitionIterator_TResult], partition: System.Linq.IPartition[System_Linq_Enumerable_CreateSelectIPartitionIterator_TSource], result: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_CreateSelectIPartitionIterator_TResult]) -> None:
        ...

    @staticmethod
    @overload
    def CreateSelectIPartitionIterator(selector: typing.Callable[[System_Linq_Enumerable_CreateSelectIPartitionIterator_TSource], System_Linq_Enumerable_CreateSelectIPartitionIterator_TResult], partition: System.Linq.IPartition[System_Linq_Enumerable_CreateSelectIPartitionIterator_TSource], result: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_CreateSelectIPartitionIterator_TResult]) -> None:
        ...

    @staticmethod
    @overload
    def DefaultIfEmpty(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_DefaultIfEmpty_TSource]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_DefaultIfEmpty_TSource]:
        ...

    @staticmethod
    @overload
    def DefaultIfEmpty(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_DefaultIfEmpty_TSource], defaultValue: System_Linq_Enumerable_DefaultIfEmpty_TSource) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_DefaultIfEmpty_TSource]:
        ...

    @staticmethod
    @overload
    def Distinct(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Distinct_TSource]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Distinct_TSource]:
        ...

    @staticmethod
    @overload
    def Distinct(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Distinct_TSource], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_Enumerable_Distinct_TSource]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Distinct_TSource]:
        ...

    @staticmethod
    @overload
    def DistinctBy(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_DistinctBy_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_DistinctBy_TSource], System_Linq_Enumerable_DistinctBy_TKey]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_DistinctBy_TSource]:
        """
        Returns distinct elements from a sequence according to a specified key selector function.
        
        :param source: The sequence to remove duplicate elements from.
        :param keySelector: A function to extract the key for each element.
        :returns: An IEnumerable{T} that contains distinct elements from the source sequence.
        """
        ...

    @staticmethod
    @overload
    def DistinctBy(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_DistinctBy_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_DistinctBy_TSource], System_Linq_Enumerable_DistinctBy_TKey], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_Enumerable_DistinctBy_TKey]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_DistinctBy_TSource]:
        """
        Returns distinct elements from a sequence according to a specified key selector function.
        
        :param source: The sequence to remove duplicate elements from.
        :param keySelector: A function to extract the key for each element.
        :param comparer: An IEqualityComparer{TKey} to compare keys.
        :returns: An IEnumerable{T} that contains distinct elements from the source sequence.
        """
        ...

    @staticmethod
    @overload
    def ElementAt(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_ElementAt_TSource], index: int) -> System_Linq_Enumerable_ElementAt_TSource:
        ...

    @staticmethod
    @overload
    def ElementAt(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_ElementAt_TSource], index: System.Index) -> System_Linq_Enumerable_ElementAt_TSource:
        """
        Returns the element at a specified index in a sequence.
        
        :param source: An IEnumerable{T} to return an element from.
        :param index: The index of the element to retrieve, which is either from the start or the end.
        :returns: The element at the specified position in the  sequence.
        """
        ...

    @staticmethod
    @overload
    def ElementAtOrDefault(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_ElementAtOrDefault_TSource], index: int) -> System_Linq_Enumerable_ElementAtOrDefault_TSource:
        ...

    @staticmethod
    @overload
    def ElementAtOrDefault(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_ElementAtOrDefault_TSource], index: System.Index) -> System_Linq_Enumerable_ElementAtOrDefault_TSource:
        """
        Returns the element at a specified index in a sequence or a default value if the index is out of range.
        
        :param source: An IEnumerable{T} to return an element from.
        :param index: The index of the element to retrieve, which is either from the start or the end.
        :returns: default if  is outside the bounds of the  sequence; otherwise, the element at the specified position in the  sequence.
        """
        ...

    @staticmethod
    @overload
    def Empty() -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Empty_TResult]:
        ...

    @staticmethod
    @overload
    def Empty() -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Empty_TResult]:
        ...

    @staticmethod
    @overload
    def Except(first: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Except_TSource], second: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Except_TSource]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Except_TSource]:
        ...

    @staticmethod
    @overload
    def Except(first: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Except_TSource], second: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Except_TSource], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_Enumerable_Except_TSource]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Except_TSource]:
        ...

    @staticmethod
    @overload
    def ExceptBy(first: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_ExceptBy_TSource], second: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_ExceptBy_TKey], keySelector: typing.Callable[[System_Linq_Enumerable_ExceptBy_TSource], System_Linq_Enumerable_ExceptBy_TKey]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_ExceptBy_TSource]:
        """
        Produces the set difference of two sequences according to a specified key selector function.
        
        :param first: An IEnumerable{TSource} whose keys that are not also in  will be returned.
        :param second: An IEnumerable{TKey} whose keys that also occur in the first sequence will cause those elements to be removed from the returned sequence.
        :param keySelector: A function to extract the key for each element.
        :returns: A sequence that contains the set difference of the elements of two sequences.
        """
        ...

    @staticmethod
    @overload
    def ExceptBy(first: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_ExceptBy_TSource], second: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_ExceptBy_TKey], keySelector: typing.Callable[[System_Linq_Enumerable_ExceptBy_TSource], System_Linq_Enumerable_ExceptBy_TKey], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_Enumerable_ExceptBy_TKey]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_ExceptBy_TSource]:
        """
        Produces the set difference of two sequences according to a specified key selector function.
        
        :param first: An IEnumerable{TSource} whose keys that are not also in  will be returned.
        :param second: An IEnumerable{TKey} whose keys that also occur in the first sequence will cause those elements to be removed from the returned sequence.
        :param keySelector: A function to extract the key for each element.
        :param comparer: The IEqualityComparer{TKey} to compare values.
        :returns: A sequence that contains the set difference of the elements of two sequences.
        """
        ...

    @staticmethod
    @overload
    def First(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_First_TSource]) -> System_Linq_Enumerable_First_TSource:
        ...

    @staticmethod
    @overload
    def First(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_First_TSource], predicate: typing.Callable[[System_Linq_Enumerable_First_TSource], bool]) -> System_Linq_Enumerable_First_TSource:
        ...

    @staticmethod
    @overload
    def FirstOrDefault(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_FirstOrDefault_TSource]) -> System_Linq_Enumerable_FirstOrDefault_TSource:
        ...

    @staticmethod
    @overload
    def FirstOrDefault(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_FirstOrDefault_TSource], defaultValue: System_Linq_Enumerable_FirstOrDefault_TSource) -> System_Linq_Enumerable_FirstOrDefault_TSource:
        """
        Returns the first element of a sequence, or a default value if the sequence contains no elements.
        
        :param source: The IEnumerable{T} to return the first element of.
        :param defaultValue: The default value to return if the sequence is empty.
        :returns: if  is empty; otherwise, the first element in .
        """
        ...

    @staticmethod
    @overload
    def FirstOrDefault(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_FirstOrDefault_TSource], predicate: typing.Callable[[System_Linq_Enumerable_FirstOrDefault_TSource], bool]) -> System_Linq_Enumerable_FirstOrDefault_TSource:
        ...

    @staticmethod
    @overload
    def FirstOrDefault(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_FirstOrDefault_TSource], predicate: typing.Callable[[System_Linq_Enumerable_FirstOrDefault_TSource], bool], defaultValue: System_Linq_Enumerable_FirstOrDefault_TSource) -> System_Linq_Enumerable_FirstOrDefault_TSource:
        """
        Returns the first element of the sequence that satisfies a condition or a default value if no such element is found.
        
        :param source: An IEnumerable{T} to return an element from.
        :param predicate: A function to test each element for a condition.
        :param defaultValue: The default value to return if the sequence is empty.
        :returns: if  is empty or if no element passes the test specified by ; otherwise, the first element in  that passes the test specified by .
        """
        ...

    @staticmethod
    @overload
    def GroupBy(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupBy_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_GroupBy_TSource], System_Linq_Enumerable_GroupBy_TKey]) -> System.Collections.Generic.IEnumerable[System.Linq.IGrouping[System_Linq_Enumerable_GroupBy_TKey, System_Linq_Enumerable_GroupBy_TSource]]:
        ...

    @staticmethod
    @overload
    def GroupBy(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupBy_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_GroupBy_TSource], System_Linq_Enumerable_GroupBy_TKey], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_Enumerable_GroupBy_TKey]) -> System.Collections.Generic.IEnumerable[System.Linq.IGrouping[System_Linq_Enumerable_GroupBy_TKey, System_Linq_Enumerable_GroupBy_TSource]]:
        ...

    @staticmethod
    @overload
    def GroupBy(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupBy_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_GroupBy_TSource], System_Linq_Enumerable_GroupBy_TKey], elementSelector: typing.Callable[[System_Linq_Enumerable_GroupBy_TSource], System_Linq_Enumerable_GroupBy_TElement]) -> System.Collections.Generic.IEnumerable[System.Linq.IGrouping[System_Linq_Enumerable_GroupBy_TKey, System_Linq_Enumerable_GroupBy_TElement]]:
        ...

    @staticmethod
    @overload
    def GroupBy(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupBy_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_GroupBy_TSource], System_Linq_Enumerable_GroupBy_TKey], elementSelector: typing.Callable[[System_Linq_Enumerable_GroupBy_TSource], System_Linq_Enumerable_GroupBy_TElement], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_Enumerable_GroupBy_TKey]) -> System.Collections.Generic.IEnumerable[System.Linq.IGrouping[System_Linq_Enumerable_GroupBy_TKey, System_Linq_Enumerable_GroupBy_TElement]]:
        ...

    @staticmethod
    @overload
    def GroupBy(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupBy_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_GroupBy_TSource], System_Linq_Enumerable_GroupBy_TKey], resultSelector: typing.Callable[[System_Linq_Enumerable_GroupBy_TKey, System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupBy_TSource]], System_Linq_Enumerable_GroupBy_TResult]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupBy_TResult]:
        ...

    @staticmethod
    @overload
    def GroupBy(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupBy_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_GroupBy_TSource], System_Linq_Enumerable_GroupBy_TKey], elementSelector: typing.Callable[[System_Linq_Enumerable_GroupBy_TSource], System_Linq_Enumerable_GroupBy_TElement], resultSelector: typing.Callable[[System_Linq_Enumerable_GroupBy_TKey, System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupBy_TElement]], System_Linq_Enumerable_GroupBy_TResult]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupBy_TResult]:
        ...

    @staticmethod
    @overload
    def GroupBy(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupBy_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_GroupBy_TSource], System_Linq_Enumerable_GroupBy_TKey], resultSelector: typing.Callable[[System_Linq_Enumerable_GroupBy_TKey, System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupBy_TSource]], System_Linq_Enumerable_GroupBy_TResult], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_Enumerable_GroupBy_TKey]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupBy_TResult]:
        ...

    @staticmethod
    @overload
    def GroupBy(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupBy_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_GroupBy_TSource], System_Linq_Enumerable_GroupBy_TKey], elementSelector: typing.Callable[[System_Linq_Enumerable_GroupBy_TSource], System_Linq_Enumerable_GroupBy_TElement], resultSelector: typing.Callable[[System_Linq_Enumerable_GroupBy_TKey, System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupBy_TElement]], System_Linq_Enumerable_GroupBy_TResult], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_Enumerable_GroupBy_TKey]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupBy_TResult]:
        ...

    @staticmethod
    @overload
    def GroupJoin(outer: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupJoin_TOuter], inner: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupJoin_TInner], outerKeySelector: typing.Callable[[System_Linq_Enumerable_GroupJoin_TOuter], System_Linq_Enumerable_GroupJoin_TKey], innerKeySelector: typing.Callable[[System_Linq_Enumerable_GroupJoin_TInner], System_Linq_Enumerable_GroupJoin_TKey], resultSelector: typing.Callable[[System_Linq_Enumerable_GroupJoin_TOuter, System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupJoin_TInner]], System_Linq_Enumerable_GroupJoin_TResult]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupJoin_TResult]:
        ...

    @staticmethod
    @overload
    def GroupJoin(outer: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupJoin_TOuter], inner: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupJoin_TInner], outerKeySelector: typing.Callable[[System_Linq_Enumerable_GroupJoin_TOuter], System_Linq_Enumerable_GroupJoin_TKey], innerKeySelector: typing.Callable[[System_Linq_Enumerable_GroupJoin_TInner], System_Linq_Enumerable_GroupJoin_TKey], resultSelector: typing.Callable[[System_Linq_Enumerable_GroupJoin_TOuter, System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupJoin_TInner]], System_Linq_Enumerable_GroupJoin_TResult], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_Enumerable_GroupJoin_TKey]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_GroupJoin_TResult]:
        ...

    @staticmethod
    @overload
    def Intersect(first: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Intersect_TSource], second: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Intersect_TSource]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Intersect_TSource]:
        ...

    @staticmethod
    @overload
    def Intersect(first: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Intersect_TSource], second: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Intersect_TSource], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_Enumerable_Intersect_TSource]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Intersect_TSource]:
        ...

    @staticmethod
    @overload
    def IntersectBy(first: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_IntersectBy_TSource], second: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_IntersectBy_TKey], keySelector: typing.Callable[[System_Linq_Enumerable_IntersectBy_TSource], System_Linq_Enumerable_IntersectBy_TKey]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_IntersectBy_TSource]:
        """
        Produces the set intersection of two sequences according to a specified key selector function.
        
        :param first: An IEnumerable{T} whose distinct elements that also appear in  will be returned.
        :param second: An IEnumerable{T} whose distinct elements that also appear in the first sequence will be returned.
        :param keySelector: A function to extract the key for each element.
        :returns: A sequence that contains the elements that form the set intersection of two sequences.
        """
        ...

    @staticmethod
    @overload
    def IntersectBy(first: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_IntersectBy_TSource], second: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_IntersectBy_TKey], keySelector: typing.Callable[[System_Linq_Enumerable_IntersectBy_TSource], System_Linq_Enumerable_IntersectBy_TKey], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_Enumerable_IntersectBy_TKey]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_IntersectBy_TSource]:
        """
        Produces the set intersection of two sequences according to a specified key selector function.
        
        :param first: An IEnumerable{T} whose distinct elements that also appear in  will be returned.
        :param second: An IEnumerable{T} whose distinct elements that also appear in the first sequence will be returned.
        :param keySelector: A function to extract the key for each element.
        :param comparer: An IEqualityComparer{TKey} to compare keys.
        :returns: A sequence that contains the elements that form the set intersection of two sequences.
        """
        ...

    @staticmethod
    @overload
    def Join(outer: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Join_TOuter], inner: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Join_TInner], outerKeySelector: typing.Callable[[System_Linq_Enumerable_Join_TOuter], System_Linq_Enumerable_Join_TKey], innerKeySelector: typing.Callable[[System_Linq_Enumerable_Join_TInner], System_Linq_Enumerable_Join_TKey], resultSelector: typing.Callable[[System_Linq_Enumerable_Join_TOuter, System_Linq_Enumerable_Join_TInner], System_Linq_Enumerable_Join_TResult]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Join_TResult]:
        ...

    @staticmethod
    @overload
    def Join(outer: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Join_TOuter], inner: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Join_TInner], outerKeySelector: typing.Callable[[System_Linq_Enumerable_Join_TOuter], System_Linq_Enumerable_Join_TKey], innerKeySelector: typing.Callable[[System_Linq_Enumerable_Join_TInner], System_Linq_Enumerable_Join_TKey], resultSelector: typing.Callable[[System_Linq_Enumerable_Join_TOuter, System_Linq_Enumerable_Join_TInner], System_Linq_Enumerable_Join_TResult], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_Enumerable_Join_TKey]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Join_TResult]:
        ...

    @staticmethod
    @overload
    def Last(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Last_TSource]) -> System_Linq_Enumerable_Last_TSource:
        ...

    @staticmethod
    @overload
    def Last(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Last_TSource], predicate: typing.Callable[[System_Linq_Enumerable_Last_TSource], bool]) -> System_Linq_Enumerable_Last_TSource:
        ...

    @staticmethod
    @overload
    def LastOrDefault(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_LastOrDefault_TSource]) -> System_Linq_Enumerable_LastOrDefault_TSource:
        ...

    @staticmethod
    @overload
    def LastOrDefault(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_LastOrDefault_TSource], defaultValue: System_Linq_Enumerable_LastOrDefault_TSource) -> System_Linq_Enumerable_LastOrDefault_TSource:
        """
        Returns the last element of a sequence, or a default value if the sequence contains no elements.
        
        :param source: An IEnumerable{T} to return the last element of.
        :param defaultValue: The default value to return if the sequence is empty.
        :returns: if the source sequence is empty; otherwise, the last element in the IEnumerable{T}.
        """
        ...

    @staticmethod
    @overload
    def LastOrDefault(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_LastOrDefault_TSource], predicate: typing.Callable[[System_Linq_Enumerable_LastOrDefault_TSource], bool]) -> System_Linq_Enumerable_LastOrDefault_TSource:
        ...

    @staticmethod
    @overload
    def LastOrDefault(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_LastOrDefault_TSource], predicate: typing.Callable[[System_Linq_Enumerable_LastOrDefault_TSource], bool], defaultValue: System_Linq_Enumerable_LastOrDefault_TSource) -> System_Linq_Enumerable_LastOrDefault_TSource:
        """
        Returns the last element of a sequence that satisfies a condition or a default value if no such element is found.
        
        :param source: An IEnumerable{T} to return an element from.
        :param predicate: A function to test each element for a condition.
        :param defaultValue: The default value to return if the sequence is empty.
        :returns: if the sequence is empty or if no elements pass the test in the predicate function; otherwise, the last element that passes the test in the predicate function.
        """
        ...

    @staticmethod
    @overload
    def LongCount(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_LongCount_TSource]) -> int:
        ...

    @staticmethod
    @overload
    def LongCount(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_LongCount_TSource], predicate: typing.Callable[[System_Linq_Enumerable_LongCount_TSource], bool]) -> int:
        ...

    @staticmethod
    @overload
    def Max(source: System.Collections.Generic.IEnumerable[int]) -> int:
        ...

    @staticmethod
    @overload
    def Max(source: System.Collections.Generic.IEnumerable[int]) -> int:
        ...

    @staticmethod
    @overload
    def Max(source: System.Collections.Generic.IEnumerable[typing.Optional[int]]) -> typing.Optional[int]:
        ...

    @staticmethod
    @overload
    def Max(source: System.Collections.Generic.IEnumerable[typing.Optional[int]]) -> typing.Optional[int]:
        ...

    @staticmethod
    @overload
    def Max(source: System.Collections.Generic.IEnumerable[float]) -> float:
        ...

    @staticmethod
    @overload
    def Max(source: System.Collections.Generic.IEnumerable[typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Max(source: System.Collections.Generic.IEnumerable[float]) -> float:
        ...

    @staticmethod
    @overload
    def Max(source: System.Collections.Generic.IEnumerable[typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Max(source: System.Collections.Generic.IEnumerable[float]) -> float:
        ...

    @staticmethod
    @overload
    def Max(source: System.Collections.Generic.IEnumerable[typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Max(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Max_TSource]) -> System_Linq_Enumerable_Max_TSource:
        ...

    @staticmethod
    @overload
    def Max(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Max_TSource], comparer: System.Collections.Generic.IComparer[System_Linq_Enumerable_Max_TSource]) -> System_Linq_Enumerable_Max_TSource:
        """
        Returns the maximum value in a generic sequence.
        
        :param source: A sequence of values to determine the maximum value of.
        :param comparer: The IComparer{T} to compare values.
        :returns: The maximum value in the sequence.
        """
        ...

    @staticmethod
    @overload
    def Max(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Max_TSource], selector: typing.Callable[[System_Linq_Enumerable_Max_TSource], int]) -> int:
        ...

    @staticmethod
    @overload
    def Max(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Max_TSource], selector: typing.Callable[[System_Linq_Enumerable_Max_TSource], typing.Optional[int]]) -> typing.Optional[int]:
        ...

    @staticmethod
    @overload
    def Max(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Max_TSource], selector: typing.Callable[[System_Linq_Enumerable_Max_TSource], int]) -> int:
        ...

    @staticmethod
    @overload
    def Max(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Max_TSource], selector: typing.Callable[[System_Linq_Enumerable_Max_TSource], typing.Optional[int]]) -> typing.Optional[int]:
        ...

    @staticmethod
    @overload
    def Max(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Max_TSource], selector: typing.Callable[[System_Linq_Enumerable_Max_TSource], float]) -> float:
        ...

    @staticmethod
    @overload
    def Max(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Max_TSource], selector: typing.Callable[[System_Linq_Enumerable_Max_TSource], typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Max(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Max_TSource], selector: typing.Callable[[System_Linq_Enumerable_Max_TSource], float]) -> float:
        ...

    @staticmethod
    @overload
    def Max(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Max_TSource], selector: typing.Callable[[System_Linq_Enumerable_Max_TSource], typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Max(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Max_TSource], selector: typing.Callable[[System_Linq_Enumerable_Max_TSource], float]) -> float:
        ...

    @staticmethod
    @overload
    def Max(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Max_TSource], selector: typing.Callable[[System_Linq_Enumerable_Max_TSource], typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Max(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Max_TSource], selector: typing.Callable[[System_Linq_Enumerable_Max_TSource], System_Linq_Enumerable_Max_TResult]) -> System_Linq_Enumerable_Max_TResult:
        ...

    @staticmethod
    @overload
    def MaxBy(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_MaxBy_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_MaxBy_TSource], System_Linq_Enumerable_MaxBy_TKey]) -> System_Linq_Enumerable_MaxBy_TSource:
        """
        Returns the maximum value in a generic sequence according to a specified key selector function.
        
        :param source: A sequence of values to determine the maximum value of.
        :param keySelector: A function to extract the key for each element.
        :returns: The value with the maximum key in the sequence.
        """
        ...

    @staticmethod
    @overload
    def MaxBy(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_MaxBy_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_MaxBy_TSource], System_Linq_Enumerable_MaxBy_TKey], comparer: System.Collections.Generic.IComparer[System_Linq_Enumerable_MaxBy_TKey]) -> System_Linq_Enumerable_MaxBy_TSource:
        """
        Returns the maximum value in a generic sequence according to a specified key selector function.
        
        :param source: A sequence of values to determine the maximum value of.
        :param keySelector: A function to extract the key for each element.
        :param comparer: The IComparer{TKey} to compare keys.
        :returns: The value with the maximum key in the sequence.
        """
        ...

    @staticmethod
    @overload
    def Min(source: System.Collections.Generic.IEnumerable[int]) -> int:
        ...

    @staticmethod
    @overload
    def Min(source: System.Collections.Generic.IEnumerable[int]) -> int:
        ...

    @staticmethod
    @overload
    def Min(source: System.Collections.Generic.IEnumerable[typing.Optional[int]]) -> typing.Optional[int]:
        ...

    @staticmethod
    @overload
    def Min(source: System.Collections.Generic.IEnumerable[typing.Optional[int]]) -> typing.Optional[int]:
        ...

    @staticmethod
    @overload
    def Min(source: System.Collections.Generic.IEnumerable[float]) -> float:
        ...

    @staticmethod
    @overload
    def Min(source: System.Collections.Generic.IEnumerable[typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Min(source: System.Collections.Generic.IEnumerable[float]) -> float:
        ...

    @staticmethod
    @overload
    def Min(source: System.Collections.Generic.IEnumerable[typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Min(source: System.Collections.Generic.IEnumerable[float]) -> float:
        ...

    @staticmethod
    @overload
    def Min(source: System.Collections.Generic.IEnumerable[typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Min(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Min_TSource]) -> System_Linq_Enumerable_Min_TSource:
        ...

    @staticmethod
    @overload
    def Min(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Min_TSource], comparer: System.Collections.Generic.IComparer[System_Linq_Enumerable_Min_TSource]) -> System_Linq_Enumerable_Min_TSource:
        """
        Returns the minimum value in a generic sequence.
        
        :param source: A sequence of values to determine the minimum value of.
        :param comparer: The IComparer{T} to compare values.
        :returns: The minimum value in the sequence.
        """
        ...

    @staticmethod
    @overload
    def Min(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Min_TSource], selector: typing.Callable[[System_Linq_Enumerable_Min_TSource], int]) -> int:
        ...

    @staticmethod
    @overload
    def Min(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Min_TSource], selector: typing.Callable[[System_Linq_Enumerable_Min_TSource], typing.Optional[int]]) -> typing.Optional[int]:
        ...

    @staticmethod
    @overload
    def Min(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Min_TSource], selector: typing.Callable[[System_Linq_Enumerable_Min_TSource], int]) -> int:
        ...

    @staticmethod
    @overload
    def Min(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Min_TSource], selector: typing.Callable[[System_Linq_Enumerable_Min_TSource], typing.Optional[int]]) -> typing.Optional[int]:
        ...

    @staticmethod
    @overload
    def Min(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Min_TSource], selector: typing.Callable[[System_Linq_Enumerable_Min_TSource], float]) -> float:
        ...

    @staticmethod
    @overload
    def Min(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Min_TSource], selector: typing.Callable[[System_Linq_Enumerable_Min_TSource], typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Min(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Min_TSource], selector: typing.Callable[[System_Linq_Enumerable_Min_TSource], float]) -> float:
        ...

    @staticmethod
    @overload
    def Min(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Min_TSource], selector: typing.Callable[[System_Linq_Enumerable_Min_TSource], typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Min(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Min_TSource], selector: typing.Callable[[System_Linq_Enumerable_Min_TSource], float]) -> float:
        ...

    @staticmethod
    @overload
    def Min(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Min_TSource], selector: typing.Callable[[System_Linq_Enumerable_Min_TSource], typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Min(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Min_TSource], selector: typing.Callable[[System_Linq_Enumerable_Min_TSource], System_Linq_Enumerable_Min_TResult]) -> System_Linq_Enumerable_Min_TResult:
        ...

    @staticmethod
    @overload
    def MinBy(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_MinBy_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_MinBy_TSource], System_Linq_Enumerable_MinBy_TKey]) -> System_Linq_Enumerable_MinBy_TSource:
        """
        Returns the minimum value in a generic sequence according to a specified key selector function.
        
        :param source: A sequence of values to determine the minimum value of.
        :param keySelector: A function to extract the key for each element.
        :returns: The value with the minimum key in the sequence.
        """
        ...

    @staticmethod
    @overload
    def MinBy(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_MinBy_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_MinBy_TSource], System_Linq_Enumerable_MinBy_TKey], comparer: System.Collections.Generic.IComparer[System_Linq_Enumerable_MinBy_TKey]) -> System_Linq_Enumerable_MinBy_TSource:
        """
        Returns the minimum value in a generic sequence according to a specified key selector function.
        
        :param source: A sequence of values to determine the minimum value of.
        :param keySelector: A function to extract the key for each element.
        :param comparer: The IComparer{TKey} to compare keys.
        :returns: The value with the minimum key in the sequence.
        """
        ...

    @staticmethod
    def OfType(source: System.Collections.IEnumerable) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_OfType_TResult]:
        ...

    @staticmethod
    @overload
    def Order(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Order_T]) -> System.Linq.IOrderedEnumerable[System_Linq_Enumerable_Order_T]:
        """
        Sorts the elements of a sequence in ascending order.
        
        :param source: A sequence of values to order.
        :returns: An IOrderedEnumerable{TElement} whose elements are sorted.
        """
        ...

    @staticmethod
    @overload
    def Order(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Order_T], comparer: System.Collections.Generic.IComparer[System_Linq_Enumerable_Order_T]) -> System.Linq.IOrderedEnumerable[System_Linq_Enumerable_Order_T]:
        """
        Sorts the elements of a sequence in ascending order.
        
        :param source: A sequence of values to order.
        :param comparer: An IComparer{T} to compare keys.
        :returns: An IOrderedEnumerable{TElement} whose elements are sorted.
        """
        ...

    @staticmethod
    @overload
    def OrderBy(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_OrderBy_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_OrderBy_TSource], System_Linq_Enumerable_OrderBy_TKey]) -> System.Linq.IOrderedEnumerable[System_Linq_Enumerable_OrderBy_TSource]:
        ...

    @staticmethod
    @overload
    def OrderBy(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_OrderBy_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_OrderBy_TSource], System_Linq_Enumerable_OrderBy_TKey], comparer: System.Collections.Generic.IComparer[System_Linq_Enumerable_OrderBy_TKey]) -> System.Linq.IOrderedEnumerable[System_Linq_Enumerable_OrderBy_TSource]:
        ...

    @staticmethod
    @overload
    def OrderByDescending(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_OrderByDescending_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_OrderByDescending_TSource], System_Linq_Enumerable_OrderByDescending_TKey]) -> System.Linq.IOrderedEnumerable[System_Linq_Enumerable_OrderByDescending_TSource]:
        ...

    @staticmethod
    @overload
    def OrderByDescending(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_OrderByDescending_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_OrderByDescending_TSource], System_Linq_Enumerable_OrderByDescending_TKey], comparer: System.Collections.Generic.IComparer[System_Linq_Enumerable_OrderByDescending_TKey]) -> System.Linq.IOrderedEnumerable[System_Linq_Enumerable_OrderByDescending_TSource]:
        ...

    @staticmethod
    @overload
    def OrderDescending(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_OrderDescending_T]) -> System.Linq.IOrderedEnumerable[System_Linq_Enumerable_OrderDescending_T]:
        """
        Sorts the elements of a sequence in descending order.
        
        :param source: A sequence of values to order.
        :returns: An IOrderedEnumerable{TElement} whose elements are sorted.
        """
        ...

    @staticmethod
    @overload
    def OrderDescending(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_OrderDescending_T], comparer: System.Collections.Generic.IComparer[System_Linq_Enumerable_OrderDescending_T]) -> System.Linq.IOrderedEnumerable[System_Linq_Enumerable_OrderDescending_T]:
        """
        Sorts the elements of a sequence in descending order.
        
        :param source: A sequence of values to order.
        :param comparer: An IComparer{T} to compare keys.
        :returns: An IOrderedEnumerable{TElement} whose elements are sorted.
        """
        ...

    @staticmethod
    def Prepend(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Prepend_TSource], element: System_Linq_Enumerable_Prepend_TSource) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Prepend_TSource]:
        ...

    @staticmethod
    def Range(start: int, count: int) -> System.Collections.Generic.IEnumerable[int]:
        ...

    @staticmethod
    def Repeat(element: System_Linq_Enumerable_Repeat_TResult, count: int) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Repeat_TResult]:
        ...

    @staticmethod
    def Reverse(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Reverse_TSource]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Reverse_TSource]:
        ...

    @staticmethod
    @overload
    def Select(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Select_TSource], selector: typing.Callable[[System_Linq_Enumerable_Select_TSource], System_Linq_Enumerable_Select_TResult]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Select_TResult]:
        ...

    @staticmethod
    @overload
    def Select(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Select_TSource], selector: typing.Callable[[System_Linq_Enumerable_Select_TSource, int], System_Linq_Enumerable_Select_TResult]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Select_TResult]:
        ...

    @staticmethod
    @overload
    def SelectMany(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SelectMany_TSource], selector: typing.Callable[[System_Linq_Enumerable_SelectMany_TSource], System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SelectMany_TResult]]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SelectMany_TResult]:
        ...

    @staticmethod
    @overload
    def SelectMany(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SelectMany_TSource], selector: typing.Callable[[System_Linq_Enumerable_SelectMany_TSource, int], System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SelectMany_TResult]]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SelectMany_TResult]:
        ...

    @staticmethod
    @overload
    def SelectMany(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SelectMany_TSource], collectionSelector: typing.Callable[[System_Linq_Enumerable_SelectMany_TSource, int], System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SelectMany_TCollection]], resultSelector: typing.Callable[[System_Linq_Enumerable_SelectMany_TSource, System_Linq_Enumerable_SelectMany_TCollection], System_Linq_Enumerable_SelectMany_TResult]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SelectMany_TResult]:
        ...

    @staticmethod
    @overload
    def SelectMany(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SelectMany_TSource], collectionSelector: typing.Callable[[System_Linq_Enumerable_SelectMany_TSource], System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SelectMany_TCollection]], resultSelector: typing.Callable[[System_Linq_Enumerable_SelectMany_TSource, System_Linq_Enumerable_SelectMany_TCollection], System_Linq_Enumerable_SelectMany_TResult]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SelectMany_TResult]:
        ...

    @staticmethod
    @overload
    def SequenceEqual(first: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SequenceEqual_TSource], second: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SequenceEqual_TSource]) -> bool:
        ...

    @staticmethod
    @overload
    def SequenceEqual(first: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SequenceEqual_TSource], second: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SequenceEqual_TSource], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_Enumerable_SequenceEqual_TSource]) -> bool:
        ...

    @staticmethod
    @overload
    def Single(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Single_TSource]) -> System_Linq_Enumerable_Single_TSource:
        ...

    @staticmethod
    @overload
    def Single(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Single_TSource], predicate: typing.Callable[[System_Linq_Enumerable_Single_TSource], bool]) -> System_Linq_Enumerable_Single_TSource:
        ...

    @staticmethod
    @overload
    def SingleOrDefault(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SingleOrDefault_TSource]) -> System_Linq_Enumerable_SingleOrDefault_TSource:
        ...

    @staticmethod
    @overload
    def SingleOrDefault(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SingleOrDefault_TSource], defaultValue: System_Linq_Enumerable_SingleOrDefault_TSource) -> System_Linq_Enumerable_SingleOrDefault_TSource:
        """
        Returns the only element of a sequence, or a default value if the sequence is empty; this method throws an exception if there is more than one element in the sequence.
        
        :param source: An IEnumerable{T} to return the single element of.
        :param defaultValue: The default value to return if the sequence is empty.
        :returns: The single element of the input sequence, or  if the sequence contains no elements.
        """
        ...

    @staticmethod
    @overload
    def SingleOrDefault(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SingleOrDefault_TSource], predicate: typing.Callable[[System_Linq_Enumerable_SingleOrDefault_TSource], bool]) -> System_Linq_Enumerable_SingleOrDefault_TSource:
        ...

    @staticmethod
    @overload
    def SingleOrDefault(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SingleOrDefault_TSource], predicate: typing.Callable[[System_Linq_Enumerable_SingleOrDefault_TSource], bool], defaultValue: System_Linq_Enumerable_SingleOrDefault_TSource) -> System_Linq_Enumerable_SingleOrDefault_TSource:
        """
        Returns the only element of a sequence that satisfies a specified condition or a default value if no such element exists; this method throws an exception if more than one element satisfies the condition.
        
        :param source: An IEnumerable{T} to return a single element from.
        :param predicate: A function to test an element for a condition.
        :param defaultValue: The default value to return if the sequence is empty.
        :returns: The single element of the input sequence that satisfies the condition, or  if no such element is found.
        """
        ...

    @staticmethod
    def Skip(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Skip_TSource], count: int) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Skip_TSource]:
        ...

    @staticmethod
    def SkipLast(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SkipLast_TSource], count: int) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SkipLast_TSource]:
        ...

    @staticmethod
    @overload
    def SkipWhile(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SkipWhile_TSource], predicate: typing.Callable[[System_Linq_Enumerable_SkipWhile_TSource], bool]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SkipWhile_TSource]:
        ...

    @staticmethod
    @overload
    def SkipWhile(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SkipWhile_TSource], predicate: typing.Callable[[System_Linq_Enumerable_SkipWhile_TSource, int], bool]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_SkipWhile_TSource]:
        ...

    @staticmethod
    @overload
    def Sum(source: System.Collections.Generic.IEnumerable[int]) -> int:
        ...

    @staticmethod
    @overload
    def Sum(source: System.Collections.Generic.IEnumerable[int]) -> int:
        ...

    @staticmethod
    @overload
    def Sum(source: System.Collections.Generic.IEnumerable[float]) -> float:
        ...

    @staticmethod
    @overload
    def Sum(source: System.Collections.Generic.IEnumerable[float]) -> float:
        ...

    @staticmethod
    @overload
    def Sum(source: System.Collections.Generic.IEnumerable[float]) -> float:
        ...

    @staticmethod
    @overload
    def Sum(source: System.Collections.Generic.IEnumerable[typing.Optional[int]]) -> typing.Optional[int]:
        ...

    @staticmethod
    @overload
    def Sum(source: System.Collections.Generic.IEnumerable[typing.Optional[int]]) -> typing.Optional[int]:
        ...

    @staticmethod
    @overload
    def Sum(source: System.Collections.Generic.IEnumerable[typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Sum(source: System.Collections.Generic.IEnumerable[typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Sum(source: System.Collections.Generic.IEnumerable[typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Sum(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Sum_TSource], selector: typing.Callable[[System_Linq_Enumerable_Sum_TSource], int]) -> int:
        ...

    @staticmethod
    @overload
    def Sum(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Sum_TSource], selector: typing.Callable[[System_Linq_Enumerable_Sum_TSource], int]) -> int:
        ...

    @staticmethod
    @overload
    def Sum(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Sum_TSource], selector: typing.Callable[[System_Linq_Enumerable_Sum_TSource], float]) -> float:
        ...

    @staticmethod
    @overload
    def Sum(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Sum_TSource], selector: typing.Callable[[System_Linq_Enumerable_Sum_TSource], float]) -> float:
        ...

    @staticmethod
    @overload
    def Sum(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Sum_TSource], selector: typing.Callable[[System_Linq_Enumerable_Sum_TSource], float]) -> float:
        ...

    @staticmethod
    @overload
    def Sum(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Sum_TSource], selector: typing.Callable[[System_Linq_Enumerable_Sum_TSource], typing.Optional[int]]) -> typing.Optional[int]:
        ...

    @staticmethod
    @overload
    def Sum(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Sum_TSource], selector: typing.Callable[[System_Linq_Enumerable_Sum_TSource], typing.Optional[int]]) -> typing.Optional[int]:
        ...

    @staticmethod
    @overload
    def Sum(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Sum_TSource], selector: typing.Callable[[System_Linq_Enumerable_Sum_TSource], typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Sum(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Sum_TSource], selector: typing.Callable[[System_Linq_Enumerable_Sum_TSource], typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Sum(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Sum_TSource], selector: typing.Callable[[System_Linq_Enumerable_Sum_TSource], typing.Optional[float]]) -> typing.Optional[float]:
        ...

    @staticmethod
    @overload
    def Take(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Take_TSource], count: int) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Take_TSource]:
        ...

    @staticmethod
    @overload
    def Take(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Take_TSource], range: System.Range) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Take_TSource]:
        """
        Returns a specified range of contiguous elements from a sequence.
        
        :param source: The sequence to return elements from.
        :param range: The range of elements to return, which has start and end indexes either from the start or the end.
        :returns: An IEnumerable{T} that contains the specified  of elements from the  sequence.
        """
        ...

    @staticmethod
    def TakeLast(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_TakeLast_TSource], count: int) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_TakeLast_TSource]:
        ...

    @staticmethod
    @overload
    def TakeWhile(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_TakeWhile_TSource], predicate: typing.Callable[[System_Linq_Enumerable_TakeWhile_TSource], bool]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_TakeWhile_TSource]:
        ...

    @staticmethod
    @overload
    def TakeWhile(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_TakeWhile_TSource], predicate: typing.Callable[[System_Linq_Enumerable_TakeWhile_TSource, int], bool]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_TakeWhile_TSource]:
        ...

    @staticmethod
    @overload
    def ThenBy(source: System.Linq.IOrderedEnumerable[System_Linq_Enumerable_ThenBy_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_ThenBy_TSource], System_Linq_Enumerable_ThenBy_TKey]) -> System.Linq.IOrderedEnumerable[System_Linq_Enumerable_ThenBy_TSource]:
        ...

    @staticmethod
    @overload
    def ThenBy(source: System.Linq.IOrderedEnumerable[System_Linq_Enumerable_ThenBy_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_ThenBy_TSource], System_Linq_Enumerable_ThenBy_TKey], comparer: System.Collections.Generic.IComparer[System_Linq_Enumerable_ThenBy_TKey]) -> System.Linq.IOrderedEnumerable[System_Linq_Enumerable_ThenBy_TSource]:
        ...

    @staticmethod
    @overload
    def ThenByDescending(source: System.Linq.IOrderedEnumerable[System_Linq_Enumerable_ThenByDescending_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_ThenByDescending_TSource], System_Linq_Enumerable_ThenByDescending_TKey]) -> System.Linq.IOrderedEnumerable[System_Linq_Enumerable_ThenByDescending_TSource]:
        ...

    @staticmethod
    @overload
    def ThenByDescending(source: System.Linq.IOrderedEnumerable[System_Linq_Enumerable_ThenByDescending_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_ThenByDescending_TSource], System_Linq_Enumerable_ThenByDescending_TKey], comparer: System.Collections.Generic.IComparer[System_Linq_Enumerable_ThenByDescending_TKey]) -> System.Linq.IOrderedEnumerable[System_Linq_Enumerable_ThenByDescending_TSource]:
        ...

    @staticmethod
    def ToArray(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_ToArray_TSource]) -> typing.List[System_Linq_Enumerable_ToArray_TSource]:
        ...

    @staticmethod
    @overload
    def ToDictionary(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_ToDictionary_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_ToDictionary_TSource], System_Linq_Enumerable_ToDictionary_TKey]) -> System.Collections.Generic.Dictionary[System_Linq_Enumerable_ToDictionary_TKey, System_Linq_Enumerable_ToDictionary_TSource]:
        ...

    @staticmethod
    @overload
    def ToDictionary(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_ToDictionary_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_ToDictionary_TSource], System_Linq_Enumerable_ToDictionary_TKey], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_Enumerable_ToDictionary_TKey]) -> System.Collections.Generic.Dictionary[System_Linq_Enumerable_ToDictionary_TKey, System_Linq_Enumerable_ToDictionary_TSource]:
        ...

    @staticmethod
    @overload
    def ToDictionary(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_ToDictionary_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_ToDictionary_TSource], System_Linq_Enumerable_ToDictionary_TKey], elementSelector: typing.Callable[[System_Linq_Enumerable_ToDictionary_TSource], System_Linq_Enumerable_ToDictionary_TElement]) -> System.Collections.Generic.Dictionary[System_Linq_Enumerable_ToDictionary_TKey, System_Linq_Enumerable_ToDictionary_TElement]:
        ...

    @staticmethod
    @overload
    def ToDictionary(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_ToDictionary_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_ToDictionary_TSource], System_Linq_Enumerable_ToDictionary_TKey], elementSelector: typing.Callable[[System_Linq_Enumerable_ToDictionary_TSource], System_Linq_Enumerable_ToDictionary_TElement], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_Enumerable_ToDictionary_TKey]) -> System.Collections.Generic.Dictionary[System_Linq_Enumerable_ToDictionary_TKey, System_Linq_Enumerable_ToDictionary_TElement]:
        ...

    @staticmethod
    @overload
    def ToHashSet(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_ToHashSet_TSource]) -> System.Collections.Generic.HashSet[System_Linq_Enumerable_ToHashSet_TSource]:
        ...

    @staticmethod
    @overload
    def ToHashSet(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_ToHashSet_TSource], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_Enumerable_ToHashSet_TSource]) -> System.Collections.Generic.HashSet[System_Linq_Enumerable_ToHashSet_TSource]:
        ...

    @staticmethod
    def ToList(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_ToList_TSource]) -> System.Collections.Generic.List[System_Linq_Enumerable_ToList_TSource]:
        ...

    @staticmethod
    @overload
    def ToLookup(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_ToLookup_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_ToLookup_TSource], System_Linq_Enumerable_ToLookup_TKey]) -> System.Linq.ILookup[System_Linq_Enumerable_ToLookup_TKey, System_Linq_Enumerable_ToLookup_TSource]:
        ...

    @staticmethod
    @overload
    def ToLookup(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_ToLookup_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_ToLookup_TSource], System_Linq_Enumerable_ToLookup_TKey], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_Enumerable_ToLookup_TKey]) -> System.Linq.ILookup[System_Linq_Enumerable_ToLookup_TKey, System_Linq_Enumerable_ToLookup_TSource]:
        ...

    @staticmethod
    @overload
    def ToLookup(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_ToLookup_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_ToLookup_TSource], System_Linq_Enumerable_ToLookup_TKey], elementSelector: typing.Callable[[System_Linq_Enumerable_ToLookup_TSource], System_Linq_Enumerable_ToLookup_TElement]) -> System.Linq.ILookup[System_Linq_Enumerable_ToLookup_TKey, System_Linq_Enumerable_ToLookup_TElement]:
        ...

    @staticmethod
    @overload
    def ToLookup(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_ToLookup_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_ToLookup_TSource], System_Linq_Enumerable_ToLookup_TKey], elementSelector: typing.Callable[[System_Linq_Enumerable_ToLookup_TSource], System_Linq_Enumerable_ToLookup_TElement], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_Enumerable_ToLookup_TKey]) -> System.Linq.ILookup[System_Linq_Enumerable_ToLookup_TKey, System_Linq_Enumerable_ToLookup_TElement]:
        ...

    @staticmethod
    def TryGetNonEnumeratedCount(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_TryGetNonEnumeratedCount_TSource], count: typing.Optional[int]) -> typing.Union[bool, int]:
        """
        Attempts to determine the number of elements in a sequence without forcing an enumeration.
        
        :param source: A sequence that contains elements to be counted.
        :param count: When this method returns, contains the count of  if successful,     or zero if the method failed to determine the count.
        :returns: true if the count of  can be determined without enumeration;   otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def Union(first: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Union_TSource], second: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Union_TSource]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Union_TSource]:
        ...

    @staticmethod
    @overload
    def Union(first: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Union_TSource], second: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Union_TSource], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_Enumerable_Union_TSource]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Union_TSource]:
        ...

    @staticmethod
    @overload
    def UnionBy(first: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_UnionBy_TSource], second: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_UnionBy_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_UnionBy_TSource], System_Linq_Enumerable_UnionBy_TKey]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_UnionBy_TSource]:
        """
        Produces the set union of two sequences according to a specified key selector function.
        
        :param first: An IEnumerable{T} whose distinct elements form the first set for the union.
        :param second: An IEnumerable{T} whose distinct elements form the second set for the union.
        :param keySelector: A function to extract the key for each element.
        :returns: An IEnumerable{T} that contains the elements from both input sequences, excluding duplicates.
        """
        ...

    @staticmethod
    @overload
    def UnionBy(first: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_UnionBy_TSource], second: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_UnionBy_TSource], keySelector: typing.Callable[[System_Linq_Enumerable_UnionBy_TSource], System_Linq_Enumerable_UnionBy_TKey], comparer: System.Collections.Generic.IEqualityComparer[System_Linq_Enumerable_UnionBy_TKey]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_UnionBy_TSource]:
        """
        Produces the set union of two sequences according to a specified key selector function.
        
        :param first: An IEnumerable{T} whose distinct elements form the first set for the union.
        :param second: An IEnumerable{T} whose distinct elements form the second set for the union.
        :param keySelector: A function to extract the key for each element.
        :param comparer: The IEqualityComparer{T} to compare values.
        :returns: An IEnumerable{T} that contains the elements from both input sequences, excluding duplicates.
        """
        ...

    @staticmethod
    @overload
    def Where(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Where_TSource], predicate: typing.Callable[[System_Linq_Enumerable_Where_TSource], bool]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Where_TSource]:
        ...

    @staticmethod
    @overload
    def Where(source: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Where_TSource], predicate: typing.Callable[[System_Linq_Enumerable_Where_TSource, int], bool]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Where_TSource]:
        ...

    @staticmethod
    @overload
    def Zip(first: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Zip_TFirst], second: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Zip_TSecond], resultSelector: typing.Callable[[System_Linq_Enumerable_Zip_TFirst, System_Linq_Enumerable_Zip_TSecond], System_Linq_Enumerable_Zip_TResult]) -> System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Zip_TResult]:
        ...

    @staticmethod
    @overload
    def Zip(first: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Zip_TFirst], second: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Zip_TSecond]) -> System.Collections.Generic.IEnumerable[System.ValueTuple[System_Linq_Enumerable_Zip_TFirst, System_Linq_Enumerable_Zip_TSecond]]:
        ...

    @staticmethod
    @overload
    def Zip(first: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Zip_TFirst], second: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Zip_TSecond], third: System.Collections.Generic.IEnumerable[System_Linq_Enumerable_Zip_TThird]) -> System.Collections.Generic.IEnumerable[System.ValueTuple[System_Linq_Enumerable_Zip_TFirst, System_Linq_Enumerable_Zip_TSecond, System_Linq_Enumerable_Zip_TThird]]:
        """
        Produces a sequence of tuples with elements from the three specified sequences.
        
        :param first: The first sequence to merge.
        :param second: The second sequence to merge.
        :param third: The third sequence to merge.
        :returns: A sequence of tuples with elements taken from the first, second, and third sequences, in that order.
        """
        ...


class Lookup(typing.Generic[System_Linq_Lookup_TKey, System_Linq_Lookup_TElement], System.Object, System.Linq.IIListProvider[System.Linq.IGrouping[System_Linq_Lookup_TKey, System_Linq_Lookup_TElement]], System.Linq.ILookup[System_Linq_Lookup_TKey, System_Linq_Lookup_TElement], typing.Iterable[System.Linq.IGrouping[System_Linq_Lookup_TKey, System_Linq_Lookup_TElement]]):
    """This class has no documentation."""

    @property
    def Count(self) -> int:
        ...

    def __getitem__(self, key: System_Linq_Lookup_TKey) -> System.Collections.Generic.IEnumerable[System_Linq_Lookup_TElement]:
        ...

    def ApplyResultSelector(self, resultSelector: typing.Callable[[System_Linq_Lookup_TKey, System.Collections.Generic.IEnumerable[System_Linq_Lookup_TElement]], System_Linq_Lookup_ApplyResultSelector_TResult]) -> System.Collections.Generic.IEnumerable[System_Linq_Lookup_ApplyResultSelector_TResult]:
        ...

    def Contains(self, key: System_Linq_Lookup_TKey) -> bool:
        ...

    def GetCount(self, onlyIfCheap: bool) -> int:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System.Linq.IGrouping[System_Linq_Lookup_TKey, System_Linq_Lookup_TElement]]:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        ...

    def ToArray(self) -> typing.List[System.Linq.IGrouping[System_Linq_Lookup_TKey, System_Linq_Lookup_TElement]]:
        ...

    def ToList(self) -> System.Collections.Generic.List[System.Linq.IGrouping[System_Linq_Lookup_TKey, System_Linq_Lookup_TElement]]:
        ...


class Grouping(typing.Generic[System_Linq_Grouping_TKey, System_Linq_Grouping_TElement], System.Object, System.Linq.IGrouping[System_Linq_Grouping_TKey, System_Linq_Grouping_TElement], System.Collections.Generic.IList[System_Linq_Grouping_TElement], typing.Iterable[System_Linq_Grouping_TElement]):
    """This class has no documentation."""

    @property
    def _key(self) -> System_Linq_Grouping_TKey:
        ...

    @property
    def _hashCode(self) -> int:
        ...

    @property
    def _elements(self) -> typing.List[System_Linq_Grouping_TElement]:
        ...

    @_elements.setter
    def _elements(self, value: typing.List[System_Linq_Grouping_TElement]):
        ...

    @property
    def _count(self) -> int:
        ...

    @_count.setter
    def _count(self, value: int):
        ...

    @property
    def _hashNext(self) -> System.Linq.Grouping[System_Linq_Grouping_TKey, System_Linq_Grouping_TElement]:
        ...

    @_hashNext.setter
    def _hashNext(self, value: System.Linq.Grouping[System_Linq_Grouping_TKey, System_Linq_Grouping_TElement]):
        ...

    @property
    def _next(self) -> System.Linq.Grouping[System_Linq_Grouping_TKey, System_Linq_Grouping_TElement]:
        ...

    @_next.setter
    def _next(self, value: System.Linq.Grouping[System_Linq_Grouping_TKey, System_Linq_Grouping_TElement]):
        ...

    @property
    def Key(self) -> System_Linq_Grouping_TKey:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    def __getitem__(self, index: int) -> System_Linq_Grouping_TElement:
        ...

    def __setitem__(self, index: int, value: System_Linq_Grouping_TElement) -> None:
        ...

    def Add(self, item: System_Linq_Grouping_TElement) -> None:
        ...

    def Clear(self) -> None:
        ...

    def Contains(self, item: System_Linq_Grouping_TElement) -> bool:
        ...

    def CopyTo(self, array: typing.List[System_Linq_Grouping_TElement], arrayIndex: int) -> None:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System_Linq_Grouping_TElement]:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        ...

    def IndexOf(self, item: System_Linq_Grouping_TElement) -> int:
        ...

    def Insert(self, index: int, item: System_Linq_Grouping_TElement) -> None:
        ...

    def Remove(self, item: System_Linq_Grouping_TElement) -> bool:
        ...

    def RemoveAt(self, index: int) -> None:
        ...


