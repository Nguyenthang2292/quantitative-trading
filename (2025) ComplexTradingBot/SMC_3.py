import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from enum import Enum
import plotly.graph_objects as go
from dataclasses import dataclass
from typing import List, Optional

# Danh sách lưu trữ các đối tượng vẽ trên biểu đồ
fig = go.Figure()

# 📌 Định nghĩa màu sắc
GREEN = "#089981"
RED = "#F23645"
BLUE = "#2157f3"
GRAY = "#878b94"
MONO_BULLISH = "#b2b5be"
MONO_BEARISH = "#5d606b"

# 📌 Định nghĩa kiểu đường nét
SOLID = "⎯⎯⎯"
DASHED = "----"
DOTTED = "····"

# 📌 Constants (định nghĩa giá trị Bearish/Bullish Leg)
BULLISH_LEG = 1
BEARISH_LEG = 0

# 📌 Cấu hình chung
config = {
    "mode": "Historical",
    "style": "Colored",
    "show_trend": False
}

# 📌 Cấu hình Internal Structure
internal_structure = {
    "show_internals": True,
    "bullish_structure": "All",
    "bullish_color": GREEN,
    "bearish_structure": "All",
    "bearish_color": RED,
    "internal_filter_confluence": False,
    "label_size": "tiny"
}

# 📌 Cấu hình Swing Structure
swing_structure = {
    "show_structure": True,
    "bullish_structure": "All",
    "bullish_color": GREEN,
    "bearish_structure": "All",
    "bearish_color": RED,
    "swing_label_size": "small",
    "show_swings": False,
    "swings_length": 50,
    "show_high_low_swings": True
}

# 📌 Cấu hình Order Blocks
order_blocks = {
    "show_internal_order_blocks": True,
    "internal_order_blocks_size": 5,
    "show_swing_order_blocks": False,
    "swing_order_blocks_size": 5,
    "order_block_filter": "Atr",
    "order_block_mitigation": "High/Low",
    "internal_bullish_color": "#3179f5",
    "internal_bearish_color": "#f77c80",
    "swing_bullish_color": "#1848cc",
    "swing_bearish_color": "#b22833"
}

# 📌 Cấu hình Equal Highs/Lows
equal_highs_lows = {
    "show": True,
    "length": 3,
    "threshold": 0.1,
    "label_size": "tiny"
}

# 📌 Cấu hình Fair Value Gaps
fair_value_gaps = {
    "show": False,
    "auto_threshold": True,
    "timeframe": "",
    "bullish_color": "#00ff68",
    "bearish_color": "#ff0008",
    "extend_bars": 1
}

# 📌 Cấu hình Highs & Lows MTF
highs_lows_mtf = {
    "show_daily": False,
    "daily_style": SOLID,
    "daily_color": BLUE,
    "show_weekly": False,
    "weekly_style": SOLID,
    "weekly_color": BLUE,
    "show_monthly": False,
    "monthly_style": SOLID,
    "monthly_color": BLUE
}

# 📌 Cấu hình Premium & Discount Zones
premium_discount_zones = {
    "show": False,
    "premium_zone_color": RED,
    "equilibrium_zone_color": GRAY,
    "discount_zone_color": GREEN
}

# 📌 Tổng hợp tất cả cấu hình vào dictionary chính
settings = {
    "config": config,
    "internal_structure": internal_structure,
    "swing_structure": swing_structure,
    "order_blocks": order_blocks,
    "equal_highs_lows": equal_highs_lows,
    "fair_value_gaps": fair_value_gaps,
    "highs_lows_mtf": highs_lows_mtf,
    "premium_discount_zones": premium_discount_zones
}

# 📌 Định nghĩa cấu trúc cực trị (Trailing Extremes)
@dataclass
class TrailingExtremes:
    top: Optional[float] = None
    bottom: Optional[float] = None
    barTime: Optional[int] = None
    barIndex: Optional[int] = None
    lastTopTime: Optional[int] = None
    lastBottomTime: Optional[int] = None

# 📌 Định nghĩa Fair Value Gap
@dataclass
class FairValueGap:
    top: float
    bottom: float
    bias: int  # BULLISH (+1) hoặc BEARISH (-1)
    topBox: Optional[object] = None
    bottomBox: Optional[object] = None

# 📌 Định nghĩa xu hướng (Trend)
@dataclass
class Trend:
    bias: int  # BULLISH (+1) hoặc BEARISH (-1)

# 📌 Định nghĩa Pivot Point (Swing Point)
@dataclass
class Pivot:
    currentLevel: Optional[float] = None
    lastLevel: Optional[float] = None
    crossed: bool = False
    barTime: Optional[int] = None
    barIndex: Optional[int] = None

# 📌 Định nghĩa Order Block
@dataclass
class OrderBlock:
    barHigh: float
    barLow: float
    barTime: int
    bias: int  # BULLISH (+1) hoặc BEARISH (-1)

# 📌 Định nghĩa cấu trúc Equal Display để lưu label và line
@dataclass
class EqualDisplay:
    line: Optional[object] = None
    label: Optional[object] = None
    
# 📌 Biến toàn cục
swingHigh = Pivot()
swingLow = Pivot()
internalHigh = Pivot()
internalLow = Pivot()
equalHigh = Pivot()
equalLow = Pivot()
swingTrend = Trend(0)
internalTrend = Trend(0)
equalHighDisplay = EqualDisplay()
equalLowDisplay = EqualDisplay()

equalHighsLowsThresholdInput = 0.1  
showSwingsInput = True  
internalFilterConfluenceInput = False  
fairValueGapsThresholdInput = 0.05  
showSwingOrderBlocksInput = True  
showInternalOrderBlocksInput = True  
swingOrderBlocksSizeInput = 5 
fairValueGapsExtendInput = 1 

# 📌 Danh sách chứa dữ liệu
fairValueGaps: List[FairValueGap] = []
parsedHighs: List[float] = []
parsedLows: List[float] = []
highs: List[float] = []
lows: List[float] = []
times: List[int] = []
trailing = TrailingExtremes()
swingOrderBlocks: List[OrderBlock] = []
internalOrderBlocks: List[OrderBlock] = []
swingOrderBlocksBoxes: List[object] = []  # Giả định hộp giá trị sẽ được hiển thị bằng thư viện khác
internalOrderBlocksBoxes: List[object] = []

# 📌 Chỉ số thanh hiện tại
currentBarIndex = 0
lastBarIndex = 0

# 📌 Thời gian ban đầu của biểu đồ
initialTime = 0 

# 📌 Thiết lập nguồn dữ liệu cho Order Block Mitigation
orderBlockMitigationInput = "High/Low"
CLOSE = "Close"
HIGH = "High"
LOW = "Low" 

bearishOrderBlockMitigationSource = HIGH if orderBlockMitigationInput == CLOSE else HIGH
bullishOrderBlockMitigationSource = LOW if orderBlockMitigationInput == CLOSE else LOW

def compute_atr(highs, lows, closes, period=200):
    """
    Tính Average True Range (ATR)
    :param highs: Mảng giá cao
    :param lows: Mảng giá thấp
    :param closes: Mảng giá đóng cửa
    :param period: Số chu kỳ ATR
    :return: Giá trị ATR mới nhất hoặc None nếu không đủ dữ liệu
    """
    # Kiểm tra đầu vào
    if len(highs) != len(lows) or len(highs) != len(closes):
        raise ValueError("Lengths of highs, lows, and closes must be the same.")

    if len(highs) < period:
        print(f"Not enough data to compute ATR for period={period}.")
        return None

    tr = np.maximum(
        highs[:-1] - lows[:-1],
        np.maximum(
            np.abs(highs[:-1] - closes[:-1]),
            np.abs(lows[:-1] - closes[:-1])
        )
    )

    # Tính ATR bằng numpy (SMA)
    if len(tr) < period:
        print(f"Not enough data to compute ATR for period={period}. At least {period} data points are required.")
        return None
    atr = np.mean(tr[-period:])
    return atr if not np.isnan(atr) else None

# Khởi tạo các biến cần thiết
atrMeasure = compute_atr(np.array(highs), np.array(lows), np.array(closes), 200) if len(highs) > 0 else 0

ATR = "Atr"
RANGE = "Cumulative Mean Range"

orderBlockFilterInput = ATR
volatilityMeasure = (
    compute_atr(np.array(highs), np.array(lows), np.array(highs), 200)
    if orderBlockFilterInput == ATR
    else np.cumsum(np.abs(np.array(highs) - np.array(lows))) / max(1, currentBarIndex + 1)
)

# 📌 Xác định thanh có độ biến động cao
def is_high_volatility_bar(high, low, volatilityMeasure):
    return (high - low) >= (2 * volatilityMeasure)

# 📌 Lấy giá cao/thấp đã xử lý
highVolatilityBar = is_high_volatility_bar(1.2, 1.0, volatilityMeasure)  # Ví dụ
parsedHigh = 1.0 if highVolatilityBar else 1.2
parsedLow = 1.2 if highVolatilityBar else 1.0

# 📌 Lưu trữ dữ liệu mới vào danh sách
parsedHighs.append(parsedHigh)
parsedLows.append(parsedLow)
highs.append(1.2)  # Dữ liệu giả lập
lows.append(1.0)
times.append(100)  # Cần lấy từ dữ liệu thực tế

# 📌 Hàm kiểm tra có phải điểm bắt đầu của leg mới hay không
def start_of_new_leg(leg_values):
    """
    Xác định xem có phải điểm bắt đầu của leg mới không
    
    :param leg_values: (list) Danh sách các giá trị leg
    :return: (bool) True nếu có thay đổi leg
    """
    if len(leg_values) < 2:
        print("⚠️ Lỗi: Không đủ dữ liệu để xác định leg mới.")
        return False  # Không có đủ dữ liệu để so sánh
    
    return leg_values[-1] != leg_values[-2]

# 📌 Hàm kiểm tra có phải điểm bắt đầu của Bearish Leg (Swing Down)
def start_of_bearish_leg(leg_values):
    """
    Xác định xem có phải điểm bắt đầu của một bearish leg không
    
    :param leg_values: (list) Danh sách các giá trị leg
    :return: (bool) True nếu có sự thay đổi từ bullish → bearish
    """
    if len(leg_values) < 2:
        print("⚠️ Lỗi: Không đủ dữ liệu để xác định leg mới.")
        return False
    
    return (leg_values[-2] == BULLISH_LEG) and (leg_values[-1] == BEARISH_LEG)

# 📌 Hàm kiểm tra có phải điểm bắt đầu của Bullish Leg (Swing Up)
def start_of_bullish_leg(leg_values):
    """
    Xác định xem có phải điểm bắt đầu của một bullish leg không
    
    :param leg_values: (list) Danh sách các giá trị leg
    :return: (bool) True nếu có sự thay đổi từ bearish → bullish
    """
    if len(leg_values) < 2:
        print("⚠️ Lỗi: Không đủ dữ liệu để xác định leg mới.")
        return False
    
    return (leg_values[-2] == BEARISH_LEG) and (leg_values[-1] == BULLISH_LEG)

def draw_label(label_time, label_price, tag, label_color, label_style, mode="Present", text_size=12, x_offset=0, y_offset=0):
    """
    Vẽ một nhãn trên biểu đồ bằng Plotly.

    :param label_time: (int) Thời gian trên trục X.
    :param label_price: (float) Giá trên trục Y.
    :param tag: (str) Nội dung nhãn.
    :param label_color: (str) Màu sắc nhãn.
    :param label_style: (str) Kiểu nhãn ("label_up" hoặc "label_down").
    :param mode: (str) Chế độ hiển thị ("Historical" hoặc "Present").
    :param text_size: (int) Kích thước chữ (default: 12).
    :param x_offset: (int) Độ lệch X của nhãn.
    :param y_offset: (int) Độ lệch Y của nhãn.
    """

    # Nếu ở chế độ "Present", xóa nhãn cũ trước khi vẽ
    if mode == "Present":
        fig.data = []  # Xóa tất cả dữ liệu cũ

    fig.add_trace(go.Scatter(
        x=[label_time + x_offset],
        y=[label_price + y_offset],
        mode="text",
        text=tag,
        textposition="top center" if label_style == "label_up" else "bottom center",
        textfont=dict(color=label_color, size=text_size)
    ))

def draw_equal_high_low(pivot, level, size, equal_high, mode="Present", line_width=1, line_dash="dot", text_size=12):
    """
    Vẽ Equal High (EQH) hoặc Equal Low (EQL) bằng Plotly.

    :param pivot: (Pivot) Điểm pivot để vẽ đường.
    :param level: (float) Giá trị của EQH/EQL.
    :param size: (int) Độ dài khoảng cách từ pivot.
    :param equal_high: (bool) True nếu là EQH, False nếu là EQL.
    :param mode: (str) Chế độ hiển thị ("Historical" hoặc "Present").
    :param line_width: (int) Độ dày của đường (default: 1).
    :param line_dash: (str) Kiểu đường ("dot", "dash", "solid").
    :param text_size: (int) Kích thước chữ của nhãn (default: 12).
    """

    tag = "EQH" if equal_high else "EQL"
    color = "#F23645" if equal_high else "#089981"  # Màu swingBearishColor hoặc swingBullishColor
    label_style = "label_down" if equal_high else "label_up"

    # Nếu ở chế độ "Present", xóa line & label cũ
    if mode == "Present":
        fig.data = []  # Xóa tất cả dữ liệu cũ

    # Vẽ đường Equal High/Low
    fig.add_trace(go.Scatter(
        x=[pivot.barTime, times[size]],
        y=[pivot.currentLevel, level],
        mode="lines",
        line=dict(color=color, width=line_width, dash=line_dash),
        name=tag
    ))

    # Vẽ nhãn EQH/EQL
    draw_label(times[size], level, tag, color, label_style, text_size=text_size)

# 📌 Hàm lấy giá trị của current leg (bearish = 0, bullish = 1)
def leg(size, highs, lows):
    """
    Xác định giá trị leg hiện tại (0: bearish, 1: bullish)
    
    :param size: (int) Độ dài của cửa sổ kiểm tra
    :param highs: (list) Danh sách giá cao (high)
    :param lows: (list) Danh sách giá thấp (low)
    :return: (int) 0 nếu Bearish, 1 nếu Bullish
    """
    if len(highs) < size or len(lows) < size:
        return None  # Tránh lỗi khi không đủ dữ liệu

    highest_high = max(highs[-size:])  # Tìm giá cao nhất trong cửa sổ
    lowest_low = min(lows[-size:])  # Tìm giá thấp nhất trong cửa sổ

    new_leg_high = highs[-1] > highest_high
    new_leg_low = lows[-1] < lowest_low

    if new_leg_high:
        return BEARISH_LEG
    elif new_leg_low:
        return BULLISH_LEG
    return 0  # Nếu không có thay đổi, giữ nguyên giá trị cũ

# 📌 Hàm xác định cấu trúc hiện tại và điểm xoay (swing points)
def get_current_structure(size, equal_high_low=False, internal=False):
    """
    Lưu trữ cấu trúc hiện tại và trailing swing points.
    
    :param size: (int) Kích thước cấu trúc
    :param equal_high_low: (bool) Hiển thị Equal Highs/Lows
    :param internal: (bool) Xác định cấu trúc nội bộ
    """
    current_leg = leg(size)  # Xác định trạng thái leg
    new_pivot = start_of_new_leg([current_leg])  # Kiểm tra điểm xoay mới
    pivot_low = start_of_bullish_leg([current_leg])  # Kiểm tra bullish pivot
    pivot_high = start_of_bearish_leg([current_leg])  # Kiểm tra bearish pivot

    swingBullishColor = "#F23645" 
    swingBearishColor = "#089981"
    
    if new_pivot:
        if pivot_low:
            p_ivot = equalLow if equal_high_low else internalLow if internal else swingLow

            # Kiểm tra và vẽ Equal Low
            if equal_high_low and abs(p_ivot.currentLevel - lows[size]) < equalHighsLowsThresholdInput * atrMeasure:
                draw_equal_high_low(p_ivot, lows[size], size, False)

            # Cập nhật pivot point
            p_ivot.lastLevel = p_ivot.currentLevel
            p_ivot.currentLevel = lows[size]
            p_ivot.crossed = False
            p_ivot.barTime = times[size]
            p_ivot.barIndex = size  # Trong Pine Script: `bar_index[size]`

            # Cập nhật thông tin trailing bottom nếu không phải internal hoặc equal high/low
            if not equal_high_low and not internal:
                trailing.bottom = p_ivot.currentLevel
                trailing.barTime = p_ivot.barTime
                trailing.barIndex = p_ivot.barIndex
                trailing.lastBottomTime = p_ivot.barTime

            # Hiển thị swing points nếu được bật
            if showSwingsInput and not internal and not equal_high_low:
                draw_label(
                    times[size],
                    p_ivot.currentLevel,
                    "LL" if p_ivot.currentLevel < p_ivot.lastLevel else "HL",
                    swingBullishColor,
                    "label_up"
                )

        else:
            p_ivot = equalHigh if equal_high_low else internalHigh if internal else swingHigh

            # Kiểm tra và vẽ Equal High
            if equal_high_low and abs(p_ivot.currentLevel - highs[size]) < equalHighsLowsThresholdInput * atrMeasure:
                draw_equal_high_low(p_ivot, highs[size], size, True)

            # Cập nhật pivot point
            p_ivot.lastLevel = p_ivot.currentLevel
            p_ivot.currentLevel = highs[size]
            p_ivot.crossed = False
            p_ivot.barTime = times[size]
            p_ivot.barIndex = size  # Trong Pine Script: `bar_index[size]`

            # Cập nhật thông tin trailing top nếu không phải internal hoặc equal high/low
            if not equal_high_low and not internal:
                trailing.top = p_ivot.currentLevel
                trailing.barTime = p_ivot.barTime
                trailing.barIndex = p_ivot.barIndex
                trailing.lastTopTime = p_ivot.barTime

            # Hiển thị swing points nếu được bật
            if showSwingsInput and not internal and not equal_high_low:
                draw_label(
                    times[size],
                    p_ivot.currentLevel,
                    "HH" if p_ivot.currentLevel > p_ivot.lastLevel else "LH",
                    swingBearishColor,
                    "label_down"
                )
                
def draw_structure(pivot, tag, structure_color, line_style, label_style, label_size, mode="Present"):
    """
    Vẽ đường và nhãn đại diện cho một cấu trúc bằng Plotly.

    :param pivot: (Pivot) Điểm pivot cơ sở.
    :param tag: (str) Văn bản hiển thị trên nhãn.
    :param structure_color: (str) Màu sắc của cấu trúc.
    :param line_style: (str) Kiểu đường (solid, dash, dot).
    :param label_style: (str) Kiểu nhãn ("label_up" hoặc "label_down").
    :param label_size: (int) Cỡ chữ hiển thị trên nhãn.
    :param mode: (str) Chế độ hiển thị ("Historical" hoặc "Present").
    :return: None (Thêm trực tiếp vào `fig`)
    """

    # Nếu ở chế độ "Present", xóa dữ liệu cũ trước khi vẽ mới
    if mode == "Present":
        fig.data = []  # Xóa tất cả dữ liệu cũ

    # Vẽ đường cấu trúc
    fig.add_trace(go.Scatter(
        x=[pivot.barTime, pivot.barTime + 5],  # Placeholder: Kéo dài đường 5 điểm thời gian
        y=[pivot.currentLevel, pivot.currentLevel],
        mode="lines",
        line=dict(color=structure_color, width=2, dash=line_style),
        name=tag
    ))

    # Vị trí hiển thị nhãn
    label_position_x = pivot.barTime + 2  # Dịch chuyển nhãn về phía phải
    label_position_y = pivot.currentLevel

    # Vẽ nhãn
    fig.add_trace(go.Scatter(
        x=[label_position_x],
        y=[label_position_y],
        mode="text",
        text=tag,
        textposition="top center" if label_style == "label_up" else "bottom center",
        textfont=dict(color=structure_color, size=label_size)
    ))
    
     
# Hàm main
def main():
    df = yf.download("AAPL", start="2024-01-01", end="2025-02-03", interval="1d")
    if df.empty:
        print("⚠️ Lỗi: Không tải được dữ liệu AAPL từ yfinance. Vui lòng kiểm tra kết nối mạng hoặc mã cổ phiếu.")
        return
    
    df_filtered = pd.DataFrame({
        "Date": df.index,
        "Open": df["Open"].squeeze(),
        "High": df["High"].squeeze(),
        "Low": df["Low"].squeeze(),
        "Close": df["Close"].squeeze()
    })
    df_filtered.set_index("Date", inplace=True)
    print(df_filtered)
    
    # Hiển thị biểu đồ với các Equal Highs/Lows và nhãn
    fig.show()
    
if __name__ == "__main__":
    main()