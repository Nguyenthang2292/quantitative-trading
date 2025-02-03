import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from enum import Enum
import plotly.graph_objects as go


# ---------------------------------------------
# 1) Định nghĩa các HẰNG SỐ, ENUM
# ---------------------------------------------

class Leg(Enum):
    BEARISH_LEG = 0
    BULLISH_LEG = 1

class Bias(Enum):
    BEARISH = -1
    BULLISH = 1

# (Màu sắc - tuỳ vào matplotlib, ta có thể dùng 'r', 'g', v.v. hoặc mã hex)
COLOR_BULLISH = "green"
COLOR_BEARISH = "red"

# Chế độ hiển thị (ví dụ, Historical/PRESENT), ta demo 1 biến cứng
MODE = "Historical"  # Hoặc "Present"

# ---------------------------------------------
# 2) Cấu trúc dữ liệu chuyển từ 'type' Pine Script
# ---------------------------------------------

@dataclass
class Alerts:
    """Các cờ (flag) cho alert, ta có thể thêm dần."""
    swingBullishBOS: bool = False
    swingBearishBOS: bool = False
    swingBullishCHoCH: bool = False
    swingBearishCHoCH: bool = False
    # ... có thể bổ sung Internal BOS/CHoCH, OB breakout, FVG, etc.

@dataclass
class Pivot:
    """Đại diện cho 1 pivot (swing)"""
    currentLevel: float = np.nan
    lastLevel: float = np.nan
    crossed: bool = False  # Giá đã vượt pivot chưa
    barIndex: int = 0      # index của thanh pivot
    time: pd.Timestamp = None

@dataclass
class Trend:
    """Đại diện cho xu hướng (bias)"""
    bias: Bias = Bias.BULLISH  # hoặc Bias.BEARISH

# ---------------------------------------------
# 3) Hàm tiện ích
# ---------------------------------------------

def identify_leg(highs, lows, idx, lookback=5):
    """
    Xác định leg ở vị trí idx, dựa vào lookback nến trước.
    """
    if idx - lookback < 0 or idx >= len(highs):
        print(f"❌ Lỗi: idx ({idx}) vượt quá phạm vi của highs (size={len(highs)})")
        return None

    segment_highs = highs.iloc[idx-lookback : idx+1]
    segment_lows  = lows.iloc[idx-lookback : idx+1]

    if segment_highs.empty or segment_lows.empty:
        print(f"⚠️ Cảnh báo: segment_highs hoặc segment_lows rỗng tại idx={idx}")
        return None

    local_max = segment_highs.max() if not segment_highs.empty else np.nan
    local_min = segment_lows.min() if not segment_lows.empty else np.nan

    print(f"🔎 DEBUG - Index {idx}: highs[idx]={highs.iloc[idx]}, local_max={local_max}")

    # Sửa đổi điều kiện để nhận diện leg tốt hơn
    is_bearish_leg = (highs.iloc[idx] >= local_max) and (highs.iloc[idx-1] < local_max)
    is_bullish_leg = (lows.iloc[idx] <= local_min) and (lows.iloc[idx-1] > local_min)

    print(f"  🔹 is_bearish_leg: {is_bearish_leg}, is_bullish_leg: {is_bullish_leg}")

    if is_bearish_leg:
        print("  ✅ Bearish Leg detected!")
        return Leg.BEARISH_LEG
    elif is_bullish_leg:
        print("  ✅ Bullish Leg detected!")
        return Leg.BULLISH_LEG

    print("  ❌ No leg detected.")
    return None


def detect_swing_structure(data, lookback=5):
    """
    Hàm chính để duyệt qua DataFrame, xác định pivot & BOS/CHoCH ở cấp swing
    (rất giản lược).
    """
    # Các pivot "cao" / "thấp" (chúng ta giả lập)
    swingHigh = Pivot()
    swingLow  = Pivot()
    # Xu hướng swing
    swingTrend = Trend(bias=Bias.BULLISH)  # giả định ban đầu

    # List để ghi lại đánh dấu BOS/CHoCH
    bos_choch_marks = []  # (index, price, text, color)

    # Alerts
    currentAlerts = Alerts()

    # DataFrame: data.index => mốc thời gian, cột: [Open, High, Low, Close, ...]
    highs = data["High"]
    lows  = data["Low"]
    close = data["Close"]

    # Leg cũ
    prev_leg = None

    for i in range(len(data)):
        # 1) Xác định leg
        curr_leg = identify_leg(highs, lows, i, lookback=lookback)

        # 2) Kiểm tra xem có "start of new leg" không (giả lập logic "startOfNewLeg")
        if curr_leg is not None and prev_leg != curr_leg:
            # => pivot thay đổi
            if curr_leg == Leg.BULLISH_LEG:
                # pivot Low mới
                swingLow.lastLevel = swingLow.currentLevel
                swingLow.currentLevel = lows[i]
                swingLow.crossed = False
                swingLow.barIndex = i
                swingLow.time = data.index[i]
            elif curr_leg == Leg.BEARISH_LEG:
                # pivot High mới
                swingHigh.lastLevel = swingHigh.currentLevel
                swingHigh.currentLevel = highs[i]
                swingHigh.crossed = False
                swingHigh.barIndex = i
                swingHigh.time = data.index[i]

            prev_leg = curr_leg

        # 3) Kiểm tra breakout pivot => BOS / CHoCH
        #    Giả sử khi close > pivotHigh => bullish BOS/CHoCH
        #    Hoặc close < pivotLow => bearish BOS/CHoCH
        #    Từ Pine Script: if ta.crossover(close, pivotHigh.currentLevel) ...
        #    Mình mô phỏng:
        
        # Kiểm tra pivot High
        if not swingHigh.crossed and not np.isnan(swingHigh.currentLevel):
            if close[i] > swingHigh.currentLevel:
                # => breakout pivot high
                # Xem đây là BOS hay CHoCH
                if swingTrend.bias == Bias.BEARISH:
                    # => CHoCH
                    currentAlerts.swingBullishCHoCH = True
                    mark_text = "CHoCH ↑"
                else:
                    # => BOS
                    currentAlerts.swingBullishBOS = True
                    mark_text = "BOS ↑"
                # Cập nhật trend
                swingTrend.bias = Bias.BULLISH
                swingHigh.crossed = True

                bos_choch_marks.append((i, swingHigh.currentLevel, mark_text, COLOR_BULLISH))

        # Kiểm tra pivot Low
        if not swingLow.crossed and not np.isnan(swingLow.currentLevel):
            if close[i] < swingLow.currentLevel:
                # => breakout pivot low
                if swingTrend.bias == Bias.BULLISH:
                    currentAlerts.swingBearishCHoCH = True
                    mark_text = "CHoCH ↓"
                else:
                    currentAlerts.swingBearishBOS = True
                    mark_text = "BOS ↓"

                swingTrend.bias = Bias.BEARISH
                swingLow.crossed = True

                bos_choch_marks.append((i, swingLow.currentLevel, mark_text, COLOR_BEARISH))

    # Trả về list đánh dấu, và Alert “có gì xảy ra không”
    return bos_choch_marks, currentAlerts

# ---------------------------------------------
# 4) Hàm main: Lấy dữ liệu từ yfinance, xử lý, vẽ
# ---------------------------------------------

def main():
    #Tải dữ liệu AAPL từ 2014-01-01 đến hiện tại
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

    # Đặt lại index về cột Date
    df_filtered.set_index("Date", inplace=True)
    #===========================================================================
    # Phát hiện structure SMC (BOS, CHoCH) trên data
    bos_choch_marks, alerts = detect_swing_structure(df_filtered, lookback=5)


    # ------------------------------------------------
    # Vẽ biểu đồ nến + đánh dấu BOS/CHoCH
    # ------------------------------------------------
    # Tạo Figure
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
    xaxis_rangeslider_visible=False,
    template="plotly_dark"
    )

    # Vẽ các điểm BOS/CHoCH
    for (i, price, text, color) in bos_choch_marks:
        fig.add_trace(go.Scatter(
            x=[df_filtered.index[i]],
            y=[price],
            mode="markers+text",
            marker=dict(color=color, size=10),
            text=[text],
            textposition="top center"
        ))

    # Cập nhật tiêu đề và nhãn
    fig.update_layout(
        title="SMC (BOS/CHoCH) demo trên AAPL - khung Daily",
        xaxis_title="Thời gian",
        yaxis_title="Giá (USD)",
        showlegend=True
    )

    # Hiển thị biểu đồ
    fig.show()

    # In ra alert cuối cùng
    print("Alerts cuối cùng:", alerts)

# ---------------------------------------------
# 5) Chạy hàm main
# ---------------------------------------------
if __name__ == "__main__":
    main()
