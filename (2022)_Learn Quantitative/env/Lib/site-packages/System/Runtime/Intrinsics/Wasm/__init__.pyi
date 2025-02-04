from typing import overload
import abc
import typing

import System
import System.Runtime.Intrinsics
import System.Runtime.Intrinsics.Wasm


class PackedSimd(System.Object, metaclass=abc.ABCMeta):
    """This class provides access to the WebAssembly packed SIMD instructions via intrinsics"""

    IsSupported: bool

    @staticmethod
    @overload
    def Add(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Add(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Add(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Add(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Add(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Add(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Add(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Add(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Add(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def Add(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def Add(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Add(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i8x16.add"""
        ...

    @staticmethod
    @overload
    def Add(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i16x8.add"""
        ...

    @staticmethod
    @overload
    def Add(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i16x8.add"""
        ...

    @staticmethod
    @overload
    def Add(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i32x4.add"""
        ...

    @staticmethod
    @overload
    def Add(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i32x4.add"""
        ...

    @staticmethod
    @overload
    def Add(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i64x2.add"""
        ...

    @staticmethod
    @overload
    def Add(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i64x2.add"""
        ...

    @staticmethod
    @overload
    def Add(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        """i32x4.add"""
        ...

    @staticmethod
    @overload
    def Add(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        """i32x4.add"""
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """v128.and"""
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """v128.and"""
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """v128.and"""
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """v128.and"""
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """v128.and"""
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """v128.and"""
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """v128.and"""
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """v128.and"""
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """v128.and"""
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        """v128.and"""
        ...

    @staticmethod
    @overload
    def And(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        """v128.and"""
        ...

    @staticmethod
    @overload
    def Bitmask(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        ...

    @staticmethod
    @overload
    def Bitmask(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        ...

    @staticmethod
    @overload
    def Bitmask(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        ...

    @staticmethod
    @overload
    def Bitmask(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        ...

    @staticmethod
    @overload
    def Bitmask(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        ...

    @staticmethod
    @overload
    def Bitmask(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        ...

    @staticmethod
    @overload
    def Bitmask(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        ...

    @staticmethod
    @overload
    def Bitmask(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        ...

    @staticmethod
    @overload
    def Bitmask(value: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> int:
        ...

    @staticmethod
    @overload
    def Bitmask(value: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> int:
        ...

    @staticmethod
    @overload
    def Bitmask(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        """i8x16.bitmask"""
        ...

    @staticmethod
    @overload
    def Bitmask(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        """i8x16.bitmask"""
        ...

    @staticmethod
    @overload
    def Bitmask(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        """i16x8.bitmask"""
        ...

    @staticmethod
    @overload
    def Bitmask(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        """i16x8.bitmask"""
        ...

    @staticmethod
    @overload
    def Bitmask(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        """i32x4.bitmask"""
        ...

    @staticmethod
    @overload
    def Bitmask(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        """i32x4.bitmask"""
        ...

    @staticmethod
    @overload
    def Bitmask(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        """i64x2.bitmask"""
        ...

    @staticmethod
    @overload
    def Bitmask(value: System.Runtime.Intrinsics.Vector128[int]) -> int:
        """i64x2.bitmask"""
        ...

    @staticmethod
    @overload
    def Bitmask(value: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> int:
        """i32x4.bitmask"""
        ...

    @staticmethod
    @overload
    def Bitmask(value: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> int:
        """i32x4.bitmask"""
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i8x16.eq"""
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i8x16.eq"""
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i16x8.eq"""
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i16x8.eq"""
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i32x4.eq"""
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i32x4.eq"""
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i64x2.eq"""
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i64x2.eq"""
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """f32x4.eq"""
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """f64x2.eq"""
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        """i32x4.eq"""
        ...

    @staticmethod
    @overload
    def CompareEqual(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        """i32x4.eq"""
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i8x16.ne"""
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i8x16.ne"""
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i16x8.ne"""
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i16x8.ne"""
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i32x4.ne"""
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i32x4.ne"""
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i64x2.ne"""
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i64x2.ne"""
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """f32x4.ne"""
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """f64x2.ne"""
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        """i32x4.ne"""
        ...

    @staticmethod
    @overload
    def CompareNotEqual(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        """i32x4.ne"""
        ...

    @staticmethod
    @overload
    def Dot(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Dot(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i32x4.dot_i16x8_s"""
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[float], index: int) -> float:
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[float], index: int) -> float:
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[System.IntPtr], index: int) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[System.UIntPtr], index: int) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
        """i8x16.extract_lane_u"""
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
        """i16x8.extract_lane_s"""
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
        """i16x8.extract_lane_u"""
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
        """i32x4.extract_lane"""
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
        """i32x4.extract_lane"""
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
        """i64x2.extract_lane"""
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[int], index: int) -> int:
        """i64x2.extract_lane"""
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[float], index: int) -> float:
        """f32x4.extract_lane"""
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[float], index: int) -> float:
        """f64x2.extract_lane"""
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[System.IntPtr], index: int) -> System.IntPtr:
        """i32x4.extract_lane"""
        ...

    @staticmethod
    @overload
    def ExtractLane(value: System.Runtime.Intrinsics.Vector128[System.UIntPtr], index: int) -> System.UIntPtr:
        """i32x4.extract_lane"""
        ...

    @staticmethod
    @overload
    def Multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Multiply(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def Multiply(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def Multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i16x8.mul"""
        ...

    @staticmethod
    @overload
    def Multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i16x8.mul"""
        ...

    @staticmethod
    @overload
    def Multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i32x4.mul"""
        ...

    @staticmethod
    @overload
    def Multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i32x4.mul"""
        ...

    @staticmethod
    @overload
    def Multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i64x2.mul"""
        ...

    @staticmethod
    @overload
    def Multiply(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i64x2.mul"""
        ...

    @staticmethod
    @overload
    def Multiply(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        """i32x4.mul"""
        ...

    @staticmethod
    @overload
    def Multiply(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        """i32x4.mul"""
        ...

    @staticmethod
    @overload
    def Negate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Negate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Negate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Negate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Negate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Negate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Negate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Negate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Negate(value: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def Negate(value: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def Negate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i8x16.neg"""
        ...

    @staticmethod
    @overload
    def Negate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i8x16.neg"""
        ...

    @staticmethod
    @overload
    def Negate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i16x8.neg"""
        ...

    @staticmethod
    @overload
    def Negate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i16x8.neg"""
        ...

    @staticmethod
    @overload
    def Negate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i32x4.neg"""
        ...

    @staticmethod
    @overload
    def Negate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i32x4.neg"""
        ...

    @staticmethod
    @overload
    def Negate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i64x2.neg"""
        ...

    @staticmethod
    @overload
    def Negate(value: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i64x2.neg"""
        ...

    @staticmethod
    @overload
    def Negate(value: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        """i32x4.neg"""
        ...

    @staticmethod
    @overload
    def Negate(value: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        """i32x4.neg"""
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[int], imm: int, value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[int], imm: int, value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[int], imm: int, value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[int], imm: int, value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[int], imm: int, value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[int], imm: int, value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[int], imm: int, value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[int], imm: int, value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[float], imm: int, value: float) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[float], imm: int, value: float) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[System.IntPtr], imm: int, value: System.IntPtr) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[System.UIntPtr], imm: int, value: System.UIntPtr) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[int], imm: int, value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """i8x16.replace_lane"""
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[int], imm: int, value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """i8x16.replace_lane"""
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[int], imm: int, value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """i16x8.replace_lane"""
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[int], imm: int, value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """i16x8.replace_lane"""
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[int], imm: int, value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """i32x4.replace_lane"""
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[int], imm: int, value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """i32x4.replace_lane"""
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[int], imm: int, value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """i64x2.replace_lane"""
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[int], imm: int, value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """i64x2.replace_lane"""
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[float], imm: int, value: float) -> System.Runtime.Intrinsics.Vector128[float]:
        """f32x4.replace_lane"""
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[float], imm: int, value: float) -> System.Runtime.Intrinsics.Vector128[float]:
        """f64x2.replace_lane"""
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[System.IntPtr], imm: int, value: System.IntPtr) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        """i32x4.replace_lane"""
        ...

    @staticmethod
    @overload
    def ReplaceLane(vector: System.Runtime.Intrinsics.Vector128[System.UIntPtr], imm: int, value: System.UIntPtr) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        """i32x4.replace_lane"""
        ...

    @staticmethod
    @overload
    def Shuffle(lower: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Shuffle(lower: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Shuffle(lower: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i8x16.shuffle"""
        ...

    @staticmethod
    @overload
    def Shuffle(lower: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i8x16.shuffle"""
        ...

    @staticmethod
    @overload
    def Splat(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Splat(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Splat(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Splat(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Splat(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Splat(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Splat(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Splat(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Splat(value: float) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def Splat(value: float) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def Splat(value: System.IntPtr) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def Splat(value: System.UIntPtr) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def Splat(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Splat(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """i8x16.splat or v128.const"""
        ...

    @staticmethod
    @overload
    def Splat(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """i16x8.splat or v128.const"""
        ...

    @staticmethod
    @overload
    def Splat(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """i16x8.splat or v128.const"""
        ...

    @staticmethod
    @overload
    def Splat(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """i32x4.splat or v128.const"""
        ...

    @staticmethod
    @overload
    def Splat(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """i32x4.splat or v128.const"""
        ...

    @staticmethod
    @overload
    def Splat(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """i64x2.splat or v128.const"""
        ...

    @staticmethod
    @overload
    def Splat(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """i64x2.splat or v128.const"""
        ...

    @staticmethod
    @overload
    def Splat(value: float) -> System.Runtime.Intrinsics.Vector128[float]:
        """f32x4.splat or v128.const"""
        ...

    @staticmethod
    @overload
    def Splat(value: float) -> System.Runtime.Intrinsics.Vector128[float]:
        """f64x2.splat or v128.const"""
        ...

    @staticmethod
    @overload
    def Splat(value: System.IntPtr) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        """i32x4.splat or v128.const"""
        ...

    @staticmethod
    @overload
    def Splat(value: System.UIntPtr) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        """i32x4.splat or v128.const"""
        ...

    @staticmethod
    @overload
    def Subtract(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Subtract(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Subtract(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Subtract(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Subtract(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Subtract(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Subtract(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Subtract(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Subtract(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        ...

    @staticmethod
    @overload
    def Subtract(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def Subtract(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i8x16.sub"""
        ...

    @staticmethod
    @overload
    def Subtract(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i8x16.sub"""
        ...

    @staticmethod
    @overload
    def Subtract(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i16x8.sub"""
        ...

    @staticmethod
    @overload
    def Subtract(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i16x8.sub"""
        ...

    @staticmethod
    @overload
    def Subtract(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i32x4.sub"""
        ...

    @staticmethod
    @overload
    def Subtract(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i32x4.sub"""
        ...

    @staticmethod
    @overload
    def Subtract(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i64x2.sub"""
        ...

    @staticmethod
    @overload
    def Subtract(left: System.Runtime.Intrinsics.Vector128[int], right: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i64x2.sub"""
        ...

    @staticmethod
    @overload
    def Subtract(left: System.Runtime.Intrinsics.Vector128[System.IntPtr], right: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        """i32x4.sub"""
        ...

    @staticmethod
    @overload
    def Subtract(left: System.Runtime.Intrinsics.Vector128[System.UIntPtr], right: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        """i32x4.sub"""
        ...

    @staticmethod
    @overload
    def Swizzle(vector: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Swizzle(vector: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        ...

    @staticmethod
    @overload
    def Swizzle(vector: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i8x16.swizzle"""
        ...

    @staticmethod
    @overload
    def Swizzle(vector: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """i8x16.swizzle"""
        ...


