from typing import overload
import abc
import datetime
import typing

import QuantConnect
import QuantConnect.Util.RateLimit
import System


class IRefillStrategy(metaclass=abc.ABCMeta):
    """Provides a strategy for making tokens available for consumption in the ITokenBucket"""

    def Refill(self) -> int:
        """Computes the number of new tokens made available, typically via the passing of time."""
        ...


class ISleepStrategy(metaclass=abc.ABCMeta):
    """
    Defines a strategy for sleeping the current thread of execution. This is currently used via the
    ITokenBucket.Consume in order to wait for new tokens to become available for consumption.
    """

    def Sleep(self) -> None:
        """
        Sleeps the current thread in an implementation specific way
        and for an implementation specific amount of time
        """
        ...


class BusyWaitSleepStrategy(System.Object, QuantConnect.Util.RateLimit.ISleepStrategy):
    """
    Provides a CPU intensive means of waiting for more tokens to be available in ITokenBucket.
    This strategy is only viable when the requested number of tokens is expected to become available in an
    extremely short period of time. This implementation aims to keep the current thread executing to prevent
    potential content switches arising from a thread yielding or sleeping strategy.
    """

    def Sleep(self) -> None:
        """Provides a CPU intensive sleep by executing Thread.SpinWait for a single spin."""
        ...


class ITokenBucket(metaclass=abc.ABCMeta):
    """
    Defines a token bucket for rate limiting
    See: https://en.wikipedia.org/wiki/Token_bucket
    """

    @property
    @abc.abstractmethod
    def Capacity(self) -> int:
        """Gets the maximum capacity of tokens this bucket can hold."""
        ...

    @property
    @abc.abstractmethod
    def AvailableTokens(self) -> int:
        """Gets the total number of currently available tokens for consumption"""
        ...

    def Consume(self, tokens: int, timeout: int = ...) -> None:
        """
        Blocks until the specified number of tokens are available for consumption
        and then consumes that number of tokens.
        
        :param tokens: The number of tokens to consume
        :param timeout: The maximum amount of time, in milliseconds, to block. A TimeoutException is throw in the event it takes longer than the stated timeout to consume the requested number of tokens. The default timeout is set to infinite, which will block forever.
        """
        ...

    def TryConsume(self, tokens: int) -> bool:
        """
        Attempts to consume the specified number of tokens from the bucket. If the
        requested number of tokens are not immediately available, then this method
        will return false to indicate that zero tokens have been consumed.
        """
        ...


class LeakyBucket(System.Object, QuantConnect.Util.RateLimit.ITokenBucket):
    """
    Provides an implementation of ITokenBucket that implements the leaky bucket algorithm
    See: https://en.wikipedia.org/wiki/Leaky_bucket
    """

    @property
    def Capacity(self) -> int:
        """Gets the maximum capacity of tokens this bucket can hold."""
        ...

    @property
    def AvailableTokens(self) -> int:
        """Gets the total number of currently available tokens for consumption"""
        ...

    @overload
    def __init__(self, capacity: int, refillAmount: int, refillInterval: datetime.timedelta) -> None:
        """
        Initializes a new instance of the LeakyBucket class.
        This constructor initializes the bucket using the ThreadSleepStrategy.Sleep with a 1 millisecond
        sleep to prevent being CPU intensive and uses the FixedIntervalRefillStrategy to refill bucket
        tokens according to the  and  parameters.
        
        :param capacity: The maximum number of tokens this bucket can hold
        :param refillAmount: The number of tokens to add to the bucket each
        :param refillInterval: The interval which after passing more tokens are added to the bucket
        """
        ...

    @overload
    def __init__(self, capacity: int, sleep: QuantConnect.Util.RateLimit.ISleepStrategy, refill: QuantConnect.Util.RateLimit.IRefillStrategy, timeProvider: QuantConnect.ITimeProvider = None) -> None:
        """
        Initializes a new instance of the LeakyBucket class
        
        :param capacity: The maximum number of tokens this bucket can hold
        :param sleep: Defines the ISleepStrategy used when Consume is invoked but the bucket does not have enough tokens yet
        :param refill: Defines the IRefillStrategy that computes how many tokens to add back to the bucket each time consumption is attempted
        :param timeProvider: Defines the ITimeProvider used to enforce timeouts when invoking Consume
        """
        ...

    def Consume(self, tokens: int, timeout: int = ...) -> None:
        """
        Blocks until the specified number of tokens are available for consumption
        and then consumes that number of tokens.
        
        :param tokens: The number of tokens to consume
        :param timeout: The maximum amount of time, in milliseconds, to block. An exception is throw in the event it takes longer than the stated timeout to consume the requested number of tokens
        """
        ...

    def TryConsume(self, tokens: int) -> bool:
        """
        Attempts to consume the specified number of tokens from the bucket. If the
        requested number of tokens are not immediately available, then this method
        will return false to indicate that zero tokens have been consumed.
        """
        ...


class TokenBucket(System.Object):
    """
    Provides extension methods for interacting with ITokenBucket instances as well
    as access to the NullTokenBucket via TokenBucket.Null
    """

    Null: QuantConnect.Util.RateLimit.ITokenBucket = ...
    """Gets an ITokenBucket that always permits consumption"""

    @staticmethod
    def Consume(bucket: QuantConnect.Util.RateLimit.ITokenBucket, tokens: int, timeout: datetime.timedelta) -> None:
        """Provides an overload of ITokenBucket.Consume that accepts a TimeSpan timeout"""
        ...


class ThreadSleepStrategy(System.Object, QuantConnect.Util.RateLimit.ISleepStrategy):
    """
    Provides a CPU non-intensive means of waiting for more tokens to be available in ITokenBucket.
    This strategy should be the most commonly used as it either sleeps or yields the currently executing thread,
    allowing for other threads to execute while the current thread is blocked and waiting for new tokens to become
    available in the bucket for consumption.
    """

    Yielding: QuantConnect.Util.RateLimit.ISleepStrategy = ...
    """Gets an instance of ISleepStrategy that yields the current thread"""

    def __init__(self, milliseconds: int) -> None:
        """
        Initializes a new instance of the ThreadSleepStrategy using the specified
        number of  for each Sleep invocation.
        
        :param milliseconds: The duration of time to sleep, in milliseconds
        """
        ...

    def Sleep(self) -> None:
        """Sleeps the current thread using the initialized number of milliseconds"""
        ...

    @staticmethod
    def Sleeping(milliseconds: int) -> QuantConnect.Util.RateLimit.ISleepStrategy:
        """
        Gets an instance of ISleepStrategy that sleeps the current thread for
        the specified number of milliseconds
        
        :param milliseconds: The duration of time to sleep, in milliseconds
        """
        ...


class FixedIntervalRefillStrategy(System.Object, QuantConnect.Util.RateLimit.IRefillStrategy):
    """
    Provides a refill strategy that has a constant, quantized refill rate.
    For example, after 1 minute passes add 5 units. If 59 seconds has passed, it will add zero unit,
    but if 2 minutes have passed, then 10 units would be added.
    """

    def __init__(self, timeProvider: QuantConnect.ITimeProvider, refillAmount: int, refillInterval: datetime.timedelta) -> None:
        """
        Initializes a new instance of the FixedIntervalRefillStrategy class.
        
        :param timeProvider: Provides the current time used for determining how much time has elapsed between invocations of the refill method
        :param refillAmount: Defines the constant number of tokens to be made available for consumption each time the provided  has passed
        :param refillInterval: The amount of time that must pass before adding the specified  back to the bucket
        """
        ...

    def Refill(self) -> int:
        """
        Computes the number of new tokens made available to the bucket for consumption by determining the
        number of time intervals that have passed and multiplying by the number of tokens to refill for
        each time interval.
        """
        ...


