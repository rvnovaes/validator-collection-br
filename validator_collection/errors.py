class NotInListError(ValueError):
    """Exception raised when the {value} is not in the list. The validator does
    not allow values that there are not in the list.
    """
    pass