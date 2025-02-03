from dataclasses import dataclass
from typing import List, Optional
import numpy as np
import math

# # 📌 Định nghĩa màu sắc
# GREEN = "#089981"
# RED = "#F23645"
# BLUE = "#2157f3"
# GRAY = "#878b94"
# MONO_BULLISH = "#b2b5be"
# MONO_BEARISH = "#5d606b"

# 📌 Định nghĩa kiểu đường nét
# SOLID = "⎯⎯⎯"
# DASHED = "----"
# DOTTED = "····"

# # 📌 Constants (định nghĩa giá trị Bearish/Bullish Leg)
# BULLISH_LEG = 1
# BEARISH_LEG = 0

# # 📌 Cấu hình chung
# config = {
#     "mode": "Historical",
#     "style": "Colored",
#     "show_trend": False
# }

# # 📌 Cấu hình Internal Structure
# internal_structure = {
#     "show_internals": True,
#     "bullish_structure": "All",
#     "bullish_color": GREEN,
#     "bearish_structure": "All",
#     "bearish_color": RED,
#     "internal_filter_confluence": False,
#     "label_size": "tiny"
# }

# # 📌 Cấu hình Swing Structure
# swing_structure = {
#     "show_structure": True,
#     "bullish_structure": "All",
#     "bullish_color": GREEN,
#     "bearish_structure": "All",
#     "bearish_color": RED,
#     "swing_label_size": "small",
#     "show_swings": False,
#     "swings_length": 50,
#     "show_high_low_swings": True
# }

# # 📌 Cấu hình Order Blocks
# order_blocks = {
#     "show_internal_order_blocks": True,
#     "internal_order_blocks_size": 5,
#     "show_swing_order_blocks": False,
#     "swing_order_blocks_size": 5,
#     "order_block_filter": "Atr",
#     "order_block_mitigation": "High/Low",
#     "internal_bullish_color": "#3179f5",
#     "internal_bearish_color": "#f77c80",
#     "swing_bullish_color": "#1848cc",
#     "swing_bearish_color": "#b22833"
# }

# # 📌 Cấu hình Equal Highs/Lows
# equal_highs_lows = {
#     "show": True,
#     "length": 3,
#     "threshold": 0.1,
#     "label_size": "tiny"
# }

# # 📌 Cấu hình Fair Value Gaps
# fair_value_gaps = {
#     "show": False,
#     "auto_threshold": True,
#     "timeframe": "",
#     "bullish_color": "#00ff68",
#     "bearish_color": "#ff0008",
#     "extend_bars": 1
# }

# # 📌 Cấu hình Highs & Lows MTF
# highs_lows_mtf = {
#     "show_daily": False,
#     "daily_style": SOLID,
#     "daily_color": BLUE,
#     "show_weekly": False,
#     "weekly_style": SOLID,
#     "weekly_color": BLUE,
#     "show_monthly": False,
#     "monthly_style": SOLID,
#     "monthly_color": BLUE
# }

# # 📌 Cấu hình Premium & Discount Zones
# premium_discount_zones = {
#     "show": False,
#     "premium_zone_color": RED,
#     "equilibrium_zone_color": GRAY,
#     "discount_zone_color": GREEN
# }

# # 📌 Tổng hợp tất cả cấu hình vào dictionary chính
# settings = {
#     "config": config,
#     "internal_structure": internal_structure,
#     "swing_structure": swing_structure,
#     "order_blocks": order_blocks,
#     "equal_highs_lows": equal_highs_lows,
#     "fair_value_gaps": fair_value_gaps,
#     "highs_lows_mtf": highs_lows_mtf,
#     "premium_discount_zones": premium_discount_zones
# }

# 📌 Xuất settings ra để sử dụng trong bot
print(settings)

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

# # 📌 Định nghĩa cấu trúc cực trị (Trailing Extremes)
# @dataclass
# class TrailingExtremes:
#     top: Optional[float] = None
#     bottom: Optional[float] = None
#     barTime: Optional[int] = None
#     barIndex: Optional[int] = None
#     lastTopTime: Optional[int] = None
#     lastBottomTime: Optional[int] = None

# # 📌 Định nghĩa Fair Value Gap
# @dataclass
# class FairValueGap:
#     top: float
#     bottom: float
#     bias: int  # BULLISH (+1) hoặc BEARISH (-1)
#     topBox: Optional[object] = None
#     bottomBox: Optional[object] = None

# # 📌 Định nghĩa xu hướng (Trend)
# @dataclass
# class Trend:
#     bias: int  # BULLISH (+1) hoặc BEARISH (-1)

# # 📌 Định nghĩa cấu trúc hiển thị Equal Highs/Lows
# @dataclass
# class EqualDisplay:
#     line: Optional[object] = None
#     label: Optional[object] = None

# # 📌 Định nghĩa Pivot Point (Swing Point)
# @dataclass
# class Pivot:
#     currentLevel: Optional[float] = None
#     lastLevel: Optional[float] = None
#     crossed: bool = False
#     barTime: Optional[int] = None
#     barIndex: Optional[int] = None

# # 📌 Định nghĩa Order Block
# @dataclass
# class OrderBlock:
#     barHigh: float
#     barLow: float
#     barTime: int
#     bias: int  # BULLISH (+1) hoặc BEARISH (-1)

# # 📌 Biến toàn cục
# swingHigh = Pivot()
# swingLow = Pivot()
# internalHigh = Pivot()
# internalLow = Pivot()
# equalHigh = Pivot()
# equalLow = Pivot()
# swingTrend = Trend(0)
# internalTrend = Trend(0)
# equalHighDisplay = EqualDisplay()
# equalLowDisplay = EqualDisplay()

# equalHighsLowsThresholdInput = 0.1  
# showSwingsInput = True  
# internalFilterConfluenceInput = False  
# fairValueGapsThresholdInput = 0.05  
# showSwingOrderBlocksInput = True  
# showInternalOrderBlocksInput = True  
# swingOrderBlocksSizeInput = 5 
# fairValueGapsExtendInput = 1 

# # 📌 Danh sách chứa dữ liệu
# fairValueGaps: List[FairValueGap] = []
# parsedHighs: List[float] = []
# parsedLows: List[float] = []
# highs: List[float] = []
# lows: List[float] = []
# times: List[int] = []
# trailing = TrailingExtremes()
# swingOrderBlocks: List[OrderBlock] = []
# internalOrderBlocks: List[OrderBlock] = []
# swingOrderBlocksBoxes: List[object] = []  # Giả định hộp giá trị sẽ được hiển thị bằng thư viện khác
# internalOrderBlocksBoxes: List[object] = []

# 📌 Xác định màu sắc theo phong cách
styleInput = "Colored"
MONOCHROME = "Monochrome"
MONO_BULLISH = "#b2b5be"
MONO_BEARISH = "#5d606b"

swingBullishColor = MONO_BULLISH if styleInput == MONOCHROME else "#089981"
swingBearishColor = MONO_BEARISH if styleInput == MONOCHROME else "#F23645"
fairValueGapBullishColor = MONO_BULLISH if styleInput == MONOCHROME else "#00ff68"
fairValueGapBearishColor = MONO_BEARISH if styleInput == MONOCHROME else "#ff0008"
premiumZoneColor = MONO_BEARISH if styleInput == MONOCHROME else "#F23645"
discountZoneColor = MONO_BULLISH if styleInput == MONOCHROME else "#089981"

# # 📌 Chỉ số thanh hiện tại
# currentBarIndex = 0
# lastBarIndex = 0

# 📌 Cảnh báo trong thanh hiện tại
currentAlerts = Alerts()

# # 📌 Thời gian ban đầu của biểu đồ
# initialTime = 0  # Cần cập nhật từ dữ liệu thực tế

# 📌 Tạo hộp hiển thị order blocks khi lần đầu khởi chạy
def initialize_order_blocks(showSwingOrderBlocks, showInternalOrderBlocks, swingOrderBlocksSize, internalOrderBlocksSize):
    if showSwingOrderBlocks:
        for _ in range(swingOrderBlocksSize):
            swingOrderBlocksBoxes.append(None)  # Giả lập hộp giá trị
    if showInternalOrderBlocks:
        for _ in range(internalOrderBlocksSize):
            internalOrderBlocksBoxes.append(None)

# # 📌 Thiết lập nguồn dữ liệu cho Order Block Mitigation
# orderBlockMitigationInput = "High/Low"
# CLOSE = "Close"
# HIGH = "High"
# LOW = "Low"

# bearishOrderBlockMitigationSource = HIGH if orderBlockMitigationInput == CLOSE else HIGH
# bullishOrderBlockMitigationSource = LOW if orderBlockMitigationInput == CLOSE else LOW

# # Example function that computes ATR
# # Ensure `highs`, `lows`, and `closes` are numpy arrays before calling this function
# def compute_atr(highs, lows, closes, period=200):
#     if len(highs) < period or len(lows) < period or len(closes) < period:
#         return None  # Prevents error if not enough data
    
#     tr = np.maximum(highs - lows, np.maximum(abs(highs - np.roll(closes, 1)), abs(lows - np.roll(closes, 1))))
#     atr = np.convolve(tr, np.ones(period)/period, mode='valid')
#     return atr[-1] if len(atr) > 0 else None

# # Khởi tạo các biến cần thiết
# atrMeasure = compute_atr(np.array(highs), np.array(lows), np.array(closes), 200) if len(highs) > 0 else 0

# # 📌 Đo lường độ biến động
# volatilityMeasure = compute_atr(np.array(highs), np.array(lows), np.array(highs), 200)  # ATR mặc định
# ATR = "Atr"
# RANGE = "Cumulative Mean Range"

# orderBlockFilterInput = ATR
# volatilityMeasure = compute_atr(np.array(highs), np.array(lows), np.array(highs), 200) if orderBlockFilterInput == ATR else np.cumsum(np.abs(np.array(highs) - np.array(lows))) / (currentBarIndex + 1)

# # 📌 Xác định thanh có độ biến động cao
# def is_high_volatility_bar(high, low, volatilityMeasure):
#     return (high - low) >= (2 * volatilityMeasure)

# # 📌 Lấy giá cao/thấp đã xử lý
# highVolatilityBar = is_high_volatility_bar(1.2, 1.0, volatilityMeasure)  # Ví dụ
# parsedHigh = 1.0 if highVolatilityBar else 1.2
# parsedLow = 1.2 if highVolatilityBar else 1.0

# # 📌 Lưu trữ dữ liệu mới vào danh sách
# parsedHighs.append(parsedHigh)
# parsedLows.append(parsedLow)
# highs.append(1.2)  # Dữ liệu giả lập
# lows.append(1.0)
# times.append(100)  # Cần lấy từ dữ liệu thực tế

# # 📌 Hàm lấy giá trị của current leg (bearish = 0, bullish = 1)
# def leg(size, highs, lows):
#     """
#     Xác định giá trị leg hiện tại (0: bearish, 1: bullish)
    
#     :param size: (int) Độ dài của cửa sổ kiểm tra
#     :param highs: (list) Danh sách giá cao (high)
#     :param lows: (list) Danh sách giá thấp (low)
#     :return: (int) 0 nếu Bearish, 1 nếu Bullish
#     """
#     if len(highs) < size or len(lows) < size:
#         return None  # Tránh lỗi khi không đủ dữ liệu

#     highest_high = max(highs[-size:])  # Tìm giá cao nhất trong cửa sổ
#     lowest_low = min(lows[-size:])  # Tìm giá thấp nhất trong cửa sổ

#     new_leg_high = highs[-1] > highest_high
#     new_leg_low = lows[-1] < lowest_low

#     if new_leg_high:
#         return BEARISH_LEG
#     elif new_leg_low:
#         return BULLISH_LEG
#     return 0  # Nếu không có thay đổi, giữ nguyên giá trị cũ

# # 📌 Hàm kiểm tra có phải điểm bắt đầu của leg mới hay không
# def start_of_new_leg(leg_values):
#     """
#     Xác định xem có phải điểm bắt đầu của leg mới không
    
#     :param leg_values: (list) Danh sách các giá trị leg
#     :return: (bool) True nếu có thay đổi leg
#     """
#     if len(leg_values) < 2:
#         return False  # Không có đủ dữ liệu để so sánh
    
#     return leg_values[-1] != leg_values[-2]

# # 📌 Hàm kiểm tra có phải điểm bắt đầu của Bearish Leg (Swing Down)
# def start_of_bearish_leg(leg_values):
#     """
#     Xác định xem có phải điểm bắt đầu của một bearish leg không
    
#     :param leg_values: (list) Danh sách các giá trị leg
#     :return: (bool) True nếu có sự thay đổi từ bullish → bearish
#     """
#     if len(leg_values) < 2:
#         return False
    
#     return (leg_values[-2] == BULLISH_LEG) and (leg_values[-1] == BEARISH_LEG)

# # 📌 Hàm kiểm tra có phải điểm bắt đầu của Bullish Leg (Swing Up)
# def start_of_bullish_leg(leg_values):
#     """
#     Xác định xem có phải điểm bắt đầu của một bullish leg không
    
#     :param leg_values: (list) Danh sách các giá trị leg
#     :return: (bool) True nếu có sự thay đổi từ bearish → bullish
#     """
#     if len(leg_values) < 2:
#         return False
    
#     return (leg_values[-2] == BEARISH_LEG) and (leg_values[-1] == BULLISH_LEG)

# # 📌 Định nghĩa cấu trúc Equal Display để lưu label và line
# @dataclass
# class EqualDisplay:
#     line: Optional[object] = None
#     label: Optional[object] = None

# # 📌 Biến lưu nhãn Equal Highs & Lows
# equalHighDisplay = EqualDisplay()
# equalLowDisplay = EqualDisplay()

# # 📌 Hàm vẽ nhãn trên biểu đồ
# def draw_label(label_time, label_price, tag, label_color, label_style, mode="Present"):
#     """
#     Tạo một nhãn mới trên biểu đồ.

#     :param label_time: (int) Thời gian (trục X)
#     :param label_price: (float) Giá (trục Y)
#     :param tag: (str) Nội dung nhãn
#     :param label_color: (str) Màu chữ
#     :param label_style: (str) Kiểu nhãn
#     :param mode: (str) Chế độ hiển thị ("Historical" hoặc "Present")
#     :return: (object) ID của nhãn (giả lập)
#     """
#     # Nếu ở chế độ "Present", xóa nhãn cũ trước khi vẽ
#     if mode == "Present":
#         label_id = None  # Xóa nhãn cũ

#     # Giả lập tạo nhãn trên biểu đồ
#     label_id = {
#         "time": label_time,
#         "price": label_price,
#         "text": tag,
#         "color": label_color,
#         "style": label_style,
#         "size": "small"
#     }
    
#     return label_id

# # 📌 Hàm vẽ Equal High hoặc Equal Low
# def draw_equal_high_low(pivot, level, size, equal_high, mode="Present"):
#     """
#     Vẽ Equal High (EQH) hoặc Equal Low (EQL) trên biểu đồ.

#     :param pivot: (Pivot) Điểm pivot bắt đầu
#     :param level: (float) Mức giá của pivot hiện tại
#     :param size: (int) Khoảng cách từ pivot đến điểm hiện tại (số thanh nến)
#     :param equal_high: (bool) True nếu là EQH, False nếu là EQL
#     :param mode: (str) Chế độ hiển thị ("Historical" hoặc "Present")
#     :return: (dict) Thông tin về line & label đã vẽ
#     """
#     # Chọn Equal Display thích hợp
#     equal_display = equalHighDisplay if equal_high else equalLowDisplay

#     # Xác định thuộc tính
#     tag = "EQH" if equal_high else "EQL"
#     equal_color = "#F23645" if equal_high else "#089981"  # Màu swingBearishColor hoặc swingBullishColor
#     label_style = "label_down" if equal_high else "label_up"

#     # Nếu ở chế độ "Present", xóa line & label cũ
#     if mode == "Present":
#         equal_display.line = None
#         equal_display.label = None

#     # Vẽ đường Equal High/Low
#     equal_display.line = {
#         "start_time": pivot.barTime,
#         "start_price": pivot.currentLevel,
#         "end_time": size,
#         "end_price": level,
#         "style": "dotted",
#         "color": equal_color
#     }

#     # Vị trí hiển thị nhãn
#     label_position = math.round(0.5 * (pivot.barIndex + size))
    
#     # Vẽ nhãn EQH/EQL
#     equal_display.label = {
#         "time": None,
#         "price": level,
#         "text": tag,
#         "color": equal_color,
#         "style": label_style,
#         "size": "small",
#         "position": label_position
#     }
    
#     return {"line": equal_display.line, "label": equal_display.label}


# # 📌 Hàm xác định cấu trúc hiện tại và điểm xoay (swing points)
# def get_current_structure(size, equal_high_low=False, internal=False):
#     """
#     Lưu trữ cấu trúc hiện tại và trailing swing points.
    
#     :param size: (int) Kích thước cấu trúc
#     :param equal_high_low: (bool) Hiển thị Equal Highs/Lows
#     :param internal: (bool) Xác định cấu trúc nội bộ
#     """
#     current_leg = leg(size)  # Xác định trạng thái leg
#     new_pivot = start_of_new_leg([current_leg])  # Kiểm tra điểm xoay mới
#     pivot_low = start_of_bullish_leg([current_leg])  # Kiểm tra bullish pivot
#     pivot_high = start_of_bearish_leg([current_leg])  # Kiểm tra bearish pivot

#     if new_pivot:
#         if pivot_low:
#             p_ivot = equalLow if equal_high_low else internalLow if internal else swingLow

#             # Kiểm tra và vẽ Equal Low
#             if equal_high_low and abs(p_ivot.currentLevel - lows[size]) < equalHighsLowsThresholdInput * atrMeasure:
#                 draw_equal_high_low(p_ivot, lows[size], size, False)

#             # Cập nhật pivot point
#             p_ivot.lastLevel = p_ivot.currentLevel
#             p_ivot.currentLevel = lows[size]
#             p_ivot.crossed = False
#             p_ivot.barTime = times[size]
#             p_ivot.barIndex = size  # Trong Pine Script: `bar_index[size]`

#             # Cập nhật thông tin trailing bottom nếu không phải internal hoặc equal high/low
#             if not equal_high_low and not internal:
#                 trailing.bottom = p_ivot.currentLevel
#                 trailing.barTime = p_ivot.barTime
#                 trailing.barIndex = p_ivot.barIndex
#                 trailing.lastBottomTime = p_ivot.barTime

#             # Hiển thị swing points nếu được bật
#             if showSwingsInput and not internal and not equal_high_low:
#                 draw_label(
#                     times[size],
#                     p_ivot.currentLevel,
#                     "LL" if p_ivot.currentLevel < p_ivot.lastLevel else "HL",
#                     swingBullishColor,
#                     "label_up"
#                 )

#         else:
#             p_ivot = equalHigh if equal_high_low else internalHigh if internal else swingHigh

#             # Kiểm tra và vẽ Equal High
#             if equal_high_low and abs(p_ivot.currentLevel - highs[size]) < equalHighsLowsThresholdInput * atrMeasure:
#                 draw_equal_high_low(p_ivot, highs[size], size, True)

#             # Cập nhật pivot point
#             p_ivot.lastLevel = p_ivot.currentLevel
#             p_ivot.currentLevel = highs[size]
#             p_ivot.crossed = False
#             p_ivot.barTime = times[size]
#             p_ivot.barIndex = size  # Trong Pine Script: `bar_index[size]`

#             # Cập nhật thông tin trailing top nếu không phải internal hoặc equal high/low
#             if not equal_high_low and not internal:
#                 trailing.top = p_ivot.currentLevel
#                 trailing.barTime = p_ivot.barTime
#                 trailing.barIndex = p_ivot.barIndex
#                 trailing.lastTopTime = p_ivot.barTime

#             # Hiển thị swing points nếu được bật
#             if showSwingsInput and not internal and not equal_high_low:
#                 draw_label(
#                     times[size],
#                     p_ivot.currentLevel,
#                     "HH" if p_ivot.currentLevel > p_ivot.lastLevel else "LH",
#                     swingBearishColor,
#                     "label_down"
#                 )

# # 📌 Hàm vẽ đường và nhãn đại diện cho một cấu trúc
# def draw_structure(pivot, tag, structure_color, line_style, label_style, label_size, mode="Present"):
#     """
#     Vẽ đường và nhãn đại diện cho một cấu trúc.

#     :param pivot: (Pivot) Điểm pivot cơ sở
#     :param tag: (str) Văn bản hiển thị trên nhãn
#     :param structure_color: (str) Màu sắc của cấu trúc
#     :param line_style: (str) Kiểu đường
#     :param label_style: (str) Kiểu nhãn
#     :param label_size: (str) Cỡ chữ
#     :param mode: (str) Chế độ hiển thị ("Historical" hoặc "Present")
#     :return: (dict) ID của nhãn đã vẽ
#     """
#     if mode == "Present":
#         line_id, label_id = None, None  # Xóa đường và nhãn cũ

#     # Vẽ đường cấu trúc
#     line_id = {
#         "start_time": pivot.barTime,
#         "start_price": pivot.currentLevel,
#         "end_time": "current_time",  # Placeholder cho thời gian hiện tại
#         "end_price": pivot.currentLevel,
#         "style": line_style,
#         "color": structure_color
#     }

#     # Vị trí hiển thị nhãn
#     label_position = math.floor(0.5 * (pivot.barIndex + currentBarIndex))

#     # Vẽ nhãn
#     label_id = {
#         "time": None,
#         "price": pivot.currentLevel,
#         "text": tag,
#         "color": structure_color,
#         "style": label_style,
#         "size": label_size,
#         "position": label_position
#     }

#     return {"line": line_id, "label": label_id}

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

        if bearishOrderBlockMitigationSource > each_order_block.barHigh and each_order_block.bias == BEARISH_LEG:
            crossed_order_block = True
        elif bullishOrderBlockMitigationSource < each_order_block.barLow and each_order_block.bias == BULLISH_LEG:
            crossed_order_block = True

        if crossed_order_block:
            order_blocks.pop(index)


# 📌 Hàm lưu Order Blocks
def store_order_block(pivot, internal=False, bias=BULLISH_LEG):
    """
    Lưu trữ Order Blocks mới.

    :param pivot: (Pivot) Điểm pivot cơ sở
    :param internal: (bool) True nếu là Internal Order Blocks
    :param bias: (int) BULLISH (+1) hoặc BEARISH (-1)
    """
    if (not internal and showSwingOrderBlocksInput) or (internal and showInternalOrderBlocksInput):
        order_blocks = internalOrderBlocks if internal else swingOrderBlocks

        # Kiểm tra xem pivot.barIndex có hợp lệ không
        if pivot.barIndex is None or pivot.barIndex >= len(parsedHighs) or pivot.barIndex >= len(parsedLows):
            print("Invalid pivot data to compute Order Block")
            return  # Bỏ qua nếu không đủ dữ liệu

        # Xác định chỉ mục `parsed_index`
        if bias == BEARISH_LEG:
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



# 📌 Hàm vẽ Order Blocks dưới dạng hộp (box)
def draw_order_blocks(internal=False):
    """
    Vẽ Order Blocks dưới dạng hộp.

    :param internal: (bool) True nếu là Internal Order Blocks
    """
    order_blocks = internalOrderBlocks if internal else swingOrderBlocks
    order_blocks_size = len(order_blocks)

    if order_blocks_size > 0:
        max_order_blocks = internalOrderBlocksSizeInput if internal else swingOrderBlocksSizeInput
        parsed_order_blocks = order_blocks[: min(max_order_blocks, order_blocks_size)]
        boxes = internalOrderBlocksBoxes if internal else swingOrderBlocksBoxes

        for index, each_order_block in enumerate(parsed_order_blocks):
            order_block_color = (
                MONO_BEARISH if each_order_block.bias == BEARISH else MONO_BULLISH
                if styleInput == MONOCHROME
                else internalBearishOrderBlockColor
                if internal and each_order_block.bias == BEARISH
                else internalBullishOrderBlockColor
                if internal
                else swingBearishOrderBlockColor
                if each_order_block.bias == BEARISH
                else swingBullishOrderBlockColor
            )

            boxes[index] = {
                "top_left": (each_order_block.barTime, each_order_block.barHigh),
                "bottom_right": ("last_bar_time", each_order_block.barLow),
                "border_color": None if internal else order_block_color,
                "bgcolor": order_block_color,
            }


# 📌 Hàm phát hiện và vẽ cấu trúc, đồng thời lưu trữ Order Blocks
def display_structure(internal=False):
    """
    Phát hiện và vẽ cấu trúc, đồng thời lưu Order Blocks.

    :param internal: (bool) True nếu là cấu trúc nội bộ
    """
    bullish_bar, bearish_bar = True, True

    if internalFilterConfluenceInput:
        bullish_bar = highs[-1] - max(closes[-1], opens[-1]) > min(closes[-1], opens[-1] - lows[-1])
        bearish_bar = highs[-1] - max(closes[-1], opens[-1]) < min(closes[-1], opens[-1] - lows[-1])

    pivot = internalHigh if internal else swingHigh
    trend = internalTrend if internal else swingTrend

    line_style = "dashed" if internal else "solid"
    label_size = internalStructureSize if internal else swingStructureSize
    extra_condition = internal and internalHigh.currentLevel != swingHigh.currentLevel and bullish_bar
    bullish_color = MONO_BULLISH if styleInput == MONOCHROME else internalBullColorInput if internal else swingBullColorInput

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

        if showStructureInput:
            draw_structure(pivot, tag, bullish_color, line_style, "label_down", label_size)

        if (internal and showInternalOrderBlocksInput) or (not internal and showSwingOrderBlocksInput):
            store_order_block(pivot, internal, BULLISH)

    pivot = internalLow if internal else swingLow
    extra_condition = internal and internalLow.currentLevel != swingLow.currentLevel and bearish_bar
    bearish_color = MONO_BEARISH if styleInput == MONOCHROME else internalBearColorInput if internal else swingBearColorInput

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

        if showStructureInput:
            draw_structure(pivot, tag, bearish_color, line_style, "label_up", label_size)

        if (internal and showInternalOrderBlocksInput) or (not internal and showSwingOrderBlocksInput):
            store_order_block(pivot, internal, BEARISH)

# 📌 Hàm vẽ Fair Value Gap Box
def fair_value_gap_box(left_time, right_time, top_price, bottom_price, box_color):
    """
    Vẽ hộp đại diện cho Fair Value Gap (FVG).

    :param left_time: (int) Thời gian bên trái
    :param right_time: (int) Thời gian bên phải
    :param top_price: (float) Giá trên
    :param bottom_price: (float) Giá dưới
    :param box_color: (str) Màu của hộp
    :return: (dict) ID của hộp
    """
    return {
        "top_left": (left_time, top_price),
        "bottom_right": (right_time + fairValueGapsExtendInput * (times[-1] - times[-2]), bottom_price),
        "color": box_color
    }


# 📌 Hàm xóa Fair Value Gaps
def delete_fair_value_gaps():
    """
    Xóa các Fair Value Gaps nếu giá phá vỡ.
    """
    for index, each_fvg in enumerate(fairValueGaps):
        if (lows[-1] < each_fvg.bottom and each_fvg.bias == BULLISH_LEG) or (highs[-1] > each_fvg.top and each_fvg.bias == BEARISH_LEG):
            fairValueGaps.pop(index)


# 📌 Hàm vẽ Fair Value Gaps
def draw_fair_value_gaps():
    """
    Vẽ Fair Value Gaps trên biểu đồ.
    """
    last_close, last_open, last_time, current_high, current_low, current_time, last2_high, last2_low = [
        closes[-2], opens[-2], times[-2], highs[-1], lows[-1], times[-1], highs[-3], lows[-3]
    ]

    bar_delta_percent = (last_close - last_open) / (last_open * 100)
    new_timeframe = timeframe_change(fairValueGapsTimeframeInput)
    threshold = fairValueGapsThresholdInput if new_timeframe else 0

    bullish_fvg = current_low > last2_high and last_close > last2_high and bar_delta_percent > threshold and new_timeframe
    bearish_fvg = current_high < last2_low and last_close < last2_low and -bar_delta_percent > threshold and new_timeframe

    if bullish_fvg:
        currentAlerts.bullishFairValueGap = True
        fairValueGaps.insert(0, {
            "top": last2_high,
            "bottom": current_low,
            "bias": BULLISH,
            "top_box": fair_value_gap_box(last_time, current_time, current_low, (current_low + last2_high) / 2, fairValueGapBullishColor),
            "bottom_box": fair_value_gap_box(last_time, current_time, (current_low + last2_high) / 2, last2_high, fairValueGapBullishColor)
        })

    if bearish_fvg:
        currentAlerts.bearishFairValueGap = True
        fairValueGaps.insert(0, {
            "top": current_high,
            "bottom": last2_low,
            "bias": BEARISH,
            "top_box": fair_value_gap_box(last_time, current_time, current_high, (current_high + last2_low) / 2, fairValueGapBearishColor),
            "bottom_box": fair_value_gap_box(last_time, current_time, (current_high + last2_low) / 2, last2_low, fairValueGapBearishColor)
        })


# 📌 Hàm lấy kiểu đường từ chuỗi
def get_style(style):
    """
    Lấy kiểu đường từ chuỗi.

    :param style: (str) Kiểu đường
    :return: (str) Kiểu đường
    """
    styles = {
        "SOLID": "solid",
        "DASHED": "dashed",
        "DOTTED": "dotted"
    }
    return styles.get(style, "solid")


# 📌 Hàm vẽ MultiTimeFrame Levels
def draw_levels(timeframe, same_timeframe, style, level_color):
    """
    Vẽ các mức MTF (MultiTimeFrame Levels).

    :param timeframe: (str) Khung thời gian
    :param same_timeframe: (bool) True nếu khung thời gian giống nhau
    :param style: (str) Kiểu đường
    :param level_color: (str) Màu sắc
    """
    top_level, bottom_level, left_time, right_time = highs[-2], lows[-2], times[-2], times[-1]

    parsed_top = highs[-1] if same_timeframe else top_level
    parsed_bottom = lows[-1] if same_timeframe else bottom_level

    parsed_left_time = times[-1] if same_timeframe else left_time
    parsed_right_time = times[-1] if same_timeframe else right_time

    # Vẽ đường và nhãn trên biểu đồ
    top_line = {"start": (parsed_left_time, parsed_top), "end": (parsed_right_time, parsed_top), "style": get_style(style), "color": level_color}
    bottom_line = {"start": (parsed_left_time, parsed_bottom), "end": (parsed_right_time, parsed_bottom), "style": get_style(style), "color": level_color}
    
    return {"top_line": top_line, "bottom_line": bottom_line}


# 📌 Hàm kiểm tra xem khung thời gian hiện tại có cao hơn không
def higher_timeframe(timeframe):
    """
    Kiểm tra xem khung thời gian hiện tại có cao hơn khung thời gian được cung cấp không.

    :param timeframe: (str) Khung thời gian
    :return: (bool) True nếu cao hơn, False nếu thấp hơn hoặc bằng
    """
    return timeframe_in_seconds(timeframe) > timeframe_in_seconds()


# 📌 Hàm cập nhật các điểm swing
def update_trailing_extremes():
    """
    Cập nhật các điểm swing cao/thấp.
    """
    trailing.top = max(highs[-1], trailing.top)
    trailing.lastTopTime = times[-1] if trailing.top == highs[-1] else trailing.lastTopTime
    trailing.bottom = min(lows[-1], trailing.bottom)
    trailing.lastBottomTime = times[-1] if trailing.bottom == lows[-1] else trailing.lastBottomTime


# 📌 Hàm vẽ Swing High/Low
def draw_high_low_swings():
    """
    Vẽ các điểm Swing High/Low.
    """
    right_time_bar = times[-1] + 20 * (times[-1] - times[-2])

    top_line = {
        "start": (trailing.lastTopTime, trailing.top),
        "end": (right_time_bar, trailing.top),
        "color": swingBearishColor
    }

    bottom_line = {
        "start": (trailing.lastBottomTime, trailing.bottom),
        "end": (right_time_bar, trailing.bottom),
        "color": swingBullishColor
    }

    top_label = {
        "position": (right_time_bar, trailing.top),
        "text": "Strong High" if swingTrend.bias == BEARISH else "Weak High",
        "color": swingBearishColor
    }

    bottom_label = {
        "position": (right_time_bar, trailing.bottom),
        "text": "Strong Low" if swingTrend.bias == BULLISH else "Weak Low",
        "color": swingBullishColor
    }

    return {"top_line": top_line, "bottom_line": bottom_line, "top_label": top_label, "bottom_label": bottom_label}

import math

# 📌 Hàm vẽ vùng giá với nhãn và hộp
def draw_zone(label_level, label_index, top, bottom, tag, zone_color, style):
    """
    Vẽ vùng giá với nhãn và hộp.

    :param label_level: (float) Mức giá cho nhãn
    :param label_index: (int) Vị trí thanh nến cho nhãn
    :param top: (float) Giá trên của hộp
    :param bottom: (float) Giá dưới của hộp
    :param tag: (str) Nội dung hiển thị trên nhãn
    :param zone_color: (str) Màu của vùng giá
    :param style: (str) Kiểu nhãn
    """
    # Tạo hộp vùng giá
    box_data = {
        "top_left": (trailing.barTime, top),
        "bottom_right": ("last_bar_time", bottom),
        "color": zone_color
    }

    # Tạo nhãn vùng giá
    label_data = {
        "position": (None, label_index, label_level),
        "text": tag,
        "color": zone_color,
        "style": style,
        "size": "small"
    }

    return {"box": box_data, "label": label_data}


# 📌 Hàm vẽ vùng Premium/Discount
def draw_premium_discount_zones():
    """
    Vẽ vùng Premium, Discount, và Equilibrium trên biểu đồ.
    """
    last_bar_index = "last_bar_index"  # Placeholder cho chỉ số thanh nến hiện tại

    # Vẽ vùng Premium
    premium_zone = draw_zone(
        trailing.top,
        math.round(0.5 * (trailing.barIndex + last_bar_index)),
        trailing.top,
        0.95 * trailing.top + 0.05 * trailing.bottom,
        "Premium",
        premiumZoneColor,
        "label_down"
    )

    # Xác định mức Equilibrium
    equilibrium_level = (trailing.top + trailing.bottom) / 2

    # Vẽ vùng Equilibrium
    equilibrium_zone = draw_zone(
        equilibrium_level,
        last_bar_index,
        0.525 * trailing.top + 0.475 * trailing.bottom,
        0.525 * trailing.bottom + 0.475 * trailing.top,
        "Equilibrium",
        equilibriumZoneColorInput,
        "label_left"
    )

    # Vẽ vùng Discount
    discount_zone = draw_zone(
        trailing.bottom,
        math.round(0.5 * (trailing.barIndex + last_bar_index)),
        0.95 * trailing.bottom + 0.05 * trailing.top,
        trailing.bottom,
        "Discount",
        discountZoneColor,
        "label_up"
    )

    return {
        "premium_zone": premium_zone,
        "equilibrium_zone": equilibrium_zone,
        "discount_zone": discount_zone
    }

# 📌 Xác định màu của nến dựa trên xu hướng
parsed_open = opens[-1] if showTrendInput else None
candle_color = swingBullishColor if internalTrend.bias == BULLISH else swingBearishColor

# 📌 Vẽ nến có màu theo xu hướng
plot_candle = {
    "open": parsed_open,
    "high": highs[-1],
    "low": lows[-1],
    "close": closes[-1],
    "color": candle_color,
    "wick_color": candle_color,
    "border_color": candle_color
}

# 📌 Cập nhật Swing High/Low và Premium/Discount Zones nếu được bật
if showHighLowSwingsInput or showPremiumDiscountZonesInput:
    update_trailing_extremes()

    if showHighLowSwingsInput:
        draw_high_low_swings()

    if showPremiumDiscountZonesInput:
        draw_premium_discount_zones()

# 📌 Xóa Fair Value Gaps nếu được bật
if showFairValueGapsInput:
    delete_fair_value_gaps()

# 📌 Lấy cấu trúc thị trường
get_current_structure(swingsLengthInput, False)
get_current_structure(5, False, True)

# 📌 Xác định Equal Highs/Lows nếu được bật
if showEqualHighsLowsInput:
    get_current_structure(equalHighsLowsLengthInput, True)

# 📌 Xử lý cấu trúc thị trường nội bộ và Order Blocks
if showInternalsInput or showInternalOrderBlocksInput or showTrendInput:
    display_structure(True)

if showStructureInput or showSwingOrderBlocksInput or showHighLowSwingsInput:
    display_structure()

# 📌 Xóa Order Blocks nếu có
if showInternalOrderBlocksInput:
    delete_order_blocks(True)

if showSwingOrderBlocksInput:
    delete_order_blocks()

# 📌 Vẽ lại Fair Value Gaps nếu được bật
if showFairValueGapsInput:
    draw_fair_value_gaps()

# 📌 Xử lý các Order Blocks cuối cùng khi hết dữ liệu lịch sử hoặc đang cập nhật thời gian thực
if is_last_confirmed_history() or is_last_bar():
    if showInternalOrderBlocksInput:
        draw_order_blocks(True)

    if showSwingOrderBlocksInput:
        draw_order_blocks()

# 📌 Cập nhật thanh cuối cùng
lastBarIndex = currentBarIndex
currentBarIndex = get_bar_index()
newBar = currentBarIndex != lastBarIndex

# 📌 Vẽ các mức Daily, Weekly, Monthly nếu cần
if is_last_confirmed_history() or (is_realtime() and newBar):
    if showDailyLevelsInput and not higher_timeframe('D'):
        draw_levels('D', is_daily_timeframe(), dailyLevelsStyleInput, dailyLevelsColorInput)

    if showWeeklyLevelsInput and not higher_timeframe('W'):
        draw_levels('W', is_weekly_timeframe(), weeklyLevelsStyleInput, weeklyLevelsColorInput)

    if showMonthlyLevelsInput and not higher_timeframe('M'):
        draw_levels('M', is_monthly_timeframe(), monthlyLevelsStyleInput, monthlyLevelsColorInput)
