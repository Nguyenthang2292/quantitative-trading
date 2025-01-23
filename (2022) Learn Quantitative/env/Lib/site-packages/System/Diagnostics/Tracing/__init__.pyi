from typing import overload
import abc
import datetime
import typing

import System
import System.Collections.Generic
import System.Collections.ObjectModel
import System.Diagnostics.Tracing
import System.Runtime.Serialization

System_Diagnostics_Tracing_EventSource_Write_T = typing.TypeVar("System_Diagnostics_Tracing_EventSource_Write_T")
System_Diagnostics_Tracing__EventContainer_Callable = typing.TypeVar("System_Diagnostics_Tracing__EventContainer_Callable")
System_Diagnostics_Tracing__EventContainer_ReturnType = typing.TypeVar("System_Diagnostics_Tracing__EventContainer_ReturnType")


class EventLevel(System.Enum):
    """WindowsEventLevel. Custom values must be in the range from 16 through 255"""

    LogAlways = 0
    """Log always"""

    Critical = 1
    """Only critical errors"""

    Error = 2
    """All errors, including previous levels"""

    Warning = 3
    """All warnings, including previous levels"""

    Informational = 4
    """All informational events, including previous levels"""

    Verbose = 5
    """All events, including previous levels"""


class EventKeywords(System.Enum):
    """EventOpcode"""

    # Cannot convert to Python: None = ...
    """No events."""

    All = ...
    """All Events"""

    MicrosoftTelemetry = ...
    """Telemetry events"""

    WdiContext = ...
    """WDI context events"""

    WdiDiagnostic = ...
    """WDI diagnostic events"""

    Sqm = ...
    """SQM events"""

    AuditFailure = ...
    """Failed security audits"""

    AuditSuccess = ...
    """Successful security audits"""

    CorrelationHint = ...
    """
    Transfer events where the related Activity ID is a computed value and not a GUID
    N.B. The correct value for this field is 0x40000000000000.
    """

    EventLogClassic = ...
    """Events raised using classic eventlog API"""


class EventChannel(System.Enum):
    """This class has no documentation."""

    # Cannot convert to Python: None = 0
    """No channel"""

    Admin = 16

    Operational = 17
    """The operational channel"""

    Analytic = 18
    """The analytic channel"""

    Debug = 19
    """The debug channel"""


class EventManifestOptions(System.Enum):
    """
    Flags that can be used with EventSource.GenerateManifest to control how the ETW manifest for the EventSource is
    generated.
    """

    # Cannot convert to Python: None = ...
    """Only the resources associated with current UI culture are included in the  manifest"""

    Strict = ...
    """Throw exceptions for any inconsistency encountered"""

    AllCultures = ...
    """Generate a "resources" node under "localization" for every satellite assembly provided"""

    OnlyIfNeededForRegistration = ...
    """
    Generate the manifest only if the event source needs to be registered on the machine,
    otherwise return null (but still perform validation if Strict is specified)
    """

    AllowEventSourceOverride = ...
    """
    When generating the manifest do *not* enforce the rule that the current EventSource class
    must be the base class for the user-defined type passed in. This allows validation of .net
    event sources using the new validation code
    """


class EventCommand(System.Enum):
    """This class has no documentation."""

    Update = 0
    """Update EventSource state"""

    SendManifest = -1
    """Request EventSource to generate and send its manifest"""

    Enable = -2
    """Enable event"""

    Disable = -3
    """Disable event"""


class EventSourceSettings(System.Enum):
    """Enables specifying event source configuration options to be used in the EventSource constructor."""

    Default = 0
    """This specifies none of the special configuration options should be enabled."""

    ThrowOnEventWriteErrors = 1
    """Normally an EventSource NEVER throws; setting this option will tell it to throw when it encounters errors."""

    EtwManifestEventFormat = 4
    """
    Setting this option is a directive to the ETW listener should use manifest-based format when
    firing events. This is the default option when defining a type derived from EventSource
    (using the protected EventSource constructors).
    Only one of EtwManifestEventFormat or EtwSelfDescribingEventFormat should be specified
    """

    EtwSelfDescribingEventFormat = 8
    """
    Setting this option is a directive to the ETW listener should use self-describing event format
    when firing events. This is the default option when creating a new instance of the EventSource
    type (using the public EventSource constructors).
    Only one of EtwManifestEventFormat or EtwSelfDescribingEventFormat should be specified
    """


class EventCommandEventArgs(System.EventArgs):
    """Passed to the code:EventSource.OnEventCommand callback"""

    @property
    def Command(self) -> int:
        """
        Gets the command for the callback.
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventCommand enum.
        """
        ...

    @Command.setter
    def Command(self, value: int):
        """
        Gets the command for the callback.
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventCommand enum.
        """
        ...

    @property
    def Arguments(self) -> System.Collections.Generic.IDictionary[str, str]:
        """Gets the arguments for the callback."""
        ...

    @Arguments.setter
    def Arguments(self, value: System.Collections.Generic.IDictionary[str, str]):
        """Gets the arguments for the callback."""
        ...

    @property
    def eventSource(self) -> System.Diagnostics.Tracing.EventSource:
        ...

    @eventSource.setter
    def eventSource(self, value: System.Diagnostics.Tracing.EventSource):
        ...

    @property
    def dispatcher(self) -> System.Diagnostics.Tracing.EventDispatcher:
        ...

    @dispatcher.setter
    def dispatcher(self, value: System.Diagnostics.Tracing.EventDispatcher):
        ...

    @property
    def eventProviderType(self) -> System.Diagnostics.Tracing.EventProviderType:
        ...

    @eventProviderType.setter
    def eventProviderType(self, value: System.Diagnostics.Tracing.EventProviderType):
        ...

    @property
    def listener(self) -> System.Diagnostics.Tracing.EventListener:
        ...

    @listener.setter
    def listener(self, value: System.Diagnostics.Tracing.EventListener):
        ...

    @property
    def perEventSourceSessionId(self) -> int:
        ...

    @perEventSourceSessionId.setter
    def perEventSourceSessionId(self, value: int):
        ...

    @property
    def etwSessionId(self) -> int:
        ...

    @etwSessionId.setter
    def etwSessionId(self, value: int):
        ...

    @property
    def enable(self) -> bool:
        ...

    @enable.setter
    def enable(self, value: bool):
        ...

    @property
    def level(self) -> System.Diagnostics.Tracing.EventLevel:
        ...

    @level.setter
    def level(self, value: System.Diagnostics.Tracing.EventLevel):
        ...

    @property
    def matchAnyKeyword(self) -> System.Diagnostics.Tracing.EventKeywords:
        ...

    @matchAnyKeyword.setter
    def matchAnyKeyword(self, value: System.Diagnostics.Tracing.EventKeywords):
        ...

    @property
    def nextCommand(self) -> System.Diagnostics.Tracing.EventCommandEventArgs:
        ...

    @nextCommand.setter
    def nextCommand(self, value: System.Diagnostics.Tracing.EventCommandEventArgs):
        ...

    def DisableEvent(self, eventId: int) -> bool:
        """
        Disables the event that have the specified identifier.
        
        :param eventId: Event ID of event to be disabled
        :returns: true if eventId is in range.
        """
        ...

    def EnableEvent(self, eventId: int) -> bool:
        """
        Enables the event that has the specified identifier.
        
        :param eventId: Event ID of event to be enabled
        :returns: true if eventId is in range.
        """
        ...


class EventTags(System.Enum):
    """
    Tags are flags that are not interpreted by EventSource but are passed along
    to the EventListener. The EventListener determines the semantics of the flags.
    """

    # Cannot convert to Python: None = 0
    """No special traits are added to the event."""


class EventActivityOptions(System.Enum):
    """EventActivityOptions flags allow to specify different activity related characteristics."""

    # Cannot convert to Python: None = 0
    """No special options are added to the event."""

    Disable = ...
    """Disable Implicit Activity Tracking"""

    Recursive = ...
    """Allow activity event to call itself (directly or indirectly)"""

    Detachable = ...
    """Allows event activity to live beyond its parent."""


class EventSourceOptions:
    """
    Used when calling EventSource.Write.
    Optional overrides for event settings such as Level, Keywords, or Opcode.
    If overrides are not provided for a setting, default values will be used.
    """

    @property
    def keywords(self) -> System.Diagnostics.Tracing.EventKeywords:
        ...

    @keywords.setter
    def keywords(self, value: System.Diagnostics.Tracing.EventKeywords):
        ...

    @property
    def tags(self) -> System.Diagnostics.Tracing.EventTags:
        ...

    @tags.setter
    def tags(self, value: System.Diagnostics.Tracing.EventTags):
        ...

    @property
    def activityOptions(self) -> System.Diagnostics.Tracing.EventActivityOptions:
        ...

    @activityOptions.setter
    def activityOptions(self, value: System.Diagnostics.Tracing.EventActivityOptions):
        ...

    @property
    def level(self) -> int:
        ...

    @level.setter
    def level(self, value: int):
        ...

    @property
    def opcode(self) -> int:
        ...

    @opcode.setter
    def opcode(self, value: int):
        ...

    @property
    def valuesSet(self) -> int:
        ...

    @valuesSet.setter
    def valuesSet(self, value: int):
        ...

    keywordsSet: int = ...

    tagsSet: int = ...

    levelSet: int = ...

    opcodeSet: int = ...

    activityOptionsSet: int = ...

    @property
    def Level(self) -> int:
        """
        Gets or sets the level to use for the specified event. If this property
        is unset, the event's level will be 5 (Verbose).
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventLevel enum.
        """
        ...

    @Level.setter
    def Level(self, value: int):
        """
        Gets or sets the level to use for the specified event. If this property
        is unset, the event's level will be 5 (Verbose).
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventLevel enum.
        """
        ...

    @property
    def Opcode(self) -> int:
        """
        Gets or sets the opcode to use for the specified event. If this property
        is unset, the event's opcode will 0 (Info).
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventOpcode enum.
        """
        ...

    @Opcode.setter
    def Opcode(self, value: int):
        """
        Gets or sets the opcode to use for the specified event. If this property
        is unset, the event's opcode will 0 (Info).
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventOpcode enum.
        """
        ...

    @property
    def IsOpcodeSet(self) -> bool:
        ...

    @property
    def Keywords(self) -> int:
        """
        Gets or sets the keywords to use for the specified event. If this
        property is unset, the event's keywords will be 0.
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventKeywords enum.
        """
        ...

    @Keywords.setter
    def Keywords(self, value: int):
        """
        Gets or sets the keywords to use for the specified event. If this
        property is unset, the event's keywords will be 0.
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventKeywords enum.
        """
        ...

    @property
    def Tags(self) -> int:
        """
        Gets or sets the tags to use for the specified event. If this property is
        unset, the event's tags will be 0.
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventTags enum.
        """
        ...

    @Tags.setter
    def Tags(self, value: int):
        """
        Gets or sets the tags to use for the specified event. If this property is
        unset, the event's tags will be 0.
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventTags enum.
        """
        ...

    @property
    def ActivityOptions(self) -> int:
        """
        Gets or sets the activity options for this specified events. If this property is
        unset, the event's activity options will be 0.
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventActivityOptions enum.
        """
        ...

    @ActivityOptions.setter
    def ActivityOptions(self, value: int):
        """
        Gets or sets the activity options for this specified events. If this property is
        unset, the event's activity options will be 0.
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventActivityOptions enum.
        """
        ...


class EventSource(System.Object, System.IDisposable):
    """
    This class is meant to be inherited by a user-defined event source in order to define a managed
    ETW provider.   Please See DESIGN NOTES above for the internal architecture.
    The minimal definition of an EventSource simply specifies a number of ETW event methods that
    call one of the EventSource.WriteEvent overloads, EventSource.WriteEventCore,
    or EventSource.WriteEventWithRelatedActivityIdCore to log them. This functionality
    is sufficient for many users.
    
    To achieve more control over the ETW provider manifest exposed by the event source type, the
    [] attributes can be specified for the ETW event methods.
    
    For very advanced EventSources, it is possible to intercept the commands being given to the
    eventSource and change what filtering is done (see EventListener.EnableEvents and
    ) or cause actions to be performed by the eventSource,
    e.g. dumping a data structure (see EventSource.SendCommand and
    ).
    
    The eventSources can be turned on with Windows ETW controllers (e.g. logman), immediately.
    It is also possible to control and intercept the data dispatcher programmatically.  See
     for more.
    """

    IsSupported: bool

    @property
    def Name(self) -> str:
        ...

    @property
    def Guid(self) -> System.Guid:
        """Every eventSource is assigned a GUID to uniquely identify it to the system."""
        ...

    @property
    def Settings(self) -> int:
        """
        Returns the settings for the event source instance
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventSourceSettings enum.
        """
        ...

    @property
    def ConstructionException(self) -> System.Exception:
        ...

    @property
    def EventCommandExecuted(self) -> _EventContainer[typing.Callable[[System.Object, System.Diagnostics.Tracing.EventCommandEventArgs], None], None]:
        """Fires when a Command (e.g. Enable) comes from a an EventListener."""
        ...

    @EventCommandExecuted.setter
    def EventCommandExecuted(self, value: _EventContainer[typing.Callable[[System.Object, System.Diagnostics.Tracing.EventCommandEventArgs], None], None]):
        """Fires when a Command (e.g. Enable) comes from a an EventListener."""
        ...

    CurrentThreadActivityId: System.Guid
    """Retrieves the ETW activity ID associated with the current thread."""

    @property
    def m_id(self) -> int:
        ...

    @m_id.setter
    def m_id(self, value: int):
        ...

    @property
    def m_eventData(self) -> typing.List[System.Diagnostics.Tracing.EventSource.EventMetadata]:
        ...

    @m_eventData.setter
    def m_eventData(self, value: typing.List[System.Diagnostics.Tracing.EventSource.EventMetadata]):
        ...

    @property
    def m_level(self) -> System.Diagnostics.Tracing.EventLevel:
        ...

    @m_level.setter
    def m_level(self, value: System.Diagnostics.Tracing.EventLevel):
        ...

    @property
    def m_matchAnyKeyword(self) -> System.Diagnostics.Tracing.EventKeywords:
        ...

    @m_matchAnyKeyword.setter
    def m_matchAnyKeyword(self, value: System.Diagnostics.Tracing.EventKeywords):
        ...

    @property
    def m_Dispatchers(self) -> System.Diagnostics.Tracing.EventDispatcher:
        ...

    @m_Dispatchers.setter
    def m_Dispatchers(self, value: System.Diagnostics.Tracing.EventDispatcher):
        ...

    s_ActivityStartSuffix: str = "Start"

    s_ActivityStopSuffix: str = "Stop"

    DuplicateSourceNamesSwitch: str = "System.Diagnostics.Tracing.EventSource.AllowDuplicateSourceNames"

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, throwOnEventWriteErrors: bool) -> None:
        """
        By default calling the 'WriteEvent' methods do NOT throw on errors (they silently discard the event).
        This is because in most cases users assume logging is not 'precious' and do NOT wish to have logging failures
        crash the program. However for those applications where logging is 'precious' and if it fails the caller
        wishes to react, setting 'throwOnEventWriteErrors' will cause an exception to be thrown if WriteEvent
        fails. Note the fact that EventWrite succeeds does not necessarily mean that the event reached its destination
        only that operation of writing it did not fail. These EventSources will not generate self-describing ETW events.
        
        For compatibility only use the EventSourceSettings.ThrowOnEventWriteErrors flag instead.
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, settings: System.Diagnostics.Tracing.EventSourceSettings) -> None:
        """
        Construct an EventSource with additional non-default settings (see EventSourceSettings for more)
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, settings: System.Diagnostics.Tracing.EventSourceSettings, *traits: str) -> None:
        """
        Construct an EventSource with additional non-default settings.
        
        Also specify a list of key-value pairs called traits (you must pass an even number of strings).
        The first string is the key and the second is the value.   These are not interpreted by EventSource
        itself but may be interpreted the listeners.  Can be fetched with GetTrait(string).
        
        This method is protected.
        
        :param settings: See EventSourceSettings for more.
        :param traits: A collection of key-value strings (must be an even number).
        """
        ...

    @overload
    def __init__(self, eventSourceName: str) -> None:
        ...

    @overload
    def __init__(self, eventSourceName: str, config: System.Diagnostics.Tracing.EventSourceSettings) -> None:
        """
        Construct an EventSource with a given name for non-contract based events (e.g. those using the Write() API).
        
        :param eventSourceName: The name of the event source. Must not be null.
        :param config: Configuration options for the EventSource as a whole.
        """
        ...

    @overload
    def __init__(self, eventSourceName: str, config: System.Diagnostics.Tracing.EventSourceSettings, *traits: str) -> None:
        """
        Construct an EventSource with a given name for non-contract based events (e.g. those using the Write() API).
        
        Also specify a list of key-value pairs called traits (you must pass an even number of strings).
        The first string is the key and the second is the value.   These are not interpreted by EventSource
        itself but may be interpreted the listeners.  Can be fetched with GetTrait(string).
        
        :param eventSourceName: The name of the event source. Must not be null.
        :param config: Configuration options for the EventSource as a whole.
        :param traits: A collection of key-value strings (must be an even number).
        """
        ...

    @overload
    def Dispose(self) -> None:
        ...

    @overload
    def Dispose(self, disposing: bool) -> None:
        """
        Disposes of an EventSource.
        
        This method is protected.
        
        :param disposing: True if called from Dispose(), false if called from the finalizer.
        """
        ...

    @staticmethod
    @overload
    def GenerateManifest(eventSourceType: typing.Type, assemblyPathToIncludeInManifest: str) -> str:
        """
        Returns a string of the XML manifest associated with the eventSourceType. The scheme for this XML is
        documented at in EventManifest Schema https://docs.microsoft.com/en-us/windows/desktop/WES/eventmanifestschema-schema.
        This is the preferred way of generating a manifest to be embedded in the ETW stream as it is fast and
        the fact that it only includes localized entries for the current UI culture is an acceptable tradeoff.
        
        :param eventSourceType: The type of the event source class for which the manifest is generated
        :param assemblyPathToIncludeInManifest: The manifest XML fragment contains the string name of the DLL name in which it is embedded.  This parameter specifies what name will be used
        :returns: The XML data string.
        """
        ...

    @staticmethod
    @overload
    def GenerateManifest(eventSourceType: typing.Type, assemblyPathToIncludeInManifest: str, flags: System.Diagnostics.Tracing.EventManifestOptions) -> str:
        """
        Returns a string of the XML manifest associated with the eventSourceType. The scheme for this XML is
        documented at in EventManifest Schema https://docs.microsoft.com/en-us/windows/desktop/WES/eventmanifestschema-schema.
        Pass EventManifestOptions.AllCultures when generating a manifest to be registered on the machine. This
        ensures that the entries in the event log will be "optimally" localized.
        
        :param eventSourceType: The type of the event source class for which the manifest is generated
        :param assemblyPathToIncludeInManifest: The manifest XML fragment contains the string name of the DLL name in which it is embedded.  This parameter specifies what name will be used
        :param flags: The flags to customize manifest generation. If flags has bit OnlyIfNeededForRegistration specified this returns null when the eventSourceType does not require explicit registration
        :returns: The XML data string or null.
        """
        ...

    @staticmethod
    def GetGuid(eventSourceType: typing.Type) -> System.Guid:
        ...

    @staticmethod
    def GetName(eventSourceType: typing.Type) -> str:
        """
        Returns the official ETW Provider name for the eventSource defined by 'eventSourceType'.
        This API allows you to compute this without actually creating an instance of the EventSource.
        It only needs to reflect over the type.
        """
        ...

    @staticmethod
    def GetSources() -> System.Collections.Generic.IEnumerable[System.Diagnostics.Tracing.EventSource]:
        ...

    def GetTrait(self, key: str) -> str:
        """
        EventSources can have arbitrary string key-value pairs associated with them called Traits.
        These traits are not interpreted by the EventSource but may be interpreted by EventListeners
        (e.g. like the built in ETW listener).   These traits are specified at EventSource
        construction time and can be retrieved by using this GetTrait API.
        
        :param key: The key to look up in the set of key-value pairs passed to the EventSource constructor
        :returns: The value string associated with key.  Will return null if there is no such key.
        """
        ...

    @overload
    def IsEnabled(self) -> bool:
        """
        Returns true if the eventSource has been enabled at all. This is the preferred test
        to be performed before a relatively expensive EventSource operation.
        """
        ...

    @overload
    def IsEnabled(self, level: System.Diagnostics.Tracing.EventLevel, keywords: System.Diagnostics.Tracing.EventKeywords) -> bool:
        """
        Returns true if events with greater than or equal 'level' and have one of 'keywords' set are enabled.
        
        Note that the result of this function is only an approximation on whether a particular
        event is active or not. It is only meant to be used as way of avoiding expensive
        computation for logging when logging is not on, therefore it sometimes returns false
        positives (but is always accurate when returning false).  EventSources are free to
        have additional filtering.
        """
        ...

    @overload
    def IsEnabled(self, level: System.Diagnostics.Tracing.EventLevel, keywords: System.Diagnostics.Tracing.EventKeywords, channel: System.Diagnostics.Tracing.EventChannel) -> bool:
        """
        Returns true if events with greater than or equal 'level' and have one of 'keywords' set are enabled, or
        if 'keywords' specifies a channel bit for a channel that is enabled.
        
        Note that the result of this function only an approximation on whether a particular
        event is active or not. It is only meant to be used as way of avoiding expensive
        computation for logging when logging is not on, therefore it sometimes returns false
        positives (but is always accurate when returning false).  EventSources are free to
        have additional filtering.
        """
        ...

    def OnEventCommand(self, command: System.Diagnostics.Tracing.EventCommandEventArgs) -> None:
        """This method is protected."""
        ...

    @staticmethod
    def SendCommand(eventSource: System.Diagnostics.Tracing.EventSource, command: System.Diagnostics.Tracing.EventCommand, commandArguments: System.Collections.Generic.IDictionary[str, str]) -> None:
        """
        Send a command to a particular EventSource identified by 'eventSource'.
        Calling this routine simply forwards the command to the EventSource.OnEventCommand
        callback.  What the EventSource does with the command and its arguments are from
        that point EventSource-specific.
        
        :param eventSource: The instance of EventSource to send the command to
        :param command: A positive user-defined EventCommand, or EventCommand.SendManifest
        :param commandArguments: A set of (name-argument, value-argument) pairs associated with the command
        """
        ...

    @staticmethod
    @overload
    def SetCurrentThreadActivityId(activityId: System.Guid) -> None:
        ...

    @staticmethod
    @overload
    def SetCurrentThreadActivityId(activityId: System.Guid, oldActivityThatWillContinue: typing.Optional[System.Guid]) -> typing.Union[None, System.Guid]:
        """
        When a thread starts work that is on behalf of 'something else' (typically another
        thread or network request) it should mark the thread as working on that other work.
        This API marks the current thread as working on activity 'activityID'. It returns
        whatever activity the thread was previously marked with. There is a convention that
        callers can assume that callees restore this activity mark before the callee returns.
        To encourage this, this API returns the old activity, so that it can be restored later.
        
        All events created with the EventSource on this thread are also tagged with the
        activity ID of the thread.
        
        It is common, and good practice after setting the thread to an activity to log an event
        with a 'start' opcode to indicate that precise time/thread where the new activity
        started.
        
        :param activityId: A Guid that represents the new activity with which to mark the current thread
        :param oldActivityThatWillContinue: The Guid that represents the current activity which will continue at some point in the future, on the current thread
        """
        ...

    def ToString(self) -> str:
        """Displays the name and GUID for the eventSource for debugging purposes."""
        ...

    @overload
    def Write(self, eventName: str) -> None:
        """
        Writes an event with no fields and default options.
        (Native API: EventWriteTransfer)
        
        :param eventName: The name of the event.
        """
        ...

    @overload
    def Write(self, eventName: str, options: System.Diagnostics.Tracing.EventSourceOptions) -> None:
        """
        Writes an event with no fields.
        (Native API: EventWriteTransfer)
        
        :param eventName: The name of the event.
        :param options: Options for the event, such as the level, keywords, and opcode. Unset options will be set to default values.
        """
        ...

    @overload
    def Write(self, eventName: str, data: System_Diagnostics_Tracing_EventSource_Write_T) -> None:
        """
        Writes an event.
        (Native API: EventWriteTransfer)
        
        :param eventName: The name for the event. If null, the event name is automatically determined based on T, either from the Name property of T's EventData attribute or from typeof(T).Name.
        :param data: The object containing the event payload data. The type T must be an anonymous type or a type with an [EventData] attribute. The public instance properties of data will be written recursively to create the fields of the event.
        """
        ...

    @overload
    def Write(self, eventName: str, options: System.Diagnostics.Tracing.EventSourceOptions, data: System_Diagnostics_Tracing_EventSource_Write_T) -> None:
        """
        Writes an event.
        (Native API: EventWriteTransfer)
        
        :param eventName: The name for the event. If null, the event name is automatically determined based on T, either from the Name property of T's EventData attribute or from typeof(T).Name.
        :param options: Options for the event, such as the level, keywords, and opcode. Unset options will be set to default values.
        :param data: The object containing the event payload data. The type T must be an anonymous type or a type with an [EventData] attribute. The public instance properties of data will be written recursively to create the fields of the event.
        """
        ...

    @overload
    def Write(self, eventName: str, options: System.Diagnostics.Tracing.EventSourceOptions, data: System_Diagnostics_Tracing_EventSource_Write_T) -> None:
        """
        Writes an event.
        This overload is for use with extension methods that wish to efficiently
        forward the options or data parameter without performing an extra copy.
        (Native API: EventWriteTransfer)
        
        :param eventName: The name for the event. If null, the event name is automatically determined based on T, either from the Name property of T's EventData attribute or from typeof(T).Name.
        :param options: Options for the event, such as the level, keywords, and opcode. Unset options will be set to default values.
        :param data: The object containing the event payload data. The type T must be an anonymous type or a type with an [EventData] attribute. The public instance properties of data will be written recursively to create the fields of the event.
        """
        ...

    @overload
    def Write(self, eventName: str, options: System.Diagnostics.Tracing.EventSourceOptions, activityId: System.Guid, relatedActivityId: System.Guid, data: System_Diagnostics_Tracing_EventSource_Write_T) -> None:
        """
        Writes an event.
        This overload is meant for clients that need to manipuate the activityId
        and related ActivityId for the event.
        
        :param eventName: The name for the event. If null, the event name is automatically determined based on T, either from the Name property of T's EventData attribute or from typeof(T).Name.
        :param options: Options for the event, such as the level, keywords, and opcode. Unset options will be set to default values.
        :param activityId: The GUID of the activity associated with this event.
        :param relatedActivityId: The GUID of another activity that is related to this activity, or Guid.Empty if there is no related activity. Most commonly, the Start operation of a new activity specifies a parent activity as its related activity.
        :param data: The object containing the event payload data. The type T must be an anonymous type or a type with an [EventData] attribute. The public instance properties of data will be written recursively to create the fields of the event.
        """
        ...

    @overload
    def WriteEvent(self, eventId: int) -> None:
        """This method is protected."""
        ...

    @overload
    def WriteEvent(self, eventId: int, arg1: int) -> None:
        """This method is protected."""
        ...

    @overload
    def WriteEvent(self, eventId: int, arg1: int, arg2: int) -> None:
        """This method is protected."""
        ...

    @overload
    def WriteEvent(self, eventId: int, arg1: int, arg2: int, arg3: int) -> None:
        """This method is protected."""
        ...

    @overload
    def WriteEvent(self, eventId: int, arg1: int) -> None:
        """This method is protected."""
        ...

    @overload
    def WriteEvent(self, eventId: int, arg1: int, arg2: int) -> None:
        """This method is protected."""
        ...

    @overload
    def WriteEvent(self, eventId: int, arg1: int, arg2: int, arg3: int) -> None:
        """This method is protected."""
        ...

    @overload
    def WriteEvent(self, eventId: int, arg1: str) -> None:
        """This method is protected."""
        ...

    @overload
    def WriteEvent(self, eventId: int, arg1: str, arg2: str) -> None:
        """This method is protected."""
        ...

    @overload
    def WriteEvent(self, eventId: int, arg1: str, arg2: str, arg3: str) -> None:
        """This method is protected."""
        ...

    @overload
    def WriteEvent(self, eventId: int, arg1: str, arg2: int) -> None:
        """This method is protected."""
        ...

    @overload
    def WriteEvent(self, eventId: int, arg1: str, arg2: int, arg3: int) -> None:
        """This method is protected."""
        ...

    @overload
    def WriteEvent(self, eventId: int, arg1: str, arg2: int) -> None:
        """This method is protected."""
        ...

    @overload
    def WriteEvent(self, eventId: int, arg1: int, arg2: str) -> None:
        """This method is protected."""
        ...

    @overload
    def WriteEvent(self, eventId: int, arg1: int, arg2: str) -> None:
        """This method is protected."""
        ...

    @overload
    def WriteEvent(self, eventId: int, arg1: typing.List[int]) -> None:
        """This method is protected."""
        ...

    @overload
    def WriteEvent(self, eventId: int, arg1: int, arg2: typing.List[int]) -> None:
        """This method is protected."""
        ...

    @overload
    def WriteEvent(self, eventId: int, *args: typing.Any) -> None:
        """This method is protected."""
        ...

    def WriteEventCore(self, eventId: int, eventDataCount: int, data: typing.Any) -> None:
        """
        This routine allows you to create efficient WriteEvent helpers, however the code that you use to
        do this, while straightforward, is unsafe.
        
        This method is protected.
        """
        ...

    def WriteEventWithRelatedActivityId(self, eventId: int, relatedActivityId: System.Guid, *args: typing.Any) -> None:
        """
        This is the varargs helper for writing an event which also specifies a related activity. It is completely analogous
        to corresponding WriteEvent (they share implementation). It does create an array and box all the arguments so it is
        relatively inefficient and should only be used for relatively rare events (e.g. less than 100 / sec).  If your
        rates are faster than that you should use WriteEventWithRelatedActivityIdCore to create fast helpers for your
        particular method signature. Even if you use this for rare events, this call should be guarded by an IsEnabled()
        check so that the varargs call is not made when the EventSource is not active.
        
        This method is protected.
        """
        ...

    def WriteEventWithRelatedActivityIdCore(self, eventId: int, relatedActivityId: typing.Any, eventDataCount: int, data: typing.Any) -> None:
        """
        This routine allows you to create efficient WriteEventWithRelatedActivityId helpers, however the code
        that you use to do this, while straightforward, is unsafe. The only difference from
        WriteEventCore is that you pass the relatedActivityId from caller through to this API
        
        This method is protected.
        """
        ...


class DiagnosticCounter(System.Object, System.IDisposable, metaclass=abc.ABCMeta):
    """
    DiagnosticCounter is an abstract class that serves as the parent class for various Counter* classes,
    namely EventCounter, PollingCounter, IncrementingEventCounter, and IncrementingPollingCounter.
    """

    @property
    def DisplayName(self) -> str:
        ...

    @DisplayName.setter
    def DisplayName(self, value: str):
        ...

    @property
    def DisplayUnits(self) -> str:
        ...

    @DisplayUnits.setter
    def DisplayUnits(self, value: str):
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def EventSource(self) -> System.Diagnostics.Tracing.EventSource:
        ...

    def AddMetadata(self, key: str, value: str) -> None:
        """Adds a key-value metadata to the EventCounter that will be included as a part of the payload"""
        ...

    def Dispose(self) -> None:
        """
        Removes the counter from set that the EventSource will report on.  After being disposed, this
        counter will do nothing and its resource will be reclaimed if all references to it are removed.
        If an EventCounter is not explicitly disposed it will be cleaned up automatically when the
        EventSource it is attached to dies.
        """
        ...


class IncrementingPollingCounter(System.Diagnostics.Tracing.DiagnosticCounter):
    """
    IncrementingPollingCounter is a variant of EventCounter for variables that are ever-increasing.
    Ex) # of exceptions in the runtime.
    It does not calculate statistics like mean, standard deviation, etc. because it only accumulates
    the counter value.
    Unlike IncrementingEventCounter, this takes in a polling callback that it can call to update
    its own metric periodically.
    """

    @property
    def DisplayRateTimeScale(self) -> datetime.timedelta:
        ...

    @DisplayRateTimeScale.setter
    def DisplayRateTimeScale(self, value: datetime.timedelta):
        ...

    def __init__(self, name: str, eventSource: System.Diagnostics.Tracing.EventSource, totalValueProvider: typing.Callable[[], float]) -> None:
        """
        Initializes a new instance of the IncrementingPollingCounter class.
        IncrementingPollingCounter live as long as the EventSource that they are attached to unless they are
        explicitly Disposed.
        
        :param name: The name.
        :param eventSource: The event source.
        :param totalValueProvider: The delegate to invoke to get the total value for this counter.
        """
        ...

    def ToString(self) -> str:
        ...


class PollingCounter(System.Diagnostics.Tracing.DiagnosticCounter):
    """
    PollingCounter is a variant of EventCounter - it collects and calculates similar statistics
    as EventCounter. PollingCounter differs from EventCounter in that it takes in a callback
    function to collect metrics on its own rather than the user having to call WriteMetric()
    every time.
    """

    def __init__(self, name: str, eventSource: System.Diagnostics.Tracing.EventSource, metricProvider: typing.Callable[[], float]) -> None:
        """
        Initializes a new instance of the PollingCounter class.
        PollingCounter live as long as the EventSource that they are attached to unless they are
        explicitly Disposed.
        
        :param name: The name.
        :param eventSource: The event source.
        :param metricProvider: The delegate to invoke to get the current metric value.
        """
        ...

    def ToString(self) -> str:
        ...


class EventSourceCreatedEventArgs(System.EventArgs):
    """EventSourceCreatedEventArgs is passed to EventListener.EventSourceCreated"""

    @property
    def EventSource(self) -> System.Diagnostics.Tracing.EventSource:
        """The EventSource that is attaching to the listener."""
        ...

    @EventSource.setter
    def EventSource(self, value: System.Diagnostics.Tracing.EventSource):
        """The EventSource that is attaching to the listener."""
        ...


class EventWrittenEventArgs(System.EventArgs):
    """
    EventWrittenEventArgs is passed to the user-provided override for
    EventListener.OnEventWritten when an event is fired.
    """

    EmptyPayload: System.Collections.ObjectModel.ReadOnlyCollection[System.Object] = ...

    @property
    def EventName(self) -> str:
        """The name of the event."""
        ...

    @EventName.setter
    def EventName(self, value: str):
        """The name of the event."""
        ...

    @property
    def EventId(self) -> int:
        """Gets the event ID for the event that was written."""
        ...

    @property
    def ActivityId(self) -> System.Guid:
        """Gets the activity ID for the thread on which the event was written."""
        ...

    @property
    def RelatedActivityId(self) -> System.Guid:
        """Gets the related activity ID if one was specified when the event was written."""
        ...

    @property
    def Payload(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Object]:
        """Gets the payload for the event."""
        ...

    @Payload.setter
    def Payload(self, value: System.Collections.ObjectModel.ReadOnlyCollection[System.Object]):
        """Gets the payload for the event."""
        ...

    @property
    def PayloadNames(self) -> System.Collections.ObjectModel.ReadOnlyCollection[str]:
        """Gets the payload argument names."""
        ...

    @PayloadNames.setter
    def PayloadNames(self, value: System.Collections.ObjectModel.ReadOnlyCollection[str]):
        """Gets the payload argument names."""
        ...

    @property
    def EventSource(self) -> System.Diagnostics.Tracing.EventSource:
        """Gets the event source object."""
        ...

    @property
    def Keywords(self) -> int:
        """
        Gets the keywords for the event.
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventKeywords enum.
        """
        ...

    @Keywords.setter
    def Keywords(self, value: int):
        """
        Gets the keywords for the event.
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventKeywords enum.
        """
        ...

    @property
    def Opcode(self) -> int:
        """
        Gets the operation code for the event.
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventOpcode enum.
        """
        ...

    @Opcode.setter
    def Opcode(self, value: int):
        """
        Gets the operation code for the event.
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventOpcode enum.
        """
        ...

    @property
    def Task(self) -> int:
        """
        Gets the task for the event.
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventTask enum.
        """
        ...

    @property
    def Tags(self) -> int:
        """
        Any provider/user defined options associated with the event.
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventTags enum.
        """
        ...

    @Tags.setter
    def Tags(self, value: int):
        """
        Any provider/user defined options associated with the event.
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventTags enum.
        """
        ...

    @property
    def Message(self) -> str:
        """Gets the message for the event.  If the message has {N} parameters they are NOT substituted."""
        ...

    @Message.setter
    def Message(self, value: str):
        """Gets the message for the event.  If the message has {N} parameters they are NOT substituted."""
        ...

    @property
    def Version(self) -> int:
        ...

    @property
    def Level(self) -> int:
        """
        Gets the level for the event.
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventLevel enum.
        """
        ...

    @Level.setter
    def Level(self, value: int):
        """
        Gets the level for the event.
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventLevel enum.
        """
        ...

    @property
    def OSThreadId(self) -> int:
        """Gets the identifier for the OS thread that wrote the event."""
        ...

    @OSThreadId.setter
    def OSThreadId(self, value: int):
        """Gets the identifier for the OS thread that wrote the event."""
        ...

    @property
    def TimeStamp(self) -> datetime.datetime:
        """Gets a UTC DateTime that specifies when the event was written."""
        ...

    @TimeStamp.setter
    def TimeStamp(self, value: datetime.datetime):
        """Gets a UTC DateTime that specifies when the event was written."""
        ...


class EventListener(System.Object, System.IDisposable, metaclass=abc.ABCMeta):
    """
    An EventListener represents a target for the events generated by EventSources (that is subclasses
    of EventSource), in the current appdomain. When a new EventListener is created
    it is logically attached to all eventSources in that appdomain. When the EventListener is Disposed, then
    it is disconnected from the event eventSources. Note that there is a internal list of STRONG references
    to EventListeners, which means that relying on the lack of references to EventListeners to clean up
    EventListeners will NOT work. You must call EventListener.Dispose explicitly when a dispatcher is no
    longer needed.
    
    Once created, EventListeners can enable or disable on a per-eventSource basis using verbosity levels
    () and bitfields () to further restrict the set of
    events to be sent to the dispatcher. The dispatcher can also send arbitrary commands to a particular
    eventSource using the 'SendCommand' method. The meaning of the commands are eventSource specific.
    
    The Null Guid (that is (new Guid()) has special meaning as a wildcard for 'all current eventSources in
    the appdomain'. Thus it is relatively easy to turn on all events in the appdomain if desired.
    
    It is possible for there to be many EventListener's defined in a single appdomain. Each dispatcher is
    logically independent of the other listeners. Thus when one dispatcher enables or disables events, it
    affects only that dispatcher (other listeners get the events they asked for). It is possible that
    commands sent with 'SendCommand' would do a semantic operation that would affect the other listeners
    (like doing a GC, or flushing data ...), but this is the exception rather than the rule.
    
    Thus the model is that each EventSource keeps a list of EventListeners that it is sending events
    to. Associated with each EventSource-dispatcher pair is a set of filtering criteria that determine for
    that eventSource what events that dispatcher will receive.
    
    Listeners receive the events on their 'OnEventWritten' method. Thus subclasses of EventListener must
    override this method to do something useful with the data.
    
    In addition, when new eventSources are created, the 'OnEventSourceCreate' method is called. The
    invariant associated with this callback is that every eventSource gets exactly one
    'OnEventSourceCreate' call for ever eventSource that can potentially send it log messages. In
    particular when a EventListener is created, typically a series of OnEventSourceCreate' calls are
    made to notify the new dispatcher of all the eventSources that existed before the EventListener was
    created.
    """

    @property
    def EventSourceCreated(self) -> _EventContainer[typing.Callable[[System.Object, System.Diagnostics.Tracing.EventSourceCreatedEventArgs], None], None]:
        """
        This event is raised whenever a new eventSource is 'attached' to the dispatcher.
        This can happen for all existing EventSources when the EventListener is created
        as well as for any EventSources that come into existence after the EventListener
        has been created.
        
        These 'catch up' events are called during the construction of the EventListener.
        Subclasses need to be prepared for that.
        
        In a multi-threaded environment, it is possible that 'EventSourceEventWrittenCallback'
        events for a particular eventSource to occur BEFORE the EventSourceCreatedCallback is issued.
        """
        ...

    @EventSourceCreated.setter
    def EventSourceCreated(self, value: _EventContainer[typing.Callable[[System.Object, System.Diagnostics.Tracing.EventSourceCreatedEventArgs], None], None]):
        """
        This event is raised whenever a new eventSource is 'attached' to the dispatcher.
        This can happen for all existing EventSources when the EventListener is created
        as well as for any EventSources that come into existence after the EventListener
        has been created.
        
        These 'catch up' events are called during the construction of the EventListener.
        Subclasses need to be prepared for that.
        
        In a multi-threaded environment, it is possible that 'EventSourceEventWrittenCallback'
        events for a particular eventSource to occur BEFORE the EventSourceCreatedCallback is issued.
        """
        ...

    @property
    def EventWritten(self) -> _EventContainer[typing.Callable[[System.Object, System.Diagnostics.Tracing.EventWrittenEventArgs], None], None]:
        """
        This event is raised whenever an event has been written by a EventSource for which
        the EventListener has enabled events.
        """
        ...

    @EventWritten.setter
    def EventWritten(self, value: _EventContainer[typing.Callable[[System.Object, System.Diagnostics.Tracing.EventWrittenEventArgs], None], None]):
        """
        This event is raised whenever an event has been written by a EventSource for which
        the EventListener has enabled events.
        """
        ...

    EventListenersLock: System.Object
    """
    Gets a global lock that is intended to protect the code:s_Listeners linked list and the
    code:s_EventSources list.  (We happen to use the s_EventSources list as the lock object)
    """

    @property
    def m_Next(self) -> System.Diagnostics.Tracing.EventListener:
        ...

    @m_Next.setter
    def m_Next(self, value: System.Diagnostics.Tracing.EventListener):
        ...

    s_Listeners: System.Diagnostics.Tracing.EventListener

    s_EventSources: System.Collections.Generic.List[System.WeakReference[System.Diagnostics.Tracing.EventSource]]
    """
    The list of all active eventSources in the appdomain.  Note that eventSources do NOT
    remove themselves from this list this is a weak list and the GC that removes them may
    not have happened yet.  Thus it can contain event sources that are dead (thus you have
    to filter those out.
    """

    def __init__(self) -> None:
        """
        Create a new EventListener in which all events start off turned off (use EnableEvents to turn
        them on).
        
        This method is protected.
        """
        ...

    def DisableEvents(self, eventSource: System.Diagnostics.Tracing.EventSource) -> None:
        """
        Disables all events coming from eventSource identified by 'eventSource'.
        
        This call never has an effect on other EventListeners.
        """
        ...

    def Dispose(self) -> None:
        """
        Dispose should be called when the EventListener no longer desires 'OnEvent*' callbacks. Because
        there is an internal list of strong references to all EventListeners, calling 'Dispose' directly
        is the only way to actually make the listen die. Thus it is important that users of EventListener
        call Dispose when they are done with their logging.
        """
        ...

    @overload
    def EnableEvents(self, eventSource: System.Diagnostics.Tracing.EventSource, level: System.Diagnostics.Tracing.EventLevel) -> None:
        ...

    @overload
    def EnableEvents(self, eventSource: System.Diagnostics.Tracing.EventSource, level: System.Diagnostics.Tracing.EventLevel, matchAnyKeyword: System.Diagnostics.Tracing.EventKeywords) -> None:
        """
        Enable all events from the eventSource identified by 'eventSource' to the current
        dispatcher that have a verbosity level of 'level' or lower and have a event keyword
        matching any of the bits in 'matchAnyKeyword'.
        
        This call can have the effect of REDUCING the number of events sent to the
        dispatcher if 'level' indicates a less verbose level than was previously enabled or
        if 'matchAnyKeyword' has fewer keywords set than where previously set.
        
        This call never has an effect on other EventListeners.
        """
        ...

    @overload
    def EnableEvents(self, eventSource: System.Diagnostics.Tracing.EventSource, level: System.Diagnostics.Tracing.EventLevel, matchAnyKeyword: System.Diagnostics.Tracing.EventKeywords, arguments: System.Collections.Generic.IDictionary[str, str]) -> None:
        """
        Enable all events from the eventSource identified by 'eventSource' to the current
        dispatcher that have a verbosity level of 'level' or lower and have a event keyword
        matching any of the bits in 'matchAnyKeyword' as well as any (eventSource specific)
        effect passing additional 'key-value' arguments 'arguments' might have.
        
        This call can have the effect of REDUCING the number of events sent to the
        dispatcher if 'level' indicates a less verbose level than was previously enabled or
        if 'matchAnyKeyword' has fewer keywords set than where previously set.
        
        This call never has an effect on other EventListeners.
        """
        ...


class EventSourceAttribute(System.Attribute):
    """Allows customizing defaults and specifying localization support for the event source class to which it is applied."""

    @property
    def Name(self) -> str:
        """Overrides the ETW name of the event source (which defaults to the class name)"""
        ...

    @Name.setter
    def Name(self, value: str):
        """Overrides the ETW name of the event source (which defaults to the class name)"""
        ...

    @property
    def Guid(self) -> str:
        """
        Overrides the default (calculated) Guid of an EventSource type. Explicitly defining a GUID is discouraged,
        except when upgrading existing ETW providers to using event sources.
        """
        ...

    @Guid.setter
    def Guid(self, value: str):
        """
        Overrides the default (calculated) Guid of an EventSource type. Explicitly defining a GUID is discouraged,
        except when upgrading existing ETW providers to using event sources.
        """
        ...

    @property
    def LocalizationResources(self) -> str:
        """
        EventSources support localization of events. The names used for events, opcodes, tasks, keywords and maps
        can be localized to several languages if desired. This works by creating a ResX style string table
        (by simply adding a 'Resource File' to your project). This resource file is given a name e.g.
        'DefaultNameSpace.ResourceFileName' which can be passed to the ResourceManager constructor to read the
        resources. This name is the value of the LocalizationResources property.
        
        If LocalizationResources property is non-null, then EventSource will look up the localized strings for events by
        using the following resource naming scheme
        * event_EVENTNAME* task_TASKNAME* keyword_KEYWORDNAME* map_MAPNAME
        where the capitalized name is the name of the event, task, keyword, or map value that should be localized.
        Note that the localized string for an event corresponds to the Message string, and can have {0} values
        which represent the payload values.
        """
        ...

    @LocalizationResources.setter
    def LocalizationResources(self, value: str):
        """
        EventSources support localization of events. The names used for events, opcodes, tasks, keywords and maps
        can be localized to several languages if desired. This works by creating a ResX style string table
        (by simply adding a 'Resource File' to your project). This resource file is given a name e.g.
        'DefaultNameSpace.ResourceFileName' which can be passed to the ResourceManager constructor to read the
        resources. This name is the value of the LocalizationResources property.
        
        If LocalizationResources property is non-null, then EventSource will look up the localized strings for events by
        using the following resource naming scheme
        * event_EVENTNAME* task_TASKNAME* keyword_KEYWORDNAME* map_MAPNAME
        where the capitalized name is the name of the event, task, keyword, or map value that should be localized.
        Note that the localized string for an event corresponds to the Message string, and can have {0} values
        which represent the payload values.
        """
        ...


class EventAttribute(System.Attribute):
    """
    Any instance methods in a class that subclasses EventSource and that return void are
    assumed by default to be methods that generate an ETW event. Enough information can be deduced from the
    name of the method and its signature to generate basic schema information for the event. The
    EventAttribute class allows you to specify additional event schema information for an event if
    desired.
    """

    @property
    def EventId(self) -> int:
        """Event's ID"""
        ...

    @EventId.setter
    def EventId(self, value: int):
        """Event's ID"""
        ...

    @property
    def Level(self) -> int:
        """
        Event's severity level: indicates the severity or verbosity of the event
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventLevel enum.
        """
        ...

    @Level.setter
    def Level(self, value: int):
        """
        Event's severity level: indicates the severity or verbosity of the event
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventLevel enum.
        """
        ...

    @property
    def Keywords(self) -> int:
        """
        Event's keywords: allows classification of events by "categories"
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventKeywords enum.
        """
        ...

    @Keywords.setter
    def Keywords(self, value: int):
        """
        Event's keywords: allows classification of events by "categories"
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventKeywords enum.
        """
        ...

    @property
    def Opcode(self) -> int:
        """
        Event's operation code: allows defining operations, generally used with Tasks
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventOpcode enum.
        """
        ...

    @Opcode.setter
    def Opcode(self, value: int):
        """
        Event's operation code: allows defining operations, generally used with Tasks
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventOpcode enum.
        """
        ...

    @property
    def IsOpcodeSet(self) -> bool:
        ...

    @property
    def Task(self) -> int:
        """
        Event's task: allows logical grouping of events
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventTask enum.
        """
        ...

    @Task.setter
    def Task(self, value: int):
        """
        Event's task: allows logical grouping of events
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventTask enum.
        """
        ...

    @property
    def Version(self) -> int:
        ...

    @Version.setter
    def Version(self, value: int):
        ...

    @property
    def Message(self) -> str:
        """
        This can be specified to enable formatting and localization of the event's payload. You can
        use standard .NET substitution operators (eg {1}) in the string and they will be replaced
        with the 'ToString()' of the corresponding part of the  event payload.
        """
        ...

    @Message.setter
    def Message(self, value: str):
        """
        This can be specified to enable formatting and localization of the event's payload. You can
        use standard .NET substitution operators (eg {1}) in the string and they will be replaced
        with the 'ToString()' of the corresponding part of the  event payload.
        """
        ...

    @property
    def Tags(self) -> int:
        """
        User defined options associated with the event.  These do not have meaning to the EventSource but
        are passed through to listeners which given them semantics.
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventTags enum.
        """
        ...

    @Tags.setter
    def Tags(self, value: int):
        """
        User defined options associated with the event.  These do not have meaning to the EventSource but
        are passed through to listeners which given them semantics.
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventTags enum.
        """
        ...

    @property
    def ActivityOptions(self) -> int:
        """
        Allows fine control over the Activity IDs generated by start and stop events
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventActivityOptions enum.
        """
        ...

    @ActivityOptions.setter
    def ActivityOptions(self, value: int):
        """
        Allows fine control over the Activity IDs generated by start and stop events
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventActivityOptions enum.
        """
        ...

    def __init__(self, eventId: int) -> None:
        """
        Construct an EventAttribute with specified eventId
        
        :param eventId: ID of the ETW event (an integer between 1 and 65535)
        """
        ...


class NonEventAttribute(System.Attribute):
    """
    By default all instance methods in a class that subclasses code:EventSource that and return
    void are assumed to be methods that generate an event. This default can be overridden by specifying
    the code:NonEventAttribute
    """

    def __init__(self) -> None:
        """Constructs a default NonEventAttribute"""
        ...


class EventSourceException(System.Exception):
    """Exception that is thrown when an error occurs during EventSource operation."""

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the EventSourceException class."""
        ...

    @overload
    def __init__(self, message: str) -> None:
        """Initializes a new instance of the EventSourceException class with a specified error message."""
        ...

    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None:
        """
        Initializes a new instance of the EventSourceException class with a specified error message
        and a reference to the inner exception that is the cause of this exception.
        """
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        Initializes a new instance of the EventSourceException class with serialized data.
        
        This method is protected.
        """
        ...


class IncrementingEventCounter(System.Diagnostics.Tracing.DiagnosticCounter):
    """
    IncrementingEventCounter is a variant of EventCounter for variables that are ever-increasing.
    Ex) # of exceptions in the runtime.
    It does not calculate statistics like mean, standard deviation, etc. because it only accumulates
    the counter value.
    """

    @property
    def DisplayRateTimeScale(self) -> datetime.timedelta:
        ...

    @DisplayRateTimeScale.setter
    def DisplayRateTimeScale(self, value: datetime.timedelta):
        ...

    def __init__(self, name: str, eventSource: System.Diagnostics.Tracing.EventSource) -> None:
        """
        Initializes a new instance of the IncrementingEventCounter class.
        IncrementingEventCounter live as long as the EventSource that they are attached to unless they are
        explicitly Disposed.
        
        :param name: The name.
        :param eventSource: The event source.
        """
        ...

    def Increment(self, increment: float = 1) -> None:
        """
        Writes 'value' to the stream of values tracked by the counter.  This updates the sum and other statistics that will
        be logged on the next timer interval.
        
        :param increment: The value to increment by.
        """
        ...

    def ToString(self) -> str:
        ...


class EventCounter(System.Diagnostics.Tracing.DiagnosticCounter):
    """
    Provides the ability to collect statistics through EventSource
    
    See https://github.com/dotnet/runtime/blob/main/src/libraries/System.Diagnostics.Tracing/documentation/EventCounterTutorial.md
    for a tutorial guide.
    
    See https://github.com/dotnet/runtime/blob/main/src/libraries/System.Diagnostics.Tracing/tests/BasicEventSourceTest/TestEventCounter.cs
    which shows tests, which are also useful in seeing actual use.
    """

    def __init__(self, name: str, eventSource: System.Diagnostics.Tracing.EventSource) -> None:
        """
        Initializes a new instance of the EventCounter class.
        EVentCounters live as long as the EventSource that they are attached to unless they are
        explicitly Disposed.
        
        :param name: The name.
        :param eventSource: The event source.
        """
        ...

    def ToString(self) -> str:
        ...

    @overload
    def WriteMetric(self, value: float) -> None:
        """
        Writes 'value' to the stream of values tracked by the counter.  This updates the sum and other statistics that will
        be logged on the next timer interval.
        
        :param value: The value.
        """
        ...

    @overload
    def WriteMetric(self, value: float) -> None:
        ...


class EventTask(System.Enum):
    """WindowsEventTask. Custom values must be in the range from 1 through 65534"""

    # Cannot convert to Python: None = 0
    """Undefined task"""


class EventOpcode(System.Enum):
    """EventOpcode. Custom values must be in the range from 11 through 239"""

    Info = 0
    """An informational event"""

    Start = 1
    """An activity start event"""

    Stop = 2
    """An activity end event"""

    DataCollectionStart = 3
    """A trace collection start event"""

    DataCollectionStop = 4
    """A trace collection end event"""

    Extension = 5
    """An extensional event"""

    Reply = 6
    """A reply event"""

    Resume = 7
    """An event representing the activity resuming from the suspension"""

    Suspend = 8
    """An event representing the activity is suspended, pending another activity's completion"""

    Send = 9
    """An event representing the activity is transferred to another component, and can continue to work"""

    Receive = 240
    """An event representing receiving an activity transfer from another component"""


class EventFieldFormat(System.Enum):
    """
    Provides a hint that may be used by an event listener when formatting
    an event field for display. Note that the event listener may ignore the
    hint if it does not recognize a particular combination of type and format.
    Similar to TDH_OUTTYPE.
    """

    Default = 0
    """Field receives default formatting based on the field's underlying type."""

    String = 2

    Boolean = 3
    """
    Field should be formatted as boolean data. Typically applied to 8-bit
    or 32-bit integers. This is the default format for the Boolean type.
    """

    Hexadecimal = 4
    """
    Field should be formatted as hexadecimal data. Typically applied to
    integer types.
    """

    Xml = 11

    Json = 12
    """
    Field should be formatted as JSON string data. Typically applied to
    strings or arrays of 8-bit or 16-bit integers.
    """

    HResult = 15


class EventIgnoreAttribute(System.Attribute):
    """
    Used when authoring types that will be passed to EventSource.Write.
    By default, EventSource.Write will write all of an object's public
    properties to the event payload. Apply [EventIgnore] to a public
    property to prevent EventSource.Write from including the property in
    the event.
    """


class EventFieldTags(System.Enum):
    """
    Tags are flags that are not interpreted by EventSource but are passed along
    to the EventListener. The EventListener determines the semantics of the flags.
    """

    # Cannot convert to Python: None = 0
    """No special traits are added to the field."""


class EventFieldAttribute(System.Attribute):
    """
    TraceLogging: used when authoring types that will be passed to EventSource.Write.
    Controls how a field or property is handled when it is written as a
    field in a TraceLogging event. Apply this attribute to a field or
    property if the default handling is not correct. (Apply the
    TraceLoggingIgnore attribute if the property should not be
    included as a field in the event.)
    The default for Name is null, which means that the name of the
    underlying field or property will be used as the event field's name.
    The default for PiiTag is 0, which means that the event field does not
    contain personally-identifiable information.
    """

    @property
    def Tags(self) -> int:
        """
        User defined options for the field. These are not interpreted by the EventSource
        but are available to the Listener. See EventFieldSettings for details
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventFieldTags enum.
        """
        ...

    @Tags.setter
    def Tags(self, value: int):
        """
        User defined options for the field. These are not interpreted by the EventSource
        but are available to the Listener. See EventFieldSettings for details
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventFieldTags enum.
        """
        ...

    @property
    def Name(self) -> str:
        """
        Gets or sets the name to use for the field. This defaults to null.
        If null, the name of the corresponding property will be used
        as the event field's name.
        TODO REMOVE
        """
        ...

    @Name.setter
    def Name(self, value: str):
        """
        Gets or sets the name to use for the field. This defaults to null.
        If null, the name of the corresponding property will be used
        as the event field's name.
        TODO REMOVE
        """
        ...

    @property
    def Format(self) -> int:
        """
        Gets or sets a field formatting hint.
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventFieldFormat enum.
        """
        ...

    @Format.setter
    def Format(self, value: int):
        """
        Gets or sets a field formatting hint.
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventFieldFormat enum.
        """
        ...


class EventDataAttribute(System.Attribute):
    """
    Used when authoring types that will be passed to EventSource.Write.
    EventSource.Write<T> only works when T is either an anonymous type
    or a type with an [EventData] attribute. In addition, the properties
    of T must be supported property types. Supported property types include
    simple built-in types (int, string, Guid, DateTime, DateTimeOffset,
    KeyValuePair, etc.), anonymous types that only contain supported types,
    types with an [EventData] attribute, arrays of the above, and IEnumerable
    of the above.
    """

    @property
    def Name(self) -> str:
        """
        Gets or sets the name to use if this type is used for an
        implicitly-named event or an implicitly-named property.
        
        Example 1:
        
            EventSource.Write(null, new T()); // implicitly-named event
        
        The name of the event will be determined as follows:
        
        if (T has an EventData attribute and attribute.Name != null)
            eventName = attribute.Name;
        else
            eventName = typeof(T).Name;
        
        Example 2:
        
            EventSource.Write(name, new { _1 = new T() }); // implicitly-named field
        
        The name of the field will be determined as follows:
        
        if (T has an EventData attribute and attribute.Name != null)
            fieldName = attribute.Name;
        else
            fieldName = typeof(T).Name;
        """
        ...

    @Name.setter
    def Name(self, value: str):
        """
        Gets or sets the name to use if this type is used for an
        implicitly-named event or an implicitly-named property.
        
        Example 1:
        
            EventSource.Write(null, new T()); // implicitly-named event
        
        The name of the event will be determined as follows:
        
        if (T has an EventData attribute and attribute.Name != null)
            eventName = attribute.Name;
        else
            eventName = typeof(T).Name;
        
        Example 2:
        
            EventSource.Write(name, new { _1 = new T() }); // implicitly-named field
        
        The name of the field will be determined as follows:
        
        if (T has an EventData attribute and attribute.Name != null)
            fieldName = attribute.Name;
        else
            fieldName = typeof(T).Name;
        """
        ...

    @property
    def Level(self) -> int:
        """
        Gets or sets the level to use for the event.
        Invalid levels (outside the range 0..255) are treated as unset.
        Note that the Level attribute can bubble-up, i.e. if a type contains
        a sub-object (a field or property), and the sub-object's type has a
        TraceLoggingEvent attribute, the Level from the sub-object's attribute
        can affect the event's level.
        
        Example: for EventSource.Write(name, options, data), the level of the
        event will be determined as follows:
        
        if (options.Level has been set)
            eventLevel = options.Level;
        else if (data.GetType() has a TraceLoggingEvent attribute and attribute.Level has been set)
            eventLevel = attribute.Level;
        else if (a field/property contained in data has a TraceLoggingEvent attribute and attribute.Level has been set)
            eventLevel = attribute.Level;
        else
            eventLevel = EventLevel.LogAlways;
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventLevel enum.
        """
        ...

    @Level.setter
    def Level(self, value: int):
        """
        Gets or sets the level to use for the event.
        Invalid levels (outside the range 0..255) are treated as unset.
        Note that the Level attribute can bubble-up, i.e. if a type contains
        a sub-object (a field or property), and the sub-object's type has a
        TraceLoggingEvent attribute, the Level from the sub-object's attribute
        can affect the event's level.
        
        Example: for EventSource.Write(name, options, data), the level of the
        event will be determined as follows:
        
        if (options.Level has been set)
            eventLevel = options.Level;
        else if (data.GetType() has a TraceLoggingEvent attribute and attribute.Level has been set)
            eventLevel = attribute.Level;
        else if (a field/property contained in data has a TraceLoggingEvent attribute and attribute.Level has been set)
            eventLevel = attribute.Level;
        else
            eventLevel = EventLevel.LogAlways;
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventLevel enum.
        """
        ...

    @property
    def Opcode(self) -> int:
        """
        Gets or sets the opcode to use for the event.
        Invalid opcodes (outside the range 0..255) are treated as unset.
        Note that the Opcode attribute can bubble-up, i.e. if a type contains
        a sub-object (a field or property), and the sub-object's type has a
        TraceLoggingEvent attribute, the Opcode from the sub-object's attribute
        can affect the event's opcode.
        
        Example: for EventSource.Write(name, options, data), the opcode of the
        event will be determined as follows:
        
        if (options.Opcode has been set)
            eventOpcode = options.Opcode;
        else if (data.GetType() has a TraceLoggingEvent attribute and attribute.Opcode has been set)
            eventOpcode = attribute.Opcode;
        else if (a field/property contained in data has a TraceLoggingEvent attribute and attribute.Opcode has been set)
            eventOpcode = attribute.Opcode;
        else
            eventOpcode = EventOpcode.Info;
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventOpcode enum.
        """
        ...

    @Opcode.setter
    def Opcode(self, value: int):
        """
        Gets or sets the opcode to use for the event.
        Invalid opcodes (outside the range 0..255) are treated as unset.
        Note that the Opcode attribute can bubble-up, i.e. if a type contains
        a sub-object (a field or property), and the sub-object's type has a
        TraceLoggingEvent attribute, the Opcode from the sub-object's attribute
        can affect the event's opcode.
        
        Example: for EventSource.Write(name, options, data), the opcode of the
        event will be determined as follows:
        
        if (options.Opcode has been set)
            eventOpcode = options.Opcode;
        else if (data.GetType() has a TraceLoggingEvent attribute and attribute.Opcode has been set)
            eventOpcode = attribute.Opcode;
        else if (a field/property contained in data has a TraceLoggingEvent attribute and attribute.Opcode has been set)
            eventOpcode = attribute.Opcode;
        else
            eventOpcode = EventOpcode.Info;
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventOpcode enum.
        """
        ...

    @property
    def Keywords(self) -> int:
        """
        Gets or sets the keywords to use for the event.
        Note that the Keywords attribute can bubble-up, i.e. if a type contains
        a sub-object (a field or property), and the sub-object's type has a
        TraceLoggingEvent attribute, the Keywords from the sub-object's attribute
        can affect the event's keywords.
        
        Example: for EventSource.Write(name, options, data), the keywords of the
        event will be determined as follows:
        
        eventKeywords = options.Keywords;
        if (data.GetType() has a TraceLoggingEvent attribute)
            eventKeywords |= attribute.Keywords;
        if (a field/property contained in data has a TraceLoggingEvent attribute)
            eventKeywords |= attribute.Keywords;
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventKeywords enum.
        """
        ...

    @Keywords.setter
    def Keywords(self, value: int):
        """
        Gets or sets the keywords to use for the event.
        Note that the Keywords attribute can bubble-up, i.e. if a type contains
        a sub-object (a field or property), and the sub-object's type has a
        TraceLoggingEvent attribute, the Keywords from the sub-object's attribute
        can affect the event's keywords.
        
        Example: for EventSource.Write(name, options, data), the keywords of the
        event will be determined as follows:
        
        eventKeywords = options.Keywords;
        if (data.GetType() has a TraceLoggingEvent attribute)
            eventKeywords |= attribute.Keywords;
        if (a field/property contained in data has a TraceLoggingEvent attribute)
            eventKeywords |= attribute.Keywords;
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventKeywords enum.
        """
        ...

    @property
    def Tags(self) -> int:
        """
        Gets or sets the flags for an event. These flags are ignored by ETW,
        but can have meaning to the event consumer.
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventTags enum.
        """
        ...

    @Tags.setter
    def Tags(self, value: int):
        """
        Gets or sets the flags for an event. These flags are ignored by ETW,
        but can have meaning to the event consumer.
        
        This property contains the int value of a member of the System.Diagnostics.Tracing.EventTags enum.
        """
        ...


class _EventContainer(typing.Generic[System_Diagnostics_Tracing__EventContainer_Callable, System_Diagnostics_Tracing__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_Diagnostics_Tracing__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_Diagnostics_Tracing__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_Diagnostics_Tracing__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


