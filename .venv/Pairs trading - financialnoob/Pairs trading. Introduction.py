## 1. Pairs trading. Introduction.
## From pair trading - financial noob

import numpy as np
import matplotlib.pyplot as plt

### First we generate stocks price time series. 
## We will generate two price series, P_a and P_b, that are cointegrated. 
## We will use a random walk process to generate the stock price series. 
## The stock price series will be generated as follows:
# generate random walk process
np.random.seed(112)
F = [50]
for i in range(252):
    F.append(F[i] + np.random.randn())
F = np.array(F)

# generate price series
P_a = F + np.random.randn(len(F))
P_b = F + np.random.randn(len(F))

Now let's plot the prices that we generated.