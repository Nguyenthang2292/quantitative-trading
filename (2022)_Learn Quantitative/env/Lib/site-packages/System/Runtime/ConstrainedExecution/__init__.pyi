from typing import overload
import abc

import System
import System.Runtime.ConstrainedExecution


class Consistency(System.Enum):
    """Obsoletions.ConstrainedExecutionRegionMessage"""

    MayCorruptProcess = 0

    MayCorruptAppDomain = 1

    MayCorruptInstance = 2

    WillNotCorruptState = 3


class Cer(System.Enum):
    """Obsoletions.ConstrainedExecutionRegionMessage"""

    # Cannot convert to Python: None = 0

    MayFail = 1

    Success = 2


class PrePrepareMethodAttribute(System.Attribute):
    """Obsoletions.ConstrainedExecutionRegionMessage"""

    def __init__(self) -> None:
        ...


class ReliabilityContractAttribute(System.Attribute):
    """Obsoletions.ConstrainedExecutionRegionMessage"""

    @property
    def ConsistencyGuarantee(self) -> int:
        """This property contains the int value of a member of the System.Runtime.ConstrainedExecution.Consistency enum."""
        ...

    @property
    def Cer(self) -> int:
        """This property contains the int value of a member of the System.Runtime.ConstrainedExecution.Cer enum."""
        ...

    def __init__(self, consistencyGuarantee: System.Runtime.ConstrainedExecution.Consistency, cer: System.Runtime.ConstrainedExecution.Cer) -> None:
        ...


class CriticalFinalizerObject(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __init__(self) -> None:
        """This method is protected."""
        ...


