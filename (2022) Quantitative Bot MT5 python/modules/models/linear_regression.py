import pandas as pd
import pandas_ta
import plotly.graph_objects as go
import plotly.express as px
import os
from pathlib import Path
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt, mpld3
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split

# Prepare for data
df = pd.read_csv(f'{Path(os.getcwd()).parent.parent.absolute()}/data/AUDCAD_H1_2022-1-1_2022-5-5.csv')
df.set_index(pd.DatetimeIndex(df['datetime']), inplace=True)
df = df[['close']]

print(df)

# Add EMA to dataframe by appending
# Note: pandas_ta integrates seamlessly into
# our existing dataframe
df.ta.ema(close='close', length=10, append=True)

# Drop the first n-rows
df = df.iloc[10:]
# View our newly-formed dataset
print(df.head(10))

# Plot the chart
fig = go.Figure([go.Scatter(y=df['close'], name = 'Close price')])
fig.add_trace(go.Scatter(y=df['EMA_10'], name = 'EMA'))
# fig.show()

# Split data into testing and training sets
# Việc sử dụng 80% dữ liệu để train và 20% còn lại để test là cách làm phổ biến. 
# Sự phân chia 80/20 này là cách tiếp cận phổ biến nhất nhưng cũng có thể sử dụng các cách tiếp cận công thức hơn (Guyon, 1997)
X_train, X_test, y_train, y_test = train_test_split(df[['close']], df[['EMA_10']], test_size=.2)

# Create Regression Model
model = LinearRegression()
# Train the model
model.fit(X_train, y_train)
# Use model to make predictions
# Sử dụng tham số X_test cho mô hình Linear Regression để dự đoán kết quả y_predict sau đó so sánh kết quả y_predict và y_test
y_predict = model.predict(X_test)

# In kết quả ra
print('====================================')
print(y_predict)

# Printout relevant metrics
print("Model Coefficients:", model.coef_)
print("Mean Absolute Error:", mean_absolute_error(y_test, y_predict))
print("Mean Square Error:", mean_squared_error(y_test, y_predict))
print("Coefficient of Determination:", r2_score(y_test, y_predict))

model_2 = sm.OLS(y_train['EMA_10'], X_train['close'])
result = model_2.fit()
print(result.summary())

# Use the Autocorrelation function from the statsmodel library passing our DataFrame object in as the data
# https://www.alpharithms.com/autocorrelation-time-series-python-432909/
# Note: Limiting Lags to 50
# plot_acf(df)
# Show the AR as a plot
# mpld3.show()



