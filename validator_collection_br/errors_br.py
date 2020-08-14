class NotInListError(ValueError):
    """Exception raised when the {value} is not in the list. The validator does
    not allow values that there are not in the list.
    """
    pass


class DataTypeError(TypeError):
    """Exception raised when a value is an unexpected datatype.

    **INHERITS FROM:** :class:`TypeError <python:TypeError>`

    """
    pass


class InvalidCpfError(ValueError):
    """Exception thrown when value has unexpected check digits.

    **INHERITS FROM:** :class:`ValueError <python:ValueError>`

    """
    pass


class InvalidCpfEqualError(ValueError):
    """Exception thrown when all digits of value are equal

    **INHERITS FROM:** :class:`ValueError <python:ValueError>`

    """
    pass


class InvalidCpfMaskError(ValueError):
    """Exception thrown when value does not follow xxx.xxx.xxx-xx pattern. x must be a digit

    **INHERITS FROM:** :class:`ValueError <python:ValueError>`

    """
    pass


class InvalidCnpjError(ValueError):
    """Exception thrown when value has unexpected check digits.

    **INHERITS FROM:** :class:`ValueError <python:ValueError>`

    """
    pass


class InvalidCnpjMaskError(ValueError):
    """Exception thrown when value has unexpected check digits.

    **INHERITS FROM:** :class:`ValueError <python:ValueError>`

    """
    pass


class InvalidCnpjEqualError(ValueError):
    """Exception thrown when all digits of value are equal

    **INHERITS FROM:** :class:`ValueError <python:ValueError>`

    """
    pass


class InvalidCnjError(ValueError):
    """Exception thrown when value has unexpected check digits.

    **INHERITS FROM:** :class:`ValueError <python:ValueError>`

    """
    pass


class InvalidCnjMaskError(ValueError):
    """Exception thrown when value has unexpected check digits.

    **INHERITS FROM:** :class:`ValueError <python:ValueError>`

    """
    pass


class InvalidFullNameError(ValueError):
    """Exception thrown when value has unexpected check digits.

    **INHERITS FROM:** :class:`ValueError <python:ValueError>`

    """
    pass
