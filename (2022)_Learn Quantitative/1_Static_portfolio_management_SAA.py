import yfinance as yf
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis
import calculateMaxDD

# STATIC PORTFOLIO STRATEGIES - we buy the stocks in suitable proportions

# =========================================================================================
# THE TRADITIONAL PORTFOLIO OPTIMIZATION METHODS
# =========================================================================================
# =========================================================================================
# DEFINITION MEAN-VARIANCE CRITERION
# =========================================================================================


def MV_criterion(weights, data):
    """
    --------------------------------------------------------------------------
    | Output: optimization portfolio criterion |
    --------------------------------------------------------------------------
    | Inputs: -weight (type ndarray numpy): Weight for portfolio |
    | -data (type ndarray numpy): Returns of stocks |
    --------------------------------------------------------------------------
    """

    # Parameters
    Lambda = 3
    W = 1

    # The risk-free wealth is 1 + the risk-free rate (0.25%)
    Wbar = 1 + 0.25/100

    # Compute portfolio returns
    # Multiply the columns by their coefficient to keep a matrix with shape (n,m)
    portfolio_return = np.multiply(data, np.transpose(weights))
    # Sum all the columns to have the portfolio (shape=(n,1))
    portfolio_return = portfolio_return. sum(axis=1)

    # Compute mean and volatility of the portfolio
    # Compute the mean of the portfolio daily returns (using axis=0 to do on the rows)
    mean = np.mean(portfolio_return, axis=0)

    # Compute the daily volatility of the portfolio (the standard deviation).
    std = np.std(portfolio_return, axis=0)

    # Compute Umv(w) using the previous formula
    criterion = Wbar ** (1 - Lambda) / (1 + Lambda) + Wbar ** (-Lambda) \
        * W * mean - Lambda / 2 * Wbar ** (-1 - Lambda) * W ** 2 * std ** 2

    # Return the opposite of the criterion to minimize it
    criterion = -criterion
    return criterion

    # Once we have a function to minimize (maximize the inverse of U(w)), we need to configure the bounds for the following
    # optimization problem.

    # It means we will maximize the utility under the constraints to use all the capital because the sum of must equal 100%. Therefore, we
    # need to use all our capital. Thus, the bounds for each asset are (0,1). We also need to set a weight for the start of the optimization.
    # Furthermore, we will only perform the optimization on the train set (70% of the data) and analyze the test set's performance (30% of the data)

# =========================================================================================
# DEFINITION MEAN-VARIANCE-SKEWNESS-KURTOSIS CRITERION
# =========================================================================================


def SK_criterion(weights, data):
    """
    --------------------------------------------------------------------------
    | Output: optimization portfolio criterion |
    --------------------------------------------------------------------------
    | Inputs: -weight (type ndarray numpy): Weight for portfolio |
    | -data (type ndarray numpy): Returns of stocks |
    --------------------------------------------------------------------------
    """
    # Parameter
    # Set the parameters of the models ( lambda=3 is a typical risk aversion. The higher the lambda, more you hate the risk)
    Lambda = 3
    W = 1
    Wbar = 1 + 0.25/100

    # Compute portfolio return
    # Multiple each asset by its coefficient and do the sum to have the portfolio return
    portfolio_return = np.multiply(data, np.transpose(weights))
    portfolio_return = portfolio_return. sum(axis=1)

    # Compute mean, volatility, skew, kurtosis of the portfolio
    mean = np.mean(portfolio_return, axis=0)
    std = np.std(portfolio_return, axis=0)

    # Compute the skewness, which calculates the asymmetry of the probability density function
    skewness = skew(portfolio_return, 0)

    # Compute the kurtosis, which represents the "tailedness" of the probability density function
    kurt = kurtosis(portfolio_return, 0)

    # Compute the criterion
    criterion = Wbar ** (1 - Lambda) / (1 + Lambda) + Wbar ** (-Lambda) \
        * W * mean - Lambda / 2 * Wbar ** (-1 - Lambda) * W ** 2 * std ** 2 \
        + Lambda * (Lambda + 1) / (6) * Wbar ** (-2 - Lambda) * W ** 3 * skewness \
        - Lambda * (Lambda + 1) * (Lambda + 2) / (24) * Wbar ** (-3 - Lambda) *\
        W ** 4 * kurt

    # Compute the opposite of the criterion because we will minimize it
    criterion = -criterion
    return criterion

# =========================================================================================
# THE MODERN PORTFOLIO OPTIMIZATION METHODS
# =========================================================================================
# =========================================================================================
# DEFINITION SHARPE CRITERION
# =========================================================================================


def SR_criterion(weight, data):
    """
    --------------------------------------------------------------------------
    | Output: Opposite Sharpe ratio to minimize it. |
    --------------------------------------------------------------------------
    | Inputs: -Weight (type ndarray numpy): Weight for portfolio |
    | -data (type dataframe pandas): Returns of stocks |
    --------------------------------------------------------------------------
    """

    # Compute portfolio returns
    portfolio_return = np.multiply(data, np.transpose(weight))
    portfolio_return = portfolio_return.sum(axis=1)

    # Compute mean, volatility of the portfolio
    mean = np.mean(portfolio_return, axis=0)
    std = np.std(portfolio_return, axis=0)

    # Compute the opposite of the Sharpe ratio
    Sharpe = mean / std
    Sharpe = -Sharpe
    return Sharpe

# =========================================================================================
# DEFINITION SORTINO CRITERION
# =========================================================================================
# The Sortino ratio is an excellent metric because it derives from the
# Sharpe ratio, which only considers downward volatility


def SOR_criterion(weight, data):
    """
    --------------------------------------------------------------------------
    |
    Output: Opposite Sortino ratio to do a minimization |
    --------------------------------------------------------------------------
    | Inputs: -Weight (type ndarray numpy): Wheight for portfolio |
    | -data (type dataframe pandas): Returns of stocks |
    --------------------------------------------------------------------------
    """
    # Compute portfolio returns
    portfolio_return = np.multiply(data, np.transpose(weight))
    portfolio_return = portfolio_return. sum(axis=1)

    # Compute mean, volatility of the portfolio
    # To compute the downward volatility, we take all negative returns and calculate their standard deviation.
    mean = np.mean(portfolio_return, axis=0)
    std = np.std(portfolio_return[portfolio_return < 0], axis=0)

    # Compute the opposite of the Sharpe ratio
    Sortino = mean / std
    Sortino = -Sortino
    return Sortino

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

# Print test data
print(data)

# The variable split is an integer representing the value at 70% of the data. It is a tip to select the train and test sets.
split = int(0.7 * len(data))
train_set = data.iloc[:split, :]
test_set = data.iloc[split:, :]

# Find the number of assets
# n is the number of assets, so we use the command .shape[1] to have the number of columns which is the number of assets.
n = data.shape[1]

# Initialization weight value
# Initialize the value of the weight vector. It is a vector full of one with a shape (n,)
x0 = np.ones(n)

# Optimization constraints problem
# Define the constraints of the optimization. Here, we want the investor to use all its capital. Thus,
# we wish that the sum of the weight equal 100%. (There is absolute value if we wish to short also).
cons = ({'type': 'eq', 'fun': lambda x: sum(abs(x)) - 1})

# Set the bounds
# Define the bound of the optimization. We define the bounds from 0 to 1 because we want a long-only
# strategy. If we create a long-short strategy, bounds will be (-1,1)
Bounds = [(0, 1) for i in range(0, n)]

# Optimization problem solving
# Minimize the opposite of the Umv(w) using the minimize function of scipy
res_MV = sp.optimize.minimize(MV_criterion, x0, method="SLSQP",
                              args=(train_set), bounds=Bounds,
                              constraints=cons, options={'disp': True})

res_SK = sp.optimize.minimize(SK_criterion, x0, method="SLSQP",
                              args=(train_set), bounds=Bounds,
                              constraints=cons, options={'disp': True})

res_SR = sp.optimize.minimize(SR_criterion, x0, method="SLSQP",
                              args=(train_set), bounds=Bounds,
                              constraints=cons, options={'disp': True})

res_SOR = sp.optimize.minimize(SOR_criterion, x0, method="SLSQP",
                               args=(train_set), bounds=Bounds,
                               constraints=cons, options={'disp': True})

# Result for computations
# Extract the optimal weight for our portfolio
X_MV = res_MV.x
X_SK = res_SK.x
X_SR = res_SR.x
X_SOR = res_SOR.x


# Print test result
# we have found the best allocation for this asset
print(f"Allocated portfolio follow mean-variance: {list_tickers[0]} is {X_MV[0]*100} %, {list_tickers[1]} is {X_MV[1]*100} %, {list_tickers[2]} is {X_MV[2]*100} %")
print(f"Allocated portfolio follow mean-variance-skewness-kurtosis: {list_tickers[0]} is {X_SK[0]*100} %, {list_tickers[1]} is {X_SK[1]*100} %, {list_tickers[2]} is {X_SK[2]*100} %")
print(f"Allocated portfolio follow Sharpe ratio: {list_tickers[0]} is {X_SR[0]*100} %, {list_tickers[1]} is {X_SR[1]*100} %, {list_tickers[2]} is {X_SR[2]*100} %")
print(f"Allocated portfolio follow Shotino ratio: {list_tickers[0]} is {X_SOR[0]*100} %, {list_tickers[1]} is {X_SOR[1]*100} %, {list_tickers[2]} is {X_SOR[2]*100} %")

# =========================================================================================
# COMPUTE THE CUMULATIVE RETURN OF THE PORTFOLIO (CM)
# =========================================================================================

# We have multiple columns by his coefficient
# Thus, we always have a shape (n,m) matrix
portfolio_return_MV = np.multiply(test_set, np.transpose(X_MV))
portfolio_return_SK = np.multiply(test_set, np.transpose(X_SK))
portfolio_return_SR = np.multiply(test_set, np.transpose(X_SR))
portfolio_return_SOR = np.multiply(test_set, np.transpose(X_SOR))

# We do the sum of each column to have the portfolio return
portfolio_return_MV = portfolio_return_MV.sum(axis=1)
portfolio_return_SK = portfolio_return_SK.sum(axis=1)
portfolio_return_SR = portfolio_return_SR.sum(axis=1)
portfolio_return_SR = portfolio_return_SOR.sum(axis=1)

maxDD_MV = calculateMaxDD(portfolio_return_MV)
print(
    f"Max DD of mean-variance portfolio {maxDD_MV[0]} start in day {maxDD_MV[2]}")
print(f"Max DD duration of mean-variance portfolio {maxDD_MV[1]} days")

# Plot the CM
# We change the size of the figure to have a better visualization
plt.figure(figsize=(15, 8))

# Print the cumulative sum of the portfolio and put it in percentages
plt.plot(np.cumsum(portfolio_return_MV) * 100,
         color="#035593", linewidth=3)
plt.plot(np.cumsum(portfolio_return_SK) * 100,
         color="#FF6103", linewidth=3)
plt.plot(np.cumsum(portfolio_return_SR) * 100,
         color="#458B00", linewidth=3)
plt.plot(np.cumsum(portfolio_return_SOR) * 100,
         color="#FF1493", linewidth=1)

# Put a name and increase the size of the y-labels
plt.ylabel("Cumulative return %", size=15, fontweight="bold")
plt.xticks(size=15, fontweight="bold")
plt.yticks(size=15, fontweight="bold")
plt.title("Cumulative return of the mean variance portfolio", size=20)

# Put a horizontal line at 0 to highlight this threshold
plt.axhline(0, color="r", linewidth=3)

# plt.axvline(portfolio_return_MV[maxDD_MV[2]], color="r", linewidth=3)
plt.legend(
    ["Mean-variance", "Mean-variance-skweness-kurtosis", "Sharpe", "Sortino"])
plt.xticks(size=15, fontweight="bold")
plt.yticks(size=15, fontweight="bold")
plt.show()
