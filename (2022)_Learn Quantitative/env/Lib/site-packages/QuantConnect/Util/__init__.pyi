from typing import overload
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Data
import QuantConnect.Data.Fundamental
import QuantConnect.Data.Market
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import QuantConnect.Securities
import QuantConnect.Util
import System
import System.Collections
import System.Collections.Generic
import System.Collections.Immutable
import System.Drawing
import System.IO
import System.Text
import System.Text.RegularExpressions
import System.Threading

JsonConverter = typing.Any
IsoDateTimeConverter = typing.Any
QuantConnect_Util_MarketHoursDatabaseJsonConverter_MarketHoursDatabaseJson = typing.Any
Expression = typing.Any

QuantConnect_Util_BusyBlockingCollection_T = typing.TypeVar("QuantConnect_Util_BusyBlockingCollection_T")
QuantConnect_Util_TypeChangeJsonConverter_T = typing.TypeVar("QuantConnect_Util_TypeChangeJsonConverter_T")
QuantConnect_Util_TypeChangeJsonConverter_TResult = typing.TypeVar("QuantConnect_Util_TypeChangeJsonConverter_TResult")
QuantConnect_Util_FixedSizeQueue_T = typing.TypeVar("QuantConnect_Util_FixedSizeQueue_T")
QuantConnect_Util_ComparisonOperator_Compare_T = typing.TypeVar("QuantConnect_Util_ComparisonOperator_Compare_T")
QuantConnect_Util_NullStringValueConverter_T = typing.TypeVar("QuantConnect_Util_NullStringValueConverter_T")
QuantConnect_Util_EnumeratorExtensions_Where_T = typing.TypeVar("QuantConnect_Util_EnumeratorExtensions_Where_T")
QuantConnect_Util_EnumeratorExtensions_Select_TResult = typing.TypeVar("QuantConnect_Util_EnumeratorExtensions_Select_TResult")
QuantConnect_Util_EnumeratorExtensions_Select_T = typing.TypeVar("QuantConnect_Util_EnumeratorExtensions_Select_T")
QuantConnect_Util_EnumeratorExtensions_SelectMany_TResult = typing.TypeVar("QuantConnect_Util_EnumeratorExtensions_SelectMany_TResult")
QuantConnect_Util_EnumeratorExtensions_SelectMany_T = typing.TypeVar("QuantConnect_Util_EnumeratorExtensions_SelectMany_T")
QuantConnect_Util_MemoizingEnumerable_T = typing.TypeVar("QuantConnect_Util_MemoizingEnumerable_T")
QuantConnect_Util_LinqExtensions_Median_T = typing.TypeVar("QuantConnect_Util_LinqExtensions_Median_T")
QuantConnect_Util_LinqExtensions_Median_TProperty = typing.TypeVar("QuantConnect_Util_LinqExtensions_Median_TProperty")
QuantConnect_Util_LinqExtensions_BinarySearch_TSearch = typing.TypeVar("QuantConnect_Util_LinqExtensions_BinarySearch_TSearch")
QuantConnect_Util_LinqExtensions_BinarySearch_TItem = typing.TypeVar("QuantConnect_Util_LinqExtensions_BinarySearch_TItem")
QuantConnect_Util_LinqExtensions_Range_T = typing.TypeVar("QuantConnect_Util_LinqExtensions_Range_T")
QuantConnect_Util_LinqExtensions_GetValueOrDefault_V = typing.TypeVar("QuantConnect_Util_LinqExtensions_GetValueOrDefault_V")
QuantConnect_Util_LinqExtensions_GetValueOrDefault_K = typing.TypeVar("QuantConnect_Util_LinqExtensions_GetValueOrDefault_K")
QuantConnect_Util_LinqExtensions_ToDictionary_K = typing.TypeVar("QuantConnect_Util_LinqExtensions_ToDictionary_K")
QuantConnect_Util_LinqExtensions_ToDictionary_V = typing.TypeVar("QuantConnect_Util_LinqExtensions_ToDictionary_V")
QuantConnect_Util_LinqExtensions_ToReadOnlyDictionary_K = typing.TypeVar("QuantConnect_Util_LinqExtensions_ToReadOnlyDictionary_K")
QuantConnect_Util_LinqExtensions_ToReadOnlyDictionary_V = typing.TypeVar("QuantConnect_Util_LinqExtensions_ToReadOnlyDictionary_V")
QuantConnect_Util_LinqExtensions_ToHashSet_TResult = typing.TypeVar("QuantConnect_Util_LinqExtensions_ToHashSet_TResult")
QuantConnect_Util_LinqExtensions_ToHashSet_T = typing.TypeVar("QuantConnect_Util_LinqExtensions_ToHashSet_T")
QuantConnect_Util_LinqExtensions_ToList_TResult = typing.TypeVar("QuantConnect_Util_LinqExtensions_ToList_TResult")
QuantConnect_Util_LinqExtensions_ToList_T = typing.TypeVar("QuantConnect_Util_LinqExtensions_ToList_T")
QuantConnect_Util_LinqExtensions_ToArray_TResult = typing.TypeVar("QuantConnect_Util_LinqExtensions_ToArray_TResult")
QuantConnect_Util_LinqExtensions_ToArray_T = typing.TypeVar("QuantConnect_Util_LinqExtensions_ToArray_T")
QuantConnect_Util_LinqExtensions_ToImmutableArray_TResult = typing.TypeVar("QuantConnect_Util_LinqExtensions_ToImmutableArray_TResult")
QuantConnect_Util_LinqExtensions_ToImmutableArray_T = typing.TypeVar("QuantConnect_Util_LinqExtensions_ToImmutableArray_T")
QuantConnect_Util_LinqExtensions_Except_T = typing.TypeVar("QuantConnect_Util_LinqExtensions_Except_T")
QuantConnect_Util_LinqExtensions_IsNullOrEmpty_T = typing.TypeVar("QuantConnect_Util_LinqExtensions_IsNullOrEmpty_T")
QuantConnect_Util_LinqExtensions_Memoize_T = typing.TypeVar("QuantConnect_Util_LinqExtensions_Memoize_T")
QuantConnect_Util_LinqExtensions_GroupAdjacentBy_T = typing.TypeVar("QuantConnect_Util_LinqExtensions_GroupAdjacentBy_T")
QuantConnect_Util_LinqExtensions_AreDifferent_T = typing.TypeVar("QuantConnect_Util_LinqExtensions_AreDifferent_T")
QuantConnect_Util_LinqExtensions_AsEnumerable_T = typing.TypeVar("QuantConnect_Util_LinqExtensions_AsEnumerable_T")
QuantConnect_Util_LinqExtensions_DoForEach_T = typing.TypeVar("QuantConnect_Util_LinqExtensions_DoForEach_T")
QuantConnect_Util_XElementExtensions_Get_T = typing.TypeVar("QuantConnect_Util_XElementExtensions_Get_T")
QuantConnect_Util_CircularQueue_T = typing.TypeVar("QuantConnect_Util_CircularQueue_T")
QuantConnect_Util_ConcurrentSet_T = typing.TypeVar("QuantConnect_Util_ConcurrentSet_T")
QuantConnect_Util_IReadOnlyRef_T = typing.TypeVar("QuantConnect_Util_IReadOnlyRef_T")
QuantConnect_Util_Ref_T = typing.TypeVar("QuantConnect_Util_Ref_T")
QuantConnect_Util_Ref_Create_T = typing.TypeVar("QuantConnect_Util_Ref_Create_T")
QuantConnect_Util_Ref_CreateReadOnly_T = typing.TypeVar("QuantConnect_Util_Ref_CreateReadOnly_T")
QuantConnect_Util_SingleValueListConverter_T = typing.TypeVar("QuantConnect_Util_SingleValueListConverter_T")
QuantConnect_Util_ListComparer_T = typing.TypeVar("QuantConnect_Util_ListComparer_T")
QuantConnect_Util_FixedSizeHashQueue_T = typing.TypeVar("QuantConnect_Util_FixedSizeHashQueue_T")
QuantConnect_Util_PythonUtil_ToAction_T1 = typing.TypeVar("QuantConnect_Util_PythonUtil_ToAction_T1")
QuantConnect_Util_PythonUtil_ToAction_T2 = typing.TypeVar("QuantConnect_Util_PythonUtil_ToAction_T2")
QuantConnect_Util_PythonUtil_ToFunc_T1 = typing.TypeVar("QuantConnect_Util_PythonUtil_ToFunc_T1")
QuantConnect_Util_PythonUtil_ToFunc_T2 = typing.TypeVar("QuantConnect_Util_PythonUtil_ToFunc_T2")
QuantConnect_Util_BusyCollection_T = typing.TypeVar("QuantConnect_Util_BusyCollection_T")
QuantConnect_Util_ObjectActivator_Clone_T = typing.TypeVar("QuantConnect_Util_ObjectActivator_Clone_T")
QuantConnect_Util_ReferenceWrapper_T = typing.TypeVar("QuantConnect_Util_ReferenceWrapper_T")
QuantConnect_Util_ExpressionBuilder_Single_T = typing.TypeVar("QuantConnect_Util_ExpressionBuilder_Single_T")
QuantConnect_Util_ExpressionBuilder_OfType_T = typing.TypeVar("QuantConnect_Util_ExpressionBuilder_OfType_T")
QuantConnect_Util_Composer_Single_T = typing.TypeVar("QuantConnect_Util_Composer_Single_T")
QuantConnect_Util_Composer_AddPart_T = typing.TypeVar("QuantConnect_Util_Composer_AddPart_T")
QuantConnect_Util_Composer_GetPart_T = typing.TypeVar("QuantConnect_Util_Composer_GetPart_T")
QuantConnect_Util_Composer_GetExportedValueByTypeName_T = typing.TypeVar("QuantConnect_Util_Composer_GetExportedValueByTypeName_T")
QuantConnect_Util_Composer_GetExportedValues_T = typing.TypeVar("QuantConnect_Util_Composer_GetExportedValues_T")
QuantConnect_Util__EventContainer_Callable = typing.TypeVar("QuantConnect_Util__EventContainer_Callable")
QuantConnect_Util__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Util__EventContainer_ReturnType")


class BusyBlockingCollection(typing.Generic[QuantConnect_Util_BusyBlockingCollection_T], System.Object, QuantConnect.Interfaces.IBusyCollection[QuantConnect_Util_BusyBlockingCollection_T]):
    """
    A small wrapper around BlockingCollection{T} used to communicate busy state of the items
    being processed
    """

    @property
    def WaitHandle(self) -> System.Threading.WaitHandle:
        """
        Gets a wait handle that can be used to wait until this instance is done
        processing all of it's item
        """
        ...

    @property
    def Count(self) -> int:
        """Gets the number of items held within this collection"""
        ...

    @property
    def IsBusy(self) -> bool:
        """Returns true if processing, false otherwise"""
        ...

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the BusyBlockingCollection{T} class
        with a bounded capacity of int.MaxValue
        """
        ...

    @overload
    def __init__(self, boundedCapacity: int) -> None:
        """
        Initializes a new instance of the BusyBlockingCollection{T} class
        with the specified
        
        :param boundedCapacity: The maximum number of items allowed in the collection
        """
        ...

    @overload
    def Add(self, item: QuantConnect_Util_BusyBlockingCollection_T) -> None:
        """
        Adds the items to this collection
        
        :param item: The item to be added
        """
        ...

    @overload
    def Add(self, item: QuantConnect_Util_BusyBlockingCollection_T, cancellationToken: System.Threading.CancellationToken) -> None:
        """
        Adds the items to this collection
        
        :param item: The item to be added
        :param cancellationToken: A cancellation token to observer
        """
        ...

    def CompleteAdding(self) -> None:
        """Marks the BusyBlockingCollection{T} as not accepting any more additions"""
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    @overload
    def GetConsumingEnumerable(self) -> System.Collections.Generic.IEnumerable[QuantConnect_Util_BusyBlockingCollection_T]:
        """
        Provides a consuming enumerable for items in this collection.
        
        :returns: An enumerable that removes and returns items from the collection.
        """
        ...

    @overload
    def GetConsumingEnumerable(self, cancellationToken: System.Threading.CancellationToken) -> System.Collections.Generic.IEnumerable[QuantConnect_Util_BusyBlockingCollection_T]:
        """
        Provides a consuming enumerable for items in this collection.
        
        :param cancellationToken: A cancellation token to observer
        :returns: An enumerable that removes and returns items from the collection.
        """
        ...


class TypeChangeJsonConverter(typing.Generic[QuantConnect_Util_TypeChangeJsonConverter_T, QuantConnect_Util_TypeChangeJsonConverter_TResult], JsonConverter, metaclass=abc.ABCMeta):
    """
    Provides a base class for a JsonConverter that serializes a
    an input type as some other output type
    """

    @property
    def PopulateProperties(self) -> bool:
        """
        True will populate TResult object returned by Convert(TResult) with json properties
        
        This property is protected.
        """
        ...

    def CanConvert(self, objectType: typing.Type) -> bool:
        """
        Determines whether this instance can convert the specified object type.
        
        :param objectType: Type of the object.
        :returns: true if this instance can convert the specified object type; otherwise, false.
        """
        ...

    @overload
    def Convert(self, value: QuantConnect_Util_TypeChangeJsonConverter_T) -> QuantConnect_Util_TypeChangeJsonConverter_TResult:
        """
        Convert the input value to a value to be serialized
        
        This method is protected.
        
        :param value: The input value to be converted before serialziation
        :returns: A new instance of TResult that is to be serialzied.
        """
        ...

    @overload
    def Convert(self, value: QuantConnect_Util_TypeChangeJsonConverter_TResult) -> QuantConnect_Util_TypeChangeJsonConverter_T:
        """
        Converts the input value to be deserialized
        
        This method is protected.
        
        :param value: The deserialized value that needs to be converted to T
        :returns: The converted value.
        """
        ...

    def Create(self, type: typing.Type, token: typing.Any) -> QuantConnect_Util_TypeChangeJsonConverter_T:
        """
        Creates an instance of the un-projected type to be deserialized
        
        This method is protected.
        
        :param type: The input object type, this is the data held in the token
        :param token: The input data to be converted into a T
        :returns: A new instance of T that is to be serialized using default rules.
        """
        ...

    def ReadJson(self, reader: typing.Any, objectType: typing.Type, existingValue: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Reads the JSON representation of the object.
        
        :param reader: The Newtonsoft.Json.JsonReader to read from.
        :param objectType: Type of the object.
        :param existingValue: The existing value of object being read.
        :param serializer: The calling serializer.
        :returns: The object value.
        """
        ...

    def WriteJson(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """
        Writes the JSON representation of the object.
        
        :param writer: The Newtonsoft.Json.JsonWriter to write to.
        :param value: The value.
        :param serializer: The calling serializer.
        """
        ...


class FixedSizeQueue(typing.Generic[QuantConnect_Util_FixedSizeQueue_T], System.Collections.Generic.Queue[QuantConnect_Util_FixedSizeQueue_T]):
    """
    Helper method for a limited length queue which self-removes the extra elements.
    http://stackoverflow.com/questions/5852863/fixed-size-queue-which-automatically-dequeues-old-values-upon-new-enques
    """

    @property
    def Limit(self) -> int:
        """Max Length"""
        ...

    @Limit.setter
    def Limit(self, value: int):
        """Max Length"""
        ...

    def __init__(self, limit: int) -> None:
        """Create a new fixed length queue:"""
        ...

    def Enqueue(self, item: QuantConnect_Util_FixedSizeQueue_T) -> None:
        """Enqueue a new item int the generic fixed length queue:"""
        ...


class StreamReaderExtensions(System.Object):
    """Extension methods to fetch data from a StreamReader instance"""

    @staticmethod
    def GetDateTime(stream: System.IO.StreamReader, format: str = ..., delimiter: str = ...) -> datetime.datetime:
        """
        Gets a date time instance from a stream reader
        
        :param stream: The data stream
        :param format: The format in which the date time is
        :param delimiter: The data delimiter character to use, default is ','
        :returns: The date time instance read.
        """
        ...

    @staticmethod
    @overload
    def GetDecimal(stream: System.IO.StreamReader, delimiter: str = ...) -> float:
        """
        Gets a decimal from the provided stream reader
        
        :param stream: The data stream
        :param delimiter: The data delimiter character to use, default is ','
        :returns: The decimal read from the stream.
        """
        ...

    @staticmethod
    @overload
    def GetDecimal(stream: System.IO.StreamReader, pastEndLine: typing.Optional[bool], delimiter: str = ...) -> typing.Union[float, bool]:
        """
        Gets a decimal from the provided stream reader
        
        :param stream: The data stream
        :param pastEndLine: True if end line was past, useful for consumers to know a line ended
        :param delimiter: The data delimiter character to use, default is ','
        :returns: The decimal read from the stream.
        """
        ...

    @staticmethod
    def GetInt32(stream: System.IO.StreamReader, delimiter: str = ...) -> int:
        """
        Gets an integer from a stream reader
        
        :param stream: The data stream
        :param delimiter: The data delimiter character to use, default is ','
        :returns: The integer instance read.
        """
        ...

    @staticmethod
    def GetString(stream: System.IO.StreamReader, delimiter: str = ...) -> str:
        """
        Gets a string from a stream reader
        
        :param stream: The data stream
        :param delimiter: The data delimiter character to use, default is ','
        :returns: The string instance read.
        """
        ...


class JsonRoundingConverter(JsonConverter):
    """
    Helper JsonConverter that will round decimal and double types,
    to FractionalDigits fractional digits
    """

    FractionalDigits: int = 4
    """The number of fractional digits to round to"""

    @property
    def CanRead(self) -> bool:
        """
        Will always return false.
        Gets a value indicating whether this Newtonsoft.Json.JsonConverter can read JSON.
        """
        ...

    def CanConvert(self, objectType: typing.Type) -> bool:
        """
        Determines whether this instance can convert the specified object type.
        
        :param objectType: Type of the object.
        :returns: True if this instance can convert the specified object type.
        """
        ...

    def ReadJson(self, reader: typing.Any, objectType: typing.Type, existingValue: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Not implemented, will throw NotImplementedException
        
        :param reader: The Newtonsoft.Json.JsonReader to read from.
        :param objectType: Type of the object.
        :param existingValue: The existing value of object being read.
        :param serializer: The calling serializer.
        """
        ...

    def WriteJson(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """
        Writes the JSON representation of the object.
        
        :param writer: The Newtonsoft.Json.JsonWriter to write to.
        :param value: The value.
        :param serializer: The calling serializer.
        """
        ...


class ComparisonOperatorTypes(System.Enum):
    """Comparison operators"""

    Equals = 0
    """Check if their operands are equal"""

    NotEqual = 1
    """Check if their operands are not equal"""

    Greater = 2
    """Checks left-hand operand is greater than its right-hand operand"""

    GreaterOrEqual = 3
    """Checks left-hand operand is greater or equal to its right-hand operand"""

    Less = 4
    """Checks left-hand operand is less than its right-hand operand"""

    LessOrEqual = 5
    """Checks left-hand operand is less or equal to its right-hand operand"""


class ComparisonOperator(System.Object):
    """Utility Comparison Operator class"""

    @staticmethod
    def Compare(op: QuantConnect.Util.ComparisonOperatorTypes, arg1: QuantConnect_Util_ComparisonOperator_Compare_T, arg2: QuantConnect_Util_ComparisonOperator_Compare_T) -> bool:
        """
        Compares two values using given operator
        
        :param op: Comparison operator
        :param arg1: The first value
        :param arg2: The second value
        :returns: Returns true if its left-hand operand meets the operator value to its right-hand operand, false otherwise.
        """
        ...


class DateTimeJsonConverter(IsoDateTimeConverter):
    """Provides a json converter that allows defining the date time format used"""

    def __init__(self, format: str) -> None:
        """
        Initializes a new instance of the DateTimeJsonConverter class
        
        :param format: The date time format
        """
        ...


class ReaderWriterLockSlimExtensions(System.Object):
    """Provides extension methods to make working with the ReaderWriterLockSlim class easier"""

    @staticmethod
    def Read(readerWriterLockSlim: System.Threading.ReaderWriterLockSlim) -> System.IDisposable:
        """
        Opens the read lock
        
        :param readerWriterLockSlim: The lock to open for read
        :returns: A disposable reference which will release the lock upon disposal.
        """
        ...

    @staticmethod
    def Write(readerWriterLockSlim: System.Threading.ReaderWriterLockSlim) -> System.IDisposable:
        """
        Opens the write lock
        
        :param readerWriterLockSlim: The lock to open for write
        :returns: A disposale reference which will release thelock upon disposal.
        """
        ...


class NullStringValueConverter(typing.Generic[QuantConnect_Util_NullStringValueConverter_T], JsonConverter):
    """
    Converts the string "null" into a new instance of T.
    This converter only handles deserialization concerns.
    """

    def CanConvert(self, objectType: typing.Type) -> bool:
        """
        Determines whether this instance can convert the specified object type.
        
        :param objectType: Type of the object.
        :returns: true if this instance can convert the specified object type; otherwise, false.
        """
        ...

    def ReadJson(self, reader: typing.Any, objectType: typing.Type, existingValue: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Reads the JSON representation of the object.
        
        :param reader: The Newtonsoft.Json.JsonReader to read from.
        :param objectType: Type of the object.
        :param existingValue: The existing value of object being read.
        :param serializer: The calling serializer.
        :returns: The object value.
        """
        ...

    def WriteJson(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """
        Writes the JSON representation of the object.
        
        :param writer: The Newtonsoft.Json.JsonWriter to write to.
        :param value: The value.
        :param serializer: The calling serializer.
        """
        ...


class RateGate(System.Object, System.IDisposable):
    """Used to control the rate of some occurrence per unit of time."""

    @property
    def Occurrences(self) -> int:
        """Number of occurrences allowed per unit of time."""
        ...

    @Occurrences.setter
    def Occurrences(self, value: int):
        """Number of occurrences allowed per unit of time."""
        ...

    @property
    def TimeUnitMilliseconds(self) -> int:
        """The length of the time unit, in milliseconds."""
        ...

    @TimeUnitMilliseconds.setter
    def TimeUnitMilliseconds(self, value: int):
        """The length of the time unit, in milliseconds."""
        ...

    @property
    def IsRateLimited(self) -> bool:
        """Flag indicating we are currently being rate limited"""
        ...

    def __init__(self, occurrences: int, timeUnit: datetime.timedelta) -> None:
        """
        Initializes a RateGate with a rate of 
        per .
        
        :param occurrences: Number of occurrences allowed per unit of time.
        :param timeUnit: Length of the time unit.
        """
        ...

    @overload
    def Dispose(self) -> None:
        """Releases unmanaged resources held by an instance of this class."""
        ...

    @overload
    def Dispose(self, isDisposing: bool) -> None:
        """
        Releases unmanaged resources held by an instance of this class.
        
        This method is protected.
        
        :param isDisposing: Whether this object is being disposed.
        """
        ...

    @overload
    def WaitToProceed(self, millisecondsTimeout: int) -> bool:
        """
        Blocks the current thread until allowed to proceed or until the
        specified timeout elapses.
        
        :param millisecondsTimeout: Number of milliseconds to wait, or -1 to wait indefinitely.
        :returns: true if the thread is allowed to proceed, or false if timed out.
        """
        ...

    @overload
    def WaitToProceed(self, timeout: datetime.timedelta) -> bool:
        """
        Blocks the current thread until allowed to proceed or until the
        specified timeout elapses.
        
        :returns: true if the thread is allowed to proceed, or false if timed out.
        """
        ...

    @overload
    def WaitToProceed(self) -> None:
        """Blocks the current thread indefinitely until allowed to proceed."""
        ...


class EnumeratorExtensions(System.Object):
    """Provides convenience of linq extension methods for IEnumerator{T} types"""

    @staticmethod
    def Select(enumerator: System.Collections.Generic.IEnumerator[QuantConnect_Util_EnumeratorExtensions_Select_T], selector: typing.Callable[[QuantConnect_Util_EnumeratorExtensions_Select_T], QuantConnect_Util_EnumeratorExtensions_Select_TResult]) -> System.Collections.Generic.IEnumerator[QuantConnect_Util_EnumeratorExtensions_Select_TResult]:
        """Project the enumerator using the specified selector"""
        ...

    @staticmethod
    def SelectMany(enumerator: System.Collections.Generic.IEnumerator[QuantConnect_Util_EnumeratorExtensions_SelectMany_T], selector: typing.Callable[[QuantConnect_Util_EnumeratorExtensions_SelectMany_T], System.Collections.Generic.IEnumerator[QuantConnect_Util_EnumeratorExtensions_SelectMany_TResult]]) -> System.Collections.Generic.IEnumerator[QuantConnect_Util_EnumeratorExtensions_SelectMany_TResult]:
        """Project the enumerator using the specified selector"""
        ...

    @staticmethod
    def Where(enumerator: System.Collections.Generic.IEnumerator[QuantConnect_Util_EnumeratorExtensions_Where_T], predicate: typing.Callable[[QuantConnect_Util_EnumeratorExtensions_Where_T], bool]) -> System.Collections.Generic.IEnumerator[QuantConnect_Util_EnumeratorExtensions_Where_T]:
        """Filter the enumerator using the specified predicate"""
        ...


class StringDecimalJsonConverter(QuantConnect.Util.TypeChangeJsonConverter[float, str]):
    """Allows for conversion of string numeric values from JSON to the decimal type"""

    def __init__(self, defaultOnFailure: bool = False) -> None:
        """
        Creates an instance of the class, with an optional flag to default to decimal's default value on failure.
        
        :param defaultOnFailure: Default to decimal's default value on failure
        """
        ...

    @overload
    def Convert(self, value: float) -> str:
        """
        Converts a decimal to a string
        
        This method is protected.
        
        :param value: The input value to be converted before serialization
        :returns: String representation of the decimal.
        """
        ...

    @overload
    def Convert(self, value: str) -> float:
        """
        Converts the input string to a decimal
        
        This method is protected.
        
        :param value: The deserialized value that needs to be converted to T
        :returns: The converted value.
        """
        ...


class MemoizingEnumerable(typing.Generic[QuantConnect_Util_MemoizingEnumerable_T], System.Object, typing.Iterable[QuantConnect_Util_MemoizingEnumerable_T]):
    """
    Defines an enumerable that can be enumerated many times while
    only performing a single enumeration of the root enumerable
    """

    @property
    def Enabled(self) -> bool:
        """Allow disableing the buffering"""
        ...

    @Enabled.setter
    def Enabled(self, value: bool):
        """Allow disableing the buffering"""
        ...

    def __init__(self, enumerable: System.Collections.Generic.IEnumerable[QuantConnect_Util_MemoizingEnumerable_T]) -> None:
        """
        Initializes a new instance of the MemoizingEnumerable{T} class
        
        :param enumerable: The source enumerable to be memoized
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect_Util_MemoizingEnumerable_T]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: A System.Collections.Generic.IEnumerator`1 that can be used to iterate through the collection.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        """
        Returns an enumerator that iterates through a collection.
        
        :returns: An System.Collections.IEnumerator object that can be used to iterate through the collection.
        """
        ...


class LinqExtensions(System.Object):
    """Provides more extension methods for the enumerable types"""

    @staticmethod
    def AreDifferent(left: System.Collections.Generic.ISet[QuantConnect_Util_LinqExtensions_AreDifferent_T], right: System.Collections.Generic.ISet[QuantConnect_Util_LinqExtensions_AreDifferent_T]) -> bool:
        """
        Determines if there are any differences between the left and right collections.
        This method uses sets to improve performance and also uses lazy evaluation so if a
        difference is found, true is immediately returned and evaluation is halted.
        
        :param left: The left set
        :param right: The right set
        :returns: True if there are any differences between the two sets, false otherwise.
        """
        ...

    @staticmethod
    def AsEnumerable(enumerator: System.Collections.Generic.IEnumerator[QuantConnect_Util_LinqExtensions_AsEnumerable_T]) -> System.Collections.Generic.IEnumerable[QuantConnect_Util_LinqExtensions_AsEnumerable_T]:
        """
        Converts an IEnumerator{T} to an IEnumerable{T}
        
        :param enumerator: The enumerator to convert to an enumerable
        :returns: An enumerable wrapping the specified enumerator.
        """
        ...

    @staticmethod
    @overload
    def BinarySearch(list: System.Collections.Generic.IList[QuantConnect_Util_LinqExtensions_BinarySearch_TItem], value: QuantConnect_Util_LinqExtensions_BinarySearch_TSearch, comparer: typing.Callable[[QuantConnect_Util_LinqExtensions_BinarySearch_TSearch, QuantConnect_Util_LinqExtensions_BinarySearch_TItem], int]) -> int:
        """
        Performs a binary search on the specified collection.
        
        :param list: The list to be searched.
        :param value: The value to search for.
        :param comparer: The comparer that is used to compare the value with the list items.
        :returns: The index of the item if found, otherwise the bitwise complement where the value should be per MSDN specs.
        """
        ...

    @staticmethod
    @overload
    def BinarySearch(list: System.Collections.Generic.IList[QuantConnect_Util_LinqExtensions_BinarySearch_TItem], value: QuantConnect_Util_LinqExtensions_BinarySearch_TItem) -> int:
        """
        Performs a binary search on the specified collection.
        
        :param list: The list to be searched.
        :param value: The value to search for.
        :returns: The index of the item if found, otherwise the bitwise complement where the value should be per MSDN specs.
        """
        ...

    @staticmethod
    @overload
    def BinarySearch(list: System.Collections.Generic.IList[QuantConnect_Util_LinqExtensions_BinarySearch_TItem], value: QuantConnect_Util_LinqExtensions_BinarySearch_TItem, comparer: System.Collections.Generic.IComparer[QuantConnect_Util_LinqExtensions_BinarySearch_TItem]) -> int:
        """
        Performs a binary search on the specified collection.
        
        :param list: The list to be searched.
        :param value: The value to search for.
        :param comparer: The comparer that is used to compare the value with the list items.
        :returns: The index of the item if found, otherwise the bitwise complement where the value should be per MSDN specs.
        """
        ...

    @staticmethod
    def DoForEach(source: System.Collections.Generic.IEnumerable[QuantConnect_Util_LinqExtensions_DoForEach_T], action: typing.Callable[[QuantConnect_Util_LinqExtensions_DoForEach_T], None]) -> None:
        """
        Performs an action for each element in collection source
        
        :param source: Collection source
        :param action: An action to perform
        """
        ...

    @staticmethod
    def Except(enumerable: System.Collections.Generic.IEnumerable[QuantConnect_Util_LinqExtensions_Except_T], set: System.Collections.Generic.ISet[QuantConnect_Util_LinqExtensions_Except_T]) -> System.Collections.Generic.IEnumerable[QuantConnect_Util_LinqExtensions_Except_T]:
        """
        Produces the set difference of two sequences by using the default equality comparer to compare values.
        
        :param enumerable: An System.Collections.Generic.IEnumerable`1 whose elements that are not also in  will be returned.
        :param set: An System.Collections.Generic.IEnumerable`1 whose elements that also occur in the first sequence will cause those elements to be removed from the returned sequence.
        :returns: A sequence that contains the set difference of the elements of two sequences.
        """
        ...

    @staticmethod
    def GetValueOrDefault(dictionary: System.Collections.Generic.IDictionary[QuantConnect_Util_LinqExtensions_GetValueOrDefault_K, QuantConnect_Util_LinqExtensions_GetValueOrDefault_V], key: QuantConnect_Util_LinqExtensions_GetValueOrDefault_K, defaultValue: QuantConnect_Util_LinqExtensions_GetValueOrDefault_V = ...) -> QuantConnect_Util_LinqExtensions_GetValueOrDefault_V:
        """
        Gets the value associated with the specified key or provided default value if key is not found.
        
        :param dictionary: The dictionary instance
        :param key: Lookup key
        :param defaultValue: Default value
        :returns: Value associated with the specified key or  default value.
        """
        ...

    @staticmethod
    def GroupAdjacentBy(enumerable: System.Collections.Generic.IEnumerable[QuantConnect_Util_LinqExtensions_GroupAdjacentBy_T], grouper: typing.Callable[[QuantConnect_Util_LinqExtensions_GroupAdjacentBy_T, QuantConnect_Util_LinqExtensions_GroupAdjacentBy_T], bool]) -> System.Collections.Generic.IEnumerable[System.Collections.Generic.IEnumerable[QuantConnect_Util_LinqExtensions_GroupAdjacentBy_T]]:
        """
        Groups adjacent elements of the enumerale using the specified grouper function
        
        :param enumerable: The source enumerable to be grouped
        :param grouper: A function that accepts the previous value and the next value and returns true if the next value belongs in the same group as the previous value, otherwise returns false
        :returns: A new enumerable of the groups defined by grouper. These groups don't have a key and are only grouped by being emitted separately from this enumerable.
        """
        ...

    @staticmethod
    def IsNullOrEmpty(enumerable: System.Collections.Generic.IEnumerable[QuantConnect_Util_LinqExtensions_IsNullOrEmpty_T]) -> bool:
        """
        Returns true if the specified enumerable is null or has no elements
        
        :param enumerable: The enumerable to check for a value
        :returns: True if the enumerable has elements, false otherwise.
        """
        ...

    @staticmethod
    @overload
    def Median(enumerable: System.Collections.Generic.IEnumerable[QuantConnect_Util_LinqExtensions_Median_T]) -> QuantConnect_Util_LinqExtensions_Median_T:
        """
        Gets the median value in the collection
        
        :param enumerable: The enumerable of items to search
        :returns: The median value, throws InvalidOperationException if no items are present.
        """
        ...

    @staticmethod
    @overload
    def Median(collection: System.Collections.Generic.IEnumerable[QuantConnect_Util_LinqExtensions_Median_T], selector: typing.Callable[[QuantConnect_Util_LinqExtensions_Median_T], QuantConnect_Util_LinqExtensions_Median_TProperty]) -> QuantConnect_Util_LinqExtensions_Median_TProperty:
        """
        Gets the median value in the collection
        
        :param collection: The collection of items to search
        :param selector: Function used to select a value from collection items
        :returns: The median value, throws InvalidOperationException if no items are present.
        """
        ...

    @staticmethod
    def Memoize(enumerable: System.Collections.Generic.IEnumerable[QuantConnect_Util_LinqExtensions_Memoize_T]) -> System.Collections.Generic.IEnumerable[QuantConnect_Util_LinqExtensions_Memoize_T]:
        """
        Wraps the specified enumerable such that it will only be enumerated once
        
        :param enumerable: The source enumerable to be wrapped
        :returns: A new enumerable that can be enumerated multiple times without re-enumerating the source enumerable.
        """
        ...

    @staticmethod
    def Range(start: QuantConnect_Util_LinqExtensions_Range_T, end: QuantConnect_Util_LinqExtensions_Range_T, incrementer: typing.Callable[[QuantConnect_Util_LinqExtensions_Range_T], QuantConnect_Util_LinqExtensions_Range_T], includeEndPoint: bool = False) -> System.Collections.Generic.IEnumerable[QuantConnect_Util_LinqExtensions_Range_T]:
        """
        Produces the an enumerable of the range of values between start and end using the specified
        incrementing function
        
        :param start: The start of the range
        :param end: The end of the range, non-inclusive by default
        :param incrementer: The incrementing function, with argument of the current item
        :param includeEndPoint: True to emit the end point, false otherwise
        :returns: An enumerable of the range of items between start and end.
        """
        ...

    @staticmethod
    def ToArray(enumerable: System.Collections.Generic.IEnumerable[QuantConnect_Util_LinqExtensions_ToArray_T], selector: typing.Callable[[QuantConnect_Util_LinqExtensions_ToArray_T], QuantConnect_Util_LinqExtensions_ToArray_TResult]) -> typing.List[QuantConnect_Util_LinqExtensions_ToArray_TResult]:
        """
        Creates a new array from the projected elements in the specified enumerable
        
        :param enumerable: The items to be placed into the array
        :param selector: Selects items from the enumerable to be placed into the array
        :returns: A new array containing the items in the enumerable.
        """
        ...

    @staticmethod
    def ToDictionary(enumerable: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[QuantConnect_Util_LinqExtensions_ToDictionary_K, QuantConnect_Util_LinqExtensions_ToDictionary_V]]) -> System.Collections.Generic.Dictionary[QuantConnect_Util_LinqExtensions_ToDictionary_K, QuantConnect_Util_LinqExtensions_ToDictionary_V]:
        """
        Creates a dictionary enumerable of key value pairs
        
        :param enumerable: The IEnumerable of KeyValuePair instances to convert to a dictionary
        :returns: A dictionary holding the same data as the enumerable.
        """
        ...

    @staticmethod
    def ToHashSet(enumerable: System.Collections.Generic.IEnumerable[QuantConnect_Util_LinqExtensions_ToHashSet_T], selector: typing.Callable[[QuantConnect_Util_LinqExtensions_ToHashSet_T], QuantConnect_Util_LinqExtensions_ToHashSet_TResult]) -> System.Collections.Generic.HashSet[QuantConnect_Util_LinqExtensions_ToHashSet_TResult]:
        """
        Creates a new HashSet{T} from the elements in the specified enumerable
        
        :param enumerable: The items to be placed into the enumerable
        :param selector: Selects items from the enumerable to be placed into the HashSet{T}
        :returns: A new HashSet{T} containing the items in the enumerable.
        """
        ...

    @staticmethod
    def ToImmutableArray(enumerable: System.Collections.Generic.IEnumerable[QuantConnect_Util_LinqExtensions_ToImmutableArray_T], selector: typing.Callable[[QuantConnect_Util_LinqExtensions_ToImmutableArray_T], QuantConnect_Util_LinqExtensions_ToImmutableArray_TResult]) -> System.Collections.Immutable.ImmutableArray[QuantConnect_Util_LinqExtensions_ToImmutableArray_TResult]:
        """
        Creates a new immutable array from the projected elements in the specified enumerable
        
        :param enumerable: The items to be placed into the array
        :param selector: Selects items from the enumerable to be placed into the array
        :returns: A new array containing the items in the enumerable.
        """
        ...

    @staticmethod
    def ToList(enumerable: System.Collections.Generic.IEnumerable[QuantConnect_Util_LinqExtensions_ToList_T], selector: typing.Callable[[QuantConnect_Util_LinqExtensions_ToList_T], QuantConnect_Util_LinqExtensions_ToList_TResult]) -> System.Collections.Generic.List[QuantConnect_Util_LinqExtensions_ToList_TResult]:
        """
        Creates a new IList{T} from the projected elements in the specified enumerable
        
        :param enumerable: The items to be placed into the list
        :param selector: Selects items from the enumerable to be placed into the List{T}
        :returns: A new List{T} containing the items in the enumerable.
        """
        ...

    @staticmethod
    def ToReadOnlyDictionary(enumerable: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[QuantConnect_Util_LinqExtensions_ToReadOnlyDictionary_K, QuantConnect_Util_LinqExtensions_ToReadOnlyDictionary_V]]) -> System.Collections.Generic.IReadOnlyDictionary[QuantConnect_Util_LinqExtensions_ToReadOnlyDictionary_K, QuantConnect_Util_LinqExtensions_ToReadOnlyDictionary_V]:
        """
        Creates a new read-only dictionary from the key value pairs
        
        :param enumerable: The IEnumerable of KeyValuePair instances to convert to a dictionary
        :returns: A read-only dictionary holding the same data as the enumerable.
        """
        ...


class XElementExtensions(System.Object):
    """Provides extension methods for the XML to LINQ types"""

    @staticmethod
    def Get(element: typing.Any, name: str) -> QuantConnect_Util_XElementExtensions_Get_T:
        """
        Gets the value from the element and converts it to the specified type.
        
        :param element: The element to access
        :param name: The attribute name to access on the element
        :returns: The converted value.
        """
        ...


class CircularQueue(typing.Generic[QuantConnect_Util_CircularQueue_T], System.Object):
    """A never ending queue that will dequeue and reenqueue the same item"""

    @property
    def CircleCompleted(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Fired when we do a full circle"""
        ...

    @CircleCompleted.setter
    def CircleCompleted(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]):
        """Fired when we do a full circle"""
        ...

    @overload
    def __init__(self, *items: QuantConnect_Util_CircularQueue_T) -> None:
        """
        Initializes a new instance of the CircularQueue{T} class
        
        :param items: The items in the queue
        """
        ...

    @overload
    def __init__(self, items: System.Collections.Generic.IEnumerable[QuantConnect_Util_CircularQueue_T]) -> None:
        """
        Initializes a new instance of the CircularQueue{T} class
        
        :param items: The items in the queue
        """
        ...

    def Dequeue(self) -> QuantConnect_Util_CircularQueue_T:
        """
        Dequeues the next item
        
        :returns: The next item.
        """
        ...

    def OnCircleCompleted(self) -> None:
        """
        Event invocator for the CircleCompleted evet
        
        This method is protected.
        """
        ...


class Validate(System.Object):
    """Provides methods for validating strings following a certain format, such as an email address"""

    class RegularExpression(System.Object):
        """Provides static storage of compiled regular expressions to preclude parsing on each invocation"""

        EmailDomainName: System.Text.RegularExpressions.Regex = ...
        """
        Matches the domain name in an email address ignored@[domain.com]
        Pattern sourced via msdn:
        https://docs.microsoft.com/en-us/dotnet/standard/base-types/how-to-verify-that-strings-are-in-valid-email-format
        """

        Email: System.Text.RegularExpressions.Regex = ...
        """
        Matches a valid email address address@sub.domain.com
        Pattern sourced via msdn:
        https://docs.microsoft.com/en-us/dotnet/standard/base-types/how-to-verify-that-strings-are-in-valid-email-format
        """

    @staticmethod
    def EmailAddress(emailAddress: str) -> bool:
        """
        Validates the provided email address
        
        :param emailAddress: The email address to be validated
        :returns: True if the provided email address is valid.
        """
        ...


class ConcurrentSet(typing.Generic[QuantConnect_Util_ConcurrentSet_T], System.Object, System.Collections.Generic.ISet[QuantConnect_Util_ConcurrentSet_T], typing.Iterable[QuantConnect_Util_ConcurrentSet_T]):
    """
    Provides a thread-safe set collection that mimics the behavior of HashSet{T}
    and will be keep insertion order
    """

    @property
    def Count(self) -> int:
        """Gets the number of elements contained in the System.Collections.Generic.ICollection`1."""
        ...

    @property
    def IsReadOnly(self) -> bool:
        """Gets a value indicating whether the System.Collections.Generic.ICollection`1 is read-only."""
        ...

    @overload
    def Add(self, item: QuantConnect_Util_ConcurrentSet_T) -> None:
        """
        Adds an item to the System.Collections.Generic.ICollection`1.
        
        :param item: The object to add to the System.Collections.Generic.ICollection`1.
        """
        ...

    @overload
    def Add(self, item: QuantConnect_Util_ConcurrentSet_T) -> bool:
        """
        Adds an element to the current set and returns a value to indicate if the element was successfully added.
        
        :param item: The element to add to the set.
        :returns: true if the element is added to the set; false if the element is already in the set.
        """
        ...

    def Clear(self) -> None:
        """Removes all items from the System.Collections.Generic.ICollection`1."""
        ...

    def Contains(self, item: QuantConnect_Util_ConcurrentSet_T) -> bool:
        """
        Determines whether the System.Collections.Generic.ICollection`1 contains a specific value.
        
        :param item: The object to locate in the System.Collections.Generic.ICollection`1.
        :returns: true if  is found in the System.Collections.Generic.ICollection`1; otherwise, false.
        """
        ...

    def CopyTo(self, array: typing.List[QuantConnect_Util_ConcurrentSet_T], arrayIndex: int) -> None:
        """
        Copies the elements of the System.Collections.Generic.ICollection`1 to an System.Array, starting at a particular System.Array index.
        
        :param array: The one-dimensional System.Array that is the destination of the elements copied from System.Collections.Generic.ICollection`1. The System.Array must have zero-based indexing.
        :param arrayIndex: The zero-based index in  at which copying begins.
        """
        ...

    def ExceptWith(self, other: System.Collections.Generic.IEnumerable[QuantConnect_Util_ConcurrentSet_T]) -> None:
        """
        Removes all elements in the specified collection from the current set.
        
        :param other: The collection of items to remove from the set.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect_Util_ConcurrentSet_T]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: A System.Collections.Generic.IEnumerator`1 that can be used to iterate through the collection.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        """
        Returns an enumerator that iterates through a collection.
        
        :returns: An System.Collections.IEnumerator object that can be used to iterate through the collection.
        """
        ...

    def IntersectWith(self, other: System.Collections.Generic.IEnumerable[QuantConnect_Util_ConcurrentSet_T]) -> None:
        """
        Modifies the current set so that it contains only elements that are also in a specified collection.
        
        :param other: The collection to compare to the current set.
        """
        ...

    def IsProperSubsetOf(self, other: System.Collections.Generic.IEnumerable[QuantConnect_Util_ConcurrentSet_T]) -> bool:
        """
        Determines whether the current set is a proper (strict) subset of a specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set is a proper subset of ; otherwise, false.
        """
        ...

    def IsProperSupersetOf(self, other: System.Collections.Generic.IEnumerable[QuantConnect_Util_ConcurrentSet_T]) -> bool:
        """
        Determines whether the current set is a proper (strict) superset of a specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set is a proper superset of ; otherwise, false.
        """
        ...

    def IsSubsetOf(self, other: System.Collections.Generic.IEnumerable[QuantConnect_Util_ConcurrentSet_T]) -> bool:
        """
        Determines whether a set is a subset of a specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set is a subset of ; otherwise, false.
        """
        ...

    def IsSupersetOf(self, other: System.Collections.Generic.IEnumerable[QuantConnect_Util_ConcurrentSet_T]) -> bool:
        """
        Determines whether the current set is a superset of a specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set is a superset of ; otherwise, false.
        """
        ...

    def Overlaps(self, other: System.Collections.Generic.IEnumerable[QuantConnect_Util_ConcurrentSet_T]) -> bool:
        """
        Determines whether the current set overlaps with the specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set and  share at least one common element; otherwise, false.
        """
        ...

    def Remove(self, item: QuantConnect_Util_ConcurrentSet_T) -> bool:
        """
        Removes the first occurrence of a specific object from the System.Collections.Generic.ICollection`1.
        
        :param item: The object to remove from the System.Collections.Generic.ICollection`1.
        :returns: true if  was successfully removed from the System.Collections.Generic.ICollection`1; otherwise, false. This method also returns false if  is not found in the original System.Collections.Generic.ICollection`1.
        """
        ...

    def SetEquals(self, other: System.Collections.Generic.IEnumerable[QuantConnect_Util_ConcurrentSet_T]) -> bool:
        """
        Determines whether the current set and the specified collection contain the same elements.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set is equal to ; otherwise, false.
        """
        ...

    def SymmetricExceptWith(self, other: System.Collections.Generic.IEnumerable[QuantConnect_Util_ConcurrentSet_T]) -> None:
        """
        Modifies the current set so that it contains only elements that are present either in the current set or in the specified collection, but not both.
        
        :param other: The collection to compare to the current set.
        """
        ...

    def UnionWith(self, other: System.Collections.Generic.IEnumerable[QuantConnect_Util_ConcurrentSet_T]) -> None:
        """
        Modifies the current set so that it contains all elements that are present in either the current set or the specified collection.
        
        :param other: The collection to compare to the current set.
        """
        ...


class MarketHoursDatabaseJsonConverter(QuantConnect.Util.TypeChangeJsonConverter[QuantConnect.Securities.MarketHoursDatabase, QuantConnect_Util_MarketHoursDatabaseJsonConverter_MarketHoursDatabaseJson]):
    """Provides json conversion for the MarketHoursDatabase class"""

    class MarketHoursDatabaseJson(System.Object):
        """Defines the json structure of the market-hours-database.json file"""

        @property
        def Entries(self) -> System.Collections.Generic.Dictionary[str, QuantConnect.Util.MarketHoursDatabaseJsonConverter.MarketHoursDatabaseEntryJson]:
            """The entries in the market hours database, keyed by SecurityDatabaseKey"""
            ...

        @Entries.setter
        def Entries(self, value: System.Collections.Generic.Dictionary[str, QuantConnect.Util.MarketHoursDatabaseJsonConverter.MarketHoursDatabaseEntryJson]):
            """The entries in the market hours database, keyed by SecurityDatabaseKey"""
            ...

        def __init__(self, database: QuantConnect.Securities.MarketHoursDatabase) -> None:
            """
            Initializes a new instance of the MarketHoursDatabaseJson class
            
            :param database: The database instance to copy
            """
            ...

        def Convert(self) -> QuantConnect.Securities.MarketHoursDatabase:
            """
            Converts this json representation to the MarketHoursDatabase type
            
            :returns: A new instance of the MarketHoursDatabase class.
            """
            ...

    class MarketHoursDatabaseEntryJson(System.Object):
        """Defines the json structure of a single entry in the market-hours-database.json file"""

        @property
        def DataTimeZone(self) -> str:
            """The data's raw time zone"""
            ...

        @DataTimeZone.setter
        def DataTimeZone(self, value: str):
            """The data's raw time zone"""
            ...

        @property
        def ExchangeTimeZone(self) -> str:
            """The exchange's time zone id from the tzdb"""
            ...

        @ExchangeTimeZone.setter
        def ExchangeTimeZone(self, value: str):
            """The exchange's time zone id from the tzdb"""
            ...

        @property
        def Sunday(self) -> System.Collections.Generic.List[QuantConnect.Securities.MarketHoursSegment]:
            """Sunday market hours segments"""
            ...

        @Sunday.setter
        def Sunday(self, value: System.Collections.Generic.List[QuantConnect.Securities.MarketHoursSegment]):
            """Sunday market hours segments"""
            ...

        @property
        def Monday(self) -> System.Collections.Generic.List[QuantConnect.Securities.MarketHoursSegment]:
            """Monday market hours segments"""
            ...

        @Monday.setter
        def Monday(self, value: System.Collections.Generic.List[QuantConnect.Securities.MarketHoursSegment]):
            """Monday market hours segments"""
            ...

        @property
        def Tuesday(self) -> System.Collections.Generic.List[QuantConnect.Securities.MarketHoursSegment]:
            """Tuesday market hours segments"""
            ...

        @Tuesday.setter
        def Tuesday(self, value: System.Collections.Generic.List[QuantConnect.Securities.MarketHoursSegment]):
            """Tuesday market hours segments"""
            ...

        @property
        def Wednesday(self) -> System.Collections.Generic.List[QuantConnect.Securities.MarketHoursSegment]:
            """Wednesday market hours segments"""
            ...

        @Wednesday.setter
        def Wednesday(self, value: System.Collections.Generic.List[QuantConnect.Securities.MarketHoursSegment]):
            """Wednesday market hours segments"""
            ...

        @property
        def Thursday(self) -> System.Collections.Generic.List[QuantConnect.Securities.MarketHoursSegment]:
            """Thursday market hours segments"""
            ...

        @Thursday.setter
        def Thursday(self, value: System.Collections.Generic.List[QuantConnect.Securities.MarketHoursSegment]):
            """Thursday market hours segments"""
            ...

        @property
        def Friday(self) -> System.Collections.Generic.List[QuantConnect.Securities.MarketHoursSegment]:
            """Friday market hours segments"""
            ...

        @Friday.setter
        def Friday(self, value: System.Collections.Generic.List[QuantConnect.Securities.MarketHoursSegment]):
            """Friday market hours segments"""
            ...

        @property
        def Saturday(self) -> System.Collections.Generic.List[QuantConnect.Securities.MarketHoursSegment]:
            """Saturday market hours segments"""
            ...

        @Saturday.setter
        def Saturday(self, value: System.Collections.Generic.List[QuantConnect.Securities.MarketHoursSegment]):
            """Saturday market hours segments"""
            ...

        @property
        def Holidays(self) -> System.Collections.Generic.List[str]:
            """Holiday date strings"""
            ...

        @Holidays.setter
        def Holidays(self, value: System.Collections.Generic.List[str]):
            """Holiday date strings"""
            ...

        @property
        def EarlyCloses(self) -> System.Collections.Generic.Dictionary[str, datetime.timedelta]:
            """Early closes by date"""
            ...

        @EarlyCloses.setter
        def EarlyCloses(self, value: System.Collections.Generic.Dictionary[str, datetime.timedelta]):
            """Early closes by date"""
            ...

        @property
        def LateOpens(self) -> System.Collections.Generic.Dictionary[str, datetime.timedelta]:
            """Late opens by date"""
            ...

        @LateOpens.setter
        def LateOpens(self, value: System.Collections.Generic.Dictionary[str, datetime.timedelta]):
            """Late opens by date"""
            ...

        def __init__(self, entry: QuantConnect.Securities.MarketHoursDatabase.Entry) -> None:
            """
            Initializes a new instance of the MarketHoursDatabaseEntryJson class
            
            :param entry: The entry instance to copy
            """
            ...

        def Convert(self) -> QuantConnect.Securities.MarketHoursDatabase.Entry:
            """
            Converts this json representation to the MarketHoursDatabase.Entry type
            
            :returns: A new instance of the MarketHoursDatabase.Entry class.
            """
            ...

    @overload
    def Convert(self, value: QuantConnect.Securities.MarketHoursDatabase) -> QuantConnect.Util.MarketHoursDatabaseJsonConverter.MarketHoursDatabaseJson:
        """
        Convert the input value to a value to be serialzied
        
        This method is protected.
        
        :param value: The input value to be converted before serialziation
        :returns: A new instance of TResult that is to be serialzied.
        """
        ...

    @overload
    def Convert(self, value: QuantConnect.Util.MarketHoursDatabaseJsonConverter.MarketHoursDatabaseJson) -> QuantConnect.Securities.MarketHoursDatabase:
        """
        Converts the input value to be deserialized
        
        This method is protected.
        
        :param value: The deserialized value that needs to be converted to T
        :returns: The converted value.
        """
        ...

    def Create(self, type: typing.Type, token: typing.Any) -> QuantConnect.Securities.MarketHoursDatabase:
        """
        Creates an instance of the un-projected type to be deserialized
        
        This method is protected.
        
        :param type: The input object type, this is the data held in the token
        :param token: The input data to be converted into a T
        :returns: A new instance of T that is to be serialized using default rules.
        """
        ...


class FuncTextWriter(System.IO.TextWriter):
    """Provides an implementation of TextWriter that redirects Write(string) and WriteLine(string)"""

    @property
    def Encoding(self) -> System.Text.Encoding:
        ...

    def __init__(self, writer: typing.Callable[[str], None]) -> None:
        """
        Initializes a new instance of the FuncTextWriter that will direct
        messages to the algorithm's Debug function.
        
        :param writer: The algorithm hosting the Debug function where messages will be directed
        """
        ...

    def Write(self, value: str) -> None:
        """
        Writes the string value using the delegate provided at construction
        
        :param value: The string value to be written
        """
        ...

    def WriteLine(self, value: str) -> None:
        """Writes the string value using the delegate provided at construction"""
        ...


class StreamReaderEnumerable(System.Object, System.IDisposable, typing.Iterable[str]):
    """Converts a StreamReader into an enumerable of string"""

    @overload
    def __init__(self, stream: System.IO.Stream, *disposables: System.IDisposable) -> None:
        """
        Initializes a new instance of the StreamReaderEnumerable class
        
        :param stream: The stream to be read
        :param disposables: Allows specifying other resources that should be disposed when this instance is disposed
        """
        ...

    @overload
    def __init__(self, reader: System.IO.StreamReader, *disposables: System.IDisposable) -> None:
        """
        Initializes a new instance of the StreamReaderEnumerable class
        
        :param reader: The stream reader instance to convert to an enumerable of string
        :param disposables: Allows specifying other resources that should be disposed when this instance is disposed
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[str]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: A System.Collections.Generic.IEnumerator`1 that can be used to iterate through the collection.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        """
        Returns an enumerator that iterates through a collection.
        
        :returns: An System.Collections.IEnumerator object that can be used to iterate through the collection.
        """
        ...


class IReadOnlyRef(typing.Generic[QuantConnect_Util_IReadOnlyRef_T], metaclass=abc.ABCMeta):
    """Represents a read-only reference to any value, T"""

    @property
    @abc.abstractmethod
    def Value(self) -> QuantConnect_Util_IReadOnlyRef_T:
        """Gets the current value this reference points to"""
        ...


class Ref(typing.Generic[QuantConnect_Util_Ref_T], System.Object, QuantConnect.Util.IReadOnlyRef[QuantConnect_Util_Ref_T]):
    """Represents a reference to any value, T"""

    @property
    def Value(self) -> QuantConnect_Util_Ref_T:
        """Gets or sets the value of this reference"""
        ...

    @Value.setter
    def Value(self, value: QuantConnect_Util_Ref_T):
        """Gets or sets the value of this reference"""
        ...

    def __init__(self, getter: typing.Callable[[], QuantConnect_Util_Ref_T], setter: typing.Callable[[QuantConnect_Util_Ref_T], None]) -> None:
        """
        Initializes a new instance of the Ref{T} class
        
        :param getter: A function delegate to get the current value
        :param setter: A function delegate to set the current value
        """
        ...

    def AsReadOnly(self) -> QuantConnect.Util.IReadOnlyRef[QuantConnect_Util_Ref_T]:
        """
        Returns a read-only version of this instance
        
        :returns: A new instance with read-only semantics/gaurantees.
        """
        ...

    @staticmethod
    @overload
    def Create(getter: typing.Callable[[], QuantConnect_Util_Ref_Create_T], setter: typing.Callable[[QuantConnect_Util_Ref_Create_T], None]) -> QuantConnect.Util.Ref[QuantConnect_Util_Ref_Create_T]:
        """Creates a new Ref{T} instance"""
        ...

    @staticmethod
    @overload
    def Create(initialValue: QuantConnect_Util_Ref_Create_T) -> QuantConnect.Util.Ref[QuantConnect_Util_Ref_Create_T]:
        """
        Creates a new Ref{T} instance by closing over
        the specified  variable.
        NOTE: This won't close over the variable input to the function,
        but rather a copy of the variable. This reference will use it's
        own storage.
        """
        ...

    @staticmethod
    def CreateReadOnly(getter: typing.Callable[[], QuantConnect_Util_Ref_CreateReadOnly_T]) -> QuantConnect.Util.IReadOnlyRef[QuantConnect_Util_Ref_CreateReadOnly_T]:
        """Creates a new IReadOnlyRef{T} instance"""
        ...


class SingleValueListConverter(typing.Generic[QuantConnect_Util_SingleValueListConverter_T], JsonConverter):
    """Reads json and always produces a List, even if the input has just an object"""

    def CanConvert(self, objectType: typing.Type) -> bool:
        """
        Determines whether this instance can convert the specified object type.
        
        :param objectType: Type of the object.
        :returns: true if this instance can convert the specified object type; otherwise, false.
        """
        ...

    def ReadJson(self, reader: typing.Any, objectType: typing.Type, existingValue: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Reads the JSON representation of the object. If the JSON represents a singular instance, it will be returned
        in a list.
        
        :param reader: The Newtonsoft.Json.JsonReader to read from.
        :param objectType: Type of the object.
        :param existingValue: The existing value of object being read.
        :param serializer: The calling serializer.
        :returns: The object value.
        """
        ...

    def WriteJson(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """
        Writes the JSON representation of the object. If the instance is not a list then it will
        be wrapped in a list
        
        :param writer: The Newtonsoft.Json.JsonWriter to write to.
        :param value: The value.
        :param serializer: The calling serializer.
        """
        ...


class LeanData(System.Object):
    """Provides methods for generating lean data file content"""

    SecurityTypeAsDataPath: System.Collections.Generic.HashSet[str]
    """The different SecurityType used for data paths"""

    @staticmethod
    def AggregateQuoteBars(bars: System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.QuoteBar], symbol: typing.Union[QuantConnect.Symbol, str], resolution: datetime.timedelta) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.QuoteBar]:
        """
        Aggregates a list of second/minute bars at the requested resolution
        
        :param bars: List of QuoteBars
        :param symbol: Symbol of all QuoteBars
        :param resolution: Desired resolution for new QuoteBars
        :returns: List of aggregated QuoteBars.
        """
        ...

    @staticmethod
    def AggregateTicks(ticks: System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.Tick], symbol: typing.Union[QuantConnect.Symbol, str], resolution: datetime.timedelta) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.QuoteBar]:
        """
        Aggregates a list of ticks at the requested resolution
        
        :param ticks: List of QuoteBars
        :param symbol: Symbol of all QuoteBars
        :param resolution: Desired resolution for new QuoteBars
        :returns: List of aggregated QuoteBars.
        """
        ...

    @staticmethod
    def AggregateTradeBars(bars: System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.TradeBar], symbol: typing.Union[QuantConnect.Symbol, str], resolution: datetime.timedelta) -> System.Collections.Generic.IEnumerable[QuantConnect.Data.Market.TradeBar]:
        """
        Aggregates a list of second/minute bars at the requested resolution
        
        :param bars: List of TradeBars
        :param symbol: Symbol of all tradeBars
        :param resolution: Desired resolution for new TradeBars
        :returns: List of aggregated TradeBars.
        """
        ...

    @staticmethod
    @overload
    def GenerateLine(data: QuantConnect.Data.IBaseData, resolution: QuantConnect.Resolution, exchangeTimeZone: typing.Any, dataTimeZone: typing.Any) -> str:
        """
        Converts the specified base data instance into a lean data file csv line.
        This method takes into account the fake that base data instances typically
        are time stamped in the exchange time zone, but need to be written to disk
        in the data time zone.
        """
        ...

    @staticmethod
    @overload
    def GenerateLine(data: QuantConnect.Data.IBaseData, securityType: QuantConnect.SecurityType, resolution: QuantConnect.Resolution) -> str:
        """Converts the specified base data instance into a lean data file csv line"""
        ...

    @staticmethod
    def GenerateRelativeFactorFilePath(symbol: typing.Union[QuantConnect.Symbol, str]) -> str:
        """Generates relative factor file paths for equities"""
        ...

    @staticmethod
    def GenerateRelativeZipFileDirectory(symbol: typing.Union[QuantConnect.Symbol, str], resolution: QuantConnect.Resolution) -> str:
        """Generates the relative zip directory for the specified symbol/resolution"""
        ...

    @staticmethod
    @overload
    def GenerateRelativeZipFilePath(symbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date], resolution: QuantConnect.Resolution, tickType: QuantConnect.TickType) -> str:
        """Generates the relative zip file path rooted in the /Data directory"""
        ...

    @staticmethod
    @overload
    def GenerateRelativeZipFilePath(symbol: str, securityType: QuantConnect.SecurityType, market: str, date: typing.Union[datetime.datetime, datetime.date], resolution: QuantConnect.Resolution) -> str:
        """Generates the relative zip file path rooted in the /Data directory"""
        ...

    @staticmethod
    def GenerateZipEntryName(symbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date], resolution: QuantConnect.Resolution, tickType: QuantConnect.TickType) -> str:
        """Generate's the zip entry name to hold the specified data."""
        ...

    @staticmethod
    @overload
    def GenerateZipFileName(symbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date], resolution: QuantConnect.Resolution, tickType: QuantConnect.TickType) -> str:
        """Generates the zip file name for the specified date of data."""
        ...

    @staticmethod
    @overload
    def GenerateZipFileName(symbol: str, securityType: QuantConnect.SecurityType, date: typing.Union[datetime.datetime, datetime.date], resolution: QuantConnect.Resolution, tickType: typing.Optional[QuantConnect.TickType] = None) -> str:
        """Creates the zip file name for a QC zip data file"""
        ...

    @staticmethod
    @overload
    def GenerateZipFilePath(dataDirectory: str, symbol: typing.Union[QuantConnect.Symbol, str], date: typing.Union[datetime.datetime, datetime.date], resolution: QuantConnect.Resolution, tickType: QuantConnect.TickType) -> str:
        """Generates the full zip file path rooted in the"""
        ...

    @staticmethod
    @overload
    def GenerateZipFilePath(dataDirectory: str, symbol: str, securityType: QuantConnect.SecurityType, market: str, date: typing.Union[datetime.datetime, datetime.date], resolution: QuantConnect.Resolution) -> str:
        """Generates the full zip file path rooted in the"""
        ...

    @staticmethod
    def GetCommonTickType(securityType: QuantConnect.SecurityType) -> int:
        """
        Gets the tick type most commonly associated with the specified security type
        
        :param securityType: The security type
        :returns: The most common tick type for the specified security type. This method returns the int value of a member of the QuantConnect.TickType enum.
        """
        ...

    @staticmethod
    def GetCommonTickTypeForCommonDataTypes(type: typing.Type, securityType: QuantConnect.SecurityType) -> int:
        """
        Get the TickType for common Lean data types.
        If not a Lean common data type, return a TickType of Trade.
        
        :param type: A Type used to determine the TickType
        :param securityType: The SecurityType used to determine the TickType
        :returns: A TickType corresponding to the type. This method returns the int value of a member of the QuantConnect.TickType enum.
        """
        ...

    @staticmethod
    def GetDataType(resolution: QuantConnect.Resolution, tickType: QuantConnect.TickType) -> typing.Type:
        """
        Gets the data type required for the specified combination of resolution and tick type
        
        :param resolution: The resolution, if Tick, the Type returned is always Tick
        :param tickType: The TickType that primarily dictates the type returned
        :returns: The Type used to create a subscription.
        """
        ...

    @staticmethod
    def IsCommonLeanDataType(baseDataType: typing.Type) -> bool:
        """
        Determines if the Type is a 'common' type used throughout lean
        This method is helpful in creating SubscriptionDataConfig
        
        :param baseDataType: The Type to check
        :returns: A bool indicating whether the type is of type TradeBarQuoteBar or OpenInterest.
        """
        ...

    @staticmethod
    def IsValidConfiguration(securityType: QuantConnect.SecurityType, resolution: QuantConnect.Resolution, tickType: QuantConnect.TickType) -> bool:
        """Helper method to determine if a configuration set is valid"""
        ...

    @staticmethod
    def ParseDataSecurityType(securityType: str) -> int:
        """
        Matches a data path security type with the SecurityType
        
        :param securityType: The data path security type
        :returns: The matching security type for the given data path. This method returns the int value of a member of the QuantConnect.SecurityType enum.
        """
        ...

    @staticmethod
    def ParseKey(key: str, fileName: typing.Optional[str], entryName: typing.Optional[str]) -> typing.Union[None, str, str]:
        """
        Helper to separate filename and entry from a given key for DataProviders
        
        :param key: The key to parse
        :param fileName: File name extracted
        :param entryName: Entry name extracted
        """
        ...

    @staticmethod
    def ParseTime(line: str, date: typing.Union[datetime.datetime, datetime.date], resolution: QuantConnect.Resolution) -> datetime.datetime:
        """Helper method that will parse a given data line in search of an associated date time"""
        ...

    @staticmethod
    def ReadSymbolFromZipEntry(symbol: typing.Union[QuantConnect.Symbol, str], resolution: QuantConnect.Resolution, zipEntryName: str) -> QuantConnect.Symbol:
        """
        Creates a symbol from the specified zip entry name
        
        :param symbol: The root symbol of the output symbol
        :param resolution: The resolution of the data source producing the zip entry name
        :param zipEntryName: The zip entry name to be parsed
        :returns: A new symbol representing the zip entry name.
        """
        ...

    @staticmethod
    @overload
    def TryParsePath(filePath: str, symbol: typing.Optional[typing.Union[QuantConnect.Symbol, str]], date: typing.Optional[typing.Union[datetime.datetime, datetime.date]], resolution: typing.Optional[QuantConnect.Resolution], tickType: typing.Optional[QuantConnect.TickType], dataType: typing.Optional[typing.Type]) -> typing.Union[bool, typing.Union[QuantConnect.Symbol, str], typing.Union[datetime.datetime, datetime.date], QuantConnect.Resolution, QuantConnect.TickType, typing.Type]:
        """
        Parses file name into a Security and DateTime
        
        :param filePath: File path to be parsed
        :param symbol: The symbol as parsed from the fileName
        :param date: Date of data in the file path. Only returned if the resolution is lower than Hourly
        :param resolution: The resolution of the symbol as parsed from the filePath
        :param tickType: The tick type
        :param dataType: The data type
        """
        ...

    @staticmethod
    @overload
    def TryParsePath(fileName: str, symbol: typing.Optional[typing.Union[QuantConnect.Symbol, str]], date: typing.Optional[typing.Union[datetime.datetime, datetime.date]], resolution: typing.Optional[QuantConnect.Resolution]) -> typing.Union[bool, typing.Union[QuantConnect.Symbol, str], typing.Union[datetime.datetime, datetime.date], QuantConnect.Resolution]:
        """
        Parses file name into a Security and DateTime
        
        :param fileName: File name to be parsed
        :param symbol: The symbol as parsed from the fileName
        :param date: Date of data in the file path. Only returned if the resolution is lower than Hourly
        :param resolution: The resolution of the symbol as parsed from the filePath
        """
        ...

    @staticmethod
    def TryParseSecurityType(fileName: str, securityType: typing.Optional[QuantConnect.SecurityType], market: typing.Optional[str]) -> typing.Union[bool, QuantConnect.SecurityType, str]:
        """
        Parses file name into a Security and DateTime
        
        :param fileName: File name to be parsed
        :param securityType: The securityType as parsed from the fileName
        :param market: The market as parsed from the fileName
        """
        ...


class SecurityIdentifierJsonConverter(QuantConnect.Util.TypeChangeJsonConverter[QuantConnect.SecurityIdentifier, str]):
    """A JsonConverter implementation that serializes a SecurityIdentifier as a string"""

    @overload
    def Convert(self, value: QuantConnect.SecurityIdentifier) -> str:
        """
        Converts as security identifier to a string
        
        This method is protected.
        
        :param value: The input value to be converted before serialziation
        :returns: A new instance of TResult that is to be serialzied.
        """
        ...

    @overload
    def Convert(self, value: str) -> QuantConnect.SecurityIdentifier:
        """
        Converts the input string to a security identifier
        
        This method is protected.
        
        :param value: The deserialized value that needs to be converted to T
        :returns: The converted value.
        """
        ...


class ListComparer(typing.Generic[QuantConnect_Util_ListComparer_T], System.Object, System.Collections.Generic.IEqualityComparer[System.Collections.Generic.List[QuantConnect_Util_ListComparer_T]]):
    """
    An implementation of IEqualityComparer{T} for List{T}.
    Useful when using a List{T} as the key of a collection.
    """

    def Equals(self, x: System.Collections.Generic.List[QuantConnect_Util_ListComparer_T], y: System.Collections.Generic.List[QuantConnect_Util_ListComparer_T]) -> bool:
        """
        Determines whether the specified objects are equal.
        
        :returns: true if the specified objects are equal; otherwise, false.
        """
        ...

    def GetHashCode(self, obj: System.Collections.Generic.List[QuantConnect_Util_ListComparer_T]) -> int:
        """
        Returns a hash code for the specified object.
        
        :returns: A hash code for the specified object created from combining the hash code of all the elements in the collection.
        """
        ...


class WorkerThread(System.Object, System.IDisposable):
    """
    This worker tread is required to guarantee all python operations are
    executed by the same thread, to enable complete debugging functionality.
    We don't use the main thread, to avoid any chance of blocking the process
    """

    Instance: QuantConnect.Util.WorkerThread = ...
    """The worker thread instance"""

    @property
    def FinishedWorkItem(self) -> System.Threading.AutoResetEvent:
        """Will be set when the worker thread finishes a work item"""
        ...

    def __init__(self) -> None:
        """
        Creates a new instance, which internally launches a new worker thread
        
        This method is protected.
        """
        ...

    def Add(self, action: typing.Callable[[], None]) -> None:
        """
        Adds a new item of work
        
        :param action: The work item to add
        """
        ...

    def Dispose(self) -> None:
        """Disposes the worker thread."""
        ...


class FixedSizeHashQueue(typing.Generic[QuantConnect_Util_FixedSizeHashQueue_T], System.Object, typing.Iterable[QuantConnect_Util_FixedSizeHashQueue_T]):
    """Provides an implementation of an add-only fixed length, unique queue system"""

    def __init__(self, size: int) -> None:
        """
        Initializes a new instance of the FixedSizeHashQueue{T} class
        
        :param size: The maximum number of items to hold
        """
        ...

    def Add(self, item: QuantConnect_Util_FixedSizeHashQueue_T) -> bool:
        """Returns true if the item was added and didn't already exists"""
        ...

    def Contains(self, item: QuantConnect_Util_FixedSizeHashQueue_T) -> bool:
        """Returns true if the specified item exists in the collection"""
        ...

    def Dequeue(self) -> QuantConnect_Util_FixedSizeHashQueue_T:
        """Dequeues and returns the next item in the queue"""
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[QuantConnect_Util_FixedSizeHashQueue_T]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: A System.Collections.Generic.IEnumerator`1 that can be used to iterate through the collection.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        """
        Returns an enumerator that iterates through a collection.
        
        :returns: An System.Collections.IEnumerator object that can be used to iterate through the collection.
        """
        ...

    def TryPeek(self, item: typing.Optional[QuantConnect_Util_FixedSizeHashQueue_T]) -> typing.Union[bool, QuantConnect_Util_FixedSizeHashQueue_T]:
        """Tries to inspect the first item in the queue"""
        ...


class DoubleUnixSecondsDateTimeJsonConverter(QuantConnect.Util.TypeChangeJsonConverter[typing.Optional[datetime.datetime], typing.Optional[float]]):
    """Defines a JsonConverter that serializes DateTime use the number of whole and fractional seconds since unix epoch"""

    def CanConvert(self, objectType: typing.Type) -> bool:
        """
        Determines whether this instance can convert the specified object type.
        
        :param objectType: Type of the object.
        :returns: true if this instance can convert the specified object type; otherwise, false.
        """
        ...

    @overload
    def Convert(self, value: typing.Optional[datetime.datetime]) -> typing.Optional[float]:
        """
        Convert the input value to a value to be serialzied
        
        This method is protected.
        
        :param value: The input value to be converted before serialziation
        :returns: A new instance of TResult that is to be serialzied.
        """
        ...

    @overload
    def Convert(self, value: typing.Optional[float]) -> typing.Optional[datetime.datetime]:
        """
        Converts the input value to be deserialized
        
        This method is protected.
        
        :param value: The deserialized value that needs to be converted to T
        :returns: The converted value.
        """
        ...


class PythonUtil(System.Object):
    """Collection of utils for python objects processing"""

    ExceptionLineShift: int
    """The python exception stack trace line shift to use"""

    @staticmethod
    def ConvertToSymbols(input: typing.Any) -> System.Collections.Generic.IEnumerable[QuantConnect.Symbol]:
        """
        Convert Python input to a list of Symbols
        
        :param input: Object with the desired property
        :returns: List of Symbols.
        """
        ...

    @staticmethod
    def PythonExceptionMessageParser(message: str) -> str:
        """
        Parsers PythonException.Message into a readable message
        
        :param message: The python exception message
        :returns: String with relevant part of the stacktrace.
        """
        ...

    @staticmethod
    def PythonExceptionParser(pythonException: typing.Any) -> str:
        """
        Parsers PythonException into a readable message
        
        :param pythonException: The exception to parse
        :returns: String with relevant part of the stacktrace.
        """
        ...

    @staticmethod
    def PythonExceptionStackParser(value: str) -> str:
        """
        Parsers PythonException.StackTrace into a readable message
        
        :param value: String with the stacktrace information
        :returns: String with relevant part of the stacktrace.
        """
        ...

    @staticmethod
    @overload
    def ToAction(pyObject: typing.Any) -> typing.Callable[[QuantConnect_Util_PythonUtil_ToAction_T1], None]:
        """
        Encapsulates a python method with a System.Action{T1}
        
        :param pyObject: The python method
        :returns: A System.Action{T1} that encapsulates the python method.
        """
        ...

    @staticmethod
    @overload
    def ToAction(pyObject: typing.Any) -> typing.Callable[[QuantConnect_Util_PythonUtil_ToAction_T1, QuantConnect_Util_PythonUtil_ToAction_T2], None]:
        """
        Encapsulates a python method with a System.Action{T1, T2}
        
        :param pyObject: The python method
        :returns: A System.Action{T1, T2} that encapsulates the python method.
        """
        ...

    @staticmethod
    def ToCoarseFundamentalSelector(pyObject: typing.Any) -> typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.UniverseSelection.CoarseFundamental]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]:
        """
        Encapsulates a python method in coarse fundamental universe selector.
        
        :param pyObject: The python method
        :returns: A Func{T, TResult} (parameter is IEnumerable{CoarseFundamental}, return value is IEnumerable{Symbol}) that encapsulates the python method.
        """
        ...

    @staticmethod
    def ToFineFundamentalSelector(pyObject: typing.Any) -> typing.Callable[[System.Collections.Generic.IEnumerable[QuantConnect.Data.Fundamental.FineFundamental]], System.Collections.Generic.IEnumerable[QuantConnect.Symbol]]:
        """
        Encapsulates a python method in fine fundamental universe selector.
        
        :param pyObject: The python method
        :returns: A Func{T, TResult} (parameter is IEnumerable{FineFundamental}, return value is IEnumerable{Symbol}) that encapsulates the python method.
        """
        ...

    @staticmethod
    def ToFunc(pyObject: typing.Any) -> typing.Callable[[QuantConnect_Util_PythonUtil_ToFunc_T1], QuantConnect_Util_PythonUtil_ToFunc_T2]:
        """
        Encapsulates a python method with a System.Func{T1, T2}
        
        :param pyObject: The python method
        :returns: A System.Func{T1, T2} that encapsulates the python method.
        """
        ...


class LeanDataPathComponents(System.Object):
    """Type representing the various pieces of information emebedded into a lean data file path"""

    @property
    def Date(self) -> datetime.datetime:
        """Gets the date component from the file name"""
        ...

    @Date.setter
    def Date(self, value: datetime.datetime):
        """Gets the date component from the file name"""
        ...

    @property
    def SecurityType(self) -> int:
        """
        Gets the security type from the path
        
        This property contains the int value of a member of the QuantConnect.SecurityType enum.
        """
        ...

    @SecurityType.setter
    def SecurityType(self, value: int):
        """
        Gets the security type from the path
        
        This property contains the int value of a member of the QuantConnect.SecurityType enum.
        """
        ...

    @property
    def Market(self) -> str:
        """Gets the market from the path"""
        ...

    @Market.setter
    def Market(self, value: str):
        """Gets the market from the path"""
        ...

    @property
    def Resolution(self) -> int:
        """
        Gets the resolution from the path
        
        This property contains the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    @Resolution.setter
    def Resolution(self, value: int):
        """
        Gets the resolution from the path
        
        This property contains the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    @property
    def Filename(self) -> str:
        """Gets the file name, not inluding directory information"""
        ...

    @Filename.setter
    def Filename(self, value: str):
        """Gets the file name, not inluding directory information"""
        ...

    @property
    def Symbol(self) -> QuantConnect.Symbol:
        """
        Gets the symbol object implied by the path. For options, or any
        multi-entry zip file, this should be the canonical symbol
        """
        ...

    @Symbol.setter
    def Symbol(self, value: QuantConnect.Symbol):
        """
        Gets the symbol object implied by the path. For options, or any
        multi-entry zip file, this should be the canonical symbol
        """
        ...

    @property
    def TickType(self) -> int:
        """
        Gets the tick type from the file name
        
        This property contains the int value of a member of the QuantConnect.TickType enum.
        """
        ...

    @TickType.setter
    def TickType(self, value: int):
        """
        Gets the tick type from the file name
        
        This property contains the int value of a member of the QuantConnect.TickType enum.
        """
        ...

    def __init__(self, securityType: QuantConnect.SecurityType, market: str, resolution: QuantConnect.Resolution, symbol: typing.Union[QuantConnect.Symbol, str], filename: str, date: typing.Union[datetime.datetime, datetime.date], tickType: QuantConnect.TickType) -> None:
        """Initializes a new instance of the LeanDataPathComponents class"""
        ...

    @staticmethod
    def Parse(path: str) -> QuantConnect.Util.LeanDataPathComponents:
        """
        Parses the specified path into a new instance of the LeanDataPathComponents class
        
        :param path: The path to be parsed
        :returns: A new instance of the LeanDataPathComponents class representing the specified path.
        """
        ...


class BusyCollection(typing.Generic[QuantConnect_Util_BusyCollection_T], System.Object, QuantConnect.Interfaces.IBusyCollection[QuantConnect_Util_BusyCollection_T]):
    """A non blocking IBusyCollection{T} implementation"""

    @property
    def WaitHandle(self) -> System.Threading.WaitHandle:
        """
        Gets a wait handle that can be used to wait until this instance is done
        processing all of it's item
        """
        ...

    @property
    def Count(self) -> int:
        """Gets the number of items held within this collection"""
        ...

    @property
    def IsBusy(self) -> bool:
        """Returns true if processing, false otherwise"""
        ...

    @overload
    def Add(self, item: QuantConnect_Util_BusyCollection_T) -> None:
        """
        Adds the items to this collection
        
        :param item: The item to be added
        """
        ...

    @overload
    def Add(self, item: QuantConnect_Util_BusyCollection_T, cancellationToken: System.Threading.CancellationToken) -> None:
        """
        Adds the items to this collection
        
        :param item: The item to be added
        :param cancellationToken: A cancellation token to observer
        """
        ...

    def CompleteAdding(self) -> None:
        """Marks the collection as not accepting any more additions"""
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    @overload
    def GetConsumingEnumerable(self) -> System.Collections.Generic.IEnumerable[QuantConnect_Util_BusyCollection_T]:
        """
        Provides a consuming enumerable for items in this collection.
        
        :returns: An enumerable that removes and returns items from the collection.
        """
        ...

    @overload
    def GetConsumingEnumerable(self, cancellationToken: System.Threading.CancellationToken) -> System.Collections.Generic.IEnumerable[QuantConnect_Util_BusyCollection_T]:
        """
        Provides a consuming enumerable for items in this collection.
        
        :param cancellationToken: A cancellation token to observer
        :returns: An enumerable that removes and returns items from the collection.
        """
        ...


class ObjectActivator(System.Object):
    """Provides methods for creating new instances of objects"""

    @staticmethod
    def AddActivator(key: typing.Type, value: typing.Callable[[typing.List[System.Object]], System.Object]) -> None:
        """
        Adds method to return an instance of object
        
        :param key: The key of the method to add
        :param value: The value of the method to add
        """
        ...

    @staticmethod
    @overload
    def Clone(instanceToClone: typing.Any) -> System.Object:
        """
        Clones the specified instance using reflection
        
        :param instanceToClone: The instance to be cloned
        :returns: A field/property wise, non-recursive clone of the instance.
        """
        ...

    @staticmethod
    @overload
    def Clone(instanceToClone: QuantConnect_Util_ObjectActivator_Clone_T) -> QuantConnect_Util_ObjectActivator_Clone_T:
        """Clones the specified instance and then casts it to T before returning"""
        ...

    @staticmethod
    def GetActivator(dataType: typing.Type) -> typing.Callable[[typing.List[System.Object]], System.Object]:
        """
        Fast Object Creator from Generic Type:
        Modified from http://rogeralsing.com/2008/02/28/linq-expressions-creating-objects/
        
        :param dataType: Type of the object we wish to create
        :returns: Method to return an instance of object.
        """
        ...

    @staticmethod
    def ResetActivators() -> None:
        """Reset the object activators"""
        ...


class CurrencyPairUtil(System.Object):
    """Utility methods for decomposing and comparing currency pairs"""

    class Match(System.Enum):
        """Represents the relation between two currency pairs"""

        NoMatch = 0
        """The two currency pairs don't match each other normally nor when one is reversed"""

        ExactMatch = 1
        """The two currency pairs match each other exactly"""

        InverseMatch = 2
        """The two currency pairs are the inverse of each other"""

    @staticmethod
    def ComparePair(pairA: typing.Union[QuantConnect.Symbol, str], baseCurrencyB: str, quoteCurrencyB: str) -> int:
        """
        Returns how two currency pairs are related to each other
        
        :param pairA: The first pair
        :param baseCurrencyB: The base currency of the second pair
        :param quoteCurrencyB: The quote currency of the second pair
        :returns: The Match member that represents the relation between the two pairs. This method returns the int value of a member of the QuantConnect.Util.CurrencyPairUtil.Match enum.
        """
        ...

    @staticmethod
    @overload
    def CurrencyPairDual(currencyPair: typing.Union[QuantConnect.Symbol, str], knownSymbol: str) -> str:
        """
        You have currencyPair AB and one known symbol (A or B). This function returns the other symbol (B or A).
        
        :param currencyPair: Currency pair AB
        :param knownSymbol: Known part of the currencyPair (either A or B)
        :returns: The other part of currencyPair (either B or A), or null if known symbol is not part of currencyPair.
        """
        ...

    @staticmethod
    @overload
    def CurrencyPairDual(baseCurrency: str, quoteCurrency: str, knownSymbol: str) -> str:
        """
        You have currencyPair AB and one known symbol (A or B). This function returns the other symbol (B or A).
        
        :param baseCurrency: The base currency of the currency pair
        :param quoteCurrency: The quote currency of the currency pair
        :param knownSymbol: Known part of the currencyPair (either A or B)
        :returns: The other part of currencyPair (either B or A), or null if known symbol is not part of the currency pair.
        """
        ...

    @staticmethod
    def DecomposeCurrencyPair(currencyPair: typing.Union[QuantConnect.Symbol, str], baseCurrency: typing.Optional[str], quoteCurrency: typing.Optional[str], defaultQuoteCurrency: str = ...) -> typing.Union[None, str, str]:
        """
        Decomposes the specified currency pair into a base and quote currency provided as out parameters
        
        :param currencyPair: The input currency pair to be decomposed
        :param baseCurrency: The output base currency
        :param quoteCurrency: The output quote currency
        :param defaultQuoteCurrency: Optionally can provide a default quote currency
        """
        ...

    @staticmethod
    def IsDecomposable(currencyPair: typing.Union[QuantConnect.Symbol, str]) -> bool:
        """
        Checks whether a symbol is decomposable into a base and a quote currency
        
        :param currencyPair: The pair to check for
        :returns: True if the pair can be decomposed into base and quote currencies, false if not.
        """
        ...

    @staticmethod
    def TryDecomposeCurrencyPair(currencyPair: typing.Union[QuantConnect.Symbol, str], baseCurrency: typing.Optional[str], quoteCurrency: typing.Optional[str]) -> typing.Union[bool, str, str]:
        """
        Tries to decomposes the specified currency pair into a base and quote currency provided as out parameters
        
        :param currencyPair: The input currency pair to be decomposed
        :param baseCurrency: The output base currency
        :param quoteCurrency: The output quote currency
        :returns: True if was able to decompose the currency pair.
        """
        ...


class SeriesJsonConverter(JsonConverter):
    """Json Converter for Series which handles special Pie Series serialization case"""

    @property
    def CanRead(self) -> bool:
        """This converter wont be used to read JSON. Will throw exception if manually called."""
        ...

    def CanConvert(self, objectType: typing.Type) -> bool:
        """
        Determine if this Converter can convert this type
        
        :param objectType: Type that we would like to convert
        :returns: True if Series.
        """
        ...

    def ReadJson(self, reader: typing.Any, objectType: typing.Type, existingValue: typing.Any, serializer: typing.Any) -> System.Object:
        """Not implemented"""
        ...

    def WriteJson(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """
        Write Series to Json
        
        :param writer: The Json Writer to use
        :param value: The value to written to Json
        :param serializer: The Json Serializer to use
        """
        ...


class DisposableExtensions(System.Object):
    """Provides extensions methods for IDisposable"""

    @staticmethod
    @overload
    def DisposeSafely(disposable: System.IDisposable) -> bool:
        """
        Calls IDisposable.Dispose within a try/catch and logs any errors.
        
        :param disposable: The IDisposable to be disposed
        :returns: True if the object was successfully disposed, false if an error was thrown.
        """
        ...

    @staticmethod
    @overload
    def DisposeSafely(disposable: System.IDisposable, errorHandler: typing.Callable[[System.Exception], None]) -> bool:
        """
        Calls IDisposable.Dispose within a try/catch and invokes the
         on any errors.
        
        :param disposable: The IDisposable to be disposed
        :param errorHandler: Error handler delegate invoked if an exception is thrown while calling IDisposable.Dispose
        :returns: True if the object was successfully disposed, false if an error was thrown or the specified disposable was null.
        """
        ...


class ColorJsonConverter(QuantConnect.Util.TypeChangeJsonConverter[System.Drawing.Color, str]):
    """
    A JsonConverter implementation that serializes a Color as a string.
    If Color is empty, string is also empty and vice-versa. Meaning that color is autogen.
    """

    @overload
    def Convert(self, value: System.Drawing.Color) -> str:
        """
        Converts a .NET Color to a hexadecimal as a string
        
        This method is protected.
        
        :param value: The input value to be converted before serialization
        :returns: Hexadecimal number as a string. If .NET Color is null, returns default #000000.
        """
        ...

    @overload
    def Convert(self, value: str) -> System.Drawing.Color:
        """
        Converts the input string to a .NET Color object
        
        This method is protected.
        
        :param value: The deserialized value that needs to be converted to T
        :returns: The converted value.
        """
        ...


class ReferenceWrapper(typing.Generic[QuantConnect_Util_ReferenceWrapper_T], System.Object):
    """
    We wrap a T instance, a value type, with a class, a reference type, to achieve thread safety when assigning new values
    and reading from multiple threads. This is possible because assignments are atomic operations in C# for reference types (among others).
    """

    @property
    def Value(self) -> QuantConnect_Util_ReferenceWrapper_T:
        """The current value"""
        ...

    def __init__(self, value: QuantConnect_Util_ReferenceWrapper_T) -> None:
        """
        Creates a new instance
        
        :param value: The value to use
        """
        ...


class SecurityExtensions(System.Object):
    """
    Provides useful infrastructure methods to the Security class.
    These are added in this way to avoid mudding the class's public API
    """

    @staticmethod
    def IsInternalFeed(security: QuantConnect.Securities.Security) -> bool:
        """Determines if all subscriptions for the security are internal feeds"""
        ...


class ExpressionBuilder(System.Object):
    """Provides methods for constructing expressions at runtime"""

    @staticmethod
    def AsEnumerable(expression: typing.Any) -> System.Collections.Generic.IEnumerable[Expression]:
        """
        Converts the specified expression into an enumerable of expressions by walking the expression tree
        
        :param expression: The expression to enumerate
        :returns: An enumerable containing all expressions in the input expression.
        """
        ...

    @staticmethod
    def IsBinaryComparison(type: typing.Any) -> bool:
        """Determines whether or not the specified  is a binary comparison."""
        ...

    @staticmethod
    def MakeBinaryComparisonLambda(type: typing.Any) -> typing.Any:
        """
        Constructs a lambda expression that accepts two parameters of type T and applies
        the specified binary comparison and returns the boolean result.
        """
        ...

    @staticmethod
    @overload
    def MakePropertyOrFieldSelector(type: typing.Type, propertyOrField: str) -> typing.Any:
        """
        Constructs a selector of the form: x => x.propertyOrField where x is an instance of 'type'
        
        :param type: The type of the parameter in the expression
        :param propertyOrField: The name of the property or field to bind to
        :returns: A new lambda expression that represents accessing the property or field on 'type'.
        """
        ...

    @staticmethod
    @overload
    def MakePropertyOrFieldSelector(propertyOrField: str) -> typing.Any:
        """
        Constructs a selector of the form: x => x.propertyOrField where x is an instance of 'type'
        
        :param propertyOrField: The name of the property or field to bind to
        :returns: A new lambda expression that represents accessing the property or field on 'type'.
        """
        ...

    @staticmethod
    def OfType(expression: typing.Any) -> System.Collections.Generic.IEnumerable[QuantConnect_Util_ExpressionBuilder_OfType_T]:
        """
        Returns all the expressions of the specified type in the given expression tree
        
        :param expression: The expression to search
        :returns: All expressions of the given type in the specified expression.
        """
        ...

    @staticmethod
    @overload
    def Single(expression: typing.Any) -> QuantConnect_Util_ExpressionBuilder_Single_T:
        """
        Returns the single expression of the specified type or throws if none or more than one expression
        of the specified type is contained within the expression.
        
        :param expression: The expression to search
        :returns: Expression of the specified type.
        """
        ...

    @staticmethod
    @overload
    def Single(expressions: System.Collections.Generic.IEnumerable[Expression]) -> QuantConnect_Util_ExpressionBuilder_Single_T:
        """
        Returns the single expression of the specified type or throws if none or more than one expression
        of the specified type is contained within the expression.
        
        :param expressions: The expressions to search
        :returns: Expression of the specified type.
        """
        ...


class Composer(System.Object):
    """Provides methods for obtaining exported MEF instances"""

    Instance: QuantConnect.Util.Composer
    """Gets the singleton instance"""

    def __init__(self) -> None:
        """
        Initializes a new instance of the Composer class. This type
        is a light wrapper on top of an MEF CompositionContainer
        """
        ...

    def AddPart(self, instance: QuantConnect_Util_Composer_AddPart_T) -> None:
        """
        Adds the specified instance to this instance to allow it to be recalled via GetExportedValueByTypeName
        
        :param instance: The instance to add
        """
        ...

    def GetExportedTypes(self) -> System.Collections.Generic.IEnumerable[typing.Type]:
        """Will return all loaded types that are assignable to T type"""
        ...

    def GetExportedValueByTypeName(self, typeName: str, forceTypeNameOnExisting: bool = True) -> QuantConnect_Util_Composer_GetExportedValueByTypeName_T:
        """
        Extension method to searches the composition container for an export that has a matching type name. This function
        will first try to match on Type.AssemblyQualifiedName, then Type.FullName, and finally on Type.Name
        
        This method will not throw if multiple types are found matching the name, it will just return the first one it finds.
        
        :param typeName: The name of the type to find. This can be an assembly qualified name, a full name, or just the type's name
        :param forceTypeNameOnExisting: When false, if any existing instance of type T is found, it will be returned even if type name doesn't match. This is useful in cases where a single global instance is desired, like for IDataAggregator
        :returns: The export instance.
        """
        ...

    def GetExportedValues(self) -> System.Collections.Generic.IEnumerable[QuantConnect_Util_Composer_GetExportedValues_T]:
        """Gets all exports of type T"""
        ...

    def GetPart(self) -> QuantConnect_Util_Composer_GetPart_T:
        """Gets the first type T instance if any"""
        ...

    def Reset(self) -> None:
        """Clears the cache of exported values, causing new instances to be created."""
        ...

    def Single(self, predicate: typing.Callable[[QuantConnect_Util_Composer_Single_T], bool]) -> QuantConnect_Util_Composer_Single_T:
        """
        Gets the export matching the predicate
        
        :param predicate: Function used to pick which imported instance to return, if null the first instance is returned
        :returns: The only export matching the specified predicate.
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Util__EventContainer_Callable, QuantConnect_Util__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Util__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Util__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Util__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


