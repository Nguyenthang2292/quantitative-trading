from typing import overload
import datetime
import typing

import System
import System.ComponentModel
import System.Timers

System_Timers__EventContainer_Callable = typing.TypeVar("System_Timers__EventContainer_Callable")
System_Timers__EventContainer_ReturnType = typing.TypeVar("System_Timers__EventContainer_ReturnType")


class ElapsedEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def SignalTime(self) -> datetime.datetime:
        ...


class Timer(System.ComponentModel.Component, System.ComponentModel.ISupportInitialize):
    """Handles recurring events in an application."""

    @property
    def AutoReset(self) -> bool:
        """
        Gets or sets a value indicating whether the Timer raises the Tick event each time the specified
        Interval has elapsed, when Enabled is set to true.
        """
        ...

    @AutoReset.setter
    def AutoReset(self, value: bool):
        """
        Gets or sets a value indicating whether the Timer raises the Tick event each time the specified
        Interval has elapsed, when Enabled is set to true.
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Gets or sets a value indicating whether the System.Timers.Timer
        is able to raise events at a defined interval.
        The default value by design is false, don't change it.
        """
        ...

    @Enabled.setter
    def Enabled(self, value: bool):
        """
        Gets or sets a value indicating whether the System.Timers.Timer
        is able to raise events at a defined interval.
        The default value by design is false, don't change it.
        """
        ...

    @property
    def Interval(self) -> float:
        """Gets or sets the interval on which to raise events."""
        ...

    @Interval.setter
    def Interval(self, value: float):
        """Gets or sets the interval on which to raise events."""
        ...

    @property
    def Elapsed(self) -> _EventContainer[typing.Callable[[System.Object, System.Timers.ElapsedEventArgs], None], None]:
        """
        Occurs when the System.Timers.Timer.Interval has
        elapsed.
        """
        ...

    @Elapsed.setter
    def Elapsed(self, value: _EventContainer[typing.Callable[[System.Object, System.Timers.ElapsedEventArgs], None], None]):
        """
        Occurs when the System.Timers.Timer.Interval has
        elapsed.
        """
        ...

    @property
    def Site(self) -> System.ComponentModel.ISite:
        """Sets the enable property in design mode to true by default."""
        ...

    @Site.setter
    def Site(self, value: System.ComponentModel.ISite):
        """Sets the enable property in design mode to true by default."""
        ...

    @property
    def SynchronizingObject(self) -> System.ComponentModel.ISynchronizeInvoke:
        """
        Gets or sets the object used to marshal event-handler calls that are issued when
        an interval has elapsed.
        """
        ...

    @SynchronizingObject.setter
    def SynchronizingObject(self, value: System.ComponentModel.ISynchronizeInvoke):
        """
        Gets or sets the object used to marshal event-handler calls that are issued when
        an interval has elapsed.
        """
        ...

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the System.Timers.Timer class, with the properties
        set to initial values.
        """
        ...

    @overload
    def __init__(self, interval: float) -> None:
        """
        Initializes a new instance of the System.Timers.Timer class, setting the System.Timers.Timer.Interval property to the specified period.
        
        :param interval: The time, in milliseconds, between events. The value must be greater than zero and less than or equal to int.MaxValue.
        """
        ...

    @overload
    def __init__(self, interval: datetime.timedelta) -> None:
        """
        Initializes a new instance of the Timer class, setting the Interval property to the specified period.
        
        :param interval: The time between events. The value in milliseconds must be greater than zero and less than or equal to int.MaxValue.
        """
        ...

    def BeginInit(self) -> None:
        """Notifies the object that initialization is beginning and tells it to stand by."""
        ...

    def Close(self) -> None:
        """
        Disposes of the resources (other than memory) used by
        the System.Timers.Timer.
        """
        ...

    def Dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def EndInit(self) -> None:
        """Notifies the object that initialization is complete."""
        ...

    def Start(self) -> None:
        """Starts the timing by setting System.Timers.Timer.Enabled to true."""
        ...

    def Stop(self) -> None:
        """Stops the timing by setting System.Timers.Timer.Enabled to false."""
        ...


class TimersDescriptionAttribute(System.ComponentModel.DescriptionAttribute):
    """
    DescriptionAttribute marks a property, event, or extender with a
    description. Visual designers can display this description when referencing
    the member.
    """

    @property
    def Description(self) -> str:
        """Retrieves the description text."""
        ...

    def __init__(self, description: str) -> None:
        """Constructs a new sys description."""
        ...


class _EventContainer(typing.Generic[System_Timers__EventContainer_Callable, System_Timers__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_Timers__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_Timers__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_Timers__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


