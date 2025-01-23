from typing import overload
import abc

import System
import System.Security
import System.Security.Permissions


class SecurityAction(System.Enum):
    """Obsoletions.CodeAccessSecurityMessage"""

    Assert = 3

    Demand = 2

    Deny = 4

    InheritanceDemand = 7

    LinkDemand = 6

    PermitOnly = 5

    RequestMinimum = 8

    RequestOptional = 9

    RequestRefuse = 10


class SecurityAttribute(System.Attribute, metaclass=abc.ABCMeta):
    """Obsoletions.CodeAccessSecurityMessage"""

    @property
    def Action(self) -> int:
        """This property contains the int value of a member of the System.Security.Permissions.SecurityAction enum."""
        ...

    @Action.setter
    def Action(self, value: int):
        """This property contains the int value of a member of the System.Security.Permissions.SecurityAction enum."""
        ...

    @property
    def Unrestricted(self) -> bool:
        ...

    @Unrestricted.setter
    def Unrestricted(self, value: bool):
        ...

    def __init__(self, action: System.Security.Permissions.SecurityAction) -> None:
        """This method is protected."""
        ...

    def CreatePermission(self) -> System.Security.IPermission:
        ...


class CodeAccessSecurityAttribute(System.Security.Permissions.SecurityAttribute, metaclass=abc.ABCMeta):
    """Obsoletions.CodeAccessSecurityMessage"""

    def __init__(self, action: System.Security.Permissions.SecurityAction) -> None:
        """This method is protected."""
        ...


class SecurityPermissionFlag(System.Enum):
    """Obsoletions.CodeAccessSecurityMessage"""

    AllFlags = 16383

    Assertion = 1

    BindingRedirects = 8192

    ControlAppDomain = 1024

    ControlDomainPolicy = 256

    ControlEvidence = 32

    ControlPolicy = 64

    ControlPrincipal = 512

    ControlThread = 16

    Execution = 8

    Infrastructure = 4096

    NoFlags = 0

    RemotingConfiguration = 2048

    SerializationFormatter = 128

    SkipVerification = 4

    UnmanagedCode = 2


class SecurityPermissionAttribute(System.Security.Permissions.CodeAccessSecurityAttribute):
    """Obsoletions.CodeAccessSecurityMessage"""

    @property
    def Assertion(self) -> bool:
        ...

    @Assertion.setter
    def Assertion(self, value: bool):
        ...

    @property
    def BindingRedirects(self) -> bool:
        ...

    @BindingRedirects.setter
    def BindingRedirects(self, value: bool):
        ...

    @property
    def ControlAppDomain(self) -> bool:
        ...

    @ControlAppDomain.setter
    def ControlAppDomain(self, value: bool):
        ...

    @property
    def ControlDomainPolicy(self) -> bool:
        ...

    @ControlDomainPolicy.setter
    def ControlDomainPolicy(self, value: bool):
        ...

    @property
    def ControlEvidence(self) -> bool:
        ...

    @ControlEvidence.setter
    def ControlEvidence(self, value: bool):
        ...

    @property
    def ControlPolicy(self) -> bool:
        ...

    @ControlPolicy.setter
    def ControlPolicy(self, value: bool):
        ...

    @property
    def ControlPrincipal(self) -> bool:
        ...

    @ControlPrincipal.setter
    def ControlPrincipal(self, value: bool):
        ...

    @property
    def ControlThread(self) -> bool:
        ...

    @ControlThread.setter
    def ControlThread(self, value: bool):
        ...

    @property
    def Execution(self) -> bool:
        ...

    @Execution.setter
    def Execution(self, value: bool):
        ...

    @property
    def Flags(self) -> int:
        """This property contains the int value of a member of the System.Security.Permissions.SecurityPermissionFlag enum."""
        ...

    @Flags.setter
    def Flags(self, value: int):
        """This property contains the int value of a member of the System.Security.Permissions.SecurityPermissionFlag enum."""
        ...

    @property
    def Infrastructure(self) -> bool:
        ...

    @Infrastructure.setter
    def Infrastructure(self, value: bool):
        ...

    @property
    def RemotingConfiguration(self) -> bool:
        ...

    @RemotingConfiguration.setter
    def RemotingConfiguration(self, value: bool):
        ...

    @property
    def SerializationFormatter(self) -> bool:
        ...

    @SerializationFormatter.setter
    def SerializationFormatter(self, value: bool):
        ...

    @property
    def SkipVerification(self) -> bool:
        ...

    @SkipVerification.setter
    def SkipVerification(self, value: bool):
        ...

    @property
    def UnmanagedCode(self) -> bool:
        ...

    @UnmanagedCode.setter
    def UnmanagedCode(self, value: bool):
        ...

    def __init__(self, action: System.Security.Permissions.SecurityAction) -> None:
        ...

    def CreatePermission(self) -> System.Security.IPermission:
        ...


class PermissionState(System.Enum):
    """This class has no documentation."""

    # Cannot convert to Python: None = 0

    Unrestricted = 1


