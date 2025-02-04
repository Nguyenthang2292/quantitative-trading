from typing import overload
import abc
import typing

import QuantConnect.Optimizer.Parameters
import System
import System.Collections.Generic

JsonConverter = typing.Any

QuantConnect_Optimizer_Parameters_OptimizationParameterEnumerator_T = typing.TypeVar("QuantConnect_Optimizer_Parameters_OptimizationParameterEnumerator_T")


class OptimizationParameterEnumerator(typing.Generic[QuantConnect_Optimizer_Parameters_OptimizationParameterEnumerator_T], System.Object, metaclass=abc.ABCMeta):
    """Enumerates all possible values for specific optimization parameter"""

    @property
    def OptimizationParameter(self) -> QuantConnect_Optimizer_Parameters_OptimizationParameterEnumerator_T:
        """
        The target optimization parameter to enumerate
        
        This field is protected.
        """
        ...

    @property
    def Index(self) -> int:
        """
        The current enumeration state
        
        This field is protected.
        """
        ...

    @Index.setter
    def Index(self, value: int):
        """
        The current enumeration state
        
        This field is protected.
        """
        ...

    @property
    @abc.abstractmethod
    def Current(self) -> str:
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    def __init__(self, optimizationParameter: QuantConnect_Optimizer_Parameters_OptimizationParameterEnumerator_T) -> None:
        """This method is protected."""
        ...

    def Dispose(self) -> None:
        """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
        ...

    def MoveNext(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        ...

    def Reset(self) -> None:
        """Sets the enumerator to its initial position, which is before the first element in the collection."""
        ...


class OptimizationParameter(System.Object, metaclass=abc.ABCMeta):
    """Defines the optimization parameter meta information"""

    @property
    def Name(self) -> str:
        """Name of optimization parameter"""
        ...

    def __init__(self, name: str) -> None:
        """
        Create an instance of OptimizationParameter based on configuration
        
        This method is protected.
        
        :param name: parameter name
        """
        ...

    @overload
    def Equals(self, other: QuantConnect.Optimizer.Parameters.OptimizationParameter) -> bool:
        """
        Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the  parameter; otherwise, false.
        """
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified object is equal to the current object.
        
        :param obj: The object to compare with the current object.
        :returns: true if the specified object  is equal to the current object; otherwise, false.
        """
        ...

    def GetHashCode(self) -> int:
        """
        Serves as the default hash function.
        
        :returns: A hash code for the current object.
        """
        ...


class OptimizationStepParameter(QuantConnect.Optimizer.Parameters.OptimizationParameter):
    """Defines the step based optimization parameter"""

    @property
    def MinValue(self) -> float:
        """Minimum value of optimization parameter, applicable for boundary conditions"""
        ...

    @property
    def MaxValue(self) -> float:
        """Maximum value of optimization parameter, applicable for boundary conditions"""
        ...

    @property
    def Step(self) -> typing.Optional[float]:
        """Movement, should be positive"""
        ...

    @Step.setter
    def Step(self, value: typing.Optional[float]):
        """Movement, should be positive"""
        ...

    @property
    def MinStep(self) -> typing.Optional[float]:
        """Minimal possible movement for current parameter, should be positive"""
        ...

    @MinStep.setter
    def MinStep(self, value: typing.Optional[float]):
        """Minimal possible movement for current parameter, should be positive"""
        ...

    @overload
    def __init__(self, name: str, min: float, max: float) -> None:
        """
        Create an instance of OptimizationParameter based on configuration
        
        :param name: parameter name
        :param min: minimal value
        :param max: maximal value
        """
        ...

    @overload
    def __init__(self, name: str, min: float, max: float, step: float) -> None:
        """
        Create an instance of OptimizationParameter based on configuration
        
        :param name: parameter name
        :param min: minimal value
        :param max: maximal value
        :param step: movement
        """
        ...

    @overload
    def __init__(self, name: str, min: float, max: float, step: float, minStep: float) -> None:
        """
        Create an instance of OptimizationParameter based on configuration
        
        :param name: parameter name
        :param min: minimal value
        :param max: maximal value
        :param step: movement
        :param minStep: minimal possible movement
        """
        ...


class OptimizationStepParameterEnumerator(QuantConnect.Optimizer.Parameters.OptimizationParameterEnumerator[QuantConnect.Optimizer.Parameters.OptimizationStepParameter]):
    """Enumerates all possible values for specific optimization parameter"""

    @property
    def Current(self) -> str:
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    def __init__(self, optimizationParameter: QuantConnect.Optimizer.Parameters.OptimizationStepParameter) -> None:
        """
        Creates an instance of OptimizationStepParameterEnumerator
        
        :param optimizationParameter: Step-based optimization parameter
        """
        ...

    def MoveNext(self) -> bool:
        """
        Advances the enumerator to the next element of the collection.
        
        :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
        """
        ...


class StaticOptimizationParameter(QuantConnect.Optimizer.Parameters.OptimizationParameter):
    """Defines the step based optimization parameter"""

    @property
    def Value(self) -> str:
        """Minimum value of optimization parameter, applicable for boundary conditions"""
        ...

    def __init__(self, name: str, value: str) -> None:
        """
        Creates a new instance
        
        :param name: The name of the parameter
        :param value: The fixed value of this parameter
        """
        ...


class OptimizationParameterJsonConverter(JsonConverter):
    """
    Override OptimizationParameter deserialization method.
    Can handle OptimizationArrayParameter and OptimizationStepParameter instances
    """

    def CanConvert(self, objectType: typing.Type) -> bool:
        ...

    def ReadJson(self, reader: typing.Any, objectType: typing.Type, existingValue: typing.Any, serializer: typing.Any) -> System.Object:
        ...

    def WriteJson(self, writer: typing.Any, value: typing.Any, serializer: typing.Any) -> None:
        ...


class ParameterSet(System.Object):
    """Represents a single combination of optimization parameters"""

    @property
    def Id(self) -> int:
        """The unique identifier within scope (current optimization job)"""
        ...

    @property
    def Value(self) -> System.Collections.Generic.IReadOnlyDictionary[str, str]:
        """Represent a combination as key value of parameters, i.e. order doesn't matter"""
        ...

    def __init__(self, id: int, value: System.Collections.Generic.Dictionary[str, str]) -> None:
        """
        Creates an instance of ParameterSet based on new combination of optimization parameters
        
        :param id: Unique identifier
        :param value: Combination of optimization parameters
        """
        ...

    def ToString(self) -> str:
        """String representation of this parameter set"""
        ...


