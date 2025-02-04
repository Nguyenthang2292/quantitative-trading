from typing import overload
import abc
import datetime
import typing
import warnings

import QuantConnect
import QuantConnect.Data.UniverseSelection
import QuantConnect.Interfaces
import QuantConnect.Lean.Engine.RealTime
import QuantConnect.Lean.Engine.Results
import QuantConnect.Packets
import QuantConnect.Scheduling
import QuantConnect.Securities
import System
import System.Collections.Concurrent
import System.Collections.Generic


class IRealTimeHandler(QuantConnect.Scheduling.IEventSchedule, metaclass=abc.ABCMeta):
    """Real time event handler, trigger functions at regular or pretimed intervals"""

    @property
    @abc.abstractmethod
    def IsActive(self) -> bool:
        """Thread status flag."""
        ...

    def Exit(self) -> None:
        """Trigger and exit signal to terminate real time event scanner."""
        ...

    def OnSecuritiesChanged(self, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """Event fired each time that we add/remove securities from the data feed"""
        ...

    def ScanPastEvents(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scan for past events that didn't fire because there was no data at the scheduled time.
        
        :param time: Current time.
        """
        ...

    def SetTime(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Set the current time for the event scanner (so we can use same code for backtesting and live events)
        
        :param time: Current real or backtest time.
        """
        ...

    def Setup(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.AlgorithmNodePacket, resultHandler: QuantConnect.Lean.Engine.Results.IResultHandler, api: QuantConnect.Interfaces.IApi, isolatorLimitProvider: QuantConnect.IIsolatorLimitResultProvider) -> None:
        """Initializes the real time handler for the specified algorithm and job"""
        ...


class BaseRealTimeHandler(System.Object, QuantConnect.Lean.Engine.RealTime.IRealTimeHandler, metaclass=abc.ABCMeta):
    """
    Base class for the real time handler LiveTradingRealTimeHandler
    and BacktestingRealTimeHandler implementations
    """

    @property
    @abc.abstractmethod
    def IsActive(self) -> bool:
        """Thread status flag."""
        ...

    @IsActive.setter
    @abc.abstractmethod
    def IsActive(self, value: bool):
        """Thread status flag."""
        ...

    @property
    def ScheduledEvents(self) -> System.Collections.Concurrent.ConcurrentDictionary[QuantConnect.Scheduling.ScheduledEvent, int]:
        """
        The scheduled events container
        
        This property is protected.
        """
        ...

    @property
    def IsolatorLimitProvider(self) -> QuantConnect.IIsolatorLimitResultProvider:
        """
        The isolator limit result provider instance
        
        This property is protected.
        """
        ...

    @IsolatorLimitProvider.setter
    def IsolatorLimitProvider(self, value: QuantConnect.IIsolatorLimitResultProvider):
        """
        The isolator limit result provider instance
        
        This property is protected.
        """
        ...

    @property
    def Algorithm(self) -> QuantConnect.Interfaces.IAlgorithm:
        """
        The algorithm instance
        
        This property is protected.
        """
        ...

    @Algorithm.setter
    def Algorithm(self, value: QuantConnect.Interfaces.IAlgorithm):
        """
        The algorithm instance
        
        This property is protected.
        """
        ...

    @property
    def TimeMonitor(self) -> QuantConnect.Scheduling.TimeMonitor:
        """
        The time monitor instance to use
        
        This property is protected.
        """
        ...

    @TimeMonitor.setter
    def TimeMonitor(self, value: QuantConnect.Scheduling.TimeMonitor):
        """
        The time monitor instance to use
        
        This property is protected.
        """
        ...

    def Add(self, scheduledEvent: QuantConnect.Scheduling.ScheduledEvent) -> None:
        """
        Adds the specified event to the schedule
        
        :param scheduledEvent: The event to be scheduled, including the date/times the event fires and the callback
        """
        ...

    def Exit(self) -> None:
        """Stop the real time thread"""
        ...

    def GetScheduledEventUniqueId(self) -> int:
        """
        Gets a new scheduled event unique id
        
        This method is protected.
        """
        ...

    def GetTimeMonitorTimeout(self) -> int:
        """
        Get's the timeout the scheduled task time monitor should use
        
        This method is protected.
        """
        ...

    def OnSecuritiesChanged(self, changes: QuantConnect.Data.UniverseSelection.SecurityChanges) -> None:
        """Event fired each time that we add/remove securities from the data feed"""
        ...

    def Remove(self, scheduledEvent: QuantConnect.Scheduling.ScheduledEvent) -> None:
        """
        Removes the specified event from the schedule
        
        :param scheduledEvent: The event to be removed
        """
        ...

    def ScanPastEvents(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scan for past events that didn't fire because there was no data at the scheduled time.
        
        :param time: Current time.
        """
        ...

    def SetTime(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Set the current time for the event scanner (so we can use same code for backtesting and live events)
        
        :param time: Current real or backtest time.
        """
        ...

    def Setup(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.AlgorithmNodePacket, resultHandler: QuantConnect.Lean.Engine.Results.IResultHandler, api: QuantConnect.Interfaces.IApi, isolatorLimitProvider: QuantConnect.IIsolatorLimitResultProvider) -> None:
        """
        Initializes the real time handler for the specified algorithm and job.
        Adds EndOfDayEvents
        """
        ...


class BacktestingRealTimeHandler(QuantConnect.Lean.Engine.RealTime.BaseRealTimeHandler):
    """Pseudo realtime event processing for backtesting to simulate realtime events in fast forward."""

    @property
    def IsActive(self) -> bool:
        """
        Flag indicating the hander thread is completely finished and ready to dispose.
        this doesn't run as its own thread
        """
        ...

    @IsActive.setter
    def IsActive(self, value: bool):
        """
        Flag indicating the hander thread is completely finished and ready to dispose.
        this doesn't run as its own thread
        """
        ...

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

    def ScanPastEvents(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scan for past events that didn't fire because there was no data at the scheduled time.
        
        :param time: Current time.
        """
        ...

    def SetTime(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Set the time for the realtime event handler.
        
        :param time: Current time.
        """
        ...

    def Setup(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.AlgorithmNodePacket, resultHandler: QuantConnect.Lean.Engine.Results.IResultHandler, api: QuantConnect.Interfaces.IApi, isolatorLimitProvider: QuantConnect.IIsolatorLimitResultProvider) -> None:
        """Initializes the real time handler for the specified algorithm and job"""
        ...

    @staticmethod
    def SortFirstElement(scheduledEvents: System.Collections.Generic.IList[QuantConnect.Scheduling.ScheduledEvent]) -> None:
        """
        Sorts the first element of the provided list and supposes the rest of the collection is sorted.
        Supposes the collection has at least 1 element
        """
        ...


class ScheduledEventFactory(System.Object):
    """Provides methods for creating common scheduled events"""

    @staticmethod
    def CreateEventName(scope: str, name: str) -> str:
        """
        Defines the format of event names generated by this system.
        
        :param scope: The scope of the event, example, 'Algorithm' or 'Security'
        :param name: A name for this specified event in this scope, example, 'EndOfDay'
        :returns: A string representing a fully scoped event name.
        """
        ...

    @staticmethod
    def EveryAlgorithmEndOfDay(algorithm: QuantConnect.Interfaces.IAlgorithm, resultHandler: QuantConnect.Lean.Engine.Results.IResultHandler, start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date], endOfDayDelta: datetime.timedelta, currentUtcTime: typing.Optional[datetime.datetime] = None) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Creates a new ScheduledEvent that will fire before market close by the specified time
        
        This method is deprecated. It will generate ScheduledEvents for the deprecated IAlgorithm.OnEndOfDay()
        
        :param algorithm: The algorithm instance the event is fo
        :param resultHandler: The result handler, used to communicate run time errors
        :param start: The date to start the events
        :param end: The date to end the events
        :param endOfDayDelta: The time difference between the market close and the event, positive time will fire before market close
        :param currentUtcTime: Specfies the current time in UTC, before which, no events will be scheduled. Specify null to skip this filter.
        :returns: The new ScheduledEvent that will fire near market close each tradeable dat.
        """
        warnings.warn("This method is deprecated. It will generate ScheduledEvents for the deprecated IAlgorithm.OnEndOfDay()", DeprecationWarning)

    @staticmethod
    def EveryDayAt(name: str, dates: System.Collections.Generic.IEnumerable[datetime.datetime], timeOfDay: datetime.timedelta, callback: typing.Callable[[str, datetime.datetime], None], currentUtcTime: typing.Optional[datetime.datetime] = None) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Creates a new ScheduledEvent that will fire at the specified  for every day in
        
        :param name: An identifier for this event
        :param dates: The dates to set events for at the specified time. These act as a base time to which the  is added to, that is, the implementation does not use .Date before the addition
        :param timeOfDay: The time each tradeable date to fire the event
        :param callback: The delegate to call when an event fires
        :param currentUtcTime: Specfies the current time in UTC, before which, no events will be scheduled. Specify null to skip this filter.
        :returns: A new ScheduledEvent instance that fires events each tradeable day from the start to the finish at the specified time.
        """
        ...

    @staticmethod
    def EverySecurityEndOfDay(algorithm: QuantConnect.Interfaces.IAlgorithm, resultHandler: QuantConnect.Lean.Engine.Results.IResultHandler, security: QuantConnect.Securities.Security, start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date], endOfDayDelta: datetime.timedelta, currentUtcTime: typing.Optional[datetime.datetime] = None) -> QuantConnect.Scheduling.ScheduledEvent:
        """
        Creates a new ScheduledEvent that will fire before market close by the specified time
        
        :param algorithm: The algorithm instance the event is fo
        :param resultHandler: The result handler, used to communicate run time errors
        :param security: The security used for defining tradeable dates
        :param start: The first date for the events
        :param end: The date to end the events
        :param endOfDayDelta: The time difference between the market close and the event, positive time will fire before market close
        :param currentUtcTime: Specfies the current time in UTC, before which, no events will be scheduled. Specify null to skip this filter.
        :returns: The new ScheduledEvent that will fire near market close each tradeable dat.
        """
        ...


class LiveTradingRealTimeHandler(QuantConnect.Lean.Engine.RealTime.BacktestingRealTimeHandler):
    """Live trading realtime event processing."""

    @property
    def IsActive(self) -> bool:
        """Boolean flag indicating thread state."""
        ...

    @IsActive.setter
    def IsActive(self, value: bool):
        """Boolean flag indicating thread state."""
        ...

    def Exit(self) -> None:
        """Stop the real time thread"""
        ...

    def GetTimeMonitorTimeout(self) -> int:
        """
        Get's the timeout the scheduled task time monitor should use
        
        This method is protected.
        """
        ...

    def ScanPastEvents(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Scan for past events that didn't fire because there was no data at the scheduled time.
        
        :param time: Current time.
        """
        ...

    def SetTime(self, time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """Set the current time. If the date changes re-start the realtime event setup routines."""
        ...

    def Setup(self, algorithm: QuantConnect.Interfaces.IAlgorithm, job: QuantConnect.Packets.AlgorithmNodePacket, resultHandler: QuantConnect.Lean.Engine.Results.IResultHandler, api: QuantConnect.Interfaces.IApi, isolatorLimitProvider: QuantConnect.IIsolatorLimitResultProvider) -> None:
        """Initializes the real time handler for the specified algorithm and job"""
        ...


