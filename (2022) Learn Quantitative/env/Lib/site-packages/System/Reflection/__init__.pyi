from typing import overload
import abc
import typing
import warnings

import System
import System.Collections.Generic
import System.Globalization
import System.IO
import System.Reflection
import System.Runtime.Serialization

System_Reflection_CustomAttributeTypedArgument = typing.Any
System_Reflection_CustomAttributeNamedArgument = typing.Any

System_Reflection_MethodInfo_CreateDelegate_T = typing.TypeVar("System_Reflection_MethodInfo_CreateDelegate_T")
System_Reflection_CustomAttributeExtensions_GetCustomAttribute_T = typing.TypeVar("System_Reflection_CustomAttributeExtensions_GetCustomAttribute_T")
System_Reflection_CustomAttributeExtensions_GetCustomAttributes_T = typing.TypeVar("System_Reflection_CustomAttributeExtensions_GetCustomAttributes_T")
System_Reflection__EventContainer_Callable = typing.TypeVar("System_Reflection__EventContainer_Callable")
System_Reflection__EventContainer_ReturnType = typing.TypeVar("System_Reflection__EventContainer_ReturnType")


class CustomAttributeTypedArgument(System.IEquatable[System_Reflection_CustomAttributeTypedArgument]):
    """This class has no documentation."""

    @property
    def ArgumentType(self) -> typing.Type:
        ...

    @property
    def Value(self) -> System.Object:
        ...

    @overload
    def __init__(self, argumentType: typing.Type, value: typing.Any) -> None:
        ...

    @overload
    def __init__(self, value: typing.Any) -> None:
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def Equals(self, other: System.Reflection.CustomAttributeTypedArgument) -> bool:
        """
        Indicates whether the current instance is equal to another instance of the same type.
        
        :param other: An instance to compare with this instance.
        :returns: true if the current instance is equal to the other instance; otherwise, false.
        """
        ...

    def GetHashCode(self) -> int:
        ...

    def ToString(self) -> str:
        ...


class IReflectableType(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def GetTypeInfo(self) -> System.Reflection.TypeInfo:
        ...


class ICustomAttributeProvider(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @overload
    def GetCustomAttributes(self, inherit: bool) -> typing.List[System.Object]:
        ...

    @overload
    def GetCustomAttributes(self, attributeType: typing.Type, inherit: bool) -> typing.List[System.Object]:
        ...

    def IsDefined(self, attributeType: typing.Type, inherit: bool) -> bool:
        ...


class MethodInfo(System.Reflection.MethodBase, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def GenericParameterCount(self) -> int:
        ...

    @property
    def MemberType(self) -> int:
        """This property contains the int value of a member of the System.Reflection.MemberTypes enum."""
        ...

    @property
    def ReturnParameter(self) -> System.Reflection.ParameterInfo:
        ...

    @property
    def ReturnType(self) -> typing.Type:
        ...

    @property
    @abc.abstractmethod
    def ReturnTypeCustomAttributes(self) -> System.Reflection.ICustomAttributeProvider:
        ...

    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def CreateDelegate(self, delegateType: typing.Type) -> System.Delegate:
        ...

    @overload
    def CreateDelegate(self, delegateType: typing.Type, target: typing.Any) -> System.Delegate:
        ...

    @overload
    def CreateDelegate(self) -> System_Reflection_MethodInfo_CreateDelegate_T:
        """Creates a delegate of the given type 'T' from this method."""
        ...

    @overload
    def CreateDelegate(self, target: typing.Any) -> System_Reflection_MethodInfo_CreateDelegate_T:
        """Creates a delegate of the given type 'T' with the specified target from this method."""
        ...

    def Equals(self, obj: typing.Any) -> bool:
        ...

    def GetBaseDefinition(self) -> System.Reflection.MethodInfo:
        ...

    def GetGenericArguments(self) -> typing.List[typing.Type]:
        ...

    def GetGenericMethodDefinition(self) -> System.Reflection.MethodInfo:
        ...

    def GetHashCode(self) -> int:
        ...

    def MakeGenericMethod(self, *typeArguments: typing.Type) -> System.Reflection.MethodInfo:
        ...


class BindingFlags(System.Enum):
    """This class has no documentation."""

    Default = ...

    IgnoreCase = ...

    DeclaredOnly = ...

    Instance = ...

    Static = ...

    Public = ...

    NonPublic = ...

    FlattenHierarchy = ...

    InvokeMethod = ...

    CreateInstance = ...

    GetField = ...

    SetField = ...

    GetProperty = ...

    SetProperty = ...

    PutDispProperty = ...

    PutRefDispProperty = ...

    ExactBinding = ...

    SuppressChangeType = ...

    OptionalParamBinding = ...

    IgnoreReturn = ...

    DoNotWrapExceptions = ...


class CallingConventions(System.Enum):
    """This class has no documentation."""

    Standard = ...

    VarArgs = ...

    Any = ...

    HasThis = ...

    ExplicitThis = ...


class FieldInfo(System.Reflection.MemberInfo, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def MemberType(self) -> int:
        """This property contains the int value of a member of the System.Reflection.MemberTypes enum."""
        ...

    @property
    @abc.abstractmethod
    def Attributes(self) -> int:
        """This property contains the int value of a member of the System.Reflection.FieldAttributes enum."""
        ...

    @property
    @abc.abstractmethod
    def FieldType(self) -> typing.Type:
        ...

    @property
    def IsInitOnly(self) -> bool:
        ...

    @property
    def IsLiteral(self) -> bool:
        ...

    @property
    def IsNotSerialized(self) -> bool:
        ...

    @property
    def IsPinvokeImpl(self) -> bool:
        ...

    @property
    def IsSpecialName(self) -> bool:
        ...

    @property
    def IsStatic(self) -> bool:
        ...

    @property
    def IsAssembly(self) -> bool:
        ...

    @property
    def IsFamily(self) -> bool:
        ...

    @property
    def IsFamilyAndAssembly(self) -> bool:
        ...

    @property
    def IsFamilyOrAssembly(self) -> bool:
        ...

    @property
    def IsPrivate(self) -> bool:
        ...

    @property
    def IsPublic(self) -> bool:
        ...

    @property
    def IsSecurityCritical(self) -> bool:
        ...

    @property
    def IsSecuritySafeCritical(self) -> bool:
        ...

    @property
    def IsSecurityTransparent(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def FieldHandle(self) -> System.RuntimeFieldHandle:
        ...

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def Equals(self, obj: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def GetFieldFromHandle(handle: System.RuntimeFieldHandle) -> System.Reflection.FieldInfo:
        ...

    @staticmethod
    @overload
    def GetFieldFromHandle(handle: System.RuntimeFieldHandle, declaringType: System.RuntimeTypeHandle) -> System.Reflection.FieldInfo:
        ...

    def GetHashCode(self) -> int:
        ...

    def GetOptionalCustomModifiers(self) -> typing.List[typing.Type]:
        ...

    def GetRawConstantValue(self) -> System.Object:
        ...

    def GetRequiredCustomModifiers(self) -> typing.List[typing.Type]:
        ...

    def GetValue(self, obj: typing.Any) -> System.Object:
        ...

    def GetValueDirect(self, obj: System.TypedReference) -> System.Object:
        ...

    @overload
    def SetValue(self, obj: typing.Any, value: typing.Any) -> None:
        ...

    @overload
    def SetValue(self, obj: typing.Any, value: typing.Any, invokeAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, culture: System.Globalization.CultureInfo) -> None:
        ...

    def SetValueDirect(self, obj: System.TypedReference, value: typing.Any) -> None:
        ...


class PortableExecutableKinds(System.Enum):
    """This class has no documentation."""

    NotAPortableExecutableImage = ...

    ILOnly = ...

    Required32Bit = ...

    PE32Plus = ...

    Unmanaged32Bit = ...

    Preferred32Bit = ...


class ImageFileMachine(System.Enum):
    """This class has no documentation."""

    I386 = ...

    IA64 = ...

    AMD64 = ...

    ARM = ...


class ParameterModifier:
    """This class has no documentation."""

    def __getitem__(self, index: int) -> bool:
        ...

    def __init__(self, parameterCount: int) -> None:
        ...

    def __setitem__(self, index: int, value: bool) -> None:
        ...


class Module(System.Object, System.Reflection.ICustomAttributeProvider, System.Runtime.Serialization.ISerializable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def Assembly(self) -> System.Reflection.Assembly:
        ...

    UnknownStringMessageInRAF: str = "Returns <Unknown> for modules with no file path"

    @property
    def FullyQualifiedName(self) -> str:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def MDStreamVersion(self) -> int:
        ...

    @property
    def ModuleVersionId(self) -> System.Guid:
        ...

    @property
    def ScopeName(self) -> str:
        ...

    @property
    def ModuleHandle(self) -> System.ModuleHandle:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def MetadataToken(self) -> int:
        ...

    FilterTypeName: typing.Callable[[typing.Type, System.Object], bool] = ...

    FilterTypeNameIgnoreCase: typing.Callable[[typing.Type, System.Object], bool] = ...

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def Equals(self, o: typing.Any) -> bool:
        ...

    def FindTypes(self, filter: typing.Callable[[typing.Type, System.Object], bool], filterCriteria: typing.Any) -> typing.List[typing.Type]:
        ...

    @overload
    def GetCustomAttributes(self, inherit: bool) -> typing.List[System.Object]:
        ...

    @overload
    def GetCustomAttributes(self, attributeType: typing.Type, inherit: bool) -> typing.List[System.Object]:
        ...

    def GetCustomAttributesData(self) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    @overload
    def GetField(self, name: str) -> System.Reflection.FieldInfo:
        ...

    @overload
    def GetField(self, name: str, bindingAttr: System.Reflection.BindingFlags) -> System.Reflection.FieldInfo:
        ...

    @overload
    def GetFields(self) -> typing.List[System.Reflection.FieldInfo]:
        ...

    @overload
    def GetFields(self, bindingFlags: System.Reflection.BindingFlags) -> typing.List[System.Reflection.FieldInfo]:
        ...

    def GetHashCode(self) -> int:
        ...

    @overload
    def GetMethod(self, name: str) -> System.Reflection.MethodInfo:
        ...

    @overload
    def GetMethod(self, name: str, types: typing.List[typing.Type]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def GetMethod(self, name: str, bindingAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, callConvention: System.Reflection.CallingConventions, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        ...

    def GetMethodImpl(self, name: str, bindingAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, callConvention: System.Reflection.CallingConventions, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        """This method is protected."""
        ...

    @overload
    def GetMethods(self) -> typing.List[System.Reflection.MethodInfo]:
        ...

    @overload
    def GetMethods(self, bindingFlags: System.Reflection.BindingFlags) -> typing.List[System.Reflection.MethodInfo]:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def GetPEKind(self, peKind: typing.Optional[System.Reflection.PortableExecutableKinds], machine: typing.Optional[System.Reflection.ImageFileMachine]) -> typing.Union[None, System.Reflection.PortableExecutableKinds, System.Reflection.ImageFileMachine]:
        ...

    @overload
    def GetType(self, className: str) -> typing.Type:
        ...

    @overload
    def GetType(self, className: str, ignoreCase: bool) -> typing.Type:
        ...

    @overload
    def GetType(self, className: str, throwOnError: bool, ignoreCase: bool) -> typing.Type:
        ...

    def GetTypes(self) -> typing.List[typing.Type]:
        ...

    def IsDefined(self, attributeType: typing.Type, inherit: bool) -> bool:
        ...

    def IsResource(self) -> bool:
        ...

    @overload
    def ResolveField(self, metadataToken: int) -> System.Reflection.FieldInfo:
        ...

    @overload
    def ResolveField(self, metadataToken: int, genericTypeArguments: typing.List[typing.Type], genericMethodArguments: typing.List[typing.Type]) -> System.Reflection.FieldInfo:
        ...

    @overload
    def ResolveMember(self, metadataToken: int) -> System.Reflection.MemberInfo:
        ...

    @overload
    def ResolveMember(self, metadataToken: int, genericTypeArguments: typing.List[typing.Type], genericMethodArguments: typing.List[typing.Type]) -> System.Reflection.MemberInfo:
        ...

    @overload
    def ResolveMethod(self, metadataToken: int) -> System.Reflection.MethodBase:
        ...

    @overload
    def ResolveMethod(self, metadataToken: int, genericTypeArguments: typing.List[typing.Type], genericMethodArguments: typing.List[typing.Type]) -> System.Reflection.MethodBase:
        ...

    def ResolveSignature(self, metadataToken: int) -> typing.List[int]:
        ...

    def ResolveString(self, metadataToken: int) -> str:
        ...

    @overload
    def ResolveType(self, metadataToken: int) -> typing.Type:
        ...

    @overload
    def ResolveType(self, metadataToken: int, genericTypeArguments: typing.List[typing.Type], genericMethodArguments: typing.List[typing.Type]) -> typing.Type:
        ...

    def ToString(self) -> str:
        ...


class MemberInfo(System.Object, System.Reflection.ICustomAttributeProvider, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def MemberType(self) -> int:
        """This property contains the int value of a member of the System.Reflection.MemberTypes enum."""
        ...

    @property
    @abc.abstractmethod
    def Name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def DeclaringType(self) -> typing.Type:
        ...

    @property
    @abc.abstractmethod
    def ReflectedType(self) -> typing.Type:
        ...

    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def IsCollectible(self) -> bool:
        ...

    @property
    def MetadataToken(self) -> int:
        ...

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def Equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def GetCustomAttributes(self, inherit: bool) -> typing.List[System.Object]:
        ...

    @overload
    def GetCustomAttributes(self, attributeType: typing.Type, inherit: bool) -> typing.List[System.Object]:
        ...

    def GetCustomAttributesData(self) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    def GetHashCode(self) -> int:
        ...

    def HasSameMetadataDefinitionAs(self, other: System.Reflection.MemberInfo) -> bool:
        ...

    def IsDefined(self, attributeType: typing.Type, inherit: bool) -> bool:
        ...


class EventInfo(System.Reflection.MemberInfo, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def MemberType(self) -> int:
        """This property contains the int value of a member of the System.Reflection.MemberTypes enum."""
        ...

    @property
    @abc.abstractmethod
    def Attributes(self) -> int:
        """This property contains the int value of a member of the System.Reflection.EventAttributes enum."""
        ...

    @property
    def IsSpecialName(self) -> bool:
        ...

    @property
    def AddMethod(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def RemoveMethod(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def RaiseMethod(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def IsMulticast(self) -> bool:
        ...

    @property
    def EventHandlerType(self) -> typing.Type:
        ...

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def AddEventHandler(self, target: typing.Any, handler: System.Delegate) -> None:
        ...

    def Equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def GetAddMethod(self) -> System.Reflection.MethodInfo:
        ...

    @overload
    def GetAddMethod(self, nonPublic: bool) -> System.Reflection.MethodInfo:
        ...

    def GetHashCode(self) -> int:
        ...

    @overload
    def GetOtherMethods(self) -> typing.List[System.Reflection.MethodInfo]:
        ...

    @overload
    def GetOtherMethods(self, nonPublic: bool) -> typing.List[System.Reflection.MethodInfo]:
        ...

    @overload
    def GetRaiseMethod(self) -> System.Reflection.MethodInfo:
        ...

    @overload
    def GetRaiseMethod(self, nonPublic: bool) -> System.Reflection.MethodInfo:
        ...

    @overload
    def GetRemoveMethod(self) -> System.Reflection.MethodInfo:
        ...

    @overload
    def GetRemoveMethod(self, nonPublic: bool) -> System.Reflection.MethodInfo:
        ...

    def RemoveEventHandler(self, target: typing.Any, handler: System.Delegate) -> None:
        ...


class ParameterAttributes(System.Enum):
    """This class has no documentation."""

    # Cannot convert to Python: None = ...

    In = ...

    Out = ...

    Lcid = ...

    Retval = ...

    Optional = ...

    HasDefault = ...

    HasFieldMarshal = ...

    Reserved3 = ...

    Reserved4 = ...

    ReservedMask = ...


class ConstructorInfo(System.Reflection.MethodBase, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def MemberType(self) -> int:
        """This property contains the int value of a member of the System.Reflection.MemberTypes enum."""
        ...

    ConstructorName: str = ".ctor"

    TypeConstructorName: str = ".cctor"

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def Equals(self, obj: typing.Any) -> bool:
        ...

    def GetHashCode(self) -> int:
        ...

    @overload
    def Invoke(self, parameters: typing.List[System.Object]) -> System.Object:
        ...

    @overload
    def Invoke(self, invokeAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, parameters: typing.List[System.Object], culture: System.Globalization.CultureInfo) -> System.Object:
        ...


class ResourceLocation(System.Enum):
    """This class has no documentation."""

    ContainedInAnotherAssembly = 2

    ContainedInManifestFile = 4

    Embedded = 1


class ManifestResourceInfo(System.Object):
    """This class has no documentation."""

    @property
    def ReferencedAssembly(self) -> System.Reflection.Assembly:
        ...

    @property
    def FileName(self) -> str:
        ...

    @property
    def ResourceLocation(self) -> int:
        """This property contains the int value of a member of the System.Reflection.ResourceLocation enum."""
        ...

    def __init__(self, containingAssembly: System.Reflection.Assembly, containingFileName: str, resourceLocation: System.Reflection.ResourceLocation) -> None:
        ...


class StrongNameKeyPair(System.Object, System.Runtime.Serialization.IDeserializationCallback, System.Runtime.Serialization.ISerializable):
    """Obsoletions.StrongNameKeyPairMessage"""

    @property
    def PublicKey(self) -> typing.List[int]:
        ...

    @overload
    def __init__(self, keyPairFile: System.IO.FileStream) -> None:
        ...

    @overload
    def __init__(self, keyPairArray: typing.List[int]) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, keyPairContainer: str) -> None:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def OnDeserialization(self, sender: typing.Any) -> None:
        ...


class AssemblyName(System.Object, System.ICloneable, System.Runtime.Serialization.IDeserializationCallback, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    @property
    def Name(self) -> str:
        ...

    @Name.setter
    def Name(self, value: str):
        ...

    @property
    def Version(self) -> System.Version:
        ...

    @Version.setter
    def Version(self, value: System.Version):
        ...

    @property
    def CultureInfo(self) -> System.Globalization.CultureInfo:
        ...

    @CultureInfo.setter
    def CultureInfo(self, value: System.Globalization.CultureInfo):
        ...

    @property
    def CultureName(self) -> str:
        ...

    @CultureName.setter
    def CultureName(self, value: str):
        ...

    @property
    def CodeBase(self) -> str:
        """Obsoletions.AssemblyNameCodeBaseMessage"""
        warnings.warn("Obsoletions.AssemblyNameCodeBaseMessage", DeprecationWarning)

    @CodeBase.setter
    def CodeBase(self, value: str):
        """Obsoletions.AssemblyNameCodeBaseMessage"""
        warnings.warn("Obsoletions.AssemblyNameCodeBaseMessage", DeprecationWarning)

    @property
    def EscapedCodeBase(self) -> str:
        """Obsoletions.AssemblyNameCodeBaseMessage"""
        warnings.warn("Obsoletions.AssemblyNameCodeBaseMessage", DeprecationWarning)

    @property
    def ProcessorArchitecture(self) -> int:
        """
        This property contains the int value of a member of the System.Reflection.ProcessorArchitecture enum.
        
        Obsoletions.AssemblyNameMembersMessage
        """
        warnings.warn("Obsoletions.AssemblyNameMembersMessage", DeprecationWarning)

    @ProcessorArchitecture.setter
    def ProcessorArchitecture(self, value: int):
        """
        This property contains the int value of a member of the System.Reflection.ProcessorArchitecture enum.
        
        Obsoletions.AssemblyNameMembersMessage
        """
        warnings.warn("Obsoletions.AssemblyNameMembersMessage", DeprecationWarning)

    @property
    def ContentType(self) -> int:
        """This property contains the int value of a member of the System.Reflection.AssemblyContentType enum."""
        ...

    @ContentType.setter
    def ContentType(self, value: int):
        """This property contains the int value of a member of the System.Reflection.AssemblyContentType enum."""
        ...

    @property
    def Flags(self) -> int:
        """This property contains the int value of a member of the System.Reflection.AssemblyNameFlags enum."""
        ...

    @Flags.setter
    def Flags(self, value: int):
        """This property contains the int value of a member of the System.Reflection.AssemblyNameFlags enum."""
        ...

    @property
    def HashAlgorithm(self) -> System.Reflection.AssemblyHashAlgorithm:
        """Obsoletions.AssemblyNameMembersMessage"""
        warnings.warn("Obsoletions.AssemblyNameMembersMessage", DeprecationWarning)

    @HashAlgorithm.setter
    def HashAlgorithm(self, value: System.Reflection.AssemblyHashAlgorithm):
        """Obsoletions.AssemblyNameMembersMessage"""
        warnings.warn("Obsoletions.AssemblyNameMembersMessage", DeprecationWarning)

    @property
    def VersionCompatibility(self) -> int:
        """
        This property contains the int value of a member of the System.Configuration.Assemblies.AssemblyVersionCompatibility enum.
        
        Obsoletions.AssemblyNameMembersMessage
        """
        warnings.warn("Obsoletions.AssemblyNameMembersMessage", DeprecationWarning)

    @VersionCompatibility.setter
    def VersionCompatibility(self, value: int):
        """
        This property contains the int value of a member of the System.Configuration.Assemblies.AssemblyVersionCompatibility enum.
        
        Obsoletions.AssemblyNameMembersMessage
        """
        warnings.warn("Obsoletions.AssemblyNameMembersMessage", DeprecationWarning)

    @property
    def KeyPair(self) -> System.Reflection.StrongNameKeyPair:
        """Obsoletions.StrongNameKeyPairMessage"""
        warnings.warn("Obsoletions.StrongNameKeyPairMessage", DeprecationWarning)

    @KeyPair.setter
    def KeyPair(self, value: System.Reflection.StrongNameKeyPair):
        """Obsoletions.StrongNameKeyPairMessage"""
        warnings.warn("Obsoletions.StrongNameKeyPairMessage", DeprecationWarning)

    @property
    def FullName(self) -> str:
        ...

    c_DummyChar: str = ...

    @overload
    def __init__(self, assemblyName: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    def Clone(self) -> System.Object:
        ...

    @staticmethod
    def GetAssemblyName(assemblyFile: str) -> System.Reflection.AssemblyName:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def GetPublicKey(self) -> typing.List[int]:
        ...

    def GetPublicKeyToken(self) -> typing.List[int]:
        ...

    def OnDeserialization(self, sender: typing.Any) -> None:
        ...

    @staticmethod
    def ReferenceMatchesDefinition(reference: System.Reflection.AssemblyName, definition: System.Reflection.AssemblyName) -> bool:
        """
        Compares the simple names disregarding Version, Culture and PKT. While this clearly does not
        match the intent of this api, this api has been broken this way since its debut and we cannot
        change its behavior now.
        """
        ...

    def SetPublicKey(self, publicKey: typing.List[int]) -> None:
        ...

    def SetPublicKeyToken(self, publicKeyToken: typing.List[int]) -> None:
        ...

    def ToString(self) -> str:
        ...


class Assembly(System.Object, System.Reflection.ICustomAttributeProvider, System.Runtime.Serialization.ISerializable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def DefinedTypes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.TypeInfo]:
        ...

    @property
    def ExportedTypes(self) -> System.Collections.Generic.IEnumerable[typing.Type]:
        ...

    ThrowingMessageInRAF: str = "This member throws an exception for assemblies embedded in a single-file app"

    @property
    def CodeBase(self) -> str:
        """Assembly.CodeBase and Assembly.EscapedCodeBase are only included for .NET Framework compatibility. Use Assembly.Location."""
        warnings.warn("Assembly.CodeBase and Assembly.EscapedCodeBase are only included for .NET Framework compatibility. Use Assembly.Location.", DeprecationWarning)

    @property
    def EntryPoint(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def FullName(self) -> str:
        ...

    @property
    def ImageRuntimeVersion(self) -> str:
        ...

    @property
    def IsDynamic(self) -> bool:
        ...

    @property
    def Location(self) -> str:
        ...

    @property
    def ReflectionOnly(self) -> bool:
        ...

    @property
    def IsCollectible(self) -> bool:
        ...

    @property
    def IsFullyTrusted(self) -> bool:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def EscapedCodeBase(self) -> str:
        """Assembly.CodeBase and Assembly.EscapedCodeBase are only included for .NET Framework compatibility. Use Assembly.Location."""
        warnings.warn("Assembly.CodeBase and Assembly.EscapedCodeBase are only included for .NET Framework compatibility. Use Assembly.Location.", DeprecationWarning)

    @property
    def ModuleResolve(self) -> _EventContainer[typing.Callable[[System.Object, System.ResolveEventArgs], System.Reflection.Module], System.Reflection.Module]:
        ...

    @ModuleResolve.setter
    def ModuleResolve(self, value: _EventContainer[typing.Callable[[System.Object, System.ResolveEventArgs], System.Reflection.Module], System.Reflection.Module]):
        ...

    @property
    def ManifestModule(self) -> System.Reflection.Module:
        ...

    @property
    def Modules(self) -> System.Collections.Generic.IEnumerable[System.Reflection.Module]:
        ...

    @property
    def GlobalAssemblyCache(self) -> bool:
        """Obsoletions.GlobalAssemblyCacheMessage"""
        warnings.warn("Obsoletions.GlobalAssemblyCacheMessage", DeprecationWarning)

    @property
    def HostContext(self) -> int:
        ...

    @property
    def SecurityRuleSet(self) -> int:
        """This property contains the int value of a member of the System.Security.SecurityRuleSet enum."""
        ...

    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def CreateInstance(self, typeName: str) -> System.Object:
        ...

    @overload
    def CreateInstance(self, typeName: str, ignoreCase: bool) -> System.Object:
        ...

    @overload
    def CreateInstance(self, typeName: str, ignoreCase: bool, bindingAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, args: typing.List[System.Object], culture: System.Globalization.CultureInfo, activationAttributes: typing.List[System.Object]) -> System.Object:
        ...

    @staticmethod
    def CreateQualifiedName(assemblyName: str, typeName: str) -> str:
        ...

    def Equals(self, o: typing.Any) -> bool:
        ...

    @staticmethod
    def GetAssembly(type: typing.Type) -> System.Reflection.Assembly:
        ...

    @staticmethod
    def GetCallingAssembly() -> System.Reflection.Assembly:
        ...

    @overload
    def GetCustomAttributes(self, inherit: bool) -> typing.List[System.Object]:
        ...

    @overload
    def GetCustomAttributes(self, attributeType: typing.Type, inherit: bool) -> typing.List[System.Object]:
        ...

    def GetCustomAttributesData(self) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    @staticmethod
    def GetEntryAssembly() -> System.Reflection.Assembly:
        ...

    @staticmethod
    def GetExecutingAssembly() -> System.Reflection.Assembly:
        ...

    def GetExportedTypes(self) -> typing.List[typing.Type]:
        ...

    def GetFile(self, name: str) -> System.IO.FileStream:
        ...

    @overload
    def GetFiles(self) -> typing.List[System.IO.FileStream]:
        ...

    @overload
    def GetFiles(self, getResourceModules: bool) -> typing.List[System.IO.FileStream]:
        ...

    def GetForwardedTypes(self) -> typing.List[typing.Type]:
        ...

    def GetHashCode(self) -> int:
        ...

    @overload
    def GetLoadedModules(self) -> typing.List[System.Reflection.Module]:
        ...

    @overload
    def GetLoadedModules(self, getResourceModules: bool) -> typing.List[System.Reflection.Module]:
        ...

    def GetManifestResourceInfo(self, resourceName: str) -> System.Reflection.ManifestResourceInfo:
        ...

    def GetManifestResourceNames(self) -> typing.List[str]:
        ...

    @overload
    def GetManifestResourceStream(self, name: str) -> System.IO.Stream:
        ...

    @overload
    def GetManifestResourceStream(self, type: typing.Type, name: str) -> System.IO.Stream:
        ...

    def GetModule(self, name: str) -> System.Reflection.Module:
        ...

    @overload
    def GetModules(self) -> typing.List[System.Reflection.Module]:
        ...

    @overload
    def GetModules(self, getResourceModules: bool) -> typing.List[System.Reflection.Module]:
        ...

    @overload
    def GetName(self) -> System.Reflection.AssemblyName:
        ...

    @overload
    def GetName(self, copiedName: bool) -> System.Reflection.AssemblyName:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def GetReferencedAssemblies(self) -> typing.List[System.Reflection.AssemblyName]:
        ...

    @overload
    def GetSatelliteAssembly(self, culture: System.Globalization.CultureInfo) -> System.Reflection.Assembly:
        ...

    @overload
    def GetSatelliteAssembly(self, culture: System.Globalization.CultureInfo, version: System.Version) -> System.Reflection.Assembly:
        ...

    @overload
    def GetType(self, name: str) -> typing.Type:
        ...

    @overload
    def GetType(self, name: str, throwOnError: bool) -> typing.Type:
        ...

    @overload
    def GetType(self, name: str, throwOnError: bool, ignoreCase: bool) -> typing.Type:
        ...

    def GetTypes(self) -> typing.List[typing.Type]:
        ...

    def IsDefined(self, attributeType: typing.Type, inherit: bool) -> bool:
        ...

    @staticmethod
    @overload
    def Load(rawAssembly: typing.List[int]) -> System.Reflection.Assembly:
        ...

    @staticmethod
    @overload
    def Load(rawAssembly: typing.List[int], rawSymbolStore: typing.List[int]) -> System.Reflection.Assembly:
        ...

    @staticmethod
    @overload
    def Load(assemblyString: str) -> System.Reflection.Assembly:
        ...

    @staticmethod
    @overload
    def Load(assemblyRef: System.Reflection.AssemblyName) -> System.Reflection.Assembly:
        ...

    @staticmethod
    def LoadFile(path: str) -> System.Reflection.Assembly:
        ...

    @staticmethod
    @overload
    def LoadFrom(assemblyFile: str) -> System.Reflection.Assembly:
        ...

    @staticmethod
    @overload
    def LoadFrom(assemblyFile: str, hashValue: typing.List[int], hashAlgorithm: System.Reflection.AssemblyHashAlgorithm) -> System.Reflection.Assembly:
        ...

    @overload
    def LoadModule(self, moduleName: str, rawModule: typing.List[int]) -> System.Reflection.Module:
        ...

    @overload
    def LoadModule(self, moduleName: str, rawModule: typing.List[int], rawSymbolStore: typing.List[int]) -> System.Reflection.Module:
        ...

    @staticmethod
    def LoadWithPartialName(partialName: str) -> System.Reflection.Assembly:
        """Assembly.LoadWithPartialName has been deprecated. Use Assembly.Load() instead."""
        warnings.warn("Assembly.LoadWithPartialName has been deprecated. Use Assembly.Load() instead.", DeprecationWarning)

    @staticmethod
    @overload
    def ReflectionOnlyLoad(rawAssembly: typing.List[int]) -> System.Reflection.Assembly:
        """Obsoletions.ReflectionOnlyLoadingMessage"""
        ...

    @staticmethod
    @overload
    def ReflectionOnlyLoad(assemblyString: str) -> System.Reflection.Assembly:
        """Obsoletions.ReflectionOnlyLoadingMessage"""
        ...

    @staticmethod
    def ReflectionOnlyLoadFrom(assemblyFile: str) -> System.Reflection.Assembly:
        """Obsoletions.ReflectionOnlyLoadingMessage"""
        warnings.warn("Obsoletions.ReflectionOnlyLoadingMessage", DeprecationWarning)

    def ToString(self) -> str:
        ...

    @staticmethod
    def UnsafeLoadFrom(assemblyFile: str) -> System.Reflection.Assembly:
        ...


class CustomAttributeNamedArgument(System.IEquatable[System_Reflection_CustomAttributeNamedArgument]):
    """This class has no documentation."""

    @property
    def ArgumentType(self) -> typing.Type:
        ...

    @property
    def MemberInfo(self) -> System.Reflection.MemberInfo:
        ...

    @property
    def TypedValue(self) -> System.Reflection.CustomAttributeTypedArgument:
        ...

    @property
    def MemberName(self) -> str:
        ...

    @property
    def IsField(self) -> bool:
        ...

    @overload
    def __init__(self, memberInfo: System.Reflection.MemberInfo, value: typing.Any) -> None:
        ...

    @overload
    def __init__(self, memberInfo: System.Reflection.MemberInfo, typedArgument: System.Reflection.CustomAttributeTypedArgument) -> None:
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def Equals(self, other: System.Reflection.CustomAttributeNamedArgument) -> bool:
        """
        Indicates whether the current instance is equal to another instance of the same type.
        
        :param other: An instance to compare with this instance.
        :returns: true if the current instance is equal to the other instance; otherwise, false.
        """
        ...

    def GetHashCode(self) -> int:
        ...

    def ToString(self) -> str:
        ...


class CustomAttributeData(System.Object):
    """This class has no documentation."""

    @property
    def AttributeType(self) -> typing.Type:
        ...

    @property
    def Constructor(self) -> System.Reflection.ConstructorInfo:
        ...

    @property
    def ConstructorArguments(self) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeTypedArgument]:
        ...

    @property
    def NamedArguments(self) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeNamedArgument]:
        ...

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def Equals(self, obj: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def GetCustomAttributes(target: System.Reflection.MemberInfo) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    @staticmethod
    @overload
    def GetCustomAttributes(target: System.Reflection.Module) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    @staticmethod
    @overload
    def GetCustomAttributes(target: System.Reflection.Assembly) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    @staticmethod
    @overload
    def GetCustomAttributes(target: System.Reflection.ParameterInfo) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    def GetHashCode(self) -> int:
        ...

    def ToString(self) -> str:
        ...


class ParameterInfo(System.Object, System.Reflection.ICustomAttributeProvider, System.Runtime.Serialization.IObjectReference):
    """This class has no documentation."""

    @property
    def Attributes(self) -> int:
        """This property contains the int value of a member of the System.Reflection.ParameterAttributes enum."""
        ...

    @property
    def Member(self) -> System.Reflection.MemberInfo:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def ParameterType(self) -> typing.Type:
        ...

    @property
    def Position(self) -> int:
        ...

    @property
    def IsIn(self) -> bool:
        ...

    @property
    def IsLcid(self) -> bool:
        ...

    @property
    def IsOptional(self) -> bool:
        ...

    @property
    def IsOut(self) -> bool:
        ...

    @property
    def IsRetval(self) -> bool:
        ...

    @property
    def DefaultValue(self) -> System.Object:
        ...

    @property
    def RawDefaultValue(self) -> System.Object:
        ...

    @property
    def HasDefaultValue(self) -> bool:
        ...

    @property
    def CustomAttributes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.CustomAttributeData]:
        ...

    @property
    def MetadataToken(self) -> int:
        ...

    @property
    def AttrsImpl(self) -> System.Reflection.ParameterAttributes:
        """This field is protected."""
        ...

    @AttrsImpl.setter
    def AttrsImpl(self, value: System.Reflection.ParameterAttributes):
        """This field is protected."""
        ...

    @property
    def ClassImpl(self) -> typing.Type:
        """This field is protected."""
        ...

    @ClassImpl.setter
    def ClassImpl(self, value: typing.Type):
        """This field is protected."""
        ...

    @property
    def DefaultValueImpl(self) -> System.Object:
        """This field is protected."""
        ...

    @DefaultValueImpl.setter
    def DefaultValueImpl(self, value: System.Object):
        """This field is protected."""
        ...

    @property
    def MemberImpl(self) -> System.Reflection.MemberInfo:
        """This field is protected."""
        ...

    @MemberImpl.setter
    def MemberImpl(self, value: System.Reflection.MemberInfo):
        """This field is protected."""
        ...

    @property
    def NameImpl(self) -> str:
        """This field is protected."""
        ...

    @NameImpl.setter
    def NameImpl(self, value: str):
        """This field is protected."""
        ...

    @property
    def PositionImpl(self) -> int:
        """This field is protected."""
        ...

    @PositionImpl.setter
    def PositionImpl(self, value: int):
        """This field is protected."""
        ...

    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def GetCustomAttributes(self, inherit: bool) -> typing.List[System.Object]:
        ...

    @overload
    def GetCustomAttributes(self, attributeType: typing.Type, inherit: bool) -> typing.List[System.Object]:
        ...

    def GetCustomAttributesData(self) -> System.Collections.Generic.IList[System.Reflection.CustomAttributeData]:
        ...

    def GetOptionalCustomModifiers(self) -> typing.List[typing.Type]:
        ...

    def GetRealObject(self, context: System.Runtime.Serialization.StreamingContext) -> System.Object:
        ...

    def GetRequiredCustomModifiers(self) -> typing.List[typing.Type]:
        ...

    def IsDefined(self, attributeType: typing.Type, inherit: bool) -> bool:
        ...

    def ToString(self) -> str:
        ...


class PropertyInfo(System.Reflection.MemberInfo, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def MemberType(self) -> int:
        """This property contains the int value of a member of the System.Reflection.MemberTypes enum."""
        ...

    @property
    @abc.abstractmethod
    def PropertyType(self) -> typing.Type:
        ...

    @property
    @abc.abstractmethod
    def Attributes(self) -> int:
        """This property contains the int value of a member of the System.Reflection.PropertyAttributes enum."""
        ...

    @property
    def IsSpecialName(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def CanRead(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def CanWrite(self) -> bool:
        ...

    @property
    def GetMethod(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def SetMethod(self) -> System.Reflection.MethodInfo:
        ...

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def Equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def GetAccessors(self) -> typing.List[System.Reflection.MethodInfo]:
        ...

    @overload
    def GetAccessors(self, nonPublic: bool) -> typing.List[System.Reflection.MethodInfo]:
        ...

    def GetConstantValue(self) -> System.Object:
        ...

    @overload
    def GetGetMethod(self) -> System.Reflection.MethodInfo:
        ...

    @overload
    def GetGetMethod(self, nonPublic: bool) -> System.Reflection.MethodInfo:
        ...

    def GetHashCode(self) -> int:
        ...

    def GetIndexParameters(self) -> typing.List[System.Reflection.ParameterInfo]:
        ...

    def GetOptionalCustomModifiers(self) -> typing.List[typing.Type]:
        ...

    def GetRawConstantValue(self) -> System.Object:
        ...

    def GetRequiredCustomModifiers(self) -> typing.List[typing.Type]:
        ...

    @overload
    def GetSetMethod(self) -> System.Reflection.MethodInfo:
        ...

    @overload
    def GetSetMethod(self, nonPublic: bool) -> System.Reflection.MethodInfo:
        ...

    @overload
    def GetValue(self, obj: typing.Any) -> System.Object:
        ...

    @overload
    def GetValue(self, obj: typing.Any, index: typing.List[System.Object]) -> System.Object:
        ...

    @overload
    def GetValue(self, obj: typing.Any, invokeAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, index: typing.List[System.Object], culture: System.Globalization.CultureInfo) -> System.Object:
        ...

    @overload
    def SetValue(self, obj: typing.Any, value: typing.Any) -> None:
        ...

    @overload
    def SetValue(self, obj: typing.Any, value: typing.Any, index: typing.List[System.Object]) -> None:
        ...

    @overload
    def SetValue(self, obj: typing.Any, value: typing.Any, invokeAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, index: typing.List[System.Object], culture: System.Globalization.CultureInfo) -> None:
        ...


class TypeInfo(typing.Type, System.Reflection.IReflectableType, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def GenericTypeParameters(self) -> typing.List[typing.Type]:
        ...

    @property
    def DeclaredConstructors(self) -> System.Collections.Generic.IEnumerable[System.Reflection.ConstructorInfo]:
        ...

    @property
    def DeclaredEvents(self) -> System.Collections.Generic.IEnumerable[System.Reflection.EventInfo]:
        ...

    @property
    def DeclaredFields(self) -> System.Collections.Generic.IEnumerable[System.Reflection.FieldInfo]:
        ...

    @property
    def DeclaredMembers(self) -> System.Collections.Generic.IEnumerable[System.Reflection.MemberInfo]:
        ...

    @property
    def DeclaredMethods(self) -> System.Collections.Generic.IEnumerable[System.Reflection.MethodInfo]:
        ...

    @property
    def DeclaredNestedTypes(self) -> System.Collections.Generic.IEnumerable[System.Reflection.TypeInfo]:
        ...

    @property
    def DeclaredProperties(self) -> System.Collections.Generic.IEnumerable[System.Reflection.PropertyInfo]:
        ...

    @property
    def ImplementedInterfaces(self) -> System.Collections.Generic.IEnumerable[typing.Type]:
        ...

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def AsType(self) -> typing.Type:
        ...

    def GetDeclaredEvent(self, name: str) -> System.Reflection.EventInfo:
        ...

    def GetDeclaredField(self, name: str) -> System.Reflection.FieldInfo:
        ...

    def GetDeclaredMethod(self, name: str) -> System.Reflection.MethodInfo:
        ...

    def GetDeclaredMethods(self, name: str) -> System.Collections.Generic.IEnumerable[System.Reflection.MethodInfo]:
        ...

    def GetDeclaredNestedType(self, name: str) -> System.Reflection.TypeInfo:
        ...

    def GetDeclaredProperty(self, name: str) -> System.Reflection.PropertyInfo:
        ...

    def GetTypeInfo(self) -> System.Reflection.TypeInfo:
        ...

    def IsAssignableFrom(self, typeInfo: System.Reflection.TypeInfo) -> bool:
        ...


class Binder(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def BindToField(self, bindingAttr: System.Reflection.BindingFlags, match: typing.List[System.Reflection.FieldInfo], value: typing.Any, culture: System.Globalization.CultureInfo) -> System.Reflection.FieldInfo:
        ...

    def BindToMethod(self, bindingAttr: System.Reflection.BindingFlags, match: typing.List[System.Reflection.MethodBase], args: typing.List[System.Object], modifiers: typing.List[System.Reflection.ParameterModifier], culture: System.Globalization.CultureInfo, names: typing.List[str], state: typing.Optional[typing.Any]) -> typing.Union[System.Reflection.MethodBase, typing.Any]:
        ...

    def ChangeType(self, value: typing.Any, type: typing.Type, culture: System.Globalization.CultureInfo) -> System.Object:
        ...

    def ReorderArgumentArray(self, args: typing.List[System.Object], state: typing.Any) -> None:
        ...

    def SelectMethod(self, bindingAttr: System.Reflection.BindingFlags, match: typing.List[System.Reflection.MethodBase], types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodBase:
        ...

    def SelectProperty(self, bindingAttr: System.Reflection.BindingFlags, match: typing.List[System.Reflection.PropertyInfo], returnType: typing.Type, indexes: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.PropertyInfo:
        ...


class MemberTypes(System.Enum):
    """This class has no documentation."""

    Constructor = ...

    Event = ...

    Field = ...

    Method = ...

    Property = ...

    TypeInfo = ...

    Custom = ...

    NestedType = ...

    All = ...


class InterfaceMapping:
    """This class has no documentation."""

    @property
    def TargetType(self) -> typing.Type:
        ...

    @TargetType.setter
    def TargetType(self, value: typing.Type):
        ...

    @property
    def InterfaceType(self) -> typing.Type:
        ...

    @InterfaceType.setter
    def InterfaceType(self, value: typing.Type):
        ...

    @property
    def TargetMethods(self) -> typing.List[System.Reflection.MethodInfo]:
        ...

    @TargetMethods.setter
    def TargetMethods(self, value: typing.List[System.Reflection.MethodInfo]):
        ...

    @property
    def InterfaceMethods(self) -> typing.List[System.Reflection.MethodInfo]:
        ...

    @InterfaceMethods.setter
    def InterfaceMethods(self, value: typing.List[System.Reflection.MethodInfo]):
        ...


class TypeDelegator(System.Reflection.TypeInfo):
    """This class has no documentation."""

    @property
    def typeImpl(self) -> typing.Type:
        """This field is protected."""
        ...

    @typeImpl.setter
    def typeImpl(self, value: typing.Type):
        """This field is protected."""
        ...

    @property
    def GUID(self) -> System.Guid:
        ...

    @property
    def MetadataToken(self) -> int:
        ...

    @property
    def Module(self) -> System.Reflection.Module:
        ...

    @property
    def Assembly(self) -> System.Reflection.Assembly:
        ...

    @property
    def TypeHandle(self) -> System.RuntimeTypeHandle:
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def FullName(self) -> str:
        ...

    @property
    def Namespace(self) -> str:
        ...

    @property
    def AssemblyQualifiedName(self) -> str:
        ...

    @property
    def BaseType(self) -> typing.Type:
        ...

    @property
    def IsTypeDefinition(self) -> bool:
        ...

    @property
    def IsSZArray(self) -> bool:
        ...

    @property
    def IsVariableBoundArray(self) -> bool:
        ...

    @property
    def IsGenericTypeParameter(self) -> bool:
        ...

    @property
    def IsGenericMethodParameter(self) -> bool:
        ...

    @property
    def IsByRefLike(self) -> bool:
        ...

    @property
    def IsConstructedGenericType(self) -> bool:
        ...

    @property
    def IsCollectible(self) -> bool:
        ...

    @property
    def UnderlyingSystemType(self) -> typing.Type:
        ...

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, delegatingType: typing.Type) -> None:
        ...

    def GetAttributeFlagsImpl(self) -> int:
        """
        This method is protected.
        
        :returns: This method returns the int value of a member of the System.Reflection.TypeAttributes enum.
        """
        ...

    def GetConstructorImpl(self, bindingAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, callConvention: System.Reflection.CallingConventions, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.ConstructorInfo:
        """This method is protected."""
        ...

    def GetConstructors(self, bindingAttr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.ConstructorInfo]:
        ...

    @overload
    def GetCustomAttributes(self, inherit: bool) -> typing.List[System.Object]:
        ...

    @overload
    def GetCustomAttributes(self, attributeType: typing.Type, inherit: bool) -> typing.List[System.Object]:
        ...

    def GetElementType(self) -> typing.Type:
        ...

    def GetEvent(self, name: str, bindingAttr: System.Reflection.BindingFlags) -> System.Reflection.EventInfo:
        ...

    @overload
    def GetEvents(self) -> typing.List[System.Reflection.EventInfo]:
        ...

    @overload
    def GetEvents(self, bindingAttr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.EventInfo]:
        ...

    def GetField(self, name: str, bindingAttr: System.Reflection.BindingFlags) -> System.Reflection.FieldInfo:
        ...

    def GetFields(self, bindingAttr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.FieldInfo]:
        ...

    def GetInterface(self, name: str, ignoreCase: bool) -> typing.Type:
        ...

    def GetInterfaceMap(self, interfaceType: typing.Type) -> System.Reflection.InterfaceMapping:
        ...

    def GetInterfaces(self) -> typing.List[typing.Type]:
        ...

    def GetMember(self, name: str, type: System.Reflection.MemberTypes, bindingAttr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.MemberInfo]:
        ...

    def GetMembers(self, bindingAttr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.MemberInfo]:
        ...

    def GetMemberWithSameMetadataDefinitionAs(self, member: System.Reflection.MemberInfo) -> System.Reflection.MemberInfo:
        ...

    def GetMethodImpl(self, name: str, bindingAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, callConvention: System.Reflection.CallingConventions, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        """This method is protected."""
        ...

    def GetMethods(self, bindingAttr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.MethodInfo]:
        ...

    def GetNestedType(self, name: str, bindingAttr: System.Reflection.BindingFlags) -> typing.Type:
        ...

    def GetNestedTypes(self, bindingAttr: System.Reflection.BindingFlags) -> typing.List[typing.Type]:
        ...

    def GetProperties(self, bindingAttr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.PropertyInfo]:
        ...

    def GetPropertyImpl(self, name: str, bindingAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, returnType: typing.Type, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.PropertyInfo:
        """This method is protected."""
        ...

    def HasElementTypeImpl(self) -> bool:
        """This method is protected."""
        ...

    def InvokeMember(self, name: str, invokeAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, target: typing.Any, args: typing.List[System.Object], modifiers: typing.List[System.Reflection.ParameterModifier], culture: System.Globalization.CultureInfo, namedParameters: typing.List[str]) -> System.Object:
        ...

    def IsArrayImpl(self) -> bool:
        """This method is protected."""
        ...

    def IsAssignableFrom(self, typeInfo: System.Reflection.TypeInfo) -> bool:
        ...

    def IsByRefImpl(self) -> bool:
        """This method is protected."""
        ...

    def IsCOMObjectImpl(self) -> bool:
        """This method is protected."""
        ...

    def IsDefined(self, attributeType: typing.Type, inherit: bool) -> bool:
        ...

    def IsPointerImpl(self) -> bool:
        """This method is protected."""
        ...

    def IsPrimitiveImpl(self) -> bool:
        """This method is protected."""
        ...

    def IsValueTypeImpl(self) -> bool:
        """This method is protected."""
        ...


class ObfuscateAssemblyAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def AssemblyIsPrivate(self) -> bool:
        ...

    @property
    def StripAfterObfuscation(self) -> bool:
        ...

    @StripAfterObfuscation.setter
    def StripAfterObfuscation(self, value: bool):
        ...

    def __init__(self, assemblyIsPrivate: bool) -> None:
        ...


class IntrospectionExtensions(System.Object):
    """This class has no documentation."""

    @staticmethod
    def GetTypeInfo(type: typing.Type) -> System.Reflection.TypeInfo:
        ...


class ExceptionHandlingClauseOptions(System.Enum):
    """This class has no documentation."""

    Clause = ...

    Filter = ...

    Finally = ...

    Fault = ...


class ExceptionHandlingClause(System.Object):
    """This class has no documentation."""

    @property
    def Flags(self) -> int:
        """This property contains the int value of a member of the System.Reflection.ExceptionHandlingClauseOptions enum."""
        ...

    @property
    def TryOffset(self) -> int:
        ...

    @property
    def TryLength(self) -> int:
        ...

    @property
    def HandlerOffset(self) -> int:
        ...

    @property
    def HandlerLength(self) -> int:
        ...

    @property
    def FilterOffset(self) -> int:
        ...

    @property
    def CatchType(self) -> typing.Type:
        ...

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def ToString(self) -> str:
        ...


class LocalVariableInfo(System.Object):
    """This class has no documentation."""

    @property
    def LocalType(self) -> typing.Type:
        ...

    @property
    def LocalIndex(self) -> int:
        ...

    @property
    def IsPinned(self) -> bool:
        ...

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def ToString(self) -> str:
        ...


class MethodBody(System.Object):
    """This class has no documentation."""

    @property
    def LocalSignatureMetadataToken(self) -> int:
        ...

    @property
    def LocalVariables(self) -> System.Collections.Generic.IList[System.Reflection.LocalVariableInfo]:
        ...

    @property
    def MaxStackSize(self) -> int:
        ...

    @property
    def InitLocals(self) -> bool:
        ...

    @property
    def ExceptionHandlingClauses(self) -> System.Collections.Generic.IList[System.Reflection.ExceptionHandlingClause]:
        ...

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def GetILAsByteArray(self) -> typing.List[int]:
        ...


class MethodBase(System.Reflection.MemberInfo, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def Attributes(self) -> int:
        """This property contains the int value of a member of the System.Reflection.MethodAttributes enum."""
        ...

    @property
    def MethodImplementationFlags(self) -> int:
        """This property contains the int value of a member of the System.Reflection.MethodImplAttributes enum."""
        ...

    @property
    def CallingConvention(self) -> int:
        """This property contains the int value of a member of the System.Reflection.CallingConventions enum."""
        ...

    @property
    def IsAbstract(self) -> bool:
        ...

    @property
    def IsConstructor(self) -> bool:
        ...

    @property
    def IsFinal(self) -> bool:
        ...

    @property
    def IsHideBySig(self) -> bool:
        ...

    @property
    def IsSpecialName(self) -> bool:
        ...

    @property
    def IsStatic(self) -> bool:
        ...

    @property
    def IsVirtual(self) -> bool:
        ...

    @property
    def IsAssembly(self) -> bool:
        ...

    @property
    def IsFamily(self) -> bool:
        ...

    @property
    def IsFamilyAndAssembly(self) -> bool:
        ...

    @property
    def IsFamilyOrAssembly(self) -> bool:
        ...

    @property
    def IsPrivate(self) -> bool:
        ...

    @property
    def IsPublic(self) -> bool:
        ...

    @property
    def IsConstructedGenericMethod(self) -> bool:
        ...

    @property
    def IsGenericMethod(self) -> bool:
        ...

    @property
    def IsGenericMethodDefinition(self) -> bool:
        ...

    @property
    def ContainsGenericParameters(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def MethodHandle(self) -> System.RuntimeMethodHandle:
        ...

    @property
    def IsSecurityCritical(self) -> bool:
        ...

    @property
    def IsSecuritySafeCritical(self) -> bool:
        ...

    @property
    def IsSecurityTransparent(self) -> bool:
        ...

    MethodNameBufferSize: int = 100

    MaxStackAllocArgCount: int = 4

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def Equals(self, obj: typing.Any) -> bool:
        ...

    @staticmethod
    def GetCurrentMethod() -> System.Reflection.MethodBase:
        ...

    def GetGenericArguments(self) -> typing.List[typing.Type]:
        ...

    def GetHashCode(self) -> int:
        ...

    def GetMethodBody(self) -> System.Reflection.MethodBody:
        ...

    @staticmethod
    @overload
    def GetMethodFromHandle(handle: System.RuntimeMethodHandle) -> System.Reflection.MethodBase:
        ...

    @staticmethod
    @overload
    def GetMethodFromHandle(handle: System.RuntimeMethodHandle, declaringType: System.RuntimeTypeHandle) -> System.Reflection.MethodBase:
        ...

    def GetMethodImplementationFlags(self) -> int:
        """:returns: This method returns the int value of a member of the System.Reflection.MethodImplAttributes enum."""
        ...

    def GetParameters(self) -> typing.List[System.Reflection.ParameterInfo]:
        ...

    @overload
    def Invoke(self, obj: typing.Any, parameters: typing.List[System.Object]) -> System.Object:
        ...

    @overload
    def Invoke(self, obj: typing.Any, invokeAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, parameters: typing.List[System.Object], culture: System.Globalization.CultureInfo) -> System.Object:
        ...


class CustomAttributeFormatException(System.FormatException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...


class IReflect(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def UnderlyingSystemType(self) -> typing.Type:
        ...

    def GetField(self, name: str, bindingAttr: System.Reflection.BindingFlags) -> System.Reflection.FieldInfo:
        ...

    def GetFields(self, bindingAttr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.FieldInfo]:
        ...

    def GetMember(self, name: str, bindingAttr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.MemberInfo]:
        ...

    def GetMembers(self, bindingAttr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.MemberInfo]:
        ...

    @overload
    def GetMethod(self, name: str, bindingAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def GetMethod(self, name: str, bindingAttr: System.Reflection.BindingFlags) -> System.Reflection.MethodInfo:
        ...

    def GetMethods(self, bindingAttr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.MethodInfo]:
        ...

    def GetProperties(self, bindingAttr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.PropertyInfo]:
        ...

    @overload
    def GetProperty(self, name: str, bindingAttr: System.Reflection.BindingFlags) -> System.Reflection.PropertyInfo:
        ...

    @overload
    def GetProperty(self, name: str, bindingAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, returnType: typing.Type, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.PropertyInfo:
        ...

    def InvokeMember(self, name: str, invokeAttr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, target: typing.Any, args: typing.List[System.Object], modifiers: typing.List[System.Reflection.ParameterModifier], culture: System.Globalization.CultureInfo, namedParameters: typing.List[str]) -> System.Object:
        ...


class AssemblyDefaultAliasAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def DefaultAlias(self) -> str:
        ...

    def __init__(self, defaultAlias: str) -> None:
        ...


class ObfuscationAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def StripAfterObfuscation(self) -> bool:
        ...

    @StripAfterObfuscation.setter
    def StripAfterObfuscation(self, value: bool):
        ...

    @property
    def Exclude(self) -> bool:
        ...

    @Exclude.setter
    def Exclude(self, value: bool):
        ...

    @property
    def ApplyToMembers(self) -> bool:
        ...

    @ApplyToMembers.setter
    def ApplyToMembers(self, value: bool):
        ...

    @property
    def Feature(self) -> str:
        ...

    @Feature.setter
    def Feature(self, value: str):
        ...

    def __init__(self) -> None:
        ...


class ReflectionTypeLoadException(System.SystemException, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    @property
    def Types(self) -> typing.List[typing.Type]:
        ...

    @property
    def LoaderExceptions(self) -> typing.List[System.Exception]:
        ...

    @property
    def Message(self) -> str:
        ...

    @overload
    def __init__(self, classes: typing.List[typing.Type], exceptions: typing.List[System.Exception]) -> None:
        ...

    @overload
    def __init__(self, classes: typing.List[typing.Type], exceptions: typing.List[System.Exception], message: str) -> None:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def ToString(self) -> str:
        ...


class FieldAttributes(System.Enum):
    """This class has no documentation."""

    FieldAccessMask = ...

    PrivateScope = ...

    Private = ...

    FamANDAssem = ...

    Assembly = ...

    Family = ...

    FamORAssem = ...

    Public = ...

    Static = ...

    InitOnly = ...

    Literal = ...

    NotSerialized = ...

    SpecialName = ...

    PinvokeImpl = ...

    RTSpecialName = ...

    HasFieldMarshal = ...

    HasDefault = ...

    HasFieldRVA = ...

    ReservedMask = ...


class AssemblyFileVersionAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Version(self) -> str:
        ...

    def __init__(self, version: str) -> None:
        ...


class AssemblyCompanyAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Company(self) -> str:
        ...

    def __init__(self, company: str) -> None:
        ...


class AssemblyDescriptionAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Description(self) -> str:
        ...

    def __init__(self, description: str) -> None:
        ...


class PropertyAttributes(System.Enum):
    """This class has no documentation."""

    # Cannot convert to Python: None = ...

    SpecialName = ...

    RTSpecialName = ...

    HasDefault = ...

    Reserved2 = ...

    Reserved3 = ...

    Reserved4 = ...

    ReservedMask = ...


class MethodImplAttributes(System.Enum):
    """This class has no documentation."""

    CodeTypeMask = ...

    IL = ...

    Native = ...

    OPTIL = ...

    Runtime = ...

    ManagedMask = ...

    Unmanaged = ...

    Managed = ...

    ForwardRef = ...

    PreserveSig = ...

    InternalCall = ...

    Synchronized = ...

    NoInlining = ...

    AggressiveInlining = ...

    NoOptimization = ...

    AggressiveOptimization = ...

    MaxMethodImplVal = ...


class Missing(System.Object, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    Value: System.Reflection.Missing = ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class RuntimeReflectionExtensions(System.Object):
    """This class has no documentation."""

    @staticmethod
    def GetRuntimeBaseDefinition(method: System.Reflection.MethodInfo) -> System.Reflection.MethodInfo:
        ...

    @staticmethod
    def GetRuntimeEvent(type: typing.Type, name: str) -> System.Reflection.EventInfo:
        ...

    @staticmethod
    def GetRuntimeEvents(type: typing.Type) -> System.Collections.Generic.IEnumerable[System.Reflection.EventInfo]:
        ...

    @staticmethod
    def GetRuntimeField(type: typing.Type, name: str) -> System.Reflection.FieldInfo:
        ...

    @staticmethod
    def GetRuntimeFields(type: typing.Type) -> System.Collections.Generic.IEnumerable[System.Reflection.FieldInfo]:
        ...

    @staticmethod
    def GetRuntimeInterfaceMap(typeInfo: System.Reflection.TypeInfo, interfaceType: typing.Type) -> System.Reflection.InterfaceMapping:
        ...

    @staticmethod
    def GetRuntimeMethod(type: typing.Type, name: str, parameters: typing.List[typing.Type]) -> System.Reflection.MethodInfo:
        ...

    @staticmethod
    def GetRuntimeMethods(type: typing.Type) -> System.Collections.Generic.IEnumerable[System.Reflection.MethodInfo]:
        ...

    @staticmethod
    def GetRuntimeProperties(type: typing.Type) -> System.Collections.Generic.IEnumerable[System.Reflection.PropertyInfo]:
        ...

    @staticmethod
    def GetRuntimeProperty(type: typing.Type, name: str) -> System.Reflection.PropertyInfo:
        ...


class AssemblyContentType(System.Enum):
    """This class has no documentation."""

    Default = 0

    WindowsRuntime = 1


class TargetException(System.ApplicationException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...


class AssemblyNameProxy(System.MarshalByRefObject):
    """This class has no documentation."""

    def GetAssemblyName(self, assemblyFile: str) -> System.Reflection.AssemblyName:
        ...


class AssemblyCultureAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Culture(self) -> str:
        ...

    def __init__(self, culture: str) -> None:
        ...


class TargetInvocationException(System.ApplicationException):
    """This class has no documentation."""

    @overload
    def __init__(self, inner: System.Exception) -> None:
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception) -> None:
        ...


class NullabilityInfo(System.Object):
    """A class that represents nullability info"""

    @property
    def Type(self) -> typing.Type:
        """
        The System.Type of the member or generic parameter
        to which this NullabilityInfo belongs
        """
        ...

    @property
    def ReadState(self) -> int:
        """
        The nullability read state of the member
        
        This property contains the int value of a member of the System.Reflection.NullabilityState enum.
        """
        ...

    @ReadState.setter
    def ReadState(self, value: int):
        """
        The nullability read state of the member
        
        This property contains the int value of a member of the System.Reflection.NullabilityState enum.
        """
        ...

    @property
    def WriteState(self) -> int:
        """
        The nullability write state of the member
        
        This property contains the int value of a member of the System.Reflection.NullabilityState enum.
        """
        ...

    @WriteState.setter
    def WriteState(self, value: int):
        """
        The nullability write state of the member
        
        This property contains the int value of a member of the System.Reflection.NullabilityState enum.
        """
        ...

    @property
    def ElementType(self) -> System.Reflection.NullabilityInfo:
        """If the member type is an array, gives the NullabilityInfo of the elements of the array, null otherwise"""
        ...

    @property
    def GenericTypeArguments(self) -> typing.List[System.Reflection.NullabilityInfo]:
        """If the member type is a generic type, gives the array of NullabilityInfo for each type parameter"""
        ...


class NullabilityState(System.Enum):
    """An enum that represents nullability state"""

    Unknown = 0
    """Nullability context not enabled (oblivious)"""

    NotNull = 1
    """Non nullable value or reference type"""

    Nullable = 2
    """Nullable value or reference type"""


class InvalidFilterCriteriaException(System.ApplicationException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...


class ReflectionContext(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def GetTypeForObject(self, value: typing.Any) -> System.Reflection.TypeInfo:
        ...

    def MapAssembly(self, assembly: System.Reflection.Assembly) -> System.Reflection.Assembly:
        ...

    def MapType(self, type: System.Reflection.TypeInfo) -> System.Reflection.TypeInfo:
        ...


class ProcessorArchitecture(System.Enum):
    """This class has no documentation."""

    # Cannot convert to Python: None = ...

    MSIL = ...

    X86 = ...

    IA64 = ...

    Amd64 = ...

    Arm = ...


class AssemblyNameFlags(System.Enum):
    """This class has no documentation."""

    # Cannot convert to Python: None = ...

    PublicKey = ...

    EnableJITcompileOptimizer = ...

    EnableJITcompileTracking = ...

    Retargetable = ...


class AssemblyVersionAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Version(self) -> str:
        ...

    def __init__(self, version: str) -> None:
        ...


class Pointer(System.Object, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    @staticmethod
    def Box(ptr: typing.Any, type: typing.Type) -> System.Object:
        ...

    def Equals(self, obj: typing.Any) -> bool:
        ...

    def GetHashCode(self) -> int:
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    @staticmethod
    def Unbox(ptr: typing.Any) -> typing.Any:
        ...


class AssemblyProductAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Product(self) -> str:
        ...

    def __init__(self, product: str) -> None:
        ...


class AssemblyMetadataAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Key(self) -> str:
        ...

    @property
    def Value(self) -> str:
        ...

    def __init__(self, key: str, value: str) -> None:
        ...


class TargetParameterCountException(System.ApplicationException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception) -> None:
        ...


class AssemblyDelaySignAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def DelaySign(self) -> bool:
        ...

    def __init__(self, delaySign: bool) -> None:
        ...


class DefaultMemberAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def MemberName(self) -> str:
        ...

    def __init__(self, memberName: str) -> None:
        ...


class TypeAttributes(System.Enum):
    """This class has no documentation."""

    VisibilityMask = ...

    NotPublic = ...

    Public = ...

    NestedPublic = ...

    NestedPrivate = ...

    NestedFamily = ...

    NestedAssembly = ...

    NestedFamANDAssem = ...

    NestedFamORAssem = ...

    LayoutMask = ...

    AutoLayout = ...

    SequentialLayout = ...

    ExplicitLayout = ...

    ClassSemanticsMask = ...

    Class = ...

    Interface = ...

    Abstract = ...

    Sealed = ...

    SpecialName = ...

    Import = ...

    Serializable = ...

    WindowsRuntime = ...

    StringFormatMask = ...

    AnsiClass = ...

    UnicodeClass = ...

    AutoClass = ...

    CustomFormatClass = ...

    CustomFormatMask = ...

    BeforeFieldInit = ...

    RTSpecialName = ...

    HasSecurity = ...

    ReservedMask = ...


class AssemblyTitleAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Title(self) -> str:
        ...

    def __init__(self, title: str) -> None:
        ...


class AssemblyCopyrightAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Copyright(self) -> str:
        ...

    def __init__(self, copyright: str) -> None:
        ...


class AssemblyKeyFileAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def KeyFile(self) -> str:
        ...

    def __init__(self, keyFile: str) -> None:
        ...


class EventAttributes(System.Enum):
    """This class has no documentation."""

    # Cannot convert to Python: None = ...

    SpecialName = ...

    RTSpecialName = ...

    ReservedMask = ...


class AssemblyTrademarkAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Trademark(self) -> str:
        ...

    def __init__(self, trademark: str) -> None:
        ...


class GenericParameterAttributes(System.Enum):
    """This class has no documentation."""

    # Cannot convert to Python: None = ...

    VarianceMask = ...

    Covariant = ...

    Contravariant = ...

    SpecialConstraintMask = ...

    ReferenceTypeConstraint = ...

    NotNullableValueTypeConstraint = ...

    DefaultConstructorConstraint = ...


class MethodAttributes(System.Enum):
    """This class has no documentation."""

    MemberAccessMask = ...

    PrivateScope = ...

    Private = ...

    FamANDAssem = ...

    Assembly = ...

    Family = ...

    FamORAssem = ...

    Public = ...

    Static = ...

    Final = ...

    Virtual = ...

    HideBySig = ...

    CheckAccessOnOverride = ...

    VtableLayoutMask = ...

    ReuseSlot = ...

    NewSlot = ...

    Abstract = ...

    SpecialName = ...

    PinvokeImpl = ...

    UnmanagedExport = ...

    RTSpecialName = ...

    HasSecurity = ...

    RequireSecObject = ...

    ReservedMask = ...


class ResourceAttributes(System.Enum):
    """This class has no documentation."""

    Public = ...

    Private = ...


class CustomAttributeExtensions(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def GetCustomAttribute(element: System.Reflection.Assembly, attributeType: typing.Type) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def GetCustomAttribute(element: System.Reflection.Module, attributeType: typing.Type) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def GetCustomAttribute(element: System.Reflection.MemberInfo, attributeType: typing.Type) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def GetCustomAttribute(element: System.Reflection.ParameterInfo, attributeType: typing.Type) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def GetCustomAttribute(element: System.Reflection.Assembly) -> System_Reflection_CustomAttributeExtensions_GetCustomAttribute_T:
        ...

    @staticmethod
    @overload
    def GetCustomAttribute(element: System.Reflection.Module) -> System_Reflection_CustomAttributeExtensions_GetCustomAttribute_T:
        ...

    @staticmethod
    @overload
    def GetCustomAttribute(element: System.Reflection.MemberInfo) -> System_Reflection_CustomAttributeExtensions_GetCustomAttribute_T:
        ...

    @staticmethod
    @overload
    def GetCustomAttribute(element: System.Reflection.ParameterInfo) -> System_Reflection_CustomAttributeExtensions_GetCustomAttribute_T:
        ...

    @staticmethod
    @overload
    def GetCustomAttribute(element: System.Reflection.MemberInfo, attributeType: typing.Type, inherit: bool) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def GetCustomAttribute(element: System.Reflection.ParameterInfo, attributeType: typing.Type, inherit: bool) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def GetCustomAttribute(element: System.Reflection.MemberInfo, inherit: bool) -> System_Reflection_CustomAttributeExtensions_GetCustomAttribute_T:
        ...

    @staticmethod
    @overload
    def GetCustomAttribute(element: System.Reflection.ParameterInfo, inherit: bool) -> System_Reflection_CustomAttributeExtensions_GetCustomAttribute_T:
        ...

    @staticmethod
    @overload
    def GetCustomAttributes(element: System.Reflection.Assembly) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def GetCustomAttributes(element: System.Reflection.Module) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def GetCustomAttributes(element: System.Reflection.MemberInfo) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def GetCustomAttributes(element: System.Reflection.ParameterInfo) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def GetCustomAttributes(element: System.Reflection.MemberInfo, inherit: bool) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def GetCustomAttributes(element: System.Reflection.ParameterInfo, inherit: bool) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def GetCustomAttributes(element: System.Reflection.Assembly, attributeType: typing.Type) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def GetCustomAttributes(element: System.Reflection.Module, attributeType: typing.Type) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def GetCustomAttributes(element: System.Reflection.MemberInfo, attributeType: typing.Type) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def GetCustomAttributes(element: System.Reflection.ParameterInfo, attributeType: typing.Type) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def GetCustomAttributes(element: System.Reflection.Assembly) -> System.Collections.Generic.IEnumerable[System_Reflection_CustomAttributeExtensions_GetCustomAttributes_T]:
        ...

    @staticmethod
    @overload
    def GetCustomAttributes(element: System.Reflection.Module) -> System.Collections.Generic.IEnumerable[System_Reflection_CustomAttributeExtensions_GetCustomAttributes_T]:
        ...

    @staticmethod
    @overload
    def GetCustomAttributes(element: System.Reflection.MemberInfo) -> System.Collections.Generic.IEnumerable[System_Reflection_CustomAttributeExtensions_GetCustomAttributes_T]:
        ...

    @staticmethod
    @overload
    def GetCustomAttributes(element: System.Reflection.ParameterInfo) -> System.Collections.Generic.IEnumerable[System_Reflection_CustomAttributeExtensions_GetCustomAttributes_T]:
        ...

    @staticmethod
    @overload
    def GetCustomAttributes(element: System.Reflection.MemberInfo, attributeType: typing.Type, inherit: bool) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def GetCustomAttributes(element: System.Reflection.ParameterInfo, attributeType: typing.Type, inherit: bool) -> System.Collections.Generic.IEnumerable[System.Attribute]:
        ...

    @staticmethod
    @overload
    def GetCustomAttributes(element: System.Reflection.MemberInfo, inherit: bool) -> System.Collections.Generic.IEnumerable[System_Reflection_CustomAttributeExtensions_GetCustomAttributes_T]:
        ...

    @staticmethod
    @overload
    def GetCustomAttributes(element: System.Reflection.ParameterInfo, inherit: bool) -> System.Collections.Generic.IEnumerable[System_Reflection_CustomAttributeExtensions_GetCustomAttributes_T]:
        ...

    @staticmethod
    @overload
    def IsDefined(element: System.Reflection.Assembly, attributeType: typing.Type) -> bool:
        ...

    @staticmethod
    @overload
    def IsDefined(element: System.Reflection.Module, attributeType: typing.Type) -> bool:
        ...

    @staticmethod
    @overload
    def IsDefined(element: System.Reflection.MemberInfo, attributeType: typing.Type) -> bool:
        ...

    @staticmethod
    @overload
    def IsDefined(element: System.Reflection.ParameterInfo, attributeType: typing.Type) -> bool:
        ...

    @staticmethod
    @overload
    def IsDefined(element: System.Reflection.MemberInfo, attributeType: typing.Type, inherit: bool) -> bool:
        ...

    @staticmethod
    @overload
    def IsDefined(element: System.Reflection.ParameterInfo, attributeType: typing.Type, inherit: bool) -> bool:
        ...


class AssemblySignatureKeyAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def PublicKey(self) -> str:
        ...

    @property
    def Countersignature(self) -> str:
        ...

    def __init__(self, publicKey: str, countersignature: str) -> None:
        ...


class AssemblyKeyNameAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def KeyName(self) -> str:
        ...

    def __init__(self, keyName: str) -> None:
        ...


class AssemblyInformationalVersionAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def InformationalVersion(self) -> str:
        ...

    def __init__(self, informationalVersion: str) -> None:
        ...


class NullabilityInfoContext(System.Object):
    """
    Provides APIs for populating nullability information/context from reflection members:
    ParameterInfo, FieldInfo, PropertyInfo and EventInfo.
    """

    IsSupported: bool

    @overload
    def Create(self, parameterInfo: System.Reflection.ParameterInfo) -> System.Reflection.NullabilityInfo:
        """
        Populates NullabilityInfo for the given ParameterInfo.
        If the nullablePublicOnly feature is set for an assembly, like it does in .NET SDK, the private and/or internal member's
        nullability attributes are omitted, in this case the API will return NullabilityState.Unknown state.
        
        :param parameterInfo: The parameter which nullability info gets populated
        :returns: NullabilityInfo.
        """
        ...

    @overload
    def Create(self, propertyInfo: System.Reflection.PropertyInfo) -> System.Reflection.NullabilityInfo:
        """
        Populates NullabilityInfo for the given PropertyInfo.
        If the nullablePublicOnly feature is set for an assembly, like it does in .NET SDK, the private and/or internal member's
        nullability attributes are omitted, in this case the API will return NullabilityState.Unknown state.
        
        :param propertyInfo: The parameter which nullability info gets populated
        :returns: NullabilityInfo.
        """
        ...

    @overload
    def Create(self, eventInfo: System.Reflection.EventInfo) -> System.Reflection.NullabilityInfo:
        """
        Populates NullabilityInfo for the given EventInfo.
        If the nullablePublicOnly feature is set for an assembly, like it does in .NET SDK, the private and/or internal member's
        nullability attributes are omitted, in this case the API will return NullabilityState.Unknown state.
        
        :param eventInfo: The parameter which nullability info gets populated
        :returns: NullabilityInfo.
        """
        ...

    @overload
    def Create(self, fieldInfo: System.Reflection.FieldInfo) -> System.Reflection.NullabilityInfo:
        """
        Populates NullabilityInfo for the given FieldInfo
        If the nullablePublicOnly feature is set for an assembly, like it does in .NET SDK, the private and/or internal member's
        nullability attributes are omitted, in this case the API will return NullabilityState.Unknown state.
        
        :param fieldInfo: The parameter which nullability info gets populated
        :returns: NullabilityInfo.
        """
        ...


class AssemblyFlagsAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Flags(self) -> int:
        """AssemblyFlagsAttribute.Flags has been deprecated. Use AssemblyFlags instead."""
        warnings.warn("AssemblyFlagsAttribute.Flags has been deprecated. Use AssemblyFlags instead.", DeprecationWarning)

    @property
    def AssemblyFlags(self) -> int:
        ...

    @overload
    def __init__(self, assemblyFlags: System.Reflection.AssemblyNameFlags) -> None:
        ...

    @overload
    def __init__(self, flags: int) -> None:
        """This constructor has been deprecated. Use AssemblyFlagsAttribute(AssemblyNameFlags) instead."""
        ...

    @overload
    def __init__(self, assemblyFlags: int) -> None:
        """This constructor has been deprecated. Use AssemblyFlagsAttribute(AssemblyNameFlags) instead."""
        ...


class AssemblyConfigurationAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Configuration(self) -> str:
        ...

    def __init__(self, configuration: str) -> None:
        ...


class AssemblyAlgorithmIdAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def AlgorithmId(self) -> int:
        ...

    @overload
    def __init__(self, algorithmId: System.Reflection.AssemblyHashAlgorithm) -> None:
        ...

    @overload
    def __init__(self, algorithmId: int) -> None:
        ...


class AmbiguousMatchException(System.SystemException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception) -> None:
        ...


class ICustomTypeProvider(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def GetCustomType(self) -> typing.Type:
        ...


class _EventContainer(typing.Generic[System_Reflection__EventContainer_Callable, System_Reflection__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_Reflection__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_Reflection__EventContainer_Callable) -> None:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_Reflection__EventContainer_Callable) -> None:
        """Unregisters an event handler."""
        ...


