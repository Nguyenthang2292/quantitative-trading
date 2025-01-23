from typing import overload
import abc

import System
import System.Security.Principal


class TokenImpersonationLevel(System.Enum):
    """This class has no documentation."""

    # Cannot convert to Python: None = 0

    Anonymous = 1

    Identification = 2

    Impersonation = 3

    Delegation = 4


class IIdentity(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def AuthenticationType(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def IsAuthenticated(self) -> bool:
        ...


class IPrincipal(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def Identity(self) -> System.Security.Principal.IIdentity:
        ...

    def IsInRole(self, role: str) -> bool:
        ...


class PrincipalPolicy(System.Enum):
    """This class has no documentation."""

    UnauthenticatedPrincipal = 0

    NoPrincipal = 1

    WindowsPrincipal = 2


