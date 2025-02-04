from typing import overload
import abc
import typing

import System
import System.Runtime.InteropServices.ComTypes


class FILETIME:
    """This class has no documentation."""

    @property
    def dwLowDateTime(self) -> int:
        ...

    @dwLowDateTime.setter
    def dwLowDateTime(self, value: int):
        ...

    @property
    def dwHighDateTime(self) -> int:
        ...

    @dwHighDateTime.setter
    def dwHighDateTime(self, value: int):
        ...


class STATSTG:
    """This class has no documentation."""

    @property
    def pwcsName(self) -> str:
        ...

    @pwcsName.setter
    def pwcsName(self, value: str):
        ...

    @property
    def type(self) -> int:
        ...

    @type.setter
    def type(self, value: int):
        ...

    @property
    def cbSize(self) -> int:
        ...

    @cbSize.setter
    def cbSize(self, value: int):
        ...

    @property
    def mtime(self) -> System.Runtime.InteropServices.ComTypes.FILETIME:
        ...

    @mtime.setter
    def mtime(self, value: System.Runtime.InteropServices.ComTypes.FILETIME):
        ...

    @property
    def ctime(self) -> System.Runtime.InteropServices.ComTypes.FILETIME:
        ...

    @ctime.setter
    def ctime(self, value: System.Runtime.InteropServices.ComTypes.FILETIME):
        ...

    @property
    def atime(self) -> System.Runtime.InteropServices.ComTypes.FILETIME:
        ...

    @atime.setter
    def atime(self, value: System.Runtime.InteropServices.ComTypes.FILETIME):
        ...

    @property
    def grfMode(self) -> int:
        ...

    @grfMode.setter
    def grfMode(self, value: int):
        ...

    @property
    def grfLocksSupported(self) -> int:
        ...

    @grfLocksSupported.setter
    def grfLocksSupported(self, value: int):
        ...

    @property
    def clsid(self) -> System.Guid:
        ...

    @clsid.setter
    def clsid(self, value: System.Guid):
        ...

    @property
    def grfStateBits(self) -> int:
        ...

    @grfStateBits.setter
    def grfStateBits(self, value: int):
        ...

    @property
    def reserved(self) -> int:
        ...

    @reserved.setter
    def reserved(self, value: int):
        ...


class IStream(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def Clone(self, ppstm: typing.Optional[System.Runtime.InteropServices.ComTypes.IStream]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.IStream]:
        ...

    def Commit(self, grfCommitFlags: int) -> None:
        ...

    def CopyTo(self, pstm: System.Runtime.InteropServices.ComTypes.IStream, cb: int, pcbRead: System.IntPtr, pcbWritten: System.IntPtr) -> None:
        ...

    def LockRegion(self, libOffset: int, cb: int, dwLockType: int) -> None:
        ...

    def Read(self, pv: typing.List[int], cb: int, pcbRead: System.IntPtr) -> None:
        ...

    def Revert(self) -> None:
        ...

    def Seek(self, dlibMove: int, dwOrigin: int, plibNewPosition: System.IntPtr) -> None:
        ...

    def SetSize(self, libNewSize: int) -> None:
        ...

    def Stat(self, pstatstg: typing.Optional[System.Runtime.InteropServices.ComTypes.STATSTG], grfStatFlag: int) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.STATSTG]:
        ...

    def UnlockRegion(self, libOffset: int, cb: int, dwLockType: int) -> None:
        ...

    def Write(self, pv: typing.List[int], cb: int, pcbWritten: System.IntPtr) -> None:
        ...


class IMoniker(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def BindToObject(self, pbc: System.Runtime.InteropServices.ComTypes.IBindCtx, pmkToLeft: System.Runtime.InteropServices.ComTypes.IMoniker, riidResult: System.Guid, ppvResult: typing.Optional[typing.Any]) -> typing.Union[None, typing.Any]:
        ...

    def BindToStorage(self, pbc: System.Runtime.InteropServices.ComTypes.IBindCtx, pmkToLeft: System.Runtime.InteropServices.ComTypes.IMoniker, riid: System.Guid, ppvObj: typing.Optional[typing.Any]) -> typing.Union[None, typing.Any]:
        ...

    def CommonPrefixWith(self, pmkOther: System.Runtime.InteropServices.ComTypes.IMoniker, ppmkPrefix: typing.Optional[System.Runtime.InteropServices.ComTypes.IMoniker]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.IMoniker]:
        ...

    def ComposeWith(self, pmkRight: System.Runtime.InteropServices.ComTypes.IMoniker, fOnlyIfNotGeneric: bool, ppmkComposite: typing.Optional[System.Runtime.InteropServices.ComTypes.IMoniker]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.IMoniker]:
        ...

    def Enum(self, fForward: bool, ppenumMoniker: typing.Optional[System.Runtime.InteropServices.ComTypes.IEnumMoniker]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.IEnumMoniker]:
        ...

    def GetClassID(self, pClassID: typing.Optional[System.Guid]) -> typing.Union[None, System.Guid]:
        ...

    def GetDisplayName(self, pbc: System.Runtime.InteropServices.ComTypes.IBindCtx, pmkToLeft: System.Runtime.InteropServices.ComTypes.IMoniker, ppszDisplayName: typing.Optional[str]) -> typing.Union[None, str]:
        ...

    def GetSizeMax(self, pcbSize: typing.Optional[int]) -> typing.Union[None, int]:
        ...

    def GetTimeOfLastChange(self, pbc: System.Runtime.InteropServices.ComTypes.IBindCtx, pmkToLeft: System.Runtime.InteropServices.ComTypes.IMoniker, pFileTime: typing.Optional[System.Runtime.InteropServices.ComTypes.FILETIME]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.FILETIME]:
        ...

    def Hash(self, pdwHash: typing.Optional[int]) -> typing.Union[None, int]:
        ...

    def Inverse(self, ppmk: typing.Optional[System.Runtime.InteropServices.ComTypes.IMoniker]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.IMoniker]:
        ...

    def IsDirty(self) -> int:
        ...

    def IsEqual(self, pmkOtherMoniker: System.Runtime.InteropServices.ComTypes.IMoniker) -> int:
        ...

    def IsRunning(self, pbc: System.Runtime.InteropServices.ComTypes.IBindCtx, pmkToLeft: System.Runtime.InteropServices.ComTypes.IMoniker, pmkNewlyRunning: System.Runtime.InteropServices.ComTypes.IMoniker) -> int:
        ...

    def IsSystemMoniker(self, pdwMksys: typing.Optional[int]) -> typing.Union[int, int]:
        ...

    def Load(self, pStm: System.Runtime.InteropServices.ComTypes.IStream) -> None:
        ...

    def ParseDisplayName(self, pbc: System.Runtime.InteropServices.ComTypes.IBindCtx, pmkToLeft: System.Runtime.InteropServices.ComTypes.IMoniker, pszDisplayName: str, pchEaten: typing.Optional[int], ppmkOut: typing.Optional[System.Runtime.InteropServices.ComTypes.IMoniker]) -> typing.Union[None, int, System.Runtime.InteropServices.ComTypes.IMoniker]:
        ...

    def Reduce(self, pbc: System.Runtime.InteropServices.ComTypes.IBindCtx, dwReduceHowFar: int, ppmkToLeft: System.Runtime.InteropServices.ComTypes.IMoniker, ppmkReduced: typing.Optional[System.Runtime.InteropServices.ComTypes.IMoniker]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.IMoniker]:
        ...

    def RelativePathTo(self, pmkOther: System.Runtime.InteropServices.ComTypes.IMoniker, ppmkRelPath: typing.Optional[System.Runtime.InteropServices.ComTypes.IMoniker]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.IMoniker]:
        ...

    def Save(self, pStm: System.Runtime.InteropServices.ComTypes.IStream, fClearDirty: bool) -> None:
        ...


class IEnumMoniker(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def Clone(self, ppenum: typing.Optional[System.Runtime.InteropServices.ComTypes.IEnumMoniker]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.IEnumMoniker]:
        ...

    def Next(self, celt: int, rgelt: typing.List[System.Runtime.InteropServices.ComTypes.IMoniker], pceltFetched: System.IntPtr) -> int:
        ...

    def Reset(self) -> None:
        ...

    def Skip(self, celt: int) -> int:
        ...


class IConnectionPointContainer(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def EnumConnectionPoints(self, ppEnum: typing.Optional[System.Runtime.InteropServices.ComTypes.IEnumConnectionPoints]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.IEnumConnectionPoints]:
        ...

    def FindConnectionPoint(self, riid: System.Guid, ppCP: typing.Optional[System.Runtime.InteropServices.ComTypes.IConnectionPoint]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.IConnectionPoint]:
        ...


class CONNECTDATA:
    """This class has no documentation."""

    @property
    def pUnk(self) -> System.Object:
        ...

    @pUnk.setter
    def pUnk(self, value: System.Object):
        ...

    @property
    def dwCookie(self) -> int:
        ...

    @dwCookie.setter
    def dwCookie(self, value: int):
        ...


class IEnumConnections(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def Clone(self, ppenum: typing.Optional[System.Runtime.InteropServices.ComTypes.IEnumConnections]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.IEnumConnections]:
        ...

    def Next(self, celt: int, rgelt: typing.List[System.Runtime.InteropServices.ComTypes.CONNECTDATA], pceltFetched: System.IntPtr) -> int:
        ...

    def Reset(self) -> None:
        ...

    def Skip(self, celt: int) -> int:
        ...


class IConnectionPoint(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def Advise(self, pUnkSink: typing.Any, pdwCookie: typing.Optional[int]) -> typing.Union[None, int]:
        ...

    def EnumConnections(self, ppEnum: typing.Optional[System.Runtime.InteropServices.ComTypes.IEnumConnections]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.IEnumConnections]:
        ...

    def GetConnectionInterface(self, pIID: typing.Optional[System.Guid]) -> typing.Union[None, System.Guid]:
        ...

    def GetConnectionPointContainer(self, ppCPC: typing.Optional[System.Runtime.InteropServices.ComTypes.IConnectionPointContainer]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.IConnectionPointContainer]:
        ...

    def Unadvise(self, dwCookie: int) -> None:
        ...


class TYPEKIND(System.Enum):
    """This class has no documentation."""

    TKIND_ENUM = 0

    TKIND_RECORD = ...

    TKIND_MODULE = ...

    TKIND_INTERFACE = ...

    TKIND_DISPATCH = ...

    TKIND_COCLASS = ...

    TKIND_ALIAS = ...

    TKIND_UNION = ...

    TKIND_MAX = ...


class TYPEFLAGS(System.Enum):
    """This class has no documentation."""

    TYPEFLAG_FAPPOBJECT = ...

    TYPEFLAG_FCANCREATE = ...

    TYPEFLAG_FLICENSED = ...

    TYPEFLAG_FPREDECLID = ...

    TYPEFLAG_FHIDDEN = ...

    TYPEFLAG_FCONTROL = ...

    TYPEFLAG_FDUAL = ...

    TYPEFLAG_FNONEXTENSIBLE = ...

    TYPEFLAG_FOLEAUTOMATION = ...

    TYPEFLAG_FRESTRICTED = ...

    TYPEFLAG_FAGGREGATABLE = ...

    TYPEFLAG_FREPLACEABLE = ...

    TYPEFLAG_FDISPATCHABLE = ...

    TYPEFLAG_FREVERSEBIND = ...

    TYPEFLAG_FPROXY = ...


class IMPLTYPEFLAGS(System.Enum):
    """This class has no documentation."""

    IMPLTYPEFLAG_FDEFAULT = ...

    IMPLTYPEFLAG_FSOURCE = ...

    IMPLTYPEFLAG_FRESTRICTED = ...

    IMPLTYPEFLAG_FDEFAULTVTABLE = ...


class TYPEDESC:
    """This class has no documentation."""

    @property
    def lpValue(self) -> System.IntPtr:
        ...

    @lpValue.setter
    def lpValue(self, value: System.IntPtr):
        ...

    @property
    def vt(self) -> int:
        ...

    @vt.setter
    def vt(self, value: int):
        ...


class IDLFLAG(System.Enum):
    """This class has no documentation."""

    IDLFLAG_NONE = ...

    IDLFLAG_FIN = ...

    IDLFLAG_FOUT = ...

    IDLFLAG_FLCID = ...

    IDLFLAG_FRETVAL = ...


class IDLDESC:
    """This class has no documentation."""

    @property
    def dwReserved(self) -> System.IntPtr:
        ...

    @dwReserved.setter
    def dwReserved(self, value: System.IntPtr):
        ...

    @property
    def wIDLFlags(self) -> System.Runtime.InteropServices.ComTypes.IDLFLAG:
        ...

    @wIDLFlags.setter
    def wIDLFlags(self, value: System.Runtime.InteropServices.ComTypes.IDLFLAG):
        ...


class TYPEATTR:
    """This class has no documentation."""

    MEMBER_ID_NIL: int = ...

    @property
    def guid(self) -> System.Guid:
        ...

    @guid.setter
    def guid(self, value: System.Guid):
        ...

    @property
    def lcid(self) -> int:
        ...

    @lcid.setter
    def lcid(self, value: int):
        ...

    @property
    def dwReserved(self) -> int:
        ...

    @dwReserved.setter
    def dwReserved(self, value: int):
        ...

    @property
    def memidConstructor(self) -> int:
        ...

    @memidConstructor.setter
    def memidConstructor(self, value: int):
        ...

    @property
    def memidDestructor(self) -> int:
        ...

    @memidDestructor.setter
    def memidDestructor(self, value: int):
        ...

    @property
    def lpstrSchema(self) -> System.IntPtr:
        ...

    @lpstrSchema.setter
    def lpstrSchema(self, value: System.IntPtr):
        ...

    @property
    def cbSizeInstance(self) -> int:
        ...

    @cbSizeInstance.setter
    def cbSizeInstance(self, value: int):
        ...

    @property
    def typekind(self) -> System.Runtime.InteropServices.ComTypes.TYPEKIND:
        ...

    @typekind.setter
    def typekind(self, value: System.Runtime.InteropServices.ComTypes.TYPEKIND):
        ...

    @property
    def cFuncs(self) -> int:
        ...

    @cFuncs.setter
    def cFuncs(self, value: int):
        ...

    @property
    def cVars(self) -> int:
        ...

    @cVars.setter
    def cVars(self, value: int):
        ...

    @property
    def cImplTypes(self) -> int:
        ...

    @cImplTypes.setter
    def cImplTypes(self, value: int):
        ...

    @property
    def cbSizeVft(self) -> int:
        ...

    @cbSizeVft.setter
    def cbSizeVft(self, value: int):
        ...

    @property
    def cbAlignment(self) -> int:
        ...

    @cbAlignment.setter
    def cbAlignment(self, value: int):
        ...

    @property
    def wTypeFlags(self) -> System.Runtime.InteropServices.ComTypes.TYPEFLAGS:
        ...

    @wTypeFlags.setter
    def wTypeFlags(self, value: System.Runtime.InteropServices.ComTypes.TYPEFLAGS):
        ...

    @property
    def wMajorVerNum(self) -> int:
        ...

    @wMajorVerNum.setter
    def wMajorVerNum(self, value: int):
        ...

    @property
    def wMinorVerNum(self) -> int:
        ...

    @wMinorVerNum.setter
    def wMinorVerNum(self, value: int):
        ...

    @property
    def tdescAlias(self) -> System.Runtime.InteropServices.ComTypes.TYPEDESC:
        ...

    @tdescAlias.setter
    def tdescAlias(self, value: System.Runtime.InteropServices.ComTypes.TYPEDESC):
        ...

    @property
    def idldescType(self) -> System.Runtime.InteropServices.ComTypes.IDLDESC:
        ...

    @idldescType.setter
    def idldescType(self, value: System.Runtime.InteropServices.ComTypes.IDLDESC):
        ...


class FUNCKIND(System.Enum):
    """This class has no documentation."""

    FUNC_VIRTUAL = 0

    FUNC_PUREVIRTUAL = 1

    FUNC_NONVIRTUAL = 2

    FUNC_STATIC = 3

    FUNC_DISPATCH = 4


class INVOKEKIND(System.Enum):
    """This class has no documentation."""

    INVOKE_FUNC = ...

    INVOKE_PROPERTYGET = ...

    INVOKE_PROPERTYPUT = ...

    INVOKE_PROPERTYPUTREF = ...


class CALLCONV(System.Enum):
    """This class has no documentation."""

    CC_CDECL = 1

    CC_MSCPASCAL = 2

    CC_PASCAL = ...

    CC_MACPASCAL = 3

    CC_STDCALL = 4

    CC_RESERVED = 5

    CC_SYSCALL = 6

    CC_MPWCDECL = 7

    CC_MPWPASCAL = 8

    CC_MAX = 9


class PARAMFLAG(System.Enum):
    """This class has no documentation."""

    PARAMFLAG_NONE = 0

    PARAMFLAG_FIN = ...

    PARAMFLAG_FOUT = ...

    PARAMFLAG_FLCID = ...

    PARAMFLAG_FRETVAL = ...

    PARAMFLAG_FOPT = ...

    PARAMFLAG_FHASDEFAULT = ...

    PARAMFLAG_FHASCUSTDATA = ...


class PARAMDESC:
    """This class has no documentation."""

    @property
    def lpVarValue(self) -> System.IntPtr:
        ...

    @lpVarValue.setter
    def lpVarValue(self, value: System.IntPtr):
        ...

    @property
    def wParamFlags(self) -> System.Runtime.InteropServices.ComTypes.PARAMFLAG:
        ...

    @wParamFlags.setter
    def wParamFlags(self, value: System.Runtime.InteropServices.ComTypes.PARAMFLAG):
        ...


class ELEMDESC:
    """This class has no documentation."""

    class DESCUNION:
        """This class has no documentation."""

        @property
        def idldesc(self) -> System.Runtime.InteropServices.ComTypes.IDLDESC:
            ...

        @idldesc.setter
        def idldesc(self, value: System.Runtime.InteropServices.ComTypes.IDLDESC):
            ...

        @property
        def paramdesc(self) -> System.Runtime.InteropServices.ComTypes.PARAMDESC:
            ...

        @paramdesc.setter
        def paramdesc(self, value: System.Runtime.InteropServices.ComTypes.PARAMDESC):
            ...

    @property
    def tdesc(self) -> System.Runtime.InteropServices.ComTypes.TYPEDESC:
        ...

    @tdesc.setter
    def tdesc(self, value: System.Runtime.InteropServices.ComTypes.TYPEDESC):
        ...

    @property
    def desc(self) -> System.Runtime.InteropServices.ComTypes.ELEMDESC.DESCUNION:
        ...

    @desc.setter
    def desc(self, value: System.Runtime.InteropServices.ComTypes.ELEMDESC.DESCUNION):
        ...


class FUNCDESC:
    """This class has no documentation."""

    @property
    def memid(self) -> int:
        ...

    @memid.setter
    def memid(self, value: int):
        ...

    @property
    def lprgscode(self) -> System.IntPtr:
        ...

    @lprgscode.setter
    def lprgscode(self, value: System.IntPtr):
        ...

    @property
    def lprgelemdescParam(self) -> System.IntPtr:
        ...

    @lprgelemdescParam.setter
    def lprgelemdescParam(self, value: System.IntPtr):
        ...

    @property
    def funckind(self) -> System.Runtime.InteropServices.ComTypes.FUNCKIND:
        ...

    @funckind.setter
    def funckind(self, value: System.Runtime.InteropServices.ComTypes.FUNCKIND):
        ...

    @property
    def invkind(self) -> System.Runtime.InteropServices.ComTypes.INVOKEKIND:
        ...

    @invkind.setter
    def invkind(self, value: System.Runtime.InteropServices.ComTypes.INVOKEKIND):
        ...

    @property
    def callconv(self) -> System.Runtime.InteropServices.ComTypes.CALLCONV:
        ...

    @callconv.setter
    def callconv(self, value: System.Runtime.InteropServices.ComTypes.CALLCONV):
        ...

    @property
    def cParams(self) -> int:
        ...

    @cParams.setter
    def cParams(self, value: int):
        ...

    @property
    def cParamsOpt(self) -> int:
        ...

    @cParamsOpt.setter
    def cParamsOpt(self, value: int):
        ...

    @property
    def oVft(self) -> int:
        ...

    @oVft.setter
    def oVft(self, value: int):
        ...

    @property
    def cScodes(self) -> int:
        ...

    @cScodes.setter
    def cScodes(self, value: int):
        ...

    @property
    def elemdescFunc(self) -> System.Runtime.InteropServices.ComTypes.ELEMDESC:
        ...

    @elemdescFunc.setter
    def elemdescFunc(self, value: System.Runtime.InteropServices.ComTypes.ELEMDESC):
        ...

    @property
    def wFuncFlags(self) -> int:
        ...

    @wFuncFlags.setter
    def wFuncFlags(self, value: int):
        ...


class VARKIND(System.Enum):
    """This class has no documentation."""

    VAR_PERINSTANCE = ...

    VAR_STATIC = ...

    VAR_CONST = ...

    VAR_DISPATCH = ...


class VARDESC:
    """This class has no documentation."""

    class DESCUNION:
        """This class has no documentation."""

        @property
        def oInst(self) -> int:
            ...

        @oInst.setter
        def oInst(self, value: int):
            ...

        @property
        def lpvarValue(self) -> System.IntPtr:
            ...

        @lpvarValue.setter
        def lpvarValue(self, value: System.IntPtr):
            ...

    @property
    def memid(self) -> int:
        ...

    @memid.setter
    def memid(self, value: int):
        ...

    @property
    def lpstrSchema(self) -> str:
        ...

    @lpstrSchema.setter
    def lpstrSchema(self, value: str):
        ...

    @property
    def desc(self) -> System.Runtime.InteropServices.ComTypes.VARDESC.DESCUNION:
        ...

    @desc.setter
    def desc(self, value: System.Runtime.InteropServices.ComTypes.VARDESC.DESCUNION):
        ...

    @property
    def elemdescVar(self) -> System.Runtime.InteropServices.ComTypes.ELEMDESC:
        ...

    @elemdescVar.setter
    def elemdescVar(self, value: System.Runtime.InteropServices.ComTypes.ELEMDESC):
        ...

    @property
    def wVarFlags(self) -> int:
        ...

    @wVarFlags.setter
    def wVarFlags(self, value: int):
        ...

    @property
    def varkind(self) -> System.Runtime.InteropServices.ComTypes.VARKIND:
        ...

    @varkind.setter
    def varkind(self, value: System.Runtime.InteropServices.ComTypes.VARKIND):
        ...


class DISPPARAMS:
    """This class has no documentation."""

    @property
    def rgvarg(self) -> System.IntPtr:
        ...

    @rgvarg.setter
    def rgvarg(self, value: System.IntPtr):
        ...

    @property
    def rgdispidNamedArgs(self) -> System.IntPtr:
        ...

    @rgdispidNamedArgs.setter
    def rgdispidNamedArgs(self, value: System.IntPtr):
        ...

    @property
    def cArgs(self) -> int:
        ...

    @cArgs.setter
    def cArgs(self, value: int):
        ...

    @property
    def cNamedArgs(self) -> int:
        ...

    @cNamedArgs.setter
    def cNamedArgs(self, value: int):
        ...


class EXCEPINFO:
    """This class has no documentation."""

    @property
    def wCode(self) -> int:
        ...

    @wCode.setter
    def wCode(self, value: int):
        ...

    @property
    def wReserved(self) -> int:
        ...

    @wReserved.setter
    def wReserved(self, value: int):
        ...

    @property
    def bstrSource(self) -> str:
        ...

    @bstrSource.setter
    def bstrSource(self, value: str):
        ...

    @property
    def bstrDescription(self) -> str:
        ...

    @bstrDescription.setter
    def bstrDescription(self, value: str):
        ...

    @property
    def bstrHelpFile(self) -> str:
        ...

    @bstrHelpFile.setter
    def bstrHelpFile(self, value: str):
        ...

    @property
    def dwHelpContext(self) -> int:
        ...

    @dwHelpContext.setter
    def dwHelpContext(self, value: int):
        ...

    @property
    def pvReserved(self) -> System.IntPtr:
        ...

    @pvReserved.setter
    def pvReserved(self, value: System.IntPtr):
        ...

    @property
    def pfnDeferredFillIn(self) -> System.IntPtr:
        ...

    @pfnDeferredFillIn.setter
    def pfnDeferredFillIn(self, value: System.IntPtr):
        ...

    @property
    def scode(self) -> int:
        ...

    @scode.setter
    def scode(self, value: int):
        ...


class FUNCFLAGS(System.Enum):
    """This class has no documentation."""

    FUNCFLAG_FRESTRICTED = ...

    FUNCFLAG_FSOURCE = ...

    FUNCFLAG_FBINDABLE = ...

    FUNCFLAG_FREQUESTEDIT = ...

    FUNCFLAG_FDISPLAYBIND = ...

    FUNCFLAG_FDEFAULTBIND = ...

    FUNCFLAG_FHIDDEN = ...

    FUNCFLAG_FUSESGETLASTERROR = ...

    FUNCFLAG_FDEFAULTCOLLELEM = ...

    FUNCFLAG_FUIDEFAULT = ...

    FUNCFLAG_FNONBROWSABLE = ...

    FUNCFLAG_FREPLACEABLE = ...

    FUNCFLAG_FIMMEDIATEBIND = ...


class VARFLAGS(System.Enum):
    """This class has no documentation."""

    VARFLAG_FREADONLY = ...

    VARFLAG_FSOURCE = ...

    VARFLAG_FBINDABLE = ...

    VARFLAG_FREQUESTEDIT = ...

    VARFLAG_FDISPLAYBIND = ...

    VARFLAG_FDEFAULTBIND = ...

    VARFLAG_FHIDDEN = ...

    VARFLAG_FRESTRICTED = ...

    VARFLAG_FDEFAULTCOLLELEM = ...

    VARFLAG_FUIDEFAULT = ...

    VARFLAG_FNONBROWSABLE = ...

    VARFLAG_FREPLACEABLE = ...

    VARFLAG_FIMMEDIATEBIND = ...


class DESCKIND(System.Enum):
    """This class has no documentation."""

    DESCKIND_NONE = 0

    DESCKIND_FUNCDESC = ...

    DESCKIND_VARDESC = ...

    DESCKIND_TYPECOMP = ...

    DESCKIND_IMPLICITAPPOBJ = ...

    DESCKIND_MAX = ...


class BINDPTR:
    """This class has no documentation."""

    @property
    def lpfuncdesc(self) -> System.IntPtr:
        ...

    @lpfuncdesc.setter
    def lpfuncdesc(self, value: System.IntPtr):
        ...

    @property
    def lpvardesc(self) -> System.IntPtr:
        ...

    @lpvardesc.setter
    def lpvardesc(self, value: System.IntPtr):
        ...

    @property
    def lptcomp(self) -> System.IntPtr:
        ...

    @lptcomp.setter
    def lptcomp(self, value: System.IntPtr):
        ...


class ITypeComp(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def Bind(self, szName: str, lHashVal: int, wFlags: int, ppTInfo: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeInfo], pDescKind: typing.Optional[System.Runtime.InteropServices.ComTypes.DESCKIND], pBindPtr: typing.Optional[System.Runtime.InteropServices.ComTypes.BINDPTR]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.ITypeInfo, System.Runtime.InteropServices.ComTypes.DESCKIND, System.Runtime.InteropServices.ComTypes.BINDPTR]:
        ...

    def BindType(self, szName: str, lHashVal: int, ppTInfo: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeInfo], ppTComp: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeComp]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.ITypeInfo, System.Runtime.InteropServices.ComTypes.ITypeComp]:
        ...


class ITypeLib(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def FindName(self, szNameBuf: str, lHashVal: int, ppTInfo: typing.List[System.Runtime.InteropServices.ComTypes.ITypeInfo], rgMemId: typing.List[int], pcFound: int) -> None:
        ...

    def GetDocumentation(self, index: int, strName: typing.Optional[str], strDocString: typing.Optional[str], dwHelpContext: typing.Optional[int], strHelpFile: typing.Optional[str]) -> typing.Union[None, str, str, int, str]:
        ...

    def GetLibAttr(self, ppTLibAttr: typing.Optional[System.IntPtr]) -> typing.Union[None, System.IntPtr]:
        ...

    def GetTypeComp(self, ppTComp: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeComp]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.ITypeComp]:
        ...

    def GetTypeInfo(self, index: int, ppTI: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeInfo]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.ITypeInfo]:
        ...

    def GetTypeInfoCount(self) -> int:
        ...

    def GetTypeInfoOfGuid(self, guid: System.Guid, ppTInfo: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeInfo]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.ITypeInfo]:
        ...

    def GetTypeInfoType(self, index: int, pTKind: typing.Optional[System.Runtime.InteropServices.ComTypes.TYPEKIND]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.TYPEKIND]:
        ...

    def IsName(self, szNameBuf: str, lHashVal: int) -> bool:
        ...

    def ReleaseTLibAttr(self, pTLibAttr: System.IntPtr) -> None:
        ...


class ITypeInfo(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def AddressOfMember(self, memid: int, invKind: System.Runtime.InteropServices.ComTypes.INVOKEKIND, ppv: typing.Optional[System.IntPtr]) -> typing.Union[None, System.IntPtr]:
        ...

    def CreateInstance(self, pUnkOuter: typing.Any, riid: System.Guid, ppvObj: typing.Optional[typing.Any]) -> typing.Union[None, typing.Any]:
        ...

    def GetContainingTypeLib(self, ppTLB: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeLib], pIndex: typing.Optional[int]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.ITypeLib, int]:
        ...

    def GetDllEntry(self, memid: int, invKind: System.Runtime.InteropServices.ComTypes.INVOKEKIND, pBstrDllName: System.IntPtr, pBstrName: System.IntPtr, pwOrdinal: System.IntPtr) -> None:
        ...

    def GetDocumentation(self, index: int, strName: typing.Optional[str], strDocString: typing.Optional[str], dwHelpContext: typing.Optional[int], strHelpFile: typing.Optional[str]) -> typing.Union[None, str, str, int, str]:
        ...

    def GetFuncDesc(self, index: int, ppFuncDesc: typing.Optional[System.IntPtr]) -> typing.Union[None, System.IntPtr]:
        ...

    def GetIDsOfNames(self, rgszNames: typing.List[str], cNames: int, pMemId: typing.List[int]) -> None:
        ...

    def GetImplTypeFlags(self, index: int, pImplTypeFlags: typing.Optional[System.Runtime.InteropServices.ComTypes.IMPLTYPEFLAGS]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.IMPLTYPEFLAGS]:
        ...

    def GetMops(self, memid: int, pBstrMops: typing.Optional[str]) -> typing.Union[None, str]:
        ...

    def GetNames(self, memid: int, rgBstrNames: typing.List[str], cMaxNames: int, pcNames: typing.Optional[int]) -> typing.Union[None, int]:
        ...

    def GetRefTypeInfo(self, hRef: int, ppTI: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeInfo]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.ITypeInfo]:
        ...

    def GetRefTypeOfImplType(self, index: int, href: typing.Optional[int]) -> typing.Union[None, int]:
        ...

    def GetTypeAttr(self, ppTypeAttr: typing.Optional[System.IntPtr]) -> typing.Union[None, System.IntPtr]:
        ...

    def GetTypeComp(self, ppTComp: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeComp]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.ITypeComp]:
        ...

    def GetVarDesc(self, index: int, ppVarDesc: typing.Optional[System.IntPtr]) -> typing.Union[None, System.IntPtr]:
        ...

    def Invoke(self, pvInstance: typing.Any, memid: int, wFlags: int, pDispParams: System.Runtime.InteropServices.ComTypes.DISPPARAMS, pVarResult: System.IntPtr, pExcepInfo: System.IntPtr, puArgErr: typing.Optional[int]) -> typing.Union[None, int]:
        ...

    def ReleaseFuncDesc(self, pFuncDesc: System.IntPtr) -> None:
        ...

    def ReleaseTypeAttr(self, pTypeAttr: System.IntPtr) -> None:
        ...

    def ReleaseVarDesc(self, pVarDesc: System.IntPtr) -> None:
        ...


class IEnumConnectionPoints(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def Clone(self, ppenum: typing.Optional[System.Runtime.InteropServices.ComTypes.IEnumConnectionPoints]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.IEnumConnectionPoints]:
        ...

    def Next(self, celt: int, rgelt: typing.List[System.Runtime.InteropServices.ComTypes.IConnectionPoint], pceltFetched: System.IntPtr) -> int:
        ...

    def Reset(self) -> None:
        ...

    def Skip(self, celt: int) -> int:
        ...


class IEnumVARIANT(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def Clone(self) -> System.Runtime.InteropServices.ComTypes.IEnumVARIANT:
        ...

    def Next(self, celt: int, rgVar: typing.List[System.Object], pceltFetched: System.IntPtr) -> int:
        ...

    def Reset(self) -> int:
        ...

    def Skip(self, celt: int) -> int:
        ...


class BIND_OPTS:
    """This class has no documentation."""

    @property
    def cbStruct(self) -> int:
        ...

    @cbStruct.setter
    def cbStruct(self, value: int):
        ...

    @property
    def grfFlags(self) -> int:
        ...

    @grfFlags.setter
    def grfFlags(self, value: int):
        ...

    @property
    def grfMode(self) -> int:
        ...

    @grfMode.setter
    def grfMode(self, value: int):
        ...

    @property
    def dwTickCountDeadline(self) -> int:
        ...

    @dwTickCountDeadline.setter
    def dwTickCountDeadline(self, value: int):
        ...


class IRunningObjectTable(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def EnumRunning(self, ppenumMoniker: typing.Optional[System.Runtime.InteropServices.ComTypes.IEnumMoniker]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.IEnumMoniker]:
        ...

    def GetObject(self, pmkObjectName: System.Runtime.InteropServices.ComTypes.IMoniker, ppunkObject: typing.Optional[typing.Any]) -> typing.Union[int, typing.Any]:
        ...

    def GetTimeOfLastChange(self, pmkObjectName: System.Runtime.InteropServices.ComTypes.IMoniker, pfiletime: typing.Optional[System.Runtime.InteropServices.ComTypes.FILETIME]) -> typing.Union[int, System.Runtime.InteropServices.ComTypes.FILETIME]:
        ...

    def IsRunning(self, pmkObjectName: System.Runtime.InteropServices.ComTypes.IMoniker) -> int:
        ...

    def NoteChangeTime(self, dwRegister: int, pfiletime: System.Runtime.InteropServices.ComTypes.FILETIME) -> None:
        ...

    def Register(self, grfFlags: int, punkObject: typing.Any, pmkObjectName: System.Runtime.InteropServices.ComTypes.IMoniker) -> int:
        ...

    def Revoke(self, dwRegister: int) -> None:
        ...


class IEnumString(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def Clone(self, ppenum: typing.Optional[System.Runtime.InteropServices.ComTypes.IEnumString]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.IEnumString]:
        ...

    def Next(self, celt: int, rgelt: typing.List[str], pceltFetched: System.IntPtr) -> int:
        ...

    def Reset(self) -> None:
        ...

    def Skip(self, celt: int) -> int:
        ...


class IBindCtx(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def EnumObjectParam(self, ppenum: typing.Optional[System.Runtime.InteropServices.ComTypes.IEnumString]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.IEnumString]:
        ...

    def GetBindOptions(self, pbindopts: System.Runtime.InteropServices.ComTypes.BIND_OPTS) -> None:
        ...

    def GetObjectParam(self, pszKey: str, ppunk: typing.Optional[typing.Any]) -> typing.Union[None, typing.Any]:
        ...

    def GetRunningObjectTable(self, pprot: typing.Optional[System.Runtime.InteropServices.ComTypes.IRunningObjectTable]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.IRunningObjectTable]:
        ...

    def RegisterObjectBound(self, punk: typing.Any) -> None:
        ...

    def RegisterObjectParam(self, pszKey: str, punk: typing.Any) -> None:
        ...

    def ReleaseBoundObjects(self) -> None:
        ...

    def RevokeObjectBound(self, punk: typing.Any) -> None:
        ...

    def RevokeObjectParam(self, pszKey: str) -> int:
        ...

    def SetBindOptions(self, pbindopts: System.Runtime.InteropServices.ComTypes.BIND_OPTS) -> None:
        ...


class IPersistFile(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def GetClassID(self, pClassID: typing.Optional[System.Guid]) -> typing.Union[None, System.Guid]:
        ...

    def GetCurFile(self, ppszFileName: typing.Optional[str]) -> typing.Union[None, str]:
        ...

    def IsDirty(self) -> int:
        ...

    def Load(self, pszFileName: str, dwMode: int) -> None:
        ...

    def Save(self, pszFileName: str, fRemember: bool) -> None:
        ...

    def SaveCompleted(self, pszFileName: str) -> None:
        ...


class ITypeInfo2(System.Runtime.InteropServices.ComTypes.ITypeInfo, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def AddressOfMember(self, memid: int, invKind: System.Runtime.InteropServices.ComTypes.INVOKEKIND, ppv: typing.Optional[System.IntPtr]) -> typing.Union[None, System.IntPtr]:
        ...

    def CreateInstance(self, pUnkOuter: typing.Any, riid: System.Guid, ppvObj: typing.Optional[typing.Any]) -> typing.Union[None, typing.Any]:
        ...

    def GetAllCustData(self, pCustData: System.IntPtr) -> None:
        ...

    def GetAllFuncCustData(self, index: int, pCustData: System.IntPtr) -> None:
        ...

    def GetAllImplTypeCustData(self, index: int, pCustData: System.IntPtr) -> None:
        ...

    def GetAllParamCustData(self, indexFunc: int, indexParam: int, pCustData: System.IntPtr) -> None:
        ...

    def GetAllVarCustData(self, index: int, pCustData: System.IntPtr) -> None:
        ...

    def GetContainingTypeLib(self, ppTLB: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeLib], pIndex: typing.Optional[int]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.ITypeLib, int]:
        ...

    def GetCustData(self, guid: System.Guid, pVarVal: typing.Optional[typing.Any]) -> typing.Union[None, typing.Any]:
        ...

    def GetDllEntry(self, memid: int, invKind: System.Runtime.InteropServices.ComTypes.INVOKEKIND, pBstrDllName: System.IntPtr, pBstrName: System.IntPtr, pwOrdinal: System.IntPtr) -> None:
        ...

    def GetDocumentation(self, index: int, strName: typing.Optional[str], strDocString: typing.Optional[str], dwHelpContext: typing.Optional[int], strHelpFile: typing.Optional[str]) -> typing.Union[None, str, str, int, str]:
        ...

    def GetDocumentation2(self, memid: int, pbstrHelpString: typing.Optional[str], pdwHelpStringContext: typing.Optional[int], pbstrHelpStringDll: typing.Optional[str]) -> typing.Union[None, str, int, str]:
        ...

    def GetFuncCustData(self, index: int, guid: System.Guid, pVarVal: typing.Optional[typing.Any]) -> typing.Union[None, typing.Any]:
        ...

    def GetFuncDesc(self, index: int, ppFuncDesc: typing.Optional[System.IntPtr]) -> typing.Union[None, System.IntPtr]:
        ...

    def GetFuncIndexOfMemId(self, memid: int, invKind: System.Runtime.InteropServices.ComTypes.INVOKEKIND, pFuncIndex: typing.Optional[int]) -> typing.Union[None, int]:
        ...

    def GetIDsOfNames(self, rgszNames: typing.List[str], cNames: int, pMemId: typing.List[int]) -> None:
        ...

    def GetImplTypeCustData(self, index: int, guid: System.Guid, pVarVal: typing.Optional[typing.Any]) -> typing.Union[None, typing.Any]:
        ...

    def GetImplTypeFlags(self, index: int, pImplTypeFlags: typing.Optional[System.Runtime.InteropServices.ComTypes.IMPLTYPEFLAGS]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.IMPLTYPEFLAGS]:
        ...

    def GetMops(self, memid: int, pBstrMops: typing.Optional[str]) -> typing.Union[None, str]:
        ...

    def GetNames(self, memid: int, rgBstrNames: typing.List[str], cMaxNames: int, pcNames: typing.Optional[int]) -> typing.Union[None, int]:
        ...

    def GetParamCustData(self, indexFunc: int, indexParam: int, guid: System.Guid, pVarVal: typing.Optional[typing.Any]) -> typing.Union[None, typing.Any]:
        ...

    def GetRefTypeInfo(self, hRef: int, ppTI: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeInfo]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.ITypeInfo]:
        ...

    def GetRefTypeOfImplType(self, index: int, href: typing.Optional[int]) -> typing.Union[None, int]:
        ...

    def GetTypeAttr(self, ppTypeAttr: typing.Optional[System.IntPtr]) -> typing.Union[None, System.IntPtr]:
        ...

    def GetTypeComp(self, ppTComp: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeComp]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.ITypeComp]:
        ...

    def GetTypeFlags(self, pTypeFlags: typing.Optional[int]) -> typing.Union[None, int]:
        ...

    def GetTypeKind(self, pTypeKind: typing.Optional[System.Runtime.InteropServices.ComTypes.TYPEKIND]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.TYPEKIND]:
        ...

    def GetVarCustData(self, index: int, guid: System.Guid, pVarVal: typing.Optional[typing.Any]) -> typing.Union[None, typing.Any]:
        ...

    def GetVarDesc(self, index: int, ppVarDesc: typing.Optional[System.IntPtr]) -> typing.Union[None, System.IntPtr]:
        ...

    def GetVarIndexOfMemId(self, memid: int, pVarIndex: typing.Optional[int]) -> typing.Union[None, int]:
        ...

    def Invoke(self, pvInstance: typing.Any, memid: int, wFlags: int, pDispParams: System.Runtime.InteropServices.ComTypes.DISPPARAMS, pVarResult: System.IntPtr, pExcepInfo: System.IntPtr, puArgErr: typing.Optional[int]) -> typing.Union[None, int]:
        ...

    def ReleaseFuncDesc(self, pFuncDesc: System.IntPtr) -> None:
        ...

    def ReleaseTypeAttr(self, pTypeAttr: System.IntPtr) -> None:
        ...

    def ReleaseVarDesc(self, pVarDesc: System.IntPtr) -> None:
        ...


class ITypeLib2(System.Runtime.InteropServices.ComTypes.ITypeLib, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def FindName(self, szNameBuf: str, lHashVal: int, ppTInfo: typing.List[System.Runtime.InteropServices.ComTypes.ITypeInfo], rgMemId: typing.List[int], pcFound: int) -> None:
        ...

    def GetAllCustData(self, pCustData: System.IntPtr) -> None:
        ...

    def GetCustData(self, guid: System.Guid, pVarVal: typing.Optional[typing.Any]) -> typing.Union[None, typing.Any]:
        ...

    def GetDocumentation(self, index: int, strName: typing.Optional[str], strDocString: typing.Optional[str], dwHelpContext: typing.Optional[int], strHelpFile: typing.Optional[str]) -> typing.Union[None, str, str, int, str]:
        ...

    def GetDocumentation2(self, index: int, pbstrHelpString: typing.Optional[str], pdwHelpStringContext: typing.Optional[int], pbstrHelpStringDll: typing.Optional[str]) -> typing.Union[None, str, int, str]:
        ...

    def GetLibAttr(self, ppTLibAttr: typing.Optional[System.IntPtr]) -> typing.Union[None, System.IntPtr]:
        ...

    def GetLibStatistics(self, pcUniqueNames: System.IntPtr, pcchUniqueNames: typing.Optional[int]) -> typing.Union[None, int]:
        ...

    def GetTypeComp(self, ppTComp: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeComp]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.ITypeComp]:
        ...

    def GetTypeInfo(self, index: int, ppTI: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeInfo]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.ITypeInfo]:
        ...

    def GetTypeInfoCount(self) -> int:
        ...

    def GetTypeInfoOfGuid(self, guid: System.Guid, ppTInfo: typing.Optional[System.Runtime.InteropServices.ComTypes.ITypeInfo]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.ITypeInfo]:
        ...

    def GetTypeInfoType(self, index: int, pTKind: typing.Optional[System.Runtime.InteropServices.ComTypes.TYPEKIND]) -> typing.Union[None, System.Runtime.InteropServices.ComTypes.TYPEKIND]:
        ...

    def IsName(self, szNameBuf: str, lHashVal: int) -> bool:
        ...

    def ReleaseTLibAttr(self, pTLibAttr: System.IntPtr) -> None:
        ...


class SYSKIND(System.Enum):
    """This class has no documentation."""

    SYS_WIN16 = 0

    SYS_WIN32 = ...

    SYS_MAC = ...

    SYS_WIN64 = ...


class LIBFLAGS(System.Enum):
    """This class has no documentation."""

    LIBFLAG_FRESTRICTED = ...

    LIBFLAG_FCONTROL = ...

    LIBFLAG_FHIDDEN = ...

    LIBFLAG_FHASDISKIMAGE = ...


class TYPELIBATTR:
    """This class has no documentation."""

    @property
    def guid(self) -> System.Guid:
        ...

    @guid.setter
    def guid(self, value: System.Guid):
        ...

    @property
    def lcid(self) -> int:
        ...

    @lcid.setter
    def lcid(self, value: int):
        ...

    @property
    def syskind(self) -> System.Runtime.InteropServices.ComTypes.SYSKIND:
        ...

    @syskind.setter
    def syskind(self, value: System.Runtime.InteropServices.ComTypes.SYSKIND):
        ...

    @property
    def wMajorVerNum(self) -> int:
        ...

    @wMajorVerNum.setter
    def wMajorVerNum(self, value: int):
        ...

    @property
    def wMinorVerNum(self) -> int:
        ...

    @wMinorVerNum.setter
    def wMinorVerNum(self, value: int):
        ...

    @property
    def wLibFlags(self) -> System.Runtime.InteropServices.ComTypes.LIBFLAGS:
        ...

    @wLibFlags.setter
    def wLibFlags(self, value: System.Runtime.InteropServices.ComTypes.LIBFLAGS):
        ...


