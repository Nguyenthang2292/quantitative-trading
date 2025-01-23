from typing import overload
import typing

import Internal
import System


class Console(System.Object):
    """This class has no documentation."""

    class Error(System.Object):
        """This class has no documentation."""

        @staticmethod
        @overload
        def Write(s: str) -> None:
            ...

        @staticmethod
        @overload
        def Write(s: str) -> None:
            ...

        @staticmethod
        @overload
        def Write(s: str) -> None:
            ...

    @staticmethod
    @overload
    def Write(s: str) -> None:
        ...

    @staticmethod
    @overload
    def Write(s: str) -> None:
        ...

    @staticmethod
    @overload
    def Write(s: str) -> None:
        ...

    @staticmethod
    @overload
    def WriteLine(s: str) -> None:
        ...

    @staticmethod
    @overload
    def WriteLine() -> None:
        ...


