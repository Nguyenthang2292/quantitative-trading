from typing import overload
import abc
import datetime
import typing

import System
import System.Collections
import System.Collections.Concurrent
import System.Collections.Generic
import System.Threading

System_Collections_Concurrent_ConcurrentQueue_T = typing.TypeVar("System_Collections_Concurrent_ConcurrentQueue_T")
System_Collections_Concurrent_IProducerConsumerCollection_T = typing.TypeVar("System_Collections_Concurrent_IProducerConsumerCollection_T")
System_Collections_Concurrent_ConcurrentStack_T = typing.TypeVar("System_Collections_Concurrent_ConcurrentStack_T")
System_Collections_Concurrent_BlockingCollection_T = typing.TypeVar("System_Collections_Concurrent_BlockingCollection_T")
System_Collections_Concurrent_ConcurrentDictionary_TKey = typing.TypeVar("System_Collections_Concurrent_ConcurrentDictionary_TKey")
System_Collections_Concurrent_ConcurrentDictionary_TValue = typing.TypeVar("System_Collections_Concurrent_ConcurrentDictionary_TValue")
System_Collections_Concurrent_ConcurrentDictionary_GetOrAdd_TArg = typing.TypeVar("System_Collections_Concurrent_ConcurrentDictionary_GetOrAdd_TArg")
System_Collections_Concurrent_ConcurrentDictionary_AddOrUpdate_TArg = typing.TypeVar("System_Collections_Concurrent_ConcurrentDictionary_AddOrUpdate_TArg")
System_Collections_Concurrent_ConcurrentBag_T = typing.TypeVar("System_Collections_Concurrent_ConcurrentBag_T")
System_Collections_Concurrent_Partitioner_TSource = typing.TypeVar("System_Collections_Concurrent_Partitioner_TSource")
System_Collections_Concurrent_Partitioner_Create_TSource = typing.TypeVar("System_Collections_Concurrent_Partitioner_Create_TSource")
System_Collections_Concurrent_OrderablePartitioner_TSource = typing.TypeVar("System_Collections_Concurrent_OrderablePartitioner_TSource")


class IProducerConsumerCollection(typing.Generic[System_Collections_Concurrent_IProducerConsumerCollection_T], System.Collections.ICollection, metaclass=abc.ABCMeta):
    """
    A common interface for all concurrent collections.
    Defines methods to manipulate thread-safe collections intended for producer/consumer usage.
    """

    def CopyTo(self, array: typing.List[System_Collections_Concurrent_IProducerConsumerCollection_T], index: int) -> None:
        """
        Copies the elements of the IProducerConsumerCollection{T} to
        an
        System.Array, starting at a specified index.
        
        :param array: The one-dimensional System.Array that is the destination of the elements copied from the IProducerConsumerCollection{T}. The array must have zero-based indexing.
        :param index: The zero-based index in  at which copying begins.
        """
        ...

    def ToArray(self) -> typing.List[System_Collections_Concurrent_IProducerConsumerCollection_T]:
        """
        Copies the elements contained in the IProducerConsumerCollection{T} to a new array.
        
        :returns: A new array containing the elements copied from the IProducerConsumerCollection{T}.
        """
        ...

    def TryAdd(self, item: System_Collections_Concurrent_IProducerConsumerCollection_T) -> bool:
        """
        Attempts to add an object to the IProducerConsumerCollection{T}.
        
        :param item: The object to add to the IProducerConsumerCollection{T}.
        :returns: true if the object was added successfully; otherwise, false.
        """
        ...

    def TryTake(self, item: typing.Optional[System_Collections_Concurrent_IProducerConsumerCollection_T]) -> typing.Union[bool, System_Collections_Concurrent_IProducerConsumerCollection_T]:
        """
        Attempts to remove and return an object from the IProducerConsumerCollection{T}.
        
        :param item: When this method returns, if the object was removed and returned successfully,  contains the removed object. If no object was available to be removed, the value is unspecified.
        :returns: true if an object was removed and returned successfully; otherwise, false.
        """
        ...


class ConcurrentQueue(typing.Generic[System_Collections_Concurrent_ConcurrentQueue_T], System.Object, System.Collections.Concurrent.IProducerConsumerCollection[System_Collections_Concurrent_ConcurrentQueue_T], System.Collections.Generic.IReadOnlyCollection[System_Collections_Concurrent_ConcurrentQueue_T], typing.Iterable[System_Collections_Concurrent_ConcurrentQueue_T]):
    """Represents a thread-safe first-in, first-out collection of objects."""

    @property
    def IsSynchronized(self) -> bool:
        """
        Gets a value indicating whether access to the ICollection is
        synchronized with the SyncRoot.
        """
        ...

    @property
    def SyncRoot(self) -> System.Object:
        """Gets an object that can be used to synchronize access to the ICollection. This property is not supported."""
        ...

    @property
    def IsEmpty(self) -> bool:
        """Gets a value that indicates whether the ConcurrentQueue{T} is empty."""
        ...

    @property
    def Count(self) -> int:
        """Gets the number of elements contained in the ConcurrentQueue{T}."""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the ConcurrentQueue{T} class."""
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Concurrent_ConcurrentQueue_T]) -> None:
        """
        Initializes a new instance of the ConcurrentQueue{T} class that contains elements copied
        from the specified collection.
        
        :param collection: The collection whose elements are copied to the new ConcurrentQueue{T}.
        """
        ...

    def Clear(self) -> None:
        """Removes all objects from the ConcurrentQueue{T}."""
        ...

    @overload
    def CopyTo(self, array: System.Array, index: int) -> None:
        """
        Copies the elements of the ICollection to an Array, starting at a particular Array index.
        
        :param array: The one-dimensional Array that is the destination of the elements copied from the ConcurrentQueue{T}.  must have zero-based indexing.
        :param index: The zero-based index in  at which copying begins.
        """
        ...

    @overload
    def CopyTo(self, array: typing.List[System_Collections_Concurrent_ConcurrentQueue_T], index: int) -> None:
        """
        Copies the ConcurrentQueue{T} elements to an existing one-dimensional Array, starting at the specified array index.
        
        :param array: The one-dimensional Array that is the destination of the elements copied from the ConcurrentQueue{T}. The Array must have zero-based indexing.
        :param index: The zero-based index in  at which copying begins.
        """
        ...

    def Enqueue(self, item: System_Collections_Concurrent_ConcurrentQueue_T) -> None:
        """
        Adds an object to the end of the ConcurrentQueue{T}.
        
        :param item: The object to add to the end of the ConcurrentQueue{T}. The value can be a null reference (Nothing in Visual Basic) for reference types.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        """
        Returns an enumerator that iterates through a collection.
        
        :returns: An IEnumerator that can be used to iterate through the collection.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Concurrent_ConcurrentQueue_T]:
        """
        Returns an enumerator that iterates through the ConcurrentQueue{T}.
        
        :returns: An enumerator for the contents of the ConcurrentQueue{T}.
        """
        ...

    def ToArray(self) -> typing.List[System_Collections_Concurrent_ConcurrentQueue_T]:
        """
        Copies the elements stored in the ConcurrentQueue{T} to a new array.
        
        :returns: A new array containing a snapshot of elements copied from the ConcurrentQueue{T}.
        """
        ...

    def TryAdd(self, item: System_Collections_Concurrent_ConcurrentQueue_T) -> bool:
        """
        Attempts to add an object to the Concurrent.IProducerConsumerCollection{T}.
        
        :param item: The object to add to the Concurrent.IProducerConsumerCollection{T}. The value can be a null reference (Nothing in Visual Basic) for reference types.
        :returns: true if the object was added successfully; otherwise, false.
        """
        ...

    def TryDequeue(self, result: typing.Optional[System_Collections_Concurrent_ConcurrentQueue_T]) -> typing.Union[bool, System_Collections_Concurrent_ConcurrentQueue_T]:
        """
        Attempts to remove and return the object at the beginning of the ConcurrentQueue{T}.
        
        :param result: When this method returns, if the operation was successful,  contains the object removed. If no object was available to be removed, the value is unspecified.
        :returns: true if an element was removed and returned from the beginning of the ConcurrentQueue{T} successfully; otherwise, false.
        """
        ...

    def TryPeek(self, result: typing.Optional[System_Collections_Concurrent_ConcurrentQueue_T]) -> typing.Union[bool, System_Collections_Concurrent_ConcurrentQueue_T]:
        """
        Attempts to return an object from the beginning of the ConcurrentQueue{T}
        without removing it.
        
        :param result: When this method returns,  contains an object from the beginning of the Concurrent.ConcurrentQueue{T} or default(T) if the operation failed.
        :returns: true if and object was returned successfully; otherwise, false.
        """
        ...

    def TryTake(self, item: typing.Optional[System_Collections_Concurrent_ConcurrentQueue_T]) -> typing.Union[bool, System_Collections_Concurrent_ConcurrentQueue_T]:
        """
        Attempts to remove and return an object from the Concurrent.IProducerConsumerCollection{T}.
        
        :param item: When this method returns, if the operation was successful,  contains the object removed. If no object was available to be removed, the value is unspecified.
        :returns: true if an element was removed and returned successfully; otherwise, false.
        """
        ...


class ConcurrentStack(typing.Generic[System_Collections_Concurrent_ConcurrentStack_T], System.Object, System.Collections.Concurrent.IProducerConsumerCollection[System_Collections_Concurrent_ConcurrentStack_T], System.Collections.Generic.IReadOnlyCollection[System_Collections_Concurrent_ConcurrentStack_T], typing.Iterable[System_Collections_Concurrent_ConcurrentStack_T]):
    """This class has no documentation."""

    @property
    def IsEmpty(self) -> bool:
        """Gets a value that indicates whether the ConcurrentStack{T} is empty."""
        ...

    @property
    def Count(self) -> int:
        """Gets the number of elements contained in the ConcurrentStack{T}."""
        ...

    @property
    def IsSynchronized(self) -> bool:
        """
        Gets a value indicating whether access to the System.Collections.ICollection is
        synchronized with the SyncRoot.
        """
        ...

    @property
    def SyncRoot(self) -> System.Object:
        """Gets an object that can be used to synchronize access to the System.Collections.ICollection. This property is not supported."""
        ...

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the ConcurrentStack{T}
        class.
        """
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Concurrent_ConcurrentStack_T]) -> None:
        """
        Initializes a new instance of the ConcurrentStack{T}
        class that contains elements copied from the specified collection
        
        :param collection: The collection whose elements are copied to the new ConcurrentStack{T}.
        """
        ...

    def Clear(self) -> None:
        """Removes all objects from the ConcurrentStack{T}."""
        ...

    @overload
    def CopyTo(self, array: System.Array, index: int) -> None:
        """
        Copies the elements of the System.Collections.ICollection to an System.Array, starting at a particular
        System.Array index.
        
        :param array: The one-dimensional System.Array that is the destination of the elements copied from the ConcurrentStack{T}. The System.Array must have zero-based indexing.
        :param index: The zero-based index in  at which copying begins.
        """
        ...

    @overload
    def CopyTo(self, array: typing.List[System_Collections_Concurrent_ConcurrentStack_T], index: int) -> None:
        """
        Copies the ConcurrentStack{T} elements to an existing one-dimensional System.Array, starting at the specified array index.
        
        :param array: The one-dimensional System.Array that is the destination of the elements copied from the ConcurrentStack{T}. The System.Array must have zero-based indexing.
        :param index: The zero-based index in  at which copying begins.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Concurrent_ConcurrentStack_T]:
        """
        Returns an enumerator that iterates through the ConcurrentStack{T}.
        
        :returns: An enumerator for the ConcurrentStack{T}.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        """
        Returns an enumerator that iterates through a collection.
        
        :returns: An System.Collections.IEnumerator that can be used to iterate through the collection.
        """
        ...

    def Push(self, item: System_Collections_Concurrent_ConcurrentStack_T) -> None:
        """
        Inserts an object at the top of the ConcurrentStack{T}.
        
        :param item: The object to push onto the ConcurrentStack{T}. The value can be a null reference (Nothing in Visual Basic) for reference types.
        """
        ...

    @overload
    def PushRange(self, items: typing.List[System_Collections_Concurrent_ConcurrentStack_T]) -> None:
        """
        Inserts multiple objects at the top of the ConcurrentStack{T} atomically.
        
        :param items: The objects to push onto the ConcurrentStack{T}.
        """
        ...

    @overload
    def PushRange(self, items: typing.List[System_Collections_Concurrent_ConcurrentStack_T], startIndex: int, count: int) -> None:
        """
        Inserts multiple objects at the top of the ConcurrentStack{T} atomically.
        
        :param items: The objects to push onto the ConcurrentStack{T}.
        :param startIndex: The zero-based offset in  at which to begin inserting elements onto the top of the ConcurrentStack{T}.
        :param count: The number of elements to be inserted onto the top of the ConcurrentStack{T}.
        """
        ...

    def ToArray(self) -> typing.List[System_Collections_Concurrent_ConcurrentStack_T]:
        """
        Copies the items stored in the ConcurrentStack{T} to a new array.
        
        :returns: A new array containing a snapshot of elements copied from the ConcurrentStack{T}.
        """
        ...

    def TryAdd(self, item: System_Collections_Concurrent_ConcurrentStack_T) -> bool:
        """
        Attempts to add an object to the System.Collections.Concurrent.IProducerConsumerCollection{T}.
        
        :param item: The object to add to the System.Collections.Concurrent.IProducerConsumerCollection{T}. The value can be a null reference (Nothing in Visual Basic) for reference types.
        :returns: true if the object was added successfully; otherwise, false.
        """
        ...

    def TryPeek(self, result: typing.Optional[System_Collections_Concurrent_ConcurrentStack_T]) -> typing.Union[bool, System_Collections_Concurrent_ConcurrentStack_T]:
        """
        Attempts to return an object from the top of the ConcurrentStack{T}
        without removing it.
        
        :param result: When this method returns,  contains an object from the top of the System.Collections.Concurrent.ConcurrentStack{T} or an unspecified value if the operation failed.
        :returns: true if and object was returned successfully; otherwise, false.
        """
        ...

    def TryPop(self, result: typing.Optional[System_Collections_Concurrent_ConcurrentStack_T]) -> typing.Union[bool, System_Collections_Concurrent_ConcurrentStack_T]:
        """
        Attempts to pop and return the object at the top of the ConcurrentStack{T}.
        
        :param result: When this method returns, if the operation was successful,  contains the object removed. If no object was available to be removed, the value is unspecified.
        :returns: true if an element was removed and returned from the top of the ConcurrentStack{T} successfully; otherwise, false.
        """
        ...

    @overload
    def TryPopRange(self, items: typing.List[System_Collections_Concurrent_ConcurrentStack_T]) -> int:
        """
        Attempts to pop and return multiple objects from the top of the ConcurrentStack{T}
        atomically.
        
        :param items: The System.Array to which objects popped from the top of the ConcurrentStack{T} will be added.
        :returns: The number of objects successfully popped from the top of the ConcurrentStack{T} and inserted in .
        """
        ...

    @overload
    def TryPopRange(self, items: typing.List[System_Collections_Concurrent_ConcurrentStack_T], startIndex: int, count: int) -> int:
        """
        Attempts to pop and return multiple objects from the top of the ConcurrentStack{T}
        atomically.
        
        :param items: The System.Array to which objects popped from the top of the ConcurrentStack{T} will be added.
        :param startIndex: The zero-based offset in  at which to begin inserting elements from the top of the ConcurrentStack{T}.
        :param count: The number of elements to be popped from top of the ConcurrentStack{T} and inserted into .
        :returns: The number of objects successfully popped from the top of the ConcurrentStack{T} and inserted in .
        """
        ...

    def TryTake(self, item: typing.Optional[System_Collections_Concurrent_ConcurrentStack_T]) -> typing.Union[bool, System_Collections_Concurrent_ConcurrentStack_T]:
        """
        Attempts to remove and return an object from the System.Collections.Concurrent.IProducerConsumerCollection{T}.
        
        :param item: When this method returns, if the operation was successful,  contains the object removed. If no object was available to be removed, the value is unspecified.
        :returns: true if an element was removed and returned successfully; otherwise, false.
        """
        ...


class BlockingCollection(typing.Generic[System_Collections_Concurrent_BlockingCollection_T], System.Object, System.Collections.ICollection, System.IDisposable, System.Collections.Generic.IReadOnlyCollection[System_Collections_Concurrent_BlockingCollection_T], typing.Iterable[System_Collections_Concurrent_BlockingCollection_T]):
    """
    Provides blocking and bounding capabilities for thread-safe collections that
    implement System.Collections.Concurrent.IProducerConsumerCollection{T}.
    """

    @property
    def BoundedCapacity(self) -> int:
        ...

    @property
    def IsAddingCompleted(self) -> bool:
        """Gets whether this System.Collections.Concurrent.BlockingCollection{T} has been marked as complete for adding."""
        ...

    @property
    def IsCompleted(self) -> bool:
        """Gets whether this System.Collections.Concurrent.BlockingCollection{T} has been marked as complete for adding and is empty."""
        ...

    @property
    def Count(self) -> int:
        """Gets the number of items contained in the System.Collections.Concurrent.BlockingCollection{T}."""
        ...

    @property
    def IsSynchronized(self) -> bool:
        """Gets a value indicating whether access to the System.Collections.ICollection is synchronized."""
        ...

    @property
    def SyncRoot(self) -> System.Object:
        """Gets an object that can be used to synchronize access to the System.Collections.ICollection. This property is not supported."""
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, boundedCapacity: int) -> None:
        """
        Initializes a new instance of the System.Collections.Concurrent.BlockingCollection{T}
        class with the specified upper-bound.
        
        :param boundedCapacity: The bounded size of the collection.
        """
        ...

    @overload
    def __init__(self, collection: System.Collections.Concurrent.IProducerConsumerCollection[System_Collections_Concurrent_BlockingCollection_T], boundedCapacity: int) -> None:
        """
        Initializes a new instance of the System.Collections.Concurrent.BlockingCollection{T}
        class with the specified upper-bound and using the provided
        System.Collections.Concurrent.IProducerConsumerCollection{T} as its underlying data store.
        
        :param collection: The collection to use as the underlying data store.
        :param boundedCapacity: The bounded size of the collection.
        """
        ...

    @overload
    def __init__(self, collection: System.Collections.Concurrent.IProducerConsumerCollection[System_Collections_Concurrent_BlockingCollection_T]) -> None:
        """
        Initializes a new instance of the System.Collections.Concurrent.BlockingCollection{T}
        class without an upper-bound and using the provided
        System.Collections.Concurrent.IProducerConsumerCollection{T} as its underlying data store.
        
        :param collection: The collection to use as the underlying data store.
        """
        ...

    @overload
    def Add(self, item: System_Collections_Concurrent_BlockingCollection_T) -> None:
        """
        Adds the item to the System.Collections.Concurrent.BlockingCollection{T}.
        
        :param item: The item to be added to the collection. The value can be a null reference.
        """
        ...

    @overload
    def Add(self, item: System_Collections_Concurrent_BlockingCollection_T, cancellationToken: System.Threading.CancellationToken) -> None:
        """
        Adds the item to the System.Collections.Concurrent.BlockingCollection{T}.
        A System.OperationCanceledException is thrown if the CancellationToken is
        canceled.
        
        :param item: The item to be added to the collection. The value can be a null reference.
        :param cancellationToken: A cancellation token to observe.
        """
        ...

    @staticmethod
    @overload
    def AddToAny(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: System_Collections_Concurrent_BlockingCollection_T) -> int:
        """
        Adds the specified item to any one of the specified
        System.Collections.Concurrent.BlockingCollection{T} instances.
        
        :param collections: The array of collections.
        :param item: The item to be added to one of the collections.
        :returns: The index of the collection in the  array to which the item was added.
        """
        ...

    @staticmethod
    @overload
    def AddToAny(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: System_Collections_Concurrent_BlockingCollection_T, cancellationToken: System.Threading.CancellationToken) -> int:
        """
        Adds the specified item to any one of the specified
        System.Collections.Concurrent.BlockingCollection{T} instances.
        A System.OperationCanceledException is thrown if the CancellationToken is
        canceled.
        
        :param collections: The array of collections.
        :param item: The item to be added to one of the collections.
        :param cancellationToken: A cancellation token to observe.
        :returns: The index of the collection in the  array to which the item was added.
        """
        ...

    def CompleteAdding(self) -> None:
        """
        Marks the System.Collections.Concurrent.BlockingCollection{T} instances
        as not accepting any more additions.
        """
        ...

    @overload
    def CopyTo(self, array: typing.List[System_Collections_Concurrent_BlockingCollection_T], index: int) -> None:
        """
        Copies all of the items in the System.Collections.Concurrent.BlockingCollection{T} instance
        to a compatible one-dimensional array, starting at the specified index of the target array.
        
        :param array: The one-dimensional array that is the destination of the elements copied from the System.Collections.Concurrent.BlockingCollection{T} instance. The array must have zero-based indexing.
        :param index: The zero-based index in  at which copying begins.
        """
        ...

    @overload
    def CopyTo(self, array: System.Array, index: int) -> None:
        """
        Copies all of the items in the System.Collections.Concurrent.BlockingCollection{T} instance
        to a compatible one-dimensional array, starting at the specified index of the target array.
        
        :param array: The one-dimensional array that is the destination of the elements copied from the System.Collections.Concurrent.BlockingCollection{T} instance. The array must have zero-based indexing.
        :param index: The zero-based index in  at which copying begins.
        """
        ...

    @overload
    def Dispose(self) -> None:
        """Releases resources used by the System.Collections.Concurrent.BlockingCollection{T} instance."""
        ...

    @overload
    def Dispose(self, disposing: bool) -> None:
        """
        Releases resources used by the System.Collections.Concurrent.BlockingCollection{T} instance.
        
        This method is protected.
        
        :param disposing: Whether being disposed explicitly (true) or due to a finalizer (false).
        """
        ...

    @overload
    def GetConsumingEnumerable(self) -> System.Collections.Generic.IEnumerable[System_Collections_Concurrent_BlockingCollection_T]:
        """
        Provides a consuming System.Collections.Generic.IEnumerable{T} for items in the collection.
        
        :returns: An System.Collections.Generic.IEnumerable{T} that removes and returns items from the collection.
        """
        ...

    @overload
    def GetConsumingEnumerable(self, cancellationToken: System.Threading.CancellationToken) -> System.Collections.Generic.IEnumerable[System_Collections_Concurrent_BlockingCollection_T]:
        """
        Provides a consuming System.Collections.Generic.IEnumerable{T} for items in the collection.
        Calling MoveNext on the returned enumerable will block if there is no data available, or will
        throw an System.OperationCanceledException if the CancellationToken is canceled.
        
        :param cancellationToken: A cancellation token to observe.
        :returns: An System.Collections.Generic.IEnumerable{T} that removes and returns items from the collection.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Concurrent_BlockingCollection_T]:
        """
        Provides an System.Collections.Generic.IEnumerator{T} for items in the collection.
        
        :returns: An System.Collections.Generic.IEnumerator{T} for the items in the collection.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        """
        Provides an System.Collections.IEnumerator for items in the collection.
        
        :returns: An System.Collections.IEnumerator for the items in the collection.
        """
        ...

    @overload
    def Take(self) -> System_Collections_Concurrent_BlockingCollection_T:
        """
        Takes an item from the System.Collections.Concurrent.BlockingCollection{T}.
        
        :returns: The item removed from the collection.
        """
        ...

    @overload
    def Take(self, cancellationToken: System.Threading.CancellationToken) -> System_Collections_Concurrent_BlockingCollection_T:
        """
        Takes an item from the System.Collections.Concurrent.BlockingCollection{T}.
        
        :returns: The item removed from the collection.
        """
        ...

    @staticmethod
    @overload
    def TakeFromAny(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: typing.Optional[System_Collections_Concurrent_BlockingCollection_T]) -> typing.Union[int, System_Collections_Concurrent_BlockingCollection_T]:
        """
        Takes an item from any one of the specified
        System.Collections.Concurrent.BlockingCollection{T} instances.
        
        :param collections: The array of collections.
        :param item: The item removed from one of the collections.
        :returns: The index of the collection in the  array from which the item was removed, or -1 if an item could not be removed.
        """
        ...

    @staticmethod
    @overload
    def TakeFromAny(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: typing.Optional[System_Collections_Concurrent_BlockingCollection_T], cancellationToken: System.Threading.CancellationToken) -> typing.Union[int, System_Collections_Concurrent_BlockingCollection_T]:
        """
        Takes an item from any one of the specified
        System.Collections.Concurrent.BlockingCollection{T} instances.
        A System.OperationCanceledException is thrown if the CancellationToken is
        canceled.
        
        :param collections: The array of collections.
        :param item: The item removed from one of the collections.
        :param cancellationToken: A cancellation token to observe.
        :returns: The index of the collection in the  array from which the item was removed, or -1 if an item could not be removed.
        """
        ...

    def ToArray(self) -> typing.List[System_Collections_Concurrent_BlockingCollection_T]:
        """
        Copies the items from the System.Collections.Concurrent.BlockingCollection{T} instance into a new array.
        
        :returns: An array containing copies of the elements of the collection.
        """
        ...

    @overload
    def TryAdd(self, item: System_Collections_Concurrent_BlockingCollection_T) -> bool:
        """
        Attempts to add the specified item to the System.Collections.Concurrent.BlockingCollection{T}.
        
        :param item: The item to be added to the collection.
        :returns: true if the  could be added; otherwise, false.
        """
        ...

    @overload
    def TryAdd(self, item: System_Collections_Concurrent_BlockingCollection_T, timeout: datetime.timedelta) -> bool:
        """
        Attempts to add the specified item to the System.Collections.Concurrent.BlockingCollection{T}.
        
        :param item: The item to be added to the collection.
        :param timeout: A System.TimeSpan that represents the number of milliseconds to wait, or a System.TimeSpan that represents -1 milliseconds to wait indefinitely.
        :returns: true if the  could be added to the collection within the alloted time; otherwise, false.
        """
        ...

    @overload
    def TryAdd(self, item: System_Collections_Concurrent_BlockingCollection_T, millisecondsTimeout: int) -> bool:
        """
        Attempts to add the specified item to the System.Collections.Concurrent.BlockingCollection{T}.
        
        :param item: The item to be added to the collection.
        :param millisecondsTimeout: The number of milliseconds to wait, or System.Threading.Timeout.Infinite (-1) to wait indefinitely.
        :returns: true if the  could be added to the collection within the alloted time; otherwise, false.
        """
        ...

    @overload
    def TryAdd(self, item: System_Collections_Concurrent_BlockingCollection_T, millisecondsTimeout: int, cancellationToken: System.Threading.CancellationToken) -> bool:
        """
        Attempts to add the specified item to the System.Collections.Concurrent.BlockingCollection{T}.
        A System.OperationCanceledException is thrown if the CancellationToken is
        canceled.
        
        :param item: The item to be added to the collection.
        :param millisecondsTimeout: The number of milliseconds to wait, or System.Threading.Timeout.Infinite (-1) to wait indefinitely.
        :param cancellationToken: A cancellation token to observe.
        :returns: true if the  could be added to the collection within the alloted time; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def TryAddToAny(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: System_Collections_Concurrent_BlockingCollection_T) -> int:
        """
        Attempts to add the specified item to any one of the specified
        System.Collections.Concurrent.BlockingCollection{T} instances.
        
        :param collections: The array of collections.
        :param item: The item to be added to one of the collections.
        :returns: The index of the collection in the  array to which the item was added, or -1 if the item could not be added.
        """
        ...

    @staticmethod
    @overload
    def TryAddToAny(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: System_Collections_Concurrent_BlockingCollection_T, timeout: datetime.timedelta) -> int:
        """
        Attempts to add the specified item to any one of the specified
        System.Collections.Concurrent.BlockingCollection{T} instances.
        
        :param collections: The array of collections.
        :param item: The item to be added to one of the collections.
        :param timeout: A System.TimeSpan that represents the number of milliseconds to wait, or a System.TimeSpan that represents -1 milliseconds to wait indefinitely.
        :returns: The index of the collection in the  array to which the item was added, or -1 if the item could not be added.
        """
        ...

    @staticmethod
    @overload
    def TryAddToAny(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: System_Collections_Concurrent_BlockingCollection_T, millisecondsTimeout: int) -> int:
        """
        Attempts to add the specified item to any one of the specified
        System.Collections.Concurrent.BlockingCollection{T} instances.
        
        :param collections: The array of collections.
        :param item: The item to be added to one of the collections.
        :param millisecondsTimeout: The number of milliseconds to wait, or System.Threading.Timeout.Infinite (-1) to wait indefinitely.
        :returns: The index of the collection in the  array to which the item was added, or -1 if the item could not be added.
        """
        ...

    @staticmethod
    @overload
    def TryAddToAny(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: System_Collections_Concurrent_BlockingCollection_T, millisecondsTimeout: int, cancellationToken: System.Threading.CancellationToken) -> int:
        """
        Attempts to add the specified item to any one of the specified
        System.Collections.Concurrent.BlockingCollection{T} instances.
        A System.OperationCanceledException is thrown if the CancellationToken is
        canceled.
        
        :param collections: The array of collections.
        :param item: The item to be added to one of the collections.
        :param millisecondsTimeout: The number of milliseconds to wait, or System.Threading.Timeout.Infinite (-1) to wait indefinitely.
        :param cancellationToken: A cancellation token to observe.
        :returns: The index of the collection in the  array to which the item was added, or -1 if the item could not be added.
        """
        ...

    @overload
    def TryTake(self, item: typing.Optional[System_Collections_Concurrent_BlockingCollection_T]) -> typing.Union[bool, System_Collections_Concurrent_BlockingCollection_T]:
        """
        Attempts to remove an item from the System.Collections.Concurrent.BlockingCollection{T}.
        
        :param item: The item removed from the collection.
        :returns: true if an item could be removed; otherwise, false.
        """
        ...

    @overload
    def TryTake(self, item: typing.Optional[System_Collections_Concurrent_BlockingCollection_T], timeout: datetime.timedelta) -> typing.Union[bool, System_Collections_Concurrent_BlockingCollection_T]:
        """
        Attempts to remove an item from the System.Collections.Concurrent.BlockingCollection{T}.
        
        :param item: The item removed from the collection.
        :param timeout: A System.TimeSpan that represents the number of milliseconds to wait, or a System.TimeSpan that represents -1 milliseconds to wait indefinitely.
        :returns: true if an item could be removed from the collection within the alloted time; otherwise, false.
        """
        ...

    @overload
    def TryTake(self, item: typing.Optional[System_Collections_Concurrent_BlockingCollection_T], millisecondsTimeout: int) -> typing.Union[bool, System_Collections_Concurrent_BlockingCollection_T]:
        """
        Attempts to remove an item from the System.Collections.Concurrent.BlockingCollection{T}.
        
        :param item: The item removed from the collection.
        :param millisecondsTimeout: The number of milliseconds to wait, or System.Threading.Timeout.Infinite (-1) to wait indefinitely.
        :returns: true if an item could be removed from the collection within the alloted time; otherwise, false.
        """
        ...

    @overload
    def TryTake(self, item: typing.Optional[System_Collections_Concurrent_BlockingCollection_T], millisecondsTimeout: int, cancellationToken: System.Threading.CancellationToken) -> typing.Union[bool, System_Collections_Concurrent_BlockingCollection_T]:
        """
        Attempts to remove an item from the System.Collections.Concurrent.BlockingCollection{T}.
        A System.OperationCanceledException is thrown if the CancellationToken is
        canceled.
        
        :param item: The item removed from the collection.
        :param millisecondsTimeout: The number of milliseconds to wait, or System.Threading.Timeout.Infinite (-1) to wait indefinitely.
        :param cancellationToken: A cancellation token to observe.
        :returns: true if an item could be removed from the collection within the alloted time; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def TryTakeFromAny(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: typing.Optional[System_Collections_Concurrent_BlockingCollection_T]) -> typing.Union[int, System_Collections_Concurrent_BlockingCollection_T]:
        """
        Attempts to remove an item from any one of the specified
        System.Collections.Concurrent.BlockingCollection{T} instances.
        
        :param collections: The array of collections.
        :param item: The item removed from one of the collections.
        :returns: The index of the collection in the  array from which the item was removed, or -1 if an item could not be removed.
        """
        ...

    @staticmethod
    @overload
    def TryTakeFromAny(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: typing.Optional[System_Collections_Concurrent_BlockingCollection_T], timeout: datetime.timedelta) -> typing.Union[int, System_Collections_Concurrent_BlockingCollection_T]:
        """
        Attempts to remove an item from any one of the specified
        System.Collections.Concurrent.BlockingCollection{T} instances.
        
        :param collections: The array of collections.
        :param item: The item removed from one of the collections.
        :param timeout: A System.TimeSpan that represents the number of milliseconds to wait, or a System.TimeSpan that represents -1 milliseconds to wait indefinitely.
        :returns: The index of the collection in the  array from which the item was removed, or -1 if an item could not be removed.
        """
        ...

    @staticmethod
    @overload
    def TryTakeFromAny(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: typing.Optional[System_Collections_Concurrent_BlockingCollection_T], millisecondsTimeout: int) -> typing.Union[int, System_Collections_Concurrent_BlockingCollection_T]:
        """
        Attempts to remove an item from any one of the specified
        System.Collections.Concurrent.BlockingCollection{T} instances.
        
        :param collections: The array of collections.
        :param item: The item removed from one of the collections.
        :param millisecondsTimeout: The number of milliseconds to wait, or System.Threading.Timeout.Infinite (-1) to wait indefinitely.
        :returns: The index of the collection in the  array from which the item was removed, or -1 if an item could not be removed.
        """
        ...

    @staticmethod
    @overload
    def TryTakeFromAny(collections: typing.List[System.Collections.Concurrent.BlockingCollection[System_Collections_Concurrent_BlockingCollection_T]], item: typing.Optional[System_Collections_Concurrent_BlockingCollection_T], millisecondsTimeout: int, cancellationToken: System.Threading.CancellationToken) -> typing.Union[int, System_Collections_Concurrent_BlockingCollection_T]:
        """
        Attempts to remove an item from any one of the specified
        System.Collections.Concurrent.BlockingCollection{T} instances.
        A System.OperationCanceledException is thrown if the CancellationToken is
        canceled.
        
        :param collections: The array of collections.
        :param item: The item removed from one of the collections.
        :param millisecondsTimeout: The number of milliseconds to wait, or System.Threading.Timeout.Infinite (-1) to wait indefinitely.
        :param cancellationToken: A cancellation token to observe.
        :returns: The index of the collection in the  array from which the item was removed, or -1 if an item could not be removed.
        """
        ...


class ConcurrentDictionary(typing.Generic[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue], System.Object, System.Collections.Generic.IDictionary[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue], System.Collections.IDictionary, System.Collections.Generic.IReadOnlyDictionary[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue], typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue]]):
    """Represents a thread-safe collection of keys and values."""

    @property
    def Comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Concurrent_ConcurrentDictionary_TKey]:
        """
        Gets the IEqualityComparer{TKey}
        that is used to determine equality of keys for the dictionary.
        """
        ...

    @property
    def Count(self) -> int:
        """Gets the number of key/value pairs contained in the ConcurrentDictionary{TKey,TValue}."""
        ...

    @property
    def IsEmpty(self) -> bool:
        """Gets a value that indicates whether the ConcurrentDictionary{TKey,TValue} is empty."""
        ...

    @property
    def Keys(self) -> System.Collections.Generic.ICollection[System_Collections_Concurrent_ConcurrentDictionary_TKey]:
        """Gets a collection containing the keys in the Dictionary{TKey,TValue}."""
        ...

    @property
    def Values(self) -> System.Collections.Generic.ICollection[System_Collections_Concurrent_ConcurrentDictionary_TValue]:
        """Gets a collection containing the values in the Dictionary{TKey,TValue}."""
        ...

    @property
    def IsReadOnly(self) -> bool:
        """Gets a value indicating whether the dictionary is read-only."""
        ...

    @property
    def IsFixedSize(self) -> bool:
        """Gets a value indicating whether the IDictionary has a fixed size."""
        ...

    @property
    def IsSynchronized(self) -> bool:
        """
        Gets a value indicating whether access to the ICollection is
        synchronized with the SyncRoot.
        """
        ...

    @property
    def SyncRoot(self) -> System.Object:
        """Gets an object that can be used to synchronize access to the ICollection. This property is not supported."""
        ...

    @overload
    def __getitem__(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey) -> System_Collections_Concurrent_ConcurrentDictionary_TValue:
        """
        Gets or sets the value associated with the specified key.
        
        :param key: The key of the value to get or set.
        """
        ...

    @overload
    def __getitem__(self, key: typing.Any) -> typing.Any:
        """
        Gets or sets the value associated with the specified key.
        
        :param key: The key of the value to get or set.
        """
        ...

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the ConcurrentDictionary{TKey,TValue}
        class that is empty, has the default concurrency level, has the default initial capacity, and
        uses the default comparer for the key type.
        """
        ...

    @overload
    def __init__(self, concurrencyLevel: int, capacity: int) -> None:
        """
        Initializes a new instance of the ConcurrentDictionary{TKey,TValue}
        class that is empty, has the specified concurrency level and capacity, and uses the default
        comparer for the key type.
        
        :param concurrencyLevel: The estimated number of threads that will update the ConcurrentDictionary{TKey,TValue} concurrently.
        :param capacity: The initial number of elements that the ConcurrentDictionary{TKey,TValue} can contain.
        """
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue]]) -> None:
        """
        Initializes a new instance of the ConcurrentDictionary{TKey,TValue}
        class that contains elements copied from the specified IEnumerable{T}, has the default concurrency
        level, has the default initial capacity, and uses the default comparer for the key type.
        
        :param collection: The IEnumerable{T} whose elements are copied to the new ConcurrentDictionary{TKey,TValue}.
        """
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Concurrent_ConcurrentDictionary_TKey]) -> None:
        """
        Initializes a new instance of the ConcurrentDictionary{TKey,TValue}
        class that is empty, has the specified concurrency level and capacity, and uses the specified
        IEqualityComparer{TKey}.
        
        :param comparer: The IEqualityComparer{TKey} implementation to use when comparing keys.
        """
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue]], comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Concurrent_ConcurrentDictionary_TKey]) -> None:
        """
        Initializes a new instance of the ConcurrentDictionary{TKey,TValue}
        class that contains elements copied from the specified IEnumerable, has the default concurrency
        level, has the default initial capacity, and uses the specified IEqualityComparer{TKey}.
        
        :param collection: The IEnumerable{T} whose elements are copied to the new ConcurrentDictionary{TKey,TValue}.
        :param comparer: The IEqualityComparer{TKey} implementation to use when comparing keys.
        """
        ...

    @overload
    def __init__(self, concurrencyLevel: int, collection: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue]], comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Concurrent_ConcurrentDictionary_TKey]) -> None:
        """
        Initializes a new instance of the ConcurrentDictionary{TKey,TValue}
        class that contains elements copied from the specified IEnumerable,
        has the specified concurrency level, has the specified initial capacity, and uses the specified
        IEqualityComparer{TKey}.
        
        :param concurrencyLevel: The estimated number of threads that will update the ConcurrentDictionary{TKey,TValue} concurrently.
        :param collection: The IEnumerable{T} whose elements are copied to the new ConcurrentDictionary{TKey,TValue}.
        :param comparer: The IEqualityComparer{TKey} implementation to use when comparing keys.
        """
        ...

    @overload
    def __init__(self, concurrencyLevel: int, capacity: int, comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Concurrent_ConcurrentDictionary_TKey]) -> None:
        """
        Initializes a new instance of the ConcurrentDictionary{TKey,TValue}
        class that is empty, has the specified concurrency level, has the specified initial capacity, and
        uses the specified IEqualityComparer{TKey}.
        
        :param concurrencyLevel: The estimated number of threads that will update the ConcurrentDictionary{TKey,TValue} concurrently.
        :param capacity: The initial number of elements that the ConcurrentDictionary{TKey,TValue} can contain.
        :param comparer: The IEqualityComparer{TKey} implementation to use when comparing keys.
        """
        ...

    @overload
    def __setitem__(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey, value: System_Collections_Concurrent_ConcurrentDictionary_TValue) -> None:
        """
        Gets or sets the value associated with the specified key.
        
        :param key: The key of the value to get or set.
        """
        ...

    @overload
    def __setitem__(self, key: typing.Any, value: typing.Any) -> None:
        """
        Gets or sets the value associated with the specified key.
        
        :param key: The key of the value to get or set.
        """
        ...

    @overload
    def Add(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey, value: System_Collections_Concurrent_ConcurrentDictionary_TValue) -> None:
        ...

    @overload
    def Add(self, keyValuePair: System.Collections.Generic.KeyValuePair[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue]) -> None:
        ...

    @overload
    def Add(self, key: typing.Any, value: typing.Any) -> None:
        ...

    @overload
    def AddOrUpdate(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey, addValueFactory: typing.Callable[[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_AddOrUpdate_TArg], System_Collections_Concurrent_ConcurrentDictionary_TValue], updateValueFactory: typing.Callable[[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue, System_Collections_Concurrent_ConcurrentDictionary_AddOrUpdate_TArg], System_Collections_Concurrent_ConcurrentDictionary_TValue], factoryArgument: System_Collections_Concurrent_ConcurrentDictionary_AddOrUpdate_TArg) -> System_Collections_Concurrent_ConcurrentDictionary_TValue:
        """
        Adds a key/value pair to the ConcurrentDictionary{TKey,TValue} if the key does not already
        exist, or updates a key/value pair in the ConcurrentDictionary{TKey,TValue} if the key
        already exists.
        
        :param key: The key to be added or whose value should be updated
        :param addValueFactory: The function used to generate a value for an absent key
        :param updateValueFactory: The function used to generate a new value for an existing key based on the key's existing value
        :param factoryArgument: An argument to pass into  and .
        :returns: The new value for the key.  This will be either be the result of addValueFactory (if the key was absent) or the result of updateValueFactory (if the key was present).
        """
        ...

    @overload
    def AddOrUpdate(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey, addValueFactory: typing.Callable[[System_Collections_Concurrent_ConcurrentDictionary_TKey], System_Collections_Concurrent_ConcurrentDictionary_TValue], updateValueFactory: typing.Callable[[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue], System_Collections_Concurrent_ConcurrentDictionary_TValue]) -> System_Collections_Concurrent_ConcurrentDictionary_TValue:
        """
        Adds a key/value pair to the ConcurrentDictionary{TKey,TValue} if the key does not already
        exist, or updates a key/value pair in the ConcurrentDictionary{TKey,TValue} if the key
        already exists.
        
        :param key: The key to be added or whose value should be updated
        :param addValueFactory: The function used to generate a value for an absent key
        :param updateValueFactory: The function used to generate a new value for an existing key based on the key's existing value
        :returns: The new value for the key.  This will be either the result of addValueFactory (if the key was absent) or the result of updateValueFactory (if the key was present).
        """
        ...

    @overload
    def AddOrUpdate(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey, addValue: System_Collections_Concurrent_ConcurrentDictionary_TValue, updateValueFactory: typing.Callable[[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue], System_Collections_Concurrent_ConcurrentDictionary_TValue]) -> System_Collections_Concurrent_ConcurrentDictionary_TValue:
        """
        Adds a key/value pair to the ConcurrentDictionary{TKey,TValue} if the key does not already
        exist, or updates a key/value pair in the ConcurrentDictionary{TKey,TValue} if the key
        already exists.
        
        :param key: The key to be added or whose value should be updated
        :param addValue: The value to be added for an absent key
        :param updateValueFactory: The function used to generate a new value for an existing key based on the key's existing value
        :returns: The new value for the key.  This will be either the value of addValue (if the key was absent) or the result of updateValueFactory (if the key was present).
        """
        ...

    def Clear(self) -> None:
        """Removes all keys and values from the ConcurrentDictionary{TKey,TValue}."""
        ...

    @overload
    def Contains(self, keyValuePair: System.Collections.Generic.KeyValuePair[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue]) -> bool:
        """
        Determines whether the ICollection{T}
        contains a specific key and value.
        
        :param keyValuePair: The KeyValuePair{TKey,TValue} structure to locate in the ICollection{TValue}.
        :returns: true if the  is found in the ICollection{T}; otherwise, false.
        """
        ...

    @overload
    def Contains(self, key: typing.Any) -> bool:
        """
        Gets whether the IDictionary contains an
        element with the specified key.
        
        :param key: The key to locate in the IDictionary.
        :returns: true if the IDictionary contains an element with the specified key; otherwise, false.
        """
        ...

    def ContainsKey(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey) -> bool:
        """
        Determines whether the ConcurrentDictionary{TKey, TValue} contains the specified key.
        
        :param key: The key to locate in the ConcurrentDictionary{TKey, TValue}.
        :returns: true if the ConcurrentDictionary{TKey, TValue} contains an element with the specified key; otherwise, false.
        """
        ...

    @overload
    def CopyTo(self, array: typing.List[System.Collections.Generic.KeyValuePair[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue]], index: int) -> None:
        """
        Copies the elements of the ICollection{T} to an array of type KeyValuePair{TKey,TValue},
        starting at the specified array index.
        
        :param array: The one-dimensional array of type KeyValuePair{TKey,TValue} that is the destination of the KeyValuePair{TKey,TValue} elements copied from the ICollection. The array must have zero-based indexing.
        :param index: The zero-based index in  at which copying begins.
        """
        ...

    @overload
    def CopyTo(self, array: System.Array, index: int) -> None:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue]]:
        """
        Returns an enumerator that iterates through the ConcurrentDictionary{TKey,TValue}.
        
        :returns: An enumerator for the ConcurrentDictionary{TKey,TValue}.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IDictionaryEnumerator:
        """
        Provides an IDictionaryEnumerator for the
        IDictionary.
        
        :returns: An IDictionaryEnumerator for the IDictionary.
        """
        ...

    @overload
    def GetOrAdd(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey, valueFactory: typing.Callable[[System_Collections_Concurrent_ConcurrentDictionary_TKey], System_Collections_Concurrent_ConcurrentDictionary_TValue]) -> System_Collections_Concurrent_ConcurrentDictionary_TValue:
        """
        Adds a key/value pair to the ConcurrentDictionary{TKey,TValue}
        if the key does not already exist.
        
        :param key: The key of the element to add.
        :param valueFactory: The function used to generate a value for the key
        :returns: The value for the key.  This will be either the existing value for the key if the key is already in the dictionary, or the new value for the key as returned by valueFactory if the key was not in the dictionary.
        """
        ...

    @overload
    def GetOrAdd(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey, valueFactory: typing.Callable[[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_GetOrAdd_TArg], System_Collections_Concurrent_ConcurrentDictionary_TValue], factoryArgument: System_Collections_Concurrent_ConcurrentDictionary_GetOrAdd_TArg) -> System_Collections_Concurrent_ConcurrentDictionary_TValue:
        """
        Adds a key/value pair to the ConcurrentDictionary{TKey,TValue}
        if the key does not already exist.
        
        :param key: The key of the element to add.
        :param valueFactory: The function used to generate a value for the key
        :param factoryArgument: An argument value to pass into .
        :returns: The value for the key.  This will be either the existing value for the key if the key is already in the dictionary, or the new value for the key as returned by valueFactory if the key was not in the dictionary.
        """
        ...

    @overload
    def GetOrAdd(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey, value: System_Collections_Concurrent_ConcurrentDictionary_TValue) -> System_Collections_Concurrent_ConcurrentDictionary_TValue:
        """
        Adds a key/value pair to the ConcurrentDictionary{TKey,TValue}
        if the key does not already exist.
        
        :param key: The key of the element to add.
        :param value: the value to be added, if the key does not already exist
        :returns: The value for the key.  This will be either the existing value for the key if the key is already in the dictionary, or the new value if the key was not in the dictionary.
        """
        ...

    @overload
    def Remove(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey) -> bool:
        """
        Removes the element with the specified key from the IDictionary{TKey,TValue}.
        
        :param key: The key of the element to remove.
        :returns: true if the element is successfully remove; otherwise false. This method also returns false if  was not found in the original IDictionary{TKey,TValue}.
        """
        ...

    @overload
    def Remove(self, keyValuePair: System.Collections.Generic.KeyValuePair[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue]) -> bool:
        """
        Removes a key and value from the dictionary.
        
        :param keyValuePair: The KeyValuePair{TKey,TValue} structure representing the key and value to remove from the Dictionary{TKey,TValue}.
        :returns: true if the key and value represented by  is successfully found and removed; otherwise, false.
        """
        ...

    @overload
    def Remove(self, key: typing.Any) -> None:
        """
        Removes the element with the specified key from the IDictionary.
        
        :param key: The key of the element to remove.
        """
        ...

    def ToArray(self) -> typing.List[System.Collections.Generic.KeyValuePair[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue]]:
        """
        Copies the key and value pairs stored in the ConcurrentDictionary{TKey,TValue} to a
        new array.
        
        :returns: A new array containing a snapshot of key and value pairs copied from the ConcurrentDictionary{TKey,TValue}.
        """
        ...

    def TryAdd(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey, value: System_Collections_Concurrent_ConcurrentDictionary_TValue) -> bool:
        """
        Attempts to add the specified key and value to the ConcurrentDictionary{TKey, TValue}.
        
        :param key: The key of the element to add.
        :param value: The value of the element to add. The value can be a null reference (Nothing in Visual Basic) for reference types.
        :returns: true if the key/value pair was added to the ConcurrentDictionary{TKey, TValue} successfully; otherwise, false.
        """
        ...

    def TryGetValue(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey, value: typing.Optional[System_Collections_Concurrent_ConcurrentDictionary_TValue]) -> typing.Union[bool, System_Collections_Concurrent_ConcurrentDictionary_TValue]:
        """
        Attempts to get the value associated with the specified key from the ConcurrentDictionary{TKey,TValue}.
        
        :param key: The key of the value to get.
        :param value: When this method returns,  contains the object from the ConcurrentDictionary{TKey,TValue} with the specified key or the default value of TValue, if the operation failed.
        :returns: true if the key was found in the ConcurrentDictionary{TKey,TValue}; otherwise, false.
        """
        ...

    @overload
    def TryRemove(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey, value: typing.Optional[System_Collections_Concurrent_ConcurrentDictionary_TValue]) -> typing.Union[bool, System_Collections_Concurrent_ConcurrentDictionary_TValue]:
        """
        Attempts to remove and return the value with the specified key from the ConcurrentDictionary{TKey, TValue}.
        
        :param key: The key of the element to remove and return.
        :param value: When this method returns,  contains the object removed from the ConcurrentDictionary{TKey,TValue} or the default value of TValue if the operation failed.
        :returns: true if an object was removed successfully; otherwise, false.
        """
        ...

    @overload
    def TryRemove(self, item: System.Collections.Generic.KeyValuePair[System_Collections_Concurrent_ConcurrentDictionary_TKey, System_Collections_Concurrent_ConcurrentDictionary_TValue]) -> bool:
        """
        Removes a key and value from the dictionary.
        
        :param item: The KeyValuePair{TKey,TValue} representing the key and value to remove.
        :returns: true if the key and value represented by  are successfully found and removed; otherwise, false.
        """
        ...

    def TryUpdate(self, key: System_Collections_Concurrent_ConcurrentDictionary_TKey, newValue: System_Collections_Concurrent_ConcurrentDictionary_TValue, comparisonValue: System_Collections_Concurrent_ConcurrentDictionary_TValue) -> bool:
        """
        Updates the value associated with  to  if the existing value is equal
        to .
        
        :param key: The key whose value is compared with  and possibly replaced.
        :param newValue: The value that replaces the value of the element with  if the comparison results in equality.
        :param comparisonValue: The value that is compared to the value of the element with .
        :returns: true if the value with  was equal to  and replaced with ; otherwise, false.
        """
        ...


class ConcurrentBag(typing.Generic[System_Collections_Concurrent_ConcurrentBag_T], System.Object, System.Collections.Concurrent.IProducerConsumerCollection[System_Collections_Concurrent_ConcurrentBag_T], System.Collections.Generic.IReadOnlyCollection[System_Collections_Concurrent_ConcurrentBag_T], typing.Iterable[System_Collections_Concurrent_ConcurrentBag_T]):
    """Represents a thread-safe, unordered collection of objects."""

    @property
    def Count(self) -> int:
        """Gets the number of elements contained in the ConcurrentBag{T}."""
        ...

    @property
    def IsEmpty(self) -> bool:
        """Gets a value that indicates whether the ConcurrentBag{T} is empty."""
        ...

    @property
    def IsSynchronized(self) -> bool:
        """
        Gets a value indicating whether access to the System.Collections.ICollection is
        synchronized with the SyncRoot.
        """
        ...

    @property
    def SyncRoot(self) -> System.Object:
        """Gets an object that can be used to synchronize access to the System.Collections.ICollection. This property is not supported."""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the ConcurrentBag{T} class."""
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Concurrent_ConcurrentBag_T]) -> None:
        """
        Initializes a new instance of the ConcurrentBag{T}
        class that contains elements copied from the specified collection.
        
        :param collection: The collection whose elements are copied to the new ConcurrentBag{T}.
        """
        ...

    def Add(self, item: System_Collections_Concurrent_ConcurrentBag_T) -> None:
        """
        Adds an object to the ConcurrentBag{T}.
        
        :param item: The object to be added to the ConcurrentBag{T}. The value can be a null reference (Nothing in Visual Basic) for reference types.
        """
        ...

    def Clear(self) -> None:
        """Removes all values from the ConcurrentBag{T}."""
        ...

    @overload
    def CopyTo(self, array: typing.List[System_Collections_Concurrent_ConcurrentBag_T], index: int) -> None:
        """
        Copies the ConcurrentBag{T} elements to an existing
        one-dimensional System.Array, starting at the specified array
        index.
        
        :param array: The one-dimensional System.Array that is the destination of the elements copied from the ConcurrentBag{T}. The System.Array must have zero-based indexing.
        :param index: The zero-based index in  at which copying begins.
        """
        ...

    @overload
    def CopyTo(self, array: System.Array, index: int) -> None:
        """
        Copies the elements of the System.Collections.ICollection to an System.Array, starting at a particular
        System.Array index.
        
        :param array: The one-dimensional System.Array that is the destination of the elements copied from the ConcurrentBag{T}. The System.Array must have zero-based indexing.
        :param index: The zero-based index in  at which copying begins.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Concurrent_ConcurrentBag_T]:
        """
        Returns an enumerator that iterates through the ConcurrentBag{T}.
        
        :returns: An enumerator for the contents of the ConcurrentBag{T}.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        """
        Returns an enumerator that iterates through the ConcurrentBag{T}.
        
        :returns: An enumerator for the contents of the ConcurrentBag{T}.
        """
        ...

    def ToArray(self) -> typing.List[System_Collections_Concurrent_ConcurrentBag_T]:
        """
        Copies the ConcurrentBag{T} elements to a new array.
        
        :returns: A new array containing a snapshot of elements copied from the ConcurrentBag{T}.
        """
        ...

    def TryAdd(self, item: System_Collections_Concurrent_ConcurrentBag_T) -> bool:
        """
        Attempts to add an object to the ConcurrentBag{T}.
        
        :param item: The object to be added to the ConcurrentBag{T}. The value can be a null reference (Nothing in Visual Basic) for reference types.
        :returns: Always returns true.
        """
        ...

    def TryPeek(self, result: typing.Optional[System_Collections_Concurrent_ConcurrentBag_T]) -> typing.Union[bool, System_Collections_Concurrent_ConcurrentBag_T]:
        """
        Attempts to return an object from the ConcurrentBag{T} without removing it.
        
        :param result: When this method returns,  contains an object from the ConcurrentBag{T} or the default value of T if the operation failed.
        :returns: true if and object was returned successfully; otherwise, false.
        """
        ...

    def TryTake(self, result: typing.Optional[System_Collections_Concurrent_ConcurrentBag_T]) -> typing.Union[bool, System_Collections_Concurrent_ConcurrentBag_T]:
        """
        Attempts to remove and return an object from the ConcurrentBag{T}.
        
        :param result: When this method returns,  contains the object removed from the ConcurrentBag{T} or the default value of T if the operation failed.
        :returns: true if an object was removed successfully; otherwise, false.
        """
        ...


class OrderablePartitioner(typing.Generic[System_Collections_Concurrent_OrderablePartitioner_TSource], System.Collections.Concurrent.Partitioner[System_Collections_Concurrent_OrderablePartitioner_TSource], metaclass=abc.ABCMeta):
    """Represents a particular manner of splitting an orderable data source into multiple partitions."""

    @property
    def KeysOrderedInEachPartition(self) -> bool:
        """Gets whether elements in each partition are yielded in the order of increasing keys."""
        ...

    @KeysOrderedInEachPartition.setter
    def KeysOrderedInEachPartition(self, value: bool):
        """Gets whether elements in each partition are yielded in the order of increasing keys."""
        ...

    @property
    def KeysOrderedAcrossPartitions(self) -> bool:
        """Gets whether elements in an earlier partition always come before elements in a later partition."""
        ...

    @KeysOrderedAcrossPartitions.setter
    def KeysOrderedAcrossPartitions(self, value: bool):
        """Gets whether elements in an earlier partition always come before elements in a later partition."""
        ...

    @property
    def KeysNormalized(self) -> bool:
        """Gets whether order keys are normalized."""
        ...

    @KeysNormalized.setter
    def KeysNormalized(self, value: bool):
        """Gets whether order keys are normalized."""
        ...

    def __init__(self, keysOrderedInEachPartition: bool, keysOrderedAcrossPartitions: bool, keysNormalized: bool) -> None:
        """
        Initializes a new instance of the OrderablePartitioner{TSource} class with the
        specified constraints on the index keys.
        
        This method is protected.
        
        :param keysOrderedInEachPartition: Indicates whether the elements in each partition are yielded in the order of increasing keys.
        :param keysOrderedAcrossPartitions: Indicates whether elements in an earlier partition always come before elements in a later partition. If true, each element in partition 0 has a smaller order key than any element in partition 1, each element in partition 1 has a smaller order key than any element in partition 2, and so on.
        :param keysNormalized: Indicates whether keys are normalized. If true, all order keys are distinct integers in the range [0 .. numberOfElements-1]. If false, order keys must still be distinct, but only their relative order is considered, not their absolute values.
        """
        ...

    def GetDynamicPartitions(self) -> System.Collections.Generic.IEnumerable[System_Collections_Concurrent_OrderablePartitioner_TSource]:
        """
        Creates an object that can partition the underlying collection into a variable number of
        partitions.
        
        :returns: An object that can create partitions over the underlying data source.
        """
        ...

    def GetOrderableDynamicPartitions(self) -> System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[int, System_Collections_Concurrent_OrderablePartitioner_TSource]]:
        """
        Creates an object that can partition the underlying collection into a variable number of
        partitions.
        
        :returns: An object that can create partitions over the underlying data source.
        """
        ...

    def GetOrderablePartitions(self, partitionCount: int) -> System.Collections.Generic.IList[System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[int, System_Collections_Concurrent_OrderablePartitioner_TSource]]]:
        """
        Partitions the underlying collection into the specified number of orderable partitions.
        
        :param partitionCount: The number of partitions to create.
        :returns: A list containing  enumerators.
        """
        ...

    def GetPartitions(self, partitionCount: int) -> System.Collections.Generic.IList[System.Collections.Generic.IEnumerator[System_Collections_Concurrent_OrderablePartitioner_TSource]]:
        """
        Partitions the underlying collection into the given number of ordered partitions.
        
        :param partitionCount: The number of partitions to create.
        :returns: A list containing  enumerators.
        """
        ...


class EnumerablePartitionerOptions(System.Enum):
    """
    Out-of-the-box partitioners are created with a set of default behaviors.
    For example, by default, some form of buffering and chunking will be employed to achieve
    optimal performance in the common scenario where an IEnumerable{T} implementation is fast and
    non-blocking.  These behaviors can be overridden via this enumeration.
    """

    # Cannot convert to Python: None = ...
    """Use the default behavior (i.e., use buffering to achieve optimal performance)"""

    NoBuffering = ...
    """
    Creates a partitioner that will take items from the source enumerable one at a time
    and will not use intermediate storage that can be accessed more efficiently by multiple threads.
    This option provides support for low latency (items will be processed as soon as they are available from
    the source) and partial support for dependencies between items (a thread cannot deadlock waiting for an item
    that it, itself, is responsible for processing).
    """


class Partitioner(typing.Generic[System_Collections_Concurrent_Partitioner_TSource], System.Object, metaclass=abc.ABCMeta):
    """Represents a particular manner of splitting a data source into multiple partitions."""

    @property
    def SupportsDynamicPartitions(self) -> bool:
        """Gets whether additional partitions can be created dynamically."""
        ...

    @staticmethod
    @overload
    def Create(list: System.Collections.Generic.IList[System_Collections_Concurrent_Partitioner_Create_TSource], loadBalance: bool) -> System.Collections.Concurrent.OrderablePartitioner[System_Collections_Concurrent_Partitioner_Create_TSource]:
        """
        Creates an orderable partitioner from an System.Collections.Generic.IList{T}
        instance.
        
        :param list: The list to be partitioned.
        :param loadBalance: A Boolean value that indicates whether the created partitioner should dynamically load balance between partitions rather than statically partition.
        :returns: An orderable partitioner based on the input list.
        """
        ...

    @staticmethod
    @overload
    def Create(array: typing.List[System_Collections_Concurrent_Partitioner_Create_TSource], loadBalance: bool) -> System.Collections.Concurrent.OrderablePartitioner[System_Collections_Concurrent_Partitioner_Create_TSource]:
        """
        Creates an orderable partitioner from a System.Array instance.
        
        :param array: The array to be partitioned.
        :param loadBalance: A Boolean value that indicates whether the created partitioner should dynamically load balance between partitions rather than statically partition.
        :returns: An orderable partitioner based on the input array.
        """
        ...

    @staticmethod
    @overload
    def Create(source: System.Collections.Generic.IEnumerable[System_Collections_Concurrent_Partitioner_Create_TSource]) -> System.Collections.Concurrent.OrderablePartitioner[System_Collections_Concurrent_Partitioner_Create_TSource]:
        """
        Creates an orderable partitioner from a System.Collections.Generic.IEnumerable{TSource} instance.
        
        :param source: The enumerable to be partitioned.
        :returns: An orderable partitioner based on the input array.
        """
        ...

    @staticmethod
    @overload
    def Create(source: System.Collections.Generic.IEnumerable[System_Collections_Concurrent_Partitioner_Create_TSource], partitionerOptions: System.Collections.Concurrent.EnumerablePartitionerOptions) -> System.Collections.Concurrent.OrderablePartitioner[System_Collections_Concurrent_Partitioner_Create_TSource]:
        """
        Creates an orderable partitioner from a System.Collections.Generic.IEnumerable{TSource} instance.
        
        :param source: The enumerable to be partitioned.
        :param partitionerOptions: Options to control the buffering behavior of the partitioner.
        :returns: An orderable partitioner based on the input array.
        """
        ...

    @staticmethod
    @overload
    def Create(fromInclusive: int, toExclusive: int) -> System.Collections.Concurrent.OrderablePartitioner[System.Tuple[int, int]]:
        """
        Creates a partitioner that chunks the user-specified range.
        
        :param fromInclusive: The lower, inclusive bound of the range.
        :param toExclusive: The upper, exclusive bound of the range.
        :returns: A partitioner.
        """
        ...

    @staticmethod
    @overload
    def Create(fromInclusive: int, toExclusive: int, rangeSize: int) -> System.Collections.Concurrent.OrderablePartitioner[System.Tuple[int, int]]:
        """
        Creates a partitioner that chunks the user-specified range.
        
        :param fromInclusive: The lower, inclusive bound of the range.
        :param toExclusive: The upper, exclusive bound of the range.
        :param rangeSize: The size of each subrange.
        :returns: A partitioner.
        """
        ...

    @staticmethod
    @overload
    def Create(fromInclusive: int, toExclusive: int) -> System.Collections.Concurrent.OrderablePartitioner[System.Tuple[int, int]]:
        """
        Creates a partitioner that chunks the user-specified range.
        
        :param fromInclusive: The lower, inclusive bound of the range.
        :param toExclusive: The upper, exclusive bound of the range.
        :returns: A partitioner.
        """
        ...

    @staticmethod
    @overload
    def Create(fromInclusive: int, toExclusive: int, rangeSize: int) -> System.Collections.Concurrent.OrderablePartitioner[System.Tuple[int, int]]:
        """
        Creates a partitioner that chunks the user-specified range.
        
        :param fromInclusive: The lower, inclusive bound of the range.
        :param toExclusive: The upper, exclusive bound of the range.
        :param rangeSize: The size of each subrange.
        :returns: A partitioner.
        """
        ...

    def GetDynamicPartitions(self) -> System.Collections.Generic.IEnumerable[System_Collections_Concurrent_Partitioner_TSource]:
        """
        Creates an object that can partition the underlying collection into a variable number of
        partitions.
        
        :returns: An object that can create partitions over the underlying data source.
        """
        ...

    def GetPartitions(self, partitionCount: int) -> System.Collections.Generic.IList[System.Collections.Generic.IEnumerator[System_Collections_Concurrent_Partitioner_TSource]]:
        """
        Partitions the underlying collection into the given number of partitions.
        
        :param partitionCount: The number of partitions to create.
        :returns: A list containing  enumerators.
        """
        ...


