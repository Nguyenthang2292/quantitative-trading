from typing import overload
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Scheduling
import QuantConnect.Securities
import System
import System.Collections.Generic

QuantConnect_Scheduling__EventContainer_Callable = typing.TypeVar("QuantConnect_Scheduling__EventContainer_Callable")
QuantConnect_Scheduling__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Scheduling__EventContainer_ReturnType")


class IDateRule(metaclass=abc.ABCMeta):
    """Specifies dates that events should be fired, used in conjunction with the ITimeRule"""

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        """Gets a name for this rule"""
        ...

    def GetDates(self, start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[datetime.datetime]:
        """
        Gets the dates produced by this date rule between the specified times
        
        :param start: The start of the interval to produce dates for
        :param end: The end of the interval to produce dates for
        :returns: All dates in the interval matching this date rule.
        """
        ...


class DateRules(System.Object):
    """Helper class used to provide better syntax when defining date rules"""

    @property
    def Today(self) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should only fire today in the algorithm's time zone
        using _securities.UtcTime instead of 'start' since ScheduleManager backs it up a day
        """
        ...

    @property
    def Tomorrow(self) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should only fire tomorrow in the algorithm's time zone
        using _securities.UtcTime instead of 'start' since ScheduleManager backs it up a day
        """
        ...

    def __init__(self, securities: QuantConnect.Securities.SecurityManager, timeZone: typing.Any) -> None:
        """
        Initializes a new instance of the DateRules helper class
        
        :param securities: The security manager
        :param timeZone: The algorithm's default time zone
        """
        ...

    @overload
    def Every(self, day: System.DayOfWeek) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on each of the specified days of week
        
        :param day: The day the event should fire
        :returns: A date rule that fires on every specified day of week.
        """
        ...

    @overload
    def Every(self, *days: System.DayOfWeek) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on each of the specified days of week
        
        :param days: The days the event should fire
        :returns: A date rule that fires on every specified day of week.
        """
        ...

    @overload
    def EveryDay(self) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire every day
        
        :returns: A date rule that fires every day.
        """
        ...

    @overload
    def EveryDay(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire every day the symbol is trading
        
        :param symbol: The symbol whose exchange is used to determine tradable dates
        :returns: A date rule that fires every day the specified symbol trades.
        """
        ...

    @overload
    def MonthEnd(self, daysOffset: int = 0) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on the last of each month
        
        :param daysOffset: The amount of days to offset the schedule by; must be between 0 and 30
        :returns: A date rule that fires on the last of each month - offset.
        """
        ...

    @overload
    def MonthEnd(self, symbol: typing.Union[QuantConnect.Symbol, str], daysOffset: int = 0) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on the last tradable date - offset for the specified symbol of each month
        
        :param symbol: The symbol whose exchange is used to determine the last tradable date of the month
        :param daysOffset: The amount of tradable days to offset the schedule by; must be between 0 and 30.
        :returns: A date rule that fires on the last tradable date - offset for the specified security each month.
        """
        ...

    @overload
    def MonthStart(self, daysOffset: int = 0) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on the first of each month + offset
        
        :param daysOffset: The amount of days to offset the schedule by; must be between 0 and 30.
        :returns: A date rule that fires on the first of each month + offset.
        """
        ...

    @overload
    def MonthStart(self, symbol: typing.Union[QuantConnect.Symbol, str], daysOffset: int = 0) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on the first tradable date + offset for the specified symbol of each month
        
        :param symbol: The symbol whose exchange is used to determine the first tradable date of the month
        :param daysOffset: The amount of tradable days to offset the schedule by; must be between 0 and 30
        :returns: A date rule that fires on the first tradable date + offset for the specified security each month.
        """
        ...

    @overload
    def On(self, year: int, month: int, day: int) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire only on the specified day
        
        :param year: The year
        :param month: The month
        :param day: The day
        """
        ...

    @overload
    def On(self, *dates: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire only on the specified days
        
        :param dates: The dates the event should fire
        """
        ...

    def SetDefaultTimeZone(self, timeZone: typing.Any) -> None:
        """
        Sets the default time zone
        
        :param timeZone: The time zone to use for helper methods that can't resolve a time zone
        """
        ...

    @overload
    def WeekEnd(self, daysOffset: int = 0) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on Friday - offset
        
        :param daysOffset: The amount of days to offset Friday by; must be between 0 and 6
        :returns: A date rule that fires on Friday each week.
        """
        ...

    @overload
    def WeekEnd(self, symbol: typing.Union[QuantConnect.Symbol, str], daysOffset: int = 0) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on the last - offset tradable date for the specified
        symbol of each week
        
        :param symbol: The symbol whose exchange is used to determine the last tradable date of the week
        :param daysOffset: The amount of tradable days to offset the last tradable day by each week
        :returns: A date rule that fires on the last - offset tradable date for the specified security each week.
        """
        ...

    @overload
    def WeekStart(self, daysOffset: int = 0) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on Monday + offset each week
        
        :param daysOffset: The amount of days to offset monday by; must be between 0 and 6
        :returns: A date rule that fires on Monday + offset each week.
        """
        ...

    @overload
    def WeekStart(self, symbol: typing.Union[QuantConnect.Symbol, str], daysOffset: int = 0) -> QuantConnect.Scheduling.IDateRule:
        """
        Specifies an event should fire on the first tradable date + offset for the specified
        symbol each week
        
        :param symbol: The symbol whose exchange is used to determine the first tradeable date of the week
        :param daysOffset: The amount of tradable days to offset the first tradable day by
        :returns: A date rule that fires on the first + offset tradable date for the specified security each week.
        """
        ...


class TimeConsumer(System.Object):
    """Represents a timer consumer instance"""

    @property
    def Finished(self) -> bool:
        """True if the consumer already finished it's work and no longer consumes time"""
        ...

    @Finished.setter
    def Finished(self, value: bool):
        """True if the consumer already finished it's work and no longer consumes time"""
        ...

    @property
    def TimeProvider(self) -> QuantConnect.ITimeProvider:
        """The time provider associated with this consumer"""
        ...

    @TimeProvider.setter
    def TimeProvider(self, value: QuantConnect.ITimeProvider):
        """The time provider associated with this consumer"""
        ...

    @property
    def IsolatorLimitProvider(self) -> QuantConnect.IIsolatorLimitResultProvider:
        """The isolator limit provider to be used with this consumer"""
        ...

    @IsolatorLimitProvider.setter
    def IsolatorLimitProvider(self, value: QuantConnect.IIsolatorLimitResultProvider):
        """The isolator limit provider to be used with this consumer"""
        ...

    @property
    def NextTimeRequest(self) -> typing.Optional[datetime.datetime]:
        """
        The next time, base on the TimeProvider, that time should be requested
        to be IsolatorLimitProvider
        """
        ...

    @NextTimeRequest.setter
    def NextTimeRequest(self, value: typing.Optional[datetime.datetime]):
        """
        The next time, base on the TimeProvider, that time should be requested
        to be IsolatorLimitProvider
        """
        ...


class TimeMonitor(System.Object, System.IDisposable):
    """
    Helper class that will monitor timer consumers and request more time if required.
    Used by IsolatorLimitResultProvider
    """

    @property
    def TimeConsumers(self) -> System.Collections.Generic.List[QuantConnect.Scheduling.TimeConsumer]:
        """
        List to store the coming TimeConsumer objects
        
        This field is protected.
        """
        ...

    @property
    def Count(self) -> int:
        """Returns the number of time consumers currently being monitored"""
        ...

    def __init__(self, monitorIntervalMs: int = 100) -> None:
        """Creates a new instance"""
        ...

    def Add(self, consumer: QuantConnect.Scheduling.TimeConsumer) -> None:
        """
        Adds a new time consumer element to be monitored
        
        :param consumer: Time consumer instance
        """
        ...

    def Dispose(self) -> None:
        """Disposes of the inner timer"""
        ...

    def ProcessConsumer(self, consumer: QuantConnect.Scheduling.TimeConsumer) -> None:
        """
        Process the TimeConsumer object in TimeConsumers list
        
        This method is protected.
        
        :param consumer: The TimeConsumer object to be processed
        """
        ...

    def RemoveAll(self) -> None:
        """
        Remove all TimeConsumer objects where the `Finished` field is marked as true
        
        This method is protected.
        """
        ...


class ScheduledEventException(System.Exception):
    """Throw this if there is an exception in the callback function of the scheduled event"""

    @property
    def ScheduledEventName(self) -> str:
        """Gets the name of the scheduled event"""
        ...

    def __init__(self, name: str, message: str, innerException: System.Exception) -> None:
        """
        ScheduledEventException constructor
        
        :param name: The name of the scheduled event
        :param message: The exception as a string
        :param innerException: The exception that is the cause of the current exception
        """
        ...


class ScheduledEvent(System.Object, System.IDisposable):
    """Real time self scheduling event"""

    SecurityEndOfDayDelta: datetime.timedelta = ...
    """Gets the default time before market close end of trading day events will fire"""

    AlgorithmEndOfDayDelta: datetime.timedelta = ...
    """Gets the default time before midnight end of day events will fire"""

    @property
    def EventFired(self) -> _EventContainer[typing.Callable[[str, datetime.datetime], None], None]:
        """Event that fires each time this scheduled event happens"""
        ...

    @EventFired.setter
    def EventFired(self, value: _EventContainer[typing.Callable[[str, datetime.datetime], None], None]):
        """Event that fires each time this scheduled event happens"""
        ...

    @property
    def Enabled(self) -> bool:
        """Gets or sets whether this event is enabled"""
        ...

    @Enabled.setter
    def Enabled(self, value: bool):
        """Gets or sets whether this event is enabled"""
        ...

    @property
    def IsLoggingEnabled(self) -> bool:
        """Gets or sets whether this event will log each time it fires"""
        ...

    @IsLoggingEnabled.setter
    def IsLoggingEnabled(self, value: bool):
        """Gets or sets whether this event will log each time it fires"""
        ...

    @property
    def NextEventUtcTime(self) -> datetime.datetime:
        """Gets the next time this scheduled event will fire in UTC"""
        ...

    @property
    def Name(self) -> str:
        """Gets an identifier for this event"""
        ...

    @overload
    def __init__(self, name: str, eventUtcTime: typing.Union[datetime.datetime, datetime.date], callback: typing.Callable[[str, datetime.datetime], None] = None) -> None:
        """
        Initializes a new instance of the ScheduledEvent class
        
        :param name: An identifier for this event
        :param eventUtcTime: The date time the event should fire
        :param callback: Delegate to be called when the event time passes
        """
        ...

    @overload
    def __init__(self, name: str, orderedEventUtcTimes: System.Collections.Generic.IEnumerable[datetime.datetime], callback: typing.Callable[[str, datetime.datetime], None] = None) -> None:
        """
        Initializes a new instance of the ScheduledEvent class
        
        :param name: An identifier for this event
        :param orderedEventUtcTimes: An enumerable that emits event times
        :param callback: Delegate to be called each time an event passes
        """
        ...

    @overload
    def __init__(self, name: str, orderedEventUtcTimes: System.Collections.Generic.IEnumerator[datetime.datetime], callback: typing.Callable[[str, datetime.datetime], None] = None) -> None:
        """
        Initializes a new instance of the ScheduledEvent class
        
        :param name: An identifier for this event
        :param orderedEventUtcTimes: An enumerator that emits event times
        :param callback: Delegate to be called each time an event passes
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

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

    def OnEventFired(self, triggerTime: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Event invocator for the EventFired event
        
        This method is protected.
        
        :param triggerTime: The event's time in UTC
        """
        ...

    def ToString(self) -> str:
        """Will return the ScheduledEvents name"""
        ...


class ITimeRule(metaclass=abc.ABCMeta):
    """Specifies times times on dates for events, used in conjunction with IDateRule"""

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        """Gets a name for this rule"""
        ...

    def CreateUtcEventTimes(self, dates: System.Collections.Generic.IEnumerable[datetime.datetime]) -> System.Collections.Generic.IEnumerable[datetime.datetime]:
        """
        Creates the event times for the specified dates in UTC
        
        :param dates: The dates to apply times to
        :returns: An enumerable of date times that is the result of applying this rule to the specified dates.
        """
        ...


class TimeRules(System.Object):
    """Helper class used to provide better syntax when defining time rules"""

    @property
    def Now(self) -> QuantConnect.Scheduling.ITimeRule:
        """Specifies an event should fire at the current time"""
        ...

    @property
    def Midnight(self) -> QuantConnect.Scheduling.ITimeRule:
        """Convenience property for running a scheduled event at midnight in the algorithm time zone"""
        ...

    @property
    def Noon(self) -> QuantConnect.Scheduling.ITimeRule:
        """Convenience property for running a scheduled event at noon in the algorithm time zone"""
        ...

    def __init__(self, securities: QuantConnect.Securities.SecurityManager, timeZone: typing.Any) -> None:
        """
        Initializes a new instance of the TimeRules helper class
        
        :param securities: The security manager
        :param timeZone: The algorithm's default time zone
        """
        ...

    def AfterMarketOpen(self, symbol: typing.Union[QuantConnect.Symbol, str], minutesAfterOpen: float = 0, extendedMarketOpen: bool = False) -> QuantConnect.Scheduling.ITimeRule:
        """
        Specifies an event should fire at market open +-
        
        :param symbol: The symbol whose market open we want an event for
        :param minutesAfterOpen: The minutes after market open that the event should fire
        :param extendedMarketOpen: True to use extended market open, false to use regular market open
        :returns: A time rule that fires the specified number of minutes after the symbol's market open.
        """
        ...

    @overload
    def At(self, timeOfDay: datetime.timedelta) -> QuantConnect.Scheduling.ITimeRule:
        """
        Specifies an event should fire at the specified time of day in the algorithm's time zone
        
        :param timeOfDay: The time of day in the algorithm's time zone the event should fire
        :returns: A time rule that fires at the specified time in the algorithm's time zone.
        """
        ...

    @overload
    def At(self, hour: int, minute: int, second: int = 0) -> QuantConnect.Scheduling.ITimeRule:
        """
        Specifies an event should fire at the specified time of day in the algorithm's time zone
        
        :param hour: The hour
        :param minute: The minute
        :param second: The second
        :returns: A time rule that fires at the specified time in the algorithm's time zone.
        """
        ...

    @overload
    def At(self, hour: int, minute: int, timeZone: typing.Any) -> QuantConnect.Scheduling.ITimeRule:
        """
        Specifies an event should fire at the specified time of day in the specified time zone
        
        :param hour: The hour
        :param minute: The minute
        :param timeZone: The time zone the event time is represented in
        :returns: A time rule that fires at the specified time in the algorithm's time zone.
        """
        ...

    @overload
    def At(self, hour: int, minute: int, second: int, timeZone: typing.Any) -> QuantConnect.Scheduling.ITimeRule:
        """
        Specifies an event should fire at the specified time of day in the specified time zone
        
        :param hour: The hour
        :param minute: The minute
        :param second: The second
        :param timeZone: The time zone the event time is represented in
        :returns: A time rule that fires at the specified time in the algorithm's time zone.
        """
        ...

    @overload
    def At(self, timeOfDay: datetime.timedelta, timeZone: typing.Any) -> QuantConnect.Scheduling.ITimeRule:
        """
        Specifies an event should fire at the specified time of day in the specified time zone
        
        :param timeOfDay: The time of day in the algorithm's time zone the event should fire
        :param timeZone: The time zone the date time is expressed in
        :returns: A time rule that fires at the specified time in the algorithm's time zone.
        """
        ...

    def BeforeMarketClose(self, symbol: typing.Union[QuantConnect.Symbol, str], minutesBeforeClose: float = 0, extendedMarketClose: bool = False) -> QuantConnect.Scheduling.ITimeRule:
        """
        Specifies an event should fire at the market close +-
        
        :param symbol: The symbol whose market close we want an event for
        :param minutesBeforeClose: The time before market close that the event should fire
        :param extendedMarketClose: True to use extended market close, false to use regular market close
        :returns: A time rule that fires the specified number of minutes before the symbol's market close.
        """
        ...

    def Every(self, interval: datetime.timedelta) -> QuantConnect.Scheduling.ITimeRule:
        """
        Specifies an event should fire periodically on the requested interval
        
        :param interval: The frequency with which the event should fire, can not be zero or less
        :returns: A time rule that fires after each interval passes.
        """
        ...

    def SetDefaultTimeZone(self, timeZone: typing.Any) -> None:
        """
        Sets the default time zone
        
        :param timeZone: The time zone to use for helper methods that can't resolve a time zone
        """
        ...


class IEventSchedule(metaclass=abc.ABCMeta):
    """Provides the ability to add/remove scheduled events from the real time handler"""

    def Add(self, scheduledEvent: QuantConnect.Scheduling.ScheduledEvent) -> None:
        """
        Adds the specified event to the schedule
        
        :param scheduledEvent: The event to be scheduled, including the date/times the event fires and the callback
        """
        ...

    def Remove(self, scheduledEvent: QuantConnect.Scheduling.ScheduledEvent) -> None:
        """
        Removes the specified event from the schedule
        
        :param scheduledEvent: The event to be removed
        """
        ...


class IFluentSchedulingRunnable(QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier, metaclass=abc.ABCMeta):
    """Specifies the callback component of a scheduled event, as well as final filters"""

    def DuringMarketHours(self, symbol: typing.Union[QuantConnect.Symbol, str], extendedMarket: bool = False) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Filters the event times to only include times where the symbol's market is considered open"""
        ...

    @overload
    def Run(self, callback: typing.Callable[[], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """Register the defined event with the callback"""
        ...

    @overload
    def Run(self, callback: typing.Callable[[datetime.datetime], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """Register the defined event with the callback"""
        ...

    @overload
    def Run(self, callback: typing.Callable[[str, datetime.datetime], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """Register the defined event with the callback"""
        ...

    def Where(self, predicate: typing.Callable[[datetime.datetime], bool]) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Filters the event times using the predicate"""
        ...


class IFluentSchedulingTimeSpecifier(metaclass=abc.ABCMeta):
    """Specifies the time rule component of a scheduled event"""

    def AfterMarketOpen(self, symbol: typing.Union[QuantConnect.Symbol, str], minutesAfterOpen: float = 0, extendedMarketOpen: bool = False) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Creates events that fire a specified number of minutes after market open"""
        ...

    @overload
    def At(self, hour: int, minute: int, second: int = 0) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Creates events that fire at the specified time of day in the specified time zone"""
        ...

    @overload
    def At(self, hour: int, minute: int, timeZone: typing.Any) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Creates events that fire at the specified time of day in the specified time zone"""
        ...

    @overload
    def At(self, hour: int, minute: int, second: int, timeZone: typing.Any) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Creates events that fire at the specified time of day in the specified time zone"""
        ...

    @overload
    def At(self, timeOfDay: datetime.timedelta, timeZone: typing.Any) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Creates events that fire at the specified time of day in the specified time zone"""
        ...

    @overload
    def At(self, timeOfDay: datetime.timedelta) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Creates events that fire at the specific time of day in the algorithm's time zone"""
        ...

    def BeforeMarketClose(self, symbol: typing.Union[QuantConnect.Symbol, str], minuteBeforeClose: float = 0, extendedMarketClose: bool = False) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Creates events that fire a specified numer of minutes before market close"""
        ...

    def Every(self, interval: datetime.timedelta) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Creates events that fire on a period define by the specified interval"""
        ...

    def Where(self, predicate: typing.Callable[[datetime.datetime], bool]) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Filters the event times using the predicate"""
        ...


class IFluentSchedulingDateSpecifier(metaclass=abc.ABCMeta):
    """Specifies the date rule component of a scheduled event"""

    def Every(self, *days: System.DayOfWeek) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Creates events on each of the specified day of week"""
        ...

    @overload
    def EveryDay(self) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Creates events on every day of the year"""
        ...

    @overload
    def EveryDay(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Creates events on every trading day of the year for the symbol"""
        ...

    @overload
    def MonthStart(self) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Creates events on the first day of the month"""
        ...

    @overload
    def MonthStart(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Creates events on the first trading day of the month"""
        ...

    @overload
    def On(self, year: int, month: int, day: int) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Creates events only on the specified date"""
        ...

    @overload
    def On(self, *dates: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Creates events only on the specified dates"""
        ...

    def Where(self, predicate: typing.Callable[[datetime.datetime], bool]) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Filters the event times using the predicate"""
        ...


class ScheduleManager(System.Object, QuantConnect.Scheduling.IEventSchedule):
    """Provides access to the real time handler's event scheduling feature"""

    @property
    def DateRules(self) -> QuantConnect.Scheduling.DateRules:
        """Gets the date rules helper object to make specifying dates for events easier"""
        ...

    @property
    def TimeRules(self) -> QuantConnect.Scheduling.TimeRules:
        """Gets the time rules helper object to make specifying times for events easier"""
        ...

    def __init__(self, securities: QuantConnect.Securities.SecurityManager, timeZone: typing.Any) -> None:
        """
        Initializes a new instance of the ScheduleManager class
        
        :param securities: Securities manager containing the algorithm's securities
        :param timeZone: The algorithm's time zone
        """
        ...

    def Add(self, scheduledEvent: QuantConnect.Scheduling.ScheduledEvent) -> None:
        """
        Adds the specified event to the schedule
        
        :param scheduledEvent: The event to be scheduled, including the date/times the event fires and the callback
        """
        ...

    @overload
    def Event(self) -> QuantConnect.Scheduling.IFluentSchedulingDateSpecifier:
        ...

    @overload
    def Event(self, name: str) -> QuantConnect.Scheduling.IFluentSchedulingDateSpecifier:
        """Entry point for the fluent scheduled event builder"""
        ...

    @overload
    def On(self, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, callback: typing.Callable[[], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Schedules the callback to run using the specified date and time rules
        
        :param dateRule: Specifies what dates the event should run
        :param timeRule: Specifies the times on those dates the event should run
        :param callback: The callback to be invoked
        """
        ...

    @overload
    def On(self, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, callback: typing.Any) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Schedules the callback to run using the specified date and time rules
        
        :param dateRule: Specifies what dates the event should run
        :param timeRule: Specifies the times on those dates the event should run
        :param callback: The callback to be invoked
        """
        ...

    @overload
    def On(self, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, callback: typing.Callable[[str, datetime.datetime], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Schedules the callback to run using the specified date and time rules
        
        :param dateRule: Specifies what dates the event should run
        :param timeRule: Specifies the times on those dates the event should run
        :param callback: The callback to be invoked
        """
        ...

    @overload
    def On(self, name: str, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, callback: typing.Callable[[], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Schedules the callback to run using the specified date and time rules
        
        :param name: The event's unique name
        :param dateRule: Specifies what dates the event should run
        :param timeRule: Specifies the times on those dates the event should run
        :param callback: The callback to be invoked
        """
        ...

    @overload
    def On(self, name: str, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, callback: typing.Any) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Schedules the callback to run using the specified date and time rules
        
        :param name: The event's unique name
        :param dateRule: Specifies what dates the event should run
        :param timeRule: Specifies the times on those dates the event should run
        :param callback: The callback to be invoked
        """
        ...

    @overload
    def On(self, name: str, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, callback: typing.Callable[[str, datetime.datetime], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Schedules the callback to run using the specified date and time rules
        
        :param name: The event's unique name
        :param dateRule: Specifies what dates the event should run
        :param timeRule: Specifies the times on those dates the event should run
        :param callback: The callback to be invoked
        """
        ...

    def Remove(self, scheduledEvent: QuantConnect.Scheduling.ScheduledEvent) -> None:
        """
        Removes the specified event from the schedule
        
        :param scheduledEvent: The event to be removed
        """
        ...

    @overload
    def Training(self, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, trainingCode: typing.Callable[[], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Schedules the training code to run using the specified date and time rules
        
        :param dateRule: Specifies what dates the event should run
        :param timeRule: Specifies the times on those dates the event should run
        :param trainingCode: The training code to be invoked
        """
        ...

    @overload
    def Training(self, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, trainingCode: typing.Any) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Schedules the training code to run using the specified date and time rules
        
        :param dateRule: Specifies what dates the event should run
        :param timeRule: Specifies the times on those dates the event should run
        :param trainingCode: The training code to be invoked
        """
        ...

    @overload
    def Training(self, dateRule: QuantConnect.Scheduling.IDateRule, timeRule: QuantConnect.Scheduling.ITimeRule, trainingCode: typing.Callable[[datetime.datetime], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Schedules the training code to run using the specified date and time rules
        
        :param dateRule: Specifies what dates the event should run
        :param timeRule: Specifies the times on those dates the event should run
        :param trainingCode: The training code to be invoked
        """
        ...

    @overload
    def TrainingNow(self, trainingCode: typing.Callable[[], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        ...

    @overload
    def TrainingNow(self, trainingCode: typing.Any) -> QuantConnect.Scheduling.ScheduledEvent:
        """Schedules the provided training code to execute immediately"""
        ...


class FluentScheduledEventBuilder(System.Object, QuantConnect.Scheduling.IFluentSchedulingDateSpecifier, QuantConnect.Scheduling.IFluentSchedulingRunnable):
    """Provides a builder class to allow for fluent syntax when constructing new events"""

    def __init__(self, schedule: QuantConnect.Scheduling.ScheduleManager, securities: QuantConnect.Securities.SecurityManager, name: str = None) -> None:
        """
        Initializes a new instance of the FluentScheduledEventBuilder class
        
        :param schedule: The schedule to send created events to
        :param securities: The algorithm's security manager
        :param name: A specific name for this event
        """
        ...

    def AfterMarketOpen(self, symbol: typing.Union[QuantConnect.Symbol, str], minutesAfterOpen: float, extendedMarketOpen: bool) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Creates events that fire a specified number of minutes after market open"""
        ...

    @overload
    def At(self, timeOfDay: datetime.timedelta) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Creates events that fire at the specific time of day in the algorithm's time zone"""
        ...

    @overload
    def At(self, hour: int, minute: int, second: int) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        ...

    @overload
    def At(self, hour: int, minute: int, timeZone: typing.Any) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        ...

    @overload
    def At(self, hour: int, minute: int, second: int, timeZone: typing.Any) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        ...

    @overload
    def At(self, timeOfDay: datetime.timedelta, timeZone: typing.Any) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        ...

    def BeforeMarketClose(self, symbol: typing.Union[QuantConnect.Symbol, str], minuteBeforeClose: float, extendedMarketClose: bool) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Creates events that fire a specified numer of minutes before market close"""
        ...

    def DuringMarketHours(self, symbol: typing.Union[QuantConnect.Symbol, str], extendedMarket: bool) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Filters the event times to only include times where the symbol's market is considered open"""
        ...

    @overload
    def Every(self, *days: System.DayOfWeek) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        ...

    @overload
    def Every(self, interval: datetime.timedelta) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Creates events that fire on a period define by the specified interval"""
        ...

    @overload
    def EveryDay(self) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Creates events on every day of the year"""
        ...

    @overload
    def EveryDay(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Creates events on every trading day of the year for the symbol"""
        ...

    @overload
    def MonthStart(self) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Creates events on the first day of the month"""
        ...

    @overload
    def MonthStart(self, symbol: typing.Union[QuantConnect.Symbol, str]) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Creates events on the first trading day of the month"""
        ...

    @overload
    def On(self, year: int, month: int, day: int) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        ...

    @overload
    def On(self, *dates: typing.Union[datetime.datetime, datetime.date]) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        ...

    @overload
    def Run(self, callback: typing.Callable[[], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """Register the defined event with the callback"""
        ...

    @overload
    def Run(self, callback: typing.Callable[[datetime.datetime], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """Register the defined event with the callback"""
        ...

    @overload
    def Run(self, callback: typing.Callable[[str, datetime.datetime], None]) -> QuantConnect.Scheduling.ScheduledEvent:
        """Register the defined event with the callback"""
        ...

    @overload
    def Where(self, predicate: typing.Callable[[datetime.datetime], bool]) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Filters the event times using the predicate"""
        ...

    @overload
    def Where(self, predicate: typing.Callable[[datetime.datetime], bool]) -> QuantConnect.Scheduling.IFluentSchedulingTimeSpecifier:
        """Filters the event times using the predicate"""
        ...

    @overload
    def Where(self, predicate: typing.Callable[[datetime.datetime], bool]) -> QuantConnect.Scheduling.IFluentSchedulingRunnable:
        """Filters the event times using the predicate"""
        ...


class FuncDateRule(System.Object, QuantConnect.Scheduling.IDateRule):
    """Uses a function to define an enumerable of dates over a requested start/end period"""

    @property
    def Name(self) -> str:
        """Gets a name for this rule"""
        ...

    @Name.setter
    def Name(self, value: str):
        """Gets a name for this rule"""
        ...

    def __init__(self, name: str, getDatesFunction: typing.Callable[[datetime.datetime, datetime.datetime], System.Collections.Generic.IEnumerable[datetime.datetime]]) -> None:
        """
        Initializes a new instance of the FuncDateRule class
        
        :param name: The name of this rule
        :param getDatesFunction: The time applicator function
        """
        ...

    def GetDates(self, start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date]) -> System.Collections.Generic.IEnumerable[datetime.datetime]:
        """
        Gets the dates produced by this date rule between the specified times
        
        :param start: The start of the interval to produce dates for
        :param end: The end of the interval to produce dates for
        :returns: All dates in the interval matching this date rule.
        """
        ...


class CompositeTimeRule(System.Object, QuantConnect.Scheduling.ITimeRule):
    """Combines multiple time rules into a single rule that emits for each rule"""

    @property
    def Rules(self) -> System.Collections.Generic.IReadOnlyList[QuantConnect.Scheduling.ITimeRule]:
        """Gets the individual rules for this composite rule"""
        ...

    @property
    def Name(self) -> str:
        """Gets a name for this rule"""
        ...

    @overload
    def __init__(self, *timeRules: QuantConnect.Scheduling.ITimeRule) -> None:
        """
        Initializes a new instance of the CompositeTimeRule class
        
        :param timeRules: The time rules to compose
        """
        ...

    @overload
    def __init__(self, timeRules: System.Collections.Generic.IEnumerable[QuantConnect.Scheduling.ITimeRule]) -> None:
        """
        Initializes a new instance of the CompositeTimeRule class
        
        :param timeRules: The time rules to compose
        """
        ...

    def CreateUtcEventTimes(self, dates: System.Collections.Generic.IEnumerable[datetime.datetime]) -> System.Collections.Generic.IEnumerable[datetime.datetime]:
        """
        Creates the event times for the specified dates in UTC
        
        :param dates: The dates to apply times to
        :returns: An enumerable of date times that is the result of applying this rule to the specified dates.
        """
        ...


class FuncTimeRule(System.Object, QuantConnect.Scheduling.ITimeRule):
    """Uses a function to define a time rule as a projection of date times to date times"""

    @property
    def Name(self) -> str:
        """Gets a name for this rule"""
        ...

    @Name.setter
    def Name(self, value: str):
        """Gets a name for this rule"""
        ...

    def __init__(self, name: str, createUtcEventTimesFunction: typing.Callable[[System.Collections.Generic.IEnumerable[datetime.datetime]], System.Collections.Generic.IEnumerable[datetime.datetime]]) -> None:
        """
        Initializes a new instance of the FuncTimeRule class
        
        :param name: The name of the time rule
        :param createUtcEventTimesFunction: Function used to transform dates into event date times
        """
        ...

    def CreateUtcEventTimes(self, dates: System.Collections.Generic.IEnumerable[datetime.datetime]) -> System.Collections.Generic.IEnumerable[datetime.datetime]:
        """
        Creates the event times for the specified dates in UTC
        
        :param dates: The dates to apply times to
        :returns: An enumerable of date times that is the result of applying this rule to the specified dates.
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Scheduling__EventContainer_Callable, QuantConnect_Scheduling__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Scheduling__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Scheduling__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Scheduling__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


