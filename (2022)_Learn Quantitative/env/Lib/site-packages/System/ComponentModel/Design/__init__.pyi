from typing import overload
import abc
import typing

import System
import System.Collections
import System.ComponentModel
import System.ComponentModel.Design
import System.Globalization
import System.IO
import System.Reflection
import System.Resources
import System.Runtime.InteropServices
import System.Runtime.Serialization

IServiceProvider = typing.Any

System_ComponentModel_Design__EventContainer_Callable = typing.TypeVar("System_ComponentModel_Design__EventContainer_Callable")
System_ComponentModel_Design__EventContainer_ReturnType = typing.TypeVar("System_ComponentModel_Design__EventContainer_ReturnType")


class TypeDescriptionProviderService(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @overload
    def GetProvider(self, instance: typing.Any) -> System.ComponentModel.TypeDescriptionProvider:
        ...

    @overload
    def GetProvider(self, type: typing.Type) -> System.ComponentModel.TypeDescriptionProvider:
        ...


class IDictionaryService(metaclass=abc.ABCMeta):
    """
    Provides a generic dictionary service that a designer can use
    to store user-defined data on the site.
    """

    def GetKey(self, value: typing.Any) -> System.Object:
        """Gets the key corresponding to the specified value."""
        ...

    def GetValue(self, key: typing.Any) -> System.Object:
        """Gets the value corresponding to the specified key."""
        ...

    def SetValue(self, key: typing.Any, value: typing.Any) -> None:
        """Sets the specified key-value pair."""
        ...


class IEventBindingService(metaclass=abc.ABCMeta):
    """Provides a set of useful methods for binding System.ComponentModel.EventDescriptor objects to user code."""

    def CreateUniqueMethodName(self, component: System.ComponentModel.IComponent, e: System.ComponentModel.EventDescriptor) -> str:
        """
        This creates a name for an event handling method for the given component
        and event. The name that is created is guaranteed to be unique in the user's source
        code.
        """
        ...

    def GetCompatibleMethods(self, e: System.ComponentModel.EventDescriptor) -> System.Collections.ICollection:
        """
        Retrieves a collection of strings. Each string is the name of a method
        in user code that has a signature that is compatible with the given event.
        """
        ...

    def GetEvent(self, property: System.ComponentModel.PropertyDescriptor) -> System.ComponentModel.EventDescriptor:
        """
        For properties that are representing events, this will return the event
        that the property represents.
        """
        ...

    def GetEventProperties(self, events: System.ComponentModel.EventDescriptorCollection) -> System.ComponentModel.PropertyDescriptorCollection:
        """Converts a set of event descriptors to a set of property descriptors."""
        ...

    def GetEventProperty(self, e: System.ComponentModel.EventDescriptor) -> System.ComponentModel.PropertyDescriptor:
        """Converts a single event to a property."""
        ...

    @overload
    def ShowCode(self) -> bool:
        """
        Displays the user code for the designer. This will return true if the user
        code could be displayed, or false otherwise.
        """
        ...

    @overload
    def ShowCode(self, lineNumber: int) -> bool:
        """
        Displays the user code for the designer. This will return true if the user
        code could be displayed, or false otherwise.
        """
        ...

    @overload
    def ShowCode(self, component: System.ComponentModel.IComponent, e: System.ComponentModel.EventDescriptor) -> bool:
        """
        Displays the user code for the given event. This will return true if the user
        code could be displayed, or false otherwise.
        """
        ...


class DesigntimeLicenseContext(System.ComponentModel.LicenseContext):
    """Provides design-time support for licensing."""

    @property
    def _savedLicenseKeys(self) -> System.Collections.Hashtable:
        ...

    @_savedLicenseKeys.setter
    def _savedLicenseKeys(self, value: System.Collections.Hashtable):
        ...

    @property
    def UsageMode(self) -> int:
        """
        Gets or sets the license usage mode.
        
        This property contains the int value of a member of the System.ComponentModel.LicenseUsageMode enum.
        """
        ...

    def GetSavedLicenseKey(self, type: typing.Type, resourceAssembly: System.Reflection.Assembly) -> str:
        """Gets a saved license key."""
        ...

    def SetSavedLicenseKey(self, type: typing.Type, key: str) -> None:
        """Sets a saved license key."""
        ...


class IServiceContainer(IServiceProvider, metaclass=abc.ABCMeta):
    """
    This interface provides a container for services. A service container
    is, by definition, a service provider. In addition to providing services
    it also provides a mechanism for adding and removing services.
    """

    @overload
    def AddService(self, serviceType: typing.Type, serviceInstance: typing.Any) -> None:
        """Adds the given service to the service container."""
        ...

    @overload
    def AddService(self, serviceType: typing.Type, serviceInstance: typing.Any, promote: bool) -> None:
        """Adds the given service to the service container."""
        ...

    @overload
    def AddService(self, serviceType: typing.Type, callback: typing.Callable[[System.ComponentModel.Design.IServiceContainer, typing.Type], System.Object]) -> None:
        """Adds the given service to the service container."""
        ...

    @overload
    def AddService(self, serviceType: typing.Type, callback: typing.Callable[[System.ComponentModel.Design.IServiceContainer, typing.Type], System.Object], promote: bool) -> None:
        """Adds the given service to the service container."""
        ...

    @overload
    def RemoveService(self, serviceType: typing.Type) -> None:
        """Removes the given service type from the service container."""
        ...

    @overload
    def RemoveService(self, serviceType: typing.Type, promote: bool) -> None:
        """Removes the given service type from the service container."""
        ...


class DesignerTransaction(System.Object, System.IDisposable, metaclass=abc.ABCMeta):
    """
    Identifies a transaction within a designer. Transactions are
    used to wrap several changes into one unit of work, which
    helps performance.
    """

    @property
    def Canceled(self) -> bool:
        ...

    @Canceled.setter
    def Canceled(self, value: bool):
        ...

    @property
    def Committed(self) -> bool:
        ...

    @Committed.setter
    def Committed(self, value: bool):
        ...

    @property
    def Description(self) -> str:
        ...

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, description: str) -> None:
        """This method is protected."""
        ...

    def Cancel(self) -> None:
        ...

    def Commit(self) -> None:
        """
        Commits this transaction. Once a transaction has been committed, further
        calls to this method will do nothing. You should always call this method
        after creating a transaction to ensure that the transaction is closed properly.
        """
        ...

    @overload
    def Dispose(self) -> None:
        """
        Private implementation of IDisaposable. When a transaction is disposed
        it is committed.
        """
        ...

    @overload
    def Dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def OnCancel(self) -> None:
        """
        User code should implement this method to perform the actual work of
        committing a transaction.
        
        This method is protected.
        """
        ...

    def OnCommit(self) -> None:
        """
        User code should implement this method to perform the actual work of
        committing a transaction.
        
        This method is protected.
        """
        ...


class CommandID(System.Object):
    """
    Represents a numeric Command ID and globally unique ID (GUID) menu
    identifier that together uniquely identify a command.
    """

    @property
    def ID(self) -> int:
        """Gets or sets the numeric command ID."""
        ...

    @property
    def Guid(self) -> System.Guid:
        """
        Gets or sets the globally unique ID (GUID) of the menu group that the
        menu command this CommandID represents belongs to.
        """
        ...

    def __init__(self, menuGroup: System.Guid, commandID: int) -> None:
        """
        Initializes a new instance of the System.ComponentModel.Design.CommandID
        class. Creates a new command ID.
        """
        ...

    def Equals(self, obj: typing.Any) -> bool:
        """Overrides Object's Equals method."""
        ...

    def GetHashCode(self) -> int:
        ...

    def ToString(self) -> str:
        """Overrides Object's ToString method."""
        ...


class MenuCommand(System.Object):
    """Represents a Windows menu or toolbar item."""

    @property
    def Checked(self) -> bool:
        """Gets or sets a value indicating whether this menu item is checked."""
        ...

    @Checked.setter
    def Checked(self, value: bool):
        """Gets or sets a value indicating whether this menu item is checked."""
        ...

    @property
    def Enabled(self) -> bool:
        """Gets or sets a value indicating whether this menu item is available."""
        ...

    @Enabled.setter
    def Enabled(self, value: bool):
        """Gets or sets a value indicating whether this menu item is available."""
        ...

    @property
    def Properties(self) -> System.Collections.IDictionary:
        ...

    @property
    def Supported(self) -> bool:
        """Gets or sets a value indicating whether this menu item is supported."""
        ...

    @Supported.setter
    def Supported(self, value: bool):
        """Gets or sets a value indicating whether this menu item is supported."""
        ...

    @property
    def Visible(self) -> bool:
        """Gets or sets a value indicating if this menu item is visible."""
        ...

    @Visible.setter
    def Visible(self, value: bool):
        """Gets or sets a value indicating if this menu item is visible."""
        ...

    @property
    def CommandChanged(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Occurs when the menu command changes."""
        ...

    @CommandChanged.setter
    def CommandChanged(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]):
        """Occurs when the menu command changes."""
        ...

    @property
    def CommandID(self) -> System.ComponentModel.Design.CommandID:
        """Gets the System.ComponentModel.Design.CommandID associated with this menu command."""
        ...

    @property
    def OleStatus(self) -> int:
        """Gets the OLE command status code for this menu item."""
        ...

    def __init__(self, handler: typing.Callable[[System.Object, System.EventArgs], None], command: System.ComponentModel.Design.CommandID) -> None:
        """Initializes a new instance of System.ComponentModel.Design.MenuCommand."""
        ...

    @overload
    def Invoke(self) -> None:
        """Invokes a menu item."""
        ...

    @overload
    def Invoke(self, arg: typing.Any) -> None:
        """
        Invokes a menu item. The default implementation of this method ignores
        the argument, but deriving classes may override this method.
        """
        ...

    def OnCommandChanged(self, e: System.EventArgs) -> None:
        """
        Provides notification and is called in response to
        a System.ComponentModel.Design.MenuCommand.CommandChanged event.
        
        This method is protected.
        """
        ...

    def ToString(self) -> str:
        """Overrides object's ToString()."""
        ...


class DesignerVerb(System.ComponentModel.Design.MenuCommand):
    """Represents a verb that can be executed by a component's designer."""

    @property
    def Description(self) -> str:
        """Gets or sets the description of the menu item for the verb."""
        ...

    @Description.setter
    def Description(self, value: str):
        """Gets or sets the description of the menu item for the verb."""
        ...

    @property
    def Text(self) -> str:
        """Gets or sets the text to show on the menu item for the verb."""
        ...

    @overload
    def __init__(self, text: str, handler: typing.Callable[[System.Object, System.EventArgs], None]) -> None:
        """Initializes a new instance of the System.ComponentModel.Design.DesignerVerb class."""
        ...

    @overload
    def __init__(self, text: str, handler: typing.Callable[[System.Object, System.EventArgs], None], startCommandID: System.ComponentModel.Design.CommandID) -> None:
        """
        Initializes a new instance of the System.ComponentModel.Design.DesignerVerb
        class.
        """
        ...

    def ToString(self) -> str:
        """Overrides object's ToString()."""
        ...


class DesignerVerbCollection(System.Collections.CollectionBase):
    """This class has no documentation."""

    def __getitem__(self, index: int) -> System.ComponentModel.Design.DesignerVerb:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, value: typing.List[System.ComponentModel.Design.DesignerVerb]) -> None:
        ...

    def __setitem__(self, index: int, value: System.ComponentModel.Design.DesignerVerb) -> None:
        ...

    def Add(self, value: System.ComponentModel.Design.DesignerVerb) -> int:
        ...

    @overload
    def AddRange(self, value: typing.List[System.ComponentModel.Design.DesignerVerb]) -> None:
        ...

    @overload
    def AddRange(self, value: System.ComponentModel.Design.DesignerVerbCollection) -> None:
        ...

    def Contains(self, value: System.ComponentModel.Design.DesignerVerb) -> bool:
        ...

    def CopyTo(self, array: typing.List[System.ComponentModel.Design.DesignerVerb], index: int) -> None:
        ...

    def IndexOf(self, value: System.ComponentModel.Design.DesignerVerb) -> int:
        ...

    def Insert(self, index: int, value: System.ComponentModel.Design.DesignerVerb) -> None:
        ...

    def OnValidate(self, value: typing.Any) -> None:
        """This method is protected."""
        ...

    def Remove(self, value: System.ComponentModel.Design.DesignerVerb) -> None:
        ...


class IDesigner(System.IDisposable, metaclass=abc.ABCMeta):
    """
    Provides the basic framework for building a custom designer.
    This interface stores the verbs available to the designer, as well as basic
    services for the designer.
    """

    @property
    @abc.abstractmethod
    def Component(self) -> System.ComponentModel.IComponent:
        """Gets or sets the base component this designer is designing."""
        ...

    @property
    @abc.abstractmethod
    def Verbs(self) -> System.ComponentModel.Design.DesignerVerbCollection:
        """Gets or sets the design-time verbs supported by the designer."""
        ...

    def DoDefaultAction(self) -> None:
        """Performs the default action for this designer."""
        ...

    def Initialize(self, component: System.ComponentModel.IComponent) -> None:
        """Initializes the designer with the given component."""
        ...


class DesignerTransactionCloseEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def TransactionCommitted(self) -> bool:
        ...

    @property
    def LastTransaction(self) -> bool:
        ...

    @overload
    def __init__(self, commit: bool, lastTransaction: bool) -> None:
        """
        Creates a new event args. Commit is true if the transaction is committed, and
        lastTransaction is true if this is the last transaction to close.
        """
        ...

    @overload
    def __init__(self, commit: bool) -> None:
        """
        Creates a new event args. Commit is true if the transaction is committed. This
        defaults the LastTransaction property to true.
        
        This constructor has been deprecated. Use DesignerTransactionCloseEventArgs(bool, bool) instead.
        """
        ...


class IDesignerHost(System.ComponentModel.Design.IServiceContainer, metaclass=abc.ABCMeta):
    """
    Provides methods to adjust the configuration of and retrieve
    information about the services and behavior of a designer.
    """

    @property
    @abc.abstractmethod
    def Loading(self) -> bool:
        """
        Gets or sets a value indicating whether the designer host
        is currently loading the document.
        """
        ...

    @property
    @abc.abstractmethod
    def InTransaction(self) -> bool:
        """Gets a value indicating whether the designer host is currently in a transaction."""
        ...

    @property
    @abc.abstractmethod
    def Container(self) -> System.ComponentModel.IContainer:
        """Gets the container for this designer host."""
        ...

    @property
    @abc.abstractmethod
    def RootComponent(self) -> System.ComponentModel.IComponent:
        """Gets the instance of the base class used as the base class for the current design."""
        ...

    @property
    @abc.abstractmethod
    def RootComponentClassName(self) -> str:
        """Gets the fully qualified name of the class that is being designed."""
        ...

    @property
    @abc.abstractmethod
    def TransactionDescription(self) -> str:
        """Gets the description of the current transaction."""
        ...

    @property
    @abc.abstractmethod
    def Activated(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IDesignerHost.Activated event."""
        ...

    @Activated.setter
    @abc.abstractmethod
    def Activated(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]):
        """Adds an event handler for the System.ComponentModel.Design.IDesignerHost.Activated event."""
        ...

    @property
    @abc.abstractmethod
    def Deactivated(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IDesignerHost.Deactivated event."""
        ...

    @Deactivated.setter
    @abc.abstractmethod
    def Deactivated(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]):
        """Adds an event handler for the System.ComponentModel.Design.IDesignerHost.Deactivated event."""
        ...

    @property
    @abc.abstractmethod
    def LoadComplete(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IDesignerHost.LoadComplete event."""
        ...

    @LoadComplete.setter
    @abc.abstractmethod
    def LoadComplete(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]):
        """Adds an event handler for the System.ComponentModel.Design.IDesignerHost.LoadComplete event."""
        ...

    @property
    @abc.abstractmethod
    def TransactionClosed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerTransactionCloseEventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IDesignerHost.TransactionClosed event."""
        ...

    @TransactionClosed.setter
    @abc.abstractmethod
    def TransactionClosed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerTransactionCloseEventArgs], None], None]):
        """Adds an event handler for the System.ComponentModel.Design.IDesignerHost.TransactionClosed event."""
        ...

    @property
    @abc.abstractmethod
    def TransactionClosing(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerTransactionCloseEventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IDesignerHost.TransactionClosing event."""
        ...

    @TransactionClosing.setter
    @abc.abstractmethod
    def TransactionClosing(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerTransactionCloseEventArgs], None], None]):
        """Adds an event handler for the System.ComponentModel.Design.IDesignerHost.TransactionClosing event."""
        ...

    @property
    @abc.abstractmethod
    def TransactionOpened(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IDesignerHost.TransactionOpened event."""
        ...

    @TransactionOpened.setter
    @abc.abstractmethod
    def TransactionOpened(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]):
        """Adds an event handler for the System.ComponentModel.Design.IDesignerHost.TransactionOpened event."""
        ...

    @property
    @abc.abstractmethod
    def TransactionOpening(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IDesignerHost.TransactionOpening event."""
        ...

    @TransactionOpening.setter
    @abc.abstractmethod
    def TransactionOpening(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]):
        """Adds an event handler for the System.ComponentModel.Design.IDesignerHost.TransactionOpening event."""
        ...

    def Activate(self) -> None:
        """Activates the designer that this host is hosting."""
        ...

    @overload
    def CreateComponent(self, componentClass: typing.Type) -> System.ComponentModel.IComponent:
        """Creates a component of the specified class type."""
        ...

    @overload
    def CreateComponent(self, componentClass: typing.Type, name: str) -> System.ComponentModel.IComponent:
        """Creates a component of the given class type and name and places it into the designer container."""
        ...

    @overload
    def CreateTransaction(self) -> System.ComponentModel.Design.DesignerTransaction:
        """
        Lengthy operations that involve multiple components may raise many events. These events
        may cause other side-effects, such as flicker or performance degradation. When operating
        on multiple components at one time, or setting multiple properties on a single component,
        you should encompass these changes inside a transaction. Transactions are used
        to improve performance and reduce flicker. Slow operations can listen to
        transaction events and only do work when the transaction completes.
        """
        ...

    @overload
    def CreateTransaction(self, description: str) -> System.ComponentModel.Design.DesignerTransaction:
        """
        Lengthy operations that involve multiple components may raise many events. These events
        may cause other side-effects, such as flicker or performance degradation. When operating
        on multiple components at one time, or setting multiple properties on a single component,
        you should encompass these changes inside a transaction. Transactions are used
        to improve performance and reduce flicker. Slow operations can listen to
        transaction events and only do work when the transaction completes.
        """
        ...

    def DestroyComponent(self, component: System.ComponentModel.IComponent) -> None:
        """Destroys the given component, removing it from the design container."""
        ...

    def GetDesigner(self, component: System.ComponentModel.IComponent) -> System.ComponentModel.Design.IDesigner:
        """Gets the designer instance for the specified component."""
        ...

    def GetType(self, typeName: str) -> typing.Type:
        """Gets the type instance for the specified fully qualified type name ."""
        ...


class DesignerEventArgs(System.EventArgs):
    """
    Provides data for the System.ComponentModel.Design.IDesignerEventService.DesignerEvent
    event that is generated when a document is created or disposed.
    """

    @property
    def Designer(self) -> System.ComponentModel.Design.IDesignerHost:
        """Gets or sets the host of the document."""
        ...

    def __init__(self, host: System.ComponentModel.Design.IDesignerHost) -> None:
        """
        Initializes a new instance of the System.ComponentModel.Design.DesignerEventArgs
        class.
        """
        ...


class IReferenceService(metaclass=abc.ABCMeta):
    """
    Provides an interface to get names and references to objects. These
    methods can search using the specified name or reference.
    """

    def GetComponent(self, reference: typing.Any) -> System.ComponentModel.IComponent:
        """Gets the base component that anchors this reference."""
        ...

    def GetName(self, reference: typing.Any) -> str:
        """Gets the name for this reference."""
        ...

    def GetReference(self, name: str) -> System.Object:
        """Gets a reference for the specified name."""
        ...

    @overload
    def GetReferences(self) -> typing.List[System.Object]:
        """Gets all available references."""
        ...

    @overload
    def GetReferences(self, baseType: typing.Type) -> typing.List[System.Object]:
        """Gets all available references of this type."""
        ...


class IComponentInitializer(metaclass=abc.ABCMeta):
    """
    IComponentInitializer can be implemented on an object that also implements IDesigner.
    This interface allows a newly created component to be given some stock default values,
    such as a caption, default size, or other values. Recommended default values for
    the component's properties are passed in as a dictionary.
    """

    def InitializeExistingComponent(self, defaultValues: System.Collections.IDictionary) -> None:
        """
        This method is called when an existing component is being re-initialized. This may occur after
        dragging a component to another container, for example. The defaultValues
        property contains a name/value dictionary of default values that should be applied
        to properties. This dictionary may be null if no default values are specified.
        You may use the defaultValues dictionary to apply recommended defaults to properties
        but you should not modify component properties beyond what is stored in the
        dictionary, because this is an existing component that may already have properties
        set on it.
        """
        ...

    def InitializeNewComponent(self, defaultValues: System.Collections.IDictionary) -> None:
        """
        This method is called when a component is first initialized, typically after being first added
        to a design surface. The defaultValues property contains a name/value dictionary of default
        values that should be applied to properties. This dictionary may be null if no default values
        are specified. You may perform any initialization of this component that you like, and you
        may even ignore the defaultValues dictionary altogether if you wish.
        """
        ...


class DesigntimeLicenseContextSerializer(System.Object):
    """Provides support for design-time license context serialization."""

    BinaryWriterMagic: int = 255

    @staticmethod
    def Serialize(o: System.IO.Stream, cryptoKey: str, context: System.ComponentModel.Design.DesigntimeLicenseContext) -> None:
        """
        Serializes the licenses within the specified design-time license context
        using the specified key and output stream.
        """
        ...


class StandardToolWindows(System.Object):
    """
    Defines GUID specifiers that contain GUIDs which reference the standard set of tool windows that are available in
    the design environment.
    """

    ObjectBrowser: System.Guid = ...
    """Gets the GUID for the object browser."""

    OutputWindow: System.Guid = ...
    """Gets the GUID for the output window."""

    ProjectExplorer: System.Guid = ...
    """Gets the GUID for the project explorer."""

    PropertyBrowser: System.Guid = ...
    """Gets the GUID for the properties window."""

    RelatedLinks: System.Guid = ...
    """Gets the GUID for the related links frame."""

    ServerExplorer: System.Guid = ...
    """Gets the GUID for the server explorer."""

    TaskList: System.Guid = ...
    """Gets the GUID for the task list."""

    Toolbox: System.Guid = ...
    """Gets the GUID for the toolbox."""


class ActiveDesignerEventArgs(System.EventArgs):
    """
    Provides data for the System.ComponentModel.Design.IDesignerEventService.ActiveDesigner
    event.
    """

    @property
    def OldDesigner(self) -> System.ComponentModel.Design.IDesignerHost:
        """Gets or sets the document that is losing activation."""
        ...

    @property
    def NewDesigner(self) -> System.ComponentModel.Design.IDesignerHost:
        """Gets or sets the document that is gaining activation."""
        ...

    def __init__(self, oldDesigner: System.ComponentModel.Design.IDesignerHost, newDesigner: System.ComponentModel.Design.IDesignerHost) -> None:
        """
        Initializes a new instance of the System.ComponentModel.Design.ActiveDesignerEventArgs
        class.
        """
        ...


class SelectionTypes(System.Enum):
    """
    Specifies identifiers that indicate the type of selection for a component or
    group of components that are selected.
    """

    Auto = ...
    """
    A Normal selection. With this type of selection, the selection service responds
    to the control and shift keys to support appending or toggling components into the
    selection as needed.
    """

    Normal = ...
    """
    A Normal selection. With this type of selection, the selection service responds
    to the control and shift keys to support appending or toggling components into the
    selection as needed.
    
    SelectionTypes.Normal has been deprecated. Use SelectionTypes.Auto instead.
    """

    Replace = ...
    """
    A Replace selection. This causes the selection service to always replace the
    current selection with the replacement.
    """

    MouseDown = ...
    """
    A MouseDown selection. Happens when the user presses down on
    the mouse button when the pointer is over a control (or component). If a
    component in the selection list is already selected, it does not remove the
    existing selection, but promotes that component to be the primary selection.
    
    SelectionTypes.MouseDown has been deprecated and is not supported.
    """

    MouseUp = ...
    """
    A MouseUp selection. Happens when the user releases the
    mouse button when a control (or component) has been selected. If a component
    in the selection list is already selected, it does not remove the
    existing selection, but promotes that component to be the primary selection.
    
    SelectionTypes.MouseUp has been deprecated and is not supported.
    """

    Click = ...
    """
    A Click selection.
    Happens when a user clicks on a component. If a component in the selection list is already
    selected, it does not remove the existing selection, but promotes that component to be the
    primary selection.
    
    SelectionTypes.Click has been deprecated. Use SelectionTypes.Primary instead.
    """

    Primary = ...
    """
    A Primary selection.
    Happens when a user clicks on a component. If a component in the selection list is already
    selected, it does not remove the existing selection, but promotes that component to be the
    primary selection.
    """

    Toggle = ...
    """
    A toggle selection.
    This selection toggles the current selection with the provided selection. So, if
    a component is already selected and is passed into SetSelectedComponents with a
    selection type of Toggle, it will be unselected.
    """

    Add = ...
    """
    An Add selection.
    This selection adds the selected components to the current selection,
    maintaining the current set of selected components.
    """

    Remove = ...
    """
    A Remove selection.
    This selection removes the selected components from the current selection,
    maintaining the current set of selected components.
    """

    Valid = ...
    """
    Limits valid selection types to Normal, Replace, MouseDown, MouseUp,
    Click, Toggle or Add.
    
    SelectionTypes.Valid has been deprecated. Use Enum class methods to determine valid values, or use a type converter instead.
    """


class ComponentEventArgs(System.EventArgs):
    """
    Provides data for the System.ComponentModel.Design.IComponentChangeService.ComponentEvent
    event raised for component-level events.
    """

    @property
    def Component(self) -> System.ComponentModel.IComponent:
        """Gets or sets the component associated with the event."""
        ...

    def __init__(self, component: System.ComponentModel.IComponent) -> None:
        """Initializes a new instance of the System.ComponentModel.Design.ComponentEventArgs class."""
        ...


class IDesignerHostTransactionState(metaclass=abc.ABCMeta):
    """Methods for the Designer host to report on the state of transactions."""

    @property
    @abc.abstractmethod
    def IsClosingTransaction(self) -> bool:
        ...


class HelpKeywordAttribute(System.Attribute):
    """
    Allows specification of the context keyword that will be specified for this class or member. By default,
    the help keyword for a class is the Type's full name, and for a member it's the full name of the type that declared the property,
    plus the property name itself.
    
    For example, consider System.Windows.Forms.Button and it's Text property:
    
    The class keyword is "System.Windows.Forms.Button", but the Text property keyword is "System.Windows.Forms.Control.Text", because the Text
    property is declared on the System.Windows.Forms.Control class rather than the Button class itself; the Button class inherits the property.
    By contrast, the DialogResult property is declared on the Button so its keyword would be "System.Windows.Forms.Button.DialogResult".
    
    When the help system gets the keywords, it will first look at this attribute. At the class level, it will return the string specified by the
    HelpContextAttribute. Note this will not be used for members of the Type in question. They will still reflect the declaring Type's actual
    full name, plus the member name. To override this, place the attribute on the member itself.
    
    Example:
    
    [HelpKeywordAttribute(typeof(Component))]
    public class MyComponent : Component {
    
    
    public string Property1 { get{return "";};
    
    [HelpKeywordAttribute("SomeNamespace.SomeOtherClass.Property2")]
    public string Property2 { get{return "";};
    
    }
    
    
    For the above class (default without attribution):
    
    Class keyword: "System.ComponentModel.Component" ("MyNamespace.MyComponent')
    Property1 keyword: "MyNamespace.MyComponent.Property1" (default)
    Property2 keyword: "SomeNamespace.SomeOtherClass.Property2" ("MyNamespace.MyComponent.Property2")
    """

    Default: System.ComponentModel.Design.HelpKeywordAttribute = ...
    """Default value for HelpKeywordAttribute, which is null."""

    @property
    def HelpKeyword(self) -> str:
        """Retrieves the HelpKeyword this attribute supplies."""
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor, which creates an attribute with a null HelpKeyword."""
        ...

    @overload
    def __init__(self, keyword: str) -> None:
        """Creates a HelpKeywordAttribute with the value being the given keyword string."""
        ...

    @overload
    def __init__(self, t: typing.Type) -> None:
        """Creates a HelpKeywordAttribute with the value being the full name of the given type."""
        ...

    def Equals(self, obj: typing.Any) -> bool:
        """Two instances of a HelpKeywordAttribute are equal if they're HelpKeywords are equal."""
        ...

    def GetHashCode(self) -> int:
        """"""
        ...

    def IsDefaultAttribute(self) -> bool:
        """Returns true if this Attribute's HelpKeyword is null."""
        ...


class ComponentRenameEventArgs(System.EventArgs):
    """Provides data for the System.ComponentModel.Design.IComponentChangeService.ComponentRename event."""

    @property
    def Component(self) -> System.Object:
        """Gets or sets the component that is being renamed."""
        ...

    @property
    def OldName(self) -> str:
        """Gets or sets the name of the component before the rename."""
        ...

    @property
    def NewName(self) -> str:
        """Gets or sets the current name of the component."""
        ...

    def __init__(self, component: typing.Any, oldName: str, newName: str) -> None:
        """
        Initializes a new instance of the System.ComponentModel.Design.ComponentRenameEventArgs
        class.
        """
        ...


class DesignerCollection(System.Object, System.Collections.ICollection):
    """Provides a read-only collection of documents."""

    @property
    def Count(self) -> int:
        """Gets or sets the number of documents in the collection."""
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    def __getitem__(self, index: int) -> System.ComponentModel.Design.IDesignerHost:
        """Gets or sets the document at the specified index."""
        ...

    @overload
    def __init__(self, designers: typing.List[System.ComponentModel.Design.IDesignerHost]) -> None:
        """
        Initializes a new instance of the System.ComponentModel.Design.DesignerCollection class
        that stores an array with a pointer to each System.ComponentModel.Design.IDesignerHost
        for each document in the collection.
        """
        ...

    @overload
    def __init__(self, designers: System.Collections.IList) -> None:
        """
        Initializes a new instance of the System.ComponentModel.Design.DesignerCollection class
        that stores an array with a pointer to each System.ComponentModel.Design.IDesignerHost
        for each document in the collection.
        """
        ...

    def CopyTo(self, array: System.Array, index: int) -> None:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        """Creates and retrieves a new enumerator for this collection."""
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        ...


class ViewTechnology(System.Enum):
    """Specifies a set of technologies designer hosts should support."""

    Passthrough = 0
    """
    Specifies that the view for a root designer is defined by some
    private interface contract between the designer and the
    development environment. This implies a tight coupling
    between the development environment and the designer, and should
    be avoided. This does allow older COM2 technologies to
    be shown in development environments that support
    COM2 interface technologies such as doc objects and ActiveX
    controls.
    
    ViewTechnology.Passthrough has been deprecated. Use ViewTechnology.Default instead.
    """

    WindowsForms = 1
    """
    Specifies that the view for a root designer is supplied through
    a Windows Forms control object. The designer host will fill the
    development environment's document window with this control.
    
    ViewTechnology.WindowsForms has been deprecated. Use ViewTechnology.Default instead.
    """

    Default = 2
    """
    Specifies the default view technology support. Here, the root designer may return
    any type of object it wishes, but it must be an object that can be "fitted" with
    an adapter to the technology of the host. Hosting environments such as Visual
    Studio will provide a way to plug in new view technology adapters. The default
    view object for the Windows Forms designer is a Control instance, while the
    default view object for the Avalon designer is an Element instance.
    """


class IRootDesigner(System.ComponentModel.Design.IDesigner, metaclass=abc.ABCMeta):
    """
    Defines the root designer. A root designer is the designer that sits
    at the top, or root, of the object hierarchy. The root designer's job
    is to provide the design-time user interface for the design surface.
    It does this through the View property.
    """

    @property
    @abc.abstractmethod
    def SupportedTechnologies(self) -> typing.List[System.ComponentModel.Design.ViewTechnology]:
        """
        The list of technologies that this designer can support
        for its view. Examples of different technologies are
        Windows Forms and Web Forms. Other object models can be
        supported at design time, but they most be able to
        provide a view in one of the supported technologies.
        """
        ...

    def GetView(self, technology: System.ComponentModel.Design.ViewTechnology) -> System.Object:
        """
        The user interface to present to the user. The returning
        data type is an object because there can be a variety
        of different user interface technologies. Development
        environments typically support more than one technology.
        """
        ...


class CheckoutException(System.Runtime.InteropServices.ExternalException):
    """
    The exception thrown when an attempt is made to edit a file that is checked into
    a source control program.
    """

    Canceled: System.ComponentModel.Design.CheckoutException = ...
    """
    Initializes a System.ComponentModel.Design.CheckoutException that specifies that the checkout
    was canceled. This field is read-only.
    """

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the System.ComponentModel.Design.CheckoutException class with
        no associated message or error code.
        """
        ...

    @overload
    def __init__(self, message: str) -> None:
        """
        Initializes a new instance of the System.ComponentModel.Design.CheckoutException
        class with the specified message.
        """
        ...

    @overload
    def __init__(self, message: str, errorCode: int) -> None:
        """
        Initializes a new instance of the System.ComponentModel.Design.CheckoutException
        class with the specified message and error code.
        """
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        Need this constructor since Exception implements ISerializable. We don't have any fields,
        so just forward this to base.
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None:
        """
        Initializes a new instance of the Exception class with a specified error message and a
        reference to the inner exception that is the cause of this exception.
        FxCop CA1032: Multiple constructors are required to correctly implement a custom exception.
        """
        ...


class StandardCommands(System.Object):
    """
    Specifies identifiers for the standard set of commands that are available to
    most applications.
    """

    AlignBottom: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the AlignBottom command. Read only."""

    AlignHorizontalCenters: System.ComponentModel.Design.CommandID = ...
    """
    Gets the GUID/integer value pair for the AlignHorizontalCenters command. Read
    only.
    """

    AlignLeft: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the AlignLeft command. Read only."""

    AlignRight: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the AlignRight command. Read only."""

    AlignToGrid: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the AlignToGrid command. Read only."""

    AlignTop: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the AlignTop command. Read only."""

    AlignVerticalCenters: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the AlignVerticalCenters command. Read only."""

    ArrangeBottom: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the ArrangeBottom command. Read only."""

    ArrangeRight: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the ArrangeRight command. Read only."""

    BringForward: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the BringForward command. Read only."""

    BringToFront: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the BringToFront command. Read only."""

    CenterHorizontally: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the CenterHorizontally command. Read only."""

    CenterVertically: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the CenterVertically command. Read only."""

    ViewCode: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the Code command. Read only."""

    DocumentOutline: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the DocumentOutline command. Read only."""

    Copy: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the Copy command. Read only."""

    Cut: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the Cut command. Read only."""

    Delete: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the Delete command. Read only."""

    Group: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the Group command. Read only."""

    HorizSpaceConcatenate: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the HorizSpaceConcatenate command. Read only."""

    HorizSpaceDecrease: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the HorizSpaceDecrease command. Read only."""

    HorizSpaceIncrease: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the HorizSpaceIncrease command. Read only."""

    HorizSpaceMakeEqual: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the HorizSpaceMakeEqual command. Read only."""

    Paste: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the Paste command. Read only."""

    Properties: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the Properties command. Read only."""

    Redo: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the Redo command. Read only."""

    MultiLevelRedo: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the MultiLevelRedo command. Read only."""

    SelectAll: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the SelectAll command. Read only."""

    SendBackward: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the SendBackward command. Read only."""

    SendToBack: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the SendToBack command. Read only."""

    SizeToControl: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the SizeToControl command. Read only."""

    SizeToControlHeight: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the SizeToControlHeight command. Read only."""

    SizeToControlWidth: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the SizeToControlWidth command. Read only."""

    SizeToFit: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the SizeToFit command. Read only."""

    SizeToGrid: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the SizeToGrid command. Read only."""

    SnapToGrid: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the SnapToGrid command. Read only."""

    TabOrder: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the TabOrder command. Read only."""

    Undo: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the Undo command. Read only."""

    MultiLevelUndo: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the MultiLevelUndo command. Read only."""

    Ungroup: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the Ungroup command. Read only."""

    VertSpaceConcatenate: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the VertSpaceConcatenate command. Read only."""

    VertSpaceDecrease: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the VertSpaceDecrease command. Read only."""

    VertSpaceIncrease: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the VertSpaceIncrease command. Read only."""

    VertSpaceMakeEqual: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the VertSpaceMakeEqual command. Read only."""

    ShowGrid: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the ShowGrid command. Read only."""

    ViewGrid: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the ViewGrid command. Read only."""

    Replace: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the Replace command. Read only."""

    PropertiesWindow: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the PropertiesWindow command. Read only."""

    LockControls: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the LockControls command. Read only."""

    F1Help: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the F1Help command. Read only."""

    ArrangeIcons: System.ComponentModel.Design.CommandID = ...

    LineupIcons: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the LineupIcons command. Read only."""

    ShowLargeIcons: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the ShowLargeIcons command. Read only."""

    VerbFirst: System.ComponentModel.Design.CommandID = ...
    """Gets the first of a set of verbs. Read only."""

    VerbLast: System.ComponentModel.Design.CommandID = ...
    """Gets the last of a set of verbs.Read only."""


class IDesignerOptionService(metaclass=abc.ABCMeta):
    """Provides access to get and set option values for a designer."""

    def GetOptionValue(self, pageName: str, valueName: str) -> System.Object:
        """Gets the value of an option defined in this package."""
        ...

    def SetOptionValue(self, pageName: str, valueName: str, value: typing.Any) -> None:
        """Sets the value of an option defined in this package."""
        ...


class DesignerOptionService(System.Object, System.ComponentModel.Design.IDesignerOptionService, metaclass=abc.ABCMeta):
    """Provides access to get and set option values for a designer."""

    class DesignerOptionCollection(System.Object, System.Collections.IList):
        """
        The DesignerOptionCollection class is a collection that contains
        other DesignerOptionCollection objects. This forms a tree of options,
        with each branch of the tree having a name and a possible collection of
        properties. Each parent branch of the tree contains a union of the
        properties if all the branch's children.
        """

        @property
        def Count(self) -> int:
            """The count of child options collections this collection contains."""
            ...

        @property
        def Name(self) -> str:
            """
            The name of this collection. Names are programmatic names and are not
            localized. A name search is case insensitive.
            """
            ...

        @property
        def Parent(self) -> System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection:
            """Returns the parent collection object, or null if there is no parent."""
            ...

        @property
        def Properties(self) -> System.ComponentModel.PropertyDescriptorCollection:
            """
            The collection of properties that this OptionCollection, along with all of
            its children, offers. PropertyDescriptors are taken directly from the
            value passed to CreateObjectCollection and wrapped in an additional property
            descriptor that hides the value object from the user. This means that any
            value may be passed into the "component" parameter of the various
            PropertyDescriptor methods. The value is ignored and is replaced with
            the correct value internally.
            """
            ...

        @property
        def IsSynchronized(self) -> bool:
            """Private ICollection implementation."""
            ...

        @property
        def SyncRoot(self) -> System.Object:
            """Private ICollection implementation."""
            ...

        @property
        def IsFixedSize(self) -> bool:
            """Private IList implementation."""
            ...

        @property
        def IsReadOnly(self) -> bool:
            """Private IList implementation."""
            ...

        @overload
        def __getitem__(self, index: int) -> System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection:
            """Retrieves the child collection at the given index."""
            ...

        @overload
        def __getitem__(self, name: str) -> System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection:
            """
            Retrieves the child collection at the given name. The name search is case
            insensitive.
            """
            ...

        @overload
        def __getitem__(self, index: int) -> typing.Any:
            """Private IList implementation."""
            ...

        def __setitem__(self, index: int, value: typing.Any) -> None:
            """Private IList implementation."""
            ...

        def Add(self, value: typing.Any) -> int:
            """Private IList implementation."""
            ...

        def Clear(self) -> None:
            """Private IList implementation."""
            ...

        def Contains(self, value: typing.Any) -> bool:
            """Private IList implementation."""
            ...

        def CopyTo(self, array: System.Array, index: int) -> None:
            """Copies this collection to an array."""
            ...

        def GetEnumerator(self) -> System.Collections.IEnumerator:
            """Returns an enumerator that can be used to iterate this collection."""
            ...

        @overload
        def IndexOf(self, value: System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection) -> int:
            """Returns the numerical index of the given value."""
            ...

        @overload
        def IndexOf(self, value: typing.Any) -> int:
            """Private IList implementation."""
            ...

        def Insert(self, index: int, value: typing.Any) -> None:
            """Private IList implementation."""
            ...

        def Remove(self, value: typing.Any) -> None:
            """Private IList implementation."""
            ...

        def RemoveAt(self, index: int) -> None:
            """Private IList implementation."""
            ...

        def ShowDialog(self) -> bool:
            """
            Displays a dialog-based user interface that allows the user to
            configure the various options.
            """
            ...

    @property
    def Options(self) -> System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection:
        """
        Returns the options collection for this service. There is
        always a global options collection that contains child collections.
        """
        ...

    def CreateOptionCollection(self, parent: System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection, name: str, value: typing.Any) -> System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection:
        """
        Creates a new DesignerOptionCollection with the given name, and adds it to
        the given parent. The "value" parameter specifies an object whose public
        properties will be used in the Properties collection of the option collection.
        The value parameter can be null if this options collection does not offer
        any properties. Properties will be wrapped in such a way that passing
        anything into the component parameter of the property descriptor will be
        ignored and the value object will be substituted.
        
        This method is protected.
        """
        ...

    def GetOptionValue(self, pageName: str, valueName: str) -> System.Object:
        """Gets the value of an option defined in this package."""
        ...

    def PopulateOptionCollection(self, options: System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection) -> None:
        """
        This method is called on demand the first time a user asks for child
        options or properties of an options collection.
        
        This method is protected.
        """
        ...

    def SetOptionValue(self, pageName: str, valueName: str, value: typing.Any) -> None:
        """Sets the value of an option defined in this package."""
        ...

    def ShowDialog(self, options: System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection, optionObject: typing.Any) -> bool:
        """
        This method must be implemented to show the options dialog UI for the given object.
        
        This method is protected.
        """
        ...


class IMenuCommandService(metaclass=abc.ABCMeta):
    """
    Provides an interface for a designer to add menu items to the Visual Studio
    7.0 menu.
    """

    @property
    @abc.abstractmethod
    def Verbs(self) -> System.ComponentModel.Design.DesignerVerbCollection:
        """
        Gets or sets an array of type System.ComponentModel.Design.DesignerVerb
        that indicates the verbs that are currently available.
        """
        ...

    def AddCommand(self, command: System.ComponentModel.Design.MenuCommand) -> None:
        """Adds a menu command to the document."""
        ...

    def AddVerb(self, verb: System.ComponentModel.Design.DesignerVerb) -> None:
        """Adds a verb to the set of global verbs."""
        ...

    def FindCommand(self, commandID: System.ComponentModel.Design.CommandID) -> System.ComponentModel.Design.MenuCommand:
        """
        Searches for the given command ID and returns the System.ComponentModel.Design.MenuCommand
        associated with it.
        """
        ...

    def GlobalInvoke(self, commandID: System.ComponentModel.Design.CommandID) -> bool:
        """Invokes a command on the local form or in the global environment."""
        ...

    def RemoveCommand(self, command: System.ComponentModel.Design.MenuCommand) -> None:
        """Removes the specified System.ComponentModel.Design.MenuCommand from the document."""
        ...

    def RemoveVerb(self, verb: System.ComponentModel.Design.DesignerVerb) -> None:
        """Removes the specified verb from the document."""
        ...

    def ShowContextMenu(self, menuID: System.ComponentModel.Design.CommandID, x: int, y: int) -> None:
        """Shows the context menu with the specified command ID at the specified location."""
        ...


class ServiceContainer(System.Object, System.ComponentModel.Design.IServiceContainer, System.IDisposable):
    """This is a simple implementation of IServiceContainer."""

    @property
    def DefaultServices(self) -> typing.List[typing.Type]:
        """
        This property returns the default services that are implemented directly on this IServiceContainer.
        the default implementation of this property is to return the IServiceContainer and ServiceContainer
        types. You may override this property and return your own types, modifying the default behavior
        of GetService.
        
        This property is protected.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new service object container."""
        ...

    @overload
    def __init__(self, parentProvider: typing.Optional[IServiceProvider]) -> None:
        """Creates a new service object container."""
        ...

    @overload
    def AddService(self, serviceType: typing.Type, serviceInstance: typing.Any) -> None:
        """Adds the given service to the service container."""
        ...

    @overload
    def AddService(self, serviceType: typing.Type, serviceInstance: typing.Any, promote: bool) -> None:
        """Adds the given service to the service container."""
        ...

    @overload
    def AddService(self, serviceType: typing.Type, callback: typing.Callable[[System.ComponentModel.Design.IServiceContainer, typing.Type], System.Object]) -> None:
        """Adds the given service to the service container."""
        ...

    @overload
    def AddService(self, serviceType: typing.Type, callback: typing.Callable[[System.ComponentModel.Design.IServiceContainer, typing.Type], System.Object], promote: bool) -> None:
        """Adds the given service to the service container."""
        ...

    @overload
    def Dispose(self) -> None:
        """
        Disposes this service container. This also walks all instantiated services within the container
        and disposes any that implement IDisposable, and clears the service list.
        """
        ...

    @overload
    def Dispose(self, disposing: bool) -> None:
        """
        Disposes this service container. This also walks all instantiated services within the container
        and disposes any that implement IDisposable, and clears the service list.
        
        This method is protected.
        """
        ...

    def GetService(self, serviceType: typing.Type) -> System.Object:
        """Retrieves the requested service."""
        ...

    @overload
    def RemoveService(self, serviceType: typing.Type) -> None:
        """Removes the given service type from the service container."""
        ...

    @overload
    def RemoveService(self, serviceType: typing.Type, promote: bool) -> None:
        """Removes the given service type from the service container."""
        ...


class IDesignerFilter(metaclass=abc.ABCMeta):
    """
    Provides access to, and an interface for filtering, the dictionaries that store the
    properties, attributes, or events of a component.
    """

    def PostFilterAttributes(self, attributes: System.Collections.IDictionary) -> None:
        """
        Allows a designer to filter the set of attributes the component being designed will expose
        through the System.ComponentModel.TypeDescriptor object.
        """
        ...

    def PostFilterEvents(self, events: System.Collections.IDictionary) -> None:
        """
        Allows a designer to filter the set of events the component being designed will expose
        through the System.ComponentModel.TypeDescriptor object.
        """
        ...

    def PostFilterProperties(self, properties: System.Collections.IDictionary) -> None:
        """
        Allows a designer to filter the set of properties the component being designed will expose
        through the System.ComponentModel.TypeDescriptor object.
        """
        ...

    def PreFilterAttributes(self, attributes: System.Collections.IDictionary) -> None:
        """
        Allows a designer to filter the set of attributes the component being designed will expose
        through the System.ComponentModel.TypeDescriptor object.
        """
        ...

    def PreFilterEvents(self, events: System.Collections.IDictionary) -> None:
        """
        Allows a designer to filter the set of events the component being designed will expose
        through the System.ComponentModel.TypeDescriptor object.
        """
        ...

    def PreFilterProperties(self, properties: System.Collections.IDictionary) -> None:
        """
        Allows a designer to filter the set of properties the component being designed will expose
        through the System.ComponentModel.TypeDescriptor object.
        """
        ...


class IExtenderProviderService(metaclass=abc.ABCMeta):
    """Provides an interface to add and remove extender providers."""

    def AddExtenderProvider(self, provider: System.ComponentModel.IExtenderProvider) -> None:
        """Adds an extender provider."""
        ...

    def RemoveExtenderProvider(self, provider: System.ComponentModel.IExtenderProvider) -> None:
        """Removes an extender provider."""
        ...


class ITypeDiscoveryService(metaclass=abc.ABCMeta):
    """
    The type discovery service is used to discover available types at design time,
    when the consumer doesn't know the names of existing types or referenced assemblies.
    """

    def GetTypes(self, baseType: typing.Type, excludeGlobalTypes: bool) -> System.Collections.ICollection:
        """
        Retrieves the list of available types. If baseType is null, all
        types are returned. Otherwise, only types deriving from the
        specified base type are returned. If bool excludeGlobalTypes is false,
        types from all referenced assemblies are checked. Otherwise,
        only types from non-GAC referenced assemblies are checked.
        """
        ...


class IComponentDiscoveryService(metaclass=abc.ABCMeta):
    """
    This service allows design-time enumeration of components across the toolbox
    and other available types at design-time.
    """

    def GetComponentTypes(self, designerHost: System.ComponentModel.Design.IDesignerHost, baseType: typing.Type) -> System.Collections.ICollection:
        """
        Retrieves the list of available component types, i.e. types implementing
        IComponent. If baseType is null, all components are retrieved; otherwise
        only component types derived from the specified baseType are returned.
        """
        ...


class ITreeDesigner(System.ComponentModel.Design.IDesigner, metaclass=abc.ABCMeta):
    """
    ITreeDesigner is a variation of IDesigner that provides support for
    generically indicating parent / child relationships within a designer.
    """

    @property
    @abc.abstractmethod
    def Children(self) -> System.Collections.ICollection:
        """
        Retrieves the children of this designer. This will return an empty collection
        if this designer has no children.
        """
        ...

    @property
    @abc.abstractmethod
    def Parent(self) -> System.ComponentModel.Design.IDesigner:
        """
        Retrieves the parent designer for this designer. This may return null if
        there is no parent.
        """
        ...


class ITypeDescriptorFilterService(metaclass=abc.ABCMeta):
    """Modifies the set of type descriptors that a component provides."""

    def FilterAttributes(self, component: System.ComponentModel.IComponent, attributes: System.Collections.IDictionary) -> bool:
        """Provides a way to filter the attributes from a component that are displayed to the user."""
        ...

    def FilterEvents(self, component: System.ComponentModel.IComponent, events: System.Collections.IDictionary) -> bool:
        """Provides a way to filter the events from a component that are displayed to the user."""
        ...

    def FilterProperties(self, component: System.ComponentModel.IComponent, properties: System.Collections.IDictionary) -> bool:
        """Provides a way to filter the properties from a component that are displayed to the user."""
        ...


class IResourceService(metaclass=abc.ABCMeta):
    """Provides designers a way to access a resource for the current design-time object."""

    def GetResourceReader(self, info: System.Globalization.CultureInfo) -> System.Resources.IResourceReader:
        """
        Locates the resource reader for the specified culture and
        returns it.
        """
        ...

    def GetResourceWriter(self, info: System.Globalization.CultureInfo) -> typing.Any:
        """
        Locates the resource writer for the specified culture
        and returns it. This will create a new resource for
        the specified culture and destroy any existing resource,
        should it exist.
        """
        ...


class ISelectionService(metaclass=abc.ABCMeta):
    """Provides an interface for a designer to select components."""

    @property
    @abc.abstractmethod
    def PrimarySelection(self) -> System.Object:
        """Gets the object that is currently the primary selection."""
        ...

    @property
    @abc.abstractmethod
    def SelectionCount(self) -> int:
        """Gets the count of selected objects."""
        ...

    @property
    @abc.abstractmethod
    def SelectionChanged(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Adds a System.ComponentModel.Design.ISelectionService.SelectionChanged event handler to the selection service."""
        ...

    @SelectionChanged.setter
    @abc.abstractmethod
    def SelectionChanged(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]):
        """Adds a System.ComponentModel.Design.ISelectionService.SelectionChanged event handler to the selection service."""
        ...

    @property
    @abc.abstractmethod
    def SelectionChanging(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Adds an event handler to the selection service."""
        ...

    @SelectionChanging.setter
    @abc.abstractmethod
    def SelectionChanging(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]):
        """Adds an event handler to the selection service."""
        ...

    def GetComponentSelected(self, component: typing.Any) -> bool:
        """Gets a value indicating whether the component is currently selected."""
        ...

    def GetSelectedComponents(self) -> System.Collections.ICollection:
        """Gets a collection of components that are currently part of the user's selection."""
        ...

    @overload
    def SetSelectedComponents(self, components: System.Collections.ICollection) -> None:
        """Sets the currently selected set of components."""
        ...

    @overload
    def SetSelectedComponents(self, components: System.Collections.ICollection, selectionType: System.ComponentModel.Design.SelectionTypes) -> None:
        """Sets the currently selected set of components to those with the specified selection type within the specified array of components."""
        ...


class HelpKeywordType(System.Enum):
    """Specifies identifiers that can be used to indicate the type of a help keyword."""

    F1Keyword = 0
    """Indicates the keyword is a word F1 was pressed to request help regarding."""

    GeneralKeyword = 1
    """Indicates the keyword is a general keyword."""

    FilterKeyword = 2
    """Indicates the keyword is a filter keyword."""


class HelpContextType(System.Enum):
    """This class has no documentation."""

    Ambient = 0

    Window = 1

    Selection = 2

    ToolWindowSelection = 3


class IHelpService(metaclass=abc.ABCMeta):
    """
    Provides the Integrated Development Environment (IDE) help
    system with contextual information for the current task.
    """

    def AddContextAttribute(self, name: str, value: str, keywordType: System.ComponentModel.Design.HelpKeywordType) -> None:
        """Adds a context attribute to the document."""
        ...

    def ClearContextAttributes(self) -> None:
        """Clears all existing context attributes from the document."""
        ...

    def CreateLocalContext(self, contextType: System.ComponentModel.Design.HelpContextType) -> System.ComponentModel.Design.IHelpService:
        """Creates a Local IHelpService to manage subcontexts."""
        ...

    def RemoveContextAttribute(self, name: str, value: str) -> None:
        """Removes a previously added context attribute."""
        ...

    def RemoveLocalContext(self, localContext: System.ComponentModel.Design.IHelpService) -> None:
        """Removes a context that was created with CreateLocalContext"""
        ...

    def ShowHelpFromKeyword(self, helpKeyword: str) -> None:
        """Shows the help topic that corresponds to the specified keyword."""
        ...

    def ShowHelpFromUrl(self, helpUrl: str) -> None:
        """Shows the help topic that corresponds with the specified Url and topic navigation ID."""
        ...


class ComponentChangedEventArgs(System.EventArgs):
    """Provides data for the System.ComponentModel.Design.IComponentChangeService.ComponentChanged event."""

    @property
    def Component(self) -> System.Object:
        """Gets or sets the component that is the cause of this event."""
        ...

    @property
    def Member(self) -> System.ComponentModel.MemberDescriptor:
        """Gets or sets the member that is about to change."""
        ...

    @property
    def NewValue(self) -> System.Object:
        """Gets or sets the new value of the changed member."""
        ...

    @property
    def OldValue(self) -> System.Object:
        """Gets or sets the old value of the changed member."""
        ...

    def __init__(self, component: typing.Any, member: System.ComponentModel.MemberDescriptor, oldValue: typing.Any, newValue: typing.Any) -> None:
        """Initializes a new instance of the System.ComponentModel.Design.ComponentChangedEventArgs class."""
        ...


class IInheritanceService(metaclass=abc.ABCMeta):
    """Provides a set of utilities for analyzing and identifying inherited components."""

    def AddInheritedComponents(self, component: System.ComponentModel.IComponent, container: System.ComponentModel.IContainer) -> None:
        """Adds inherited components from the specified component to the specified container."""
        ...

    def GetInheritanceAttribute(self, component: System.ComponentModel.IComponent) -> System.ComponentModel.InheritanceAttribute:
        """
        Gets the inheritance attribute of the specified
        component. If the component is not being inherited, this method will return the
        value System.ComponentModel.InheritanceAttribute.NotInherited.
        Otherwise it will return the inheritance attribute for this component.
        """
        ...


class IDesignerEventService(metaclass=abc.ABCMeta):
    """Provides global event notifications and the ability to create designers."""

    @property
    @abc.abstractmethod
    def ActiveDesigner(self) -> System.ComponentModel.Design.IDesignerHost:
        """Gets the currently active designer."""
        ...

    @property
    @abc.abstractmethod
    def Designers(self) -> System.ComponentModel.Design.DesignerCollection:
        """Gets or sets a collection of running design documents in the development environment."""
        ...

    @property
    @abc.abstractmethod
    def ActiveDesignerChanged(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ActiveDesignerEventArgs], None], None]:
        """Adds an event that will be raised when the currently active designer changes."""
        ...

    @ActiveDesignerChanged.setter
    @abc.abstractmethod
    def ActiveDesignerChanged(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ActiveDesignerEventArgs], None], None]):
        """Adds an event that will be raised when the currently active designer changes."""
        ...

    @property
    @abc.abstractmethod
    def DesignerCreated(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerEventArgs], None], None]:
        """Adds an event that will be raised when a designer is created."""
        ...

    @DesignerCreated.setter
    @abc.abstractmethod
    def DesignerCreated(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerEventArgs], None], None]):
        """Adds an event that will be raised when a designer is created."""
        ...

    @property
    @abc.abstractmethod
    def DesignerDisposed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerEventArgs], None], None]:
        """Adds an event that will be raised when a designer is disposed."""
        ...

    @DesignerDisposed.setter
    @abc.abstractmethod
    def DesignerDisposed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerEventArgs], None], None]):
        """Adds an event that will be raised when a designer is disposed."""
        ...

    @property
    @abc.abstractmethod
    def SelectionChanged(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Adds an event that will be raised when the global selection changes."""
        ...

    @SelectionChanged.setter
    @abc.abstractmethod
    def SelectionChanged(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]):
        """Adds an event that will be raised when the global selection changes."""
        ...


class IExtenderListService(metaclass=abc.ABCMeta):
    """Provides an interface to list extender providers."""

    def GetExtenderProviders(self) -> typing.List[System.ComponentModel.IExtenderProvider]:
        """Gets the set of extender providers for the component."""
        ...


class ComponentChangingEventArgs(System.EventArgs):
    """Provides data for the System.ComponentModel.Design.IComponentChangeService.ComponentChanging event."""

    @property
    def Component(self) -> System.Object:
        """Gets or sets the component that is being changed or that is the parent container of the member being changed."""
        ...

    @property
    def Member(self) -> System.ComponentModel.MemberDescriptor:
        """Gets or sets the member of the component that is about to be changed."""
        ...

    def __init__(self, component: typing.Any, member: System.ComponentModel.MemberDescriptor) -> None:
        """Initializes a new instance of the System.ComponentModel.Design.ComponentChangingEventArgs class."""
        ...


class IComponentChangeService(metaclass=abc.ABCMeta):
    """Provides an interface to add and remove the event handlers for System.ComponentModel.Design.IComponentChangeService.ComponentAdded, System.ComponentModel.Design.IComponentChangeService.ComponentAdding, System.ComponentModel.Design.IComponentChangeService.ComponentChanged, System.ComponentModel.Design.IComponentChangeService.ComponentChanging, System.ComponentModel.Design.IComponentChangeService.ComponentRemoved, System.ComponentModel.Design.IComponentChangeService.ComponentRemoving, and System.ComponentModel.Design.IComponentChangeService.ComponentRename events."""

    @property
    @abc.abstractmethod
    def ComponentAdded(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IComponentChangeService.ComponentAdded event."""
        ...

    @ComponentAdded.setter
    @abc.abstractmethod
    def ComponentAdded(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], None], None]):
        """Adds an event handler for the System.ComponentModel.Design.IComponentChangeService.ComponentAdded event."""
        ...

    @property
    @abc.abstractmethod
    def ComponentAdding(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IComponentChangeService.ComponentAdding event."""
        ...

    @ComponentAdding.setter
    @abc.abstractmethod
    def ComponentAdding(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], None], None]):
        """Adds an event handler for the System.ComponentModel.Design.IComponentChangeService.ComponentAdding event."""
        ...

    @property
    @abc.abstractmethod
    def ComponentChanged(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentChangedEventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IComponentChangeService.ComponentChanged event."""
        ...

    @ComponentChanged.setter
    @abc.abstractmethod
    def ComponentChanged(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentChangedEventArgs], None], None]):
        """Adds an event handler for the System.ComponentModel.Design.IComponentChangeService.ComponentChanged event."""
        ...

    @property
    @abc.abstractmethod
    def ComponentChanging(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentChangingEventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IComponentChangeService.ComponentChanging event."""
        ...

    @ComponentChanging.setter
    @abc.abstractmethod
    def ComponentChanging(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentChangingEventArgs], None], None]):
        """Adds an event handler for the System.ComponentModel.Design.IComponentChangeService.ComponentChanging event."""
        ...

    @property
    @abc.abstractmethod
    def ComponentRemoved(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IComponentChangeService.OnComponentRemoved event."""
        ...

    @ComponentRemoved.setter
    @abc.abstractmethod
    def ComponentRemoved(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], None], None]):
        """Adds an event handler for the System.ComponentModel.Design.IComponentChangeService.OnComponentRemoved event."""
        ...

    @property
    @abc.abstractmethod
    def ComponentRemoving(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IComponentChangeService.OnComponentRemoving event."""
        ...

    @ComponentRemoving.setter
    @abc.abstractmethod
    def ComponentRemoving(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], None], None]):
        """Adds an event handler for the System.ComponentModel.Design.IComponentChangeService.OnComponentRemoving event."""
        ...

    @property
    @abc.abstractmethod
    def ComponentRename(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentRenameEventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IComponentChangeService.OnComponentRename event."""
        ...

    @ComponentRename.setter
    @abc.abstractmethod
    def ComponentRename(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentRenameEventArgs], None], None]):
        """Adds an event handler for the System.ComponentModel.Design.IComponentChangeService.OnComponentRename event."""
        ...

    def OnComponentChanged(self, component: typing.Any, member: System.ComponentModel.MemberDescriptor, oldValue: typing.Any, newValue: typing.Any) -> None:
        """Announces to the component change service that a particular component has changed."""
        ...

    def OnComponentChanging(self, component: typing.Any, member: System.ComponentModel.MemberDescriptor) -> None:
        """Announces to the component change service that a particular component is changing."""
        ...


class ITypeResolutionService(metaclass=abc.ABCMeta):
    """The type resolution service is used to load types at design time."""

    @overload
    def GetAssembly(self, name: System.Reflection.AssemblyName) -> System.Reflection.Assembly:
        """Retrieves the requested assembly."""
        ...

    @overload
    def GetAssembly(self, name: System.Reflection.AssemblyName, throwOnError: bool) -> System.Reflection.Assembly:
        """Retrieves the requested assembly."""
        ...

    def GetPathOfAssembly(self, name: System.Reflection.AssemblyName) -> str:
        """Returns the path to the file name from which the assembly was loaded."""
        ...

    @overload
    def GetType(self, name: str) -> typing.Type:
        """Loads a type with the given name."""
        ...

    @overload
    def GetType(self, name: str, throwOnError: bool) -> typing.Type:
        """Loads a type with the given name."""
        ...

    @overload
    def GetType(self, name: str, throwOnError: bool, ignoreCase: bool) -> typing.Type:
        """Loads a type with the given name."""
        ...

    def ReferenceAssembly(self, name: System.Reflection.AssemblyName) -> None:
        """
        References the given assembly name. Once an assembly has
        been referenced types may be loaded from it without
        qualifying them with the assembly.
        """
        ...


class _EventContainer(typing.Generic[System_ComponentModel_Design__EventContainer_Callable, System_ComponentModel_Design__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_ComponentModel_Design__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_ComponentModel_Design__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_ComponentModel_Design__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


