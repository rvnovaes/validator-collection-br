import re
import numpy as np

from .errors_br import *

CPF_REGEX = re.compile(
    r"/\d{3}\.?\d{3}\.?\d{3}\-?\d{2}/"
)

CNPJ_REGEX = re.compile(
    r"[0-9]{2}\.?[0-9]{3}\.[0-9]{3}\/?[0-9]{4}\-?[0-9]{2}"
)

CNJ_REGEX = re.compile(
    r"[0-9]{7}\-[0-9]{2}\.[0-9]{4}\.[0-9]{1}\.[0-9]{2}\.[0-9]{4}"
)

def validator_cpf(value,
                  allow_empty=False,
                  ):

    # check empty
    if not value and not allow_empty:
        return "Não foi fornecido um valor"
    elif not value:
        return None

    # check datatype and regex
    if not isinstance(value, str):
        return "O valor fornecido não é uma string"
    # else:
    #     is_valid = CPF_REGEX.search(value)
    #
    #     if not is_valid:
    #         return "Caracteres digitados inválidos"

    value

    # defining the two vectors of validation --> http://www.macoratti.net/alg_cpf.htm
    lista_validacao_um = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    lista_validacao_dois = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    value = value.replace("-", "")
    value = value.replace(".", "")

    # extract the verifying digits as string for later comparison
    verificadores = value[-2:]

    # transforms the str into a list of characters
    value = list(value)
    # verifying the lenght of the cpf

    # Verificar mínimo
    if len(value) < 11:
        return "O CPF deve ter no mínimo 11 dígitos"

    # Verificar máximo
    if len(value) > 11:
        return "O CPF deve ter no máximo 11 dígitos"

    # casts each character to int
    value = [int(i) for i in value]

    # calculating the first digit
    cabeca = value[:9]
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

    # returnig
    if not bool(verificadores == digito_1 + digito_2):
        return "O CPF está inválido"

    return True

def validator_cnpj(value,
                  allow_empty=False,
                  ):

    # check empty
    if not value and not allow_empty:
        return "Não foi fornecido um valor"
    elif not value:
        return None

    # check datatype and regex
    if not isinstance(value, str):
        return "O valor fornecido não é uma string"
    # else:
    #     is_valid = CPF_REGEX.search(value)
    #
    #     if not is_valid:
    #         return "Caracteres digitados inválidos"

    # defining the two vectors of validation --> http://www.macoratti.net/alg_cpf.htm
    lista_validacao_um = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    lista_validacao_dois = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    value = value.replace("-", "")
    value = value.replace(".", "")
    value = value.replace("/", "")

    # extract the verifying digits as string for later comparison
    verificadores = value[-2:]

    # transforms the str into a list of characters
    value = list(value)

    # Verificar mínimo
    if len(value) < 14:
        return "O CNPJ deve ter no mínimo 11 dígitos"

    # Verificar máximo
    if len(value) > 14:
        return "O CNPJ deve ter no máximo 11 dígitos"

      # casts each character to int
    value = [int(i) for i in value]

    # calculating the first digit
    cabeca = value[:12]
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

    # returnig
    if not bool(verificadores == digito_1 + digito_2):
        return "O CNPJ está inválido"

    return True

def validator_cnj(value,
                  allow_empty=False,
                  ):
 
    # check empty
    if not value and not allow_empty:
        return "Não foi fornecido um valor"
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
        return "O CNPJ deve ter no mínimo 20 dígitos"

    # Verificar máximo
    if len(cnj_caracteres) > 20:
        return "O CNPJ deve ter no máximo 20 dígitos"

    # check datatype and regex
    if not isinstance(value, str):
        return "O valor fornecido não é uma string"
#    else:
#        is_valid = CNJ_REGEX.search(value)
#
#        if not is_valid:
#            return "Caracteres digitados inválidos"

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
        return "O CNJ está inválido"