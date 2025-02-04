from typing import overload
import abc
import datetime
import typing

import System
import System.Collections.Generic
import System.ComponentModel
import System.ComponentModel.DataAnnotations
import System.Runtime.Serialization

IServiceProvider = typing.Any


class FilterUIHintAttribute(System.Attribute):
    """
    An attribute used to specify the filtering behavior for a column.
    
    FilterUIHintAttribute has been deprecated and is not supported.
    """

    @property
    def FilterUIHint(self) -> str:
        """
        Gets the name of the control that is most appropriate for this associated
        property or field
        """
        ...

    @property
    def PresentationLayer(self) -> str:
        """
        Gets the name of the presentation layer that supports the control type
        in FilterUIHint
        """
        ...

    @property
    def ControlParameters(self) -> System.Collections.Generic.IDictionary[str, System.Object]:
        """Gets the name-value pairs used as parameters to the control's constructor"""
        ...

    @overload
    def __init__(self, filterUIHint: str) -> None:
        """
        Constructor that accepts the name of the control, without specifying
        which presentation layer to use
        
        :param filterUIHint: The name of the UI control.
        """
        ...

    @overload
    def __init__(self, filterUIHint: str, presentationLayer: str) -> None:
        """
        Constructor that accepts both the name of the control as well as the
        presentation layer
        
        :param filterUIHint: The name of the control to use
        :param presentationLayer: The name of the presentation layer that supports this control
        """
        ...

    @overload
    def __init__(self, filterUIHint: str, presentationLayer: str, *controlParameters: typing.Any) -> None:
        """
        Full constructor that accepts the name of the control, presentation layer,
        and optional parameters to use when constructing the control
        
        :param filterUIHint: The name of the control
        :param presentationLayer: The presentation layer
        :param controlParameters: The list of parameters for the control
        """
        ...

    def Equals(self, obj: typing.Any) -> bool:
        """
        Determines whether this instance of FilterUIHintAttribute and a specified object,
        which must also be a FilterUIHintAttribute object, have the same value.
        
        :param obj: An System.Object.
        :returns: true if obj is a FilterUIHintAttribute and its value is the same as this instance; otherwise, false.
        """
        ...

    def GetHashCode(self) -> int:
        """
        Returns the hash code for this FilterUIHintAttribute.
        
        :returns: A 32-bit signed integer hash code.
        """
        ...


class AssociationAttribute(System.Attribute):
    """
    Used to mark an Entity member as an association
    
    AssociationAttribute has been deprecated and is not supported.
    """

    @property
    def Name(self) -> str:
        """
        Gets the name of the association. For bi-directional associations, the name must
        be the same on both sides of the association
        """
        ...

    @property
    def ThisKey(self) -> str:
        """
        Gets a comma separated list of the property names of the key values
        on this side of the association
        """
        ...

    @property
    def OtherKey(self) -> str:
        """
        Gets a comma separated list of the property names of the key values
        on the other side of the association
        """
        ...

    @property
    def IsForeignKey(self) -> bool:
        """
        Gets or sets a value indicating whether this association member represents
        the foreign key side of an association
        """
        ...

    @IsForeignKey.setter
    def IsForeignKey(self, value: bool):
        """
        Gets or sets a value indicating whether this association member represents
        the foreign key side of an association
        """
        ...

    @property
    def ThisKeyMembers(self) -> System.Collections.Generic.IEnumerable[str]:
        """Gets the collection of individual key members specified in the ThisKey string."""
        ...

    @property
    def OtherKeyMembers(self) -> System.Collections.Generic.IEnumerable[str]:
        """Gets the collection of individual key members specified in the OtherKey string."""
        ...

    def __init__(self, name: str, thisKey: str, otherKey: str) -> None:
        """
        Full form of constructor
        
        :param name: The name of the association. For bi-directional associations, the name must be the same on both sides of the association
        :param thisKey: Comma separated list of the property names of the key values on this side of the association
        :param otherKey: Comma separated list of the property names of the key values on the other side of the association
        """
        ...


class ValidationResult(System.Object):
    """
    Container class for the results of a validation request.
        
            Use the static  to represent successful validation.
    """

    Success: System.ComponentModel.DataAnnotations.ValidationResult

    @property
    def MemberNames(self) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @property
    def ErrorMessage(self) -> str:
        """Gets the error message for this result.  It may be null."""
        ...

    @ErrorMessage.setter
    def ErrorMessage(self, value: str):
        """Gets the error message for this result.  It may be null."""
        ...

    @overload
    def __init__(self, errorMessage: str) -> None:
        ...

    @overload
    def __init__(self, errorMessage: str, memberNames: System.Collections.Generic.IEnumerable[str]) -> None:
        """
        Constructor that accepts an error message as well as a list of member names involved in the validation.
            This error message would override any error message provided on the ValidationAttribute.
        
        :param errorMessage: The user-visible error message.  If null, ValidationAttribute.GetValidationResult     will use ValidationAttribute.FormatErrorMessage for its error message.
        :param memberNames: The list of member names affected by this result.     This list of member names is meant to be used by presentation layers to indicate which fields are in error.
        """
        ...

    @overload
    def __init__(self, validationResult: System.ComponentModel.DataAnnotations.ValidationResult) -> None:
        """
        Constructor that creates a copy of an existing ValidationResult.
        
        This method is protected.
        
        :param validationResult: The validation result.
        """
        ...

    def ToString(self) -> str:
        ...


class ValidationContext(IServiceProvider):
    """Describes the context in which a validation is being performed."""

    InstanceTypeNotStaticallyDiscovered: str = "The Type of instance cannot be statically discovered."

    @property
    def ObjectInstance(self) -> System.Object:
        ...

    @property
    def ObjectType(self) -> typing.Type:
        """Gets the type of the object being validated.  It will not be null."""
        ...

    @property
    def DisplayName(self) -> str:
        """Gets or sets the user-visible name of the type or property being validated."""
        ...

    @DisplayName.setter
    def DisplayName(self, value: str):
        """Gets or sets the user-visible name of the type or property being validated."""
        ...

    @property
    def MemberName(self) -> str:
        """Gets or sets the name of the type or property being validated."""
        ...

    @MemberName.setter
    def MemberName(self, value: str):
        """Gets or sets the name of the type or property being validated."""
        ...

    @property
    def Items(self) -> System.Collections.Generic.IDictionary[System.Object, System.Object]:
        """Gets the dictionary of key/value pairs associated with this context."""
        ...

    @overload
    def __init__(self, instance: typing.Any) -> None:
        ...

    @overload
    def __init__(self, instance: typing.Any, items: System.Collections.Generic.IDictionary[System.Object, System.Object]) -> None:
        """
        Construct a ValidationContext for a given object instance and an optional
            property bag of .
        
        :param instance: The object instance being validated.  It cannot be null.
        :param items: Optional set of key/value pairs to make available to consumers via Items.     If null, an empty dictionary will be created.  If not null, the set of key/value pairs will be copied into a     new dictionary, preventing consumers from modifying the original dictionary.
        """
        ...

    @overload
    def __init__(self, instance: typing.Any, serviceProvider: typing.Optional[IServiceProvider], items: System.Collections.Generic.IDictionary[System.Object, System.Object]) -> None:
        """
        Construct a ValidationContext for a given object instance, an optional
            , and an optional
            property bag of .
        
        :param instance: The object instance being validated.  It cannot be null.
        :param serviceProvider: Optional IServiceProvider to use when GetService is called.     If it is null, GetService will always return null.
        :param items: Optional set of key/value pairs to make available to consumers via Items.     If null, an empty dictionary will be created.  If not null, the set of key/value pairs will be copied into a     new dictionary, preventing consumers from modifying the original dictionary.
        """
        ...

    def GetService(self, serviceType: typing.Type) -> System.Object:
        ...

    def InitializeServiceProvider(self, serviceProvider: typing.Callable[[typing.Type], System.Object]) -> None:
        """
        Initializes the ValidationContext with a service provider that can return
            service instances by Type when GetService is called.
        
        :param serviceProvider: A Func{T, TResult} that can return service instances given the     desired Type when GetService is called.     If it is null, GetService will always return null.
        """
        ...


class ValidationAttribute(System.Attribute, metaclass=abc.ABCMeta):
    """
    Base class for all validation attributes.
        Override  to implement validation logic.
    """

    @property
    def DefaultErrorMessage(self) -> str:
        ...

    @DefaultErrorMessage.setter
    def DefaultErrorMessage(self, value: str):
        ...

    @property
    def ErrorMessageString(self) -> str:
        """This property is protected."""
        ...

    @property
    def CustomErrorMessageSet(self) -> bool:
        """
        A flag indicating whether a developer has customized the attribute's error message by setting any one of
            ErrorMessage, ErrorMessageResourceName, ErrorMessageResourceType or DefaultErrorMessage.
        """
        ...

    @CustomErrorMessageSet.setter
    def CustomErrorMessageSet(self, value: bool):
        """
        A flag indicating whether a developer has customized the attribute's error message by setting any one of
            ErrorMessage, ErrorMessageResourceName, ErrorMessageResourceType or DefaultErrorMessage.
        """
        ...

    @property
    def RequiresValidationContext(self) -> bool:
        """
        A flag indicating that the attribute requires a non-null
            ValidationContext to perform validation.
            Base class returns false. Override in child classes as appropriate.
        """
        ...

    @property
    def ErrorMessage(self) -> str:
        ...

    @ErrorMessage.setter
    def ErrorMessage(self, value: str):
        ...

    @property
    def ErrorMessageResourceName(self) -> str:
        """Gets or sets the resource name (property name) to use as the key for lookups on the resource type."""
        ...

    @ErrorMessageResourceName.setter
    def ErrorMessageResourceName(self, value: str):
        """Gets or sets the resource name (property name) to use as the key for lookups on the resource type."""
        ...

    @property
    def ErrorMessageResourceType(self) -> typing.Type:
        """Gets or sets the resource type to use for error message lookups."""
        ...

    @ErrorMessageResourceType.setter
    def ErrorMessageResourceType(self, value: typing.Type):
        """Gets or sets the resource type to use for error message lookups."""
        ...

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, errorMessage: str) -> None:
        """
        Constructor that accepts a fixed validation error message.
        
        This method is protected.
        
        :param errorMessage: A non-localized error message to use in ErrorMessageString.
        """
        ...

    @overload
    def __init__(self, errorMessageAccessor: typing.Callable[[], str]) -> None:
        """
        Allows for providing a resource accessor function that will be used by the ErrorMessageString
            property to retrieve the error message.  An example would be to have something like
            CustomAttribute() : base( () => MyResources.MyErrorMessage ) {}.
        
        This method is protected.
        
        :param errorMessageAccessor: The Func{T} that will return an error message.
        """
        ...

    def FormatErrorMessage(self, name: str) -> str:
        ...

    def GetValidationResult(self, value: typing.Any, validationContext: System.ComponentModel.DataAnnotations.ValidationContext) -> System.ComponentModel.DataAnnotations.ValidationResult:
        """
        Tests whether the given  is valid with respect to the current
            validation attribute without throwing a ValidationException
        
        :param value: The value to validate
        :param validationContext: A ValidationContext instance that provides     context about the validation operation, such as the object and member being validated.
        :returns: When validation is valid, ValidationResult.Success.              When validation is invalid, an instance of .
        """
        ...

    @overload
    def IsValid(self, value: typing.Any) -> bool:
        """
        Gets the value indicating whether or not the specified  is valid
            with respect to the current validation attribute.
            
                Derived classes should not override this method as it is only available for backwards compatibility.
                Instead, implement .
        
        :param value: The value to validate
        :returns: true if the  is acceptable, false if it is not acceptable.
        """
        ...

    @overload
    def IsValid(self, value: typing.Any, validationContext: System.ComponentModel.DataAnnotations.ValidationContext) -> System.ComponentModel.DataAnnotations.ValidationResult:
        """
        Protected virtual method to override and implement validation logic.
            
                Derived classes should override this method instead of , which is deprecated.
        
        This method is protected.
        
        :param value: The value to validate.
        :param validationContext: A ValidationContext instance that provides     context about the validation operation, such as the object and member being validated.
        :returns: When validation is valid, ValidationResult.Success.              When validation is invalid, an instance of .
        """
        ...

    @overload
    def Validate(self, value: typing.Any, name: str) -> None:
        """
        Validates the specified  and throws ValidationException if it is not.
            
                The overloaded  is the recommended entry point as it
                can provide additional context to the  being validated.
        
        :param value: The value to validate
        :param name: The string to be included in the validation error message if  is not valid
        """
        ...

    @overload
    def Validate(self, value: typing.Any, validationContext: System.ComponentModel.DataAnnotations.ValidationContext) -> None:
        """
        Validates the specified  and throws ValidationException if it is not.
        
        :param value: The value to validate
        :param validationContext: Additional context that may be used for validation.  It cannot be null.
        """
        ...


class StringLengthAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """Validation attribute to assert a string property, field or parameter does not exceed a maximum length"""

    @property
    def MaximumLength(self) -> int:
        """Gets the maximum acceptable length of the string"""
        ...

    @property
    def MinimumLength(self) -> int:
        """Gets or sets the minimum acceptable length of the string"""
        ...

    @MinimumLength.setter
    def MinimumLength(self, value: int):
        """Gets or sets the minimum acceptable length of the string"""
        ...

    def __init__(self, maximumLength: int) -> None:
        """
        Constructor that accepts the maximum length of the string.
        
        :param maximumLength: The maximum length, inclusive.  It may not be negative.
        """
        ...

    def FormatErrorMessage(self, name: str) -> str:
        """
        Override of ValidationAttribute.FormatErrorMessage
        
        :param name: The name to include in the formatted string
        :returns: A localized string to describe the maximum acceptable length.
        """
        ...

    def IsValid(self, value: typing.Any) -> bool:
        """
        Override of ValidationAttribute.IsValid(object)
        
        :param value: The value to test.
        :returns: true if the value is null or less than or equal to the set maximum length.
        """
        ...


class ScaffoldColumnAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def Scaffold(self) -> bool:
        ...

    def __init__(self, scaffold: bool) -> None:
        ...


class DisplayFormatAttribute(System.Attribute):
    """
    Allows overriding various display-related options for a given field. The options have the same meaning as in
        BoundField.
    """

    @property
    def DataFormatString(self) -> str:
        """Gets or sets the format string"""
        ...

    @DataFormatString.setter
    def DataFormatString(self, value: str):
        """Gets or sets the format string"""
        ...

    @property
    def NullDisplayText(self) -> str:
        """
        Gets or sets the string to display when the value is null, which may be a resource key string.
            
                Consumers should use the  method to retrieve the UI display string.
        """
        ...

    @NullDisplayText.setter
    def NullDisplayText(self, value: str):
        """
        Gets or sets the string to display when the value is null, which may be a resource key string.
            
                Consumers should use the  method to retrieve the UI display string.
        """
        ...

    @property
    def ConvertEmptyStringToNull(self) -> bool:
        """Gets or sets a value indicating whether empty strings should be set to null"""
        ...

    @ConvertEmptyStringToNull.setter
    def ConvertEmptyStringToNull(self, value: bool):
        """Gets or sets a value indicating whether empty strings should be set to null"""
        ...

    @property
    def ApplyFormatInEditMode(self) -> bool:
        """Gets or sets a value indicating whether the format string should be used in edit mode"""
        ...

    @ApplyFormatInEditMode.setter
    def ApplyFormatInEditMode(self, value: bool):
        """Gets or sets a value indicating whether the format string should be used in edit mode"""
        ...

    @property
    def HtmlEncode(self) -> bool:
        """Gets or sets a value indicating whether the field should be html encoded"""
        ...

    @HtmlEncode.setter
    def HtmlEncode(self, value: bool):
        """Gets or sets a value indicating whether the field should be html encoded"""
        ...

    @property
    def NullDisplayTextResourceType(self) -> typing.Type:
        """
        Gets or sets the Type that contains the resources for NullDisplayText.
            Using NullDisplayTextResourceType along with NullDisplayText, allows the GetNullDisplayText
            method to return localized values.
        """
        ...

    @NullDisplayTextResourceType.setter
    def NullDisplayTextResourceType(self, value: typing.Type):
        """
        Gets or sets the Type that contains the resources for NullDisplayText.
            Using NullDisplayTextResourceType along with NullDisplayText, allows the GetNullDisplayText
            method to return localized values.
        """
        ...

    def __init__(self) -> None:
        """Default constructor"""
        ...

    def GetNullDisplayText(self) -> str:
        """
        Gets the UI display string for NullDisplayText.
            
                This can be either a literal, non-localized string provided to  or the
                localized string found when  has been specified and 
                represents a resource key within that resource type.
        
        :returns: When NullDisplayTextResourceType has not been specified, the value of     NullDisplayText will be returned.              When  has been specified and          represents a resource key within that resource type, then the localized value will be returned.              When  and  have not been set, returns null.
        """
        ...


class DataType(System.Enum):
    """Enumeration of logical data types that may appear in DataTypeAttribute"""

    Custom = 0
    """Custom data type, not one of the static data types we know"""

    DateTime = 1
    """DateTime data type"""

    Date = 2
    """Date data type"""

    Time = 3
    """Time data type"""

    Duration = 4
    """Duration data type"""

    PhoneNumber = 5
    """Phone number data type"""

    Currency = 6
    """Currency data type"""

    Text = 7
    """Plain text data type"""

    Html = 8
    """Html data type"""

    MultilineText = 9
    """Multiline text data type"""

    EmailAddress = 10
    """Email address data type"""

    Password = 11
    """Password data type -- do not echo in UI"""

    Url = 12
    """URL data type"""

    ImageUrl = 13
    """URL to an Image -- to be displayed as an image instead of text"""

    CreditCard = 14
    """Credit card data type"""

    PostalCode = 15
    """Postal code data type"""

    Upload = 16
    """File upload data type"""


class DataTypeAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """
    Allows for clarification of the DataType represented by a given
        property (such as System.ComponentModel.DataAnnotations.DataType.PhoneNumber
        or System.ComponentModel.DataAnnotations.DataType.Url)
    """

    @property
    def DataType(self) -> int:
        """
        Gets the DataType. If it equals DataType.Custom, CustomDataType should also be retrieved.
        
        This property contains the int value of a member of the System.ComponentModel.DataAnnotations.DataType enum.
        """
        ...

    @property
    def CustomDataType(self) -> str:
        """
        Gets the string representing a custom data type. Returns a non-null value only if DataType is
            DataType.Custom.
        """
        ...

    @property
    def DisplayFormat(self) -> System.ComponentModel.DataAnnotations.DisplayFormatAttribute:
        """Gets the default display format that gets used along with this DataType."""
        ...

    @DisplayFormat.setter
    def DisplayFormat(self, value: System.ComponentModel.DataAnnotations.DisplayFormatAttribute):
        """Gets the default display format that gets used along with this DataType."""
        ...

    @overload
    def __init__(self, dataType: System.ComponentModel.DataAnnotations.DataType) -> None:
        """
        Constructor that accepts a data type enumeration
        
        :param dataType: The DataType enum value indicating the type to apply.
        """
        ...

    @overload
    def __init__(self, customDataType: str) -> None:
        """
        Constructor that accepts the string name of a custom data type
        
        :param customDataType: The string name of the custom data type.
        """
        ...

    def GetDataTypeName(self) -> str:
        """
        Return the name of the data type, either using the DataType enum or CustomDataType
            string
        
        :returns: The name of the data type enum.
        """
        ...

    def IsValid(self, value: typing.Any) -> bool:
        """
        Override of ValidationAttribute.IsValid(object)
        
        :param value: The value to validate
        :returns: Unconditionally returns true.
        """
        ...


class PhoneAttribute(System.ComponentModel.DataAnnotations.DataTypeAttribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def IsValid(self, value: typing.Any) -> bool:
        ...


class DisplayAttribute(System.Attribute):
    """
    DisplayAttribute is a general-purpose attribute to specify user-visible globalizable strings for types and members.
        The string properties of this class can be used either as literals or as resource identifiers into a specified
        ResourceType
    """

    @property
    def ShortName(self) -> str:
        ...

    @ShortName.setter
    def ShortName(self, value: str):
        ...

    @property
    def Name(self) -> str:
        """
        Gets or sets the Name attribute property, which may be a resource key string.
            
                Consumers must use the  method to retrieve the UI display string.
        """
        ...

    @Name.setter
    def Name(self, value: str):
        """
        Gets or sets the Name attribute property, which may be a resource key string.
            
                Consumers must use the  method to retrieve the UI display string.
        """
        ...

    @property
    def Description(self) -> str:
        """
        Gets or sets the Description attribute property, which may be a resource key string.
            
                Consumers must use the  method to retrieve the UI display string.
        """
        ...

    @Description.setter
    def Description(self, value: str):
        """
        Gets or sets the Description attribute property, which may be a resource key string.
            
                Consumers must use the  method to retrieve the UI display string.
        """
        ...

    @property
    def Prompt(self) -> str:
        """
        Gets or sets the Prompt attribute property, which may be a resource key string.
            
                Consumers must use the  method to retrieve the UI display string.
        """
        ...

    @Prompt.setter
    def Prompt(self, value: str):
        """
        Gets or sets the Prompt attribute property, which may be a resource key string.
            
                Consumers must use the  method to retrieve the UI display string.
        """
        ...

    @property
    def GroupName(self) -> str:
        """
        Gets or sets the GroupName attribute property, which may be a resource key string.
            
                Consumers must use the  method to retrieve the UI display string.
        """
        ...

    @GroupName.setter
    def GroupName(self, value: str):
        """
        Gets or sets the GroupName attribute property, which may be a resource key string.
            
                Consumers must use the  method to retrieve the UI display string.
        """
        ...

    @property
    def ResourceType(self) -> typing.Type:
        """
        Gets or sets the System.Type that contains the resources for ShortName,
            Name, Description, Prompt, and GroupName.
            Using ResourceType along with these Key properties, allows the GetShortName,
            GetName, GetDescription, GetPrompt, and GetGroupName
            methods to return localized values.
        """
        ...

    @ResourceType.setter
    def ResourceType(self, value: typing.Type):
        """
        Gets or sets the System.Type that contains the resources for ShortName,
            Name, Description, Prompt, and GroupName.
            Using ResourceType along with these Key properties, allows the GetShortName,
            GetName, GetDescription, GetPrompt, and GetGroupName
            methods to return localized values.
        """
        ...

    @property
    def AutoGenerateField(self) -> bool:
        """
        Gets or sets whether UI should be generated automatically to display this field. If this property is not
            set then the presentation layer will automatically determine whether UI should be generated. Setting this
            property allows an override of the default behavior of the presentation layer.
            
                Consumers must use the  method to retrieve the value, as this property
                getter will throw an exception if the value has not been set.
        """
        ...

    @AutoGenerateField.setter
    def AutoGenerateField(self, value: bool):
        """
        Gets or sets whether UI should be generated automatically to display this field. If this property is not
            set then the presentation layer will automatically determine whether UI should be generated. Setting this
            property allows an override of the default behavior of the presentation layer.
            
                Consumers must use the  method to retrieve the value, as this property
                getter will throw an exception if the value has not been set.
        """
        ...

    @property
    def AutoGenerateFilter(self) -> bool:
        """
        Gets or sets whether UI should be generated automatically to display filtering for this field. If this property is
            not set then the presentation layer will automatically determine whether filtering UI should be generated. Setting this
            property allows an override of the default behavior of the presentation layer.
            
                Consumers must use the  method to retrieve the value, as this property
                getter will throw
                an exception if the value has not been set.
        """
        ...

    @AutoGenerateFilter.setter
    def AutoGenerateFilter(self, value: bool):
        """
        Gets or sets whether UI should be generated automatically to display filtering for this field. If this property is
            not set then the presentation layer will automatically determine whether filtering UI should be generated. Setting this
            property allows an override of the default behavior of the presentation layer.
            
                Consumers must use the  method to retrieve the value, as this property
                getter will throw
                an exception if the value has not been set.
        """
        ...

    @property
    def Order(self) -> int:
        """
        Gets or sets the order in which this field should be displayed.  If this property is not set then
            the presentation layer will automatically determine the order.  Setting this property explicitly
            allows an override of the default behavior of the presentation layer.
            
                Consumers must use the  method to retrieve the value, as this property getter will throw
                an exception if the value has not been set.
        """
        ...

    @Order.setter
    def Order(self, value: int):
        """
        Gets or sets the order in which this field should be displayed.  If this property is not set then
            the presentation layer will automatically determine the order.  Setting this property explicitly
            allows an override of the default behavior of the presentation layer.
            
                Consumers must use the  method to retrieve the value, as this property getter will throw
                an exception if the value has not been set.
        """
        ...

    def GetAutoGenerateField(self) -> typing.Optional[bool]:
        """
        Gets the value of AutoGenerateField if it has been set, or null.
        
        :returns: When AutoGenerateField has been set returns the value of that property.              When  has not been set returns null.
        """
        ...

    def GetAutoGenerateFilter(self) -> typing.Optional[bool]:
        """
        Gets the value of AutoGenerateFilter if it has been set, or null.
        
        :returns: When AutoGenerateFilter has been set returns the value of that property.              When  has not been set returns null.
        """
        ...

    def GetDescription(self) -> str:
        """
        Gets the UI display string for Description.
            
                This can be either a literal, non-localized string provided to  or the
                localized string found when  has been specified and 
                represents a resource key within that resource type.
        
        :returns: When ResourceType has not been specified, the value of     Description will be returned.              When  has been specified and          represents a resource key within that resource type, then the localized value will be returned.
        """
        ...

    def GetGroupName(self) -> str:
        """
        Gets the UI display string for GroupName.
            
                This can be either a literal, non-localized string provided to  or the
                localized string found when  has been specified and 
                represents a resource key within that resource type.
        
        :returns: When ResourceType has not been specified, the value of     GroupName will be returned.              When  has been specified and          represents a resource key within that resource type, then the localized value will be returned.
        """
        ...

    def GetName(self) -> str:
        """
        Gets the UI display string for Name.
            
                This can be either a literal, non-localized string provided to  or the
                localized string found when  has been specified and 
                represents a resource key within that resource type.
        
        :returns: When ResourceType has not been specified, the value of     Name will be returned.              When  has been specified and          represents a resource key within that resource type, then the localized value will be returned.              Can return null and will not fall back onto other values, as it's more likely for the         consumer to want to fall back onto the property name.
        """
        ...

    def GetOrder(self) -> typing.Optional[int]:
        """
        Gets the value of Order if it has been set, or null.
        
        :returns: When Order has been set returns the value of that property.              When  has not been set returns null.
        """
        ...

    def GetPrompt(self) -> str:
        """
        Gets the UI display string for Prompt.
            
                This can be either a literal, non-localized string provided to  or the
                localized string found when  has been specified and 
                represents a resource key within that resource type.
        
        :returns: When ResourceType has not been specified, the value of     Prompt will be returned.              When  has been specified and          represents a resource key within that resource type, then the localized value will be returned.
        """
        ...

    def GetShortName(self) -> str:
        ...


class UIHintAttribute(System.Attribute):
    """Attribute to provide a hint to the presentation layer about what control it should use"""

    @property
    def UIHint(self) -> str:
        """Gets the name of the control that is most appropriate for this associated property or field"""
        ...

    @property
    def PresentationLayer(self) -> str:
        """Gets the name of the presentation layer that supports the control type in UIHint"""
        ...

    @property
    def ControlParameters(self) -> System.Collections.Generic.IDictionary[str, System.Object]:
        """Gets the name-value pairs used as parameters to the control's constructor"""
        ...

    @overload
    def __init__(self, uiHint: str) -> None:
        """
        Constructor that accepts the name of the control, without specifying which presentation layer to use
        
        :param uiHint: The name of the UI control.
        """
        ...

    @overload
    def __init__(self, uiHint: str, presentationLayer: str) -> None:
        """
        Constructor that accepts both the name of the control as well as the presentation layer
        
        :param uiHint: The name of the control to use
        :param presentationLayer: The name of the presentation layer that supports this control
        """
        ...

    @overload
    def __init__(self, uiHint: str, presentationLayer: str, *controlParameters: typing.Any) -> None:
        """
        Full constructor that accepts the name of the control, presentation layer, and optional parameters
            to use when constructing the control
        
        :param uiHint: The name of the control
        :param presentationLayer: The presentation layer
        :param controlParameters: The list of parameters for the control
        """
        ...

    def Equals(self, obj: typing.Any) -> bool:
        ...

    def GetHashCode(self) -> int:
        ...


class EnumDataTypeAttribute(System.ComponentModel.DataAnnotations.DataTypeAttribute):
    """This class has no documentation."""

    @property
    def EnumType(self) -> typing.Type:
        ...

    def __init__(self, enumType: typing.Type) -> None:
        ...

    def IsValid(self, value: typing.Any) -> bool:
        ...


class MinLengthAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """Specifies the minimum length of collection/string data allowed in a property."""

    @property
    def Length(self) -> int:
        """Gets the minimum allowable length of the collection/string data."""
        ...

    def __init__(self, length: int) -> None:
        """
        Initializes a new instance of the MinLengthAttribute class.
        
        :param length: The minimum allowable length of collection/string data.     Value must be greater than or equal to zero.
        """
        ...

    def FormatErrorMessage(self, name: str) -> str:
        """
        Applies formatting to a specified error message. (Overrides ValidationAttribute.FormatErrorMessage)
        
        :param name: The name to include in the formatted string.
        :returns: A localized string to describe the minimum acceptable length.
        """
        ...

    def IsValid(self, value: typing.Any) -> bool:
        """
        Determines whether a specified object is valid. (Overrides ValidationAttribute.IsValid(object))
        
        :param value: The object to validate.
        :returns: true if the value is null or greater than or equal to the specified minimum length, otherwise     false.
        """
        ...


class MetadataTypeAttribute(System.Attribute):
    """Specifies the metadata class to associate with a data model class."""

    @property
    def MetadataClassType(self) -> typing.Type:
        """Gets the metadata class that is associated with a data-model partial class."""
        ...

    def __init__(self, metadataClassType: typing.Type) -> None:
        """
        Initializes a new instance of the System.ComponentModel.DataAnnotations.MetadataTypeAttribute
        class.
        
        :param metadataClassType: The metadata class to reference.
        """
        ...


class RangeAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """Used for specifying a range constraint"""

    @property
    def Minimum(self) -> System.Object:
        """Gets the minimum value for the range"""
        ...

    @Minimum.setter
    def Minimum(self, value: System.Object):
        """Gets the minimum value for the range"""
        ...

    @property
    def Maximum(self) -> System.Object:
        """Gets the maximum value for the range"""
        ...

    @Maximum.setter
    def Maximum(self, value: System.Object):
        """Gets the maximum value for the range"""
        ...

    @property
    def OperandType(self) -> typing.Type:
        """
        Gets the type of the Minimum and Maximum values (e.g. Int32, Double, or some custom
            type)
        """
        ...

    @property
    def ParseLimitsInInvariantCulture(self) -> bool:
        """
        Determines whether string values for Minimum and Maximum are parsed in the invariant
        culture rather than the current culture in effect at the time of the validation.
        """
        ...

    @ParseLimitsInInvariantCulture.setter
    def ParseLimitsInInvariantCulture(self, value: bool):
        """
        Determines whether string values for Minimum and Maximum are parsed in the invariant
        culture rather than the current culture in effect at the time of the validation.
        """
        ...

    @property
    def ConvertValueInInvariantCulture(self) -> bool:
        """
        Determines whether any conversions necessary from the value being validated to OperandType as set
        by the type parameter of the RangeAttribute(Type, string, string) constructor are carried
        out in the invariant culture rather than the current culture in effect at the time of the validation.
        """
        ...

    @ConvertValueInInvariantCulture.setter
    def ConvertValueInInvariantCulture(self, value: bool):
        """
        Determines whether any conversions necessary from the value being validated to OperandType as set
        by the type parameter of the RangeAttribute(Type, string, string) constructor are carried
        out in the invariant culture rather than the current culture in effect at the time of the validation.
        """
        ...

    @overload
    def __init__(self, minimum: int, maximum: int) -> None:
        """
        Constructor that takes integer minimum and maximum values
        
        :param minimum: The minimum value, inclusive
        :param maximum: The maximum value, inclusive
        """
        ...

    @overload
    def __init__(self, minimum: float, maximum: float) -> None:
        """
        Constructor that takes double minimum and maximum values
        
        :param minimum: The minimum value, inclusive
        :param maximum: The maximum value, inclusive
        """
        ...

    @overload
    def __init__(self, type: typing.Type, minimum: str, maximum: str) -> None:
        """
        Allows for specifying range for arbitrary types. The minimum and maximum strings
            will be converted to the target type.
        
        :param type: The type of the range parameters. Must implement IComparable.
        :param minimum: The minimum allowable value.
        :param maximum: The maximum allowable value.
        """
        ...

    def FormatErrorMessage(self, name: str) -> str:
        """
        Override of ValidationAttribute.FormatErrorMessage
        
        :param name: The user-visible name to include in the formatted message.
        :returns: A localized string describing the minimum and maximum values.
        """
        ...

    def IsValid(self, value: typing.Any) -> bool:
        """
        Returns true if the value falls between min and max, inclusive.
        
        :param value: The value to test for validity.
        :returns: true means the  is valid.
        """
        ...


class ValidationException(System.Exception):
    """Exception used for validation using ValidationAttribute."""

    @property
    def ValidationAttribute(self) -> System.ComponentModel.DataAnnotations.ValidationAttribute:
        """Gets the ValidationAttribute instance that triggered this exception."""
        ...

    @property
    def ValidationResult(self) -> System.ComponentModel.DataAnnotations.ValidationResult:
        """Gets the ValidationResult instance that describes the validation error."""
        ...

    @property
    def Value(self) -> System.Object:
        """Gets the value that caused the validating attribute to trigger the exception"""
        ...

    @overload
    def __init__(self, validationResult: System.ComponentModel.DataAnnotations.ValidationResult, validatingAttribute: System.ComponentModel.DataAnnotations.ValidationAttribute, value: typing.Any) -> None:
        """
        Constructor that accepts a structured ValidationResult describing the problem.
        
        :param validationResult: The value describing the validation error
        :param validatingAttribute: The attribute that triggered this exception
        :param value: The value that caused the validating attribute to trigger the exception
        """
        ...

    @overload
    def __init__(self, errorMessage: str, validatingAttribute: System.ComponentModel.DataAnnotations.ValidationAttribute, value: typing.Any) -> None:
        """
        Constructor that accepts an error message, the failing attribute, and the invalid value.
        
        :param errorMessage: The localized error message
        :param validatingAttribute: The attribute that triggered this exception
        :param value: The value that caused the validating attribute to trigger the exception
        """
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor."""
        ...

    @overload
    def __init__(self, message: str) -> None:
        """
        Constructor that accepts only a localized message
        
        :param message: The localized message
        """
        ...

    @overload
    def __init__(self, message: str, innerException: System.Exception) -> None:
        """
        Constructor that accepts a localized message and an inner exception
        
        :param message: The localized error message
        :param innerException: inner exception
        """
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        Constructor that takes a SerializationInfo.
        
        This method is protected.
        
        :param info: The SerializationInfo.
        :param context: The StreamingContext.
        """
        ...


class KeyAttribute(System.Attribute):
    """Used to mark one or more entity properties that provide the entity's unique identity"""


class FileExtensionsAttribute(System.ComponentModel.DataAnnotations.DataTypeAttribute):
    """This class has no documentation."""

    @property
    def Extensions(self) -> str:
        ...

    @Extensions.setter
    def Extensions(self, value: str):
        ...

    def __init__(self) -> None:
        ...

    def FormatErrorMessage(self, name: str) -> str:
        ...

    def IsValid(self, value: typing.Any) -> bool:
        ...


class Validator(System.Object):
    """
    Helper class to validate objects, properties and other values using their associated
        ValidationAttribute
        custom attributes.
    """

    @staticmethod
    @overload
    def TryValidateObject(instance: typing.Any, validationContext: System.ComponentModel.DataAnnotations.ValidationContext, validationResults: System.Collections.Generic.ICollection[System.ComponentModel.DataAnnotations.ValidationResult]) -> bool:
        """
        Tests whether the given object instance is valid.
        
        :param instance: The object instance to test.  It cannot be null.
        :param validationContext: Describes the object to validate and provides services and context for the validators.
        :param validationResults: Optional collection to receive ValidationResults for the failures.
        :returns: true if the object is valid, false if any validation errors are encountered.
        """
        ...

    @staticmethod
    @overload
    def TryValidateObject(instance: typing.Any, validationContext: System.ComponentModel.DataAnnotations.ValidationContext, validationResults: System.Collections.Generic.ICollection[System.ComponentModel.DataAnnotations.ValidationResult], validateAllProperties: bool) -> bool:
        """
        Tests whether the given object instance is valid.
        
        :param instance: The object instance to test.  It cannot be null.
        :param validationContext: Describes the object to validate and provides services and context for the validators.
        :param validationResults: Optional collection to receive ValidationResults for the failures.
        :param validateAllProperties: If true, also evaluates all properties of the object (this process is not     recursive over properties of the properties).
        :returns: true if the object is valid, false if any validation errors are encountered.
        """
        ...

    @staticmethod
    def TryValidateProperty(value: typing.Any, validationContext: System.ComponentModel.DataAnnotations.ValidationContext, validationResults: System.Collections.Generic.ICollection[System.ComponentModel.DataAnnotations.ValidationResult]) -> bool:
        """
        Tests whether the given property value is valid.
        
        :param value: The value to test.
        :param validationContext: Describes the property member to validate and provides services and context for the     validators.
        :param validationResults: Optional collection to receive ValidationResults for the failures.
        :returns: true if the value is valid, false if any validation errors are encountered.
        """
        ...

    @staticmethod
    def TryValidateValue(value: typing.Any, validationContext: System.ComponentModel.DataAnnotations.ValidationContext, validationResults: System.Collections.Generic.ICollection[System.ComponentModel.DataAnnotations.ValidationResult], validationAttributes: System.Collections.Generic.IEnumerable[System.ComponentModel.DataAnnotations.ValidationAttribute]) -> bool:
        """
        Tests whether the given value is valid against a specified list of ValidationAttributes.
        
        :param value: The value to test.  It cannot be null.
        :param validationContext: Describes the object being validated and provides services and context for the     validators.
        :param validationResults: Optional collection to receive ValidationResults for the failures.
        :param validationAttributes: The list of ValidationAttributes to validate this      against.
        :returns: true if the object is valid, false if any validation errors are encountered.
        """
        ...

    @staticmethod
    @overload
    def ValidateObject(instance: typing.Any, validationContext: System.ComponentModel.DataAnnotations.ValidationContext) -> None:
        """
        Throws a ValidationException if the given  is not valid.
        
        :param instance: The object instance to test.  It cannot be null.
        :param validationContext: Describes the object being validated and provides services and context for the     validators.  It cannot be null.
        """
        ...

    @staticmethod
    @overload
    def ValidateObject(instance: typing.Any, validationContext: System.ComponentModel.DataAnnotations.ValidationContext, validateAllProperties: bool) -> None:
        """
        Throws a ValidationException if the given object instance is not valid.
        
        :param instance: The object instance to test.  It cannot be null.
        :param validationContext: Describes the object being validated and provides services and context for the     validators.  It cannot be null.
        :param validateAllProperties: If true, also validates all the 's properties.
        """
        ...

    @staticmethod
    def ValidateProperty(value: typing.Any, validationContext: System.ComponentModel.DataAnnotations.ValidationContext) -> None:
        """
        Throws a ValidationException if the given property  is not valid.
        
        :param value: The value to test.
        :param validationContext: Describes the object being validated and provides services and context for the     validators.  It cannot be null.
        """
        ...

    @staticmethod
    def ValidateValue(value: typing.Any, validationContext: System.ComponentModel.DataAnnotations.ValidationContext, validationAttributes: System.Collections.Generic.IEnumerable[System.ComponentModel.DataAnnotations.ValidationAttribute]) -> None:
        """
        Throw a ValidationException if the given value is not valid for the
            ValidationAttributes.
        
        :param value: The value to test.  It cannot be null.
        :param validationContext: Describes the object being tested.
        :param validationAttributes: The list of ValidationAttributes to validate against this instance.
        """
        ...


class CreditCardAttribute(System.ComponentModel.DataAnnotations.DataTypeAttribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def IsValid(self, value: typing.Any) -> bool:
        ...


class TimestampAttribute(System.Attribute):
    """This attribute is used to mark a Timestamp member of a Type."""


class UrlAttribute(System.ComponentModel.DataAnnotations.DataTypeAttribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def IsValid(self, value: typing.Any) -> bool:
        ...


class MaxLengthAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """Specifies the maximum length of collection/string data allowed in a property."""

    @property
    def Length(self) -> int:
        """Gets the maximum allowable length of the collection/string data."""
        ...

    @overload
    def __init__(self, length: int) -> None:
        """
        Initializes a new instance of the MaxLengthAttribute class.
        
        :param length: The maximum allowable length of collection/string data.     Value must be greater than zero.
        """
        ...

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the MaxLengthAttribute class.
            The maximum allowable length supported by the database will be used.
        """
        ...

    def FormatErrorMessage(self, name: str) -> str:
        """
        Applies formatting to a specified error message. (Overrides ValidationAttribute.FormatErrorMessage)
        
        :param name: The name to include in the formatted string.
        :returns: A localized string to describe the maximum acceptable length.
        """
        ...

    def IsValid(self, value: typing.Any) -> bool:
        """
        Determines whether a specified object is valid. (Overrides ValidationAttribute.IsValid(object))
        
        :param value: The object to validate.
        :returns: true if the value is null or less than or equal to the specified maximum length, otherwise false.
        """
        ...


class AssociatedMetadataTypeTypeDescriptionProvider(System.ComponentModel.TypeDescriptionProvider):
    """
    Extends the metadata information for a class by adding attributes and property
    information that is defined in an associated class.
    """

    @overload
    def __init__(self, type: typing.Type) -> None:
        """
        Initializes a new instance of the System.ComponentModel.DataAnnotations.AssociatedMetadataTypeTypeDescriptionProvider
        class by using the specified type.
        
        :param type: The type for which the metadata provider is created.
        """
        ...

    @overload
    def __init__(self, type: typing.Type, associatedMetadataType: typing.Type) -> None:
        """
        Initializes a new instance of the System.ComponentModel.DataAnnotations.AssociatedMetadataTypeTypeDescriptionProvider
        class by using the specified metadata provider type and associated type.
        
        :param type: The type for which the metadata provider is created.
        :param associatedMetadataType: The associated type that contains the metadata.
        """
        ...

    def GetTypeDescriptor(self, objectType: typing.Type, instance: typing.Any) -> System.ComponentModel.ICustomTypeDescriptor:
        """
        Gets a type descriptor for the specified type and object.
        
        :param objectType: The type of object to retrieve the type descriptor for.
        :param instance: An instance of the type.
        :returns: The descriptor that provides metadata for the type.
        """
        ...


class EditableAttribute(System.Attribute):
    """
    Indicates whether the consumer of a field or property, such as a client application,
        should allow editing of the value.
    """

    @property
    def AllowEdit(self) -> bool:
        """
        Indicates whether or not the field/property allows editing of the
            value.
        """
        ...

    @property
    def AllowInitialValue(self) -> bool:
        """
        Indicates whether or not the field/property allows an initial value
            to be specified.
        """
        ...

    @AllowInitialValue.setter
    def AllowInitialValue(self, value: bool):
        """
        Indicates whether or not the field/property allows an initial value
            to be specified.
        """
        ...

    def __init__(self, allowEdit: bool) -> None:
        """
        Indicate whether or not a field/property is editable.
        
        :param allowEdit: Indicates whether the field/property is editable.  The value provided     will apply to both AllowEdit and     AllowInitialValue unless the AllowInitialValue     property is explicitly specified.
        """
        ...


class EmailAddressAttribute(System.ComponentModel.DataAnnotations.DataTypeAttribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def IsValid(self, value: typing.Any) -> bool:
        ...


class CompareAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """This class has no documentation."""

    @property
    def OtherProperty(self) -> str:
        ...

    @property
    def OtherPropertyDisplayName(self) -> str:
        ...

    @OtherPropertyDisplayName.setter
    def OtherPropertyDisplayName(self, value: str):
        ...

    @property
    def RequiresValidationContext(self) -> bool:
        ...

    def __init__(self, otherProperty: str) -> None:
        ...

    def FormatErrorMessage(self, name: str) -> str:
        ...

    def IsValid(self, value: typing.Any, validationContext: System.ComponentModel.DataAnnotations.ValidationContext) -> System.ComponentModel.DataAnnotations.ValidationResult:
        """This method is protected."""
        ...


class IValidatableObject(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def Validate(self, validationContext: System.ComponentModel.DataAnnotations.ValidationContext) -> System.Collections.Generic.IEnumerable[System.ComponentModel.DataAnnotations.ValidationResult]:
        ...


class RequiredAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """Validation attribute to indicate that a property field or parameter is required."""

    @property
    def AllowEmptyStrings(self) -> bool:
        """Gets or sets a flag indicating whether the attribute should allow empty strings."""
        ...

    @AllowEmptyStrings.setter
    def AllowEmptyStrings(self, value: bool):
        """Gets or sets a flag indicating whether the attribute should allow empty strings."""
        ...

    def __init__(self) -> None:
        """Default constructor."""
        ...

    def IsValid(self, value: typing.Any) -> bool:
        """
        Override of ValidationAttribute.IsValid(object)
        
        :param value: The value to test
        :returns: false if the  is null or an empty string. If     RequiredAttribute.AllowEmptyStrings     then false is returned only if  is null.
        """
        ...


class ConcurrencyCheckAttribute(System.Attribute):
    """
    This attribute is used to mark the members of a Type that participate in
        optimistic concurrency checks.
    """


class CustomValidationAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """
    Validation attribute that executes a user-supplied method at runtime, using one of these signatures:
        
            public static  Method(object value) { ... }
        
            public static  Method(object value,  context) {
            ... }
        
            The value can be strongly typed as type conversion will be attempted.
    """

    @property
    def ValidatorType(self) -> typing.Type:
        ...

    @property
    def TypeId(self) -> System.Object:
        """Gets a unique identifier for this attribute."""
        ...

    @property
    def Method(self) -> str:
        """Gets the name of the method in ValidatorType to invoke to perform validation."""
        ...

    @property
    def RequiresValidationContext(self) -> bool:
        ...

    def __init__(self, validatorType: typing.Type, method: str) -> None:
        ...

    def FormatErrorMessage(self, name: str) -> str:
        """
        Override of ValidationAttribute.FormatErrorMessage
        
        :param name: The name to include in the formatted string
        :returns: A localized string to describe the problem.
        """
        ...

    def IsValid(self, value: typing.Any, validationContext: System.ComponentModel.DataAnnotations.ValidationContext) -> System.ComponentModel.DataAnnotations.ValidationResult:
        """This method is protected."""
        ...


class DisplayColumnAttribute(System.Attribute):
    """
    Sets the display column, the sort column, and the sort order for when a table is used as a parent table in FK
        relationships.
    """

    @property
    def DisplayColumn(self) -> str:
        ...

    @property
    def SortColumn(self) -> str:
        ...

    @property
    def SortDescending(self) -> bool:
        ...

    @overload
    def __init__(self, displayColumn: str) -> None:
        ...

    @overload
    def __init__(self, displayColumn: str, sortColumn: str) -> None:
        ...

    @overload
    def __init__(self, displayColumn: str, sortColumn: str, sortDescending: bool) -> None:
        ...


class RegularExpressionAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """Regular expression validation attribute"""

    @property
    def MatchTimeoutInMilliseconds(self) -> int:
        """
        Gets or sets the timeout to use when matching the regular expression pattern (in milliseconds)
            (-1 means never timeout).
        """
        ...

    @MatchTimeoutInMilliseconds.setter
    def MatchTimeoutInMilliseconds(self, value: int):
        """
        Gets or sets the timeout to use when matching the regular expression pattern (in milliseconds)
            (-1 means never timeout).
        """
        ...

    @property
    def MatchTimeout(self) -> datetime.timedelta:
        """Gets the timeout to use when matching the regular expression pattern"""
        ...

    @property
    def Pattern(self) -> str:
        """Gets the regular expression pattern to use"""
        ...

    def __init__(self, pattern: str) -> None:
        """
        Constructor that accepts the regular expression pattern
        
        :param pattern: The regular expression to use.  It cannot be null.
        """
        ...

    def FormatErrorMessage(self, name: str) -> str:
        """
        Override of ValidationAttribute.FormatErrorMessage
        
        :param name: The user-visible name to include in the formatted message.
        :returns: The localized message to present to the user.
        """
        ...

    def IsValid(self, value: typing.Any) -> bool:
        """
        Override of ValidationAttribute.IsValid(object)
        
        :param value: The value to test for validity.
        :returns: true if the given value matches the current regular expression pattern.
        """
        ...


