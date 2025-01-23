from typing import overload
import typing

import System
import System.Runtime.Remoting


class ObjectHandle(System.MarshalByRefObject):
    """This class has no documentation."""

    def __init__(self, o: typing.Any) -> None:
        ...

    def Unwrap(self) -> System.Object:
        ...


