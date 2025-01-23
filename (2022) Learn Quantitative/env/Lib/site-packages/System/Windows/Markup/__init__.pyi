from typing import overload
import typing

import System
import System.Windows.Markup


class ValueSerializerAttribute(System.Attribute):
    """
    Attribute to associate a ValueSerializer class with a value type or to override
    which value serializer to use for a property. A value serializer can be associated
    with an attached property by placing the attribute on the static accessor for the
    attached property.
    """

    @property
    def ValueSerializerType(self) -> typing.Type:
        """The type of the value serializer to create for this type or property."""
        ...

    @property
    def ValueSerializerTypeName(self) -> str:
        """The assembly qualified name of the value serializer type for this type or property."""
        ...

    @overload
    def __init__(self, valueSerializerType: typing.Type) -> None:
        """
        Constructor for the ValueSerializerAttribute
        
        :param valueSerializerType: Type of the value serializer being associated with a type or property
        """
        ...

    @overload
    def __init__(self, valueSerializerTypeName: str) -> None:
        """
        Constructor for the ValueSerializerAttribute
        
        :param valueSerializerTypeName: Fully qualified type name of the value serializer being associated with a type or property
        """
        ...


