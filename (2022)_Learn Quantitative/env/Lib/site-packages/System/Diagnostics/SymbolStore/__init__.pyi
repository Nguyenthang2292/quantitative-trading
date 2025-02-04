from typing import overload
import abc
import typing

import System
import System.Diagnostics.SymbolStore


class ISymbolDocumentWriter(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def SetCheckSum(self, algorithmId: System.Guid, checkSum: typing.List[int]) -> None:
        ...

    def SetSource(self, source: typing.List[int]) -> None:
        ...


