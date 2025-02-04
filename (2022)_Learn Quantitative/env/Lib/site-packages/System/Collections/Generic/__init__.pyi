from typing import overload
import abc
import typing

import System
import System.Collections
import System.Collections.Generic
import System.Collections.ObjectModel
import System.Runtime.Serialization
import System.Threading
import System.Threading.Tasks

System_Collections_Generic_IList_T = typing.TypeVar("System_Collections_Generic_IList_T")
System_Collections_Generic_Comparer_T = typing.TypeVar("System_Collections_Generic_Comparer_T")
System_Collections_Generic_GenericComparer_T = typing.TypeVar("System_Collections_Generic_GenericComparer_T")
System_Collections_Generic_NullableComparer_T = typing.TypeVar("System_Collections_Generic_NullableComparer_T")
System_Collections_Generic_ObjectComparer_T = typing.TypeVar("System_Collections_Generic_ObjectComparer_T")
System_Collections_Generic_IAsyncEnumerable_T = typing.TypeVar("System_Collections_Generic_IAsyncEnumerable_T")
System_Collections_Generic_IReadOnlyList_T = typing.TypeVar("System_Collections_Generic_IReadOnlyList_T")
System_Collections_Generic_IAsyncEnumerator_T = typing.TypeVar("System_Collections_Generic_IAsyncEnumerator_T")
System_Collections_Generic_KeyValuePair_TKey = typing.TypeVar("System_Collections_Generic_KeyValuePair_TKey")
System_Collections_Generic_KeyValuePair_TValue = typing.TypeVar("System_Collections_Generic_KeyValuePair_TValue")
System_Collections_Generic_KeyValuePair_Create_TKey = typing.TypeVar("System_Collections_Generic_KeyValuePair_Create_TKey")
System_Collections_Generic_KeyValuePair_Create_TValue = typing.TypeVar("System_Collections_Generic_KeyValuePair_Create_TValue")
System_Collections_Generic_IReadOnlyCollection_T = typing.TypeVar("System_Collections_Generic_IReadOnlyCollection_T")
System_Collections_Generic_ISet_T = typing.TypeVar("System_Collections_Generic_ISet_T")
System_Collections_Generic_IDictionary_TValue = typing.TypeVar("System_Collections_Generic_IDictionary_TValue")
System_Collections_Generic_IDictionary_TKey = typing.TypeVar("System_Collections_Generic_IDictionary_TKey")
System_Collections_Generic_Queue_T = typing.TypeVar("System_Collections_Generic_Queue_T")
System_Collections_Generic_IEqualityComparer_T = typing.TypeVar("System_Collections_Generic_IEqualityComparer_T")
System_Collections_Generic_IReadOnlySet_T = typing.TypeVar("System_Collections_Generic_IReadOnlySet_T")
System_Collections_Generic_HashSet_T = typing.TypeVar("System_Collections_Generic_HashSet_T")
System_Collections_Generic_IEnumerable_T = typing.TypeVar("System_Collections_Generic_IEnumerable_T")
System_Collections_Generic_IReadOnlyDictionary_TKey = typing.TypeVar("System_Collections_Generic_IReadOnlyDictionary_TKey")
System_Collections_Generic_IReadOnlyDictionary_TValue = typing.TypeVar("System_Collections_Generic_IReadOnlyDictionary_TValue")
System_Collections_Generic_List_T = typing.TypeVar("System_Collections_Generic_List_T")
System_Collections_Generic_List_ConvertAll_TOutput = typing.TypeVar("System_Collections_Generic_List_ConvertAll_TOutput")
System_Collections_Generic_IComparer_T = typing.TypeVar("System_Collections_Generic_IComparer_T")
System_Collections_Generic_ICollection_T = typing.TypeVar("System_Collections_Generic_ICollection_T")
System_Collections_Generic_IEnumerator_T = typing.TypeVar("System_Collections_Generic_IEnumerator_T")
System_Collections_Generic_CollectionExtensions_GetValueOrDefault_TValue = typing.TypeVar("System_Collections_Generic_CollectionExtensions_GetValueOrDefault_TValue")
System_Collections_Generic_CollectionExtensions_GetValueOrDefault_TKey = typing.TypeVar("System_Collections_Generic_CollectionExtensions_GetValueOrDefault_TKey")
System_Collections_Generic_CollectionExtensions_TryAdd_TKey = typing.TypeVar("System_Collections_Generic_CollectionExtensions_TryAdd_TKey")
System_Collections_Generic_CollectionExtensions_TryAdd_TValue = typing.TypeVar("System_Collections_Generic_CollectionExtensions_TryAdd_TValue")
System_Collections_Generic_CollectionExtensions_Remove_TKey = typing.TypeVar("System_Collections_Generic_CollectionExtensions_Remove_TKey")
System_Collections_Generic_CollectionExtensions_Remove_TValue = typing.TypeVar("System_Collections_Generic_CollectionExtensions_Remove_TValue")
System_Collections_Generic_CollectionExtensions_AsReadOnly_T = typing.TypeVar("System_Collections_Generic_CollectionExtensions_AsReadOnly_T")
System_Collections_Generic_CollectionExtensions_AsReadOnly_TKey = typing.TypeVar("System_Collections_Generic_CollectionExtensions_AsReadOnly_TKey")
System_Collections_Generic_CollectionExtensions_AsReadOnly_TValue = typing.TypeVar("System_Collections_Generic_CollectionExtensions_AsReadOnly_TValue")
System_Collections_Generic_CollectionExtensions_AddRange_T = typing.TypeVar("System_Collections_Generic_CollectionExtensions_AddRange_T")
System_Collections_Generic_CollectionExtensions_InsertRange_T = typing.TypeVar("System_Collections_Generic_CollectionExtensions_InsertRange_T")
System_Collections_Generic_CollectionExtensions_CopyTo_T = typing.TypeVar("System_Collections_Generic_CollectionExtensions_CopyTo_T")
System_Collections_Generic_EqualityComparer_T = typing.TypeVar("System_Collections_Generic_EqualityComparer_T")
System_Collections_Generic_GenericEqualityComparer_T = typing.TypeVar("System_Collections_Generic_GenericEqualityComparer_T")
System_Collections_Generic_NullableEqualityComparer_T = typing.TypeVar("System_Collections_Generic_NullableEqualityComparer_T")
System_Collections_Generic_ObjectEqualityComparer_T = typing.TypeVar("System_Collections_Generic_ObjectEqualityComparer_T")
System_Collections_Generic_EnumEqualityComparer_T = typing.TypeVar("System_Collections_Generic_EnumEqualityComparer_T")
System_Collections_Generic_Dictionary_TValue = typing.TypeVar("System_Collections_Generic_Dictionary_TValue")
System_Collections_Generic_Dictionary_TKey = typing.TypeVar("System_Collections_Generic_Dictionary_TKey")
System_Collections_Generic_SortedSet_T = typing.TypeVar("System_Collections_Generic_SortedSet_T")
System_Collections_Generic_SortedList_TKey = typing.TypeVar("System_Collections_Generic_SortedList_TKey")
System_Collections_Generic_SortedList_TValue = typing.TypeVar("System_Collections_Generic_SortedList_TValue")
System_Collections_Generic_SortedDictionary_TValue = typing.TypeVar("System_Collections_Generic_SortedDictionary_TValue")
System_Collections_Generic_SortedDictionary_TKey = typing.TypeVar("System_Collections_Generic_SortedDictionary_TKey")
System_Collections_Generic_TreeSet_T = typing.TypeVar("System_Collections_Generic_TreeSet_T")
System_Collections_Generic_Stack_T = typing.TypeVar("System_Collections_Generic_Stack_T")
System_Collections_Generic_LinkedList_T = typing.TypeVar("System_Collections_Generic_LinkedList_T")
System_Collections_Generic_LinkedListNode_T = typing.TypeVar("System_Collections_Generic_LinkedListNode_T")
System_Collections_Generic_PriorityQueue_TElement = typing.TypeVar("System_Collections_Generic_PriorityQueue_TElement")
System_Collections_Generic_PriorityQueue_TPriority = typing.TypeVar("System_Collections_Generic_PriorityQueue_TPriority")


class ICollection(typing.Generic[System_Collections_Generic_ICollection_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def Count(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def IsReadOnly(self) -> bool:
        ...

    def __contains__(self, item: System_Collections_Generic_ICollection_T) -> bool:
        ...

    def __len__(self) -> int:
        ...

    def Add(self, item: System_Collections_Generic_ICollection_T) -> None:
        ...

    def Clear(self) -> None:
        ...

    def Contains(self, item: System_Collections_Generic_ICollection_T) -> bool:
        ...

    def CopyTo(self, array: typing.List[System_Collections_Generic_ICollection_T], arrayIndex: int) -> None:
        ...

    def Remove(self, item: System_Collections_Generic_ICollection_T) -> bool:
        ...


class IList(typing.Generic[System_Collections_Generic_IList_T], System.Collections.Generic.ICollection[System_Collections_Generic_IList_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __getitem__(self, index: int) -> System_Collections_Generic_IList_T:
        ...

    def __setitem__(self, index: int, value: System_Collections_Generic_IList_T) -> None:
        ...

    def IndexOf(self, item: System_Collections_Generic_IList_T) -> int:
        ...

    def Insert(self, index: int, item: System_Collections_Generic_IList_T) -> None:
        ...

    def RemoveAt(self, index: int) -> None:
        ...


class IComparer(typing.Generic[System_Collections_Generic_IComparer_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def Compare(self, x: System_Collections_Generic_IComparer_T, y: System_Collections_Generic_IComparer_T) -> int:
        ...


class Comparer(typing.Generic[System_Collections_Generic_Comparer_T], System.Object, System.Collections.IComparer, System.Collections.Generic.IComparer[System_Collections_Generic_Comparer_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    Default: System.Collections.Generic.Comparer[System_Collections_Generic_Comparer_T]

    @overload
    def Compare(self, x: System_Collections_Generic_Comparer_T, y: System_Collections_Generic_Comparer_T) -> int:
        ...

    @overload
    def Compare(self, x: typing.Any, y: typing.Any) -> int:
        ...

    @staticmethod
    def Create(comparison: typing.Callable[[System_Collections_Generic_Comparer_T, System_Collections_Generic_Comparer_T], int]) -> System.Collections.Generic.Comparer[System_Collections_Generic_Comparer_T]:
        ...


class GenericComparer(typing.Generic[System_Collections_Generic_GenericComparer_T], System.Collections.Generic.Comparer[System_Collections_Generic_GenericComparer_T]):
    """This class has no documentation."""

    def Compare(self, x: System_Collections_Generic_GenericComparer_T, y: System_Collections_Generic_GenericComparer_T) -> int:
        ...

    def Equals(self, obj: typing.Any) -> bool:
        ...

    def GetHashCode(self) -> int:
        ...


class NullableComparer(typing.Generic[System_Collections_Generic_NullableComparer_T], System.Collections.Generic.Comparer[typing.Optional[System_Collections_Generic_NullableComparer_T]], System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def Compare(self, x: typing.Optional[System_Collections_Generic_NullableComparer_T], y: typing.Optional[System_Collections_Generic_NullableComparer_T]) -> int:
        ...

    def Equals(self, obj: typing.Any) -> bool:
        ...

    def GetHashCode(self) -> int:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class ObjectComparer(typing.Generic[System_Collections_Generic_ObjectComparer_T], System.Collections.Generic.Comparer[System_Collections_Generic_ObjectComparer_T]):
    """This class has no documentation."""

    def Compare(self, x: System_Collections_Generic_ObjectComparer_T, y: System_Collections_Generic_ObjectComparer_T) -> int:
        ...

    def Equals(self, obj: typing.Any) -> bool:
        ...

    def GetHashCode(self) -> int:
        ...


class IAsyncEnumerator(typing.Generic[System_Collections_Generic_IAsyncEnumerator_T], System.IAsyncDisposable, metaclass=abc.ABCMeta):
    """Supports a simple asynchronous iteration over a generic collection."""

    @property
    @abc.abstractmethod
    def Current(self) -> System_Collections_Generic_IAsyncEnumerator_T:
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    def MoveNextAsync(self) -> System.Threading.Tasks.ValueTask[bool]:
        """
        Advances the enumerator asynchronously to the next element of the collection.
        
        :returns: A ValueTask{Boolean} that will complete with a result of true if the enumerator was successfully advanced to the next element, or false if the enumerator has passed the end of the collection.
        """
        ...


class IAsyncEnumerable(typing.Generic[System_Collections_Generic_IAsyncEnumerable_T], metaclass=abc.ABCMeta):
    """Exposes an enumerator that provides asynchronous iteration over values of a specified type."""

    def GetAsyncEnumerator(self, cancellationToken: System.Threading.CancellationToken = ...) -> System.Collections.Generic.IAsyncEnumerator[System_Collections_Generic_IAsyncEnumerable_T]:
        """
        Returns an enumerator that iterates asynchronously through the collection.
        
        :param cancellationToken: A CancellationToken that may be used to cancel the asynchronous iteration.
        :returns: An enumerator that can be used to iterate asynchronously through the collection.
        """
        ...


class IReadOnlyCollection(typing.Generic[System_Collections_Generic_IReadOnlyCollection_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def Count(self) -> int:
        ...


class IReadOnlyList(typing.Generic[System_Collections_Generic_IReadOnlyList_T], System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_IReadOnlyList_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __getitem__(self, index: int) -> System_Collections_Generic_IReadOnlyList_T:
        ...


class KeyValuePair(typing.Generic[System_Collections_Generic_KeyValuePair_TKey, System_Collections_Generic_KeyValuePair_TValue]):
    """This class has no documentation."""

    @property
    def Key(self) -> System_Collections_Generic_KeyValuePair_TKey:
        ...

    @property
    def Value(self) -> System_Collections_Generic_KeyValuePair_TValue:
        ...

    def __init__(self, key: System_Collections_Generic_KeyValuePair_TKey, value: System_Collections_Generic_KeyValuePair_TValue) -> None:
        ...

    @staticmethod
    def Create(key: System_Collections_Generic_KeyValuePair_Create_TKey, value: System_Collections_Generic_KeyValuePair_Create_TValue) -> System.Collections.Generic.KeyValuePair[System_Collections_Generic_KeyValuePair_Create_TKey, System_Collections_Generic_KeyValuePair_Create_TValue]:
        ...

    def Deconstruct(self, key: typing.Optional[System_Collections_Generic_KeyValuePair_TKey], value: typing.Optional[System_Collections_Generic_KeyValuePair_TValue]) -> typing.Union[None, System_Collections_Generic_KeyValuePair_TKey, System_Collections_Generic_KeyValuePair_TValue]:
        ...

    def ToString(self) -> str:
        ...


class IEnumerator(typing.Generic[System_Collections_Generic_IEnumerator_T], System.IDisposable, System.Collections.IEnumerator, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def Current(self) -> System_Collections_Generic_IEnumerator_T:
        ...


class IEnumerable(typing.Generic[System_Collections_Generic_IEnumerable_T], System.Collections.IEnumerable, typing.Iterable[System_Collections_Generic_IEnumerable_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Generic_IEnumerable_T]:
        ...


class ISet(typing.Generic[System_Collections_Generic_ISet_T], System.Collections.Generic.ICollection[System_Collections_Generic_ISet_T], metaclass=abc.ABCMeta):
    """
    Generic collection that guarantees the uniqueness of its elements, as defined
    by some comparer. It also supports basic set operations such as Union, Intersection,
    Complement and Exclusive Complement.
    """

    def Add(self, item: System_Collections_Generic_ISet_T) -> bool:
        ...

    def ExceptWith(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> None:
        ...

    def IntersectWith(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> None:
        ...

    def IsProperSubsetOf(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> bool:
        ...

    def IsProperSupersetOf(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> bool:
        ...

    def IsSubsetOf(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> bool:
        ...

    def IsSupersetOf(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> bool:
        ...

    def Overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> bool:
        ...

    def SetEquals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> bool:
        ...

    def SymmetricExceptWith(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> None:
        ...

    def UnionWith(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> None:
        ...


class KeyNotFoundException(System.SystemException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...


class IDictionary(typing.Generic[System_Collections_Generic_IDictionary_TKey, System_Collections_Generic_IDictionary_TValue], System.Collections.Generic.ICollection[System.Collections.Generic.KeyValuePair[System_Collections_Generic_IDictionary_TKey, System_Collections_Generic_IDictionary_TValue]], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def Keys(self) -> System.Collections.Generic.ICollection[System_Collections_Generic_IDictionary_TKey]:
        ...

    @property
    @abc.abstractmethod
    def Values(self) -> System.Collections.Generic.ICollection[System_Collections_Generic_IDictionary_TValue]:
        ...

    def __contains__(self, key: System_Collections_Generic_IDictionary_TKey) -> bool:
        ...

    def __getitem__(self, key: System_Collections_Generic_IDictionary_TKey) -> System_Collections_Generic_IDictionary_TValue:
        ...

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: System_Collections_Generic_IDictionary_TKey, value: System_Collections_Generic_IDictionary_TValue) -> None:
        ...

    def Add(self, key: System_Collections_Generic_IDictionary_TKey, value: System_Collections_Generic_IDictionary_TValue) -> None:
        ...

    def ContainsKey(self, key: System_Collections_Generic_IDictionary_TKey) -> bool:
        ...

    def Remove(self, key: System_Collections_Generic_IDictionary_TKey) -> bool:
        ...

    def TryGetValue(self, key: System_Collections_Generic_IDictionary_TKey, value: typing.Optional[System_Collections_Generic_IDictionary_TValue]) -> typing.Union[bool, System_Collections_Generic_IDictionary_TValue]:
        ...


class Queue(typing.Generic[System_Collections_Generic_Queue_T], System.Object, System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_Queue_T], typing.Iterable[System_Collections_Generic_Queue_T]):
    """This class has no documentation."""

    class Enumerator:
        """This class has no documentation."""

        @property
        def Current(self) -> System_Collections_Generic_Queue_T:
            ...

        def Dispose(self) -> None:
            ...

        def MoveNext(self) -> bool:
            ...

        def Reset(self) -> None:
            ...

    @property
    def Count(self) -> int:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    def __contains__(self, item: System_Collections_Generic_Queue_T) -> bool:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_Queue_T]) -> None:
        ...

    def __len__(self) -> int:
        ...

    def Clear(self) -> None:
        ...

    def Contains(self, item: System_Collections_Generic_Queue_T) -> bool:
        ...

    @overload
    def CopyTo(self, array: typing.List[System_Collections_Generic_Queue_T], arrayIndex: int) -> None:
        ...

    @overload
    def CopyTo(self, array: System.Array, index: int) -> None:
        ...

    def Dequeue(self) -> System_Collections_Generic_Queue_T:
        ...

    def Enqueue(self, item: System_Collections_Generic_Queue_T) -> None:
        ...

    def EnsureCapacity(self, capacity: int) -> int:
        """
        Ensures that the capacity of this Queue is at least the specified .
        
        :param capacity: The minimum capacity to ensure.
        :returns: The new capacity of this queue.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.Queue.Enumerator:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Generic_Queue_T]:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        ...

    def Peek(self) -> System_Collections_Generic_Queue_T:
        ...

    def ToArray(self) -> typing.List[System_Collections_Generic_Queue_T]:
        ...

    def TrimExcess(self) -> None:
        ...

    def TryDequeue(self, result: typing.Optional[System_Collections_Generic_Queue_T]) -> typing.Union[bool, System_Collections_Generic_Queue_T]:
        ...

    def TryPeek(self, result: typing.Optional[System_Collections_Generic_Queue_T]) -> typing.Union[bool, System_Collections_Generic_Queue_T]:
        ...


class IEqualityComparer(typing.Generic[System_Collections_Generic_IEqualityComparer_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def Equals(self, x: System_Collections_Generic_IEqualityComparer_T, y: System_Collections_Generic_IEqualityComparer_T) -> bool:
        ...

    def GetHashCode(self, obj: System_Collections_Generic_IEqualityComparer_T) -> int:
        ...


class IReadOnlySet(typing.Generic[System_Collections_Generic_IReadOnlySet_T], System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_IReadOnlySet_T], metaclass=abc.ABCMeta):
    """Provides a readonly abstraction of a set."""

    def __contains__(self, item: System_Collections_Generic_IReadOnlySet_T) -> bool:
        """
        Determines if the set contains a specific item
        
        :param item: The item to check if the set contains.
        :returns: true if found; otherwise false.
        """
        ...

    def __len__(self) -> int:
        ...

    def Contains(self, item: System_Collections_Generic_IReadOnlySet_T) -> bool:
        """
        Determines if the set contains a specific item
        
        :param item: The item to check if the set contains.
        :returns: true if found; otherwise false.
        """
        ...

    def IsProperSubsetOf(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_IReadOnlySet_T]) -> bool:
        """
        Determines whether the current set is a proper (strict) subset of a specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set is a proper subset of other; otherwise false.
        """
        ...

    def IsProperSupersetOf(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_IReadOnlySet_T]) -> bool:
        """
        Determines whether the current set is a proper (strict) superset of a specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the collection is a proper superset of other; otherwise false.
        """
        ...

    def IsSubsetOf(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_IReadOnlySet_T]) -> bool:
        """
        Determine whether the current set is a subset of a specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set is a subset of other; otherwise false.
        """
        ...

    def IsSupersetOf(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_IReadOnlySet_T]) -> bool:
        """
        Determine whether the current set is a super set of a specified collection.
        
        :param other: The collection to compare to the current set
        :returns: true if the current set is a subset of other; otherwise false.
        """
        ...

    def Overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_IReadOnlySet_T]) -> bool:
        """
        Determines whether the current set overlaps with the specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set and other share at least one common element; otherwise, false.
        """
        ...

    def SetEquals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_IReadOnlySet_T]) -> bool:
        """
        Determines whether the current set and the specified collection contain the same elements.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set is equal to other; otherwise, false.
        """
        ...


class HashSet(typing.Generic[System_Collections_Generic_HashSet_T], System.Object, System.Collections.Generic.ISet[System_Collections_Generic_HashSet_T], System.Collections.Generic.IReadOnlySet[System_Collections_Generic_HashSet_T], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, typing.Iterable[System_Collections_Generic_HashSet_T]):
    """This class has no documentation."""

    class Enumerator:
        """This class has no documentation."""

        @property
        def Current(self) -> System_Collections_Generic_HashSet_T:
            ...

        def Dispose(self) -> None:
            ...

        def MoveNext(self) -> bool:
            ...

        def Reset(self) -> None:
            ...

    @property
    def Count(self) -> int:
        """Gets the number of elements that are contained in the set."""
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Generic_HashSet_T]:
        """Gets the IEqualityComparer object that is used to determine equality for the values in the set."""
        ...

    def __contains__(self, item: System_Collections_Generic_HashSet_T) -> bool:
        """
        Determines whether the HashSet{T} contains the specified element.
        
        :param item: The element to locate in the HashSet{T} object.
        :returns: true if the HashSet{T} object contains the specified element; otherwise, false.
        """
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_HashSet_T]) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T], comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_HashSet_T]) -> None:
        ...

    @overload
    def __init__(self, capacity: int, comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_HashSet_T]) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...

    def __len__(self) -> int:
        ...

    @overload
    def Add(self, item: System_Collections_Generic_HashSet_T) -> None:
        ...

    @overload
    def Add(self, item: System_Collections_Generic_HashSet_T) -> bool:
        ...

    def Clear(self) -> None:
        """Removes all elements from the HashSet{T} object."""
        ...

    def Contains(self, item: System_Collections_Generic_HashSet_T) -> bool:
        """
        Determines whether the HashSet{T} contains the specified element.
        
        :param item: The element to locate in the HashSet{T} object.
        :returns: true if the HashSet{T} object contains the specified element; otherwise, false.
        """
        ...

    @overload
    def CopyTo(self, array: typing.List[System_Collections_Generic_HashSet_T]) -> None:
        ...

    @overload
    def CopyTo(self, array: typing.List[System_Collections_Generic_HashSet_T], arrayIndex: int) -> None:
        """
        Copies the elements of a HashSet{T} object to an array, starting at the specified array index.
        
        :param array: The destination array.
        :param arrayIndex: The zero-based index in array at which copying begins.
        """
        ...

    @overload
    def CopyTo(self, array: typing.List[System_Collections_Generic_HashSet_T], arrayIndex: int, count: int) -> None:
        ...

    @staticmethod
    def CreateSetComparer() -> System.Collections.Generic.IEqualityComparer[System.Collections.Generic.HashSet[System_Collections_Generic_HashSet_T]]:
        ...

    def EnsureCapacity(self, capacity: int) -> int:
        """Ensures that this hash set can hold the specified number of elements without growing."""
        ...

    def ExceptWith(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> None:
        """
        Removes all elements in the specified collection from the current HashSet{T} object.
        
        :param other: The collection to compare to the current HashSet{T} object.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.HashSet.Enumerator:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Generic_HashSet_T]:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def IntersectWith(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> None:
        """
        Modifies the current HashSet{T} object to contain only elements that are present in that object and in the specified collection.
        
        :param other: The collection to compare to the current HashSet{T} object.
        """
        ...

    def IsProperSubsetOf(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> bool:
        """
        Determines whether a HashSet{T} object is a proper subset of the specified collection.
        
        :param other: The collection to compare to the current HashSet{T} object.
        :returns: true if the HashSet{T} object is a proper subset of ; otherwise, false.
        """
        ...

    def IsProperSupersetOf(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> bool:
        """
        Determines whether a HashSet{T} object is a proper superset of the specified collection.
        
        :param other: The collection to compare to the current HashSet{T} object.
        :returns: true if the HashSet{T} object is a proper superset of ; otherwise, false.
        """
        ...

    def IsSubsetOf(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> bool:
        """
        Determines whether a HashSet{T} object is a subset of the specified collection.
        
        :param other: The collection to compare to the current HashSet{T} object.
        :returns: true if the HashSet{T} object is a subset of ; otherwise, false.
        """
        ...

    def IsSupersetOf(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> bool:
        """
        Determines whether a HashSet{T} object is a proper superset of the specified collection.
        
        :param other: The collection to compare to the current HashSet{T} object.
        :returns: true if the HashSet{T} object is a superset of ; otherwise, false.
        """
        ...

    def OnDeserialization(self, sender: typing.Any) -> None:
        ...

    def Overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> bool:
        """
        Determines whether the current HashSet{T} object and a specified collection share common elements.
        
        :param other: The collection to compare to the current HashSet{T} object.
        :returns: true if the HashSet{T} object and  share at least one common element; otherwise, false.
        """
        ...

    def Remove(self, item: System_Collections_Generic_HashSet_T) -> bool:
        ...

    def RemoveWhere(self, match: typing.Callable[[System_Collections_Generic_HashSet_T], bool]) -> int:
        """Removes all elements that match the conditions defined by the specified predicate from a HashSet{T} collection."""
        ...

    def SetEquals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> bool:
        """
        Determines whether a HashSet{T} object and the specified collection contain the same elements.
        
        :param other: The collection to compare to the current HashSet{T} object.
        :returns: true if the HashSet{T} object is equal to ; otherwise, false.
        """
        ...

    def SymmetricExceptWith(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> None:
        """
        Modifies the current HashSet{T} object to contain only elements that are present either in that object or in the specified collection, but not both.
        
        :param other: The collection to compare to the current HashSet{T} object.
        """
        ...

    def TrimExcess(self) -> None:
        """
        Sets the capacity of a HashSet{T} object to the actual number of elements it contains,
        rounded up to a nearby, implementation-specific value.
        """
        ...

    def TryGetValue(self, equalValue: System_Collections_Generic_HashSet_T, actualValue: typing.Optional[System_Collections_Generic_HashSet_T]) -> typing.Union[bool, System_Collections_Generic_HashSet_T]:
        """
        Searches the set for a given value and returns the equal value it finds, if any.
        
        :param equalValue: The value to search for.
        :param actualValue: The value from the set that the search found, or the default value of T when the search yielded no match.
        :returns: A value indicating whether the search was successful.
        """
        ...

    def UnionWith(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> None:
        """
        Modifies the current HashSet{T} object to contain all elements that are present in itself, the specified collection, or both.
        
        :param other: The collection to compare to the current HashSet{T} object.
        """
        ...


class IReadOnlyDictionary(typing.Generic[System_Collections_Generic_IReadOnlyDictionary_TKey, System_Collections_Generic_IReadOnlyDictionary_TValue], System.Collections.Generic.IReadOnlyCollection[System.Collections.Generic.KeyValuePair[System_Collections_Generic_IReadOnlyDictionary_TKey, System_Collections_Generic_IReadOnlyDictionary_TValue]], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def Keys(self) -> System.Collections.Generic.IEnumerable[System_Collections_Generic_IReadOnlyDictionary_TKey]:
        ...

    @property
    @abc.abstractmethod
    def Values(self) -> System.Collections.Generic.IEnumerable[System_Collections_Generic_IReadOnlyDictionary_TValue]:
        ...

    def __contains__(self, key: System_Collections_Generic_IReadOnlyDictionary_TKey) -> bool:
        ...

    def __getitem__(self, key: System_Collections_Generic_IReadOnlyDictionary_TKey) -> System_Collections_Generic_IReadOnlyDictionary_TValue:
        ...

    def __len__(self) -> int:
        ...

    def ContainsKey(self, key: System_Collections_Generic_IReadOnlyDictionary_TKey) -> bool:
        ...

    def TryGetValue(self, key: System_Collections_Generic_IReadOnlyDictionary_TKey, value: typing.Optional[System_Collections_Generic_IReadOnlyDictionary_TValue]) -> typing.Union[bool, System_Collections_Generic_IReadOnlyDictionary_TValue]:
        ...


class List(typing.Generic[System_Collections_Generic_List_T], System.Object, System.Collections.Generic.IList[System_Collections_Generic_List_T], System.Collections.IList, System.Collections.Generic.IReadOnlyList[System_Collections_Generic_List_T], typing.Iterable[System_Collections_Generic_List_T]):
    """This class has no documentation."""

    class Enumerator:
        """This class has no documentation."""

        @property
        def Current(self) -> System_Collections_Generic_List_T:
            ...

        def Dispose(self) -> None:
            ...

        def MoveNext(self) -> bool:
            ...

        def Reset(self) -> None:
            ...

    @property
    def _items(self) -> typing.List[System_Collections_Generic_List_T]:
        ...

    @_items.setter
    def _items(self, value: typing.List[System_Collections_Generic_List_T]):
        ...

    @property
    def _size(self) -> int:
        ...

    @_size.setter
    def _size(self, value: int):
        ...

    @property
    def _version(self) -> int:
        ...

    @_version.setter
    def _version(self, value: int):
        ...

    @property
    def Capacity(self) -> int:
        ...

    @Capacity.setter
    def Capacity(self, value: int):
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def IsFixedSize(self) -> bool:
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
    def __contains__(self, item: System_Collections_Generic_List_T) -> bool:
        ...

    @overload
    def __contains__(self, item: typing.Any) -> bool:
        ...

    @overload
    def __getitem__(self, index: int) -> System_Collections_Generic_List_T:
        ...

    @overload
    def __getitem__(self, index: int) -> typing.Any:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_List_T]) -> None:
        ...

    def __len__(self) -> int:
        ...

    @overload
    def __setitem__(self, index: int, value: System_Collections_Generic_List_T) -> None:
        ...

    @overload
    def __setitem__(self, index: int, value: typing.Any) -> None:
        ...

    @overload
    def Add(self, item: System_Collections_Generic_List_T) -> None:
        ...

    @overload
    def Add(self, item: typing.Any) -> int:
        ...

    def AddRange(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_List_T]) -> None:
        ...

    def AsReadOnly(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System_Collections_Generic_List_T]:
        ...

    @overload
    def BinarySearch(self, index: int, count: int, item: System_Collections_Generic_List_T, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_List_T]) -> int:
        ...

    @overload
    def BinarySearch(self, item: System_Collections_Generic_List_T) -> int:
        ...

    @overload
    def BinarySearch(self, item: System_Collections_Generic_List_T, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_List_T]) -> int:
        ...

    def Clear(self) -> None:
        ...

    @overload
    def Contains(self, item: System_Collections_Generic_List_T) -> bool:
        ...

    @overload
    def Contains(self, item: typing.Any) -> bool:
        ...

    def ConvertAll(self, converter: typing.Callable[[System_Collections_Generic_List_T], System_Collections_Generic_List_ConvertAll_TOutput]) -> System.Collections.Generic.List[System_Collections_Generic_List_ConvertAll_TOutput]:
        ...

    @overload
    def CopyTo(self, array: typing.List[System_Collections_Generic_List_T]) -> None:
        ...

    @overload
    def CopyTo(self, array: System.Array, arrayIndex: int) -> None:
        ...

    @overload
    def CopyTo(self, index: int, array: typing.List[System_Collections_Generic_List_T], arrayIndex: int, count: int) -> None:
        ...

    @overload
    def CopyTo(self, array: typing.List[System_Collections_Generic_List_T], arrayIndex: int) -> None:
        ...

    def EnsureCapacity(self, capacity: int) -> int:
        """
        Ensures that the capacity of this list is at least the specified .
        If the current capacity of the list is less than specified ,
        the capacity is increased by continuously twice current capacity until it is at least the specified .
        
        :param capacity: The minimum capacity to ensure.
        :returns: The new capacity of this list.
        """
        ...

    def Exists(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> bool:
        ...

    def Find(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> System_Collections_Generic_List_T:
        ...

    def FindAll(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> System.Collections.Generic.List[System_Collections_Generic_List_T]:
        ...

    @overload
    def FindIndex(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> int:
        ...

    @overload
    def FindIndex(self, startIndex: int, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> int:
        ...

    @overload
    def FindIndex(self, startIndex: int, count: int, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> int:
        ...

    def FindLast(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> System_Collections_Generic_List_T:
        ...

    @overload
    def FindLastIndex(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> int:
        ...

    @overload
    def FindLastIndex(self, startIndex: int, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> int:
        ...

    @overload
    def FindLastIndex(self, startIndex: int, count: int, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> int:
        ...

    def ForEach(self, action: typing.Callable[[System_Collections_Generic_List_T], None]) -> None:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.List.Enumerator:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Generic_List_T]:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        ...

    def GetRange(self, index: int, count: int) -> System.Collections.Generic.List[System_Collections_Generic_List_T]:
        ...

    @overload
    def IndexOf(self, item: System_Collections_Generic_List_T) -> int:
        ...

    @overload
    def IndexOf(self, item: typing.Any) -> int:
        ...

    @overload
    def IndexOf(self, item: System_Collections_Generic_List_T, index: int) -> int:
        ...

    @overload
    def IndexOf(self, item: System_Collections_Generic_List_T, index: int, count: int) -> int:
        ...

    @overload
    def Insert(self, index: int, item: System_Collections_Generic_List_T) -> None:
        ...

    @overload
    def Insert(self, index: int, item: typing.Any) -> None:
        ...

    def InsertRange(self, index: int, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_List_T]) -> None:
        ...

    @overload
    def LastIndexOf(self, item: System_Collections_Generic_List_T) -> int:
        ...

    @overload
    def LastIndexOf(self, item: System_Collections_Generic_List_T, index: int) -> int:
        ...

    @overload
    def LastIndexOf(self, item: System_Collections_Generic_List_T, index: int, count: int) -> int:
        ...

    @overload
    def Remove(self, item: System_Collections_Generic_List_T) -> bool:
        ...

    @overload
    def Remove(self, item: typing.Any) -> None:
        ...

    def RemoveAll(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> int:
        ...

    def RemoveAt(self, index: int) -> None:
        ...

    def RemoveRange(self, index: int, count: int) -> None:
        ...

    @overload
    def Reverse(self) -> None:
        ...

    @overload
    def Reverse(self, index: int, count: int) -> None:
        ...

    def Slice(self, start: int, length: int) -> System.Collections.Generic.List[System_Collections_Generic_List_T]:
        """
        Creates a shallow copy of a range of elements in the source List{T}.
        
        :param start: The zero-based List{T} index at which the range starts.
        :param length: The length of the range.
        :returns: A shallow copy of a range of elements in the source List{T}.
        """
        ...

    @overload
    def Sort(self) -> None:
        ...

    @overload
    def Sort(self, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_List_T]) -> None:
        ...

    @overload
    def Sort(self, index: int, count: int, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_List_T]) -> None:
        ...

    @overload
    def Sort(self, comparison: typing.Callable[[System_Collections_Generic_List_T, System_Collections_Generic_List_T], int]) -> None:
        ...

    def ToArray(self) -> typing.List[System_Collections_Generic_List_T]:
        ...

    def TrimExcess(self) -> None:
        ...

    def TrueForAll(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> bool:
        ...


class CollectionExtensions(System.Object):
    """This class has no documentation."""

    @staticmethod
    def AddRange(list: System.Collections.Generic.List[System_Collections_Generic_CollectionExtensions_AddRange_T], source: System.ReadOnlySpan[System_Collections_Generic_CollectionExtensions_AddRange_T]) -> None:
        """
        Adds the elements of the specified span to the end of the List{T}.
        
        :param list: The list to which the elements should be added.
        :param source: The span whose elements should be added to the end of the List{T}.
        """
        ...

    @staticmethod
    @overload
    def AsReadOnly(list: System.Collections.Generic.IList[System_Collections_Generic_CollectionExtensions_AsReadOnly_T]) -> System.Collections.ObjectModel.ReadOnlyCollection[System_Collections_Generic_CollectionExtensions_AsReadOnly_T]:
        """
        Returns a read-only ReadOnlyCollection{T} wrapper
        for the specified list.
        
        :param list: The list to wrap.
        :returns: An object that acts as a read-only wrapper around the current IList{T}.
        """
        ...

    @staticmethod
    @overload
    def AsReadOnly(dictionary: System.Collections.Generic.IDictionary[System_Collections_Generic_CollectionExtensions_AsReadOnly_TKey, System_Collections_Generic_CollectionExtensions_AsReadOnly_TValue]) -> System.Collections.ObjectModel.ReadOnlyDictionary[System_Collections_Generic_CollectionExtensions_AsReadOnly_TKey, System_Collections_Generic_CollectionExtensions_AsReadOnly_TValue]:
        """
        Returns a read-only ReadOnlyDictionary{TKey, TValue} wrapper
        for the current dictionary.
        
        :param dictionary: The dictionary to wrap.
        :returns: An object that acts as a read-only wrapper around the current IDictionary{TKey, TValue}.
        """
        ...

    @staticmethod
    def CopyTo(list: System.Collections.Generic.List[System_Collections_Generic_CollectionExtensions_CopyTo_T], destination: System.Span[System_Collections_Generic_CollectionExtensions_CopyTo_T]) -> None:
        """
        Copies the entire List{T} to a span.
        
        :param list: The list from which the elements are copied.
        :param destination: The span that is the destination of the elements copied from .
        """
        ...

    @staticmethod
    @overload
    def GetValueOrDefault(dictionary: System.Collections.Generic.IReadOnlyDictionary[System_Collections_Generic_CollectionExtensions_GetValueOrDefault_TKey, System_Collections_Generic_CollectionExtensions_GetValueOrDefault_TValue], key: System_Collections_Generic_CollectionExtensions_GetValueOrDefault_TKey) -> System_Collections_Generic_CollectionExtensions_GetValueOrDefault_TValue:
        ...

    @staticmethod
    @overload
    def GetValueOrDefault(dictionary: System.Collections.Generic.IReadOnlyDictionary[System_Collections_Generic_CollectionExtensions_GetValueOrDefault_TKey, System_Collections_Generic_CollectionExtensions_GetValueOrDefault_TValue], key: System_Collections_Generic_CollectionExtensions_GetValueOrDefault_TKey, defaultValue: System_Collections_Generic_CollectionExtensions_GetValueOrDefault_TValue) -> System_Collections_Generic_CollectionExtensions_GetValueOrDefault_TValue:
        ...

    @staticmethod
    def InsertRange(list: System.Collections.Generic.List[System_Collections_Generic_CollectionExtensions_InsertRange_T], index: int, source: System.ReadOnlySpan[System_Collections_Generic_CollectionExtensions_InsertRange_T]) -> None:
        """
        Inserts the elements of a span into the List{T} at the specified index.
        
        :param list: The list into which the elements should be inserted.
        :param index: The zero-based index at which the new elements should be inserted.
        :param source: The span whose elements should be added to the List{T}.
        """
        ...

    @staticmethod
    def Remove(dictionary: System.Collections.Generic.IDictionary[System_Collections_Generic_CollectionExtensions_Remove_TKey, System_Collections_Generic_CollectionExtensions_Remove_TValue], key: System_Collections_Generic_CollectionExtensions_Remove_TKey, value: typing.Optional[System_Collections_Generic_CollectionExtensions_Remove_TValue]) -> typing.Union[bool, System_Collections_Generic_CollectionExtensions_Remove_TValue]:
        ...

    @staticmethod
    def TryAdd(dictionary: System.Collections.Generic.IDictionary[System_Collections_Generic_CollectionExtensions_TryAdd_TKey, System_Collections_Generic_CollectionExtensions_TryAdd_TValue], key: System_Collections_Generic_CollectionExtensions_TryAdd_TKey, value: System_Collections_Generic_CollectionExtensions_TryAdd_TValue) -> bool:
        ...


class EqualityComparer(typing.Generic[System_Collections_Generic_EqualityComparer_T], System.Object, System.Collections.IEqualityComparer, System.Collections.Generic.IEqualityComparer[System_Collections_Generic_EqualityComparer_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    Default: System.Collections.Generic.EqualityComparer[System_Collections_Generic_EqualityComparer_T]

    @staticmethod
    def Create(equals: typing.Callable[[System_Collections_Generic_EqualityComparer_T, System_Collections_Generic_EqualityComparer_T], bool], getHashCode: typing.Callable[[System_Collections_Generic_EqualityComparer_T], int] = None) -> System.Collections.Generic.EqualityComparer[System_Collections_Generic_EqualityComparer_T]:
        ...

    @overload
    def Equals(self, x: System_Collections_Generic_EqualityComparer_T, y: System_Collections_Generic_EqualityComparer_T) -> bool:
        ...

    @overload
    def Equals(self, x: typing.Any, y: typing.Any) -> bool:
        ...

    @overload
    def GetHashCode(self, obj: System_Collections_Generic_EqualityComparer_T) -> int:
        ...

    @overload
    def GetHashCode(self, obj: typing.Any) -> int:
        ...


class GenericEqualityComparer(typing.Generic[System_Collections_Generic_GenericEqualityComparer_T], System.Collections.Generic.EqualityComparer[System_Collections_Generic_GenericEqualityComparer_T]):
    """This class has no documentation."""

    @overload
    def Equals(self, x: System_Collections_Generic_GenericEqualityComparer_T, y: System_Collections_Generic_GenericEqualityComparer_T) -> bool:
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def GetHashCode(self, obj: System_Collections_Generic_GenericEqualityComparer_T) -> int:
        ...

    @overload
    def GetHashCode(self) -> int:
        ...


class NullableEqualityComparer(typing.Generic[System_Collections_Generic_NullableEqualityComparer_T], System.Collections.Generic.EqualityComparer[typing.Optional[System_Collections_Generic_NullableEqualityComparer_T]], System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    @overload
    def Equals(self, x: typing.Optional[System_Collections_Generic_NullableEqualityComparer_T], y: typing.Optional[System_Collections_Generic_NullableEqualityComparer_T]) -> bool:
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def GetHashCode(self, obj: typing.Optional[System_Collections_Generic_NullableEqualityComparer_T]) -> int:
        ...

    @overload
    def GetHashCode(self) -> int:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class ObjectEqualityComparer(typing.Generic[System_Collections_Generic_ObjectEqualityComparer_T], System.Collections.Generic.EqualityComparer[System_Collections_Generic_ObjectEqualityComparer_T]):
    """This class has no documentation."""

    @overload
    def Equals(self, x: System_Collections_Generic_ObjectEqualityComparer_T, y: System_Collections_Generic_ObjectEqualityComparer_T) -> bool:
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def GetHashCode(self, obj: System_Collections_Generic_ObjectEqualityComparer_T) -> int:
        ...

    @overload
    def GetHashCode(self) -> int:
        ...


class ByteEqualityComparer(System.Collections.Generic.EqualityComparer[int]):
    """This class has no documentation."""

    @overload
    def Equals(self, x: int, y: int) -> bool:
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def GetHashCode(self, b: int) -> int:
        ...

    @overload
    def GetHashCode(self) -> int:
        ...


class EnumEqualityComparer(typing.Generic[System_Collections_Generic_EnumEqualityComparer_T], System.Collections.Generic.EqualityComparer[System_Collections_Generic_EnumEqualityComparer_T], System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def Equals(self, x: System_Collections_Generic_EnumEqualityComparer_T, y: System_Collections_Generic_EnumEqualityComparer_T) -> bool:
        ...

    @overload
    def GetHashCode(self, obj: System_Collections_Generic_EnumEqualityComparer_T) -> int:
        ...

    @overload
    def GetHashCode(self) -> int:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class Dictionary(typing.Generic[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue], System.Object, System.Collections.Generic.IDictionary[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue], System.Collections.IDictionary, System.Collections.Generic.IReadOnlyDictionary[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]]):
    """This class has no documentation."""

    class Enumerator(System.Collections.IDictionaryEnumerator):
        """This class has no documentation."""

        DictEntry: int = 1

        KeyValuePair: int = 2

        @property
        def Current(self) -> System.Collections.Generic.KeyValuePair[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]:
            ...

        @property
        def Entry(self) -> System.Collections.DictionaryEntry:
            ...

        @property
        def Key(self) -> System.Object:
            ...

        @property
        def Value(self) -> System.Object:
            ...

        def Dispose(self) -> None:
            ...

        def MoveNext(self) -> bool:
            ...

        def Reset(self) -> None:
            ...

    class KeyCollection(System.Object, System.Collections.Generic.ICollection[System_Collections_Generic_Dictionary_TKey], System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_Dictionary_TKey], typing.Iterable[System_Collections_Generic_Dictionary_TKey]):
        """This class has no documentation."""

        class Enumerator:
            """This class has no documentation."""

            @property
            def Current(self) -> System_Collections_Generic_Dictionary_TKey:
                ...

            def Dispose(self) -> None:
                ...

            def MoveNext(self) -> bool:
                ...

            def Reset(self) -> None:
                ...

        @property
        def Count(self) -> int:
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

        def __contains__(self, item: System_Collections_Generic_Dictionary_TKey) -> bool:
            ...

        def __init__(self, dictionary: System.Collections.Generic.Dictionary[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]) -> None:
            ...

        def __len__(self) -> int:
            ...

        def Add(self, item: System_Collections_Generic_Dictionary_TKey) -> None:
            ...

        def Clear(self) -> None:
            ...

        def Contains(self, item: System_Collections_Generic_Dictionary_TKey) -> bool:
            ...

        @overload
        def CopyTo(self, array: typing.List[System_Collections_Generic_Dictionary_TKey], index: int) -> None:
            ...

        @overload
        def CopyTo(self, array: System.Array, index: int) -> None:
            ...

        @overload
        def GetEnumerator(self) -> System.Collections.Generic.Dictionary.KeyCollection.Enumerator:
            ...

        @overload
        def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Generic_Dictionary_TKey]:
            ...

        @overload
        def GetEnumerator(self) -> System.Collections.IEnumerator:
            ...

        def Remove(self, item: System_Collections_Generic_Dictionary_TKey) -> bool:
            ...

    class ValueCollection(System.Object, System.Collections.Generic.ICollection[System_Collections_Generic_Dictionary_TValue], System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_Dictionary_TValue], typing.Iterable[System_Collections_Generic_Dictionary_TValue]):
        """This class has no documentation."""

        class Enumerator:
            """This class has no documentation."""

            @property
            def Current(self) -> System_Collections_Generic_Dictionary_TValue:
                ...

            def Dispose(self) -> None:
                ...

            def MoveNext(self) -> bool:
                ...

            def Reset(self) -> None:
                ...

        @property
        def Count(self) -> int:
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

        def __contains__(self, item: System_Collections_Generic_Dictionary_TValue) -> bool:
            ...

        def __init__(self, dictionary: System.Collections.Generic.Dictionary[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]) -> None:
            ...

        def __len__(self) -> int:
            ...

        def Add(self, item: System_Collections_Generic_Dictionary_TValue) -> None:
            ...

        def Clear(self) -> None:
            ...

        def Contains(self, item: System_Collections_Generic_Dictionary_TValue) -> bool:
            ...

        @overload
        def CopyTo(self, array: typing.List[System_Collections_Generic_Dictionary_TValue], index: int) -> None:
            ...

        @overload
        def CopyTo(self, array: System.Array, index: int) -> None:
            ...

        @overload
        def GetEnumerator(self) -> System.Collections.Generic.Dictionary.ValueCollection.Enumerator:
            ...

        @overload
        def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Generic_Dictionary_TValue]:
            ...

        @overload
        def GetEnumerator(self) -> System.Collections.IEnumerator:
            ...

        def Remove(self, item: System_Collections_Generic_Dictionary_TValue) -> bool:
            ...

    @property
    def Comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Generic_Dictionary_TKey]:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def Keys(self) -> System.Collections.Generic.Dictionary.KeyCollection:
        ...

    @property
    def Values(self) -> System.Collections.Generic.Dictionary.ValueCollection:
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

    @property
    def IsFixedSize(self) -> bool:
        ...

    @overload
    def __contains__(self, keyValuePair: System.Collections.Generic.KeyValuePair[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]) -> bool:
        ...

    @overload
    def __contains__(self, key: System_Collections_Generic_Dictionary_TKey) -> bool:
        ...

    @overload
    def __contains__(self, key: typing.Any) -> bool:
        ...

    @overload
    def __getitem__(self, key: System_Collections_Generic_Dictionary_TKey) -> System_Collections_Generic_Dictionary_TValue:
        ...

    @overload
    def __getitem__(self, key: typing.Any) -> typing.Any:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_Dictionary_TKey]) -> None:
        ...

    @overload
    def __init__(self, capacity: int, comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_Dictionary_TKey]) -> None:
        ...

    @overload
    def __init__(self, dictionary: System.Collections.Generic.IDictionary[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]) -> None:
        ...

    @overload
    def __init__(self, dictionary: System.Collections.Generic.IDictionary[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue], comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_Dictionary_TKey]) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]]) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]], comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_Dictionary_TKey]) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...

    def __len__(self) -> int:
        ...

    @overload
    def __setitem__(self, key: System_Collections_Generic_Dictionary_TKey, value: System_Collections_Generic_Dictionary_TValue) -> None:
        ...

    @overload
    def __setitem__(self, key: typing.Any, value: typing.Any) -> None:
        ...

    @overload
    def Add(self, key: System_Collections_Generic_Dictionary_TKey, value: System_Collections_Generic_Dictionary_TValue) -> None:
        ...

    @overload
    def Add(self, keyValuePair: System.Collections.Generic.KeyValuePair[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]) -> None:
        ...

    @overload
    def Add(self, key: typing.Any, value: typing.Any) -> None:
        ...

    def Clear(self) -> None:
        ...

    @overload
    def Contains(self, keyValuePair: System.Collections.Generic.KeyValuePair[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]) -> bool:
        ...

    @overload
    def Contains(self, key: typing.Any) -> bool:
        ...

    def ContainsKey(self, key: System_Collections_Generic_Dictionary_TKey) -> bool:
        ...

    def ContainsValue(self, value: System_Collections_Generic_Dictionary_TValue) -> bool:
        ...

    @overload
    def CopyTo(self, array: typing.List[System.Collections.Generic.KeyValuePair[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]], index: int) -> None:
        ...

    @overload
    def CopyTo(self, array: System.Array, index: int) -> None:
        ...

    def EnsureCapacity(self, capacity: int) -> int:
        """Ensures that the dictionary can hold up to 'capacity' entries without any further expansion of its backing storage"""
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.Dictionary.Enumerator:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]]:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IDictionaryEnumerator:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def OnDeserialization(self, sender: typing.Any) -> None:
        ...

    @overload
    def Remove(self, keyValuePair: System.Collections.Generic.KeyValuePair[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]) -> bool:
        ...

    @overload
    def Remove(self, key: System_Collections_Generic_Dictionary_TKey) -> bool:
        ...

    @overload
    def Remove(self, key: System_Collections_Generic_Dictionary_TKey, value: typing.Optional[System_Collections_Generic_Dictionary_TValue]) -> typing.Union[bool, System_Collections_Generic_Dictionary_TValue]:
        ...

    @overload
    def Remove(self, key: typing.Any) -> None:
        ...

    @overload
    def TrimExcess(self) -> None:
        """Sets the capacity of this dictionary to what it would be if it had been originally initialized with all its entries"""
        ...

    @overload
    def TrimExcess(self, capacity: int) -> None:
        """Sets the capacity of this dictionary to hold up 'capacity' entries without any further expansion of its backing storage"""
        ...

    def TryAdd(self, key: System_Collections_Generic_Dictionary_TKey, value: System_Collections_Generic_Dictionary_TValue) -> bool:
        ...

    def TryGetValue(self, key: System_Collections_Generic_Dictionary_TKey, value: typing.Optional[System_Collections_Generic_Dictionary_TValue]) -> typing.Union[bool, System_Collections_Generic_Dictionary_TValue]:
        ...


class NonRandomizedStringEqualityComparer(System.Object, System.Collections.Generic.IInternalStringEqualityComparer, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    def __init__(self, information: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...

    def Equals(self, x: str, y: str) -> bool:
        ...

    def GetHashCode(self, obj: str) -> int:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    @staticmethod
    def GetStringComparer(comparer: typing.Any) -> System.Collections.Generic.IEqualityComparer[str]:
        ...

    def GetUnderlyingEqualityComparer(self) -> System.Collections.Generic.IEqualityComparer[str]:
        ...


class SortedSet(typing.Generic[System_Collections_Generic_SortedSet_T], System.Object, System.Collections.Generic.ISet[System_Collections_Generic_SortedSet_T], System.Collections.Generic.IReadOnlySet[System_Collections_Generic_SortedSet_T], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, typing.Iterable[System_Collections_Generic_SortedSet_T]):
    """This class has no documentation."""

    class Enumerator(System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback):
        """This class has no documentation."""

        @property
        def Current(self) -> System_Collections_Generic_SortedSet_T:
            ...

        @property
        def NotStartedOrEnded(self) -> bool:
            ...

        def Dispose(self) -> None:
            ...

        def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
            ...

        def MoveNext(self) -> bool:
            ...

        def OnDeserialization(self, sender: typing.Any) -> None:
            ...

        def Reset(self) -> None:
            ...

    StackAllocThreshold: int = 100

    @property
    def Count(self) -> int:
        ...

    @property
    def Comparer(self) -> System.Collections.Generic.IComparer[System_Collections_Generic_SortedSet_T]:
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

    @property
    def Min(self) -> System_Collections_Generic_SortedSet_T:
        ...

    @property
    def MinInternal(self) -> System_Collections_Generic_SortedSet_T:
        ...

    @property
    def Max(self) -> System_Collections_Generic_SortedSet_T:
        ...

    @property
    def MaxInternal(self) -> System_Collections_Generic_SortedSet_T:
        ...

    def __contains__(self, item: System_Collections_Generic_SortedSet_T) -> bool:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedSet_T]) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T], comparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedSet_T]) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...

    def __len__(self) -> int:
        ...

    @overload
    def Add(self, item: System_Collections_Generic_SortedSet_T) -> bool:
        ...

    @overload
    def Add(self, item: System_Collections_Generic_SortedSet_T) -> None:
        ...

    def Clear(self) -> None:
        ...

    def Contains(self, item: System_Collections_Generic_SortedSet_T) -> bool:
        ...

    @overload
    def CopyTo(self, array: typing.List[System_Collections_Generic_SortedSet_T]) -> None:
        ...

    @overload
    def CopyTo(self, array: typing.List[System_Collections_Generic_SortedSet_T], index: int) -> None:
        ...

    @overload
    def CopyTo(self, array: typing.List[System_Collections_Generic_SortedSet_T], index: int, count: int) -> None:
        ...

    @overload
    def CopyTo(self, array: System.Array, index: int) -> None:
        ...

    @staticmethod
    @overload
    def CreateSetComparer() -> System.Collections.Generic.IEqualityComparer[System.Collections.Generic.SortedSet[System_Collections_Generic_SortedSet_T]]:
        """Returns an IEqualityComparer{T} object that can be used to create a collection that contains individual sets."""
        ...

    @staticmethod
    @overload
    def CreateSetComparer(memberEqualityComparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_SortedSet_T]) -> System.Collections.Generic.IEqualityComparer[System.Collections.Generic.SortedSet[System_Collections_Generic_SortedSet_T]]:
        """Returns an IEqualityComparer{T} object, according to a specified comparer, that can be used to create a collection that contains individual sets."""
        ...

    def ExceptWith(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> None:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.SortedSet.Enumerator:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Generic_SortedSet_T]:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        ...

    @overload
    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    @overload
    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...

    def GetViewBetween(self, lowerValue: System_Collections_Generic_SortedSet_T, upperValue: System_Collections_Generic_SortedSet_T) -> System.Collections.Generic.SortedSet[System_Collections_Generic_SortedSet_T]:
        ...

    def IntersectWith(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> None:
        ...

    def IsProperSubsetOf(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> bool:
        ...

    def IsProperSupersetOf(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> bool:
        ...

    def IsSubsetOf(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> bool:
        ...

    def IsSupersetOf(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> bool:
        ...

    @overload
    def OnDeserialization(self, sender: typing.Any) -> None:
        ...

    @overload
    def OnDeserialization(self, sender: typing.Any) -> None:
        """This method is protected."""
        ...

    def Overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> bool:
        ...

    def Remove(self, item: System_Collections_Generic_SortedSet_T) -> bool:
        ...

    def RemoveWhere(self, match: typing.Callable[[System_Collections_Generic_SortedSet_T], bool]) -> int:
        ...

    def Reverse(self) -> System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]:
        ...

    def SetEquals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> bool:
        ...

    def SymmetricExceptWith(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> None:
        ...

    def TryGetValue(self, equalValue: System_Collections_Generic_SortedSet_T, actualValue: typing.Optional[System_Collections_Generic_SortedSet_T]) -> typing.Union[bool, System_Collections_Generic_SortedSet_T]:
        ...

    def UnionWith(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> None:
        ...


class SortedList(typing.Generic[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue], System.Object, System.Collections.Generic.IDictionary[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue], System.Collections.IDictionary, System.Collections.Generic.IReadOnlyDictionary[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue], typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue]]):
    """This class has no documentation."""

    class KeyList(System.Object, System.Collections.Generic.IList[System_Collections_Generic_SortedList_TKey], typing.Iterable[System_Collections_Generic_SortedList_TKey]):
        """This class has no documentation."""

        @property
        def Count(self) -> int:
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

        def __contains__(self, key: System_Collections_Generic_SortedList_TKey) -> bool:
            ...

        def __getitem__(self, index: int) -> System_Collections_Generic_SortedList_TKey:
            ...

        def __len__(self) -> int:
            ...

        def __setitem__(self, index: int, value: System_Collections_Generic_SortedList_TKey) -> None:
            ...

        def Add(self, key: System_Collections_Generic_SortedList_TKey) -> None:
            ...

        def Clear(self) -> None:
            ...

        def Contains(self, key: System_Collections_Generic_SortedList_TKey) -> bool:
            ...

        @overload
        def CopyTo(self, array: typing.List[System_Collections_Generic_SortedList_TKey], arrayIndex: int) -> None:
            ...

        @overload
        def CopyTo(self, array: System.Array, arrayIndex: int) -> None:
            ...

        @overload
        def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Generic_SortedList_TKey]:
            ...

        @overload
        def GetEnumerator(self) -> System.Collections.IEnumerator:
            ...

        def IndexOf(self, key: System_Collections_Generic_SortedList_TKey) -> int:
            ...

        def Insert(self, index: int, value: System_Collections_Generic_SortedList_TKey) -> None:
            ...

        def Remove(self, key: System_Collections_Generic_SortedList_TKey) -> bool:
            ...

        def RemoveAt(self, index: int) -> None:
            ...

    class ValueList(System.Object, System.Collections.Generic.IList[System_Collections_Generic_SortedList_TValue], typing.Iterable[System_Collections_Generic_SortedList_TValue]):
        """This class has no documentation."""

        @property
        def Count(self) -> int:
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

        def __contains__(self, value: System_Collections_Generic_SortedList_TValue) -> bool:
            ...

        def __getitem__(self, index: int) -> System_Collections_Generic_SortedList_TValue:
            ...

        def __len__(self) -> int:
            ...

        def __setitem__(self, index: int, value: System_Collections_Generic_SortedList_TValue) -> None:
            ...

        def Add(self, key: System_Collections_Generic_SortedList_TValue) -> None:
            ...

        def Clear(self) -> None:
            ...

        def Contains(self, value: System_Collections_Generic_SortedList_TValue) -> bool:
            ...

        @overload
        def CopyTo(self, array: typing.List[System_Collections_Generic_SortedList_TValue], arrayIndex: int) -> None:
            ...

        @overload
        def CopyTo(self, array: System.Array, index: int) -> None:
            ...

        @overload
        def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Generic_SortedList_TValue]:
            ...

        @overload
        def GetEnumerator(self) -> System.Collections.IEnumerator:
            ...

        def IndexOf(self, value: System_Collections_Generic_SortedList_TValue) -> int:
            ...

        def Insert(self, index: int, value: System_Collections_Generic_SortedList_TValue) -> None:
            ...

        def Remove(self, value: System_Collections_Generic_SortedList_TValue) -> bool:
            ...

        def RemoveAt(self, index: int) -> None:
            ...

    @property
    def Capacity(self) -> int:
        ...

    @Capacity.setter
    def Capacity(self, value: int):
        ...

    @property
    def Comparer(self) -> System.Collections.Generic.IComparer[System_Collections_Generic_SortedList_TKey]:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def Keys(self) -> System.Collections.Generic.IList[System_Collections_Generic_SortedList_TKey]:
        ...

    @property
    def Values(self) -> System.Collections.Generic.IList[System_Collections_Generic_SortedList_TValue]:
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
    def __contains__(self, keyValuePair: System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue]) -> bool:
        ...

    @overload
    def __contains__(self, key: typing.Any) -> bool:
        ...

    @overload
    def __contains__(self, key: System_Collections_Generic_SortedList_TKey) -> bool:
        ...

    @overload
    def __getitem__(self, key: System_Collections_Generic_SortedList_TKey) -> System_Collections_Generic_SortedList_TValue:
        ...

    @overload
    def __getitem__(self, key: typing.Any) -> typing.Any:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedList_TKey]) -> None:
        ...

    @overload
    def __init__(self, capacity: int, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedList_TKey]) -> None:
        ...

    @overload
    def __init__(self, dictionary: System.Collections.Generic.IDictionary[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue]) -> None:
        ...

    @overload
    def __init__(self, dictionary: System.Collections.Generic.IDictionary[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue], comparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedList_TKey]) -> None:
        ...

    def __len__(self) -> int:
        ...

    @overload
    def __setitem__(self, key: System_Collections_Generic_SortedList_TKey, value: System_Collections_Generic_SortedList_TValue) -> None:
        ...

    @overload
    def __setitem__(self, key: typing.Any, value: typing.Any) -> None:
        ...

    @overload
    def Add(self, key: System_Collections_Generic_SortedList_TKey, value: System_Collections_Generic_SortedList_TValue) -> None:
        ...

    @overload
    def Add(self, keyValuePair: System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue]) -> None:
        ...

    @overload
    def Add(self, key: typing.Any, value: typing.Any) -> None:
        ...

    def Clear(self) -> None:
        ...

    @overload
    def Contains(self, keyValuePair: System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue]) -> bool:
        ...

    @overload
    def Contains(self, key: typing.Any) -> bool:
        ...

    def ContainsKey(self, key: System_Collections_Generic_SortedList_TKey) -> bool:
        ...

    def ContainsValue(self, value: System_Collections_Generic_SortedList_TValue) -> bool:
        ...

    @overload
    def CopyTo(self, array: typing.List[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue]], arrayIndex: int) -> None:
        ...

    @overload
    def CopyTo(self, array: System.Array, index: int) -> None:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue]]:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue]]:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IDictionaryEnumerator:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        ...

    def GetKeyAtIndex(self, index: int) -> System_Collections_Generic_SortedList_TKey:
        """
        Gets the key corresponding to the specified index.
        
        :param index: The zero-based index of the key within the entire SortedList{TKey, TValue}.
        :returns: The key corresponding to the specified index.
        """
        ...

    def GetValueAtIndex(self, index: int) -> System_Collections_Generic_SortedList_TValue:
        """
        Gets the value corresponding to the specified index.
        
        :param index: The zero-based index of the value within the entire SortedList{TKey, TValue}.
        :returns: The value corresponding to the specified index.
        """
        ...

    def IndexOfKey(self, key: System_Collections_Generic_SortedList_TKey) -> int:
        ...

    def IndexOfValue(self, value: System_Collections_Generic_SortedList_TValue) -> int:
        ...

    @overload
    def Remove(self, keyValuePair: System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue]) -> bool:
        ...

    @overload
    def Remove(self, key: System_Collections_Generic_SortedList_TKey) -> bool:
        ...

    @overload
    def Remove(self, key: typing.Any) -> None:
        ...

    def RemoveAt(self, index: int) -> None:
        ...

    def SetValueAtIndex(self, index: int, value: System_Collections_Generic_SortedList_TValue) -> None:
        """
        Updates the value corresponding to the specified index.
        
        :param index: The zero-based index of the value within the entire SortedList{TKey, TValue}.
        :param value: The value with which to replace the entry at the specified index.
        """
        ...

    def TrimExcess(self) -> None:
        ...

    def TryGetValue(self, key: System_Collections_Generic_SortedList_TKey, value: typing.Optional[System_Collections_Generic_SortedList_TValue]) -> typing.Union[bool, System_Collections_Generic_SortedList_TValue]:
        ...


class SortedDictionary(typing.Generic[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue], System.Object, System.Collections.Generic.IDictionary[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue], System.Collections.IDictionary, System.Collections.Generic.IReadOnlyDictionary[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue], typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]]):
    """This class has no documentation."""

    class Enumerator(System.Collections.IDictionaryEnumerator):
        """This class has no documentation."""

        KeyValuePair: int = 1

        DictEntry: int = 2

        @property
        def Current(self) -> System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]:
            ...

        @property
        def NotStartedOrEnded(self) -> bool:
            ...

        @property
        def Key(self) -> System.Object:
            ...

        @property
        def Value(self) -> System.Object:
            ...

        @property
        def Entry(self) -> System.Collections.DictionaryEntry:
            ...

        def Dispose(self) -> None:
            ...

        def MoveNext(self) -> bool:
            ...

        def Reset(self) -> None:
            ...

    class KeyCollection(System.Object, System.Collections.Generic.ICollection[System_Collections_Generic_SortedDictionary_TKey], System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_SortedDictionary_TKey], typing.Iterable[System_Collections_Generic_SortedDictionary_TKey]):
        """This class has no documentation."""

        class Enumerator:
            """This class has no documentation."""

            @property
            def Current(self) -> System_Collections_Generic_SortedDictionary_TKey:
                ...

            def Dispose(self) -> None:
                ...

            def MoveNext(self) -> bool:
                ...

            def Reset(self) -> None:
                ...

        @property
        def Count(self) -> int:
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

        def __contains__(self, item: System_Collections_Generic_SortedDictionary_TKey) -> bool:
            ...

        def __init__(self, dictionary: System.Collections.Generic.SortedDictionary[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]) -> None:
            ...

        def __len__(self) -> int:
            ...

        def Add(self, item: System_Collections_Generic_SortedDictionary_TKey) -> None:
            ...

        def Clear(self) -> None:
            ...

        def Contains(self, item: System_Collections_Generic_SortedDictionary_TKey) -> bool:
            ...

        @overload
        def CopyTo(self, array: typing.List[System_Collections_Generic_SortedDictionary_TKey], index: int) -> None:
            ...

        @overload
        def CopyTo(self, array: System.Array, index: int) -> None:
            ...

        @overload
        def GetEnumerator(self) -> System.Collections.Generic.SortedDictionary.KeyCollection.Enumerator:
            ...

        @overload
        def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Generic_SortedDictionary_TKey]:
            ...

        @overload
        def GetEnumerator(self) -> System.Collections.IEnumerator:
            ...

        def Remove(self, item: System_Collections_Generic_SortedDictionary_TKey) -> bool:
            ...

    class ValueCollection(System.Object, System.Collections.Generic.ICollection[System_Collections_Generic_SortedDictionary_TValue], System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_SortedDictionary_TValue], typing.Iterable[System_Collections_Generic_SortedDictionary_TValue]):
        """This class has no documentation."""

        class Enumerator:
            """This class has no documentation."""

            @property
            def Current(self) -> System_Collections_Generic_SortedDictionary_TValue:
                ...

            def Dispose(self) -> None:
                ...

            def MoveNext(self) -> bool:
                ...

            def Reset(self) -> None:
                ...

        @property
        def Count(self) -> int:
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

        def __contains__(self, item: System_Collections_Generic_SortedDictionary_TValue) -> bool:
            ...

        def __init__(self, dictionary: System.Collections.Generic.SortedDictionary[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]) -> None:
            ...

        def __len__(self) -> int:
            ...

        def Add(self, item: System_Collections_Generic_SortedDictionary_TValue) -> None:
            ...

        def Clear(self) -> None:
            ...

        def Contains(self, item: System_Collections_Generic_SortedDictionary_TValue) -> bool:
            ...

        @overload
        def CopyTo(self, array: typing.List[System_Collections_Generic_SortedDictionary_TValue], index: int) -> None:
            ...

        @overload
        def CopyTo(self, array: System.Array, index: int) -> None:
            ...

        @overload
        def GetEnumerator(self) -> System.Collections.Generic.SortedDictionary.ValueCollection.Enumerator:
            ...

        @overload
        def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Generic_SortedDictionary_TValue]:
            ...

        @overload
        def GetEnumerator(self) -> System.Collections.IEnumerator:
            ...

        def Remove(self, item: System_Collections_Generic_SortedDictionary_TValue) -> bool:
            ...

    class KeyValuePairComparer(System.Collections.Generic.Comparer[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]]):
        """This class has no documentation."""

        @property
        def keyComparer(self) -> System.Collections.Generic.IComparer[System_Collections_Generic_SortedDictionary_TKey]:
            ...

        @keyComparer.setter
        def keyComparer(self, value: System.Collections.Generic.IComparer[System_Collections_Generic_SortedDictionary_TKey]):
            ...

        def __init__(self, keyComparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedDictionary_TKey]) -> None:
            ...

        def Compare(self, x: System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue], y: System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]) -> int:
            ...

        def Equals(self, obj: typing.Any) -> bool:
            ...

        def GetHashCode(self) -> int:
            ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def Comparer(self) -> System.Collections.Generic.IComparer[System_Collections_Generic_SortedDictionary_TKey]:
        ...

    @property
    def Keys(self) -> System.Collections.Generic.SortedDictionary.KeyCollection:
        ...

    @property
    def Values(self) -> System.Collections.Generic.SortedDictionary.ValueCollection:
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
    def __contains__(self, keyValuePair: System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]) -> bool:
        ...

    @overload
    def __contains__(self, key: System_Collections_Generic_SortedDictionary_TKey) -> bool:
        ...

    @overload
    def __contains__(self, key: typing.Any) -> bool:
        ...

    @overload
    def __getitem__(self, key: System_Collections_Generic_SortedDictionary_TKey) -> System_Collections_Generic_SortedDictionary_TValue:
        ...

    @overload
    def __getitem__(self, key: typing.Any) -> typing.Any:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, dictionary: System.Collections.Generic.IDictionary[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]) -> None:
        ...

    @overload
    def __init__(self, dictionary: System.Collections.Generic.IDictionary[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue], comparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedDictionary_TKey]) -> None:
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedDictionary_TKey]) -> None:
        ...

    def __len__(self) -> int:
        ...

    @overload
    def __setitem__(self, key: System_Collections_Generic_SortedDictionary_TKey, value: System_Collections_Generic_SortedDictionary_TValue) -> None:
        ...

    @overload
    def __setitem__(self, key: typing.Any, value: typing.Any) -> None:
        ...

    @overload
    def Add(self, keyValuePair: System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]) -> None:
        ...

    @overload
    def Add(self, key: System_Collections_Generic_SortedDictionary_TKey, value: System_Collections_Generic_SortedDictionary_TValue) -> None:
        ...

    @overload
    def Add(self, key: typing.Any, value: typing.Any) -> None:
        ...

    def Clear(self) -> None:
        ...

    @overload
    def Contains(self, keyValuePair: System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]) -> bool:
        ...

    @overload
    def Contains(self, key: typing.Any) -> bool:
        ...

    def ContainsKey(self, key: System_Collections_Generic_SortedDictionary_TKey) -> bool:
        ...

    def ContainsValue(self, value: System_Collections_Generic_SortedDictionary_TValue) -> bool:
        ...

    @overload
    def CopyTo(self, array: typing.List[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]], index: int) -> None:
        ...

    @overload
    def CopyTo(self, array: System.Array, index: int) -> None:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.SortedDictionary.Enumerator:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]]:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IDictionaryEnumerator:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        ...

    @overload
    def Remove(self, keyValuePair: System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]) -> bool:
        ...

    @overload
    def Remove(self, key: System_Collections_Generic_SortedDictionary_TKey) -> bool:
        ...

    @overload
    def Remove(self, key: typing.Any) -> None:
        ...

    def TryGetValue(self, key: System_Collections_Generic_SortedDictionary_TKey, value: typing.Optional[System_Collections_Generic_SortedDictionary_TValue]) -> typing.Union[bool, System_Collections_Generic_SortedDictionary_TValue]:
        ...


class TreeSet(typing.Generic[System_Collections_Generic_TreeSet_T], System.Collections.Generic.SortedSet[System_Collections_Generic_TreeSet_T]):
    """
    This class is intended as a helper for backwards compatibility with existing SortedDictionaries.
    TreeSet has been converted into SortedSet{T}, which will be exposed publicly. SortedDictionaries
    have the problem where they have already been serialized to disk as having a backing class named
    TreeSet. To ensure that we can read back anything that has already been written to disk, we need to
    make sure that we have a class named TreeSet that does everything the way it used to.
    
    The only thing that makes it different from SortedSet is that it throws on duplicates
    """

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_TreeSet_T]) -> None:
        ...


class Stack(typing.Generic[System_Collections_Generic_Stack_T], System.Object, System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_Stack_T], typing.Iterable[System_Collections_Generic_Stack_T]):
    """This class has no documentation."""

    class Enumerator:
        """This class has no documentation."""

        @property
        def Current(self) -> System_Collections_Generic_Stack_T:
            ...

        def Dispose(self) -> None:
            ...

        def MoveNext(self) -> bool:
            ...

        def Reset(self) -> None:
            ...

    @property
    def Count(self) -> int:
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    def __contains__(self, item: System_Collections_Generic_Stack_T) -> bool:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_Stack_T]) -> None:
        ...

    def __len__(self) -> int:
        ...

    def Clear(self) -> None:
        ...

    def Contains(self, item: System_Collections_Generic_Stack_T) -> bool:
        ...

    @overload
    def CopyTo(self, array: typing.List[System_Collections_Generic_Stack_T], arrayIndex: int) -> None:
        ...

    @overload
    def CopyTo(self, array: System.Array, arrayIndex: int) -> None:
        ...

    def EnsureCapacity(self, capacity: int) -> int:
        """
        Ensures that the capacity of this Stack is at least the specified .
        If the current capacity of the Stack is less than specified ,
        the capacity is increased by continuously twice current capacity until it is at least the specified .
        
        :param capacity: The minimum capacity to ensure.
        :returns: The new capacity of this stack.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.Stack.Enumerator:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Generic_Stack_T]:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        ...

    def Peek(self) -> System_Collections_Generic_Stack_T:
        ...

    def Pop(self) -> System_Collections_Generic_Stack_T:
        ...

    def Push(self, item: System_Collections_Generic_Stack_T) -> None:
        ...

    def ToArray(self) -> typing.List[System_Collections_Generic_Stack_T]:
        ...

    def TrimExcess(self) -> None:
        ...

    def TryPeek(self, result: typing.Optional[System_Collections_Generic_Stack_T]) -> typing.Union[bool, System_Collections_Generic_Stack_T]:
        ...

    def TryPop(self, result: typing.Optional[System_Collections_Generic_Stack_T]) -> typing.Union[bool, System_Collections_Generic_Stack_T]:
        ...


class LinkedListNode(typing.Generic[System_Collections_Generic_LinkedListNode_T], System.Object):
    """This class has no documentation."""

    @property
    def list(self) -> System.Collections.Generic.LinkedList[System_Collections_Generic_LinkedListNode_T]:
        ...

    @list.setter
    def list(self, value: System.Collections.Generic.LinkedList[System_Collections_Generic_LinkedListNode_T]):
        ...

    @property
    def next(self) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedListNode_T]:
        ...

    @next.setter
    def next(self, value: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedListNode_T]):
        ...

    @property
    def prev(self) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedListNode_T]:
        ...

    @prev.setter
    def prev(self, value: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedListNode_T]):
        ...

    @property
    def item(self) -> System_Collections_Generic_LinkedListNode_T:
        ...

    @item.setter
    def item(self, value: System_Collections_Generic_LinkedListNode_T):
        ...

    @property
    def List(self) -> System.Collections.Generic.LinkedList[System_Collections_Generic_LinkedListNode_T]:
        ...

    @property
    def Next(self) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedListNode_T]:
        ...

    @property
    def Previous(self) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedListNode_T]:
        ...

    @property
    def Value(self) -> System_Collections_Generic_LinkedListNode_T:
        ...

    @Value.setter
    def Value(self, value: System_Collections_Generic_LinkedListNode_T):
        ...

    @property
    def ValueRef(self) -> typing.Any:
        """Gets a reference to the value held by the node."""
        ...

    def __init__(self, value: System_Collections_Generic_LinkedListNode_T) -> None:
        ...


class LinkedList(typing.Generic[System_Collections_Generic_LinkedList_T], System.Object, System.Collections.Generic.ICollection[System_Collections_Generic_LinkedList_T], System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_LinkedList_T], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, typing.Iterable[System_Collections_Generic_LinkedList_T]):
    """This class has no documentation."""

    class Enumerator(System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback):
        """This class has no documentation."""

        @property
        def Current(self) -> System_Collections_Generic_LinkedList_T:
            ...

        def Dispose(self) -> None:
            ...

        def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
            ...

        def MoveNext(self) -> bool:
            ...

        def OnDeserialization(self, sender: typing.Any) -> None:
            ...

        def Reset(self) -> None:
            ...

    @property
    def head(self) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    @head.setter
    def head(self, value: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]):
        ...

    @property
    def count(self) -> int:
        ...

    @count.setter
    def count(self, value: int):
        ...

    @property
    def version(self) -> int:
        ...

    @version.setter
    def version(self, value: int):
        ...

    @property
    def Count(self) -> int:
        ...

    @property
    def First(self) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    @property
    def Last(self) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
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

    def __contains__(self, value: System_Collections_Generic_LinkedList_T) -> bool:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_LinkedList_T]) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...

    def __len__(self) -> int:
        ...

    def Add(self, value: System_Collections_Generic_LinkedList_T) -> None:
        ...

    @overload
    def AddAfter(self, node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T], value: System_Collections_Generic_LinkedList_T) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    @overload
    def AddAfter(self, node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T], newNode: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]) -> None:
        ...

    @overload
    def AddBefore(self, node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T], value: System_Collections_Generic_LinkedList_T) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    @overload
    def AddBefore(self, node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T], newNode: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]) -> None:
        ...

    @overload
    def AddFirst(self, value: System_Collections_Generic_LinkedList_T) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    @overload
    def AddFirst(self, node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]) -> None:
        ...

    @overload
    def AddLast(self, value: System_Collections_Generic_LinkedList_T) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    @overload
    def AddLast(self, node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]) -> None:
        ...

    def Clear(self) -> None:
        ...

    def Contains(self, value: System_Collections_Generic_LinkedList_T) -> bool:
        ...

    @overload
    def CopyTo(self, array: typing.List[System_Collections_Generic_LinkedList_T], index: int) -> None:
        ...

    @overload
    def CopyTo(self, array: System.Array, index: int) -> None:
        ...

    def Find(self, value: System_Collections_Generic_LinkedList_T) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    def FindLast(self, value: System_Collections_Generic_LinkedList_T) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.LinkedList.Enumerator:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Generic_LinkedList_T]:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def OnDeserialization(self, sender: typing.Any) -> None:
        ...

    @overload
    def Remove(self, value: System_Collections_Generic_LinkedList_T) -> bool:
        ...

    @overload
    def Remove(self, node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]) -> None:
        ...

    def RemoveFirst(self) -> None:
        ...

    def RemoveLast(self) -> None:
        ...


class PriorityQueue(typing.Generic[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority], System.Object):
    """Represents a min priority queue."""

    class UnorderedItemsCollection(System.Object, System.Collections.Generic.IReadOnlyCollection[System.ValueTuple[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]], System.Collections.ICollection, typing.Iterable[System.ValueTuple[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]]):
        """Enumerates the contents of a PriorityQueue{TElement, TPriority}, without any ordering guarantees."""

        class Enumerator:
            """
            Enumerates the element and priority pairs of a PriorityQueue{TElement, TPriority},
             without any ordering guarantees.
            """

            @property
            def Current(self) -> System.ValueTuple[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]:
                """Gets the element at the current position of the enumerator."""
                ...

            def Dispose(self) -> None:
                """Releases all resources used by the Enumerator."""
                ...

            def MoveNext(self) -> bool:
                """
                Advances the enumerator to the next element of the UnorderedItems.
                
                :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
                """
                ...

            def Reset(self) -> None:
                ...

        @property
        def _queue(self) -> System.Collections.Generic.PriorityQueue[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]:
            ...

        @property
        def Count(self) -> int:
            ...

        @property
        def SyncRoot(self) -> System.Object:
            ...

        @property
        def IsSynchronized(self) -> bool:
            ...

        def CopyTo(self, array: System.Array, index: int) -> None:
            ...

        @overload
        def GetEnumerator(self) -> System.Collections.Generic.PriorityQueue.UnorderedItemsCollection.Enumerator:
            """
            Returns an enumerator that iterates through the UnorderedItems.
            
            :returns: An Enumerator for the UnorderedItems.
            """
            ...

        @overload
        def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System.ValueTuple[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]]:
            ...

        @overload
        def GetEnumerator(self) -> System.Collections.IEnumerator:
            ...

    @property
    def Count(self) -> int:
        """Gets the number of elements contained in the PriorityQueue{TElement, TPriority}."""
        ...

    @property
    def Comparer(self) -> System.Collections.Generic.IComparer[System_Collections_Generic_PriorityQueue_TPriority]:
        """Gets the priority comparer used by the PriorityQueue{TElement, TPriority}."""
        ...

    @property
    def UnorderedItems(self) -> System.Collections.Generic.PriorityQueue.UnorderedItemsCollection:
        """Gets a collection that enumerates the elements of the queue in an unordered manner."""
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, initialCapacity: int) -> None:
        """
        Initializes a new instance of the PriorityQueue{TElement, TPriority} class
         with the specified initial capacity.
        
        :param initialCapacity: Initial capacity to allocate in the underlying heap array.
        """
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_PriorityQueue_TPriority]) -> None:
        """
        Initializes a new instance of the PriorityQueue{TElement, TPriority} class
         with the specified custom priority comparer.
        
        :param comparer: Custom comparer dictating the ordering of elements.  Uses Comparer{T}.Default if the argument is null.
        """
        ...

    @overload
    def __init__(self, initialCapacity: int, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_PriorityQueue_TPriority]) -> None:
        """
        Initializes a new instance of the PriorityQueue{TElement, TPriority} class
         with the specified initial capacity and custom priority comparer.
        
        :param initialCapacity: Initial capacity to allocate in the underlying heap array.
        :param comparer: Custom comparer dictating the ordering of elements.  Uses Comparer{T}.Default if the argument is null.
        """
        ...

    @overload
    def __init__(self, items: System.Collections.Generic.IEnumerable[System.ValueTuple[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]]) -> None:
        """
        Initializes a new instance of the PriorityQueue{TElement, TPriority} class
         that is populated with the specified elements and priorities.
        
        :param items: The pairs of elements and priorities with which to populate the queue.
        """
        ...

    @overload
    def __init__(self, items: System.Collections.Generic.IEnumerable[System.ValueTuple[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]], comparer: System.Collections.Generic.IComparer[System_Collections_Generic_PriorityQueue_TPriority]) -> None:
        """
        Initializes a new instance of the PriorityQueue{TElement, TPriority} class
         that is populated with the specified elements and priorities,
         and with the specified custom priority comparer.
        
        :param items: The pairs of elements and priorities with which to populate the queue.
        :param comparer: Custom comparer dictating the ordering of elements.  Uses Comparer{T}.Default if the argument is null.
        """
        ...

    def Clear(self) -> None:
        """Removes all items from the PriorityQueue{TElement, TPriority}."""
        ...

    def Dequeue(self) -> System_Collections_Generic_PriorityQueue_TElement:
        """
        Removes and returns the minimal element from the PriorityQueue{TElement, TPriority}.
        
        :returns: The minimal element of the PriorityQueue{TElement, TPriority}.
        """
        ...

    def DequeueEnqueue(self, element: System_Collections_Generic_PriorityQueue_TElement, priority: System_Collections_Generic_PriorityQueue_TPriority) -> System_Collections_Generic_PriorityQueue_TElement:
        """
        Removes the minimal element and then immediately adds the specified element with associated priority to the PriorityQueue{TElement, TPriority},
        
        :param element: The element to add to the PriorityQueue{TElement, TPriority}.
        :param priority: The priority with which to associate the new element.
        :returns: The minimal element removed before performing the enqueue operation.
        """
        ...

    def Enqueue(self, element: System_Collections_Generic_PriorityQueue_TElement, priority: System_Collections_Generic_PriorityQueue_TPriority) -> None:
        """
        Adds the specified element with associated priority to the PriorityQueue{TElement, TPriority}.
        
        :param element: The element to add to the PriorityQueue{TElement, TPriority}.
        :param priority: The priority with which to associate the new element.
        """
        ...

    def EnqueueDequeue(self, element: System_Collections_Generic_PriorityQueue_TElement, priority: System_Collections_Generic_PriorityQueue_TPriority) -> System_Collections_Generic_PriorityQueue_TElement:
        """
        Adds the specified element with associated priority to the PriorityQueue{TElement, TPriority},
         and immediately removes the minimal element, returning the result.
        
        :param element: The element to add to the PriorityQueue{TElement, TPriority}.
        :param priority: The priority with which to associate the new element.
        :returns: The minimal element removed after the enqueue operation.
        """
        ...

    @overload
    def EnqueueRange(self, items: System.Collections.Generic.IEnumerable[System.ValueTuple[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]]) -> None:
        """
        Enqueues a sequence of element/priority pairs to the PriorityQueue{TElement, TPriority}.
        
        :param items: The pairs of elements and priorities to add to the queue.
        """
        ...

    @overload
    def EnqueueRange(self, elements: System.Collections.Generic.IEnumerable[System_Collections_Generic_PriorityQueue_TElement], priority: System_Collections_Generic_PriorityQueue_TPriority) -> None:
        """
        Enqueues a sequence of elements pairs to the PriorityQueue{TElement, TPriority},
         all associated with the specified priority.
        
        :param elements: The elements to add to the queue.
        :param priority: The priority to associate with the new elements.
        """
        ...

    def EnsureCapacity(self, capacity: int) -> int:
        """
        Ensures that the PriorityQueue{TElement, TPriority} can hold up to
          items without further expansion of its backing storage.
        
        :param capacity: The minimum capacity to be used.
        :returns: The current capacity of the PriorityQueue{TElement, TPriority}.
        """
        ...

    def Peek(self) -> System_Collections_Generic_PriorityQueue_TElement:
        """
        Returns the minimal element from the PriorityQueue{TElement, TPriority} without removing it.
        
        :returns: The minimal element of the PriorityQueue{TElement, TPriority}.
        """
        ...

    def TrimExcess(self) -> None:
        """
        Sets the capacity to the actual number of items in the PriorityQueue{TElement, TPriority},
         if that is less than 90 percent of current capacity.
        """
        ...

    def TryDequeue(self, element: typing.Optional[System_Collections_Generic_PriorityQueue_TElement], priority: typing.Optional[System_Collections_Generic_PriorityQueue_TPriority]) -> typing.Union[bool, System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]:
        """
        Removes the minimal element from the PriorityQueue{TElement, TPriority},
         and copies it to the  parameter,
         and its associated priority to the  parameter.
        
        :param element: The removed element.
        :param priority: The priority associated with the removed element.
        :returns: true if the element is successfully removed;  false if the PriorityQueue{TElement, TPriority} is empty.
        """
        ...

    def TryPeek(self, element: typing.Optional[System_Collections_Generic_PriorityQueue_TElement], priority: typing.Optional[System_Collections_Generic_PriorityQueue_TPriority]) -> typing.Union[bool, System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]:
        """
        Returns a value that indicates whether there is a minimal element in the PriorityQueue{TElement, TPriority},
         and if one is present, copies it to the  parameter,
         and its associated priority to the  parameter.
         The element is not removed from the PriorityQueue{TElement, TPriority}.
        
        :param element: The minimal element in the queue.
        :param priority: The priority associated with the minimal element.
        :returns: true if there is a minimal element;  false if the PriorityQueue{TElement, TPriority} is empty.
        """
        ...


