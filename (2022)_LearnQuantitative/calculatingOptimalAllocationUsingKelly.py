# Calculating the Optimal Allocation Using Kelly formula
import numpy as np
import pandas as pd
from numpy.linalg import inv
df1 = pd.read_excel('OIH.xls')
df2 = pd.read_excel('RKH.xls')
df = pd.merge(df1, df2, on='Date', suffixes=('_OIH', '_RKH'))
df.set_index('Date', inplace=True)
df3 = pd.read_excel('RTH.xls')
df = pd.merge(df, df3, on='Date')
df.rename(columns={"Adj Close": "Adj Close_RTH"},
          inplace=True)
df.set_index('Date', inplace=True)
df.sort_index(inplace=True)
dailyret = df.loc[:, ('Adj Close_OIH', 'Adj Close_RKH',
                      'Adj Close_RTH')].pct_change()
dailyret.rename(columns={"Adj Close_OIH": "OIH",
                         "Adj Close_RKH": "RKH", "Adj Close_RTH": "RTH"},
                inplace=True)
# Risk free rate = 0.04 and 252 trading day
excessRet = dailyret-0.04/252
M = 252*excessRet.mean()
C = 252*excessRet.cov()
F = np.dot(inv(C), M)
S = np.sqrt(np.dot(F.T, np.dot(C, F)))
