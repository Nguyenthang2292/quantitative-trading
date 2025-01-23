from typing import overload
import abc
import typing

import Microsoft.Win32.SafeHandles
import System
import System.ComponentModel
import System.Globalization
import System.Security.Authentication.ExtendedProtection


class ExtendedProtectionPolicyTypeConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def CanConvertTo(self, context: System.ComponentModel.ITypeDescriptorContext, destinationType: typing.Type) -> bool:
        ...

    def ConvertTo(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destinationType: typing.Type) -> System.Object:
        ...


class ChannelBinding(Microsoft.Win32.SafeHandles.SafeHandleZeroOrMinusOneIsInvalid, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def Size(self) -> int:
        ...

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, ownsHandle: bool) -> None:
        """This method is protected."""
        ...


class ChannelBindingKind(System.Enum):
    """This class has no documentation."""

    Unknown = 0

    Unique = ...

    Endpoint = ...


