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

BULLISH_LEG = 1
BEARISH_LEG = 0

BULLISH = +1
BEARISH = -1

GREEN = "#089981"
RED = "#F23645"
BLUE = "#2157f3"
GRAY = "#878b94"
MONO_BULLISH = "#b2b5be"
MONO_BEARISH = "#5d606b"

HISTORICAL = 'Historical'
PRESENT = 'Present'

COLORED = "Colored"
MONOCHROME = "Monochrome"

ALL = 'All'
BOS = 'BOS'
CHOCH = 'CHoCH'

TINY = "tiny"
SMALL = "small"
NORMAL = "normal"

# TINY                            = size.tiny
# SMALL                           = size.small
# NORMAL                          = size.normal

ATR = "Atr"
RANGE = "Cumulative Mean Range"

CLOSE = 'Close'
HIGHLOW = 'High/Low'

SOLID = '⎯⎯⎯'
DASHED = '----'
DOTTED = '····'

# //---------------------------------------------------------------------------------------------------------------------}
# //DATA STRUCTURES & VARIABLES
# //---------------------------------------------------------------------------------------------------------------------{
    
# 📌 Cấu hình chung
config = {
    "mode": HISTORICAL,
    "style": COLORED,
    "show_trend": False
}

# 📌 Cấu hình Internal Structure
internal_structure = {
    "show_internals": True,
    "bullish_structure": ALL,
    "bullish_color": GREEN,
    "bearish_structure": ALL,
    "bearish_color": RED,
    "internal_filter_confluence": False,
    "label_size": TINY
}

# 📌 Cấu hình Swing Structure
swing_structure = {
    "show_structure": True,
    "bullish_structure": ALL,
    "bullish_color": GREEN,
    "bearish_structure": ALL,
    "bearish_color": RED,
    "label_size": SMALL,
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
    "order_block_filter": ATR,
    "order_block_mitigation": HIGHLOW,
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
    "label_size": TINY
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


# 📌 Định nghĩa cấu trúc cảnh báo (Alerts)
@dataclass
class Alerts:
    internalBullishBOS: bool = False
    internalBearishBOS: bool = False
    internalBullishCHoCH: bool = False
    internalBearishCHoCH: bool = False
    swingBullishBOS: bool = False
    swingBearishBOS: bool = False
    swingBullishCHoCH: bool = False
    swingBearishCHoCH: bool = False
    internalBullishOrderBlock: bool = False
    internalBearishOrderBlock: bool = False
    swingBullishOrderBlock: bool = False
    swingBearishOrderBlock: bool = False
    equalHighs: bool = False
    equalLows: bool = False
    bullishFairValueGap: bool = False
    bearishFairValueGap: bool = False

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

# 📌 Định nghĩa cấu trúc Equal Display để lưu label và line
@dataclass
class EqualDisplay:
    line: Optional[object] = None
    label: Optional[object] = None

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

fairValueGaps: List[FairValueGap] = []

parsedHighs: List[float] = []

parsedLows: List[float] = []

highs: List[float] = []

lows: List[float] = []

times: List[int] = []

trailing = TrailingExtremes()

swingOrderBlocks: List[OrderBlock] = []

internalOrderBlocks: List[OrderBlock] = []

swingOrderBlocksBoxes: List[object] = []

internalOrderBlocksBoxes: List[object] = []

# Màu sắc đơn sắc (monochrome)
MONO_BULLISH = "#b2b5be"  # Màu mặc định cho xu hướng tăng trong chế độ đơn sắc
MONO_BEARISH = "#5d606b"  # Màu mặc định cho xu hướng giảm trong chế độ đơn sắc

# Định nghĩa màu sắc theo phong cách
COLOR_SCHEME = {
    "swingBullishColor": {"monochrome": MONO_BULLISH, "colored": "#089981"},
    "swingBearishColor": {"monochrome": MONO_BEARISH, "colored": "#F23645"},
    "fairValueGapBullishColor": {"monochrome": MONO_BULLISH, "colored": "#00ff68"},
    "fairValueGapBearishColor": {"monochrome": MONO_BEARISH, "colored": "#ff0008"},
    "premiumZoneColor": {"monochrome": MONO_BEARISH, "colored": "#F23645"},
    "discountZoneColor": {"monochrome": MONO_BULLISH, "colored": "#089981"},
}

# Xác định chế độ hiển thị màu sắc
styleInput = MONOCHROME  # Hoặc COLORED

# Gán giá trị màu sắc dựa trên chế độ hiển thị
swingBullishColor = COLOR_SCHEME["swingBullishColor"]["monochrome"] if styleInput == MONOCHROME else COLOR_SCHEME["swingBullishColor"]["colored"]
swingBearishColor = COLOR_SCHEME["swingBearishColor"]["monochrome"] if styleInput == MONOCHROME else COLOR_SCHEME["swingBearishColor"]["colored"]
fairValueGapBullishColor = COLOR_SCHEME["fairValueGapBullishColor"]["monochrome"] if styleInput == MONOCHROME else COLOR_SCHEME["fairValueGapBullishColor"]["colored"]
fairValueGapBearishColor = COLOR_SCHEME["fairValueGapBearishColor"]["monochrome"] if styleInput == MONOCHROME else COLOR_SCHEME["fairValueGapBearishColor"]["colored"]
premiumZoneColor = COLOR_SCHEME["premiumZoneColor"]["monochrome"] if styleInput == MONOCHROME else COLOR_SCHEME["premiumZoneColor"]["colored"]
discountZoneColor = COLOR_SCHEME["discountZoneColor"]["monochrome"] if styleInput == MONOCHROME else COLOR_SCHEME["discountZoneColor"]["colored"]

currentAlerts = Alerts()

def initialize_order_blocks(showSwingOrderBlocks, showInternalOrderBlocks, swingOrderBlocksSize, internalOrderBlocksSize):
    if showSwingOrderBlocks:
        for _ in range(swingOrderBlocksSize):
            swingOrderBlocksBoxes.append(None)  # Giả lập hộp giá trị
    if showInternalOrderBlocks:
        for _ in range(internalOrderBlocksSize):
            internalOrderBlocksBoxes.append(None)

# # Xác định nguồn sử dụng trong Bearish Order Blocks Mitigation
# bearishOrderBlockMitigationSource = CLOSE if orderBlockMitigationInput == CLOSE else HIGH

# # Xác định nguồn sử dụng trong Bullish Order Blocks Mitigation
# bullishOrderBlockMitigationSource = CLOSE if orderBlockMitigationInput == CLOSE else LOW

# Trích xuất giá trị order_block_mitigation từ dictionary
orderBlockMitigationInput = order_blocks.get("order_block_mitigation", "CLOSE")  # Mặc định là "CLOSE" nếu không tìm thấy

# Xác định nguồn sử dụng trong Bearish Order Blocks Mitigation
bearishOrderBlockMitigationSource = "Close" if orderBlockMitigationInput == "CLOSE" else "High"

# Xác định nguồn sử dụng trong Bullish Order Blocks Mitigation
bullishOrderBlockMitigationSource = "Close" if orderBlockMitigationInput == "CLOSE" else "Low"

import numpy as np

def compute_atr(highs, lows, closes, period=200):
    # Kiểm tra đầu vào
    if len(highs) != len(lows) or len(highs) != len(closes):
        raise ValueError("Lengths of highs, lows, and closes must be the same.")

    if len(highs) < period + 1:
        print(f"Not enough data to compute ATR for period={period}. Require at least {period+1} data points.")
        return None

    # Tính True Range (TR) theo chuẩn
    tr = np.maximum(
        highs[1:] - lows[1:], 
        np.maximum(
            np.abs(highs[1:] - closes[:-1]), 
            np.abs(lows[1:] - closes[:-1])
        )
    )

    # Kiểm tra lại số lượng TR có đủ cho chu kỳ ATR không
    if len(tr) < period:
        print(f"Not enough TR values to compute ATR for period={period}.")
        return None

    # Tính ATR (SMA của các giá trị TR)
    atr = np.mean(tr[-period:])
    return atr if not np.isnan(atr) else None


# 📌 Xác định thanh có độ biến động cao
def is_high_volatility_bar(high, low, volatilityMeasure):
    return (high - low) >= (2 * volatilityMeasure)

# //---------------------------------------------------------------------------------------------------------------------}
# //USER-DEFINED FUNCTIONS
# //---------------------------------------------------------------------------------------------------------------------{

# 📌 Hàm lấy giá trị của current leg (bearish = 0, bullish = 1)
def leg(size, highs, lows):
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

# 📌 Hàm kiểm tra có phải điểm bắt đầu của leg mới hay không
def start_of_new_leg(leg_values):
    if len(leg_values) < 2:
        print("⚠️ Lỗi: Không đủ dữ liệu để xác định leg mới.")
        return False  # Không có đủ dữ liệu để so sánh
    
    return leg_values[-1] != leg_values[-2]

# 📌 Hàm kiểm tra có phải điểm bắt đầu của Bearish Leg (Swing Down)
def start_of_bearish_leg(leg_values):
    if len(leg_values) < 2:
        print("⚠️ Lỗi: Không đủ dữ liệu để xác định leg mới.")
        return False
    
    return (leg_values[-2] == BULLISH_LEG) and (leg_values[-1] == BEARISH_LEG)

# 📌 Hàm kiểm tra có phải điểm bắt đầu của Bullish Leg (Swing Up)
def start_of_bullish_leg(leg_values):
    if len(leg_values) < 2:
        print("⚠️ Lỗi: Không đủ dữ liệu để xác định leg mới.")
        return False
    
    return (leg_values[-2] == BEARISH_LEG) and (leg_values[-1] == BULLISH_LEG)

def draw_label(label_time, 
            label_price, tag, label_color, 
            label_style, mode=PRESENT, 
            text_size=12, x_offset=0, y_offset=0):
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
    if mode == PRESENT:
        fig.data = []  # Xóa tất cả dữ liệu cũ

    fig.add_trace(go.Scatter(
        x=[label_time + x_offset],
        y=[label_price + y_offset],
        mode="text",
        text=tag,
        textposition="top center" if label_style == "label_up" else "bottom center",
        textfont=dict(color=label_color, size=text_size)
    ))

def draw_equal_high_low(pivot, level, size, equal_high, 
                        mode=PRESENT, line_width=1, line_dash="dot", text_size=12):
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
    if mode == PRESENT:
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

# 📌 Hàm xác định cấu trúc hiện tại và điểm xoay (swing points)
def get_current_structure(size, atrMeasure, equal_high_low=False, internal=False):
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
            if swing_structure.get("show_swings", None) and not internal and not equal_high_low:
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
            if swing_structure.get("show_swings", None) and not internal and not equal_high_low:
                draw_label(
                    times[size],
                    p_ivot.currentLevel,
                    "HH" if p_ivot.currentLevel > p_ivot.lastLevel else "LH",
                    swingBearishColor,
                    "label_down"
                )
                
def draw_structure(pivot, tag, structure_color, line_style, 
                label_style, label_size, mode=PRESENT):
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
    if mode == PRESENT:
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

# 📌 Hàm xóa Order Blocks
def delete_order_blocks(internal=False):
    """
    Xóa các order blocks nếu bị cắt ngang.

    :param internal: (bool) True nếu là Internal Order Blocks
    """
    order_blocks = internalOrderBlocks if internal else swingOrderBlocks

    for index in range(len(order_blocks) - 1, -1, -1):  # Lặp ngược để tránh lỗi khi xóa phần tử
        each_order_block = order_blocks[index]
        crossed_order_block = False

        if bearishOrderBlockMitigationSource > each_order_block.barHigh and each_order_block.bias == BEARISH:
            crossed_order_block = True
        elif bullishOrderBlockMitigationSource < each_order_block.barLow and each_order_block.bias == BULLISH:
            crossed_order_block = True

        if crossed_order_block:
            order_blocks.pop(index)

# 📌 Hàm lưu Order Blocks
def store_order_block(pivot, currentBarIndex, internal=False, bias=BULLISH):
    """
    Lưu trữ Order Blocks mới.

    :param pivot: (Pivot) Điểm pivot cơ sở
    :param internal: (bool) True nếu là Internal Order Blocks
    :param bias: (int) BULLISH (+1) hoặc BEARISH (-1)
    """
    if (not internal and order_blocks.get("show_swing_order_blocks")) or (internal and order_blocks.get("show_internal_order_blocks")):
        order_blocks = internalOrderBlocks if internal else swingOrderBlocks

        # Kiểm tra xem pivot.barIndex có hợp lệ không
        if pivot.barIndex is None or pivot.barIndex >= len(parsedHighs) or pivot.barIndex >= len(parsedLows):
            print("Invalid pivot data to compute Order Block")
            return  # Bỏ qua nếu không đủ dữ liệu

        # Xác định chỉ mục `parsed_index`
        if bias == BEARISH:
            sliced_highs = parsedHighs[pivot.barIndex:currentBarIndex]
            if sliced_highs:
                parsed_index = pivot.barIndex + sliced_highs.index(max(sliced_highs))
            else:
                print("No data to compute Order Block")
                return  # Không có dữ liệu để tính toán
        else:
            sliced_lows = parsedLows[pivot.barIndex:currentBarIndex]
            if sliced_lows:
                parsed_index = pivot.barIndex + sliced_lows.index(min(sliced_lows))
            else:
                print("No data to compute Order Block")
                return  # Không có dữ liệu để tính toán

        # Kiểm tra xem parsed_index có hợp lệ không
        if parsed_index >= len(parsedHighs) or parsed_index >= len(parsedLows) or parsed_index >= len(times):
            print("Invalid data to compute Order Block")
            return  # Bỏ qua nếu dữ liệu không hợp lệ

        # Tạo Order Block mới
        new_order_block = OrderBlock(
            parsedHighs[parsed_index],
            parsedLows[parsed_index],
            times[parsed_index],
            bias
        )

        print("New Order Block Created:", new_order_block)

        # Giữ danh sách Order Blocks dưới 100 phần tử
        if len(order_blocks) >= 100:
            order_blocks.pop()

        # Thêm Order Block vào danh sách
        order_blocks.insert(0, new_order_block)

def draw_order_blocks(fig, internal=False):
    """
    Vẽ Order Blocks dưới dạng hộp (box) sử dụng Plotly.

    :param fig: (plotly.graph_objects.Figure) Đối tượng biểu đồ để vẽ lên.
    :param internal: (bool) True nếu là Internal Order Blocks.
    """
    # Chọn danh sách orderBlocks dựa vào giá trị internal
    orderBlocks = internalOrderBlocks if internal else swingOrderBlocks

    # Lấy kích thước của danh sách orderBlocks
    order_blocks_size = len(orderBlocks)


    if order_blocks_size > 0:
        max_order_blocks = order_blocks.get("internal_order_blocks_size", None) if internal else order_blocks.get("swing_order_blocks_size", None)
        parsed_order_blocks = order_blocks[:min(max_order_blocks, order_blocks_size)]
        
        for each_order_block in parsed_order_blocks:
            order_block_color = (
                MONO_BEARISH if each_order_block.bias == BEARISH else MONO_BULLISH
                if styleInput == MONOCHROME
                else order_blocks.get("internal_bearish_color", None)
                if internal and each_order_block.bias == BEARISH
                else order_blocks.get("internal_bullish_color", None)
                if internal
                else order_blocks.get("swing_bearish_color", None)
                if each_order_block.bias == BEARISH
                else order_blocks.get("swing_bullish_color", None)
            )

            # Vẽ hình chữ nhật (Order Block)
            fig.add_trace(go.Scatter(
                x=[each_order_block.barTime, each_order_block.barTime, "last_bar_time", "last_bar_time", each_order_block.barTime],
                y=[each_order_block.barHigh, each_order_block.barLow, each_order_block.barLow, each_order_block.barHigh, each_order_block.barHigh],
                fill="toself",
                fillcolor=order_block_color,
                line=dict(color=None if internal else order_block_color),
                name="Internal Order Block" if internal else "Swing Order Block",
                opacity=0.5
            ))

    return fig

# 📌 Hàm phát hiện và vẽ cấu trúc thị trường bằng Plotly
def display_structure(opens, closes, fig, internal=False):
    """
    Phát hiện và vẽ cấu trúc thị trường, đồng thời lưu Order Blocks bằng Plotly.

    :param fig: (go.Figure) Đối tượng Figure của Plotly
    :param internal: (bool) True nếu là cấu trúc nội bộ
    """
    bullish_bar, bearish_bar = True, True

    if internal_structure.get("internal_filter_confluence", None):
        bullish_bar = highs[-1] - max(closes[-1], opens[-1]) > min(closes[-1], opens[-1] - lows[-1])
        bearish_bar = highs[-1] - max(closes[-1], opens[-1]) < min(closes[-1], opens[-1] - lows[-1])

    pivot = internalHigh if internal else swingHigh
    trend = internalTrend if internal else swingTrend

    line_style = "dash" if internal else "solid"
    label_size = internal_structure.get("label_size", None) if internal else swing_structure.get("label_size", None) 
    extra_condition = internal and internalHigh.currentLevel != swingHigh.currentLevel and bullish_bar
    bullish_color = MONO_BULLISH if styleInput == MONOCHROME else internal_structure.get("bullish_color", None) if internal else swing_structure.get("bullish_color", None)

    # 📌 Xử lý Bullish Structure
    if closes[-1] > pivot.currentLevel and not pivot.crossed and extra_condition:
        tag = CHOCH if trend.bias == BEARISH else BOS
        pivot.crossed = True
        trend.bias = BULLISH

        if internal:
            currentAlerts.internalBullishCHoCH = tag == CHOCH
            currentAlerts.internalBullishBOS = tag == BOS
        else:
            currentAlerts.swingBullishCHoCH = tag == CHOCH
            currentAlerts.swingBullishBOS = tag == BOS

        if swing_structure.get("show_structure", None):
            # 📌 Vẽ đường cấu trúc Bullish
            fig.add_trace(go.Scatter(
                x=[pivot.barTime, times[-1]], 
                y=[pivot.currentLevel, pivot.currentLevel],
                mode="lines",
                line=dict(color=bullish_color, width=2, dash=line_style),
                name=f"{tag} - Bullish"
            ))

            # 📌 Thêm nhãn (Label)
            fig.add_annotation(
                x=times[-1], y=pivot.currentLevel,
                text=tag,
                showarrow=True,
                arrowhead=2,
                font=dict(color=bullish_color, size=label_size),
                yshift=10
            )

        if (internal and order_blocks.get("show_internal_order_blocks", None)) or (not internal and order_blocks.get("show_swing_order_blocks", None)):
            store_order_block(pivot, internal, BULLISH)

    # 📌 Xử lý Bearish Structure
    pivot = internalLow if internal else swingLow
    extra_condition = internal and internalLow.currentLevel != swingLow.currentLevel and bearish_bar
    bearish_color = MONO_BEARISH if styleInput == MONOCHROME else internal_structure.get("bearish_color", None) if internal else swing_structure.get("bearish_color", None)

    if closes[-1] < pivot.currentLevel and not pivot.crossed and extra_condition:
        tag = CHOCH if trend.bias == BULLISH else BOS
        pivot.crossed = True
        trend.bias = BEARISH

        if internal:
            currentAlerts.internalBearishCHoCH = tag == CHOCH
            currentAlerts.internalBearishBOS = tag == BOS
        else:
            currentAlerts.swingBearishCHoCH = tag == CHOCH
            currentAlerts.swingBearishBOS = tag == BOS

        if swing_structure.get("show_structure", None):
            # 📌 Vẽ đường cấu trúc Bearish
            fig.add_trace(go.Scatter(
                x=[pivot.barTime, times[-1]], 
                y=[pivot.currentLevel, pivot.currentLevel],
                mode="lines",
                line=dict(color=bearish_color, width=2, dash=line_style),
                name=f"{tag} - Bearish"
            ))

            # 📌 Thêm nhãn (Label)
            fig.add_annotation(
                x=times[-1], y=pivot.currentLevel,
                text=tag,
                showarrow=True,
                arrowhead=2,
                font=dict(color=bearish_color, size=label_size),
                yshift=-10
            )

        if (internal and order_blocks.get("show_internal_order_blocks", None)) or (not internal and order_blocks.get("show_swing_order_blocks", None)):
            store_order_block(pivot, internal, BEARISH)

    return fig  # Trả về đối tượng figure đã cập nhật

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
    print("========================================")
    
    # // we create the needed boxes for displaying order blocks at the first execution
    # if barstate.isfirst
    #     if showSwingOrderBlocksInput
    #         for index = 1 to swingOrderBlocksSizeInput
    #             swingOrderBlocksBoxes.push(box.new(na,na,na,na,xloc = xloc.bar_time,extend = extend.right))
    #     if showInternalOrderBlocksInput
    #         for index = 1 to internalOrderBlocksSizeInput
    #             internalOrderBlocksBoxes.push(box.new(na,na,na,na,xloc = xloc.bar_time,extend = extend.right))
    showSwingOrderBlocksInput = order_blocks.get("show_swing_order_blocks", False)
    showInternalOrderBlocksInput = order_blocks.get("show_internal_order_blocks", True)
    swingOrderBlocksSizeInput = order_blocks.get("swing_order_blocks_size", 5)
    internalOrderBlocksSizeInput = order_blocks.get("internal_order_blocks_size", 5)
    if not df_filtered.empty:
        if "Close" in df_filtered.columns and not df_filtered["Close"].empty:
                initialize_order_blocks(showSwingOrderBlocksInput, showInternalOrderBlocksInput, 
                                        swingOrderBlocksSizeInput, internalOrderBlocksSizeInput)
                draw_order_blocks(fig, internal=False)
        else:
            print("⚠️ Cảnh báo: df_filtered không có dữ liệu 'Close'. Không thể khởi tạo Order Blocks.")
    else:
        print("⚠️ Cảnh báo: df_filtered rỗng. Không thể khởi tạo Order Blocks.")

    # Khởi tạo các biến cần thiết
    atrMeasure = compute_atr(
        df_filtered["High"].values,  
        df_filtered["Low"].values,   
        df_filtered["Close"].values, 
        200
    ) if not df_filtered.empty else 0
    print("atrMeasure:" + str(atrMeasure))
    print("========================================")

    orderBlockFilterInput = ATR
    
    if not df_filtered.empty:
        volatilityMeasure = (
            compute_atr(
                df_filtered["High"].values, 
                df_filtered["Low"].values, 
                df_filtered["Close"].values, 
                200
            ) if orderBlockFilterInput == ATR else 
            np.cumsum(np.abs(df_filtered["High"].values - df_filtered["Low"].values)) / max(1, len(df_filtered))
        )
    else:
        volatilityMeasure = 0

    print("volatilityMeasure:" + str(volatilityMeasure))
    
    # 📌 Lấy giá cao/thấp đã xử lý
    highVolatilityBar = is_high_volatility_bar(
        df_filtered["High"].iloc[-1], 
        df_filtered["Low"].iloc[-1], 
        volatilityMeasure[-1] if isinstance(volatilityMeasure, np.ndarray) else volatilityMeasure
    )

    parsedHigh = df_filtered["Low"].iloc[-1] if highVolatilityBar else df_filtered["High"].iloc[-1]
    parsedLow = df_filtered["High"].iloc[-1] if highVolatilityBar else df_filtered["Low"].iloc[-1]

    # 📌 Lưu trữ dữ liệu mới vào danh sách
    parsedHighs.append(parsedHigh)
    parsedLows.append(parsedLow)
    highs.append(df_filtered["High"].iloc[-1])
    lows.append(df_filtered["Low"].iloc[-1])
    times.append(df_filtered.index[-1])  

    # Hiển thị biểu đồ với các Equal Highs/Lows và nhãn
    # fig.show()
    
if __name__ == "__main__":
    main()