from typing import overload
import typing

import System
import System.Runtime.InteropServices
import System.Runtime.InteropServices.ObjectiveC


class ObjectiveCMarshal(System.Object):
    """API to enable Objective-C marshalling."""

    class MessageSendFunction(System.Enum):
        """Objective-C msgSend function override options."""

        MsgSend = 0
        """Overrides the Objective-C runtime's https://developer.apple.com/documentation/objectivec/1456712-objc_msgsend."""

        MsgSendFpret = 1
        """Overrides the Objective-C runtime's https://developer.apple.com/documentation/objectivec/1456697-objc_msgsend_fpret."""

        MsgSendStret = 2
        """Overrides the Objective-C runtime's https://developer.apple.com/documentation/objectivec/1456730-objc_msgsend_stret."""

        MsgSendSuper = 3
        """Overrides the Objective-C runtime's https://developer.apple.com/documentation/objectivec/1456716-objc_msgsendsuper."""

        MsgSendSuperStret = 4
        """Overrides the Objective-C runtime's https://developer.apple.com/documentation/objectivec/1456722-objc_msgsendsuper_stret."""

        MsgSend = 5
        """Overrides the Objective-C runtime's https://developer.apple.com/documentation/objectivec/1456712-objc_msgsend."""

        MsgSendFpret = 6
        """Overrides the Objective-C runtime's https://developer.apple.com/documentation/objectivec/1456697-objc_msgsend_fpret."""

        MsgSendStret = 7
        """Overrides the Objective-C runtime's https://developer.apple.com/documentation/objectivec/1456730-objc_msgsend_stret."""

        MsgSendSuper = 8
        """Overrides the Objective-C runtime's https://developer.apple.com/documentation/objectivec/1456716-objc_msgsendsuper."""

        MsgSendSuperStret = 9
        """Overrides the Objective-C runtime's https://developer.apple.com/documentation/objectivec/1456722-objc_msgsendsuper_stret."""

    @staticmethod
    @overload
    def CreateReferenceTrackingHandle(obj: typing.Any, taggedMemory: typing.Optional[System.Span[System.IntPtr]]) -> typing.Union[System.Runtime.InteropServices.GCHandle, System.Span[System.IntPtr]]:
        """
        Request native reference tracking for the supplied object.
        
        :param obj: The object to track.
        :param taggedMemory: A pointer to memory tagged to the object.
        :returns: Reference tracking GC handle.
        """
        ...

    @staticmethod
    @overload
    def CreateReferenceTrackingHandle(obj: typing.Any, taggedMemory: typing.Optional[System.Span[System.IntPtr]]) -> typing.Union[System.Runtime.InteropServices.GCHandle, System.Span[System.IntPtr]]:
        """
        Request native reference tracking for the supplied object.
        
        :param obj: The object to track.
        :param taggedMemory: A pointer to memory tagged to the object.
        :returns: Reference tracking GC handle.
        """
        ...

    @staticmethod
    @overload
    def Initialize(beginEndCallback: typing.Any, isReferencedCallback: typing.Any, trackedObjectEnteredFinalization: typing.Any, unhandledExceptionPropagationHandler: typing.Any) -> None:
        """
        Initialize the Objective-C marshalling API.
        
        :param beginEndCallback: Called when tracking begins and ends.
        :param isReferencedCallback: Called to determine if a managed object instance is referenced elsewhere, and must not be collected by the GC.
        :param trackedObjectEnteredFinalization: Called when a tracked object enters the finalization queue.
        :param unhandledExceptionPropagationHandler: Handler for the propagation of unhandled Exceptions across a managed -> native boundary (that is, Reverse P/Invoke).
        """
        ...

    @staticmethod
    @overload
    def Initialize(beginEndCallback: typing.Any, isReferencedCallback: typing.Any, trackedObjectEnteredFinalization: typing.Any, unhandledExceptionPropagationHandler: typing.Any) -> None:
        """
        Initialize the Objective-C marshalling API.
        
        :param beginEndCallback: Called when tracking begins and ends.
        :param isReferencedCallback: Called to determine if a managed object instance is referenced elsewhere, and must not be collected by the GC.
        :param trackedObjectEnteredFinalization: Called when a tracked object enters the finalization queue.
        :param unhandledExceptionPropagationHandler: Handler for the propagation of unhandled Exceptions across a managed -> native boundary (that is, Reverse P/Invoke).
        """
        ...

    @staticmethod
    @overload
    def SetMessageSendCallback(msgSendFunction: typing.Any, func: System.IntPtr) -> None:
        """
        Set a function pointer override for an Objective-C runtime message passing export.
        
        :param msgSendFunction: The export to override.
        :param func: The function override.
        """
        ...

    @staticmethod
    @overload
    def SetMessageSendCallback(msgSendFunction: typing.Any, func: System.IntPtr) -> None:
        """
        Set a function pointer override for an Objective-C runtime message passing export.
        
        :param msgSendFunction: The export to override.
        :param func: The function override.
        """
        ...

    @staticmethod
    @overload
    def SetMessageSendPendingException(exception: System.Exception) -> None:
        """
        Sets a pending exception to be thrown the next time the runtime is entered from an Objective-C msgSend P/Invoke.
        
        :param exception: The exception.
        """
        ...

    @staticmethod
    @overload
    def SetMessageSendPendingException(exception: System.Exception) -> None:
        ...

    @overload
    def UnhandledExceptionPropagationHandler(self, exception: System.Exception, lastMethod: System.RuntimeMethodHandle, context: typing.Optional[System.IntPtr]) -> typing.Union[typing.Any, System.IntPtr]:
        """
        Handler for unhandled Exceptions crossing the managed -> native boundary (that is, Reverse P/Invoke).
        
        :param exception: Unhandled exception.
        :param lastMethod: Last managed method.
        :param context: Context provided to the returned function pointer.
        :returns: Exception propagation callback.
        """
        ...

    @overload
    def UnhandledExceptionPropagationHandler(self, exception: System.Exception, lastMethod: System.RuntimeMethodHandle, context: typing.Optional[System.IntPtr]) -> typing.Union[typing.Any, System.IntPtr]:
        """
        Handler for unhandled Exceptions crossing the managed -> native boundary (that is, Reverse P/Invoke).
        
        :param exception: Unhandled exception.
        :param lastMethod: Last managed method.
        :param context: Context provided to the returned function pointer.
        :returns: Exception propagation callback.
        """
        ...


class ObjectiveCTrackedTypeAttribute(System.Attribute):
    """Attribute used to indicate a class represents a tracked Objective-C type."""

    def __init__(self) -> None:
        """Instantiate a ObjectiveCTrackedTypeAttribute instance."""
        ...


