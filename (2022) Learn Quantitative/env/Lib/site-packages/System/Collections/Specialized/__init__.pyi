from typing import overload
import abc
import typing

import System
import System.Collections
import System.Collections.Specialized

System_Collections_Specialized__EventContainer_Callable = typing.TypeVar("System_Collections_Specialized__EventContainer_Callable")
System_Collections_Specialized__EventContainer_ReturnType = typing.TypeVar("System_Collections_Specialized__EventContainer_ReturnType")


class NotifyCollectionChangedAction(System.Enum):
    """This enum describes the action that caused a CollectionChanged event."""

    Add = 0
    """One or more items were added to the collection."""

    Remove = 1
    """One or more items were removed from the collection."""

    Replace = 2
    """One or more items were replaced in the collection."""

    Move = 3
    """One or more items were moved within the collection."""

    Reset = 4
    """The contents of the collection changed dramatically."""


class NotifyCollectionChangedEventArgs(System.EventArgs):
    """
    Arguments for the CollectionChanged event.
    A collection that supports INotifyCollectionChangedThis raises this event
    whenever an item is added or removed, or when the contents of the collection
    changes dramatically.
    """

    @property
    def Action(self) -> int:
        """
        The action that caused the event.
        
        This property contains the int value of a member of the System.Collections.Specialized.NotifyCollectionChangedAction enum.
        """
        ...

    @property
    def NewItems(self) -> System.Collections.IList:
        """The items affected by the change."""
        ...

    @property
    def OldItems(self) -> System.Collections.IList:
        """The old items affected by the change (for Replace events)."""
        ...

    @property
    def NewStartingIndex(self) -> int:
        """The index where the change occurred."""
        ...

    @property
    def OldStartingIndex(self) -> int:
        """The old index where the change occurred (for Move events)."""
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction) -> None:
        """
        Construct a NotifyCollectionChangedEventArgs that describes a reset change.
        
        :param action: The action that caused the event (must be Reset).
        """
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, changedItem: typing.Any) -> None:
        """
        Construct a NotifyCollectionChangedEventArgs that describes a one-item change.
        
        :param action: The action that caused the event; can only be Reset, Add or Remove action.
        :param changedItem: The item affected by the change.
        """
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, changedItem: typing.Any, index: int) -> None:
        """
        Construct a NotifyCollectionChangedEventArgs that describes a one-item change.
        
        :param action: The action that caused the event.
        :param changedItem: The item affected by the change.
        :param index: The index where the change occurred.
        """
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, changedItems: System.Collections.IList) -> None:
        """
        Construct a NotifyCollectionChangedEventArgs that describes a multi-item change.
        
        :param action: The action that caused the event.
        :param changedItems: The items affected by the change.
        """
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, changedItems: System.Collections.IList, startingIndex: int) -> None:
        """
        Construct a NotifyCollectionChangedEventArgs that describes a multi-item change (or a reset).
        
        :param action: The action that caused the event.
        :param changedItems: The items affected by the change.
        :param startingIndex: The index where the change occurred.
        """
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, newItem: typing.Any, oldItem: typing.Any) -> None:
        """
        Construct a NotifyCollectionChangedEventArgs that describes a one-item Replace event.
        
        :param action: Can only be a Replace action.
        :param newItem: The new item replacing the original item.
        :param oldItem: The original item that is replaced.
        """
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, newItem: typing.Any, oldItem: typing.Any, index: int) -> None:
        """
        Construct a NotifyCollectionChangedEventArgs that describes a one-item Replace event.
        
        :param action: Can only be a Replace action.
        :param newItem: The new item replacing the original item.
        :param oldItem: The original item that is replaced.
        :param index: The index of the item being replaced.
        """
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, newItems: System.Collections.IList, oldItems: System.Collections.IList) -> None:
        """
        Construct a NotifyCollectionChangedEventArgs that describes a multi-item Replace event.
        
        :param action: Can only be a Replace action.
        :param newItems: The new items replacing the original items.
        :param oldItems: The original items that are replaced.
        """
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, newItems: System.Collections.IList, oldItems: System.Collections.IList, startingIndex: int) -> None:
        """
        Construct a NotifyCollectionChangedEventArgs that describes a multi-item Replace event.
        
        :param action: Can only be a Replace action.
        :param newItems: The new items replacing the original items.
        :param oldItems: The original items that are replaced.
        :param startingIndex: The starting index of the items being replaced.
        """
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, changedItem: typing.Any, index: int, oldIndex: int) -> None:
        """
        Construct a NotifyCollectionChangedEventArgs that describes a one-item Move event.
        
        :param action: Can only be a Move action.
        :param changedItem: The item affected by the change.
        :param index: The new index for the changed item.
        :param oldIndex: The old index for the changed item.
        """
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, changedItems: System.Collections.IList, index: int, oldIndex: int) -> None:
        """
        Construct a NotifyCollectionChangedEventArgs that describes a multi-item Move event.
        
        :param action: The action that caused the event.
        :param changedItems: The items affected by the change.
        :param index: The new index for the changed items.
        :param oldIndex: The old index for the changed items.
        """
        ...


class INotifyCollectionChanged(metaclass=abc.ABCMeta):
    """
    A collection implementing this interface will notify listeners of dynamic changes,
    e.g. when items get added and removed or the whole list is refreshed.
    """

    @property
    @abc.abstractmethod
    def CollectionChanged(self) -> _EventContainer[typing.Callable[[System.Object, System.Collections.Specialized.NotifyCollectionChangedEventArgs], None], None]:
        """Occurs when the collection changes, either by adding or removing an item."""
        ...

    @CollectionChanged.setter
    @abc.abstractmethod
    def CollectionChanged(self, value: _EventContainer[typing.Callable[[System.Object, System.Collections.Specialized.NotifyCollectionChangedEventArgs], None], None]):
        """Occurs when the collection changes, either by adding or removing an item."""
        ...


class _EventContainer(typing.Generic[System_Collections_Specialized__EventContainer_Callable, System_Collections_Specialized__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_Collections_Specialized__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_Collections_Specialized__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_Collections_Specialized__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


