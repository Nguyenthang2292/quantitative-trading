from typing import overload
import typing

import QuantConnect.Parameters
import System
import System.Collections.Generic
import System.Reflection


class ParameterAttribute(System.Attribute):
    """
    Specifies a field or property is a parameter that can be set
    from an AlgorithmNodePacket.Parameters dictionary
    """

    BindingFlags: System.Reflection.BindingFlags = ...
    """Specifies the binding flags used by this implementation to resolve parameter attributes"""

    @property
    def Name(self) -> str:
        """Gets the name of this parameter"""
        ...

    @Name.setter
    def Name(self, value: str):
        """Gets the name of this parameter"""
        ...

    def __init__(self, name: str = None) -> None:
        """
        Initializes a new instance of the ParameterAttribute class
        
        :param name: The name of the parameter. If null is specified then the field or property name will be used
        """
        ...

    @staticmethod
    def ApplyAttributes(parameters: System.Collections.Generic.Dictionary[str, str], instance: typing.Any) -> None:
        """
        Uses reflections to inspect the instance for any parameter attributes.
        If a value is found in the parameters dictionary, it is set.
        
        :param parameters: The parameters dictionary
        :param instance: The instance to set parameters on
        """
        ...

    @staticmethod
    def GetParametersFromAssembly(assembly: System.Reflection.Assembly) -> System.Collections.Generic.Dictionary[str, str]:
        """
        Resolves all parameter attributes from the specified compiled assembly path
        
        :param assembly: The assembly to inspect
        :returns: Parameters dictionary keyed by parameter name with a value of the member type.
        """
        ...

    @staticmethod
    def GetParametersFromType(type: typing.Type) -> System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[str, str]]:
        """
        Resolves all parameter attributes from the specified type
        
        :param type: The type to inspect
        :returns: Parameters dictionary keyed by parameter name with a value of the member type.
        """
        ...


