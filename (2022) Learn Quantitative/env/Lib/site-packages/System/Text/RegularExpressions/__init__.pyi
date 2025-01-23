from typing import overload
import abc
import datetime
import typing

import System
import System.Collections
import System.Collections.Generic
import System.Reflection
import System.Reflection.Emit
import System.Runtime.Serialization
import System.Text.RegularExpressions


class RegexParseException(System.ArgumentException):
    """
    An exception as a result of a parse error in a regular expression RegularExpressions, with
    detailed information in the Error and Offset properties.
    """

    @property
    def Error(self) -> int:
        """
        Gets the error that happened during parsing.
        
        This property contains the int value of a member of the System.Text.RegularExpressions.RegexParseError enum.
        """
        ...

    @property
    def Offset(self) -> int:
        """Gets the zero-based character offset in the regular expression pattern where the parse error occurs."""
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class RegexParseError(System.Enum):
    """
    Specifies the detailed underlying reason why a RegexParseException is thrown when a
    regular expression contains a parsing error.
    """

    Unknown = 0
    """An unknown regular expression parse error."""

    AlternationHasTooManyConditions = 1
    """An alternation in a regular expression has too many conditions."""

    AlternationHasMalformedCondition = 2
    """An alternation in a regular expression has a malformed condition."""

    InvalidUnicodePropertyEscape = 3
    """A Unicode property escape in a regular expression is invalid or unknown."""

    MalformedUnicodePropertyEscape = 4
    """A Unicode property escape is malformed."""

    UnrecognizedEscape = 5
    """An escape character or sequence in a regular expression is invalid."""

    UnrecognizedControlCharacter = 6
    """A control character in a regular expression is not recognized."""

    MissingControlCharacter = 7
    """A control character in a regular expression is missing."""

    InsufficientOrInvalidHexDigits = 8
    """A hexadecimal escape sequence in a regular expression does not have enough digits, or contains invalid digits."""

    QuantifierOrCaptureGroupOutOfRange = 9
    """A captured group or a quantifier in a regular expression is not within range, that is, it is larger than int.MaxValue."""

    UndefinedNamedReference = 10
    """A used named reference in a regular expression is not defined."""

    UndefinedNumberedReference = 11
    """A used numbered reference in a regular expression is not defined."""

    MalformedNamedReference = 12
    """A named reference in a regular expression is malformed."""

    UnescapedEndingBackslash = 13
    """A regular expression ends with a non-escaped ending backslash."""

    UnterminatedComment = 14
    """A comment in a regular expression is not terminated."""

    InvalidGroupingConstruct = 15
    """A grouping construct in a regular expression is invalid or malformed."""

    AlternationHasNamedCapture = 16
    """An alternation construct in a regular expression uses a named capture."""

    AlternationHasComment = 17
    """An alternation construct in a regular expression contains a comment."""

    AlternationHasMalformedReference = 18
    """An alternation construct in a regular expression contains a malformed reference."""

    AlternationHasUndefinedReference = 19
    """An alternation construct in a regular expression contains an undefined reference."""

    CaptureGroupNameInvalid = 20
    """The group name of a captured group in a regular expression is invalid."""

    CaptureGroupOfZero = 21
    """A regular expression defines a numbered subexpression named zero."""

    UnterminatedBracket = 22
    """A regular expression has a non-escaped left square bracket, or misses a closing right square bracket."""

    ExclusionGroupNotLast = 23
    """A character class in a regular expression with an exclusion group is not the last part of the character class."""

    ReversedCharacterRange = 24
    """A character class in a regular expression contains an inverse character range, like z-a instead of a-z."""

    ShorthandClassInCharacterRange = 25
    """A character-class in a regular expression contains a short-hand class that is not allowed inside a character class."""

    InsufficientClosingParentheses = 26
    """A regular expression has a non-escaped left parenthesis, or misses a closing right parenthesis."""

    ReversedQuantifierRange = 27
    """A quantifier range in a regular expression is inverse, like {10,1} instead of (1,10}."""

    NestedQuantifiersNotParenthesized = 28
    """Repeated quantifiers on another quantifier inside a regular expression are not grouped in parentheses."""

    QuantifierAfterNothing = 29
    """A quantifier in a regular expression is in a position where it cannot quantify anything, like at the beginning of a regular expression or in a group."""

    InsufficientOpeningParentheses = 30
    """A regular expression has a non-escaped right parenthesis, or misses an opening left parenthesis."""

    UnrecognizedUnicodeProperty = 31
    """A unicode property in a regular expression is not recognized, or invalid."""


class RegexOptions(System.Enum):
    """This class has no documentation."""

    # Cannot convert to Python: None = ...
    """Use default behavior."""

    IgnoreCase = ...
    """Use case-insensitive matching."""

    Multiline = ...
    """
    Use multiline mode, where ^ and $ match the beginning and end of each line
    (instead of the beginning and end of the input string).
    """

    ExplicitCapture = ...
    """
    Do not capture unnamed groups. The only valid captures are explicitly named
    or numbered groups of the form (?<name> subexpression).
    """

    Compiled = ...
    """Compile the regular expression to Microsoft intermediate language (MSIL)."""

    Singleline = ...
    """Use single-line mode, where the period (.) matches every character (instead of every character except \\n)."""

    IgnorePatternWhitespace = ...
    """Exclude unescaped white space from the pattern, and enable comments after a number sign (#)."""

    RightToLeft = ...
    """Change the search direction. Search moves from right to left instead of from left to right."""

    ECMAScript = ...
    """Enable ECMAScript-compliant behavior for the expression."""

    CultureInvariant = ...
    """Ignore cultural differences in language."""

    NonBacktracking = ...
    """
    Enable matching using an approach that avoids backtracking and guarantees linear-time processing
    in the length of the input.
    """


class RegexRunnerFactory(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __init__(self) -> None:
        """This method is protected."""
        ...


class Capture(System.Object):
    """
    Represents the results from a single subexpression capture. The object represents
    one substring for a single successful capture.
    """

    @property
    def Index(self) -> int:
        """Returns the position in the original string where the first character of captured substring was found."""
        ...

    @Index.setter
    def Index(self, value: int):
        """Returns the position in the original string where the first character of captured substring was found."""
        ...

    @property
    def Length(self) -> int:
        """Returns the length of the captured substring."""
        ...

    @Length.setter
    def Length(self, value: int):
        """Returns the length of the captured substring."""
        ...

    @property
    def Text(self) -> str:
        """The original string"""
        ...

    @Text.setter
    def Text(self, value: str):
        """The original string"""
        ...

    @property
    def Value(self) -> str:
        """Gets the captured substring from the input string."""
        ...

    @property
    def ValueSpan(self) -> System.ReadOnlySpan[str]:
        """Gets the captured span from the input string."""
        ...

    def ToString(self) -> str:
        """Returns the substring that was matched."""
        ...


class CaptureCollection(System.Object, System.Collections.Generic.IList[System.Text.RegularExpressions.Capture], System.Collections.Generic.IReadOnlyList[System.Text.RegularExpressions.Capture], System.Collections.IList, typing.Iterable[System.Text.RegularExpressions.Capture]):
    """
    Represents a sequence of capture substrings. The object is used
    to return the set of captures done by a single capturing group.
    """

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Count(self) -> int:
        """Returns the number of captures."""
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @overload
    def __getitem__(self, i: int) -> System.Text.RegularExpressions.Capture:
        """Returns a specific capture, by index, in this collection."""
        ...

    @overload
    def __getitem__(self, index: int) -> System.Text.RegularExpressions.Capture:
        ...

    @overload
    def __getitem__(self, index: int) -> typing.Any:
        ...

    @overload
    def __setitem__(self, index: int, value: System.Text.RegularExpressions.Capture) -> None:
        ...

    @overload
    def __setitem__(self, index: int, value: typing.Any) -> None:
        ...

    @overload
    def Add(self, item: System.Text.RegularExpressions.Capture) -> None:
        ...

    @overload
    def Add(self, value: typing.Any) -> int:
        ...

    @overload
    def Clear(self) -> None:
        ...

    @overload
    def Clear(self) -> None:
        ...

    @overload
    def Contains(self, item: System.Text.RegularExpressions.Capture) -> bool:
        ...

    @overload
    def Contains(self, value: typing.Any) -> bool:
        ...

    @overload
    def CopyTo(self, array: System.Array, arrayIndex: int) -> None:
        ...

    @overload
    def CopyTo(self, array: typing.List[System.Text.RegularExpressions.Capture], arrayIndex: int) -> None:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        """Provides an enumerator in the same order as Item[]."""
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System.Text.RegularExpressions.Capture]:
        ...

    @overload
    def IndexOf(self, item: System.Text.RegularExpressions.Capture) -> int:
        ...

    @overload
    def IndexOf(self, value: typing.Any) -> int:
        ...

    @overload
    def Insert(self, index: int, item: System.Text.RegularExpressions.Capture) -> None:
        ...

    @overload
    def Insert(self, index: int, value: typing.Any) -> None:
        ...

    @overload
    def Remove(self, item: System.Text.RegularExpressions.Capture) -> bool:
        ...

    @overload
    def Remove(self, value: typing.Any) -> None:
        ...

    @overload
    def RemoveAt(self, index: int) -> None:
        ...

    @overload
    def RemoveAt(self, index: int) -> None:
        ...


class Group(System.Text.RegularExpressions.Capture):
    """
    Represents the results from a single capturing group. A capturing group can
    capture zero, one, or more strings in a single match because of quantifiers, so
    Group supplies a collection of Capture objects.
    """

    s_emptyGroup: System.Text.RegularExpressions.Group = ...

    @property
    def _caps(self) -> typing.List[int]:
        ...

    @property
    def _capcount(self) -> int:
        ...

    @_capcount.setter
    def _capcount(self, value: int):
        ...

    @property
    def _capcoll(self) -> System.Text.RegularExpressions.CaptureCollection:
        ...

    @_capcoll.setter
    def _capcoll(self, value: System.Text.RegularExpressions.CaptureCollection):
        ...

    @property
    def Success(self) -> bool:
        """Indicates whether the match is successful."""
        ...

    @property
    def Name(self) -> str:
        ...

    @property
    def Captures(self) -> System.Text.RegularExpressions.CaptureCollection:
        """
        Returns a collection of all the captures matched by the capturing
        group, in innermost-leftmost-first order (or innermost-rightmost-first order if
        compiled with the "r" option). The collection may have zero or more items.
        """
        ...

    @staticmethod
    def Synchronized(inner: System.Text.RegularExpressions.Group) -> System.Text.RegularExpressions.Group:
        """Returns a Group object equivalent to the one supplied that is safe to share between multiple threads."""
        ...


class GroupCollection(System.Object, System.Collections.Generic.IList[System.Text.RegularExpressions.Group], System.Collections.Generic.IReadOnlyList[System.Text.RegularExpressions.Group], System.Collections.IList, System.Collections.Generic.IReadOnlyDictionary[str, System.Text.RegularExpressions.Group], typing.Iterable[System.Text.RegularExpressions.Group]):
    """
    Represents a sequence of capture substrings. The object is used
    to return the set of captures done by a single capturing group.
    """

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Count(self) -> int:
        """Returns the number of groups."""
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @property
    def Keys(self) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @property
    def Values(self) -> System.Collections.Generic.IEnumerable[System.Text.RegularExpressions.Group]:
        ...

    @overload
    def __getitem__(self, groupnum: int) -> System.Text.RegularExpressions.Group:
        ...

    @overload
    def __getitem__(self, groupname: str) -> System.Text.RegularExpressions.Group:
        ...

    @overload
    def __getitem__(self, index: int) -> System.Text.RegularExpressions.Group:
        ...

    @overload
    def __getitem__(self, index: int) -> typing.Any:
        ...

    @overload
    def __setitem__(self, index: int, value: System.Text.RegularExpressions.Group) -> None:
        ...

    @overload
    def __setitem__(self, index: int, value: typing.Any) -> None:
        ...

    @overload
    def Add(self, item: System.Text.RegularExpressions.Group) -> None:
        ...

    @overload
    def Add(self, value: typing.Any) -> int:
        ...

    @overload
    def Clear(self) -> None:
        ...

    @overload
    def Clear(self) -> None:
        ...

    @overload
    def Contains(self, item: System.Text.RegularExpressions.Group) -> bool:
        ...

    @overload
    def Contains(self, value: typing.Any) -> bool:
        ...

    def ContainsKey(self, key: str) -> bool:
        ...

    @overload
    def CopyTo(self, array: System.Array, arrayIndex: int) -> None:
        ...

    @overload
    def CopyTo(self, array: typing.List[System.Text.RegularExpressions.Group], arrayIndex: int) -> None:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        """Provides an enumerator in the same order as Item[]."""
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System.Text.RegularExpressions.Group]:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[str, System.Text.RegularExpressions.Group]]:
        ...

    @overload
    def IndexOf(self, item: System.Text.RegularExpressions.Group) -> int:
        ...

    @overload
    def IndexOf(self, value: typing.Any) -> int:
        ...

    @overload
    def Insert(self, index: int, item: System.Text.RegularExpressions.Group) -> None:
        ...

    @overload
    def Insert(self, index: int, value: typing.Any) -> None:
        ...

    @overload
    def Remove(self, item: System.Text.RegularExpressions.Group) -> bool:
        ...

    @overload
    def Remove(self, value: typing.Any) -> None:
        ...

    @overload
    def RemoveAt(self, index: int) -> None:
        ...

    @overload
    def RemoveAt(self, index: int) -> None:
        ...

    def TryGetValue(self, key: str, value: typing.Optional[System.Text.RegularExpressions.Group]) -> typing.Union[bool, System.Text.RegularExpressions.Group]:
        ...


class Match(System.Text.RegularExpressions.Group):
    """Represents the results from a single regular expression match."""

    @property
    def _groupcoll(self) -> System.Text.RegularExpressions.GroupCollection:
        ...

    @_groupcoll.setter
    def _groupcoll(self, value: System.Text.RegularExpressions.GroupCollection):
        ...

    @property
    def _regex(self) -> System.Text.RegularExpressions.Regex:
        ...

    @property
    def _textbeg(self) -> int:
        ...

    @_textbeg.setter
    def _textbeg(self, value: int):
        ...

    @property
    def _textpos(self) -> int:
        ...

    @_textpos.setter
    def _textpos(self, value: int):
        ...

    @property
    def _textend(self) -> int:
        ...

    @_textend.setter
    def _textend(self, value: int):
        ...

    @property
    def _matches(self) -> typing.List[typing.List[int]]:
        ...

    @property
    def _matchcount(self) -> typing.List[int]:
        ...

    @property
    def _balancing(self) -> bool:
        ...

    @_balancing.setter
    def _balancing(self, value: bool):
        ...

    Empty: System.Text.RegularExpressions.Match
    """Returns an empty Match object."""

    @property
    def FoundMatch(self) -> bool:
        """Returns true if this object represents a successful match, and false otherwise."""
        ...

    @property
    def Groups(self) -> System.Text.RegularExpressions.GroupCollection:
        ...

    def NextMatch(self) -> System.Text.RegularExpressions.Match:
        """
        Returns a new Match with the results for the next match, starting
        at the position at which the last match ended (at the character beyond the last
        matched character).
        """
        ...

    def Result(self, replacement: str) -> str:
        """
        Returns the expansion of the passed replacement pattern. For
        example, if the replacement pattern is ?$1$2?, Result returns the concatenation
        of Group(1).ToString() and Group(2).ToString().
        """
        ...

    @staticmethod
    def Synchronized(inner: System.Text.RegularExpressions.Match) -> System.Text.RegularExpressions.Match:
        """
        Returns a Match instance equivalent to the one supplied that is safe to share
        between multiple threads.
        """
        ...


class MatchCollection(System.Object, System.Collections.Generic.IList[System.Text.RegularExpressions.Match], System.Collections.Generic.IReadOnlyList[System.Text.RegularExpressions.Match], System.Collections.IList, typing.Iterable[System.Text.RegularExpressions.Match]):
    """
    Represents the set of names appearing as capturing group
    names in a regular expression.
    """

    @property
    def IsReadOnly(self) -> bool:
        ...

    @property
    def Count(self) -> int:
        """Returns the number of captures."""
        ...

    @property
    def IsSynchronized(self) -> bool:
        ...

    @property
    def SyncRoot(self) -> System.Object:
        ...

    @property
    def IsFixedSize(self) -> bool:
        ...

    @overload
    def __getitem__(self, i: int) -> System.Text.RegularExpressions.Match:
        """Returns the ith Match in the collection."""
        ...

    @overload
    def __getitem__(self, index: int) -> System.Text.RegularExpressions.Match:
        ...

    @overload
    def __getitem__(self, index: int) -> typing.Any:
        ...

    @overload
    def __setitem__(self, index: int, value: System.Text.RegularExpressions.Match) -> None:
        ...

    @overload
    def __setitem__(self, index: int, value: typing.Any) -> None:
        ...

    @overload
    def Add(self, item: System.Text.RegularExpressions.Match) -> None:
        ...

    @overload
    def Add(self, value: typing.Any) -> int:
        ...

    @overload
    def Clear(self) -> None:
        ...

    @overload
    def Clear(self) -> None:
        ...

    @overload
    def Contains(self, item: System.Text.RegularExpressions.Match) -> bool:
        ...

    @overload
    def Contains(self, value: typing.Any) -> bool:
        ...

    @overload
    def CopyTo(self, array: System.Array, arrayIndex: int) -> None:
        ...

    @overload
    def CopyTo(self, array: typing.List[System.Text.RegularExpressions.Match], arrayIndex: int) -> None:
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.IEnumerator:
        """Provides an enumerator in the same order as Item[i]."""
        ...

    @overload
    def GetEnumerator(self) -> System.Collections.Generic.IEnumerator[System.Text.RegularExpressions.Match]:
        ...

    @overload
    def IndexOf(self, item: System.Text.RegularExpressions.Match) -> int:
        ...

    @overload
    def IndexOf(self, value: typing.Any) -> int:
        ...

    @overload
    def Insert(self, index: int, item: System.Text.RegularExpressions.Match) -> None:
        ...

    @overload
    def Insert(self, index: int, value: typing.Any) -> None:
        ...

    @overload
    def Remove(self, item: System.Text.RegularExpressions.Match) -> bool:
        ...

    @overload
    def Remove(self, value: typing.Any) -> None:
        ...

    @overload
    def RemoveAt(self, index: int) -> None:
        ...

    @overload
    def RemoveAt(self, index: int) -> None:
        ...


class RegexCompilationInfo(System.Object):
    """Obsoletions.RegexCompileToAssemblyMessage"""

    @property
    def IsPublic(self) -> bool:
        ...

    @IsPublic.setter
    def IsPublic(self, value: bool):
        ...

    @property
    def MatchTimeout(self) -> datetime.timedelta:
        ...

    @MatchTimeout.setter
    def MatchTimeout(self, value: datetime.timedelta):
        ...

    @property
    def Name(self) -> str:
        ...

    @Name.setter
    def Name(self, value: str):
        ...

    @property
    def Namespace(self) -> str:
        ...

    @Namespace.setter
    def Namespace(self, value: str):
        ...

    @property
    def Options(self) -> int:
        """This property contains the int value of a member of the System.Text.RegularExpressions.RegexOptions enum."""
        ...

    @Options.setter
    def Options(self, value: int):
        """This property contains the int value of a member of the System.Text.RegularExpressions.RegexOptions enum."""
        ...

    @property
    def Pattern(self) -> str:
        ...

    @Pattern.setter
    def Pattern(self, value: str):
        ...

    @overload
    def __init__(self, pattern: str, options: System.Text.RegularExpressions.RegexOptions, name: str, fullnamespace: str, ispublic: bool) -> None:
        ...

    @overload
    def __init__(self, pattern: str, options: System.Text.RegularExpressions.RegexOptions, name: str, fullnamespace: str, ispublic: bool, matchTimeout: datetime.timedelta) -> None:
        ...


class ValueMatch:
    """Represents the results from a single regular expression match."""

    @property
    def Index(self) -> int:
        """Gets the position in the original span where the first character of the captured sliced span is found."""
        ...

    @property
    def Length(self) -> int:
        """Gets the length of the captured sliced span."""
        ...


class Regex(System.Object, System.Runtime.Serialization.ISerializable):
    """
    Represents an immutable regular expression. Also contains static methods that
    allow use of regular expressions without instantiating a Regex explicitly.
    """

    class ValueMatchEnumerator:
        """Represents an enumerator containing the set of successful matches found by iteratively applying a regular expression pattern to the input span."""

        @property
        def Current(self) -> System.Text.RegularExpressions.ValueMatch:
            """Gets the ValueMatch element at the current position of the enumerator."""
            ...

        def GetEnumerator(self) -> System.Text.RegularExpressions.Regex.ValueMatchEnumerator:
            """
            Provides an enumerator that iterates through the matches in the input span.
            
            :returns: A copy of this enumerator.
            """
            ...

        def MoveNext(self) -> bool:
            """
            Advances the enumerator to the next match in the span.
            
            :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator cannot find additional matches.
            """
            ...

    @property
    def pattern(self) -> str:
        """This field is protected."""
        ...

    @pattern.setter
    def pattern(self, value: str):
        """This field is protected."""
        ...

    @property
    def roptions(self) -> System.Text.RegularExpressions.RegexOptions:
        """This field is protected."""
        ...

    @roptions.setter
    def roptions(self, value: System.Text.RegularExpressions.RegexOptions):
        """This field is protected."""
        ...

    @property
    def factory(self) -> System.Text.RegularExpressions.RegexRunnerFactory:
        """This field is protected."""
        ...

    @factory.setter
    def factory(self, value: System.Text.RegularExpressions.RegexRunnerFactory):
        """This field is protected."""
        ...

    @property
    def caps(self) -> System.Collections.Hashtable:
        """This field is protected."""
        ...

    @caps.setter
    def caps(self, value: System.Collections.Hashtable):
        """This field is protected."""
        ...

    @property
    def capnames(self) -> System.Collections.Hashtable:
        """This field is protected."""
        ...

    @capnames.setter
    def capnames(self, value: System.Collections.Hashtable):
        """This field is protected."""
        ...

    @property
    def capslist(self) -> typing.List[str]:
        """This field is protected."""
        ...

    @capslist.setter
    def capslist(self, value: typing.List[str]):
        """This field is protected."""
        ...

    @property
    def capsize(self) -> int:
        """This field is protected."""
        ...

    @capsize.setter
    def capsize(self, value: int):
        """This field is protected."""
        ...

    @property
    def Caps(self) -> System.Collections.IDictionary:
        """This property is protected."""
        ...

    @Caps.setter
    def Caps(self, value: System.Collections.IDictionary):
        """This property is protected."""
        ...

    @property
    def CapNames(self) -> System.Collections.IDictionary:
        """This property is protected."""
        ...

    @CapNames.setter
    def CapNames(self, value: System.Collections.IDictionary):
        """This property is protected."""
        ...

    @property
    def Options(self) -> int:
        """
        Returns the options passed into the constructor
        
        This property contains the int value of a member of the System.Text.RegularExpressions.RegexOptions enum.
        """
        ...

    @property
    def RightToLeft(self) -> bool:
        """Indicates whether the regular expression matches from right to left."""
        ...

    @property
    def RegexReplacementWeakReference(self) -> System.WeakReference[System.Text.RegularExpressions.RegexReplacement]:
        """A weak reference to a regex replacement, lazily initialized."""
        ...

    CacheSize: int

    InfiniteMatchTimeout: datetime.timedelta = ...

    s_defaultMatchTimeout: datetime.timedelta = ...
    """
    The default timeout value to use if one isn't explicitly specified when creating the Regex
    or using its static methods (which implicitly create one if one can't be found in the cache).
    """

    @property
    def internalMatchTimeout(self) -> datetime.timedelta:
        """
        Timeout for the execution of this Regex.
        
        This field is protected.
        """
        ...

    @internalMatchTimeout.setter
    def internalMatchTimeout(self, value: datetime.timedelta):
        """
        Timeout for the execution of this Regex.
        
        This field is protected.
        """
        ...

    @property
    def MatchTimeout(self) -> datetime.timedelta:
        """Gets the timeout interval of the current instance."""
        ...

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, pattern: str) -> None:
        """Creates a regular expression object for the specified regular expression."""
        ...

    @overload
    def __init__(self, pattern: str, options: System.Text.RegularExpressions.RegexOptions) -> None:
        """Creates a regular expression object for the specified regular expression, with options that modify the pattern."""
        ...

    @overload
    def __init__(self, pattern: str, options: System.Text.RegularExpressions.RegexOptions, matchTimeout: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...

    @staticmethod
    @overload
    def CompileToAssembly(regexinfos: typing.List[System.Text.RegularExpressions.RegexCompilationInfo], assemblyname: System.Reflection.AssemblyName) -> None:
        """Obsoletions.RegexCompileToAssemblyMessage"""
        ...

    @staticmethod
    @overload
    def CompileToAssembly(regexinfos: typing.List[System.Text.RegularExpressions.RegexCompilationInfo], assemblyname: System.Reflection.AssemblyName, attributes: typing.List[System.Reflection.Emit.CustomAttributeBuilder]) -> None:
        """Obsoletions.RegexCompileToAssemblyMessage"""
        ...

    @staticmethod
    @overload
    def CompileToAssembly(regexinfos: typing.List[System.Text.RegularExpressions.RegexCompilationInfo], assemblyname: System.Reflection.AssemblyName, attributes: typing.List[System.Reflection.Emit.CustomAttributeBuilder], resourceFile: str) -> None:
        """Obsoletions.RegexCompileToAssemblyMessage"""
        ...

    @overload
    def Count(self, input: str) -> int:
        """
        Searches an input string for all occurrences of a regular expression and returns the number of matches.
        
        :param input: The string to search for a match.
        :returns: The number of matches.
        """
        ...

    @overload
    def Count(self, input: System.ReadOnlySpan[str]) -> int:
        """
        Searches an input span for all occurrences of a regular expression and returns the number of matches.
        
        :param input: The span to search for a match.
        :returns: The number of matches.
        """
        ...

    @overload
    def Count(self, input: System.ReadOnlySpan[str], startat: int) -> int:
        """
        Searches an input span for all occurrences of a regular expression and returns the number of matches.
        
        :param input: The span to search for a match.
        :param startat: The zero-based character position at which to start the search.
        :returns: The number of matches.
        """
        ...

    @staticmethod
    @overload
    def Count(input: str, pattern: str) -> int:
        """
        Searches an input string for all occurrences of a regular expression and returns the number of matches.
        
        :param input: The string to search for a match.
        :param pattern: The regular expression pattern to match.
        :returns: The number of matches.
        """
        ...

    @staticmethod
    @overload
    def Count(input: str, pattern: str, options: System.Text.RegularExpressions.RegexOptions) -> int:
        """
        Searches an input string for all occurrences of a regular expression and returns the number of matches.
        
        :param input: The string to search for a match.
        :param pattern: The regular expression pattern to match.
        :param options: A bitwise combination of the enumeration values that specify options for matching.
        :returns: The number of matches.
        """
        ...

    @staticmethod
    @overload
    def Count(input: str, pattern: str, options: System.Text.RegularExpressions.RegexOptions, matchTimeout: datetime.timedelta) -> int:
        """
        Searches an input string for all occurrences of a regular expression and returns the number of matches.
        
        :param input: The string to search for a match.
        :param pattern: The regular expression pattern to match.
        :param options: A bitwise combination of the enumeration values that specify options for matching.
        :param matchTimeout: A time-out interval, or InfiniteMatchTimeout to indicate that the method should not time out.
        :returns: The number of matches.
        """
        ...

    @staticmethod
    @overload
    def Count(input: System.ReadOnlySpan[str], pattern: str) -> int:
        """
        Searches an input span for all occurrences of a regular expression and returns the number of matches.
        
        :param input: The span to search for a match.
        :param pattern: The regular expression pattern to match.
        :returns: The number of matches.
        """
        ...

    @staticmethod
    @overload
    def Count(input: System.ReadOnlySpan[str], pattern: str, options: System.Text.RegularExpressions.RegexOptions) -> int:
        """
        Searches an input span for all occurrences of a regular expression and returns the number of matches.
        
        :param input: The span to search for a match.
        :param pattern: The regular expression pattern to match.
        :param options: A bitwise combination of the enumeration values that specify options for matching.
        :returns: The number of matches.
        """
        ...

    @staticmethod
    @overload
    def Count(input: System.ReadOnlySpan[str], pattern: str, options: System.Text.RegularExpressions.RegexOptions, matchTimeout: datetime.timedelta) -> int:
        """
        Searches an input span for all occurrences of a regular expression and returns the number of matches.
        
        :param input: The span to search for a match.
        :param pattern: The regular expression pattern to match.
        :param options: A bitwise combination of the enumeration values that specify options for matching.
        :param matchTimeout: A time-out interval, or InfiniteMatchTimeout to indicate that the method should not time out.
        :returns: The number of matches.
        """
        ...

    @staticmethod
    @overload
    def EnumerateMatches(input: System.ReadOnlySpan[str], pattern: str) -> System.Text.RegularExpressions.Regex.ValueMatchEnumerator:
        """
        Searches an input span for all occurrences of a regular expression and returns a ValueMatchEnumerator to iterate over the matches.
        
        :param input: The span to search for a match.
        :param pattern: The regular expression pattern to match.
        :returns: A ValueMatchEnumerator to iterate over the matches.
        """
        ...

    @staticmethod
    @overload
    def EnumerateMatches(input: System.ReadOnlySpan[str], pattern: str, options: System.Text.RegularExpressions.RegexOptions) -> System.Text.RegularExpressions.Regex.ValueMatchEnumerator:
        """
        Searches an input span for all occurrences of a regular expression and returns a ValueMatchEnumerator to iterate over the matches.
        
        :param input: The span to search for a match.
        :param pattern: The regular expression pattern to match.
        :param options: A bitwise combination of the enumeration values that specify options for matching.
        :returns: A ValueMatchEnumerator to iterate over the matches.
        """
        ...

    @staticmethod
    @overload
    def EnumerateMatches(input: System.ReadOnlySpan[str], pattern: str, options: System.Text.RegularExpressions.RegexOptions, matchTimeout: datetime.timedelta) -> System.Text.RegularExpressions.Regex.ValueMatchEnumerator:
        """
        Searches an input span for all occurrences of a regular expression and returns a ValueMatchEnumerator to iterate over the matches.
        
        :param input: The span to search for a match.
        :param pattern: The regular expression pattern to match.
        :param options: A bitwise combination of the enumeration values that specify options for matching.
        :param matchTimeout: A time-out interval, or InfiniteMatchTimeout to indicate that the method should not time out.
        :returns: A ValueMatchEnumerator to iterate over the matches.
        """
        ...

    @overload
    def EnumerateMatches(self, input: System.ReadOnlySpan[str]) -> System.Text.RegularExpressions.Regex.ValueMatchEnumerator:
        """
        Searches an input span for all occurrences of a regular expression and returns a ValueMatchEnumerator to iterate over the matches.
        
        :param input: The span to search for a match.
        :returns: A ValueMatchEnumerator to iterate over the matches.
        """
        ...

    @overload
    def EnumerateMatches(self, input: System.ReadOnlySpan[str], startat: int) -> System.Text.RegularExpressions.Regex.ValueMatchEnumerator:
        """
        Searches an input span for all occurrences of a regular expression and returns a ValueMatchEnumerator to iterate over the matches.
        
        :param input: The span to search for a match.
        :param startat: The zero-based character position at which to start the search.
        :returns: A ValueMatchEnumerator to iterate over the matches.
        """
        ...

    @staticmethod
    def Escape(str: str) -> str:
        """
        Escapes a minimal set of metacharacters (\\, *, +, ?, |, {, [, (, ), ^, $, ., #, and
        whitespace) by replacing them with their \\ codes. This converts a string so that
        it can be used as a constant within a regular expression safely. (Note that the
        reason # and whitespace must be escaped is so the string can be used safely
        within an expression parsed with x mode. If future Regex features add
        additional metacharacters, developers should depend on Escape to escape those
        characters as well.)
        """
        ...

    def GetGroupNames(self) -> typing.List[str]:
        """
        Returns the GroupNameCollection for the regular expression. This collection contains the
        set of strings used to name capturing groups in the expression.
        """
        ...

    def GetGroupNumbers(self) -> typing.List[int]:
        """Returns the integer group number corresponding to a group name."""
        ...

    def GetObjectData(self, si: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def GroupNameFromNumber(self, i: int) -> str:
        """Retrieves a group name that corresponds to a group number."""
        ...

    def GroupNumberFromName(self, name: str) -> int:
        """Returns a group number that corresponds to a group name, or -1 if the name is not a recognized group name."""
        ...

    def InitializeReferences(self) -> None:
        """This method is protected."""
        ...

    @staticmethod
    @overload
    def IsMatch(input: str, pattern: str) -> bool:
        """Searches the input string for one or more occurrences of the text supplied in the given pattern."""
        ...

    @staticmethod
    @overload
    def IsMatch(input: System.ReadOnlySpan[str], pattern: str) -> bool:
        """
        Indicates whether the specified regular expression finds a match in the specified input span.
        
        :param input: The span to search for a match.
        :param pattern: The regular expression pattern to match.
        :returns: true if the regular expression finds a match; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def IsMatch(input: str, pattern: str, options: System.Text.RegularExpressions.RegexOptions) -> bool:
        """
        Searches the input string for one or more occurrences of the text
        supplied in the pattern parameter with matching options supplied in the options
        parameter.
        """
        ...

    @staticmethod
    @overload
    def IsMatch(input: System.ReadOnlySpan[str], pattern: str, options: System.Text.RegularExpressions.RegexOptions) -> bool:
        """
        Indicates whether the specified regular expression finds a match in the specified input span, using the specified matching options.
        
        :param input: The span to search for a match.
        :param pattern: The regular expression pattern to match.
        :param options: A bitwise combination of the enumeration values that provide options for matching.
        :returns: true if the regular expression finds a match; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def IsMatch(input: str, pattern: str, options: System.Text.RegularExpressions.RegexOptions, matchTimeout: datetime.timedelta) -> bool:
        ...

    @staticmethod
    @overload
    def IsMatch(input: System.ReadOnlySpan[str], pattern: str, options: System.Text.RegularExpressions.RegexOptions, matchTimeout: datetime.timedelta) -> bool:
        """
        Indicates whether the specified regular expression finds a match in the specified input span, using the specified matching options and time-out interval.
        
        :param input: The span to search for a match.
        :param pattern: The regular expression pattern to match.
        :param options: A bitwise combination of the enumeration values that provide options for matching.
        :param matchTimeout: A time-out interval, or Regex.InfiniteMatchTimeout to indicate that the method should not time out.
        :returns: true if the regular expression finds a match; otherwise, false.
        """
        ...

    @overload
    def IsMatch(self, input: str) -> bool:
        """
        Searches the input string for one or more matches using the previous pattern,
        options, and starting position.
        """
        ...

    @overload
    def IsMatch(self, input: str, startat: int) -> bool:
        """
        Searches the input string for one or more matches using the previous pattern and options,
        with a new starting position.
        """
        ...

    @overload
    def IsMatch(self, input: System.ReadOnlySpan[str]) -> bool:
        """
        Indicates whether the regular expression specified in the Regex constructor finds a match in a specified input span.
        
        :param input: The span to search for a match.
        :returns: true if the regular expression finds a match; otherwise, false.
        """
        ...

    @overload
    def IsMatch(self, input: System.ReadOnlySpan[str], startat: int) -> bool:
        """
        Indicates whether the regular expression specified in the Regex constructor finds a match in a specified input span.
        
        :param input: The span to search for a match.
        :param startat: The zero-based character position at which to start the search.
        :returns: true if the regular expression finds a match; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def Match(input: str, pattern: str) -> System.Text.RegularExpressions.Match:
        """
        Searches the input string for one or more occurrences of the text
        supplied in the pattern parameter.
        """
        ...

    @staticmethod
    @overload
    def Match(input: str, pattern: str, options: System.Text.RegularExpressions.RegexOptions) -> System.Text.RegularExpressions.Match:
        """
        Searches the input string for one or more occurrences of the text
        supplied in the pattern parameter. Matching is modified with an option
        string.
        """
        ...

    @staticmethod
    @overload
    def Match(input: str, pattern: str, options: System.Text.RegularExpressions.RegexOptions, matchTimeout: datetime.timedelta) -> System.Text.RegularExpressions.Match:
        ...

    @overload
    def Match(self, input: str) -> System.Text.RegularExpressions.Match:
        """
        Matches a regular expression with a string and returns
        the precise result as a Match object.
        """
        ...

    @overload
    def Match(self, input: str, startat: int) -> System.Text.RegularExpressions.Match:
        """
        Matches a regular expression with a string and returns
        the precise result as a Match object.
        """
        ...

    @overload
    def Match(self, input: str, beginning: int, length: int) -> System.Text.RegularExpressions.Match:
        """Matches a regular expression with a string and returns the precise result as a Match object."""
        ...

    @staticmethod
    @overload
    def Matches(input: str, pattern: str) -> System.Text.RegularExpressions.MatchCollection:
        """Returns all the successful matches as if Match were called iteratively numerous times."""
        ...

    @staticmethod
    @overload
    def Matches(input: str, pattern: str, options: System.Text.RegularExpressions.RegexOptions) -> System.Text.RegularExpressions.MatchCollection:
        """Returns all the successful matches as if Match were called iteratively numerous times."""
        ...

    @staticmethod
    @overload
    def Matches(input: str, pattern: str, options: System.Text.RegularExpressions.RegexOptions, matchTimeout: datetime.timedelta) -> System.Text.RegularExpressions.MatchCollection:
        ...

    @overload
    def Matches(self, input: str) -> System.Text.RegularExpressions.MatchCollection:
        """Returns all the successful matches as if Match was called iteratively numerous times."""
        ...

    @overload
    def Matches(self, input: str, startat: int) -> System.Text.RegularExpressions.MatchCollection:
        """Returns all the successful matches as if Match was called iteratively numerous times."""
        ...

    @staticmethod
    @overload
    def Replace(input: str, pattern: str, replacement: str) -> str:
        """
        Replaces all occurrences of the pattern with the  pattern, starting at
        the first character in the input string.
        """
        ...

    @staticmethod
    @overload
    def Replace(input: str, pattern: str, replacement: str, options: System.Text.RegularExpressions.RegexOptions) -> str:
        """
        Replaces all occurrences of
        the with the 
        pattern, starting at the first character in the input string.
        """
        ...

    @staticmethod
    @overload
    def Replace(input: str, pattern: str, replacement: str, options: System.Text.RegularExpressions.RegexOptions, matchTimeout: datetime.timedelta) -> str:
        ...

    @overload
    def Replace(self, input: str, replacement: str) -> str:
        """
        Replaces all occurrences of the previously defined pattern with the
         pattern, starting at the first character in the
        input string.
        """
        ...

    @overload
    def Replace(self, input: str, replacement: str, count: int) -> str:
        """
        Replaces all occurrences of the previously defined pattern with the
         pattern, starting at the first character in the
        input string.
        """
        ...

    @overload
    def Replace(self, input: str, replacement: str, count: int, startat: int) -> str:
        """
        Replaces all occurrences of the previously defined pattern with the
         pattern, starting at the character position
        .
        """
        ...

    @staticmethod
    @overload
    def Replace(input: str, pattern: str, evaluator: typing.Callable[[System.Text.RegularExpressions.Match], str]) -> str:
        """
        Replaces all occurrences of the  with the recent
        replacement pattern.
        """
        ...

    @staticmethod
    @overload
    def Replace(input: str, pattern: str, evaluator: typing.Callable[[System.Text.RegularExpressions.Match], str], options: System.Text.RegularExpressions.RegexOptions) -> str:
        """
        Replaces all occurrences of the  with the recent
        replacement pattern, starting at the first character.
        """
        ...

    @staticmethod
    @overload
    def Replace(input: str, pattern: str, evaluator: typing.Callable[[System.Text.RegularExpressions.Match], str], options: System.Text.RegularExpressions.RegexOptions, matchTimeout: datetime.timedelta) -> str:
        ...

    @overload
    def Replace(self, input: str, evaluator: typing.Callable[[System.Text.RegularExpressions.Match], str]) -> str:
        """
        Replaces all occurrences of the previously defined pattern with the recent
        replacement pattern, starting at the first character position.
        """
        ...

    @overload
    def Replace(self, input: str, evaluator: typing.Callable[[System.Text.RegularExpressions.Match], str], count: int) -> str:
        """
        Replaces all occurrences of the previously defined pattern with the recent
        replacement pattern, starting at the first character position.
        """
        ...

    @overload
    def Replace(self, input: str, evaluator: typing.Callable[[System.Text.RegularExpressions.Match], str], count: int, startat: int) -> str:
        """
        Replaces all occurrences of the previously defined pattern with the recent
        replacement pattern, starting at the character position
        .
        """
        ...

    @staticmethod
    @overload
    def Split(input: str, pattern: str) -> typing.List[str]:
        """
        Splits the string at the position defined
        by .
        """
        ...

    @staticmethod
    @overload
    def Split(input: str, pattern: str, options: System.Text.RegularExpressions.RegexOptions) -> typing.List[str]:
        """Splits the string at the position defined by ."""
        ...

    @staticmethod
    @overload
    def Split(input: str, pattern: str, options: System.Text.RegularExpressions.RegexOptions, matchTimeout: datetime.timedelta) -> typing.List[str]:
        ...

    @overload
    def Split(self, input: str) -> typing.List[str]:
        """
        Splits the  string at the position defined by a
        previous pattern.
        """
        ...

    @overload
    def Split(self, input: str, count: int) -> typing.List[str]:
        """
        Splits the  string at the position defined by a
        previous pattern.
        """
        ...

    @overload
    def Split(self, input: str, count: int, startat: int) -> typing.List[str]:
        """Splits the  string at the position defined by a previous pattern."""
        ...

    def ToString(self) -> str:
        """Returns the regular expression pattern passed into the constructor"""
        ...

    @staticmethod
    def Unescape(str: str) -> str:
        """Unescapes any escaped characters in the input string."""
        ...

    def UseOptionC(self) -> bool:
        """
        True if the RegexOptions.Compiled option was set.
        
        This method is protected.
        """
        ...


class RegexRunner(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def runtextbeg(self) -> int:
        """This field is protected."""
        ...

    @runtextbeg.setter
    def runtextbeg(self, value: int):
        """This field is protected."""
        ...

    @property
    def runtextend(self) -> int:
        """This field is protected."""
        ...

    @runtextend.setter
    def runtextend(self, value: int):
        """This field is protected."""
        ...

    @property
    def runtextstart(self) -> int:
        """This field is protected."""
        ...

    @runtextstart.setter
    def runtextstart(self, value: int):
        """This field is protected."""
        ...

    @property
    def runtext(self) -> str:
        """This field is protected."""
        ...

    @runtext.setter
    def runtext(self, value: str):
        """This field is protected."""
        ...

    @property
    def runtextpos(self) -> int:
        """This field is protected."""
        ...

    @runtextpos.setter
    def runtextpos(self, value: int):
        """This field is protected."""
        ...

    @property
    def runtrack(self) -> typing.List[int]:
        """This field is protected."""
        ...

    @runtrack.setter
    def runtrack(self, value: typing.List[int]):
        """This field is protected."""
        ...

    @property
    def runtrackpos(self) -> int:
        """This field is protected."""
        ...

    @runtrackpos.setter
    def runtrackpos(self, value: int):
        """This field is protected."""
        ...

    @property
    def runstack(self) -> typing.List[int]:
        """This field is protected."""
        ...

    @runstack.setter
    def runstack(self, value: typing.List[int]):
        """This field is protected."""
        ...

    @property
    def runstackpos(self) -> int:
        """This field is protected."""
        ...

    @runstackpos.setter
    def runstackpos(self, value: int):
        """This field is protected."""
        ...

    @property
    def runcrawl(self) -> typing.List[int]:
        """This field is protected."""
        ...

    @runcrawl.setter
    def runcrawl(self, value: typing.List[int]):
        """This field is protected."""
        ...

    @property
    def runcrawlpos(self) -> int:
        """This field is protected."""
        ...

    @runcrawlpos.setter
    def runcrawlpos(self, value: int):
        """This field is protected."""
        ...

    @property
    def runtrackcount(self) -> int:
        """This field is protected."""
        ...

    @runtrackcount.setter
    def runtrackcount(self, value: int):
        """This field is protected."""
        ...

    @property
    def runmatch(self) -> System.Text.RegularExpressions.Match:
        """This field is protected."""
        ...

    @runmatch.setter
    def runmatch(self, value: System.Text.RegularExpressions.Match):
        """This field is protected."""
        ...

    @property
    def runregex(self) -> System.Text.RegularExpressions.Regex:
        """This field is protected."""
        ...

    @runregex.setter
    def runregex(self, value: System.Text.RegularExpressions.Regex):
        """This field is protected."""
        ...

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def Capture(self, capnum: int, start: int, end: int) -> None:
        """
        Called by Go() to capture a subexpression. Note that the
        capnum used here has already been mapped to a non-sparse
        index (by the code generator RegexWriter).
        
        This method is protected.
        """
        ...

    @staticmethod
    def CharInClass(ch: str, charClass: str) -> bool:
        """This method is protected."""
        ...

    @staticmethod
    def CharInSet(ch: str, set: str, category: str) -> bool:
        """This method is protected."""
        ...

    def Crawl(self, i: int) -> None:
        """
        Save a number on the longjump unrolling stack
        
        This method is protected.
        """
        ...

    def Crawlpos(self) -> int:
        """
        Get the height of the stack
        
        This method is protected.
        """
        ...

    def DoubleCrawl(self) -> None:
        """
        Increases the size of the longjump unrolling stack.
        
        This method is protected.
        """
        ...

    def DoubleStack(self) -> None:
        """
        Called by the implementation of Go() to increase the size of the
        grouping stack.
        
        This method is protected.
        """
        ...

    def DoubleTrack(self) -> None:
        """
        Called by the implementation of Go() to increase the size of the
        backtracking stack.
        
        This method is protected.
        """
        ...

    def EnsureStorage(self) -> None:
        """
        Called by the implementation of Go() to increase the size of storage
        
        This method is protected.
        """
        ...

    def FindFirstChar(self) -> bool:
        """
        The responsibility of FindFirstChar() is to advance runtextpos
        until it is at the next position which is a candidate for the
        beginning of a successful match.
        
        This method is protected.
        """
        ...

    def Go(self) -> None:
        """
        The responsibility of Go() is to run the regular expression at
        runtextpos and call Capture() on all the captured subexpressions,
        then to leave runtextpos at the ending position. It should leave
        runtextpos where it started if there was no match.
        
        This method is protected.
        """
        ...

    def InitTrackCount(self) -> None:
        """
        InitTrackCount must initialize the runtrackcount field; this is
        used to know how large the initial runtrack and runstack arrays
        must be.
        
        This method is protected.
        """
        ...

    def IsBoundary(self, index: int, startpos: int, endpos: int) -> bool:
        """
        Called by the implementation of Go() to decide whether the pos
        at the specified index is a boundary or not. It's just not worth
        emitting inline code for this logic.
        
        This method is protected.
        """
        ...

    def IsECMABoundary(self, index: int, startpos: int, endpos: int) -> bool:
        """This method is protected."""
        ...

    def IsMatched(self, cap: int) -> bool:
        """
        Call out to runmatch to get around visibility issues
        
        This method is protected.
        """
        ...

    def MatchIndex(self, cap: int) -> int:
        """
        Call out to runmatch to get around visibility issues
        
        This method is protected.
        """
        ...

    def MatchLength(self, cap: int) -> int:
        """
        Call out to runmatch to get around visibility issues
        
        This method is protected.
        """
        ...

    def Popcrawl(self) -> int:
        """
        Remove a number from the longjump unrolling stack
        
        This method is protected.
        """
        ...

    def Scan(self, regex: System.Text.RegularExpressions.Regex, text: str, textbeg: int, textend: int, textstart: int, prevlen: int, quick: bool) -> System.Text.RegularExpressions.Match:
        """This method is protected."""
        ...

    def TransferCapture(self, capnum: int, uncapnum: int, start: int, end: int) -> None:
        """
        Called by Go() to capture a subexpression. Note that the
        capnum used here has already been mapped to a non-sparse
        index (by the code generator RegexWriter).
        
        This method is protected.
        """
        ...

    def Uncapture(self) -> None:
        """This method is protected."""
        ...


class RegexMatchTimeoutException(System.TimeoutException, System.Runtime.Serialization.ISerializable):
    """This is the exception that is thrown when a RegEx matching timeout occurs."""

    @property
    def Input(self) -> str:
        ...

    @property
    def Pattern(self) -> str:
        ...

    @property
    def MatchTimeout(self) -> datetime.timedelta:
        ...

    @overload
    def __init__(self, regexInput: str, regexPattern: str, matchTimeout: datetime.timedelta) -> None:
        """
        Constructs a new RegexMatchTimeoutException.
        
        :param regexInput: Matching timeout occurred during matching within the specified input.
        :param regexPattern: Matching timeout occurred during matching to the specified pattern.
        :param matchTimeout: Matching timeout occurred because matching took longer than the specified timeout.
        """
        ...

    @overload
    def __init__(self) -> None:
        """
        This constructor is provided in compliance with common .NET Framework design patterns;
        developers should prefer using the constructor
        public RegexMatchTimeoutException(string input, string pattern, TimeSpan matchTimeout).
        """
        ...

    @overload
    def __init__(self, message: str) -> None:
        """
        This constructor is provided in compliance with common .NET Framework design patterns;
        developers should prefer using the constructor
        public RegexMatchTimeoutException(string input, string pattern, TimeSpan matchTimeout).
        
        :param message: The error message that explains the reason for the exception.
        """
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception) -> None:
        """
        This constructor is provided in compliance with common .NET Framework design patterns;
        developers should prefer using the constructor
        public RegexMatchTimeoutException(string input, string pattern, TimeSpan matchTimeout).
        
        :param message: The error message that explains the reason for the exception.
        :param inner: The exception that is the cause of the current exception, or a null.
        """
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...

    def GetObjectData(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class GeneratedRegexAttribute(System.Attribute):
    """Instructs the System.Text.RegularExpressions source generator to generate an implementation of the specified regular expression."""

    @property
    def Pattern(self) -> str:
        """Gets the regular expression pattern to match."""
        ...

    @property
    def Options(self) -> int:
        """
        Gets a bitwise combination of the enumeration values that modify the regular expression.
        
        This property contains the int value of a member of the System.Text.RegularExpressions.RegexOptions enum.
        """
        ...

    @property
    def MatchTimeoutMilliseconds(self) -> int:
        """Gets a time-out interval (milliseconds), or Timeout.Infinite to indicate that the method should not time out."""
        ...

    @property
    def CultureName(self) -> str:
        """Gets the name of the culture to be used for case sensitive comparisons."""
        ...

    @overload
    def __init__(self, pattern: str) -> None:
        """
        Initializes a new instance of the GeneratedRegexAttribute with the specified pattern.
        
        :param pattern: The regular expression pattern to match.
        """
        ...

    @overload
    def __init__(self, pattern: str, options: System.Text.RegularExpressions.RegexOptions) -> None:
        """
        Initializes a new instance of the GeneratedRegexAttribute with the specified pattern and options.
        
        :param pattern: The regular expression pattern to match.
        :param options: A bitwise combination of the enumeration values that modify the regular expression.
        """
        ...

    @overload
    def __init__(self, pattern: str, options: System.Text.RegularExpressions.RegexOptions, cultureName: str) -> None:
        """
        Initializes a new instance of the GeneratedRegexAttribute with the specified pattern and options.
        
        :param pattern: The regular expression pattern to match.
        :param options: A bitwise combination of the enumeration values that modify the regular expression.
        :param cultureName: The name of a culture to be used for case sensitive comparisons.  is not case-sensitive.
        """
        ...

    @overload
    def __init__(self, pattern: str, options: System.Text.RegularExpressions.RegexOptions, matchTimeoutMilliseconds: int) -> None:
        """
        Initializes a new instance of the GeneratedRegexAttribute with the specified pattern, options, and timeout.
        
        :param pattern: The regular expression pattern to match.
        :param options: A bitwise combination of the enumeration values that modify the regular expression.
        :param matchTimeoutMilliseconds: A time-out interval (milliseconds), or Timeout.Infinite to indicate that the method should not time out.
        """
        ...

    @overload
    def __init__(self, pattern: str, options: System.Text.RegularExpressions.RegexOptions, matchTimeoutMilliseconds: int, cultureName: str) -> None:
        """
        Initializes a new instance of the GeneratedRegexAttribute with the specified pattern, options, and timeout.
        
        :param pattern: The regular expression pattern to match.
        :param options: A bitwise combination of the enumeration values that modify the regular expression.
        :param matchTimeoutMilliseconds: A time-out interval (milliseconds), or Timeout.Infinite to indicate that the method should not time out.
        :param cultureName: The name of a culture to be used for case sensitive comparisons.  is not case-sensitive.
        """
        ...


