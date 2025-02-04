from typing import overload
import abc
import typing

import System
import System.Windows.Input

System_Windows_Input__EventContainer_Callable = typing.TypeVar("System_Windows_Input__EventContainer_Callable")
System_Windows_Input__EventContainer_ReturnType = typing.TypeVar("System_Windows_Input__EventContainer_ReturnType")


class ICommand(metaclass=abc.ABCMeta):
    """An interface that allows an application author to define a method to be invoked."""

    @property
    @abc.abstractmethod
    def CanExecuteChanged(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Raised when the ability of the command to execute has changed."""
        ...

    @CanExecuteChanged.setter
    @abc.abstractmethod
    def CanExecuteChanged(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]):
        """Raised when the ability of the command to execute has changed."""
        ...

    def CanExecute(self, parameter: typing.Any) -> bool:
        """
        Returns whether the command can be executed.
        
        :param parameter: A parameter that may be used in executing the command. This parameter may be ignored by some implementations.
        :returns: true if the command can be executed with the given parameter and current state. false otherwise.
        """
        ...

    def Execute(self, parameter: typing.Any) -> None:
        """
        Defines the method that should be executed when the command is executed.
        
        :param parameter: A parameter that may be used in executing the command. This parameter may be ignored by some implementations.
        """
        ...


class _EventContainer(typing.Generic[System_Windows_Input__EventContainer_Callable, System_Windows_Input__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_Windows_Input__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_Windows_Input__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_Windows_Input__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


