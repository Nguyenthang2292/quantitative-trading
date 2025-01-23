from typing import overload
import abc
import datetime
import typing

import QuantConnect.Orders
import QuantConnect.Orders.Fees
import QuantConnect.Securities
import System
import System.Collections.Generic


class OrderFee(System.Object):
    """Defines the result for IFeeModel.GetOrderFee"""

    @property
    def Value(self) -> QuantConnect.Securities.CashAmount:
        """Gets the order fee"""
        ...

    @Value.setter
    def Value(self, value: QuantConnect.Securities.CashAmount):
        """Gets the order fee"""
        ...

    Zero: QuantConnect.Orders.Fees.OrderFee = ...
    """Gets an instance of OrderFee that represents zero."""

    def __init__(self, orderFee: QuantConnect.Securities.CashAmount) -> None:
        """
        Initializes a new instance of the OrderFee class
        
        :param orderFee: The order fee
        """
        ...

    def ApplyToPortfolio(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, fill: QuantConnect.Orders.OrderEvent) -> None:
        """
        Applies the order fee to the given portfolio
        
        :param portfolio: The portfolio instance
        :param fill: The order fill event
        """
        ...

    def ToString(self) -> str:
        """This is for backward compatibility with old 'decimal' order fee"""
        ...


class ModifiedFillQuantityOrderFee(QuantConnect.Orders.Fees.OrderFee):
    """
    An order fee where the fee quantity has already been subtracted from the filled quantity so instead we subtracted
    from the quote currency when applied to the portfolio
    """

    def __init__(self, orderFee: QuantConnect.Securities.CashAmount, quoteCurrency: str, contractMultiplier: float) -> None:
        """
        Initializes a new instance of the ModifiedFillQuantityOrderFee class
        
        :param orderFee: The order fee
        :param quoteCurrency: The associated security quote currency
        :param contractMultiplier: The associated security contract multiplier
        """
        ...

    def ApplyToPortfolio(self, portfolio: QuantConnect.Securities.SecurityPortfolioManager, fill: QuantConnect.Orders.OrderEvent) -> None:
        """
        Applies the order fee to the given portfolio
        
        :param portfolio: The portfolio instance
        :param fill: The order fill event
        """
        ...


class OrderFeeParameters(System.Object):
    """Defines the parameters for IFeeModel.GetOrderFee"""

    @property
    def Security(self) -> QuantConnect.Securities.Security:
        """Gets the security"""
        ...

    @property
    def Order(self) -> QuantConnect.Orders.Order:
        """Gets the order"""
        ...

    def __init__(self, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> None:
        """
        Initializes a new instance of the OrderFeeParameters class
        
        :param security: The security
        :param order: The order
        """
        ...


class IFeeModel(metaclass=abc.ABCMeta):
    """Represents a model the simulates order fees"""

    def GetOrderFee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee associated with the specified order.
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in a CashAmount instance.
        """
        ...


class FeeModel(System.Object, QuantConnect.Orders.Fees.IFeeModel):
    """Base class for any order fee model"""

    def GetOrderFee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee associated with the specified order.
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in a CashAmount instance.
        """
        ...


class AlphaStreamsFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an implementation of FeeModel that models order fees that alpha stream clients pay/receive"""

    def GetOrderFee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee associated with the specified order. This returns the cost
        of the transaction in the account currency
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in units of the account currency.
        """
        ...


class IndiaFeeModel(System.Object, QuantConnect.Orders.Fees.IFeeModel):
    """Provides the default implementation of IFeeModel Refer to https://www.samco.in/technology/brokerage_calculator"""

    @property
    def BrokerageMultiplier(self) -> float:
        """
        Brokerage calculation Factor
        
        This property is protected.
        """
        ...

    @BrokerageMultiplier.setter
    def BrokerageMultiplier(self, value: float):
        """
        Brokerage calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def MaxBrokerage(self) -> float:
        """
        Maximum brokerage per order
        
        This property is protected.
        """
        ...

    @MaxBrokerage.setter
    def MaxBrokerage(self, value: float):
        """
        Maximum brokerage per order
        
        This property is protected.
        """
        ...

    @property
    def SecuritiesTransactionTaxTotalMultiplier(self) -> float:
        """
        Securities Transaction Tax calculation Factor
        
        This property is protected.
        """
        ...

    @SecuritiesTransactionTaxTotalMultiplier.setter
    def SecuritiesTransactionTaxTotalMultiplier(self, value: float):
        """
        Securities Transaction Tax calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def ExchangeTransactionChargeMultiplier(self) -> float:
        """
        Exchange Transaction Charge calculation Factor
        
        This property is protected.
        """
        ...

    @ExchangeTransactionChargeMultiplier.setter
    def ExchangeTransactionChargeMultiplier(self, value: float):
        """
        Exchange Transaction Charge calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def StateTaxMultiplier(self) -> float:
        """
        State Tax calculation Factor
        
        This property is protected.
        """
        ...

    @StateTaxMultiplier.setter
    def StateTaxMultiplier(self, value: float):
        """
        State Tax calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def SebiChargesMultiplier(self) -> float:
        """
        Sebi Charges calculation Factor
        
        This property is protected.
        """
        ...

    @SebiChargesMultiplier.setter
    def SebiChargesMultiplier(self, value: float):
        """
        Sebi Charges calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def StampChargesMultiplier(self) -> float:
        """
        Stamp Charges calculation Factor
        
        This property is protected.
        """
        ...

    @StampChargesMultiplier.setter
    def StampChargesMultiplier(self, value: float):
        """
        Stamp Charges calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def IsStampChargesFromOrderValue(self) -> bool:
        """
        Checks if Stamp Charges is calculated from order valur or turnover
        
        This property is protected.
        """
        ...

    @IsStampChargesFromOrderValue.setter
    def IsStampChargesFromOrderValue(self, value: bool):
        """
        Checks if Stamp Charges is calculated from order valur or turnover
        
        This property is protected.
        """
        ...

    def GetOrderFee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee associated with the specified order.
        
        :param parameters: A OrderFeeParameters object containing the security and order
        """
        ...


class ZerodhaFeeModel(QuantConnect.Orders.Fees.IndiaFeeModel):
    """Provides the default implementation of IFeeModel Refer to https://www.samco.in/technology/brokerage_calculator"""

    @property
    def BrokerageMultiplier(self) -> float:
        """
        Brokerage calculation Factor
        
        This property is protected.
        """
        ...

    @BrokerageMultiplier.setter
    def BrokerageMultiplier(self, value: float):
        """
        Brokerage calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def MaxBrokerage(self) -> float:
        """
        Maximum brokerage per order
        
        This property is protected.
        """
        ...

    @MaxBrokerage.setter
    def MaxBrokerage(self, value: float):
        """
        Maximum brokerage per order
        
        This property is protected.
        """
        ...

    @property
    def SecuritiesTransactionTaxTotalMultiplier(self) -> float:
        """
        Securities Transaction Tax calculation Factor
        
        This property is protected.
        """
        ...

    @SecuritiesTransactionTaxTotalMultiplier.setter
    def SecuritiesTransactionTaxTotalMultiplier(self, value: float):
        """
        Securities Transaction Tax calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def ExchangeTransactionChargeMultiplier(self) -> float:
        """
        Exchange Transaction Charge calculation Factor
        
        This property is protected.
        """
        ...

    @ExchangeTransactionChargeMultiplier.setter
    def ExchangeTransactionChargeMultiplier(self, value: float):
        """
        Exchange Transaction Charge calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def StateTaxMultiplier(self) -> float:
        """
        State Tax calculation Factor
        
        This property is protected.
        """
        ...

    @StateTaxMultiplier.setter
    def StateTaxMultiplier(self, value: float):
        """
        State Tax calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def SebiChargesMultiplier(self) -> float:
        """
        Sebi Charges calculation Factor
        
        This property is protected.
        """
        ...

    @SebiChargesMultiplier.setter
    def SebiChargesMultiplier(self, value: float):
        """
        Sebi Charges calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def StampChargesMultiplier(self) -> float:
        """
        Stamp Charges calculation Factor
        
        This property is protected.
        """
        ...

    @StampChargesMultiplier.setter
    def StampChargesMultiplier(self, value: float):
        """
        Stamp Charges calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def IsStampChargesFromOrderValue(self) -> bool:
        """
        Checks if Stamp Charges is calculated from order valur or turnover
        
        This property is protected.
        """
        ...

    @IsStampChargesFromOrderValue.setter
    def IsStampChargesFromOrderValue(self, value: bool):
        """
        Checks if Stamp Charges is calculated from order valur or turnover
        
        This property is protected.
        """
        ...


class AtreyuFeeModel(System.Object, QuantConnect.Orders.Fees.IFeeModel):
    """Provides an implementation of FeeModel that models Atreyu order fees"""

    def __init__(self, feesPerShare: typing.Optional[float] = None) -> None:
        """
        Creates a new instance
        
        :param feesPerShare: The fees per share to apply
        """
        ...

    def GetOrderFee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in quote currency
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in quote currency.
        """
        ...


class ExanteFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """
    Provides an implementation of FeeModel that models Exante order fees.
    According to:
    https://support.exante.eu/hc/en-us/articles/115005873143-Fees-overview-exchange-imposed-fees?source=searchhttps://exante.eu/markets/
    """

    MarketUsaRate: float = 0.02

    DefaultRate: float = 0.02

    def __init__(self, forexCommissionRate: float = 0.25) -> None:
        """
        Creates a new instance
        
        :param forexCommissionRate: Commission rate for FX operations
        """
        ...

    def GetOrderFee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee associated with the specified order.
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in a CashAmount instance.
        """
        ...


class WolverineFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an implementation of FeeModel that models Wolverine order fees"""

    def __init__(self, feesPerShare: typing.Optional[float] = None) -> None:
        """
        Creates a new instance
        
        :param feesPerShare: The fees per share to apply
        """
        ...

    def GetOrderFee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in quote currency
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in quote currency.
        """
        ...


class KrakenFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an implementation of FeeModel that models Kraken order fees"""

    MakerTier1CryptoFee: float = 0.0016
    """
    We don't use 30 day model, so using only tier1 fees.
    https://www.kraken.com/features/fee-schedule#kraken-pro
    """

    TakerTier1CryptoFee: float = 0.0026
    """
    We don't use 30 day model, so using only tier1 fees.
    https://www.kraken.com/features/fee-schedule#kraken-pro
    """

    Tier1FxFee: float = 0.002
    """
    We don't use 30 day model, so using only tier1 fees.
    https://www.kraken.com/features/fee-schedule#stablecoin-fx-pairs
    """

    @property
    def FxStablecoinList(self) -> System.Collections.Generic.List[str]:
        """Fiats and stablecoins list that have own fee."""
        ...

    def GetOrderFee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order.
        If sell - fees in base currency
        If buy - fees in quote currency
        It can be defined manually in KrakenOrderProperties
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The fee of the order.
        """
        ...


class BitfinexFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an implementation of FeeModel that models Bitfinex order fees"""

    MakerFee: float = 0.001
    """
    Tier 1 maker fees
    Maker fees are paid when you add liquidity to our order book by placing a limit order under the ticker price for buy and above the ticker price for sell.
    https://www.bitfinex.com/fees
    """

    TakerFee: float = 0.002
    """
    Tier 1 taker fees
    Taker fees are paid when you remove liquidity from our order book by placing any order that is executed against an order of the order book.
    Note: If you place a hidden order, you will always pay the taker fee. If you place a limit order that hits a hidden order, you will always pay the maker fee.
    https://www.bitfinex.com/fees
    """

    def GetOrderFee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in quote currency
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in quote currency.
        """
        ...


class GDAXFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an implementation of FeeModel that models GDAX order fees"""

    @staticmethod
    def GetFeePercentage(utcTime: typing.Union[datetime.datetime, datetime.date], isMaker: bool, isStableCoin: bool) -> float:
        """
        Returns the maker/taker fee percentage effective at the requested date.
        
        :param utcTime: The date/time requested (UTC)
        :param isMaker: true if the maker percentage fee is requested, false otherwise
        :param isStableCoin: true if the order security symbol is a StableCoin, false otherwise
        :returns: The fee percentage effective at the requested date.
        """
        ...

    def GetOrderFee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in quote currency
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in quote currency.
        """
        ...


class ConstantFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an order fee model that always returns the same order fee."""

    def __init__(self, fee: float, currency: str = "USD") -> None:
        """
        Initializes a new instance of the ConstantFeeModel class with the specified
        
        :param fee: The constant order fee used by the model
        :param currency: The currency of the order fee
        """
        ...

    def GetOrderFee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Returns the constant fee for the model in units of the account currency
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in units of the account currency.
        """
        ...


class FxcmFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an implementation of FeeModel that models FXCM order fees"""

    def __init__(self, currency: str = "USD") -> None:
        """
        Creates a new instance
        
        :param currency: The currency of the order fee, for FXCM this is the account currency
        """
        ...

    def GetOrderFee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in units of the account currency
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in units of the account currency.
        """
        ...


class FTXFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """
    Provides an implementation of FeeModel that models FTX order fees
    https://help.ftx.com/hc/en-us/articles/360024479432-Fees
    """

    @property
    def MakerFee(self) -> float:
        """Tier 1 maker fees"""
        ...

    @property
    def TakerFee(self) -> float:
        """Tier 1 taker fees"""
        ...

    def GetOrderFee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in quote currency
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in quote currency.
        """
        ...


class FTXUSFeeModel(QuantConnect.Orders.Fees.FTXFeeModel):
    """
    Provides an implementation of FeeModel that models FTX order fees
    https://help.ftx.us/hc/en-us/articles/360043579273-Fees
    """

    @property
    def MakerFee(self) -> float:
        """Tier 1 maker fees"""
        ...

    @property
    def TakerFee(self) -> float:
        """Tier 1 taker fees"""
        ...


class FeeModelExtensions(System.Object):
    """
    Provide extension method for IFeeModel to enable
    backwards compatibility of invocations.
    """

    @staticmethod
    def GetOrderFee(model: QuantConnect.Orders.Fees.IFeeModel, security: QuantConnect.Securities.Security, order: QuantConnect.Orders.Order) -> float:
        """
        Gets the order fee associated with the specified order. This returns the cost
        of the transaction in the account currency
        
        :param model: The fee model
        :param security: The security matching the order
        :param order: The order to compute fees for
        :returns: The cost of the order in units of the account currency.
        """
        ...


class InteractiveBrokersFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides the default implementation of IFeeModel"""

    def __init__(self, monthlyForexTradeAmountInUSDollars: float = 0, monthlyOptionsTradeAmountInContracts: float = 0) -> None:
        """
        Initializes a new instance of the ImmediateFillModel
        
        :param monthlyForexTradeAmountInUSDollars: Monthly FX dollar volume traded
        :param monthlyOptionsTradeAmountInContracts: Monthly options contracts traded
        """
        ...

    def GetOrderFee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Gets the order fee associated with the specified order. This returns the cost
        of the transaction in the account currency
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in units of the account currency.
        """
        ...


class BinanceFeeModel(QuantConnect.Orders.Fees.FeeModel):
    """Provides an implementation of FeeModel that models Binance order fees"""

    MakerTier1Fee: float = 0.001
    """
    Tier 1 maker fees
    https://www.binance.com/en/fee/schedule
    """

    TakerTier1Fee: float = 0.001
    """
    Tier 1 taker fees
    https://www.binance.com/en/fee/schedule
    """

    def __init__(self, mFee: float = ..., tFee: float = ...) -> None:
        """
        Creates Binance fee model setting fees values
        
        :param mFee: Maker fee value
        :param tFee: Taker fee value
        """
        ...

    def GetOrderFee(self, parameters: QuantConnect.Orders.Fees.OrderFeeParameters) -> QuantConnect.Orders.Fees.OrderFee:
        """
        Get the fee for this order in quote currency
        
        :param parameters: A OrderFeeParameters object containing the security and order
        :returns: The cost of the order in quote currency.
        """
        ...


class SamcoFeeModel(QuantConnect.Orders.Fees.IndiaFeeModel):
    """Provides the default implementation of IFeeModel Refer to https://www.samco.in/technology/brokerage_calculator"""

    @property
    def BrokerageMultiplier(self) -> float:
        """
        Brokerage calculation Factor
        
        This property is protected.
        """
        ...

    @BrokerageMultiplier.setter
    def BrokerageMultiplier(self, value: float):
        """
        Brokerage calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def MaxBrokerage(self) -> float:
        """
        Maximum brokerage per order
        
        This property is protected.
        """
        ...

    @MaxBrokerage.setter
    def MaxBrokerage(self, value: float):
        """
        Maximum brokerage per order
        
        This property is protected.
        """
        ...

    @property
    def SecuritiesTransactionTaxTotalMultiplier(self) -> float:
        """
        Securities Transaction Tax calculation Factor
        
        This property is protected.
        """
        ...

    @SecuritiesTransactionTaxTotalMultiplier.setter
    def SecuritiesTransactionTaxTotalMultiplier(self, value: float):
        """
        Securities Transaction Tax calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def ExchangeTransactionChargeMultiplier(self) -> float:
        """
        Exchange Transaction Charge calculation Factor
        
        This property is protected.
        """
        ...

    @ExchangeTransactionChargeMultiplier.setter
    def ExchangeTransactionChargeMultiplier(self, value: float):
        """
        Exchange Transaction Charge calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def StateTaxMultiplier(self) -> float:
        """
        State Tax calculation Factor
        
        This property is protected.
        """
        ...

    @StateTaxMultiplier.setter
    def StateTaxMultiplier(self, value: float):
        """
        State Tax calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def SebiChargesMultiplier(self) -> float:
        """
        Sebi Charges calculation Factor
        
        This property is protected.
        """
        ...

    @SebiChargesMultiplier.setter
    def SebiChargesMultiplier(self, value: float):
        """
        Sebi Charges calculation Factor
        
        This property is protected.
        """
        ...

    @property
    def StampChargesMultiplier(self) -> float:
        """
        Stamp Charges calculation Factor
        
        This property is protected.
        """
        ...

    @StampChargesMultiplier.setter
    def StampChargesMultiplier(self, value: float):
        """
        Stamp Charges calculation Factor
        
        This property is protected.
        """
        ...


