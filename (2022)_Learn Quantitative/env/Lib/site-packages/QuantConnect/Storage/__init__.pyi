from typing import overload
import typing

import QuantConnect.Interfaces
import QuantConnect.Packets
import QuantConnect.Storage
import System
import System.Collections
import System.Collections.Generic
import System.Text

QuantConnect_Storage_ObjectStore_ReadJson_T = typing.TypeVar("QuantConnect_Storage_ObjectStore_ReadJson_T")
QuantConnect_Storage_ObjectStore_ReadXml_T = typing.TypeVar("QuantConnect_Storage_ObjectStore_ReadXml_T")
QuantConnect_Storage_ObjectStore_SaveJson_T = typing.TypeVar("QuantConnect_Storage_ObjectStore_SaveJson_T")
QuantConnect_Storage_ObjectStore_SaveXml_T = typing.TypeVar("QuantConnect_Storage_ObjectStore_SaveXml_T")
QuantConnect_Storage__EventContainer_Callable = typing.TypeVar("QuantConnect_Storage__EventContainer_Callable")
QuantConnect_Storage__EventContainer_ReturnType = typing.TypeVar("QuantConnect_Storage__EventContainer_ReturnType")


class ObjectStore(System.Object, QuantConnect.Interfaces.IObjectStore, typing.Iterable[System.Collections.Generic.KeyValuePair[str, typing.List[int]]]):
    """Helper class for easier access to IObjectStore methods"""

    @property
    def ErrorRaised(self) -> _EventContainer[typing.Callable[[System.Object, QuantConnect.Interfaces.ObjectStoreErrorRaisedEventArgs], None], None]:
        """Event raised each time there's an error"""
        ...

    @ErrorRaised.setter
    def ErrorRaised(self, value: _EventContainer[typing.Callable[[System.Object, QuantConnect.Interfaces.ObjectStoreErrorRaisedEventArgs], None], None]):
        """Event raised each time there's an error"""
        ...

    @property
    def Keys(self) -> System.Collections.Generic.ICollection[str]:
        """Returns the file paths present in the object store. This is specially useful not to load the object store into memory"""
        ...

    def __init__(self, store: QuantConnect.Interfaces.IObjectStore) -> None:
        """
        Initializes a new instance of the ObjectStore class
        
        :param store: The IObjectStore instance to wrap
        """
        ...

    def Clear(self) -> None:
        """Will clear the object store state cache. This is useful when the object store is used concurrently by nodes which want to share information"""
        ...

    def ContainsKey(self, path: str) -> bool:
        """
        Determines whether the store contains data for the specified path
        
        :param path: The object path
        :returns: True if the key was found.
        """
        ...

    def Delete(self, path: str) -> bool:
        """
        Deletes the object data for the specified path
        
        :param path: The object path
        :returns: True if the delete operation was successful.
        """
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[str, typing.List[int]]]:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: A System.Collections.Generic.IEnumerator`1 that can be used to iterate through the collection.
        """
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        """
        Returns an enumerator that iterates through a collection.
        
        :returns: An System.Collections.IEnumerator object that can be used to iterate through the collection.
        """
        ...

    def GetFilePath(self, path: str) -> str:
        """
        Returns the file path for the specified path
        
        :param path: The object path
        :returns: The path for the file.
        """
        ...

    def Initialize(self, userId: int, projectId: int, userToken: str, controls: QuantConnect.Packets.Controls) -> None:
        """
        Initializes the object store
        
        :param userId: The user id
        :param projectId: The project id
        :param userToken: The user token
        :param controls: The job controls instance
        """
        ...

    def Read(self, path: str, encoding: System.Text.Encoding = None) -> str:
        """
        Returns the string object data for the specified path
        
        :param path: The object path
        :param encoding: The string encoding used
        :returns: A string containing the data.
        """
        ...

    def ReadBytes(self, path: str) -> typing.List[int]:
        """
        Returns the object data for the specified path
        
        :param path: The object path
        :returns: A byte array containing the data.
        """
        ...

    def ReadJson(self, path: str, encoding: System.Text.Encoding = None, settings: typing.Any = None) -> QuantConnect_Storage_ObjectStore_ReadJson_T:
        """
        Returns the JSON deserialized object data for the specified path
        
        :param path: The object path
        :param encoding: The string encoding used
        :param settings: The settings used by the JSON deserializer
        :returns: An object containing the data.
        """
        ...

    def ReadString(self, path: str, encoding: System.Text.Encoding = None) -> str:
        """
        Returns the string object data for the specified path
        
        :param path: The object path
        :param encoding: The string encoding used
        :returns: A string containing the data.
        """
        ...

    def ReadXml(self, path: str, encoding: System.Text.Encoding = None) -> QuantConnect_Storage_ObjectStore_ReadXml_T:
        """
        Returns the XML deserialized object data for the specified path
        
        :param path: The object path
        :param encoding: The string encoding used
        :returns: An object containing the data.
        """
        ...

    @overload
    def Save(self, path: str) -> bool:
        """
        Saves the data from a local file path associated with the specified path
        
        :param path: The object path
        :returns: True if the object was saved successfully.
        """
        ...

    @overload
    def Save(self, path: str, text: str, encoding: System.Text.Encoding = None) -> bool:
        """
        Saves the object data in text format for the specified path
        
        :param path: The object path
        :param text: The string object to be saved
        :param encoding: The string encoding used, Encoding.UTF8 by default
        :returns: True if the object was saved successfully.
        """
        ...

    def SaveBytes(self, path: str, contents: typing.List[int]) -> bool:
        """
        Saves the object data for the specified path
        
        :param path: The object path
        :param contents: The object data
        :returns: True if the save operation was successful.
        """
        ...

    def SaveJson(self, path: str, obj: QuantConnect_Storage_ObjectStore_SaveJson_T, encoding: System.Text.Encoding = None, settings: typing.Any = None) -> bool:
        """
        Saves the object data in JSON format for the specified path
        
        :param path: The object path
        :param obj: The object to be saved
        :param encoding: The string encoding used
        :param settings: The settings used by the JSON serializer
        :returns: True if the object was saved successfully.
        """
        ...

    def SaveString(self, path: str, text: str, encoding: System.Text.Encoding = None) -> bool:
        """
        Saves the object data in text format for the specified path
        
        :param path: The object path
        :param text: The string object to be saved
        :param encoding: The string encoding used
        :returns: True if the object was saved successfully.
        """
        ...

    def SaveXml(self, path: str, obj: QuantConnect_Storage_ObjectStore_SaveXml_T, encoding: System.Text.Encoding = None) -> bool:
        """
        Saves the object data in XML format for the specified path
        
        :param path: The object path
        :param obj: The object to be saved
        :param encoding: The string encoding used
        :returns: True if the object was saved successfully.
        """
        ...


class _EventContainer(typing.Generic[QuantConnect_Storage__EventContainer_Callable, QuantConnect_Storage__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> QuantConnect_Storage__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: QuantConnect_Storage__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: QuantConnect_Storage__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


