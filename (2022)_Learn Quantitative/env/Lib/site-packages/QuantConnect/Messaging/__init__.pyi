from typing import overload
import typing

import QuantConnect.Interfaces
import QuantConnect.Messaging
import QuantConnect.Notifications
import QuantConnect.Packets
import System

QuantConnect_Messaging__EventContainer_Callable = typing.TypeVar("QuantConnect_Messaging__EventContainer_Callable")
QuantConnect_Messaging__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Messaging__EventContainer_ReturnType")


class EventMessagingHandler(System.Object, QuantConnect.Interfaces.IMessagingHandler):
    """Desktop implementation of messaging system for Lean Engine"""

    @property
    def HasSubscribers(self) -> bool:
        """
        Gets or sets whether this messaging handler has any current subscribers.
        When set to false, messages won't be sent.
        """
        ...

    @HasSubscribers.setter
    def HasSubscribers(self, value: bool):
        """
        Gets or sets whether this messaging handler has any current subscribers.
        When set to false, messages won't be sent.
        """
        ...

    @property
    def DebugEvent(self) -> _EventContainer[typing.Callable[[QuantConnect.Packets.DebugPacket], None], None]:
        ...

    @DebugEvent.setter
    def DebugEvent(self, value: _EventContainer[typing.Callable[[QuantConnect.Packets.DebugPacket], None], None]):
        ...

    @property
    def SystemDebugEvent(self) -> _EventContainer[typing.Callable[[QuantConnect.Packets.SystemDebugPacket], None], None]:
        ...

    @SystemDebugEvent.setter
    def SystemDebugEvent(self, value: _EventContainer[typing.Callable[[QuantConnect.Packets.SystemDebugPacket], None], None]):
        ...

    @property
    def LogEvent(self) -> _EventContainer[typing.Callable[[QuantConnect.Packets.LogPacket], None], None]:
        ...

    @LogEvent.setter
    def LogEvent(self, value: _EventContainer[typing.Callable[[QuantConnect.Packets.LogPacket], None], None]):
        ...

    @property
    def RuntimeErrorEvent(self) -> _EventContainer[typing.Callable[[QuantConnect.Packets.RuntimeErrorPacket], None], None]:
        ...

    @RuntimeErrorEvent.setter
    def RuntimeErrorEvent(self, value: _EventContainer[typing.Callable[[QuantConnect.Packets.RuntimeErrorPacket], None], None]):
        ...

    @property
    def HandledErrorEvent(self) -> _EventContainer[typing.Callable[[QuantConnect.Packets.HandledErrorPacket], None], None]:
        ...

    @HandledErrorEvent.setter
    def HandledErrorEvent(self, value: _EventContainer[typing.Callable[[QuantConnect.Packets.HandledErrorPacket], None], None]):
        ...

    @property
    def BacktestResultEvent(self) -> _EventContainer[typing.Callable[[QuantConnect.Packets.BacktestResultPacket], None], None]:
        ...

    @BacktestResultEvent.setter
    def BacktestResultEvent(self, value: _EventContainer[typing.Callable[[QuantConnect.Packets.BacktestResultPacket], None], None]):
        ...

    @property
    def ConsumerReadyEvent(self) -> _EventContainer[typing.Callable[[], None], None]:
        ...

    @ConsumerReadyEvent.setter
    def ConsumerReadyEvent(self, value: _EventContainer[typing.Callable[[], None], None]):
        ...

    def BacktestResultEventRaised(self, packet: QuantConnect.Packets.BacktestResultPacket) -> None:
        ...

    def ConsumerReadyEventRaised(self) -> None:
        ...

    def DebugEventRaised(self, packet: QuantConnect.Packets.DebugPacket) -> None:
        ...

    def Dispose(self) -> None:
        """Dispose of any resources"""
        ...

    def HandledErrorEventRaised(self, packet: QuantConnect.Packets.HandledErrorPacket) -> None:
        ...

    def Initialize(self, initializeParameters: QuantConnect.Interfaces.MessagingHandlerInitializeParameters) -> None:
        """
        Initialize the Messaging System Plugin.
        
        :param initializeParameters: The parameters required for initialization
        """
        ...

    def LoadingComplete(self) -> None:
        """Set Loaded to true"""
        ...

    def LogEventRaised(self, packet: QuantConnect.Packets.LogPacket) -> None:
        ...

    def OnBacktestResultEvent(self, packet: QuantConnect.Packets.BacktestResultPacket) -> None:
        """
        Raise a backtest result event safely.
        
        This method is protected.
        """
        ...

    def OnConsumerReadyEvent(self) -> None:
        """Handler for consumer ready code."""
        ...

    def OnDebugEvent(self, packet: QuantConnect.Packets.DebugPacket) -> None:
        """
        Raise a debug event safely
        
        This method is protected.
        """
        ...

    def OnHandledErrorEvent(self, packet: QuantConnect.Packets.HandledErrorPacket) -> None:
        """
        Raise a handled error event safely
        
        This method is protected.
        """
        ...

    def OnLogEvent(self, packet: QuantConnect.Packets.LogPacket) -> None:
        """
        Raise a log event safely
        
        This method is protected.
        """
        ...

    def OnRuntimeErrorEvent(self, packet: QuantConnect.Packets.RuntimeErrorPacket) -> None:
        """
        Raise runtime error safely
        
        This method is protected.
        """
        ...

    def OnSystemDebugEvent(self, packet: QuantConnect.Packets.SystemDebugPacket) -> None:
        """
        Raise a system debug event safely
        
        This method is protected.
        """
        ...

    def RuntimeErrorEventRaised(self, packet: QuantConnect.Packets.RuntimeErrorPacket) -> None:
        ...

    def Send(self, packet: QuantConnect.Packets.Packet) -> None:
        ...

    def SendEnqueuedPackets(self) -> None:
        """Send any message with a base type of Packet that has been enqueued."""
        ...

    def SendNotification(self, notification: QuantConnect.Notifications.Notification) -> None:
        """
        Send any notification with a base type of Notification.
        
        :param notification: The notification to be sent.
        """
        ...

    def SetAuthentication(self, job: QuantConnect.Packets.AlgorithmNodePacket) -> None:
        """Set the user communication channel"""
        ...

    def SystemDebugEventRaised(self, packet: QuantConnect.Packets.SystemDebugPacket) -> None:
        ...


class StreamingMessageHandler(System.Object, QuantConnect.Interfaces.IMessagingHandler):
    """Message handler that sends messages over tcp using NetMQ."""

    @property
    def HasSubscribers(self) -> bool:
        """
        Gets or sets whether this messaging handler has any current subscribers.
        This is not used in this message handler.  Messages are sent via tcp as they arrive
        """
        ...

    @HasSubscribers.setter
    def HasSubscribers(self, value: bool):
        """
        Gets or sets whether this messaging handler has any current subscribers.
        This is not used in this message handler.  Messages are sent via tcp as they arrive
        """
        ...

    def Dispose(self) -> None:
        """Dispose any resources used before destruction"""
        ...

    def Initialize(self, initializeParameters: QuantConnect.Interfaces.MessagingHandlerInitializeParameters) -> None:
        """
        Initialize the messaging system
        
        :param initializeParameters: The parameters required for initialization
        """
        ...

    def Send(self, packet: QuantConnect.Packets.Packet) -> None:
        """Send all types of packets"""
        ...

    def SendNotification(self, notification: QuantConnect.Notifications.Notification) -> None:
        """
        Send any notification with a base type of Notification.
        
        :param notification: The notification to be sent.
        """
        ...

    def SetAuthentication(self, job: QuantConnect.Packets.AlgorithmNodePacket) -> None:
        """Set the user communication channel"""
        ...

    def Transmit(self, packet: QuantConnect.Packets.Packet) -> None:
        """
        Send a message to the _server using ZeroMQ
        
        :param packet: Packet to transmit
        """
        ...


class Messaging(System.Object, QuantConnect.Interfaces.IMessagingHandler):
    """Local/desktop implementation of messaging system for Lean Engine."""

    @property
    def HasSubscribers(self) -> bool:
        """
        This implementation ignores the  flag and
        instead will always write to the log.
        """
        ...

    @HasSubscribers.setter
    def HasSubscribers(self, value: bool):
        """
        This implementation ignores the  flag and
        instead will always write to the log.
        """
        ...

    def Dispose(self) -> None:
        """Dispose of any resources"""
        ...

    def Initialize(self, initializeParameters: QuantConnect.Interfaces.MessagingHandlerInitializeParameters) -> None:
        """
        Initialize the messaging system
        
        :param initializeParameters: The parameters required for initialization
        """
        ...

    def Send(self, packet: QuantConnect.Packets.Packet) -> None:
        """Send a generic base packet without processing"""
        ...

    def SendNotification(self, notification: QuantConnect.Notifications.Notification) -> None:
        """Send any notification with a base type of Notification."""
        ...

    def SetAuthentication(self, job: QuantConnect.Packets.AlgorithmNodePacket) -> None:
        """Set the messaging channel"""
        ...


class _EventContainer(typing.Generic[QuantConnect_Messaging__EventContainer_Callable, QuantConnect_Messaging__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Messaging__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Messaging__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Messaging__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


