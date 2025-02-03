import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go

def main():
    #Tải dữ liệu AAPL từ 2014-01-01 đến hiện tại
    df = yf.download("AAPL", start="2014-01-01", end=None, interval="1d")
    if df.empty:
        print("Không tải được dữ liệu AAPL từ yfinance.")
        return
    
    # Tạo Figure
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df["Open"].squeeze(),
        high=df["High"].squeeze(),
        low=df["Low"].squeeze(),
        close=df["Close"].squeeze(),
        name="AAPL Candlestick"
    ))
    
    fig.update_layout(
    title="Fake AAPL Candlestick Chart (Simulated Data)",
    xaxis_title="Date",
    yaxis_title="Price (USD)",
    xaxis_rangeslider_visible=False,
    template="plotly_dark"
    )
    
    # Hiển thị biểu đồ
    fig.show()

    # In ra alert cuối cùng
    print("Alerts cuối cùng:")

if __name__ == '__main__':
    main()