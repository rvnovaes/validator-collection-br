import re
import numpy as np
from validator_collection_br import errors_br
from validator_collection import errors

CELLPHONE_REGEX = re.compile(
    r'\(?([0]?[1-9][0-9])\)?\s?(9)?\s?((9|8|7)\d{3})\s?-?\s?(\d{4})$'
)
ALPHANUMERIC_REGEX = re.compile(
    r'^[a-zA-Z0-9_]+$'
)

CPF_REGEX = re.compile(r'\d{3}\.\d{3}\.\d{3}-\d{2}')

CNPJ_REGEX = re.compile(r'\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}')

CNJ_REGEX = re.compile(
    r"/[0-9]{7}\-[0-9]{2}\.[0-9]{4}\.[0-9]{1}\.[0-9]{2}\.[0-9]{4}/"
)

# permite caracteres com e sem acentuacao, ', - e deve ter pelo menos um espaco entre as palavras
NOME_COMPLETO_REGEX = re.compile(r"^['-a-zA-ZA-zÀ-ÿ]+(?:\s['-a-zA-ZA-zÀ-ÿ]+)+$")


def cpf(value, allow_empty=False):
    """
    Method to validate brazilian cpfs
    Parameters:
        - value (str) - The value to validate.
        - allow_empty (boll) - If True, returns None if value is empty. If False, returns EmptyValueError.

    Returns:
        - Value

    Raises:
        - EmptyValueError – if value is None and allow_empty is False
        - MinimumLenghtError – if minimum is supplied and value is less than the 11 characters
        - MaximumLenghtError – if maximum is supplied and value is more than the 11 characters
        - DataTypeError – If value not is String
        - InvalidCpfMaskError – If value not is not xxx.xxx.xxx-xx and x is not a digit
        - InvalidCpfError – If value not is valid cpf
    """
    # stores the original passed value to be returned in the end if all validations pass
    cpf = value

    # check empty
    if not value and not allow_empty:
        raise errors.EmptyValueError('O valor do CPF não pode ser vazio.')
    elif not value:
        return None

    # check datatype
    if not isinstance(value, str):
        raise errors_br.DataTypeError('O CPF digitado não é uma string.')

    # whitespace_padding
    value = value.strip()

    # remove mask just to verify first length and provide more specific error msg
    unmasked_value = value.replace('-', '').replace('.', '')

    # Verifying min and max lenght of the cpf
    if len(unmasked_value) < 11:
        raise errors.MinimumLengthError('O CPF digitado tem menos de 11 dígitos.')
    if len(unmasked_value) > 11:
        raise errors.MaximumLengthError('O CPF digitado tem mais de 11 dígitos.')

    # apply regex to masked value
    if not CPF_REGEX.match(value):
        raise errors_br.InvalidCpfMaskError('O CPF deve ter o formato xxx.xxx.xxx-xx e não pode conter letras ou caracteres especiais.')

    # defining the two vectors of validation --> http://www.macoratti.net/alg_cpf.htm
    lista_validacao_um = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    lista_validacao_dois = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    # extract the verifying digits as string for later comparison
    verificadores = unmasked_value[-2:]

    # transforms the str into a list of characters
    unmasked_value_list = list(unmasked_value)

    # Verifying if the digits are equal
    if all(i == unmasked_value_list[0] for i in unmasked_value_list):
        raise errors_br.InvalidCpfEqualError('O CPF não pode ter todos os dígitos idênticos.')

    # casts each character to int
    unmasked_value_int_list = [int(i) for i in unmasked_value_list]

    # calculating the first digit
    cabeca = unmasked_value_int_list[:9]
    dot_prod_1 = np.dot(cabeca, lista_validacao_um)
    dig_1_seed = dot_prod_1 % 11

    if dig_1_seed < 2:
        digito_1 = 0
    else:
        digito_1 = 11 - dig_1_seed

    # calculating the second digit
    cabeca.append(digito_1)
    dot_prod_2 = np.dot(cabeca, lista_validacao_dois)
    dig_2_seed = dot_prod_2 % 11

    if dig_2_seed < 2:
        digito_2 = 0
    else:
        digito_2 = 11 - dig_2_seed

    digito_1 = str(digito_1)
    digito_2 = str(digito_2)

    if not bool(verificadores == digito_1 + digito_2):
        raise errors_br.InvalidCpfError('O CPF digitado é inválido.')

    return cpf


def cnpj(value, allow_empty=False):
    """
    Method to validate brazilian cnpjs
    Parameters:
        - value (str) - The value to validate.
        - allow_empty (boll) - If True, returns None if value is empty. If False, returns EmptyValueError.

    Returns:
        - Value

    Raises:
        - EmptyValueError – if value is None and allow_empty is False
        - MinimumValueError – if minimum is supplied and value is less than the 11 characters
        - MaximumValueError – if maximum is supplied and value is more than the 11 characters
        - DataTypeError – If value not is String
        - InvalidCnpjMaskError – If value not is not xx.xxx.xxx/xxxx-xx and x is not a digit
        - InvalidCnpjError – If value not is valid cnpj
    """
    # stores the original passed value to be returned in the end if all validations pass
    cnpj = value

    # verify empty
    if not value and not allow_empty:
        raise errors.EmptyValueError('O valor do CNPJ não pode ser vazio.')
    elif not value:
        return None

    # verify datatype
    if not isinstance(value, str):
        raise errors_br.DataTypeError('O CNPJ digitado não é uma string.')

    # whitespace_padding
    value = value.strip()

    # remove mask just to verify first length and provide more specific error msg
    unmasked_value = value.replace('-', '').replace('.', '').replace('/', '')

    # Verifying min and max lenght of the cpf
    if len(unmasked_value) < 14:
        raise errors.MinimumLengthError('O CNPJ digitado tem menos de 14 dígitos.')
    if len(unmasked_value) > 14:
        raise errors.MaximumLengthError('O CNPJ digitado tem mais de 14 dígitos.')

    # apply regex to masked value
    if not CNPJ_REGEX.match(value):
        raise errors_br.InvalidCnpjMaskError(
            'O CNPJ deve ter o formato xx.xxx.xxx/xxxx-xx e não pode conter letras ou caracteres especiais.')

    # defining the two vectors of validation --> http://www.macoratti.net/alg_cpf.htm
    lista_validacao_um = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    lista_validacao_dois = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    # extract the verifying digits as string for later comparison
    verificadores = unmasked_value[-2:]

    # transforms the str into a list of characters
    unmasked_value_list = list(unmasked_value)

    # Verifying if the digits are equal
    if all(i == unmasked_value_list[0] for i in unmasked_value_list):
        raise errors_br.InvalidCnpjEqualError('O CNPJ não pode ter todos os dígitos idênticos.')

    # transforms the str into a list of characters
    unmasked_value_list = list(unmasked_value)

    # casts each character to int
    unmasked_value_int_list = [int(i) for i in unmasked_value_list]

    # calculating the first digit
    cabeca = unmasked_value_int_list[:12]
    dot_prod_1 = np.dot(cabeca, lista_validacao_um)
    dig_1_seed = dot_prod_1 % 11

    if dig_1_seed < 2:
        digito_1 = 0
    else:
        digito_1 = 11 - dig_1_seed

    # calculating the second digit
    cabeca.append(digito_1)
    dot_prod_2 = np.dot(cabeca, lista_validacao_dois)
    dig_2_seed = dot_prod_2 % 11

    if dig_2_seed < 2:
        digito_2 = 0
    else:
        digito_2 = 11 - dig_2_seed

    digito_1 = str(digito_1)
    digito_2 = str(digito_2)

    # returning
    if not bool(verificadores == digito_1 + digito_2):
        raise errors_br.InvalidCnpjError('O CNPJ digitado é inválido.')

    return cnpj


def cnj(value, allow_empty=False):
    """
    Method to validate brazilian cnjs
    Parameters:
        - value (str) - The value to validate.
        - allow_empty (boll) - If True, returns None if value is empty. If False, returns EmptyValueError.

    Returns:
        - Value

    Raises:
        - EmptyValueError – if value is None and allow_empty is False
        - MinimumValueError – if minimum is supplied and value is less than the 20 characters
        - MaximumValueError – if maximum is supplied and value is more than the 20 characters
        - DataTypeError – If value not is String
        - InvalidCnjError – If value not is valid cpf
    """
    # verify empty
    if not value and not allow_empty:
        raise errors.EmptyValueError()
    elif not value:
        return None

    # whitespace_padding
    value = value.strip()

    cnj_caracteres = value
    cnj_caracteres = cnj_caracteres.replace("-", "")
    cnj_caracteres = cnj_caracteres.replace(".", "")

    # transforms the str into a list of characters
    cnj_caracteres = list(cnj_caracteres)
    # Verificar mínimo
    if len(cnj_caracteres) < 20:
        raise errors.MinimumValueError()

    # Verificar máximo
    if len(cnj_caracteres) > 20:
        raise errors.MaximumValueError()

    # verify datatype and regex
    if not isinstance(value, str):
        raise errors_br.DataTypeError()
    else:
        is_valid = CNJ_REGEX.search(value)

        if not is_valid:
            raise errors_br.InvalidCnjError()

    # Estabelecendo variáveis
    cnj_number = value
    NNNNNNN = cnj_number.split('-')[0]
    DD = cnj_number.split('.')[0].split('-')[1]
    AAAA = cnj_number.split('.')[1]
    J = cnj_number.split('.')[2]
    J_dict = {'1': 'STF', '2': 'CNJ', '3': 'STJ', '4': 'Justiça Federal', '5': 'Justiça do Trabalho',
              '6': 'Justiça Eleitoral', '7': 'Jutiça Militar da União', '8': 'Justiça Estadual',
              '9': 'Justiça Militar Estadual'}
    J_extenso = J_dict[J]
    TR = cnj_number.split('.')[3]
    OOOO = cnj_number.split('.')[4]

    # Inicialmente, os dígitos verificadores D1 D0 devem ser deslocados para o final do número do processo e
    # receber valor zero
    s = NNNNNNN + AAAA + J + TR + OOOO
    s_00 = s + '00'

    # Os dígitos de verificação D1 D0 serão calculados pela aplicação da seguinte fórmula, na qual “módulo” é a
    # operação “resto da divisão inteira”:
    # D1D0 = 98 – (N6N5N4N3N2N1N0A3A2A1A0J2T1R0O3O2O1O00100 módulo 97)
    digits = str(98 - (int(s_00) % 97))

    # se o resultado tiver apenas 1 digito, colocar 0 à esquerda
    if len(digits) == 1:
        digits = '0' + digits

    # Para a validação dos dígitos basta aplicar a seguinte fórmula: = (N6N5N4N3N2N1N0A3A2A1A0J2T1R0O3O2O1O00100 módulo 97). Se o resultado da fórmula for 1, os dígitos de verificação estão corretos. Isto significa que existe uma probabilidade aproximada de 99,4% de que não tenham sido cometidos erros de digitação, situação que atinge o objetivo principal do projeto.
    s_DD = s + DD
    digits_DD = str((int(s_DD) % 97))

    if digits_DD == '1':
        return True
    else:
        raise errors_br.InvalidCnjError()


def in_list(value, values_list):
    if len(values_list) == 0:
        raise errors.EmptyValueError('The list cannot be empty')
    if value not in values_list:
        raise errors_br.NotInListError('The {value} is not in the list'.format(value=value))


def cellphoneValidator(value, allow_empty=False):
    """
    Validate that 'value' is a Brazilian Cellphonenumber

    :param value: The value to validate.

    :param allow_empty:
    If ``True``, returns :obj:`None <python:None>` if ``value`` is empty.
    If ``False``, raises a :class:`EmptyValueError <validator_collection_br.errors.EmptyValueError>`
    if ``value`` is empty. Defaults to ``False``.
    :type allow_empty: :class:`bool <python:bool>`

    if value is None and allow_empty:
        return None
    elif value is None or value == "":
        raise errors.EmptyValueError('value cannot be None')
    """
    if CELLPHONE_REGEX.search(value):
        return True
    else:
        return False


def alphanumericValidator(value, allow_empty=False):
    """
    Validate that 'value' contains alphanumeric digits.

    :param value: The value to validate.

    :param allow_empty:
    If ``True``, returns :obj:`None <python:None>` if ``value`` is empty.
    If ``False``, raises a :class:`EmptyValueError <validator_collection_br.errors.EmptyValueError>`
    if ``value`` is empty. Defaults to ``False``.
    :type allow_empty: :class:`bool <python:bool>`

    if value is None and allow_empty:
        return None
    elif value is None or value == "":
        raise errors.EmptyValueError('value cannot be None')
    """
    if ALPHANUMERIC_REGEX.match(value):
        return True
    else:
        return False


def person_full_name(value, allow_empty=False):
    """
    Valida nome completo. Permite caracteres maiúsculos e minúsculos, com e sem acentuacao, "'", "-" e deve ter pelo menos um espaço entre as palavras.
    Parâmetros:
        - value (str) - Valor a ser validado.
        - allow_empty (boolean) - Se True, retorna None se o valor for vazio. Se False, retorna InvalidFullNameError.

    Retorno:
        - Value
    """

    # verify empty
    if not value and not allow_empty:
        raise errors.EmptyValueError('O nome completo não pode ser vazio.')
    elif not value:
        return None

    # whitespace_padding
    if isinstance(value, str):
        value = value.strip()
    else:
        # check datatype
        raise errors_br.DataTypeError('O nome completo deve ser uma string.')

    # verify regex
    is_valid = NOME_COMPLETO_REGEX.search(value)

    if not is_valid:
        raise errors_br.InvalidFullNameError('O nome completo informado é inválido.')

    return value
