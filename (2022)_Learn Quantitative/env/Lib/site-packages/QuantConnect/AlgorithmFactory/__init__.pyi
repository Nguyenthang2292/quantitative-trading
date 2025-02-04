from typing import overload
import datetime
import typing

import QuantConnect
import QuantConnect.AlgorithmFactory
import QuantConnect.Interfaces
import QuantConnect.Util
import System
import System.Collections.Generic
import System.Reflection


class DebuggerHelper(System.Object):
    """Helper class used to start a new debugging session"""

    class DebuggingMethod(System.Enum):
        """The different implemented debugging methods"""

        LocalCmdline = 0
        """
        Local debugging through cmdline.
        Language.Python will use built in 'pdb'
        """

        VisualStudio = 1
        """
        Visual studio local debugging.
        Language.Python will use 'Python Tools for Visual Studio',
        attach manually selecting `Python` code type.
        """

        PTVSD = 2
        """
        Python Tool for Visual Studio Debugger for remote python debugging.
        Language.Python. Deprecated, routes to DebugPy which
        is it's replacement. Used in the same way.
        """

        DebugPy = 3
        """
        DebugPy - a debugger for Python.
        Language.Python can use  `Python Extension` in VS Code
        or attach to Python in Visual Studio
        """

        PyCharm = 4
        """
        PyCharm PyDev Debugger for remote python debugging.
        Language.Python will use 'Python Debug Server' in PyCharm
        """

    @staticmethod
    def Initialize(language: QuantConnect.Language, workersInitializationCallback: typing.Optional[typing.Callable[[], None]]) -> typing.Union[None, typing.Callable[[], None]]:
        """
        Will start a new debugging session
        
        :param language: The algorithms programming language
        :param workersInitializationCallback: Optionally, the debugging method will set an action which the data stack workers should execute so we can debug code executed by them, this is specially important for python.
        """
        ...


class Loader(System.MarshalByRefObject):
    """Loader creates and manages the memory and exception space of the algorithm, ensuring if it explodes the Lean Engine is intact."""

    @property
    def appDomain(self) -> System.AppDomain:
        """Memory space of the user algorithm"""
        ...

    @appDomain.setter
    def appDomain(self, value: System.AppDomain):
        """Memory space of the user algorithm"""
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new loader with a 10 second maximum load time that forces exactly one derived type to be found"""
        ...

    @overload
    def __init__(self, debugging: bool, language: QuantConnect.Language, loaderTimeLimit: datetime.timedelta, multipleTypeNameResolverFunction: typing.Callable[[System.Collections.Generic.List[str]], str], workerThread: QuantConnect.Util.WorkerThread = None) -> None:
        """
        Creates a new loader with the specified configuration
        
        :param debugging: True if we are debugging
        :param language: Which language are we trying to load
        :param loaderTimeLimit: Used to limit how long it takes to create a new instance
        :param multipleTypeNameResolverFunction: Used to resolve multiple type names found in assembly to a single type name, if null, defaults to names => names.SingleOrDefault()  When we search an assembly for derived types of IAlgorithm, sometimes the assembly will contain multiple matching types. This is the case for the QuantConnect.Algorithm assembly in this solution.  In order to pick the correct type, consumers must specify how to pick the type, that's what this function does, it picks the correct type from the list of types found within the assembly.
        :param workerThread: The worker thread instance the loader should use
        """
        ...

    @staticmethod
    def GetExtendedTypeNames(assembly: System.Reflection.Assembly) -> System.Collections.Generic.List[str]:
        """
        Get a list of all the matching type names in this DLL assembly:
        
        :param assembly: Assembly dll we're loading.
        :returns: String list of types available.
        """
        ...

    def TryCreateAlgorithmInstance(self, assemblyPath: str, algorithmInstance: typing.Optional[QuantConnect.Interfaces.IAlgorithm], errorMessage: typing.Optional[str]) -> typing.Union[bool, QuantConnect.Interfaces.IAlgorithm, str]:
        """
        Creates a new instance of the specified class in the library, safely.
        
        :param assemblyPath: Location of the DLL
        :param algorithmInstance: Output algorithm instance
        :param errorMessage: Output error message on failure
        :returns: Bool true on successfully loading the class.
        """
        ...

    def TryCreateAlgorithmInstanceWithIsolator(self, assemblyPath: str, ramLimit: int, algorithmInstance: typing.Optional[QuantConnect.Interfaces.IAlgorithm], errorMessage: typing.Optional[str]) -> typing.Union[bool, QuantConnect.Interfaces.IAlgorithm, str]:
        """
        Creates a new instance of the class in the library, safely.
        
        :param assemblyPath: Location of the DLL
        :param ramLimit: Limit of the RAM for this process
        :param algorithmInstance: Output algorithm instance
        :param errorMessage: Output error message on failure
        :returns: bool success.
        """
        ...

    def Unload(self) -> None:
        """Unload this factory's appDomain."""
        ...


