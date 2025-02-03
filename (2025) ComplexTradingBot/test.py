import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from dataclasses import dataclass
from enum import Enum

# ---------------------------------------------
# 1) Định nghĩa các HẰNG SỐ, ENUM
# ---------------------------------------------

class Leg(Enum):
    BEARISH_LEG = 0
    BULLISH_LEG = 1

class Bias(Enum):
    BEARISH = -1
    BULLISH = 1

COLOR_BULLISH = "green"
COLOR_BEARISH = "red"

# ---------------------------------------------
# 2) Cấu trúc dữ liệu
# ---------------------------------------------

@dataclass
class Alerts:
    swingBullishBOS: bool = False
    swingBearishBOS: bool = False
    swingBullishCHoCH: bool = False
    swingBearishCHoCH: bool = False

@dataclass
class Pivot:
    currentLevel: float = np.nan
    lastLevel: float = np.nan
    crossed: bool = False
    barIndex: int = 0
    time: pd.Timestamp = None

@dataclass
class Trend:
    bias: Bias = Bias.BULLISH

# ---------------------------------------------
# 3) Hàm tiện ích
# ---------------------------------------------

def identify_leg(highs, lows, idx, lookback=5):
    if idx - lookback < 0 or idx >= len(highs):
        return None
    
    segment_highs = highs.iloc[idx-lookback : idx+1]
    segment_lows  = lows.iloc[idx-lookback : idx+1]
    
    if segment_highs.empty or segment_lows.empty:
        return None

    local_max = segment_highs.max()
    local_min = segment_lows.min()
    
    is_bearish_leg = (highs.iloc[idx] >= local_max) and (highs.iloc[idx-1] < local_max)
    is_bullish_leg = (lows.iloc[idx] <= local_min) and (lows.iloc[idx-1] > local_min)
    
    if is_bearish_leg:
        return Leg.BEARISH_LEG
    elif is_bullish_leg:
        return Leg.BULLISH_LEG
    return None

def detect_swing_structure(data, lookback=5):
    swingHigh = Pivot()
    swingLow  = Pivot()
    swingTrend = Trend(bias=Bias.BULLISH)
    bos_choch_marks = []
    bos_lines = []
    choch_lines = []
    currentAlerts = Alerts()

    highs = data["High"]
    lows  = data["Low"]
    close = data["Close"]
    prev_leg = None

    for i in range(len(data)):
        curr_leg = identify_leg(highs, lows, i, lookback=lookback)
        
        if curr_leg is not None and prev_leg != curr_leg:
            if curr_leg == Leg.BULLISH_LEG:
                swingLow.lastLevel = swingLow.currentLevel
                swingLow.currentLevel = lows[i]
                swingLow.crossed = False
                swingLow.barIndex = i
                swingLow.time = data.index[i]
            elif curr_leg == Leg.BEARISH_LEG:
                swingHigh.lastLevel = swingHigh.currentLevel
                swingHigh.currentLevel = highs[i]
                swingHigh.crossed = False
                swingHigh.barIndex = i
                swingHigh.time = data.index[i]
            prev_leg = curr_leg

        if not swingHigh.crossed and not np.isnan(swingHigh.currentLevel):
            if close[i] > swingHigh.currentLevel:
                if swingTrend.bias == Bias.BEARISH:
                    currentAlerts.swingBullishCHoCH = True
                    mark_text = "CHoCH ↑"
                    choch_lines.append((swingHigh.barIndex, i, swingHigh.currentLevel))
                else:
                    currentAlerts.swingBullishBOS = True
                    mark_text = "BOS ↑"
                    bos_lines.append((swingHigh.barIndex, i, swingHigh.currentLevel))
                swingTrend.bias = Bias.BULLISH
                swingHigh.crossed = True
                bos_choch_marks.append((i, swingHigh.currentLevel, mark_text, COLOR_BULLISH))

        if not swingLow.crossed and not np.isnan(swingLow.currentLevel):
            if close[i] < swingLow.currentLevel:
                if swingTrend.bias == Bias.BULLISH:
                    currentAlerts.swingBearishCHoCH = True
                    mark_text = "CHoCH ↓"
                    choch_lines.append((swingLow.barIndex, i, swingLow.currentLevel))
                else:
                    currentAlerts.swingBearishBOS = True
                    mark_text = "BOS ↓"
                    bos_lines.append((swingLow.barIndex, i, swingLow.currentLevel))
                swingTrend.bias = Bias.BEARISH
                swingLow.crossed = True
                bos_choch_marks.append((i, swingLow.currentLevel, mark_text, COLOR_BEARISH))

    return bos_choch_marks, bos_lines, choch_lines, currentAlerts

# ---------------------------------------------
# 4) Hàm main
# ---------------------------------------------

def main():
    df = yf.download("AAPL", start="2014-01-01", end=None, interval="1d")
    if df.empty:
        print("Không tải được dữ liệu AAPL từ yfinance.")
        return

    df_filtered = pd.DataFrame({
    "Date": df.index,  # Lấy index làm cột Date
    "Open": df["Open"].squeeze(),
    "High": df["High"].squeeze(),
    "Low": df["Low"].squeeze(),
    "Close": df["Close"].squeeze()
    })

    bos_choch_marks, bos_lines, choch_lines, alerts = detect_swing_structure(df_filtered, lookback=5)

    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=df_filtered.index,
        open=df_filtered["Open"],
        high=df_filtered["High"],
        low=df_filtered["Low"],
        close=df_filtered["Close"],
        name="AAPL Candlestick"
    ))
    
    fig.update_layout(
        title="AAPL Candlestick Chart (Simulated Data)",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        xaxis_rangeslider_visible=True,
        template="plotly_white",
        dragmode="pan"
    )

    for (i, price, text, color) in bos_choch_marks:
        if i < len(df_filtered):
            fig.add_trace(go.Scatter(
                x=[df_filtered.index[i]],
                y=[price],
                mode="markers+text",
                marker=dict(color=color, size=10),
                text=[text],
                textposition="top center"
            ))
    
    for start, end, level in bos_lines:
        fig.add_trace(go.Scatter(
            x=[df_filtered.index[start], df_filtered.index[end]],
            y=[level, level],
            mode="lines",
            line=dict(color="green", width=2, dash="dash"),
            name="BOS"
        ))
    
    for start, end, level in choch_lines:
        fig.add_trace(go.Scatter(
            x=[df_filtered.index[start], df_filtered.index[end]],
            y=[level, level],
            mode="lines",
            line=dict(color="red", width=2, dash="dot"),
            name="CHoCH"
        ))

    fig.show()
    print("Alerts cuối cùng:", alerts)

if __name__ == "__main__":
    main()
