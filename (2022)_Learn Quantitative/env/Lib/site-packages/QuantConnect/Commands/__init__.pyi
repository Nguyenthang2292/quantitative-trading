from typing import overload
import abc
import typing

import QuantConnect
import QuantConnect.Commands
import QuantConnect.Interfaces
import QuantConnect.Packets
import System
import System.Collections.Generic
import System.IO


class ICommand(metaclass=abc.ABCMeta):
    """Represents a command that can be run against a single algorithm"""

    @property
    @abc.abstractmethod
    def Id(self) -> str:
        """Unique command id"""
        ...

    @Id.setter
    @abc.abstractmethod
    def Id(self, value: str):
        """Unique command id"""
        ...

    def Run(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> QuantConnect.Commands.CommandResultPacket:
        """
        Runs this command against the specified algorithm instance
        
        :param algorithm: The algorithm to run this command against
        """
        ...


class CommandResultPacket(QuantConnect.Packets.Packet):
    """Contains data held as the result of executing a command"""

    @property
    def CommandName(self) -> str:
        """Gets or sets the command that produced this packet"""
        ...

    @CommandName.setter
    def CommandName(self, value: str):
        """Gets or sets the command that produced this packet"""
        ...

    @property
    def Success(self) -> bool:
        """Gets or sets whether or not the"""
        ...

    @Success.setter
    def Success(self, value: bool):
        """Gets or sets whether or not the"""
        ...

    def __init__(self, command: QuantConnect.Commands.ICommand, success: bool) -> None:
        """Initializes a new instance of the CommandResultPacket class"""
        ...


class BaseCommand(System.Object, QuantConnect.Commands.ICommand, metaclass=abc.ABCMeta):
    """Base command implementation"""

    @property
    def Id(self) -> str:
        """Unique command id"""
        ...

    @Id.setter
    def Id(self, value: str):
        """Unique command id"""
        ...

    def GetSymbol(self, ticker: str, securityType: QuantConnect.SecurityType, market: str, symbol: typing.Union[QuantConnect.Symbol, str] = None) -> QuantConnect.Symbol:
        """
        Creats symbol using symbol properties.
        
        This method is protected.
        
        :param ticker: The string ticker symbol
        :param securityType: The security type of the ticker. If securityType == Option, then a canonical symbol is created
        :param market: The market the ticker resides in
        :param symbol: The algorithm to run this command against
        """
        ...

    def Run(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> QuantConnect.Commands.CommandResultPacket:
        """
        Runs this command against the specified algorithm instance
        
        :param algorithm: The algorithm to run this command against
        """
        ...


class OrderCommand(QuantConnect.Commands.BaseCommand):
    """Represents a command to submit an order to the algorithm"""

    @property
    def Symbol(self) -> QuantConnect.Symbol:
        """Gets or sets the symbol to be ordered"""
        ...

    @Symbol.setter
    def Symbol(self, value: QuantConnect.Symbol):
        """Gets or sets the symbol to be ordered"""
        ...

    @property
    def Ticker(self) -> str:
        """Gets or sets the string ticker symbol"""
        ...

    @Ticker.setter
    def Ticker(self, value: str):
        """Gets or sets the string ticker symbol"""
        ...

    @property
    def SecurityType(self) -> int:
        """
        Gets or sets the security type of the ticker.
        
        This property contains the int value of a member of the QuantConnect.SecurityType enum.
        """
        ...

    @SecurityType.setter
    def SecurityType(self, value: int):
        """
        Gets or sets the security type of the ticker.
        
        This property contains the int value of a member of the QuantConnect.SecurityType enum.
        """
        ...

    @property
    def Market(self) -> str:
        """Gets or sets the market the ticker resides in"""
        ...

    @Market.setter
    def Market(self, value: str):
        """Gets or sets the market the ticker resides in"""
        ...

    @property
    def OrderType(self) -> int:
        """
        Gets or sets the order type to be submted
        
        This property contains the int value of a member of the QuantConnect.Orders.OrderType enum.
        """
        ...

    @OrderType.setter
    def OrderType(self, value: int):
        """
        Gets or sets the order type to be submted
        
        This property contains the int value of a member of the QuantConnect.Orders.OrderType enum.
        """
        ...

    @property
    def Quantity(self) -> float:
        """Gets or sets the number of units to be ordered (directional)"""
        ...

    @Quantity.setter
    def Quantity(self, value: float):
        """Gets or sets the number of units to be ordered (directional)"""
        ...

    @property
    def LimitPrice(self) -> float:
        """Gets or sets the limit price. Only applies to QuantConnect.Orders.OrderType.Limit and QuantConnect.Orders.OrderType.StopLimit"""
        ...

    @LimitPrice.setter
    def LimitPrice(self, value: float):
        """Gets or sets the limit price. Only applies to QuantConnect.Orders.OrderType.Limit and QuantConnect.Orders.OrderType.StopLimit"""
        ...

    @property
    def StopPrice(self) -> float:
        """Gets or sets the stop price. Only applies to QuantConnect.Orders.OrderType.StopLimit and QuantConnect.Orders.OrderType.StopMarket"""
        ...

    @StopPrice.setter
    def StopPrice(self, value: float):
        """Gets or sets the stop price. Only applies to QuantConnect.Orders.OrderType.StopLimit and QuantConnect.Orders.OrderType.StopMarket"""
        ...

    @property
    def Tag(self) -> str:
        """Gets or sets an arbitrary tag to be attached to the order"""
        ...

    @Tag.setter
    def Tag(self, value: str):
        """Gets or sets an arbitrary tag to be attached to the order"""
        ...

    def Run(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> QuantConnect.Commands.CommandResultPacket:
        """
        Runs this command against the specified algorithm instance
        
        :param algorithm: The algorithm to run this command against
        """
        ...

    def ToString(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class AlgorithmStatusCommand(QuantConnect.Commands.BaseCommand):
    """Represents a command that will change the algorithm's status"""

    @property
    def Status(self) -> int:
        """
        Gets or sets the algorithm status
        
        This property contains the int value of a member of the QuantConnect.AlgorithmStatus enum.
        """
        ...

    @Status.setter
    def Status(self, value: int):
        """
        Gets or sets the algorithm status
        
        This property contains the int value of a member of the QuantConnect.AlgorithmStatus enum.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the AlgorithmStatusCommand"""
        ...

    @overload
    def __init__(self, status: QuantConnect.AlgorithmStatus) -> None:
        """
        Initializes a new instance of the AlgorithmStatusCommand with
        the specified status
        """
        ...

    def Run(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> QuantConnect.Commands.CommandResultPacket:
        """
        Sets the algorithm's status to Status
        
        :param algorithm: The algorithm to run this command against
        """
        ...


class QuitCommand(QuantConnect.Commands.AlgorithmStatusCommand):
    """Represents a command that will terminate the algorithm"""

    def __init__(self) -> None:
        """Initializes a new instance of the QuitCommand"""
        ...


class ICommandHandler(System.IDisposable, metaclass=abc.ABCMeta):
    """
    Represents a command queue for the algorithm. This is an entry point
    for external messages to act upon the running algorithm instance.
    """

    def Initialize(self, job: QuantConnect.Packets.AlgorithmNodePacket, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """
        Initializes this command queue for the specified job
        
        :param job: The job that defines what queue to bind to
        :param algorithm: The algorithm instance
        """
        ...

    def ProcessCommands(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Commands.CommandResultPacket]:
        """
        Process any commands in the queue
        
        :returns: The command result packet of each command executed if any.
        """
        ...


class UpdateOrderCommand(QuantConnect.Commands.BaseCommand):
    """Represents a command to update an order by id"""

    @property
    def OrderId(self) -> int:
        """Gets or sets the id of the order to update"""
        ...

    @OrderId.setter
    def OrderId(self, value: int):
        """Gets or sets the id of the order to update"""
        ...

    @property
    def Quantity(self) -> typing.Optional[float]:
        """Gets or sets the new quantity, specify null to not update the quantity"""
        ...

    @Quantity.setter
    def Quantity(self, value: typing.Optional[float]):
        """Gets or sets the new quantity, specify null to not update the quantity"""
        ...

    @property
    def LimitPrice(self) -> typing.Optional[float]:
        """
        Gets or sets the new limit price, specify null to not update the limit price.
        This will only be used if the order has a limit price (Limit/StopLimit orders)
        """
        ...

    @LimitPrice.setter
    def LimitPrice(self, value: typing.Optional[float]):
        """
        Gets or sets the new limit price, specify null to not update the limit price.
        This will only be used if the order has a limit price (Limit/StopLimit orders)
        """
        ...

    @property
    def StopPrice(self) -> typing.Optional[float]:
        """
        Gets or sets the new stop price, specify null to not update the stop price.
        This will onky be used if the order has a stop price (StopLimit/StopMarket orders)
        """
        ...

    @StopPrice.setter
    def StopPrice(self, value: typing.Optional[float]):
        """
        Gets or sets the new stop price, specify null to not update the stop price.
        This will onky be used if the order has a stop price (StopLimit/StopMarket orders)
        """
        ...

    @property
    def Tag(self) -> str:
        """Gets or sets the new tag for the order, specify null to not update the tag"""
        ...

    @Tag.setter
    def Tag(self, value: str):
        """Gets or sets the new tag for the order, specify null to not update the tag"""
        ...

    def Run(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> QuantConnect.Commands.CommandResultPacket:
        """
        Runs this command against the specified algorithm instance
        
        :param algorithm: The algorithm to run this command against
        """
        ...


class CancelOrderCommand(QuantConnect.Commands.BaseCommand):
    """Represents a command to cancel a specific order by id"""

    class Result(QuantConnect.Commands.CommandResultPacket):
        """Result packet type for the CancelOrderCommand command"""

        @property
        def QuantityFilled(self) -> float:
            """Gets or sets the quantity filled on the cancelled order"""
            ...

        @QuantityFilled.setter
        def QuantityFilled(self, value: float):
            """Gets or sets the quantity filled on the cancelled order"""
            ...

        def __init__(self, command: QuantConnect.Commands.ICommand, success: bool, quantityFilled: float) -> None:
            """Initializes a new instance of the Result class"""
            ...

    @property
    def OrderId(self) -> int:
        """Gets or sets the order id to be cancelled"""
        ...

    @OrderId.setter
    def OrderId(self, value: int):
        """Gets or sets the order id to be cancelled"""
        ...

    def Run(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> QuantConnect.Commands.CommandResultPacket:
        """
        Runs this command against the specified algorithm instance
        
        :param algorithm: The algorithm to run this command against
        """
        ...


class LiquidateCommand(QuantConnect.Commands.BaseCommand):
    """Represents a command that will liquidate the entire algorithm"""

    @property
    def Ticker(self) -> str:
        """Gets or sets the string ticker symbol"""
        ...

    @Ticker.setter
    def Ticker(self, value: str):
        """Gets or sets the string ticker symbol"""
        ...

    @property
    def SecurityType(self) -> int:
        """
        Gets or sets the security type of the ticker.
        
        This property contains the int value of a member of the QuantConnect.SecurityType enum.
        """
        ...

    @SecurityType.setter
    def SecurityType(self, value: int):
        """
        Gets or sets the security type of the ticker.
        
        This property contains the int value of a member of the QuantConnect.SecurityType enum.
        """
        ...

    @property
    def Market(self) -> str:
        """Gets or sets the market the ticker resides in"""
        ...

    @Market.setter
    def Market(self, value: str):
        """Gets or sets the market the ticker resides in"""
        ...

    def Run(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> QuantConnect.Commands.CommandResultPacket:
        """
        Submits orders to liquidate all current holdings in the algorithm
        
        :param algorithm: The algorithm to be liquidated
        """
        ...


class BaseCommandHandler(System.Object, QuantConnect.Commands.ICommandHandler, metaclass=abc.ABCMeta):
    """Base algorithm command handler"""

    @property
    def Algorithm(self) -> QuantConnect.Interfaces.IAlgorithm:
        """
        The algorithm instance
        
        This property is protected.
        """
        ...

    @Algorithm.setter
    def Algorithm(self, value: QuantConnect.Interfaces.IAlgorithm):
        """
        The algorithm instance
        
        This property is protected.
        """
        ...

    def Acknowledge(self, command: QuantConnect.Commands.ICommand, commandResultPacket: QuantConnect.Commands.CommandResultPacket) -> None:
        """
        Acknowledge a command that has been executed
        
        This method is protected.
        
        :param command: The command that was executed
        :param commandResultPacket: The result
        """
        ...

    def Dispose(self) -> None:
        """Disposes of this instance"""
        ...

    def GetCommands(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Commands.ICommand]:
        """
        Get the commands to run
        
        This method is protected.
        """
        ...

    def Initialize(self, job: QuantConnect.Packets.AlgorithmNodePacket, algorithm: QuantConnect.Interfaces.IAlgorithm) -> None:
        """
        Initializes this command queue for the specified job
        
        :param job: The job that defines what queue to bind to
        :param algorithm: The algorithm instance
        """
        ...

    def ProcessCommands(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Commands.CommandResultPacket]:
        """Will consumer and execute any command in the queue"""
        ...


class AddSecurityCommand(QuantConnect.Commands.BaseCommand):
    """Represents a command to add a security to the algorithm"""

    class Result(QuantConnect.Commands.CommandResultPacket):
        """Result packet type for the AddSecurityCommand command"""

        @property
        def Symbol(self) -> QuantConnect.Symbol:
            """The symbol result from the add security command"""
            ...

        @Symbol.setter
        def Symbol(self, value: QuantConnect.Symbol):
            """The symbol result from the add security command"""
            ...

        def __init__(self, command: QuantConnect.Commands.AddSecurityCommand, success: bool, symbol: typing.Union[QuantConnect.Symbol, str]) -> None:
            """Initializes a new instance of the Result class"""
            ...

    @property
    def SecurityType(self) -> int:
        """
        The security type of the security
        
        This property contains the int value of a member of the QuantConnect.SecurityType enum.
        """
        ...

    @SecurityType.setter
    def SecurityType(self, value: int):
        """
        The security type of the security
        
        This property contains the int value of a member of the QuantConnect.SecurityType enum.
        """
        ...

    @property
    def Symbol(self) -> str:
        """The security's ticker symbol"""
        ...

    @Symbol.setter
    def Symbol(self, value: str):
        """The security's ticker symbol"""
        ...

    @property
    def Resolution(self) -> int:
        """
        The requested resolution, defaults to Resolution.Minute
        
        This property contains the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    @Resolution.setter
    def Resolution(self, value: int):
        """
        The requested resolution, defaults to Resolution.Minute
        
        This property contains the int value of a member of the QuantConnect.Resolution enum.
        """
        ...

    @property
    def Market(self) -> str:
        """The security's market, defaults to QuantConnect.Market.USA except for Forex, defaults to QuantConnect.Market.FXCM"""
        ...

    @Market.setter
    def Market(self, value: str):
        """The security's market, defaults to QuantConnect.Market.USA except for Forex, defaults to QuantConnect.Market.FXCM"""
        ...

    @property
    def FillDataForward(self) -> bool:
        """The fill forward behavior, true to fill forward, false otherwise - defaults to true"""
        ...

    @FillDataForward.setter
    def FillDataForward(self, value: bool):
        """The fill forward behavior, true to fill forward, false otherwise - defaults to true"""
        ...

    @property
    def Leverage(self) -> float:
        """The leverage for the security, defaults to 2 for equity, 50 for forex, and 1 for everything else"""
        ...

    @Leverage.setter
    def Leverage(self, value: float):
        """The leverage for the security, defaults to 2 for equity, 50 for forex, and 1 for everything else"""
        ...

    @property
    def ExtendedMarketHours(self) -> bool:
        """The extended market hours flag, true to allow pre/post market data, false for only in market data"""
        ...

    @ExtendedMarketHours.setter
    def ExtendedMarketHours(self, value: bool):
        """The extended market hours flag, true to allow pre/post market data, false for only in market data"""
        ...

    def __init__(self) -> None:
        """Default construct that applies default values"""
        ...

    def Run(self, algorithm: QuantConnect.Interfaces.IAlgorithm) -> QuantConnect.Commands.CommandResultPacket:
        """
        Runs this command against the specified algorithm instance
        
        :param algorithm: The algorithm to run this command against
        """
        ...


class FileCommandHandler(QuantConnect.Commands.BaseCommandHandler):
    """Represents a command handler that sources it's commands from a file on the local disk"""

    def __init__(self) -> None:
        """
        Initializes a new instance of the FileCommandHandler class
        using the 'command-json-file' configuration value for the command json file
        """
        ...

    def Acknowledge(self, command: QuantConnect.Commands.ICommand, commandResultPacket: QuantConnect.Commands.CommandResultPacket) -> None:
        """
        Acknowledge a command that has been executed
        
        This method is protected.
        
        :param command: The command that was executed
        :param commandResultPacket: The result
        """
        ...

    @staticmethod
    def GetCommandFiles() -> System.Collections.Generic.IEnumerable[System.IO.FileInfo]:
        """
        Gets all the available command files
        
        :returns: Sorted enumerator of all the available command files.
        """
        ...

    def GetCommands(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Commands.ICommand]:
        """
        Gets the next command in the queue
        
        This method is protected.
        
        :returns: The next command in the queue, if present, null if no commands present.
        """
        ...


