from typing import overload
import typing

import System
import System.Collections
import System.ComponentModel
import System.Drawing
import System.Globalization
import System.Numerics

System_Drawing_Point = typing.Any
System_Drawing_SizeF = typing.Any
System_Drawing_Color = typing.Any
System_Drawing_RectangleF = typing.Any
System_Drawing_Size = typing.Any
System_Drawing_PointF = typing.Any
System_Drawing_Rectangle = typing.Any


class Size(System.IEquatable[System_Drawing_Size]):
    """Represents the size of a rectangular region with an ordered pair of width and height."""

    Empty: System.Drawing.Size
    """Initializes a new instance of the System.Drawing.Size class."""

    @property
    def IsEmpty(self) -> bool:
        """Tests whether this System.Drawing.Size has zero width and height."""
        ...

    @property
    def Width(self) -> int:
        """Represents the horizontal component of this System.Drawing.Size."""
        ...

    @Width.setter
    def Width(self, value: int):
        """Represents the horizontal component of this System.Drawing.Size."""
        ...

    @property
    def Height(self) -> int:
        """Represents the vertical component of this System.Drawing.Size."""
        ...

    @Height.setter
    def Height(self, value: int):
        """Represents the vertical component of this System.Drawing.Size."""
        ...

    @overload
    def __init__(self, pt: System.Drawing.Point) -> None:
        """
        Initializes a new instance of the System.Drawing.Size class from the specified
        System.Drawing.Point.
        """
        ...

    @overload
    def __init__(self, width: int, height: int) -> None:
        """Initializes a new instance of the System.Drawing.Size class from the specified dimensions."""
        ...

    @staticmethod
    def Add(sz1: System.Drawing.Size, sz2: System.Drawing.Size) -> System.Drawing.Size:
        """Performs vector addition of two System.Drawing.Size objects."""
        ...

    @staticmethod
    def Ceiling(value: System.Drawing.SizeF) -> System.Drawing.Size:
        """Converts a SizeF to a Size by performing a ceiling operation on all the coordinates."""
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        """
        Tests to see whether the specified object is a System.Drawing.Size  with the same dimensions
        as this System.Drawing.Size.
        """
        ...

    @overload
    def Equals(self, other: System.Drawing.Size) -> bool:
        ...

    def GetHashCode(self) -> int:
        """Returns a hash code."""
        ...

    @staticmethod
    def Round(value: System.Drawing.SizeF) -> System.Drawing.Size:
        """Converts a SizeF to a Size by performing a round operation on all the coordinates."""
        ...

    @staticmethod
    def Subtract(sz1: System.Drawing.Size, sz2: System.Drawing.Size) -> System.Drawing.Size:
        """Contracts a System.Drawing.Size by another System.Drawing.Size ."""
        ...

    def ToString(self) -> str:
        """Creates a human-readable string that represents this System.Drawing.Size."""
        ...

    @staticmethod
    def Truncate(value: System.Drawing.SizeF) -> System.Drawing.Size:
        """Converts a SizeF to a Size by performing a truncate operation on all the coordinates."""
        ...


class PointF(System.IEquatable[System_Drawing_PointF]):
    """Represents an ordered pair of x and y coordinates that define a point in a two-dimensional plane."""

    Empty: System.Drawing.PointF
    """Creates a new instance of the System.Drawing.PointF class with member data left uninitialized."""

    @property
    def IsEmpty(self) -> bool:
        """Gets a value indicating whether this System.Drawing.PointF is empty."""
        ...

    @property
    def X(self) -> float:
        """Gets the x-coordinate of this System.Drawing.PointF."""
        ...

    @X.setter
    def X(self, value: float):
        """Gets the x-coordinate of this System.Drawing.PointF."""
        ...

    @property
    def Y(self) -> float:
        """Gets the y-coordinate of this System.Drawing.PointF."""
        ...

    @Y.setter
    def Y(self, value: float):
        """Gets the y-coordinate of this System.Drawing.PointF."""
        ...

    @overload
    def __init__(self, x: float, y: float) -> None:
        """Initializes a new instance of the System.Drawing.PointF class with the specified coordinates."""
        ...

    @overload
    def __init__(self, vector: System.Numerics.Vector2) -> None:
        """
        Initializes a new instance of the System.Drawing.PointF struct from the specified
        System.Numerics.Vector2.
        """
        ...

    @staticmethod
    @overload
    def Add(pt: System.Drawing.PointF, sz: System.Drawing.Size) -> System.Drawing.PointF:
        """Translates a System.Drawing.PointF by a given System.Drawing.Size ."""
        ...

    @staticmethod
    @overload
    def Add(pt: System.Drawing.PointF, sz: System.Drawing.SizeF) -> System.Drawing.PointF:
        """Translates a System.Drawing.PointF by a given System.Drawing.SizeF ."""
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def Equals(self, other: System.Drawing.PointF) -> bool:
        ...

    def GetHashCode(self) -> int:
        ...

    @staticmethod
    @overload
    def Subtract(pt: System.Drawing.PointF, sz: System.Drawing.Size) -> System.Drawing.PointF:
        """Translates a System.Drawing.PointF by the negative of a given System.Drawing.Size ."""
        ...

    @staticmethod
    @overload
    def Subtract(pt: System.Drawing.PointF, sz: System.Drawing.SizeF) -> System.Drawing.PointF:
        """Translates a System.Drawing.PointF by the negative of a given System.Drawing.SizeF ."""
        ...

    def ToString(self) -> str:
        ...

    def ToVector2(self) -> System.Numerics.Vector2:
        """Creates a new System.Numerics.Vector2 from this System.Drawing.PointF."""
        ...


class Point(System.IEquatable[System_Drawing_Point]):
    """Represents an ordered pair of x and y coordinates that define a point in a two-dimensional plane."""

    Empty: System.Drawing.Point
    """Creates a new instance of the System.Drawing.Point class with member data left uninitialized."""

    @property
    def IsEmpty(self) -> bool:
        """Gets a value indicating whether this System.Drawing.Point is empty."""
        ...

    @property
    def X(self) -> int:
        """Gets the x-coordinate of this System.Drawing.Point."""
        ...

    @X.setter
    def X(self, value: int):
        """Gets the x-coordinate of this System.Drawing.Point."""
        ...

    @property
    def Y(self) -> int:
        """Gets the y-coordinate of this System.Drawing.Point."""
        ...

    @Y.setter
    def Y(self, value: int):
        """Gets the y-coordinate of this System.Drawing.Point."""
        ...

    @overload
    def __init__(self, x: int, y: int) -> None:
        """Initializes a new instance of the System.Drawing.Point class with the specified coordinates."""
        ...

    @overload
    def __init__(self, sz: System.Drawing.Size) -> None:
        """Initializes a new instance of the System.Drawing.Point class from a System.Drawing.Size ."""
        ...

    @overload
    def __init__(self, dw: int) -> None:
        """Initializes a new instance of the Point class using coordinates specified by an integer value."""
        ...

    @staticmethod
    def Add(pt: System.Drawing.Point, sz: System.Drawing.Size) -> System.Drawing.Point:
        """Translates a System.Drawing.Point by a given System.Drawing.Size ."""
        ...

    @staticmethod
    def Ceiling(value: System.Drawing.PointF) -> System.Drawing.Point:
        """Converts a PointF to a Point by performing a ceiling operation on all the coordinates."""
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        """
        Specifies whether this System.Drawing.Point contains the same coordinates as the specified
        object.
        """
        ...

    @overload
    def Equals(self, other: System.Drawing.Point) -> bool:
        ...

    def GetHashCode(self) -> int:
        """Returns a hash code."""
        ...

    @overload
    def Offset(self, dx: int, dy: int) -> None:
        """Translates this System.Drawing.Point by the specified amount."""
        ...

    @overload
    def Offset(self, p: System.Drawing.Point) -> None:
        """Translates this System.Drawing.Point by the specified amount."""
        ...

    @staticmethod
    def Round(value: System.Drawing.PointF) -> System.Drawing.Point:
        """Converts a PointF to a Point by performing a round operation on all the coordinates."""
        ...

    @staticmethod
    def Subtract(pt: System.Drawing.Point, sz: System.Drawing.Size) -> System.Drawing.Point:
        """Translates a System.Drawing.Point by the negative of a given System.Drawing.Size ."""
        ...

    def ToString(self) -> str:
        """Converts this System.Drawing.Point to a human readable string."""
        ...

    @staticmethod
    def Truncate(value: System.Drawing.PointF) -> System.Drawing.Point:
        """Converts a PointF to a Point by performing a truncate operation on all the coordinates."""
        ...


class SizeF(System.IEquatable[System_Drawing_SizeF]):
    """Represents the size of a rectangular region with an ordered pair of width and height."""

    Empty: System.Drawing.SizeF
    """Initializes a new instance of the System.Drawing.SizeF class."""

    @property
    def IsEmpty(self) -> bool:
        """Tests whether this System.Drawing.SizeF has zero width and height."""
        ...

    @property
    def Width(self) -> float:
        """Represents the horizontal component of this System.Drawing.SizeF."""
        ...

    @Width.setter
    def Width(self, value: float):
        """Represents the horizontal component of this System.Drawing.SizeF."""
        ...

    @property
    def Height(self) -> float:
        """Represents the vertical component of this System.Drawing.SizeF."""
        ...

    @Height.setter
    def Height(self, value: float):
        """Represents the vertical component of this System.Drawing.SizeF."""
        ...

    @overload
    def __init__(self, size: System.Drawing.SizeF) -> None:
        """
        Initializes a new instance of the System.Drawing.SizeF class from the specified
        existing System.Drawing.SizeF.
        """
        ...

    @overload
    def __init__(self, pt: System.Drawing.PointF) -> None:
        """
        Initializes a new instance of the System.Drawing.SizeF class from the specified
        System.Drawing.PointF.
        """
        ...

    @overload
    def __init__(self, vector: System.Numerics.Vector2) -> None:
        """
        Initializes a new instance of the System.Drawing.SizeF struct from the specified
        System.Numerics.Vector2.
        """
        ...

    @overload
    def __init__(self, width: float, height: float) -> None:
        """Initializes a new instance of the System.Drawing.SizeF class from the specified dimensions."""
        ...

    @staticmethod
    def Add(sz1: System.Drawing.SizeF, sz2: System.Drawing.SizeF) -> System.Drawing.SizeF:
        """Performs vector addition of two System.Drawing.SizeF objects."""
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        """
        Tests to see whether the specified object is a System.Drawing.SizeF  with the same dimensions
        as this System.Drawing.SizeF.
        """
        ...

    @overload
    def Equals(self, other: System.Drawing.SizeF) -> bool:
        ...

    def GetHashCode(self) -> int:
        ...

    @staticmethod
    def Subtract(sz1: System.Drawing.SizeF, sz2: System.Drawing.SizeF) -> System.Drawing.SizeF:
        """Contracts a System.Drawing.SizeF by another System.Drawing.SizeF."""
        ...

    def ToPointF(self) -> System.Drawing.PointF:
        ...

    def ToSize(self) -> System.Drawing.Size:
        ...

    def ToString(self) -> str:
        """Creates a human-readable string that represents this System.Drawing.SizeF."""
        ...

    def ToVector2(self) -> System.Numerics.Vector2:
        """Creates a new System.Numerics.Vector2 from this System.Drawing.SizeF."""
        ...


class KnownColor(System.Enum):
    """This class has no documentation."""

    ActiveBorder = 1

    ActiveCaption = 1

    ActiveCaptionText = 2

    AppWorkspace = 3

    Control = 4

    ControlDark = 5

    ControlDarkDark = 6

    ControlLight = 7

    ControlLightLight = 8

    ControlText = 9

    Desktop = 10

    GrayText = 11

    Highlight = 12

    HighlightText = 13

    HotTrack = 14

    InactiveBorder = 15

    InactiveCaption = 16

    InactiveCaptionText = 17

    Info = 18

    InfoText = 19

    Menu = 20

    MenuText = 21

    ScrollBar = 22

    Window = 23

    WindowFrame = 24

    WindowText = 25

    Transparent = 26

    AliceBlue = 27

    AntiqueWhite = 28

    Aqua = 29

    Aquamarine = 30

    Azure = 31

    Beige = 32

    Bisque = 33

    Black = 34

    BlanchedAlmond = 35

    Blue = 36

    BlueViolet = 37

    Brown = 38

    BurlyWood = 39

    CadetBlue = 40

    Chartreuse = 41

    Chocolate = 42

    Coral = 43

    CornflowerBlue = 44

    Cornsilk = 45

    Crimson = 46

    Cyan = 47

    DarkBlue = 48

    DarkCyan = 49

    DarkGoldenrod = 50

    DarkGray = 51

    DarkGreen = 52

    DarkKhaki = 53

    DarkMagenta = 54

    DarkOliveGreen = 55

    DarkOrange = 56

    DarkOrchid = 57

    DarkRed = 58

    DarkSalmon = 59

    DarkSeaGreen = 60

    DarkSlateBlue = 61

    DarkSlateGray = 62

    DarkTurquoise = 63

    DarkViolet = 64

    DeepPink = 65

    DeepSkyBlue = 66

    DimGray = 67

    DodgerBlue = 68

    Firebrick = 69

    FloralWhite = 70

    ForestGreen = 71

    Fuchsia = 72

    Gainsboro = 73

    GhostWhite = 74

    Gold = 75

    Goldenrod = 76

    Gray = 77

    Green = 78

    GreenYellow = 79

    Honeydew = 80

    HotPink = 81

    IndianRed = 82

    Indigo = 83

    Ivory = 84

    Khaki = 85

    Lavender = 86

    LavenderBlush = 87

    LawnGreen = 88

    LemonChiffon = 89

    LightBlue = 90

    LightCoral = 91

    LightCyan = 92

    LightGoldenrodYellow = 93

    LightGray = 94

    LightGreen = 95

    LightPink = 96

    LightSalmon = 97

    LightSeaGreen = 98

    LightSkyBlue = 99

    LightSlateGray = 100

    LightSteelBlue = 101

    LightYellow = 102

    Lime = 103

    LimeGreen = 104

    Linen = 105

    Magenta = 106

    Maroon = 107

    MediumAquamarine = 108

    MediumBlue = 109

    MediumOrchid = 110

    MediumPurple = 111

    MediumSeaGreen = 112

    MediumSlateBlue = 113

    MediumSpringGreen = 114

    MediumTurquoise = 115

    MediumVioletRed = 116

    MidnightBlue = 117

    MintCream = 118

    MistyRose = 119

    Moccasin = 120

    NavajoWhite = 121

    Navy = 122

    OldLace = 123

    Olive = 124

    OliveDrab = 125

    Orange = 126

    OrangeRed = 127

    Orchid = 128

    PaleGoldenrod = 129

    PaleGreen = 130

    PaleTurquoise = 131

    PaleVioletRed = 132

    PapayaWhip = 133

    PeachPuff = 134

    Peru = 135

    Pink = 136

    Plum = 137

    PowderBlue = 138

    Purple = 139

    Red = 140

    RosyBrown = 141

    RoyalBlue = 142

    SaddleBrown = 143

    Salmon = 144

    SandyBrown = 145

    SeaGreen = 146

    SeaShell = 147

    Sienna = 148

    Silver = 149

    SkyBlue = 150

    SlateBlue = 151

    SlateGray = 152

    Snow = 153

    SpringGreen = 154

    SteelBlue = 155

    Tan = 156

    Teal = 157

    Thistle = 158

    Tomato = 159

    Turquoise = 160

    Violet = 161

    Wheat = 162

    White = 163

    WhiteSmoke = 164

    Yellow = 165

    YellowGreen = 166

    ButtonFace = 167

    ButtonHighlight = 168

    ButtonShadow = 169

    GradientActiveCaption = 170

    GradientInactiveCaption = 171

    MenuBar = 172

    MenuHighlight = 173

    RebeccaPurple = 174


class Color(System.IEquatable[System_Drawing_Color]):
    """This class has no documentation."""

    Empty: System.Drawing.Color

    Transparent: System.Drawing.Color

    AliceBlue: System.Drawing.Color

    AntiqueWhite: System.Drawing.Color

    Aqua: System.Drawing.Color

    Aquamarine: System.Drawing.Color

    Azure: System.Drawing.Color

    Beige: System.Drawing.Color

    Bisque: System.Drawing.Color

    Black: System.Drawing.Color

    BlanchedAlmond: System.Drawing.Color

    Blue: System.Drawing.Color

    BlueViolet: System.Drawing.Color

    Brown: System.Drawing.Color

    BurlyWood: System.Drawing.Color

    CadetBlue: System.Drawing.Color

    Chartreuse: System.Drawing.Color

    Chocolate: System.Drawing.Color

    Coral: System.Drawing.Color

    CornflowerBlue: System.Drawing.Color

    Cornsilk: System.Drawing.Color

    Crimson: System.Drawing.Color

    Cyan: System.Drawing.Color

    DarkBlue: System.Drawing.Color

    DarkCyan: System.Drawing.Color

    DarkGoldenrod: System.Drawing.Color

    DarkGray: System.Drawing.Color

    DarkGreen: System.Drawing.Color

    DarkKhaki: System.Drawing.Color

    DarkMagenta: System.Drawing.Color

    DarkOliveGreen: System.Drawing.Color

    DarkOrange: System.Drawing.Color

    DarkOrchid: System.Drawing.Color

    DarkRed: System.Drawing.Color

    DarkSalmon: System.Drawing.Color

    DarkSeaGreen: System.Drawing.Color

    DarkSlateBlue: System.Drawing.Color

    DarkSlateGray: System.Drawing.Color

    DarkTurquoise: System.Drawing.Color

    DarkViolet: System.Drawing.Color

    DeepPink: System.Drawing.Color

    DeepSkyBlue: System.Drawing.Color

    DimGray: System.Drawing.Color

    DodgerBlue: System.Drawing.Color

    Firebrick: System.Drawing.Color

    FloralWhite: System.Drawing.Color

    ForestGreen: System.Drawing.Color

    Fuchsia: System.Drawing.Color

    Gainsboro: System.Drawing.Color

    GhostWhite: System.Drawing.Color

    Gold: System.Drawing.Color

    Goldenrod: System.Drawing.Color

    Gray: System.Drawing.Color

    Green: System.Drawing.Color

    GreenYellow: System.Drawing.Color

    Honeydew: System.Drawing.Color

    HotPink: System.Drawing.Color

    IndianRed: System.Drawing.Color

    Indigo: System.Drawing.Color

    Ivory: System.Drawing.Color

    Khaki: System.Drawing.Color

    Lavender: System.Drawing.Color

    LavenderBlush: System.Drawing.Color

    LawnGreen: System.Drawing.Color

    LemonChiffon: System.Drawing.Color

    LightBlue: System.Drawing.Color

    LightCoral: System.Drawing.Color

    LightCyan: System.Drawing.Color

    LightGoldenrodYellow: System.Drawing.Color

    LightGreen: System.Drawing.Color

    LightGray: System.Drawing.Color

    LightPink: System.Drawing.Color

    LightSalmon: System.Drawing.Color

    LightSeaGreen: System.Drawing.Color

    LightSkyBlue: System.Drawing.Color

    LightSlateGray: System.Drawing.Color

    LightSteelBlue: System.Drawing.Color

    LightYellow: System.Drawing.Color

    Lime: System.Drawing.Color

    LimeGreen: System.Drawing.Color

    Linen: System.Drawing.Color

    Magenta: System.Drawing.Color

    Maroon: System.Drawing.Color

    MediumAquamarine: System.Drawing.Color

    MediumBlue: System.Drawing.Color

    MediumOrchid: System.Drawing.Color

    MediumPurple: System.Drawing.Color

    MediumSeaGreen: System.Drawing.Color

    MediumSlateBlue: System.Drawing.Color

    MediumSpringGreen: System.Drawing.Color

    MediumTurquoise: System.Drawing.Color

    MediumVioletRed: System.Drawing.Color

    MidnightBlue: System.Drawing.Color

    MintCream: System.Drawing.Color

    MistyRose: System.Drawing.Color

    Moccasin: System.Drawing.Color

    NavajoWhite: System.Drawing.Color

    Navy: System.Drawing.Color

    OldLace: System.Drawing.Color

    Olive: System.Drawing.Color

    OliveDrab: System.Drawing.Color

    Orange: System.Drawing.Color

    OrangeRed: System.Drawing.Color

    Orchid: System.Drawing.Color

    PaleGoldenrod: System.Drawing.Color

    PaleGreen: System.Drawing.Color

    PaleTurquoise: System.Drawing.Color

    PaleVioletRed: System.Drawing.Color

    PapayaWhip: System.Drawing.Color

    PeachPuff: System.Drawing.Color

    Peru: System.Drawing.Color

    Pink: System.Drawing.Color

    Plum: System.Drawing.Color

    PowderBlue: System.Drawing.Color

    Purple: System.Drawing.Color

    RebeccaPurple: System.Drawing.Color
    """Gets a system-defined color that has an ARGB value of #663399."""

    Red: System.Drawing.Color

    RosyBrown: System.Drawing.Color

    RoyalBlue: System.Drawing.Color

    SaddleBrown: System.Drawing.Color

    Salmon: System.Drawing.Color

    SandyBrown: System.Drawing.Color

    SeaGreen: System.Drawing.Color

    SeaShell: System.Drawing.Color

    Sienna: System.Drawing.Color

    Silver: System.Drawing.Color

    SkyBlue: System.Drawing.Color

    SlateBlue: System.Drawing.Color

    SlateGray: System.Drawing.Color

    Snow: System.Drawing.Color

    SpringGreen: System.Drawing.Color

    SteelBlue: System.Drawing.Color

    Tan: System.Drawing.Color

    Teal: System.Drawing.Color

    Thistle: System.Drawing.Color

    Tomato: System.Drawing.Color

    Turquoise: System.Drawing.Color

    Violet: System.Drawing.Color

    Wheat: System.Drawing.Color

    White: System.Drawing.Color

    WhiteSmoke: System.Drawing.Color

    Yellow: System.Drawing.Color

    YellowGreen: System.Drawing.Color

    ARGBAlphaShift: int = 24

    ARGBRedShift: int = 16

    ARGBGreenShift: int = 8

    ARGBBlueShift: int = 0

    ARGBAlphaMask: int = ...

    ARGBRedMask: int = ...

    ARGBGreenMask: int = ...

    ARGBBlueMask: int = ...

    @property
    def R(self) -> int:
        ...

    @property
    def G(self) -> int:
        ...

    @property
    def B(self) -> int:
        ...

    @property
    def A(self) -> int:
        ...

    @property
    def IsKnownColor(self) -> bool:
        ...

    @property
    def IsEmpty(self) -> bool:
        ...

    @property
    def IsNamedColor(self) -> bool:
        ...

    @property
    def IsSystemColor(self) -> bool:
        ...

    @property
    def Name(self) -> str:
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def Equals(self, other: System.Drawing.Color) -> bool:
        ...

    @staticmethod
    @overload
    def FromArgb(argb: int) -> System.Drawing.Color:
        ...

    @staticmethod
    @overload
    def FromArgb(alpha: int, red: int, green: int, blue: int) -> System.Drawing.Color:
        ...

    @staticmethod
    @overload
    def FromArgb(alpha: int, baseColor: System.Drawing.Color) -> System.Drawing.Color:
        ...

    @staticmethod
    @overload
    def FromArgb(red: int, green: int, blue: int) -> System.Drawing.Color:
        ...

    @staticmethod
    def FromKnownColor(color: System.Drawing.KnownColor) -> System.Drawing.Color:
        ...

    @staticmethod
    def FromName(name: str) -> System.Drawing.Color:
        ...

    def GetBrightness(self) -> float:
        ...

    def GetHashCode(self) -> int:
        ...

    def GetHue(self) -> float:
        ...

    def GetSaturation(self) -> float:
        ...

    def ToArgb(self) -> int:
        ...

    def ToKnownColor(self) -> int:
        """:returns: This method returns the int value of a member of the System.Drawing.KnownColor enum."""
        ...

    def ToString(self) -> str:
        ...


class ColorTranslator(System.Object):
    """Translates colors to and from GDI+ Color objects."""

    COLORREF_RedShift: int = 0

    COLORREF_GreenShift: int = 8

    COLORREF_BlueShift: int = 16

    @staticmethod
    def FromHtml(htmlColor: str) -> System.Drawing.Color:
        """Translates an Html color representation to a GDI+ Color."""
        ...

    @staticmethod
    def FromOle(oleColor: int) -> System.Drawing.Color:
        """Translates an Ole color value to a GDI+ Color."""
        ...

    @staticmethod
    def FromWin32(win32Color: int) -> System.Drawing.Color:
        """Translates an Win32 color value to a GDI+ Color."""
        ...

    @staticmethod
    def ToHtml(c: System.Drawing.Color) -> str:
        """Translates the specified Color to an Html string color representation."""
        ...

    @staticmethod
    def ToOle(c: System.Drawing.Color) -> int:
        """Translates the specified Color to an Ole color."""
        ...

    @staticmethod
    def ToWin32(c: System.Drawing.Color) -> int:
        """Translates the specified Color to a Win32 color."""
        ...


class RectangleF(System.IEquatable[System_Drawing_RectangleF]):
    """Stores the location and size of a rectangular region."""

    Empty: System.Drawing.RectangleF
    """Initializes a new instance of the System.Drawing.RectangleF class."""

    @property
    def Location(self) -> System.Drawing.PointF:
        """
        Gets or sets the coordinates of the upper-left corner of the rectangular region represented by this
        System.Drawing.RectangleF.
        """
        ...

    @Location.setter
    def Location(self, value: System.Drawing.PointF):
        """
        Gets or sets the coordinates of the upper-left corner of the rectangular region represented by this
        System.Drawing.RectangleF.
        """
        ...

    @property
    def Size(self) -> System.Drawing.SizeF:
        """Gets or sets the size of this System.Drawing.RectangleF."""
        ...

    @Size.setter
    def Size(self, value: System.Drawing.SizeF):
        """Gets or sets the size of this System.Drawing.RectangleF."""
        ...

    @property
    def X(self) -> float:
        """
        Gets or sets the x-coordinate of the upper-left corner of the rectangular region defined by this
        System.Drawing.RectangleF.
        """
        ...

    @X.setter
    def X(self, value: float):
        """
        Gets or sets the x-coordinate of the upper-left corner of the rectangular region defined by this
        System.Drawing.RectangleF.
        """
        ...

    @property
    def Y(self) -> float:
        """
        Gets or sets the y-coordinate of the upper-left corner of the rectangular region defined by this
        System.Drawing.RectangleF.
        """
        ...

    @Y.setter
    def Y(self, value: float):
        """
        Gets or sets the y-coordinate of the upper-left corner of the rectangular region defined by this
        System.Drawing.RectangleF.
        """
        ...

    @property
    def Width(self) -> float:
        """Gets or sets the width of the rectangular region defined by this System.Drawing.RectangleF."""
        ...

    @Width.setter
    def Width(self, value: float):
        """Gets or sets the width of the rectangular region defined by this System.Drawing.RectangleF."""
        ...

    @property
    def Height(self) -> float:
        """Gets or sets the height of the rectangular region defined by this System.Drawing.RectangleF."""
        ...

    @Height.setter
    def Height(self, value: float):
        """Gets or sets the height of the rectangular region defined by this System.Drawing.RectangleF."""
        ...

    @property
    def Left(self) -> float:
        """
        Gets the x-coordinate of the upper-left corner of the rectangular region defined by this
        System.Drawing.RectangleF .
        """
        ...

    @property
    def Top(self) -> float:
        """
        Gets the y-coordinate of the upper-left corner of the rectangular region defined by this
        System.Drawing.RectangleF.
        """
        ...

    @property
    def Right(self) -> float:
        """
        Gets the x-coordinate of the lower-right corner of the rectangular region defined by this
        System.Drawing.RectangleF.
        """
        ...

    @property
    def Bottom(self) -> float:
        """
        Gets the y-coordinate of the lower-right corner of the rectangular region defined by this
        System.Drawing.RectangleF.
        """
        ...

    @property
    def IsEmpty(self) -> bool:
        """Tests whether this System.Drawing.RectangleF has a System.Drawing.RectangleF.Width or a System.Drawing.RectangleF.Height of 0."""
        ...

    @overload
    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        """
        Initializes a new instance of the System.Drawing.RectangleF class with the specified location
        and size.
        """
        ...

    @overload
    def __init__(self, location: System.Drawing.PointF, size: System.Drawing.SizeF) -> None:
        """
        Initializes a new instance of the System.Drawing.RectangleF class with the specified location
        and size.
        """
        ...

    @overload
    def __init__(self, vector: System.Numerics.Vector4) -> None:
        """
        Initializes a new instance of the System.Drawing.RectangleF struct from the specified
        System.Numerics.Vector4.
        """
        ...

    @overload
    def Contains(self, x: float, y: float) -> bool:
        """
        Determines if the specified point is contained within the rectangular region defined by this
        System.Drawing.Rectangle .
        """
        ...

    @overload
    def Contains(self, pt: System.Drawing.PointF) -> bool:
        """
        Determines if the specified point is contained within the rectangular region defined by this
        System.Drawing.Rectangle .
        """
        ...

    @overload
    def Contains(self, rect: System.Drawing.RectangleF) -> bool:
        """
        Determines if the rectangular region represented by  is entirely contained within
        the rectangular region represented by this System.Drawing.Rectangle .
        """
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        """
        Tests whether  is a System.Drawing.RectangleF with the same location and
        size of this System.Drawing.RectangleF.
        """
        ...

    @overload
    def Equals(self, other: System.Drawing.RectangleF) -> bool:
        ...

    @staticmethod
    def FromLTRB(left: float, top: float, right: float, bottom: float) -> System.Drawing.RectangleF:
        """Creates a new System.Drawing.RectangleF with the specified location and size."""
        ...

    def GetHashCode(self) -> int:
        """Gets the hash code for this System.Drawing.RectangleF."""
        ...

    @overload
    def Inflate(self, x: float, y: float) -> None:
        """Inflates this System.Drawing.Rectangle by the specified amount."""
        ...

    @overload
    def Inflate(self, size: System.Drawing.SizeF) -> None:
        """Inflates this System.Drawing.Rectangle by the specified amount."""
        ...

    @staticmethod
    @overload
    def Inflate(rect: System.Drawing.RectangleF, x: float, y: float) -> System.Drawing.RectangleF:
        """Creates a System.Drawing.Rectangle that is inflated by the specified amount."""
        ...

    @overload
    def Intersect(self, rect: System.Drawing.RectangleF) -> None:
        """Creates a Rectangle that represents the intersection between this Rectangle and rect."""
        ...

    @staticmethod
    @overload
    def Intersect(a: System.Drawing.RectangleF, b: System.Drawing.RectangleF) -> System.Drawing.RectangleF:
        """
        Creates a rectangle that represents the intersection between a and b. If there is no intersection, an
        empty rectangle is returned.
        """
        ...

    def IntersectsWith(self, rect: System.Drawing.RectangleF) -> bool:
        """Determines if this rectangle intersects with rect."""
        ...

    @overload
    def Offset(self, pos: System.Drawing.PointF) -> None:
        """Adjusts the location of this rectangle by the specified amount."""
        ...

    @overload
    def Offset(self, x: float, y: float) -> None:
        """Adjusts the location of this rectangle by the specified amount."""
        ...

    def ToString(self) -> str:
        """
        Converts the System.Drawing.RectangleF.Location and System.Drawing.RectangleF.Size
        of this System.Drawing.RectangleF to a human-readable string.
        """
        ...

    def ToVector4(self) -> System.Numerics.Vector4:
        """Creates a new System.Numerics.Vector4 from this System.Drawing.RectangleF."""
        ...

    @staticmethod
    def Union(a: System.Drawing.RectangleF, b: System.Drawing.RectangleF) -> System.Drawing.RectangleF:
        """Creates a rectangle that represents the union between a and b."""
        ...


class SystemColors(System.Object):
    """This class has no documentation."""

    ActiveBorder: System.Drawing.Color

    ActiveCaption: System.Drawing.Color

    ActiveCaptionText: System.Drawing.Color

    AppWorkspace: System.Drawing.Color

    ButtonFace: System.Drawing.Color

    ButtonHighlight: System.Drawing.Color

    ButtonShadow: System.Drawing.Color

    Control: System.Drawing.Color

    ControlDark: System.Drawing.Color

    ControlDarkDark: System.Drawing.Color

    ControlLight: System.Drawing.Color

    ControlLightLight: System.Drawing.Color

    ControlText: System.Drawing.Color

    Desktop: System.Drawing.Color

    GradientActiveCaption: System.Drawing.Color

    GradientInactiveCaption: System.Drawing.Color

    GrayText: System.Drawing.Color

    Highlight: System.Drawing.Color

    HighlightText: System.Drawing.Color

    HotTrack: System.Drawing.Color

    InactiveBorder: System.Drawing.Color

    InactiveCaption: System.Drawing.Color

    InactiveCaptionText: System.Drawing.Color

    Info: System.Drawing.Color

    InfoText: System.Drawing.Color

    Menu: System.Drawing.Color

    MenuBar: System.Drawing.Color

    MenuHighlight: System.Drawing.Color

    MenuText: System.Drawing.Color

    ScrollBar: System.Drawing.Color

    Window: System.Drawing.Color

    WindowFrame: System.Drawing.Color

    WindowText: System.Drawing.Color


class Rectangle(System.IEquatable[System_Drawing_Rectangle]):
    """Stores the location and size of a rectangular region."""

    Empty: System.Drawing.Rectangle

    @property
    def Location(self) -> System.Drawing.Point:
        """
        Gets or sets the coordinates of the upper-left corner of the rectangular region represented by this
        System.Drawing.Rectangle.
        """
        ...

    @Location.setter
    def Location(self, value: System.Drawing.Point):
        """
        Gets or sets the coordinates of the upper-left corner of the rectangular region represented by this
        System.Drawing.Rectangle.
        """
        ...

    @property
    def Size(self) -> System.Drawing.Size:
        """Gets or sets the size of this System.Drawing.Rectangle."""
        ...

    @Size.setter
    def Size(self, value: System.Drawing.Size):
        """Gets or sets the size of this System.Drawing.Rectangle."""
        ...

    @property
    def X(self) -> int:
        """
        Gets or sets the x-coordinate of the upper-left corner of the rectangular region defined by this
        System.Drawing.Rectangle.
        """
        ...

    @X.setter
    def X(self, value: int):
        """
        Gets or sets the x-coordinate of the upper-left corner of the rectangular region defined by this
        System.Drawing.Rectangle.
        """
        ...

    @property
    def Y(self) -> int:
        """
        Gets or sets the y-coordinate of the upper-left corner of the rectangular region defined by this
        System.Drawing.Rectangle.
        """
        ...

    @Y.setter
    def Y(self, value: int):
        """
        Gets or sets the y-coordinate of the upper-left corner of the rectangular region defined by this
        System.Drawing.Rectangle.
        """
        ...

    @property
    def Width(self) -> int:
        """Gets or sets the width of the rectangular region defined by this System.Drawing.Rectangle."""
        ...

    @Width.setter
    def Width(self, value: int):
        """Gets or sets the width of the rectangular region defined by this System.Drawing.Rectangle."""
        ...

    @property
    def Height(self) -> int:
        """Gets or sets the width of the rectangular region defined by this System.Drawing.Rectangle."""
        ...

    @Height.setter
    def Height(self, value: int):
        """Gets or sets the width of the rectangular region defined by this System.Drawing.Rectangle."""
        ...

    @property
    def Left(self) -> int:
        """
        Gets the x-coordinate of the upper-left corner of the rectangular region defined by this
        System.Drawing.Rectangle .
        """
        ...

    @property
    def Top(self) -> int:
        """
        Gets the y-coordinate of the upper-left corner of the rectangular region defined by this
        System.Drawing.Rectangle.
        """
        ...

    @property
    def Right(self) -> int:
        """
        Gets the x-coordinate of the lower-right corner of the rectangular region defined by this
        System.Drawing.Rectangle.
        """
        ...

    @property
    def Bottom(self) -> int:
        """
        Gets the y-coordinate of the lower-right corner of the rectangular region defined by this
        System.Drawing.Rectangle.
        """
        ...

    @property
    def IsEmpty(self) -> bool:
        """
        Tests whether this System.Drawing.Rectangle has a System.Drawing.Rectangle.Width
        or a System.Drawing.Rectangle.Height of 0.
        """
        ...

    @overload
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        """
        Initializes a new instance of the System.Drawing.Rectangle class with the specified location
        and size.
        """
        ...

    @overload
    def __init__(self, location: System.Drawing.Point, size: System.Drawing.Size) -> None:
        """Initializes a new instance of the Rectangle class with the specified location and size."""
        ...

    @staticmethod
    def Ceiling(value: System.Drawing.RectangleF) -> System.Drawing.Rectangle:
        """Converts a RectangleF to a Rectangle by performing a ceiling operation on all the coordinates."""
        ...

    @overload
    def Contains(self, x: int, y: int) -> bool:
        """
        Determines if the specified point is contained within the rectangular region defined by this
        System.Drawing.Rectangle .
        """
        ...

    @overload
    def Contains(self, pt: System.Drawing.Point) -> bool:
        """
        Determines if the specified point is contained within the rectangular region defined by this
        System.Drawing.Rectangle .
        """
        ...

    @overload
    def Contains(self, rect: System.Drawing.Rectangle) -> bool:
        """
        Determines if the rectangular region represented by  is entirely contained within the
        rectangular region represented by this System.Drawing.Rectangle .
        """
        ...

    @overload
    def Equals(self, obj: typing.Any) -> bool:
        """
        Tests whether  is a System.Drawing.Rectangle with the same location
        and size of this Rectangle.
        """
        ...

    @overload
    def Equals(self, other: System.Drawing.Rectangle) -> bool:
        ...

    @staticmethod
    def FromLTRB(left: int, top: int, right: int, bottom: int) -> System.Drawing.Rectangle:
        """Creates a new System.Drawing.Rectangle with the specified location and size."""
        ...

    def GetHashCode(self) -> int:
        ...

    @overload
    def Inflate(self, width: int, height: int) -> None:
        """Inflates this System.Drawing.Rectangle by the specified amount."""
        ...

    @overload
    def Inflate(self, size: System.Drawing.Size) -> None:
        """Inflates this System.Drawing.Rectangle by the specified amount."""
        ...

    @staticmethod
    @overload
    def Inflate(rect: System.Drawing.Rectangle, x: int, y: int) -> System.Drawing.Rectangle:
        """Creates a System.Drawing.Rectangle that is inflated by the specified amount."""
        ...

    @overload
    def Intersect(self, rect: System.Drawing.Rectangle) -> None:
        """Creates a Rectangle that represents the intersection between this Rectangle and rect."""
        ...

    @staticmethod
    @overload
    def Intersect(a: System.Drawing.Rectangle, b: System.Drawing.Rectangle) -> System.Drawing.Rectangle:
        """
        Creates a rectangle that represents the intersection between a and b. If there is no intersection, an
        empty rectangle is returned.
        """
        ...

    def IntersectsWith(self, rect: System.Drawing.Rectangle) -> bool:
        """Determines if this rectangle intersects with rect."""
        ...

    @overload
    def Offset(self, pos: System.Drawing.Point) -> None:
        """Adjusts the location of this rectangle by the specified amount."""
        ...

    @overload
    def Offset(self, x: int, y: int) -> None:
        """Adjusts the location of this rectangle by the specified amount."""
        ...

    @staticmethod
    def Round(value: System.Drawing.RectangleF) -> System.Drawing.Rectangle:
        """Converts a RectangleF to a Rectangle by performing a round operation on all the coordinates."""
        ...

    def ToString(self) -> str:
        """Converts the attributes of this System.Drawing.Rectangle to a human readable string."""
        ...

    @staticmethod
    def Truncate(value: System.Drawing.RectangleF) -> System.Drawing.Rectangle:
        """Converts a RectangleF to a Rectangle by performing a truncate operation on all the coordinates."""
        ...

    @staticmethod
    def Union(a: System.Drawing.Rectangle, b: System.Drawing.Rectangle) -> System.Drawing.Rectangle:
        """Creates a rectangle that represents the union between a and b."""
        ...


class RectangleConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def CanConvertFrom(self, context: System.ComponentModel.ITypeDescriptorContext, sourceType: typing.Type) -> bool:
        ...

    def CanConvertTo(self, context: System.ComponentModel.ITypeDescriptorContext, destinationType: typing.Type) -> bool:
        ...

    def ConvertFrom(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def ConvertTo(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destinationType: typing.Type) -> System.Object:
        ...

    def CreateInstance(self, context: System.ComponentModel.ITypeDescriptorContext, propertyValues: System.Collections.IDictionary) -> System.Object:
        ...

    def GetCreateInstanceSupported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...

    def GetProperties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def GetPropertiesSupported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...


class SizeConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def CanConvertFrom(self, context: System.ComponentModel.ITypeDescriptorContext, sourceType: typing.Type) -> bool:
        ...

    def CanConvertTo(self, context: System.ComponentModel.ITypeDescriptorContext, destinationType: typing.Type) -> bool:
        ...

    def ConvertFrom(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def ConvertTo(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destinationType: typing.Type) -> System.Object:
        ...

    def CreateInstance(self, context: System.ComponentModel.ITypeDescriptorContext, propertyValues: System.Collections.IDictionary) -> System.Object:
        ...

    def GetCreateInstanceSupported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...

    def GetProperties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def GetPropertiesSupported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...


class PointConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def CanConvertFrom(self, context: System.ComponentModel.ITypeDescriptorContext, sourceType: typing.Type) -> bool:
        ...

    def CanConvertTo(self, context: System.ComponentModel.ITypeDescriptorContext, destinationType: typing.Type) -> bool:
        ...

    def ConvertFrom(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def ConvertTo(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destinationType: typing.Type) -> System.Object:
        ...

    def CreateInstance(self, context: System.ComponentModel.ITypeDescriptorContext, propertyValues: System.Collections.IDictionary) -> System.Object:
        ...

    def GetCreateInstanceSupported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...

    def GetProperties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def GetPropertiesSupported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...


class SizeFConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def CanConvertFrom(self, context: System.ComponentModel.ITypeDescriptorContext, sourceType: typing.Type) -> bool:
        ...

    def CanConvertTo(self, context: System.ComponentModel.ITypeDescriptorContext, destinationType: typing.Type) -> bool:
        ...

    def ConvertFrom(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def ConvertTo(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destinationType: typing.Type) -> System.Object:
        ...

    def CreateInstance(self, context: System.ComponentModel.ITypeDescriptorContext, propertyValues: System.Collections.IDictionary) -> System.Object:
        ...

    def GetCreateInstanceSupported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...

    def GetProperties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def GetPropertiesSupported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...


class ColorConverter(System.ComponentModel.TypeConverter):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def CanConvertFrom(self, context: System.ComponentModel.ITypeDescriptorContext, sourceType: typing.Type) -> bool:
        ...

    def CanConvertTo(self, context: System.ComponentModel.ITypeDescriptorContext, destinationType: typing.Type) -> bool:
        ...

    def ConvertFrom(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        ...

    def ConvertTo(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destinationType: typing.Type) -> System.Object:
        ...

    def GetStandardValues(self, context: System.ComponentModel.ITypeDescriptorContext) -> System.ComponentModel.TypeConverter.StandardValuesCollection:
        ...

    def GetStandardValuesSupported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        ...


