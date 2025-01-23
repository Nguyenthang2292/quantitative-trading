from typing import overload
import typing

import QuantConnect.Api
import QuantConnect.Api.Serialization
import System

JsonConverter = typing.Any


class ProductJsonConverter(JsonConverter):
    """Provides an implementation of JsonConverter that can deserialize Product"""

    @property
    def CanWrite(self) -> bool:
        """Gets a value indicating whether this JsonConverter can write JSON."""
        ...

    def CanConvert(self, objectType: typing.Type) -> bool:
        """
        Determines whether this instance can convert the specified object type.
        
        :param objectType: Type of the object.
        :returns: true if this instance can convert the specified object type; otherwise, false.
        """
        ...

    def CreateProductFromJObject(self, jObject: typing.Any) -> QuantConnect.Api.Product:
        """
        Create an order from a simple JObject
        
        :returns: Order Object.
        """
        ...

    def ReadJson(self, reader: typing.Any, objectType: typing.Type, existingValue: typing.Any, serializer: typing.Any) -> System.Object:
        """
        Reads the JSON representation of the object.
        
        :param reader: The JsonReader to read from.
        :param objectType: Type of the object.
        :param existingValue: The existing value of object being read.
        :param serializer: The calling serializer.
        :returns: The object value.
        """
        ...

    def WriteJson(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        """
        Writes the JSON representation of the object.
        
        :param writer: The JsonWriter to write to.
        :param value: The value.
        :param serializer: The calling serializer.
        """
        ...


