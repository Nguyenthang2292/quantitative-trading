from typing import overload
import abc
import typing

import QuantConnect
import QuantConnect.Lean.Engine.DataFeeds.WorkScheduling
import System


class WorkScheduler(System.Object, metaclass=abc.ABCMeta):
    """Base work scheduler abstraction"""

    WorkersCount: int = ...
    """The quantity of workers to be used"""

    def QueueWork(self, symbol: typing.Union[QuantConnect.Symbol, str], workFunc: typing.Callable[[int], bool], weightFunc: typing.Callable[[], int]) -> None:
        """
        Add a new work item to the queue
        
        :param symbol: The symbol associated with this work
        :param workFunc: The work function to run
        :param weightFunc: The weight function. Work will be sorted in ascending order based on this weight
        """
        ...


class WeightedWorkScheduler(QuantConnect.Lean.Engine.DataFeeds.WorkScheduling.WorkScheduler):
    """
    This singleton class will create a thread pool to processes work
    that will be prioritized based on it's weight
    """

    WorkBatchSize: int = 50
    """This is the size of each work sprint"""

    MaxWorkWeight: int
    """
    This is the maximum size a work item can weigh,
    if reached, it will be ignored and not executed until its less
    """

    Instance: QuantConnect.Lean.Engine.DataFeeds.WorkScheduling.WeightedWorkScheduler
    """Singleton instance"""

    def AddSingleCallForAll(self, action: typing.Callable[[], None]) -> None:
        """Execute the given action in all workers once"""
        ...

    def QueueWork(self, symbol: typing.Union[QuantConnect.Symbol, str], workFunc: typing.Callable[[int], bool], weightFunc: typing.Callable[[], int]) -> None:
        """
        Add a new work item to the queue
        
        :param symbol: The symbol associated with this work
        :param workFunc: The work function to run
        :param weightFunc: The weight function. Work will be sorted in ascending order based on this weight
        """
        ...


class WorkItem(System.Object):
    """Class to represent a work item"""

    @property
    def Weight(self) -> int:
        """The current weight"""
        ...

    @Weight.setter
    def Weight(self, value: int):
        """The current weight"""
        ...

    @property
    def Work(self) -> typing.Callable[[int], bool]:
        """The work function to execute"""
        ...

    def __init__(self, work: typing.Callable[[int], bool], weightFunc: typing.Callable[[], int]) -> None:
        """
        Creates a new instance
        
        :param work: The work function, takes an int, the amount of work to do and returns a bool, false if this work item is finished
        :param weightFunc: The function used to determine the current weight
        """
        ...

    @staticmethod
    def Compare(obj: QuantConnect.Lean.Engine.DataFeeds.WorkScheduling.WorkItem, other: QuantConnect.Lean.Engine.DataFeeds.WorkScheduling.WorkItem) -> int:
        """Compares two work items based on their weights"""
        ...

    def UpdateWeight(self) -> int:
        """Updates the weight of this work item"""
        ...


