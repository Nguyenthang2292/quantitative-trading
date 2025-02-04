import typing

import System
import System.Reflection


def getPreload() -> bool:
    ...


def setPreload(preloadFlag: bool) -> None:
    ...


def AddReference(name: str) -> System.Reflection.Assembly:
    ...


def GetClrType(type: typing.Type[typing.Any]) -> System.Type:
    ...


def FindAssembly(name: str) -> str:
    ...


def ListAssemblies(verbose: bool) -> typing.List[System.Reflection.Assembly]:
    ...
