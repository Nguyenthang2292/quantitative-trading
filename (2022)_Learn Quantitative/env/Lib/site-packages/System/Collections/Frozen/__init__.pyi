from typing import overload
import abc
import typing

import System
import System.Collections
import System.Collections.Frozen
import System.Collections.Generic
import System.Collections.Immutable

System_Collections_Frozen_FrozenSet_T = typing.TypeVar("System_Collections_Frozen_FrozenSet_T")
System_Collections_Frozen_FrozenSet_ToFrozenSet_T = typing.TypeVar("System_Collections_Frozen_FrozenSet_ToFrozenSet_T")
System_Collections_Frozen_FrozenDictionary_TKey = typing.TypeVar("System_Collections_Frozen_FrozenDictionary_TKey")
System_Collections_Frozen_FrozenDictionary_TValue = typing.TypeVar("System_Collections_Frozen_FrozenDictionary_TValue")
System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TKey = typing.TypeVar("System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TKey")
System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TValue = typing.TypeVar("System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TValue")
System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TSource = typing.TypeVar("System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TSource")
System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TElement = typing.TypeVar("System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TElement")


class FrozenSet(typing.Generic[System_Collections_Frozen_FrozenSet_T], System.Object, System.Collections.Generic.ISet[System_Collections_Frozen_FrozenSet_T], System.Collections.Generic.IReadOnlyCollection[System_Collections_Frozen_FrozenSet_T], typing.Iterable[System_Collections_Frozen_FrozenSet_T], metaclass=abc.ABCMeta):
    """Provides an immutable, read-only set optimized for fast lookup and enumeration."""

    class Enumerator:
        """Enumerates the values of a FrozenSet{T}."""

        @property
        def Current(self) -> System_Collections_Frozen_FrozenSet_T:
            ...

        def Dispose(self) -> None:
            ...

        def MoveNext(self) -> bool:
            ...

        def Reset(self) -> None:
            ...

    Empty: System.Collections.Frozen.FrozenSet[System_Collections_Frozen_FrozenSet_T]
    """Gets an empty FrozenSet{T}."""

    @property
    def Comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Frozen_FrozenSet_T]:
        """Gets the comparer used by this set."""
        ...

    @property
    def Items(self) -> System.Collections.Immutable.ImmutableArray[System_Collections_Frozen_FrozenSet_T]:
        """Gets a collection containing the values in the set."""
        ...

    @property
    def Count(self) -> int:
        """Gets the number of values contained in the set."""
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @overload
    def Add(self, item: System_Collections_Frozen_FrozenSet_T) -> bool:
        ...

    @overload
    def Add(self, item: System_Collections_Frozen_FrozenSet_T) -> None:
        ...

    def Clear(self) -> None:
        ...

    def Contains(self, item: System_Collections_Frozen_FrozenSet_T) -> bool:
        """
        Determines whether the set contains the specified element.
        
        :param item: The element to locate.
        :returns: true if the set contains the specified element; otherwise, false.
        """
        ...

    @overload
    def CopyTo(self, destination: typing.List[System_Collections_Frozen_FrozenSet_T], destinationIndex: int) -> None:
        """
        Copies the values in the set to an array, starting at the specified .
        
        :param destination: The array that is the destination of the values copied from the set.
        :param destinationIndex: The zero-based index in  at which copying begins.
        """
        ...

    @overload
    def CopyTo(self, destination: System.Span[System_Collections_Frozen_FrozenSet_T]) -> None:
        """
        Copies the values in the set to a span.
        
        :param destination: The span that is the destination of the values copied from the set.
        """
        ...

    @overload
    def CopyTo(self, array: System.Array, index: int) -> None:
        ...

    def ExceptWith(self, other: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenSet_T]) -> None:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Frozen.FrozenSet.Enumerator:
        """
        Returns an enumerator that iterates through the set.
        
        :returns: An enumerator that iterates through the set.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Frozen_FrozenSet_T]:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        ...

    def IntersectWith(self, other: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenSet_T]) -> None:
        ...

    def IsProperSubsetOf(self, other: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenSet_T]) -> bool:
        ...

    def IsProperSupersetOf(self, other: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenSet_T]) -> bool:
        ...

    def IsSubsetOf(self, other: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenSet_T]) -> bool:
        ...

    def IsSupersetOf(self, other: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenSet_T]) -> bool:
        ...

    def Overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenSet_T]) -> bool:
        ...

    def Remove(self, item: System_Collections_Frozen_FrozenSet_T) -> bool:
        ...

    def SetEquals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenSet_T]) -> bool:
        ...

    def SymmetricExceptWith(self, other: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenSet_T]) -> None:
        ...

    @staticmethod
    def ToFrozenSet(source: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenSet_ToFrozenSet_T], comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Frozen_FrozenSet_ToFrozenSet_T] = None) -> System.Collections.Frozen.FrozenSet[System_Collections_Frozen_FrozenSet_ToFrozenSet_T]:
        """
        Creates a FrozenSet{T} with the specified values.
        
        :param source: The values to use to populate the set.
        :param comparer: The comparer implementation to use to compare values for equality. If null, EqualityComparer{T}.Default is used.
        :returns: A frozen set.
        """
        ...

    def TryGetValue(self, equalValue: System_Collections_Frozen_FrozenSet_T, actualValue: typing.Optional[System_Collections_Frozen_FrozenSet_T]) -> typing.Union[bool, System_Collections_Frozen_FrozenSet_T]:
        """
        Searches the set for a given value and returns the equal value it finds, if any.
        
        :param equalValue: The value to search for.
        :param actualValue: The value from the set that the search found, or the default value of T when the search yielded no match.
        :returns: A value indicating whether the search was successful.
        """
        ...

    def UnionWith(self, other: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenSet_T]) -> None:
        ...


class FrozenDictionary(typing.Generic[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue], System.Object, System.Collections.Generic.IDictionary[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue], System.Collections.Generic.IReadOnlyDictionary[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue], System.Collections.IDictionary, typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]], metaclass=abc.ABCMeta):
    """Provides an immutable, read-only dictionary optimized for fast lookup and enumeration."""

    class Enumerator:
        """Enumerates the elements of a FrozenDictionary{TKey, TValue}."""

        @property
        def Current(self) -> System.Collections.Generic.KeyValuePair[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]:
            ...

        def Dispose(self) -> None:
            ...

        def MoveNext(self) -> bool:
            ...

        def Reset(self) -> None:
            ...

    Empty: System.Collections.Frozen.FrozenDictionary[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]
    """Gets an empty FrozenDictionary{TKey, TValue}."""

    @property
    def Comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Frozen_FrozenDictionary_TKey]:
        """Gets the comparer used by this dictionary."""
        ...

    @property
    def Keys(self) -> System.Collections.Immutable.ImmutableArray[System_Collections_Frozen_FrozenDictionary_TKey]:
        """Gets a collection containing the keys in the dictionary."""
        ...

    @property
    def Values(self) -> System.Collections.Immutable.ImmutableArray[System_Collections_Frozen_FrozenDictionary_TValue]:
        """Gets a collection containing the values in the dictionary."""
        ...

    @property
    def Count(self) -> int:
        """Gets the number of key/value pairs contained in the dictionary."""
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @overload
    def __getitem__(self, key: typing.Any) -> typing.Any:
        ...

    @overload
    def __getitem__(self, key: System_Collections_Frozen_FrozenDictionary_TKey) -> typing.Any:
        """
        Gets a reference to the value associated with the specified key.
        
        :param key: The key of the value to get.
        :returns: A reference to the value associated with the specified key.
        """
        ...

    @overload
    def __getitem__(self, key: System_Collections_Frozen_FrozenDictionary_TKey) -> System_Collections_Frozen_FrozenDictionary_TValue:
        ...

    @overload
    def __getitem__(self, key: System_Collections_Frozen_FrozenDictionary_TKey) -> System_Collections_Frozen_FrozenDictionary_TValue:
        ...

    @overload
    def __setitem__(self, key: typing.Any, value: typing.Any) -> None:
        ...

    @overload
    def __setitem__(self, key: System_Collections_Frozen_FrozenDictionary_TKey, value: System_Collections_Frozen_FrozenDictionary_TValue) -> None:
        ...

    @overload
    def Add(self, key: System_Collections_Frozen_FrozenDictionary_TKey, value: System_Collections_Frozen_FrozenDictionary_TValue) -> None:
        ...

    @overload
    def Add(self, item: System.Collections.Generic.KeyValuePair[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]) -> None:
        ...

    @overload
    def Add(self, key: typing.Any, value: typing.Any) -> None:
        ...

    @overload
    def Clear(self) -> None:
        ...

    @overload
    def Clear(self) -> None:
        ...

    @overload
    def Contains(self, key: typing.Any) -> bool:
        ...

    @overload
    def Contains(self, item: System.Collections.Generic.KeyValuePair[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]) -> bool:
        ...

    def ContainsKey(self, key: System_Collections_Frozen_FrozenDictionary_TKey) -> bool:
        """
        Determines whether the dictionary contains the specified key.
        
        :param key: The key to locate in the dictionary.
        :returns: true if the dictionary contains an element with the specified key; otherwise, false.
        """
        ...

    @overload
    def CopyTo(self, destination: typing.List[System.Collections.Generic.KeyValuePair[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]], destinationIndex: int) -> None:
        """
        Copies the elements of the dictionary to an array of type KeyValuePair{TKey, TValue}, starting at the specified .
        
        :param destination: The array that is the destination of the elements copied from the dictionary.
        :param destinationIndex: The zero-based index in  at which copying begins.
        """
        ...

    @overload
    def CopyTo(self, destination: System.Span[System.Collections.Generic.KeyValuePair[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]]) -> None:
        """
        Copies the elements of the dictionary to a span of type KeyValuePair{TKey, TValue}.
        
        :param destination: The span that is the destination of the elements copied from the dictionary.
        """
        ...

    @overload
    def CopyTo(self, array: System.Array, index: int) -> None:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Frozen.FrozenDictionary.Enumerator:
        """
        Returns an enumerator that iterates through the dictionary.
        
        :returns: An enumerator that iterates through the dictionary.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]]:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IDictionaryEnumerator:
        ...

    def GetValueRefOrNullRef(self, key: System_Collections_Frozen_FrozenDictionary_TKey) -> typing.Any:
        """
        Gets either a reference to a TValue in the dictionary or a null reference if the key does not exist in the dictionary.
        
        :param key: The key used for lookup.
        :returns: A reference to a TValue in the dictionary or a null reference if the key does not exist in the dictionary.
        """
        ...

    @overload
    def Remove(self, key: System_Collections_Frozen_FrozenDictionary_TKey) -> bool:
        ...

    @overload
    def Remove(self, item: System.Collections.Generic.KeyValuePair[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]) -> bool:
        ...

    @overload
    def Remove(self, key: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def ToFrozenDictionary(source: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TValue]], comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TKey] = None) -> System.Collections.Frozen.FrozenDictionary[System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TValue]:
        """
        Creates a FrozenDictionary{TKey, TValue} with the specified key/value pairs.
        
        :param source: The key/value pairs to use to populate the dictionary.
        :param comparer: The comparer implementation to use to compare keys for equality. If null, EqualityComparer{TKey}.Default is used.
        :returns: A FrozenDictionary{TKey, TValue} that contains the specified keys and values.
        """
        ...

    @staticmethod
    @overload
    def ToFrozenDictionary(source: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TSource], keySelector: typing.Callable[[System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TSource], System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TKey], comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TKey] = None) -> System.Collections.Frozen.FrozenDictionary[System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TSource]:
        """
        Creates a FrozenDictionary{TKey, TSource} from an IEnumerable{TSource} according to specified key selector function.
        
        :param source: An IEnumerable{TSource} from which to create a FrozenDictionary{TKey, TSource}.
        :param keySelector: A function to extract a key from each element.
        :param comparer: An IEqualityComparer{TKey} to compare keys.
        :returns: A FrozenDictionary{TKey, TElement} that contains the keys and values selected from the input sequence.
        """
        ...

    @staticmethod
    @overload
    def ToFrozenDictionary(source: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TSource], keySelector: typing.Callable[[System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TSource], System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TKey], elementSelector: typing.Callable[[System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TSource], System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TElement], comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TKey] = None) -> System.Collections.Frozen.FrozenDictionary[System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_ToFrozenDictionary_TElement]:
        """
        Creates a FrozenDictionary{TKey, TElement} from an IEnumerable{TSource} according to specified key selector and element selector functions.
        
        :param source: An IEnumerable{TSource} from which to create a FrozenDictionary{TKey, TElement}.
        :param keySelector: A function to extract a key from each element.
        :param elementSelector: A transform function to produce a result element value from each element.
        :param comparer: An IEqualityComparer{TKey} to compare keys.
        :returns: A FrozenDictionary{TKey, TElement} that contains the keys and values selected from the input sequence.
        """
        ...

    def TryGetValue(self, key: System_Collections_Frozen_FrozenDictionary_TKey, value: typing.Optional[System_Collections_Frozen_FrozenDictionary_TValue]) -> typing.Union[bool, System_Collections_Frozen_FrozenDictionary_TValue]:
        """
        Gets the value associated with the specified key.
        
        :param key: The key of the value to get.
        :param value: When this method returns, contains the value associated with the specified key, if the key is found; otherwise, the default value for the type of the value parameter.
        :returns: true if the dictionary contains an element with the specified key; otherwise, false.
        """
        ...


