from typing import overload
import typing

import System
import System.Net.Cache


class RequestCacheLevel(System.Enum):
    """This class has no documentation."""

    Default = 0

    BypassCache = 1

    CacheOnly = 2

    CacheIfAvailable = 3

    Revalidate = 4

    Reload = 5

    NoCacheNoStore = 6


class RequestCachePolicy(System.Object):
    """This class has no documentation."""

    @property
    def Level(self) -> int:
        """This property contains the int value of a member of the System.Net.Cache.RequestCacheLevel enum."""
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, level: System.Net.Cache.RequestCacheLevel) -> None:
        ...

    def ToString(self) -> str:
        ...


