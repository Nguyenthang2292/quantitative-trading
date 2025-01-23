from typing import overload
import abc
import typing

import QuantConnect
import QuantConnect.Securities
import QuantConnect.Securities.CurrencyConversion
import System
import System.Collections.Generic


class ICurrencyConversion(metaclass=abc.ABCMeta):
    """Represents a type capable of calculating the conversion rate between two currencies"""

    @property
    @abc.abstractmethod
    def SourceCurrency(self) -> str:
        """The currency this conversion converts from"""
        ...

    @property
    @abc.abstractmethod
    def DestinationCurrency(self) -> str:
        """The currency this conversion converts to"""
        ...

    @property
    @abc.abstractmethod
    def ConversionRate(self) -> float:
        """The current conversion rate between SourceCurrency and DestinationCurrency"""
        ...

    @property
    @abc.abstractmethod
    def ConversionRateSecurities(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Security]:
        """The securities which the conversion rate is based on"""
        ...

    def Update(self) -> float:
        """
        Updates the internal conversion rate based on the latest data, and returns the new conversion rate
        
        :returns: The new conversion rate.
        """
        ...


class SecurityCurrencyConversion(System.Object, QuantConnect.Securities.CurrencyConversion.ICurrencyConversion):
    """Provides an implementation of ICurrencyConversion to find and use multi-leg currency conversions"""

    @property
    def SourceCurrency(self) -> str:
        """The currency this conversion converts from"""
        ...

    @property
    def DestinationCurrency(self) -> str:
        """The currency this conversion converts to"""
        ...

    @property
    def ConversionRate(self) -> float:
        """The current conversion rate"""
        ...

    @ConversionRate.setter
    def ConversionRate(self, value: float):
        """The current conversion rate"""
        ...

    @property
    def ConversionRateSecurities(self) -> System.Collections.Generic.IEnumerable[QuantConnect.Securities.Security]:
        """The securities which the conversion rate is based on"""
        ...

    @staticmethod
    def LinearSearch(sourceCurrency: str, destinationCurrency: str, existingSecurities: System.Collections.Generic.IList[QuantConnect.Securities.Security], potentialSymbols: System.Collections.Generic.IEnumerable[QuantConnect.Symbol], makeNewSecurity: typing.Callable[[QuantConnect.Symbol], QuantConnect.Securities.Security]) -> QuantConnect.Securities.CurrencyConversion.SecurityCurrencyConversion:
        """
        Finds a conversion between two currencies by looking through all available 1 and 2-leg options
        
        :param sourceCurrency: The currency to convert from
        :param destinationCurrency: The currency to convert to
        :param existingSecurities: The securities which are already added to the algorithm
        :param potentialSymbols: The symbols to consider, may overlap with existingSecurities
        :param makeNewSecurity: The function to call when a symbol becomes part of the conversion, must return the security that will provide price data about the symbol
        :returns: A new SecurityCurrencyConversion instance representing the conversion from sourceCurrency to destinationCurrency.
        """
        ...

    def Update(self) -> float:
        """
        Updates the internal conversion rate based on the latest data, and returns the new conversion rate
        
        :returns: The new conversion rate.
        """
        ...


