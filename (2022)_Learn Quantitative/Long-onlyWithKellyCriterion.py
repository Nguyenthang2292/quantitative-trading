import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta


def calcKelly(mean, std, r):
    return (mean - r) / std**2


def getKellyFactor(returns: pd.Series, r=0.01,
                   max_leverage=None, periods=252, rolling=True):
    # risk free rate is 0.01 and 252 days in trading
    '''
    Calculates the Kelly Factor for each time step based
    on the parameters provided.
    '''
    if rolling:
        std = returns.rolling(periods).std()
        mean = returns.rolling(periods).mean()
    else:
        std = returns.expanding(periods).std()
        mean = returns.expanding(periods).mean()

    r_daily = np.log((1 + r) ** (1 / 252))
    kelly_factor = calcKelly(mean, std, r_daily)

    # No shorts
    kelly_factor = np.where(kelly_factor < 0, 0, kelly_factor)
    if max_leverage is not None:
        kelly_factor = np.where(kelly_factor > max_leverage,
                                max_leverage, kelly_factor)

    return kelly_factor


def LongOnlyKellyStrategy(data, r=0.02, max_leverage=None, periods=252,
                          rolling=True):
    data['returns'] = data['Close'] / data['Close'].shift(1)
    data['log_returns'] = np.log(data['returns'])
    data['kelly_factor'] = getKellyFactor(data['log_returns'],
                                          r, max_leverage, periods, rolling)
    cash = np.zeros(data.shape[0])
    equity = np.zeros(data.shape[0])
    portfolio = cash.copy()
    portfolio[0] = 1
    cash[0] = 1
    for i, _row in enumerate(data.iterrows()):
        row = _row[1]
        if np.isnan(row['kelly_factor']):
            portfolio[i] += portfolio[i-1]
            cash[i] += cash[i-1]
            continue

        portfolio[i] += cash[i-1] * \
            (1 + r)**(1/252) + equity[i-1] * row['returns']
        equity[i] += portfolio[i] * row['kelly_factor']
        cash[i] += portfolio[i] * (1 - row['kelly_factor'])

    data['cash'] = cash
    data['equity'] = equity
    data['portfolio'] = portfolio
    data['strat_returns'] = data['portfolio'] / data['portfolio'].shift(1)
    data['strat_log_returns'] = np.log(data['strat_returns'])
    data['strat_cum_returns'] = data['strat_log_returns'].cumsum()
    data['cum_returns'] = data['log_returns'].cumsum()

    return data


the_day_before_now = datetime.now() - timedelta(days=1)
print("date and time =", the_day_before_now.strftime("%Y-%m-%d"))

ticker = 'SPY'
yfObj = yf.Ticker(ticker)
data = yfObj.history(start='1993-01-01', end=the_day_before_now)
# Drop unused columns
data.drop(['Open', 'High', 'Low', 'Volume', 'Dividends',
           'Stock Splits'], axis=1, inplace=True)
