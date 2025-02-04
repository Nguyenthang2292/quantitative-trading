# Import all the functionality you need to run algorithms
from AlgorithmImports import *

# Define a trading algorithm that is a subclass of QCAlgorithm
class MyAlgorithm(QCAlgorithm):
    # Define an Initialize method.
    # This method is the entry point of your algorithm where you define a series of settings.
    # LEAN only calls this method one time, at the start of your algorithm.
    def Initialize(self) -> None:
        # Set start and end dates
        self.SetStartDate(2018, 1, 1)
        self.SetEndDate(2022, 6, 1)
        # Set the starting cash balance to $100,000 USD
        self.SetCash(100000)
        # Add data for the S&P500 index ETF
        self.AddEquity("SPY")

    # Define an OnData method. 
    # This method receives all the data you subscribe to in discrete time slices.
    # It's where you make trading decisions.
    def OnData(self, slice: Slice) -> None:
        # Allocate 100% of the portfolio to SPY
        if not self.Portfolio.Invested:
            self.SetHoldings("SPY", 1)