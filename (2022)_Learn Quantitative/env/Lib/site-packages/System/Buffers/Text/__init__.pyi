from typing import overload
import datetime
import typing

import System
import System.Buffers
import System.Buffers.Text


class Base64(System.Object):
    """This class has no documentation."""

    @staticmethod
    def DecodeFromUtf8(utf8: System.ReadOnlySpan[int], bytes: System.Span[int], bytesConsumed: typing.Optional[int], bytesWritten: typing.Optional[int], isFinalBlock: bool = True) -> typing.Union[int, int, int]:
        """
        Decode the span of UTF-8 encoded text represented as base64 into binary data.
        If the input is not a multiple of 4, it will decode as much as it can, to the closest multiple of 4.
        
        :param utf8: The input span which contains UTF-8 encoded text in base64 that needs to be decoded.
        :param bytes: The output span which contains the result of the operation, i.e. the decoded binary data.
        :param bytesConsumed: The number of input bytes consumed during the operation. This can be used to slice the input for subsequent calls, if necessary.
        :param bytesWritten: The number of bytes written into the output span. This can be used to slice the output for subsequent calls, if necessary.
        :param isFinalBlock: true (default) when the input span contains the entire data to encode. Set to true when the source buffer contains the entirety of the data to encode. Set to false if this method is being called in a loop and if more input data may follow. At the end of the loop, call this (potentially with an empty source buffer) passing true.
        :returns: It returns the OperationStatus enum values: - Done - on successful processing of the entire input span - DestinationTooSmall - if there is not enough space in the output span to fit the decoded input - NeedMoreData - only if  is false and the input is not a multiple of 4, otherwise the partial input would be considered as InvalidData - InvalidData - if the input contains bytes outside of the expected base64 range, or if it contains invalid/more than two padding characters,   or if the input is incomplete (i.e. not a multiple of 4) and  is true. This method returns the int value of a member of the System.Buffers.OperationStatus enum.
        """
        ...

    @staticmethod
    def DecodeFromUtf8InPlace(buffer: System.Span[int], bytesWritten: typing.Optional[int]) -> typing.Union[int, int]:
        """
        Decode the span of UTF-8 encoded text in base 64 (in-place) into binary data.
        The decoded binary output is smaller than the text data contained in the input (the operation deflates the data).
        If the input is not a multiple of 4, it will not decode any.
        
        :param buffer: The input span which contains the base 64 text data that needs to be decoded.
        :param bytesWritten: The number of bytes written into the buffer.
        :returns: It returns the OperationStatus enum values: - Done - on successful processing of the entire input span - InvalidData - if the input contains bytes outside of the expected base 64 range, or if it contains invalid/more than two padding characters,   or if the input is incomplete (i.e. not a multiple of 4). It does not return DestinationTooSmall since that is not possible for base 64 decoding. It does not return NeedMoreData since this method tramples the data in the buffer and hence can only be called once with all the data in the buffer. This method returns the int value of a member of the System.Buffers.OperationStatus enum.
        """
        ...

    @staticmethod
    def EncodeToUtf8(bytes: System.ReadOnlySpan[int], utf8: System.Span[int], bytesConsumed: typing.Optional[int], bytesWritten: typing.Optional[int], isFinalBlock: bool = True) -> typing.Union[int, int, int]:
        """
        Encode the span of binary data into UTF-8 encoded text represented as base64.
        
        :param bytes: The input span which contains binary data that needs to be encoded.
        :param utf8: The output span which contains the result of the operation, i.e. the UTF-8 encoded text in base64.
        :param bytesConsumed: The number of input bytes consumed during the operation. This can be used to slice the input for subsequent calls, if necessary.
        :param bytesWritten: The number of bytes written into the output span. This can be used to slice the output for subsequent calls, if necessary.
        :param isFinalBlock: true (default) when the input span contains the entire data to encode. Set to true when the source buffer contains the entirety of the data to encode. Set to false if this method is being called in a loop and if more input data may follow. At the end of the loop, call this (potentially with an empty source buffer) passing true.
        :returns: It returns the OperationStatus enum values: - Done - on successful processing of the entire input span - DestinationTooSmall - if there is not enough space in the output span to fit the encoded input - NeedMoreData - only if  is false, otherwise the output is padded if the input is not a multiple of 3 It does not return InvalidData since that is not possible for base64 encoding. This method returns the int value of a member of the System.Buffers.OperationStatus enum.
        """
        ...

    @staticmethod
    def EncodeToUtf8InPlace(buffer: System.Span[int], dataLength: int, bytesWritten: typing.Optional[int]) -> typing.Union[int, int]:
        """
        Encode the span of binary data (in-place) into UTF-8 encoded text represented as base 64.
        The encoded text output is larger than the binary data contained in the input (the operation inflates the data).
        
        :param buffer: The input span which contains binary data that needs to be encoded. It needs to be large enough to fit the result of the operation.
        :param dataLength: The amount of binary data contained within the buffer that needs to be encoded (and needs to be smaller than the buffer length).
        :param bytesWritten: The number of bytes written into the buffer.
        :returns: It returns the OperationStatus enum values: - Done - on successful processing of the entire buffer - DestinationTooSmall - if there is not enough space in the buffer beyond dataLength to fit the result of encoding the input It does not return NeedMoreData since this method tramples the data in the buffer and hence can only be called once with all the data in the buffer. It does not return InvalidData since that is not possible for base 64 encoding. This method returns the int value of a member of the System.Buffers.OperationStatus enum.
        """
        ...

    @staticmethod
    def GetMaxDecodedFromUtf8Length(length: int) -> int:
        """Returns the maximum length (in bytes) of the result if you were to deocde base 64 encoded text within a byte span of size "length"."""
        ...

    @staticmethod
    def GetMaxEncodedToUtf8Length(length: int) -> int:
        """Returns the maximum length (in bytes) of the result if you were to encode binary data within a byte span of size "length"."""
        ...


class Utf8Formatter(System.Object):
    """Methods to format common data types as Utf8 strings."""

    @staticmethod
    @overload
    def TryFormat(value: int, destination: System.Span[int], bytesWritten: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Union[bool, int]:
        """
        Formats a Byte as a UTF8 string.
        
        :param value: Value to format
        :param destination: Buffer to write the UTF8-formatted value to
        :param bytesWritten: Receives the length of the formatted text in bytes
        :param format: The standard format to use
        :returns: true for success. "bytesWritten" contains the length of the formatted text in bytes. false if buffer was too short. Iteratively increase the size of the buffer and retry until it succeeds.
        """
        ...

    @staticmethod
    @overload
    def TryFormat(value: int, destination: System.Span[int], bytesWritten: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Union[bool, int]:
        """
        Formats an SByte as a UTF8 string.
        
        :param value: Value to format
        :param destination: Buffer to write the UTF8-formatted value to
        :param bytesWritten: Receives the length of the formatted text in bytes
        :param format: The standard format to use
        :returns: true for success. "bytesWritten" contains the length of the formatted text in bytes. false if buffer was too short. Iteratively increase the size of the buffer and retry until it succeeds.
        """
        ...

    @staticmethod
    @overload
    def TryFormat(value: int, destination: System.Span[int], bytesWritten: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Union[bool, int]:
        """
        Formats a Unt16 as a UTF8 string.
        
        :param value: Value to format
        :param destination: Buffer to write the UTF8-formatted value to
        :param bytesWritten: Receives the length of the formatted text in bytes
        :param format: The standard format to use
        :returns: true for success. "bytesWritten" contains the length of the formatted text in bytes. false if buffer was too short. Iteratively increase the size of the buffer and retry until it succeeds.
        """
        ...

    @staticmethod
    @overload
    def TryFormat(value: int, destination: System.Span[int], bytesWritten: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Union[bool, int]:
        """
        Formats an Int16 as a UTF8 string.
        
        :param value: Value to format
        :param destination: Buffer to write the UTF8-formatted value to
        :param bytesWritten: Receives the length of the formatted text in bytes
        :param format: The standard format to use
        :returns: true for success. "bytesWritten" contains the length of the formatted text in bytes. false if buffer was too short. Iteratively increase the size of the buffer and retry until it succeeds.
        """
        ...

    @staticmethod
    @overload
    def TryFormat(value: int, destination: System.Span[int], bytesWritten: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Union[bool, int]:
        """
        Formats a UInt32 as a UTF8 string.
        
        :param value: Value to format
        :param destination: Buffer to write the UTF8-formatted value to
        :param bytesWritten: Receives the length of the formatted text in bytes
        :param format: The standard format to use
        :returns: true for success. "bytesWritten" contains the length of the formatted text in bytes. false if buffer was too short. Iteratively increase the size of the buffer and retry until it succeeds.
        """
        ...

    @staticmethod
    @overload
    def TryFormat(value: int, destination: System.Span[int], bytesWritten: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Union[bool, int]:
        """
        Formats an Int32 as a UTF8 string.
        
        :param value: Value to format
        :param destination: Buffer to write the UTF8-formatted value to
        :param bytesWritten: Receives the length of the formatted text in bytes
        :param format: The standard format to use
        :returns: true for success. "bytesWritten" contains the length of the formatted text in bytes. false if buffer was too short. Iteratively increase the size of the buffer and retry until it succeeds.
        """
        ...

    @staticmethod
    @overload
    def TryFormat(value: int, destination: System.Span[int], bytesWritten: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Union[bool, int]:
        """
        Formats a UInt64 as a UTF8 string.
        
        :param value: Value to format
        :param destination: Buffer to write the UTF8-formatted value to
        :param bytesWritten: Receives the length of the formatted text in bytes
        :param format: The standard format to use
        :returns: true for success. "bytesWritten" contains the length of the formatted text in bytes. false if buffer was too short. Iteratively increase the size of the buffer and retry until it succeeds.
        """
        ...

    @staticmethod
    @overload
    def TryFormat(value: int, destination: System.Span[int], bytesWritten: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Union[bool, int]:
        """
        Formats an Int64 as a UTF8 string.
        
        :param value: Value to format
        :param destination: Buffer to write the UTF8-formatted value to
        :param bytesWritten: Receives the length of the formatted text in bytes
        :param format: The standard format to use
        :returns: true for success. "bytesWritten" contains the length of the formatted text in bytes. false if buffer was too short. Iteratively increase the size of the buffer and retry until it succeeds.
        """
        ...

    @staticmethod
    @overload
    def TryFormat(value: System.Guid, destination: System.Span[int], bytesWritten: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Union[bool, int]:
        ...

    @staticmethod
    @overload
    def TryFormat(value: float, destination: System.Span[int], bytesWritten: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Union[bool, int]:
        """
        Formats a Decimal as a UTF8 string.
        
        :param value: Value to format
        :param destination: Buffer to write the UTF8-formatted value to
        :param bytesWritten: Receives the length of the formatted text in bytes
        :param format: The standard format to use
        :returns: true for success. "bytesWritten" contains the length of the formatted text in bytes. false if buffer was too short. Iteratively increase the size of the buffer and retry until it succeeds.
        """
        ...

    @staticmethod
    @overload
    def TryFormat(value: datetime.timedelta, destination: System.Span[int], bytesWritten: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Union[bool, int]:
        """
        Formats a TimeSpan as a UTF8 string.
        
        :param value: Value to format
        :param destination: Buffer to write the UTF8-formatted value to
        :param bytesWritten: Receives the length of the formatted text in bytes
        :param format: The standard format to use
        :returns: true for success. "bytesWritten" contains the length of the formatted text in bytes. false if buffer was too short. Iteratively increase the size of the buffer and retry until it succeeds.
        """
        ...

    @staticmethod
    @overload
    def TryFormat(value: System.DateTimeOffset, destination: System.Span[int], bytesWritten: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Union[bool, int]:
        """
        Formats a DateTimeOffset as a UTF8 string.
        
        :param value: Value to format
        :param destination: Buffer to write the UTF8-formatted value to
        :param bytesWritten: Receives the length of the formatted text in bytes
        :param format: The standard format to use
        :returns: true for success. "bytesWritten" contains the length of the formatted text in bytes. false if buffer was too short. Iteratively increase the size of the buffer and retry until it succeeds.
        """
        ...

    @staticmethod
    @overload
    def TryFormat(value: typing.Union[datetime.datetime, datetime.date], destination: System.Span[int], bytesWritten: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Union[bool, int]:
        """
        Formats a DateTime as a UTF8 string.
        
        :param value: Value to format
        :param destination: Buffer to write the UTF8-formatted value to
        :param bytesWritten: Receives the length of the formatted text in bytes
        :param format: The standard format to use
        :returns: true for success. "bytesWritten" contains the length of the formatted text in bytes. false if buffer was too short. Iteratively increase the size of the buffer and retry until it succeeds.
        """
        ...

    @staticmethod
    @overload
    def TryFormat(value: bool, destination: System.Span[int], bytesWritten: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Union[bool, int]:
        """
        Formats a Boolean as a UTF8 string.
        
        :param value: Value to format
        :param destination: Buffer to write the UTF8-formatted value to
        :param bytesWritten: Receives the length of the formatted text in bytes
        :param format: The standard format to use
        :returns: true for success. "bytesWritten" contains the length of the formatted text in bytes. false if buffer was too short. Iteratively increase the size of the buffer and retry until it succeeds.
        """
        ...

    @staticmethod
    @overload
    def TryFormat(value: float, destination: System.Span[int], bytesWritten: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Union[bool, int]:
        """
        Formats a Double as a UTF8 string.
        
        :param value: Value to format
        :param destination: Buffer to write the UTF8-formatted value to
        :param bytesWritten: Receives the length of the formatted text in bytes
        :param format: The standard format to use
        :returns: true for success. "bytesWritten" contains the length of the formatted text in bytes. false if buffer was too short. Iteratively increase the size of the buffer and retry until it succeeds.
        """
        ...

    @staticmethod
    @overload
    def TryFormat(value: float, destination: System.Span[int], bytesWritten: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Union[bool, int]:
        """
        Formats a Single as a UTF8 string.
        
        :param value: Value to format
        :param destination: Buffer to write the UTF8-formatted value to
        :param bytesWritten: Receives the length of the formatted text in bytes
        :param format: The standard format to use
        :returns: true for success. "bytesWritten" contains the length of the formatted text in bytes. false if buffer was too short. Iteratively increase the size of the buffer and retry until it succeeds.
        """
        ...


class Utf8Parser(System.Object):
    """Methods to parse common data types to Utf8 strings."""

    @staticmethod
    @overload
    def TryParse(source: System.ReadOnlySpan[int], value: typing.Optional[System.Guid], bytesConsumed: typing.Optional[int], standardFormat: str = ...) -> typing.Union[bool, System.Guid, int]:
        """
        Parses a Guid at the start of a Utf8 string.
        
        :param source: The Utf8 string to parse
        :param value: Receives the parsed value
        :param bytesConsumed: On a successful parse, receives the length in bytes of the substring that was parsed
        :param standardFormat: Expected format of the Utf8 string
        :returns: true for success. "bytesConsumed" contains the length in bytes of the substring that was parsed. false if the string was not syntactically valid or an overflow or underflow occurred. "bytesConsumed" is set to 0.
        """
        ...

    @staticmethod
    @overload
    def TryParse(source: System.ReadOnlySpan[int], value: typing.Optional[datetime.timedelta], bytesConsumed: typing.Optional[int], standardFormat: str = ...) -> typing.Union[bool, datetime.timedelta, int]:
        """
        Parses a TimeSpan at the start of a Utf8 string.
        
        :param source: The Utf8 string to parse
        :param value: Receives the parsed value
        :param bytesConsumed: On a successful parse, receives the length in bytes of the substring that was parsed
        :param standardFormat: Expected format of the Utf8 string
        :returns: true for success. "bytesConsumed" contains the length in bytes of the substring that was parsed. false if the string was not syntactically valid or an overflow or underflow occurred. "bytesConsumed" is set to 0.
        """
        ...

    @staticmethod
    @overload
    def TryParse(source: System.ReadOnlySpan[int], value: typing.Optional[int], bytesConsumed: typing.Optional[int], standardFormat: str = ...) -> typing.Union[bool, int, int]:
        """
        Parses a SByte at the start of a Utf8 string.
        
        :param source: The Utf8 string to parse
        :param value: Receives the parsed value
        :param bytesConsumed: On a successful parse, receives the length in bytes of the substring that was parsed
        :param standardFormat: Expected format of the Utf8 string
        :returns: true for success. "bytesConsumed" contains the length in bytes of the substring that was parsed. false if the string was not syntactically valid or an overflow or underflow occurred. "bytesConsumed" is set to 0.
        """
        ...

    @staticmethod
    @overload
    def TryParse(source: System.ReadOnlySpan[int], value: typing.Optional[int], bytesConsumed: typing.Optional[int], standardFormat: str = ...) -> typing.Union[bool, int, int]:
        """
        Parses an Int16 at the start of a Utf8 string.
        
        :param source: The Utf8 string to parse
        :param value: Receives the parsed value
        :param bytesConsumed: On a successful parse, receives the length in bytes of the substring that was parsed
        :param standardFormat: Expected format of the Utf8 string
        :returns: true for success. "bytesConsumed" contains the length in bytes of the substring that was parsed. false if the string was not syntactically valid or an overflow or underflow occurred. "bytesConsumed" is set to 0.
        """
        ...

    @staticmethod
    @overload
    def TryParse(source: System.ReadOnlySpan[int], value: typing.Optional[int], bytesConsumed: typing.Optional[int], standardFormat: str = ...) -> typing.Union[bool, int, int]:
        """
        Parses an Int32 at the start of a Utf8 string.
        
        :param source: The Utf8 string to parse
        :param value: Receives the parsed value
        :param bytesConsumed: On a successful parse, receives the length in bytes of the substring that was parsed
        :param standardFormat: Expected format of the Utf8 string
        :returns: true for success. "bytesConsumed" contains the length in bytes of the substring that was parsed. false if the string was not syntactically valid or an overflow or underflow occurred. "bytesConsumed" is set to 0.
        """
        ...

    @staticmethod
    @overload
    def TryParse(source: System.ReadOnlySpan[int], value: typing.Optional[int], bytesConsumed: typing.Optional[int], standardFormat: str = ...) -> typing.Union[bool, int, int]:
        """
        Parses an Int64 at the start of a Utf8 string.
        
        :param source: The Utf8 string to parse
        :param value: Receives the parsed value
        :param bytesConsumed: On a successful parse, receives the length in bytes of the substring that was parsed
        :param standardFormat: Expected format of the Utf8 string
        :returns: true for success. "bytesConsumed" contains the length in bytes of the substring that was parsed. false if the string was not syntactically valid or an overflow or underflow occurred. "bytesConsumed" is set to 0.
        """
        ...

    @staticmethod
    @overload
    def TryParse(source: System.ReadOnlySpan[int], value: typing.Optional[bool], bytesConsumed: typing.Optional[int], standardFormat: str = ...) -> typing.Union[bool, bool, int]:
        """
        Parses a Boolean at the start of a Utf8 string.
        
        :param source: The Utf8 string to parse
        :param value: Receives the parsed value
        :param bytesConsumed: On a successful parse, receives the length in bytes of the substring that was parsed
        :param standardFormat: Expected format of the Utf8 string
        :returns: true for success. "bytesConsumed" contains the length in bytes of the substring that was parsed. false if the string was not syntactically valid or an overflow or underflow occurred. "bytesConsumed" is set to 0.
        """
        ...

    @staticmethod
    @overload
    def TryParse(source: System.ReadOnlySpan[int], value: typing.Optional[float], bytesConsumed: typing.Optional[int], standardFormat: str = ...) -> typing.Union[bool, float, int]:
        """
        Parses a Decimal at the start of a Utf8 string.
        
        :param source: The Utf8 string to parse
        :param value: Receives the parsed value
        :param bytesConsumed: On a successful parse, receives the length in bytes of the substring that was parsed
        :param standardFormat: Expected format of the Utf8 string
        :returns: true for success. "bytesConsumed" contains the length in bytes of the substring that was parsed. false if the string was not syntactically valid or an overflow or underflow occurred. "bytesConsumed" is set to 0.
        """
        ...

    @staticmethod
    @overload
    def TryParse(source: System.ReadOnlySpan[int], value: typing.Optional[typing.Union[datetime.datetime, datetime.date]], bytesConsumed: typing.Optional[int], standardFormat: str = ...) -> typing.Union[bool, typing.Union[datetime.datetime, datetime.date], int]:
        """
        Parses a DateTime at the start of a Utf8 string.
        
        :param source: The Utf8 string to parse
        :param value: Receives the parsed value
        :param bytesConsumed: On a successful parse, receives the length in bytes of the substring that was parsed
        :param standardFormat: Expected format of the Utf8 string
        :returns: true for success. "bytesConsumed" contains the length in bytes of the substring that was parsed. false if the string was not syntactically valid or an overflow or underflow occurred. "bytesConsumed" is set to 0.
        """
        ...

    @staticmethod
    @overload
    def TryParse(source: System.ReadOnlySpan[int], value: typing.Optional[System.DateTimeOffset], bytesConsumed: typing.Optional[int], standardFormat: str = ...) -> typing.Union[bool, System.DateTimeOffset, int]:
        """
        Parses a DateTimeOffset at the start of a Utf8 string.
        
        :param source: The Utf8 string to parse
        :param value: Receives the parsed value
        :param bytesConsumed: On a successful parse, receives the length in bytes of the substring that was parsed
        :param standardFormat: Expected format of the Utf8 string
        :returns: true for success. "bytesConsumed" contains the length in bytes of the substring that was parsed. false if the string was not syntactically valid or an overflow or underflow occurred. "bytesConsumed" is set to 0.
        """
        ...

    @staticmethod
    @overload
    def TryParse(source: System.ReadOnlySpan[int], value: typing.Optional[float], bytesConsumed: typing.Optional[int], standardFormat: str = ...) -> typing.Union[bool, float, int]:
        """
        Parses a Single at the start of a Utf8 string.
        
        :param source: The Utf8 string to parse
        :param value: Receives the parsed value
        :param bytesConsumed: On a successful parse, receives the length in bytes of the substring that was parsed
        :param standardFormat: Expected format of the Utf8 string
        :returns: true for success. "bytesConsumed" contains the length in bytes of the substring that was parsed. false if the string was not syntactically valid or an overflow or underflow occurred. "bytesConsumed" is set to 0.
        """
        ...

    @staticmethod
    @overload
    def TryParse(source: System.ReadOnlySpan[int], value: typing.Optional[float], bytesConsumed: typing.Optional[int], standardFormat: str = ...) -> typing.Union[bool, float, int]:
        """
        Parses a Double at the start of a Utf8 string.
        
        :param source: The Utf8 string to parse
        :param value: Receives the parsed value
        :param bytesConsumed: On a successful parse, receives the length in bytes of the substring that was parsed
        :param standardFormat: Expected format of the Utf8 string
        :returns: true for success. "bytesConsumed" contains the length in bytes of the substring that was parsed. false if the string was not syntactically valid or an overflow or underflow occurred. "bytesConsumed" is set to 0.
        """
        ...

    @staticmethod
    @overload
    def TryParse(source: System.ReadOnlySpan[int], value: typing.Optional[int], bytesConsumed: typing.Optional[int], standardFormat: str = ...) -> typing.Union[bool, int, int]:
        """
        Parses a Byte at the start of a Utf8 string.
        
        :param source: The Utf8 string to parse
        :param value: Receives the parsed value
        :param bytesConsumed: On a successful parse, receives the length in bytes of the substring that was parsed
        :param standardFormat: Expected format of the Utf8 string
        :returns: true for success. "bytesConsumed" contains the length in bytes of the substring that was parsed. false if the string was not syntactically valid or an overflow or underflow occurred. "bytesConsumed" is set to 0.
        """
        ...

    @staticmethod
    @overload
    def TryParse(source: System.ReadOnlySpan[int], value: typing.Optional[int], bytesConsumed: typing.Optional[int], standardFormat: str = ...) -> typing.Union[bool, int, int]:
        """
        Parses a UInt16 at the start of a Utf8 string.
        
        :param source: The Utf8 string to parse
        :param value: Receives the parsed value
        :param bytesConsumed: On a successful parse, receives the length in bytes of the substring that was parsed
        :param standardFormat: Expected format of the Utf8 string
        :returns: true for success. "bytesConsumed" contains the length in bytes of the substring that was parsed. false if the string was not syntactically valid or an overflow or underflow occurred. "bytesConsumed" is set to 0.
        """
        ...

    @staticmethod
    @overload
    def TryParse(source: System.ReadOnlySpan[int], value: typing.Optional[int], bytesConsumed: typing.Optional[int], standardFormat: str = ...) -> typing.Union[bool, int, int]:
        """
        Parses a UInt32 at the start of a Utf8 string.
        
        :param source: The Utf8 string to parse
        :param value: Receives the parsed value
        :param bytesConsumed: On a successful parse, receives the length in bytes of the substring that was parsed
        :param standardFormat: Expected format of the Utf8 string
        :returns: true for success. "bytesConsumed" contains the length in bytes of the substring that was parsed. false if the string was not syntactically valid or an overflow or underflow occurred. "bytesConsumed" is set to 0.
        """
        ...

    @staticmethod
    @overload
    def TryParse(source: System.ReadOnlySpan[int], value: typing.Optional[int], bytesConsumed: typing.Optional[int], standardFormat: str = ...) -> typing.Union[bool, int, int]:
        """
        Parses a UInt64 at the start of a Utf8 string.
        
        :param source: The Utf8 string to parse
        :param value: Receives the parsed value
        :param bytesConsumed: On a successful parse, receives the length in bytes of the substring that was parsed
        :param standardFormat: Expected format of the Utf8 string
        :returns: true for success. "bytesConsumed" contains the length in bytes of the substring that was parsed. false if the string was not syntactically valid or an overflow or underflow occurred. "bytesConsumed" is set to 0.
        """
        ...


