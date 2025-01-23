# TACTICAL ASSET ALLOCATION - we can also bet on the decrease of the stock, and it is called short selling

# MOMENTUM FACTOR
# At the beginning of a tactical asset allocation, we must choose a
# momentum factor. It is a value that we can build on the strategy

# We must understand that the momentum factor can be whatever we want. For example, we can create momentum using the interest rate
# growth, the country's inflation, the percentage of return over the last 12 months, etc.

# We set a vector factor λ for this part to do all the necessary transformations. When we have this factor, we usually create a z-score,
# the normalization of the factor. We will put the formula of a z-score to highlight the process.

# REBALANCING
# The rebalancing of a TAA is an essential thing. Indeed, at this moment that the weights of each asset in the portfolio are determined.
# In the following examples, we will use allocation with the same weights for all assets to make things easier. The dynamic of the
# strategy will be only the sign (positive if we long and negative if we short).

# equation: portfolio =  α* SAA + (1 - α)* TAA (α ∈ [0,1])

# =========================================================================================
# MOVING AVERAGE STRATEGY
# =========================================================================================

# This subsection will compute some moving averages to create the momentum factor in the second part
# The moving average is the easiest to understand technical indicator. Indeed, it is a mean, but
# instead of doing the average on all the samples, we will create a vector of a mean of the n last day for each selected day

import yfinance as yf
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# =========================================================================================
# PREPARE DATA SET
# =========================================================================================

# Importation of data from yfinance library
list_tickers = ["META", "NFLX", "TSLA"]
database = yf.download(list_tickers)

# Take only the adjusted close stock price
database = database["Adj Close"]

# Drop missing values
data = database.dropna().pct_change(1).dropna()

# Create SMA15 for data set
# data["SMA15 META"] = data["META"].rolling(15).mean().shift(1)
# data["SMA15 NFLX"] = data["NFLX"].rolling(15).mean().shift(1)
# data["SMA15 TSLA"] = data["TSLA"].rolling(15).mean().shift(1)

# Print test data
print(data)

# We do a loop to create the SMAs for each asset
for col in list_tickers:
    data[f"pct {col}"] = data[col].pct_change(1)
    data[f"SMA3 {col}"] = data[col].rolling(3).mean().shift(1)
    data[f"SMA12 {col}"] = data[col].rolling(12).mean().shift(1)
    data[f"Momentum factor {col}"] = data[f"SMA3 {col}"] - data[f"SMA12 {col}"]

# Normalizing the zscore
# We will use 70% of the data to create the strategy. Then, we will test it on the test
# set (the other 30%). The difference between the previous chapter and this one is that we keep 
# the price in absolute value and not in variations
split = int(0.7 * len(data))
train_set = data.iloc[:split, :]
test_set = data.iloc[split:, :]

# Find the mean and std vectors
columns = [f"Momentum factor {col}" for col in list_tickers]
train_set_mean = train_set[columns].mean()
train_set_std = train_set[columns].std()

# Create the zscores
# formular: Z = (x - μ)/σ
# (Z: standard score, x: observed value, μ: mean of the sample, σ: standard deviation of the sample)
# Computation of the test set z-scores using the train set's mean and std to avoid interference in
# the data. Usually, we cannot know the mean and std of this set because it is the future.
train_set[columns] = (train_set[columns]-train_set_mean) / train_set_std
test_set[columns] = (test_set[columns]-train_set_mean) / train_set_std

# Find the medians
median = train_set[columns].median()

# =========================================================================================
# BUILD THE STRATEGY
# =========================================================================================

# the median of the z-score is inferior to the z-score month. In that case, we take a short
# position the next month, and if the median of the z score is superior, we take a long position on the asset
# Compute the signals and the profits
# Loop to compute the signal and profit for each asset
for i in range(len(columns)):

    # Initialize a new column for the signal
    test_set[f"signal {columns[i]}"] = 0

    # Signal is -1 if factor < median
    test_set.loc[test_set[f"{columns[i]}"] <
                 median[i], f"signal {columns[i]}"] = -1

    # Signal is 1 if factor > median
    test_set.loc[test_set[f"{columns[i]}"] >
                 median[i], f"signal {columns[i]}"] = 1

    # Compute the profit
    test_set[f"profit {columns[i]}"] = (test_set[f"signal {columns[i]}"].shift(1)) * test_set[f"pct {list_tickers[i]}"]

# portfolio_return = np.multiply(test_set)
# portfolio_return = portfolio_return.sum(axis=1)

# plt.figure(figsize=(15, 8))
# plt.plot(np.cumsum(portfolio_return) * 100,
#          color="#035593", linewidth=3)

# # Put a name and increase the size of the y-labels
# plt.ylabel("Cumulative return %", size=15, fontweight="bold")
# plt.xticks(size=15, fontweight="bold")
# plt.yticks(size=15, fontweight="bold")
# plt.title("Cumulative return of the mean variance portfolio", size=20)

# # Put a horizontal line at 0 to highlight this threshold
# plt.axhline(0, color="r", linewidth=3)
# plt.show()
