from typing import overload
import typing

import QuantConnect.Lean.Launcher
import System


class Program(System.Object):
    """This class has no documentation."""

    @staticmethod
    def Exit(exitCode: int) -> None:
        ...

    @staticmethod
    def ExitKeyPress(sender: typing.Any, args: System.ConsoleCancelEventArgs) -> None:
        ...

    @staticmethod
    def Main(args: typing.List[str]) -> None:
        ...


