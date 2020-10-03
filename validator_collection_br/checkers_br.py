import validator_collection_br.validators_br as validators_br

from validator_collection._decorators import disable_checker_on_env


@disable_checker_on_env
def is_cnpj(value, **kwargs):
    """Indicate whether value is a brazilian cnpj number.
    Note:
        param value: The value to evaluate.
        returns: True if value is valid, False if it is not.
        rtype: :class:bool <python:bool>
        raises SyntaxError: if kwargs contains duplicate keyword parameters or duplicates
            keyword parameters passed to the underlying validator
    """
    try:
        value = validators_br.cnpj(value, **kwargs)
    except SyntaxError as error:
        raise error
    except Exception:
        return False

    return True


@disable_checker_on_env
def is_cpf(value, **kwargs):
    """Indicate whether value is a brazilian cpf number.
    Note:
        param value: The value to evaluate.
        returns: True if value is valid, False if it is not.
        rtype: class:bool <python:bool>
        raises SyntaxError: if kwargs contains duplicate keyword parameters or duplicates
                             keyword parameters passed to the underlying validator
    """
    try:
        value = validators_br.cpf(value, **kwargs)
    except SyntaxError as error:
        raise error
    except Exception:
        return False

    return True


@disable_checker_on_env
def is_cnj(value, **kwargs):
    """Indicate whether value is a brazilian lawsuit number.
    Note:
        param value: The value to evaluate.
        returns: True if value is valid, False if it is not.
        return type: class:bool <python:bool>
        raises SyntaxError: if kwargs contains duplicate keyword parameters or duplicates
                            keyword parameters passed to the underlying validator
    """
    try:
        value = validators_br.cnj(value, **kwargs)
    except SyntaxError as error:
        raise error
    except Exception:
        return False

    return True


@disable_checker_on_env
def is_person_full_name(value, **kwargs):
    """Indicate whether value is a person full name.
    Note:
        param value: The value to evaluate.
        returns: True if value is valid, False if it is not.
        rtype: :class:bool <python:bool>
        raises SyntaxError: if kwargs contains duplicate keyword parameters or duplicates
            keyword parameters passed to the underlying validator
    """
    try:
        value = validators_br.person_full_name(value, **kwargs)
    except SyntaxError as error:
        raise error
    except Exception:
        return False

    return True
