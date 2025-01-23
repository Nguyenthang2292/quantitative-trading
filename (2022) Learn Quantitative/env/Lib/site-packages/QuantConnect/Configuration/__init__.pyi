from typing import overload
import typing

import QuantConnect.Configuration
import System
import System.Collections.Generic

QuantConnect_Configuration_Config_GetValue_T = typing.TypeVar("QuantConnect_Configuration_Config_GetValue_T")
QuantConnect_Configuration_Config_TryGetValue_T = typing.TypeVar("QuantConnect_Configuration_Config_TryGetValue_T")


class CommandLineOption(System.Object):
    """Auxiliary class to keep information about a specific command line option"""

    @property
    def Type(self) -> typing.Any:
        """Command line option type"""
        ...

    @property
    def Description(self) -> str:
        """Command line option description"""
        ...

    @property
    def Name(self) -> str:
        """Command line option name"""
        ...

    def __init__(self, name: str, type: typing.Any, description: str = ...) -> None:
        """Command line option contructor"""
        ...


class ApplicationParser(System.Object):
    """Command Line application parser"""

    @staticmethod
    def GetParameterOrDefault(optionsObject: System.Collections.Generic.IReadOnlyDictionary[str, System.Object], parameter: str, defaultValue: str) -> str:
        ...

    @staticmethod
    def GetParameterOrExit(optionsObject: System.Collections.Generic.IReadOnlyDictionary[str, System.Object], parameter: str) -> str:
        ...

    @staticmethod
    def Parse(applicationName: str, applicationDescription: str, applicationHelpText: str, args: typing.List[str], options: System.Collections.Generic.List[QuantConnect.Configuration.CommandLineOption], noArgsShowHelp: bool = False) -> System.Collections.Generic.Dictionary[str, System.Object]:
        """
        This function will parse args based on options and will show application name, version, help
        
        :param applicationName: The application name to be shown
        :param applicationDescription: The application description to be shown
        :param applicationHelpText: The application help text
        :param args: The command line arguments
        :param options: The applications command line available options
        :param noArgsShowHelp: To show help when no command line arguments were provided
        :returns: The user provided options. Key is option name.
        """
        ...

    @staticmethod
    def PrintMessageAndExit(exitCode: int = 0, message: str = ...) -> None:
        ...


class LeanArgumentParser(System.Object):
    """Command Line arguments parser for Lean configuration"""

    @staticmethod
    def ParseArguments(args: typing.List[str]) -> System.Collections.Generic.Dictionary[str, System.Object]:
        """Argument parser contructor"""
        ...


class Config(System.Object):
    """Configuration class loads the required external setup variables to launch the Lean engine."""

    @staticmethod
    @overload
    def Flatten(overrideEnvironment: str) -> typing.Any:
        """
        Flattens the jobject with respect to the selected environment and then
        removes the 'environments' node
        
        :param overrideEnvironment: The environment to use
        :returns: The flattened JObject.
        """
        ...

    @staticmethod
    @overload
    def Flatten(config: typing.Any, overrideEnvironment: str) -> typing.Any:
        """
        Flattens the jobject with respect to the selected environment and then
        removes the 'environments' node
        
        :param config: The configuration represented as a JObject
        :param overrideEnvironment: The environment to use
        :returns: The flattened JObject.
        """
        ...

    @staticmethod
    def Get(key: str, defaultValue: str = ...) -> str:
        """
        Get the matching config setting from the file searching for this key.
        
        :param key: String key value we're seaching for in the config file.
        :returns: String value of the configuration setting or empty string if nothing found.
        """
        ...

    @staticmethod
    def GetBool(key: str, defaultValue: bool = False) -> bool:
        """
        Get a boolean value configuration setting by a configuration key.
        
        :param key: String value of the configuration key.
        :param defaultValue: The default value to use if not found in configuration
        :returns: Boolean value of the config setting.
        """
        ...

    @staticmethod
    def GetDouble(key: str, defaultValue: float = 0.0) -> float:
        """
        Get the double value of a config string.
        
        :param key: Search key from the config file
        :param defaultValue: The default value to use if not found in configuration
        :returns: Double value of the config setting.
        """
        ...

    @staticmethod
    def GetEnvironment() -> str:
        """
        Gets the currently selected environment. If sub-environments are defined,
        they'll be returned as {env1}.{env2}
        
        :returns: The fully qualified currently selected environment.
        """
        ...

    @staticmethod
    def GetInt(key: str, defaultValue: int = 0) -> int:
        """
        Get the int value of a config string.
        
        :param key: Search key from the config file
        :param defaultValue: The default value to use if not found in configuration
        :returns: Int value of the config setting.
        """
        ...

    @staticmethod
    def GetToken(key: str) -> typing.Any:
        """Gets the underlying JToken for the specified key"""
        ...

    @staticmethod
    def GetValue(key: str, defaultValue: QuantConnect_Configuration_Config_GetValue_T = ...) -> QuantConnect_Configuration_Config_GetValue_T:
        """
        Gets a value from configuration and converts it to the requested type, assigning a default if
        the configuration is null or empty
        
        :param key: Search key from the config file
        :param defaultValue: The default value to use if not found in configuration
        :returns: Converted value of the config setting.
        """
        ...

    @staticmethod
    def MergeCommandLineArgumentsWithConfiguration(cliArguments: System.Collections.Generic.Dictionary[str, System.Object]) -> None:
        """Merge CLI arguments with configuration file + load custom config file via CLI arg"""
        ...

    @staticmethod
    def Reset() -> None:
        """
        Resets the config settings to their default values.
        Called in regression tests where multiple algorithms are run sequentially,
        and we need to guarantee that every test starts with the same configuration.
        """
        ...

    @staticmethod
    def Set(key: str, value: typing.Any) -> None:
        """
        Sets a configuration value. This is really only used to help testing. The key heye can be
        specified as {environment}.key to set a value on a specific environment
        
        :param key: The key to be set
        :param value: The new value
        """
        ...

    @staticmethod
    def SetConfigurationFile(fileName: str) -> None:
        """Set configuration file on-fly"""
        ...

    @staticmethod
    @overload
    def TryGetValue(key: str, value: typing.Optional[QuantConnect_Configuration_Config_TryGetValue_T]) -> typing.Union[bool, QuantConnect_Configuration_Config_TryGetValue_T]:
        """
        Tries to find the specified key and parse it as a T, using
        default(T) if unable to locate the key or unable to parse it
        
        :param key: The configuration key
        :param value: The output value. If the key is found and parsed successfully, it will be the parsed value, else default(T).
        :returns: True on successful parse or if they key is not found. False only when key is found but fails to parse.
        """
        ...

    @staticmethod
    @overload
    def TryGetValue(key: str, defaultValue: QuantConnect_Configuration_Config_TryGetValue_T, value: typing.Optional[QuantConnect_Configuration_Config_TryGetValue_T]) -> typing.Union[bool, QuantConnect_Configuration_Config_TryGetValue_T]:
        """
        Tries to find the specified key and parse it as a T, using
        defaultValue if unable to locate the key or unable to parse it
        
        :param key: The configuration key
        :param defaultValue: The default value to use on key not found or unsuccessful parse
        :param value: The output value. If the key is found and parsed successfully, it will be the parsed value, else defaultValue.
        :returns: True on successful parse or if they key is not found and using defaultValue. False only when key is found but fails to parse.
        """
        ...

    @staticmethod
    def Write() -> None:
        """Write the contents of the serialized configuration back to the disk."""
        ...


class ToolboxArgumentParser(System.Object):
    """Command Line arguments parser for Toolbox configuration"""

    @staticmethod
    def GetTickers(optionsObject: System.Collections.Generic.Dictionary[str, System.Object]) -> System.Collections.Generic.List[str]:
        """Helper method to get the tickers from the provided options"""
        ...

    @staticmethod
    def ParseArguments(args: typing.List[str]) -> System.Collections.Generic.Dictionary[str, System.Object]:
        """Argument parser contructor"""
        ...


class ReportArgumentParser(System.Object):
    """Command Line arguments parser for Report Creator"""

    @staticmethod
    def ParseArguments(args: typing.List[str]) -> System.Collections.Generic.Dictionary[str, System.Object]:
        """Parse and construct the args."""
        ...


