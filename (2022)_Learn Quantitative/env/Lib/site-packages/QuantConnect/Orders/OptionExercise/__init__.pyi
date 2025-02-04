from typing import overload
import abc

import QuantConnect.Orders
import QuantConnect.Orders.OptionExercise
import QuantConnect.Securities.Option
import System
import System.Collections.Generic


class IOptionExerciseModel(metaclass=abc.ABCMeta):
    """Represents a model that simulates option exercise and lapse events"""

    def OptionExercise(self, option: QuantConnect.Securities.Option.Option, order: QuantConnect.Orders.OptionExerciseOrder) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.OrderEvent]:
        """
        Model the option exercise
        
        :param option: Option we're trading this order
        :param order: Order to update
        :returns: Order fill information detailing the average price and quantity filled.
        """
        ...


class DefaultExerciseModel(System.Object, QuantConnect.Orders.OptionExercise.IOptionExerciseModel):
    """Represents the default option exercise model (physical, cash settlement)"""

    def OptionExercise(self, option: QuantConnect.Securities.Option.Option, order: QuantConnect.Orders.OptionExerciseOrder) -> System.Collections.Generic.IEnumerable[QuantConnect.Orders.OrderEvent]:
        """
        Default option exercise model for the basic equity/index option security class.
        
        :param option: Option we're trading this order
        :param order: Order to update
        """
        ...


