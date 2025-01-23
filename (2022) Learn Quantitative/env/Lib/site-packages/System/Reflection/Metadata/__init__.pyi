from typing import overload
import typing

import System
import System.Reflection.Metadata


class MetadataUpdateHandlerAttribute(System.Attribute):
    """Specifies a type that should receive notifications of metadata updates."""

    @property
    def HandlerType(self) -> typing.Type:
        """Gets the type that handles metadata updates and that should be notified when any occur."""
        ...

    def __init__(self, handlerType: typing.Type) -> None:
        """
        Initializes the attribute.
        
        :param handlerType: A type that handles metadata updates and that should be notified when any occur.
        """
        ...


