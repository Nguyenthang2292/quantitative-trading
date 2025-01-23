from typing import overload
import abc

import QuantConnect.Packets
import QuantConnect.Report.ReportElements
import System


class ReportElement(System.Object, QuantConnect.Report.ReportElements.IReportElement, metaclass=abc.ABCMeta):
    """Common interface for template elements of the report"""

    @property
    def Name(self) -> str:
        """Name of this report element"""
        ...

    @Name.setter
    def Name(self, value: str):
        """Name of this report element"""
        ...

    @property
    def Key(self) -> str:
        """Template key code."""
        ...

    @Key.setter
    def Key(self, value: str):
        """Template key code."""
        ...

    @property
    def JsonKey(self) -> str:
        """Normalizes the key into a JSON-friendly key"""
        ...

    @property
    def Result(self) -> System.Object:
        """Result of the render as an object for serialization to JSON"""
        ...

    @Result.setter
    def Result(self, value: System.Object):
        """Result of the render as an object for serialization to JSON"""
        ...

    def Render(self) -> str:
        """The generated output string to be injected"""
        ...


class EstimatedCapacityReportElement(QuantConnect.Report.ReportElements.ReportElement):
    """Capacity Estimation Report Element"""

    def __init__(self, name: str, key: str, backtest: QuantConnect.Packets.BacktestResult, live: QuantConnect.Packets.LiveResult) -> None:
        """
        Create a new capacity estimate
        
        :param name: Name of the widget
        :param key: Location of injection
        :param backtest: Backtest result object
        :param live: Live result object
        """
        ...

    def Render(self) -> str:
        """Render element"""
        ...


