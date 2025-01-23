from typing import overload
import typing

import System
import System.Collections.Generic
import System.Diagnostics.Contracts
import System.Runtime.Serialization

System_Diagnostics_Contracts_Contract_Result_T = typing.TypeVar("System_Diagnostics_Contracts_Contract_Result_T")
System_Diagnostics_Contracts_Contract_OldValue_T = typing.TypeVar("System_Diagnostics_Contracts_Contract_OldValue_T")
System_Diagnostics_Contracts_Contract_ValueAtReturn_T = typing.TypeVar("System_Diagnostics_Contracts_Contract_ValueAtReturn_T")
System_Diagnostics_Contracts_Contract_ForAll_T = typing.TypeVar("System_Diagnostics_Contracts_Contract_ForAll_T")
System_Diagnostics_Contracts_Contract_Exists_T = typing.TypeVar("System_Diagnostics_Contracts_Contract_Exists_T")
System_Diagnostics_Contracts__EventContainer_Callable = typing.TypeVar("System_Diagnostics_Contracts__EventContainer_Callable")
System_Diagnostics_Contracts__EventContainer_ReturnType = typing.TypeVar("System_Diagnostics_Contracts__EventContainer_ReturnType")


class ContractFailureKind(System.Enum):
    """This class has no documentation."""

    Precondition = 0

    Postcondition = 1

    PostconditionOnException = 2

    Invariant = 3

    Assert = 4

    Assume = 5


class ContractFailedEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def thrownDuringHandler(self) -> System.Exception:
        ...

    @thrownDuringHandler.setter
    def thrownDuringHandler(self, value: System.Exception):
        ...

    @property
    def Message(self) -> str:
        ...

    @property
    def Condition(self) -> str:
        ...

    @property
    def FailureKind(self) -> int:
        """This property contains the int value of a member of the System.Diagnostics.Contracts.ContractFailureKind enum."""
        ...

    @property
    def OriginalException(self) -> System.Exception:
        ...

    @property
    def Handled(self) -> bool:
        ...

    @property
    def Unwind(self) -> bool:
        ...

    def __init__(self, failureKind: System.Diagnostics.Contracts.ContractFailureKind, message: str, condition: str, originalException: System.Exception) -> None:
        ...

    def SetHandled(self) -> None:
        ...

    def SetUnwind(self) -> None:
        ...


class ContractException(System.Exception):
    """This class has no documentation."""

    @property
    def Kind(self) -> int:
        """This property contains the int value of a member of the System.Diagnostics.Contracts.ContractFailureKind enum."""
        ...

    @property
    def Failure(self) -> str:
        ...

    @property
    def UserMessage(self) -> str:
        ...

    @property
    def Condition(self) -> str:
        ...

    def __init__(self, kind: System.Diagnostics.Contracts.ContractFailureKind, failure: str, userMessage: str, condition: str, innerException: System.Exception) -> None:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class PureAttribute(System.Attribute):
    """This class has no documentation."""


class ContractClassAttribute(System.Attribute):
    """Types marked with this attribute specify that a separate type contains the contracts for this type."""

    @property
    def TypeContainingContracts(self) -> typing.Type:
        ...

    def __init__(self, typeContainingContracts: typing.Type) -> None:
        ...


class ContractClassForAttribute(System.Attribute):
    """Types marked with this attribute specify that they are a contract for the type that is the argument of the constructor."""

    @property
    def TypeContractsAreFor(self) -> typing.Type:
        ...

    def __init__(self, typeContractsAreFor: typing.Type) -> None:
        ...


class ContractInvariantMethodAttribute(System.Attribute):
    """
    This attribute is used to mark a method as being the invariant
    method for a class. The method can have any name, but it must
    return "void" and take no parameters. The body of the method
    must consist solely of one or more calls to the method
    Contract.Invariant. A suggested name for the method is
    "ObjectInvariant".
    """


class ContractReferenceAssemblyAttribute(System.Attribute):
    """Attribute that specifies that an assembly is a reference assembly with contracts."""


class ContractRuntimeIgnoredAttribute(System.Attribute):
    """Methods (and properties) marked with this attribute can be used within calls to Contract methods, but have no runtime behavior associated with them."""


class ContractVerificationAttribute(System.Attribute):
    """
    Instructs downstream tools whether to assume the correctness of this assembly, type or member without performing any verification or not.
    Can use [ContractVerification(false)] to explicitly mark assembly, type or member as one to *not* have verification performed on it.
    Most specific element found (member, type, then assembly) takes precedence.
    (That is useful if downstream tools allow a user to decide which polarity is the default, unmarked case.)
    """

    @property
    def Value(self) -> bool:
        ...

    def __init__(self, value: bool) -> None:
        ...


class ContractPublicPropertyNameAttribute(System.Attribute):
    """
    Allows a field f to be used in the method contracts for a method m when f has less visibility than m.
    For instance, if the method is public, but the field is private.
    """

    @property
    def Name(self) -> str:
        ...

    def __init__(self, name: str) -> None:
        ...


class ContractArgumentValidatorAttribute(System.Attribute):
    """
    Enables factoring legacy if-then-throw into separate methods for reuse and full control over
    thrown exception and arguments
    """


class ContractAbbreviatorAttribute(System.Attribute):
    """Enables writing abbreviations for contracts that get copied to other methods"""


class ContractOptionAttribute(System.Attribute):
    """Allows setting contract and tool options at assembly, type, or method granularity."""

    @property
    def Category(self) -> str:
        ...

    @property
    def Setting(self) -> str:
        ...

    @property
    def Enabled(self) -> bool:
        ...

    @property
    def Value(self) -> str:
        ...

    @overload
    def __init__(self, category: str, setting: str, enabled: bool) -> None:
        ...

    @overload
    def __init__(self, category: str, setting: str, value: str) -> None:
        ...


class Contract(System.Object):
    """This class has no documentation."""

    ContractFailed: _EventContainer[typing.Callable[[System.Object, System.Diagnostics.Contracts.ContractFailedEventArgs], None], None]
    """
    Allows a managed application environment such as an interactive interpreter (IronPython)
    to be notified of contract failures and
    potentially "handle" them, either by throwing a particular exception type, etc.  If any of the
    event handlers sets the Cancel flag in the ContractFailedEventArgs, then the Contract class will
    not pop up an assert dialog box or trigger escalation policy.  Hooking this event requires
    full trust, because it will inform you of bugs in the appdomain and because the event handler
    could allow you to continue execution.
    """

    @staticmethod
    @overload
    def Assert(condition: bool) -> None:
        ...

    @staticmethod
    @overload
    def Assert(condition: bool, userMessage: str) -> None:
        """
        In debug builds, perform a runtime check that  is true.
        
        :param condition: Expression to check to always be true.
        :param userMessage: If it is not a constant string literal, then the contract may not be understood by tools.
        """
        ...

    @staticmethod
    @overload
    def Assume(condition: bool) -> None:
        ...

    @staticmethod
    @overload
    def Assume(condition: bool, userMessage: str) -> None:
        """
        Instructs code analysis tools to assume the expression  is true even if it can not be statically proven to always be true.
        
        :param condition: Expression to assume will always be true.
        :param userMessage: If it is not a constant string literal, then the contract may not be understood by tools.
        """
        ...

    @staticmethod
    def EndContractBlock() -> None:
        ...

    @staticmethod
    @overload
    def Ensures(condition: bool) -> None:
        ...

    @staticmethod
    @overload
    def Ensures(condition: bool, userMessage: str) -> None:
        """
        Specifies a public contract such that the expression  will be true when the enclosing method or property returns normally.
        
        :param condition: Boolean expression representing the contract. May include OldValue and Result.
        :param userMessage: If it is not a constant string literal, then the contract may not be understood by tools.
        """
        ...

    @staticmethod
    @overload
    def EnsuresOnThrow(condition: bool) -> None:
        """
        Specifies a contract such that if an exception of type TException is thrown then the expression  will be true when the enclosing method or property terminates abnormally.
        
        :param condition: Boolean expression representing the contract. May include OldValue and Result.
        """
        ...

    @staticmethod
    @overload
    def EnsuresOnThrow(condition: bool, userMessage: str) -> None:
        """
        Specifies a contract such that if an exception of type TException is thrown then the expression  will be true when the enclosing method or property terminates abnormally.
        
        :param condition: Boolean expression representing the contract. May include OldValue and Result.
        :param userMessage: If it is not a constant string literal, then the contract may not be understood by tools.
        """
        ...

    @staticmethod
    @overload
    def Exists(fromInclusive: int, toExclusive: int, predicate: typing.Callable[[int], bool]) -> bool:
        ...

    @staticmethod
    @overload
    def Exists(collection: System.Collections.Generic.IEnumerable[System_Diagnostics_Contracts_Contract_Exists_T], predicate: typing.Callable[[System_Diagnostics_Contracts_Contract_Exists_T], bool]) -> bool:
        """
        Returns whether the  returns true
        for any element in the .
        
        :param collection: The collection from which elements will be drawn from to pass to .
        :param predicate: Function that is evaluated on elements from .
        :returns: true if and only if  returns true for an element in .
        """
        ...

    @staticmethod
    @overload
    def ForAll(fromInclusive: int, toExclusive: int, predicate: typing.Callable[[int], bool]) -> bool:
        ...

    @staticmethod
    @overload
    def ForAll(collection: System.Collections.Generic.IEnumerable[System_Diagnostics_Contracts_Contract_ForAll_T], predicate: typing.Callable[[System_Diagnostics_Contracts_Contract_ForAll_T], bool]) -> bool:
        """
        Returns whether the  returns true
        for all elements in the .
        
        :param collection: The collection from which elements will be drawn from to pass to .
        :param predicate: Function that is evaluated on elements from .
        :returns: true if and only if  returns true for all elements in .
        """
        ...

    @staticmethod
    @overload
    def Invariant(condition: bool) -> None:
        ...

    @staticmethod
    @overload
    def Invariant(condition: bool, userMessage: str) -> None:
        """
        Specifies a contract such that the expression  will be true after every method or property on the enclosing class.
        
        :param condition: Boolean expression representing the contract.
        :param userMessage: If it is not a constant string literal, then the contract may not be understood by tools.
        """
        ...

    @staticmethod
    def OldValue(value: System_Diagnostics_Contracts_Contract_OldValue_T) -> System_Diagnostics_Contracts_Contract_OldValue_T:
        """
        Represents the value of  as it was at the start of the method or property.
        
        :param value: Value to represent.  This must be a field or parameter.
        :returns: Value of  at the start of the method or property.
        """
        ...

    @staticmethod
    @overload
    def Requires(condition: bool) -> None:
        ...

    @staticmethod
    @overload
    def Requires(condition: bool, userMessage: str) -> None:
        """
        Specifies a contract such that the expression  must be true before the enclosing method or property is invoked.
        
        :param condition: Boolean expression representing the contract.
        :param userMessage: If it is not a constant string literal, then the contract may not be understood by tools.
        """
        ...

    @staticmethod
    @overload
    def Requires(condition: bool) -> None:
        """
        Specifies a contract such that the expression  must be true before the enclosing method or property is invoked.
        
        :param condition: Boolean expression representing the contract.
        """
        ...

    @staticmethod
    @overload
    def Requires(condition: bool, userMessage: str) -> None:
        """
        Specifies a contract such that the expression  must be true before the enclosing method or property is invoked.
        
        :param condition: Boolean expression representing the contract.
        :param userMessage: If it is not a constant string literal, then the contract may not be understood by tools.
        """
        ...

    @staticmethod
    def Result() -> System_Diagnostics_Contracts_Contract_Result_T:
        ...

    @staticmethod
    def ValueAtReturn(value: typing.Optional[System_Diagnostics_Contracts_Contract_ValueAtReturn_T]) -> typing.Union[System_Diagnostics_Contracts_Contract_ValueAtReturn_T, System_Diagnostics_Contracts_Contract_ValueAtReturn_T]:
        """
        Represents the final (output) value of an out parameter when returning from a method.
        
        :param value: The out parameter.
        :returns: The output value of the out parameter.
        """
        ...


class _EventContainer(typing.Generic[System_Diagnostics_Contracts__EventContainer_Callable, System_Diagnostics_Contracts__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_Diagnostics_Contracts__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_Diagnostics_Contracts__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_Diagnostics_Contracts__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


