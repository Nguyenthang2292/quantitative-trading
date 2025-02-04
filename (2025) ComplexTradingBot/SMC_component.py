import yfinance as yf
import pandas as pd
import numpy as np
from dataclasses import dataclass
import plotly.graph_objects as go
from dataclasses import dataclass
from typing import List, Optional
import bisect
import logging

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

# TINY = size.tiny
# SMALL = size.small
# NORMAL = size.normal

ATR = "Atr"
RANGE = "Cumulative Mean Range"

CLOSE = 'Close'
HIGHLOW = 'High/Low'

SOLID = 'solid'
DASHED = 'dashed'
DOTTED = 'dotted'

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
    "show_swing_order_blocks": True,
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
    "show": False,
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
styleInput = COLOR_SCHEME  # Hoặc COLORED

# Gán giá trị màu sắc dựa trên chế độ hiển thị
swingBullishColor = COLOR_SCHEME["swingBullishColor"]["monochrome"] if styleInput == MONOCHROME else COLOR_SCHEME["swingBullishColor"]["colored"]
swingBearishColor = COLOR_SCHEME["swingBearishColor"]["monochrome"] if styleInput == MONOCHROME else COLOR_SCHEME["swingBearishColor"]["colored"]
fairValueGapBullishColor = COLOR_SCHEME["fairValueGapBullishColor"]["monochrome"] if styleInput == MONOCHROME else COLOR_SCHEME["fairValueGapBullishColor"]["colored"]
fairValueGapBearishColor = COLOR_SCHEME["fairValueGapBearishColor"]["monochrome"] if styleInput == MONOCHROME else COLOR_SCHEME["fairValueGapBearishColor"]["colored"]
premiumZoneColor = COLOR_SCHEME["premiumZoneColor"]["monochrome"] if styleInput == MONOCHROME else COLOR_SCHEME["premiumZoneColor"]["colored"]
discountZoneColor = COLOR_SCHEME["discountZoneColor"]["monochrome"] if styleInput == MONOCHROME else COLOR_SCHEME["discountZoneColor"]["colored"]

currentAlerts = Alerts()

def box_new(x0, x1, y0, y1, xloc, extend):
    return {
        "x0": x0,
        "x1": x1,
        "y0": y0,
        "y1": y1,
        "xloc": xloc,
        "extend": extend
    }

def initialize_order_blocks(showSwingOrderBlocks, 
                            showInternalOrderBlocks, 
                            swingOrderBlocksSize, 
                            internalOrderBlocksSize,
                            swing_box_params, 
                            internal_box_params):
    if showSwingOrderBlocks:
        for _ in range(swingOrderBlocksSize):
            swingOrderBlocksBoxes.append(box_new(*swing_box_params))
            print("Swing Order Blocks Boxes Append Success:", swingOrderBlocksBoxes)
            
    if showInternalOrderBlocks:
        for _ in range(internalOrderBlocksSize):
            internalOrderBlocksBoxes.append(box_new(*internal_box_params))
            print("Internal Order Blocks Boxes Append Success:", internalOrderBlocksBoxes)
            
# Trích xuất giá trị order_block_mitigation từ dictionary
orderBlockMitigationInput = order_blocks.get("order_block_mitigation", CLOSE)

# Xác định nguồn sử dụng trong Bearish Order Blocks Mitigation
bearishOrderBlockMitigationSource = "Close" if orderBlockMitigationInput == CLOSE else "High"

# Xác định nguồn sử dụng trong Bullish Order Blocks Mitigation
bullishOrderBlockMitigationSource = "Close" if orderBlockMitigationInput == CLOSE else "Low"

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

def draw_label(fig,
                label_time, 
                label_price, 
                tag, 
                label_color, 
                label_style, 
                mode=PRESENT, 
                text_size=12, 
                x_offset=0, 
                y_offset=0):

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
    
    return fig

def draw_equal_high_low(fig,
                        pivot, 
                        level, 
                        size, 
                        equal_high, 
                        mode=PRESENT, 
                        line_width=1, 
                        line_dash="dot", 
                        text_size=12):

    tag = "EQH" if equal_high else "EQL"
    color = "#F23645" if equal_high else "#089981"  # Màu swingBearishColor hoặc swingBullishColor
    label_style = "label_down" if equal_high else "label_up"

    # CẦN CHÚ Ý CHỖ NÀY
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
    fig = draw_label(times[size], 
            level, 
            tag, 
            color, 
            label_style, 
            text_size=text_size)
    
    return fig

# 📌 Hàm xác định cấu trúc hiện tại và điểm xoay (swing points)
def get_current_structure(size, 
                        atrMeasure, 
                        equal_high_low=False, 
                        internal=False):
    
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
            if swing_structure.get("show_swings", False) and not internal and not equal_high_low:
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
            if swing_structure.get("show_swings", False) and not internal and not equal_high_low:
                draw_label(times[size],
                        p_ivot.currentLevel,
                        "HH" if p_ivot.currentLevel > p_ivot.lastLevel else "LH",
                        swingBearishColor,
                        "label_down")
                
def draw_structure(fig,
                    pivot, 
                    tag, 
                    structure_color, 
                    line_style, 
                    label_style, 
                    label_size,
                    mode=PRESENT):
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
                textfont=dict(color=structure_color, size=label_size)))
    
    return fig

# 📌 Hàm xóa Order Blocks
def delete_order_blocks(internal=False):
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
    if (not internal and order_blocks.get("show_swing_order_blocks", True)) or (internal and order_blocks.get("show_internal_order_blocks", True)):
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
            bias)

        print("New Order Block Created:", new_order_block)

        # Giữ danh sách Order Blocks dưới 100 phần tử
        if len(order_blocks) >= 100:
            order_blocks.pop()

        # Thêm Order Block vào danh sách
        order_blocks.insert(0, new_order_block)

def draw_order_blocks(fig, internal=False):
    # Chọn danh sách orderBlocks dựa vào giá trị internal
    orderBlocks = internalOrderBlocks if internal else swingOrderBlocks

    # Lấy kích thước của danh sách orderBlocks
    order_blocks_size = len(orderBlocks)
    print("Order Blocks Size:", order_blocks_size)

    if order_blocks_size > 0:
        max_order_blocks = order_blocks.get("internal_order_blocks_size", 5) if internal else order_blocks.get("swing_order_blocks_size", 5)
        parsed_order_blocks = order_blocks[:min(max_order_blocks, order_blocks_size)]
        
        for each_order_block in parsed_order_blocks:
            order_block_color = (
                MONO_BEARISH if each_order_block.bias == BEARISH else MONO_BULLISH
                if styleInput == MONOCHROME
                else order_blocks.get("internal_bearish_color", "#f77c80")
                if internal and each_order_block.bias == BEARISH
                else order_blocks.get("internal_bullish_color", "#3179f5")
                if internal
                else order_blocks.get("swing_bearish_color", "#b22833")
                if each_order_block.bias == BEARISH
                else order_blocks.get("swing_bullish_color", "#1848cc")
            )
            
            fig.add_shape(
                type="rect",
                x0=order_block_color["x0"],
                x1=order_block_color["x1"],
                y0=order_block_color["y0"],
                y1=order_block_color["y1"],
                xref="x",  # sử dụng trục x của biểu đồ
                yref="y",
                fill="toself",
                fillcolor=order_block_color,
                line=dict(color=None if internal else order_block_color),
                name="Internal Order Block" if internal else "Swing Order Block",
                opacity=0.5   
            )

    return fig

# 📌 Hàm phát hiện và vẽ cấu trúc thị trường bằng Plotly
def display_structure(opens, closes, fig, internal=False):
    
    bullish_bar, bearish_bar = True, True

    if internal_structure.get("internal_filter_confluence", False):
        bullish_bar = highs[-1] - max(closes[-1], opens[-1]) > min(closes[-1], opens[-1] - lows[-1])
        bearish_bar = highs[-1] - max(closes[-1], opens[-1]) < min(closes[-1], opens[-1] - lows[-1])

    pivot = internalHigh if internal else swingHigh
    trend = internalTrend if internal else swingTrend

    line_style = "dash" if internal else "solid"
    label_size = internal_structure.get("label_size", TINY) if internal else swing_structure.get("label_size", SMALL) 
    extra_condition = internal and internalHigh.currentLevel != swingHigh.currentLevel and bullish_bar
    bullish_color = MONO_BULLISH if styleInput == MONOCHROME else internal_structure.get("bullish_color", GREEN) if internal else swing_structure.get("bullish_color", GREEN)

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

        if swing_structure.get("show_structure", True):
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

        if (internal and order_blocks.get("show_internal_order_blocks", True)) or (not internal and order_blocks.get("show_swing_order_blocks", True)):
            store_order_block(pivot, internal, BULLISH)
            
        return fig

    # 📌 Xử lý Bearish Structure
    pivot = internalLow if internal else swingLow
    extra_condition = internal and internalLow.currentLevel != swingLow.currentLevel and bearish_bar
    bearish_color = MONO_BEARISH if styleInput == MONOCHROME else internal_structure.get("bearish_color", RED) if internal else swing_structure.get("bearish_color", RED)

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

        if swing_structure.get("show_structure", True):
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

        if (internal and order_blocks.get("show_internal_order_blocks", True)) or (not internal and order_blocks.get("show_swing_order_blocks", True)):
            store_order_block(pivot, internal, BEARISH)

    return fig 

# --- Hàm 1: fairValueGapBox ---
def fairValueGapBox(fig, leftTime, rightTime, topPrice, bottomPrice, boxColor, time, previous_time):
    # Mở rộng thời gian bên phải
    extended_right = rightTime + fair_value_gaps.value("extend_bars", None) * (time - previous_time)
    fig.add_shape(
        type="rect",
        x0=leftTime,
        x1=extended_right,
        y0=bottomPrice,
        y1=topPrice,
        line=dict(color=boxColor),
        fillcolor=boxColor)
    
    return fig

# --- Hàm 2: deleteFairValueGaps ---
def delete_fair_value_gaps(fairValueGaps, low, high):
    for index in range(len(fairValueGaps) - 1, -1, -1):
        eachGap = fairValueGaps[index]
        crossed = False
        if low < eachGap["bottom"] and eachGap["bias"] == BULLISH:
            crossed = True
        elif high > eachGap["top"] and eachGap["bias"] == BEARISH:
            crossed = True
        if crossed:
            # Giả lập việc xóa box: trong Plotly ta không xóa shape, chỉ loại bỏ khỏi danh sách
            # Mẫu này chỉ xóa fair value gap khỏi danh sách
            fairValueGaps.pop(index)
    return fairValueGaps

# --- Hàm 3: drawFairValueGaps ---
def draw_fair_value_gaps(
                    fairValueGaps, 
                    fig,
                    fairValueGapsTimeframeInput, 
                    fairValueGapsThresholdInput,
                    lastClose, 
                    lastOpen, 
                    lastTime,
                    currentHigh, 
                    currentLow, 
                    currentTime,
                    last2High, 
                    last2Low, 
                    bar_index,
                    fairValueGapBullishColor, 
                    fairValueGapBearishColor):

    barDeltaPercent = (lastClose - lastOpen) / (lastOpen * 100)
    newTimeframe = True  # Giả sử luôn True
    if fairValueGapsThresholdInput:
        threshold = abs(barDeltaPercent) * 2 / bar_index
    else:
        threshold = 0

    bullishFairValueGap = (currentLow > last2High and lastClose > last2High and barDeltaPercent > threshold and newTimeframe)
    bearishFairValueGap = (currentHigh < last2Low and lastClose < last2Low and -barDeltaPercent > threshold and newTimeframe)

    if bullishFairValueGap:
        currentAlerts["bullishFairValueGap"] = True
        # Vẽ box cho gap bullish
        # Giả sử dùng lastTime làm leftTime và currentTime làm rightTime, và dùng (currentLow+last2High)/2 làm trung điểm
        midPrice = (currentLow + last2High) / 2
        # Vẽ top box: từ lastTime đến currentTime, box từ currentLow đến midPrice
        fig = fairValueGapBox(fig, lastTime, currentTime, currentLow, midPrice, fairValueGapBullishColor, time=lastTime, previous_time=lastTime)
        # Vẽ bottom box: từ lastTime đến currentTime, box từ midPrice đến last2High
        fig = fairValueGapBox(fig, lastTime, currentTime, midPrice, last2High, fairValueGapBullishColor, time=lastTime, previous_time=lastTime)
        new_gap = {
            "bottom": currentLow,
            "top": last2High,
            "bias": BULLISH,
            "topBox": "BoxID_top",    # placeholder
            "bottomBox": "BoxID_bottom"  # placeholder
        }
        fairValueGaps.insert(0, new_gap)

    if bearishFairValueGap:
        currentAlerts["bearishFairValueGap"] = True
        midPrice = (currentHigh + last2Low) / 2
        fig = fairValueGapBox(fig, lastTime, currentTime, currentHigh, midPrice, fairValueGapBearishColor, time=lastTime, previous_time=lastTime)
        fig = fairValueGapBox(fig, lastTime, currentTime, midPrice, last2Low, fairValueGapBearishColor, time=lastTime, previous_time=lastTime)
        new_gap = {
            "top": currentHigh,
            "bottom": last2Low,
            "bias": BEARISH,
            "topBox": "BoxID_top",
            "bottomBox": "BoxID_bottom"
        }
        fairValueGaps.insert(0, new_gap)

    return fairValueGaps, fig

# 📌 Hàm lấy kiểu đường từ chuỗi
def get_style(style):
    styles = {
        "SOLID": "solid",
        "DASHED": "dashed",
        "DOTTED": "dotted"
    }
    return styles.get(style, "solid")

def draw_levels(
    fig,                        # đối tượng Figure Plotly đã khởi tạo
    timeframe,                  # chuỗi, base timeframe
    sameTimeframe,              # bool, True nếu chart timeframe bằng base timeframe
    style,                      # kiểu đường: "solid", "dash", "dot",...
    levelColor,                 # màu của đường và nhãn (ví dụ "#FF0000")
    current_high,               # giá high hiện tại (nếu sameTimeframe)
    current_low,                # giá low hiện tại (nếu sameTimeframe)
    current_time,               # thời gian hiện tại (nếu sameTimeframe)
    security_data,              # tuple: (topLevel, bottomLevel, leftTime, rightTime) từ request.security
    times,                      # danh sách thời gian (đã sắp xếp)
    highs,                      # danh sách giá high tương ứng
    lows,                       # danh sách giá low tương ứng
    last_bar_time,              # thời gian của thanh cuối (sử dụng cho vẽ)
    time_prev,                  # thời gian của thanh trước đó (để tính delta)
    initialTime                 # thời gian khởi tạo nếu không tìm thấy dữ liệu
):
    # Lấy dữ liệu từ request.security (giả lập)
    sec_topLevel, sec_bottomLevel, sec_leftTime, sec_rightTime = security_data

    # Xác định giá và thời gian dựa trên sameTimeframe
    parsedTop = current_high if sameTimeframe else sec_topLevel
    parsedBottom = current_low if sameTimeframe else sec_bottomLevel
    parsedLeftTime = current_time if sameTimeframe else sec_leftTime
    parsedRightTime = current_time if sameTimeframe else sec_rightTime

    # Nếu cùng timeframe, dùng thời gian hiện tại
    parsedTopTime = current_time
    parsedBottomTime = current_time

    # Nếu không cùng timeframe, thực hiện binary search trên danh sách times
    if not sameTimeframe:
        # Tìm chỉ mục phải của parsedLeftTime và parsedRightTime trong mảng times
        leftIndex = bisect.bisect_right(times, parsedLeftTime) - 1
        rightIndex = bisect.bisect_right(times, parsedRightTime) - 1
        # Lấy mảng con thời gian, giá high và giá low
        timeArray = times[leftIndex:rightIndex+1]
        topArray = highs[leftIndex:rightIndex+1]
        bottomArray = lows[leftIndex:rightIndex+1]
        # Nếu có dữ liệu, xác định thời gian của điểm có giá cao nhất và thấp nhất
        if len(timeArray) > 0:
            max_top = max(topArray)
            idx_max = topArray.index(max_top)
            parsedTopTime = timeArray[idx_max]
            min_bottom = min(bottomArray)
            idx_min = bottomArray.index(min_bottom)
            parsedBottomTime = timeArray[idx_min]
        else:
            parsedTopTime = initialTime
            parsedBottomTime = initialTime

    # Tính toán điểm kết thúc cho các đường: sử dụng last_bar_time + 20*(current_time - time_prev)
    end_time = last_bar_time + 20 * (current_time - time_prev)

    line_style = get_style(style)

    # Vẽ top line
    fig.add_shape(
        type="line",
        x0=parsedTopTime,
        y0=parsedTop,
        x1=end_time,
        y1=parsedTop,
        line=dict(color=levelColor, dash=line_style))
    
    # Vẽ top label (sử dụng add_annotation)
    fig.add_annotation(
        x=end_time,
        y=parsedTop,
        text=f"P{timeframe}H",
        showarrow=True,
        arrowhead=2,
        font=dict(color=levelColor, size=10),
        xanchor="left")

    # Vẽ bottom line
    fig.add_shape(
        type="line",
        x0=parsedBottomTime,
        y0=parsedBottom,
        x1=end_time,
        y1=parsedBottom,
        line=dict(color=levelColor, dash=line_style))
    
    # Vẽ bottom label
    fig.add_annotation(
        x=end_time,
        y=parsedBottom,
        text=f"P{timeframe}L",
        showarrow=True,
        arrowhead=2,
        font=dict(color=levelColor, size=10),
        xanchor="left")

    return fig

def in_seconds(tf):
    try:
        return int(tf)
    except ValueError:
        # Nếu tf không phải là chuỗi số, bạn có thể thêm logic chuyển đổi ở đây
        return None

def higher_timeframe(chart_timeframe, timeframe):
    return in_seconds(chart_timeframe) > in_seconds(timeframe)

def update_trailing_extremes(high, low, current_time, trailing):
    trailing["top"] = max(high, trailing.get("top", high))
    trailing["lastTopTime"] = current_time if trailing["top"] == high else trailing.get("lastTopTime", current_time)
    trailing["bottom"] = min(low, trailing.get("bottom", low))
    trailing["lastBottomTime"] = current_time if trailing["bottom"] == low else trailing.get("lastBottomTime", current_time)
    return trailing

# --- Hàm 1: drawHighLowSwings ---
def draw_high_low_swings(fig, 
                        trailing, 
                        swingTrend, 
                        last_bar_time, 
                        current_time, 
                        previous_time,
                        swingBearishColor, 
                        swingBullishColor):
    # Tính thời gian kết thúc cho các đường
    rightTimeBar = last_bar_time + 20 * (current_time - previous_time)
    
    # Vẽ top line (trailing high)
    fig.add_shape(
        type="line",
        x0=trailing["lastTopTime"],
        y0=trailing["top"],
        x1=rightTimeBar,
        y1=trailing["top"],
        line=dict(color=swingBearishColor),
    )
    # Vẽ top label
    top_text = "Strong High" if swingTrend["bias"] == -1 else "Weak High"
    fig.add_annotation(
        x=rightTimeBar,
        y=trailing["top"],
        text=top_text,
        showarrow=True,
        arrowhead=2,
        font=dict(color=swingBearishColor, size=10),
        xanchor="left"
    )
    
    # Vẽ bottom line (trailing low)
    fig.add_shape(
        type="line",
        x0=trailing["lastBottomTime"],
        y0=trailing["bottom"],
        x1=rightTimeBar,
        y1=trailing["bottom"],
        line=dict(color=swingBullishColor),
    )
    # Vẽ bottom label
    bottom_text = "Strong Low" if swingTrend["bias"] == 1 else "Weak Low"
    fig.add_annotation(
        x=rightTimeBar,
        y=trailing["bottom"],
        text=bottom_text,
        showarrow=True,
        arrowhead=2,
        font=dict(color=swingBullishColor, size=10),
        xanchor="left"
    )
    return fig

# --- Hàm 2: drawZone ---
def draw_zone(fig, 
            trailing, 
            last_bar_time, 
            labelLevel, 
            labelIndex, 
            top, 
            bottom, 
            tag, 
            zoneColor, 
            style = None):
    
    # Vẽ box zone bằng add_shape (loại hình chữ nhật)
    # Giả sử sử dụng trailing["barTime"] làm điểm bên trái và last_bar_time làm bên phải.
    fig.add_shape(
        type="rect",
        x0=trailing["barTime"],
        x1=last_bar_time,
        y0=bottom,
        y1=top,
        line=dict(color="rgba(0,0,0,0)"),
        fillcolor=zoneColor) # Nếu cần hiệu ứng alpha, có thể chuyển đổi sang rgba
        
    # Vẽ nhãn zone bằng add_annotation
    fig.add_annotation(
        x=labelIndex,
        y=labelLevel,
        text=tag,
        showarrow=False,
        font=dict(color=zoneColor, size=10),
        xanchor=("left" if style else "center"))
    
    return fig

# --- Hàm 3: drawPremiumDiscountZones ---
def draw_premium_discount_zones(fig, 
                                trailing, 
                                last_bar_index, 
                                premiumZoneColor, 
                                equilibriumZoneColorInput, 
                                discountZoneColor):
    # Zone Premium: sử dụng trailing.top
    premium_label_index = round(0.5 * (trailing["barIndex"] + last_bar_index))
    premium_top = trailing["top"]
    premium_bottom = 0.95 * trailing["top"] + 0.05 * trailing["bottom"]
    fig = draw_zone(fig, 
                    trailing, 
                    last_bar_time=last_bar_index, 
                    labelLevel=premium_top,
                    labelIndex=premium_label_index, 
                    top=premium_top, 
                    bottom=premium_bottom,
                    tag="Premium", 
                    zoneColor=premiumZoneColor, 
                    style="down")
    
    # Zone Equilibrium
    equilibriumLevel = (trailing["top"] + trailing["bottom"]) / 2
    eq_top = 0.525 * trailing["top"] + 0.475 * trailing["bottom"]
    eq_bottom = 0.525 * trailing["bottom"] + 0.475 * trailing["top"]
    fig = draw_zone(fig, 
                    trailing, 
                    last_bar_time=last_bar_index, 
                    labelLevel=equilibriumLevel,
                    labelIndex=last_bar_index, 
                    top=eq_top, 
                    bottom=eq_bottom,
                    tag="Equilibrium", 
                    zoneColor=equilibriumZoneColorInput, 
                    style="left")
    
    # Zone Discount: sử dụng trailing.bottom
    discount_label_index = round(0.5 * (trailing["barIndex"] + last_bar_index))
    discount_top = 0.95 * trailing["bottom"] + 0.05 * trailing["top"]
    discount_bottom = trailing["bottom"]
    fig = draw_zone(fig, 
                    trailing, 
                    last_bar_time=last_bar_index, 
                    labelLevel=trailing["bottom"],
                    labelIndex=discount_label_index, 
                    top=discount_top, 
                    bottom=discount_bottom,
                    tag="Discount", 
                    zoneColor=discountZoneColor, 
                    style="up")
    return fig

# Hàm main
def main():
    # Thiết lập logging cho cảnh báo
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
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
    current_time = df_filtered.index[-1]
    previous_time = df_filtered.index[-2]
    last_bar_time = df_filtered.index[-2]
    
    open = df_filtered["Open"].iloc[-1]
    last_open = df_filtered["Open"].iloc[-2]
    
    high = df_filtered["High"].iloc[-1]
    last2High = df_filtered["High"].iloc[-3]
    
    low = df_filtered["Low"].iloc[-1]
    last2Low = df_filtered["Low"].iloc[-3]
    
    close= df_filtered["Close"].iloc[-1]
    last_close = df_filtered["Close"].iloc[-2]
    
    bar_index = len(df_filtered) - 1
    
    fairValueGapsTimeframeInput = 1440
    
    # 📌 Cập nhật biến và thực thi
    parsedOpen = open if config.get("show_trend", False) else None
    candleColor = swingBullishColor if internalTrend.bias == BULLISH else swingBearishColor

    # Khởi tạo biểu đồ
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=df_filtered.index,
        open=df_filtered["Open"],
        high=df_filtered["High"],
        low=df_filtered["Low"],
        close=df_filtered["Close"],
        name="AAPL Candlestick",
        # Đoạn này cho màu nến phụ thuộc Bear or Bull
        # CHÚ Ý
        # increasing_line_color=candleColor,
        # decreasing_line_color=candleColor,
        customdata=[parsedOpen] * len(df_filtered)
    ))
    
    # 📌 Cập nhật các điểm Swing High/Low và Premium/Discount Zones nếu bật
    if swing_structure.get("show_high_low_swings", True) or premium_discount_zones.get("show", False):
        fig = update_trailing_extremes(high, low, current_time, trailing)

        if swing_structure.get("show_high_low_swings", True):
            fig = draw_high_low_swings(fig,
                                    trailing,
                                    swingTrend,
                                    last_bar_time,
                                    current_time,
                                    previous_time,
                                    candleColor,
                                    candleColor)

        if premium_discount_zones.get("show", False):
            fig = draw_premium_discount_zones(fig,
                                                trailing,
                                                current_time,
                                                premiumZoneColor,
                                                premium_discount_zones.get("equilibrium_zone_color", GRAY),
                                                discountZoneColor)
    
    # 📌 Xóa Fair Value Gaps nếu bật
    if fair_value_gaps.get("show", False):
        delete_fair_value_gaps(fairValueGaps, low, high)
    
    # 📌 Lấy cấu trúc thị trường
    # GỌI HÀM 2 LẦN ĐỂ HIỂN THỊ SWINGS VÀ INTETER
    atrMeasure = compute_atr(np.array(df_filtered["High"]), 
                            np.array(df_filtered["Low"]), 
                            np.array(df_filtered["Close"]), 
                            200) if len(highs) > 0 else 0
    get_current_structure(swing_structure.get("swings_length", True), 
                            atrMeasure, 
                            False)
    get_current_structure(5, atrMeasure, False, True)
    
    # 📌 Xác định Equal Highs/Lows nếu bật
    
    if equal_highs_lows.get("show", False):
        get_current_structure(equal_highs_lows.get("length",3), atrMeasure, True)
    
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
    swing_box_params = (None, None, None, None, "bar_time", "right")
    internal_box_params = (None, None, None, None, "bar_time", "right")
            
    if not df_filtered.empty:
        if "Close" in df_filtered.columns and not df_filtered["Close"].empty:
                print("showSwingOrderBlocksInput:", showSwingOrderBlocksInput,"\n",
                        "showInternalOrderBlocksInput:", showInternalOrderBlocksInput,"\n",
                        "swingOrderBlocksSizeInput:", swingOrderBlocksSizeInput,"\n",
                        "internalOrderBlocksSizeInput:", internalOrderBlocksSizeInput)
                
                initialize_order_blocks(showSwingOrderBlocksInput, 
                                        showInternalOrderBlocksInput, 
                                        swingOrderBlocksSizeInput, 
                                        internalOrderBlocksSizeInput,
                                        swing_box_params,
                                        internal_box_params)
                print("Order Blocks Initialized")
    else:
        print("⚠️ Cảnh báo: df_filtered rỗng. Không thể khởi tạo Order Blocks.")

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
    highVolatilityBar = is_high_volatility_bar(high, low, volatilityMeasure[-1] if isinstance(volatilityMeasure, np.ndarray) else volatilityMeasure)
    print("highVolatilityBar:" + str(highVolatilityBar))
    
    parsedHigh = low if highVolatilityBar else high
    parsedLow = high if highVolatilityBar else low

    # 📌 Lưu trữ dữ liệu mới vào danh sách
    parsedHighs.append(parsedHigh)
    parsedLows.append(parsedLow)
    highs.append(high)
    lows.append(low)
    times.append(current_time)

    # 📌 Xử lý cấu trúc thị trường nội bộ và Order Blocks
    # GỌI HÀM 2 LẦN ĐỂ HIỂN THỊ SWINGS VÀ INTETER
    if internal_structure.get("show_internals", True) or showInternalOrderBlocksInput or config.get("show_trend", False):
        display_structure(df_filtered["Open"], df_filtered["Close"], fig, internal=True)

    if swing_structure.get("show_structure", True) or showSwingOrderBlocksInput or swing_structure.get("show_high_low_swings", True):
        display_structure(df_filtered["Open"], df_filtered["Close"], fig, internal=False)
        
    # 📌 Xóa Order Blocks nếu có
    if showInternalOrderBlocksInput:
        delete_order_blocks(True)

    if showSwingOrderBlocksInput:
        delete_order_blocks()
        
    # 📌 Vẽ lại Fair Value Gaps nếu bật
    if fair_value_gaps.get("show", False):
        draw_fair_value_gaps(fairValueGaps,
                            fig,
                            fairValueGapsTimeframeInput,
                            fairValueGapsThresholdInput,
                            last_close,
                            last_open,
                            last_bar_time,
                            high,
                            low,
                            current_time,
                            last2High,
                            last2Low,
                            bar_index,
                            fairValueGapBullishColor,
                            fairValueGapBearishColor)

    # Hiển thị biểu đồ với các Equal Highs/Lows và nhãn
    fig.show()
    
if __name__ == "__main__":
    main()