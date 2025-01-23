from typing import overload
import typing

import System
import System.Collections
import System.Collections.Generic
import System.Net
import System.Net.NetworkInformation


class IPAddressCollection(System.Object, System.Collections.Generic.ICollection[System.Net.IPAddress], typing.Iterable[System.Net.IPAddress]):
    """This class has no documentation."""

    @property
    def Count(self) -> int:
        ...

    @property
    def IsReadOnly(self) -> bool:
        ...

    def __getitem__(self, index: int) -> System.Net.IPAddress:
        ...

    def Add(self, address: System.Net.IPAddress) -> None:
        ...

    def Clear(self) -> None:
        ...

    def Contains(self, address: System.Net.IPAddress) -> bool:
        ...

    def CopyTo(self, array: typing.List[System.Net.IPAddress], offset: int) -> None:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System.Net.IPAddress]:
        ...

    def Remove(self, address: System.Net.IPAddress) -> bool:
        ...


