from validator_collection.errors import *


class EmptyValueErrorMsg(EmptyValueError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


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

class InvalidCnpjError(ValueError):
    """Exception thrown when value has unexpected check digits.

    **INHERITS FROM:** :class:`ValueError <python:ValueError>`

    """
    pass

class InvalidCnjError(ValueError):
    """Exception thrown when value has unexpected check digits.

    **INHERITS FROM:** :class:`ValueError <python:ValueError>`

    """
    pass