import re
import numpy as np

CPF_REGEX = re.compile(
    r"/\d{3}\.?\d{3}\.?\d{3}\-?\d{2}/"
)

def validator_cpf(value,
                  allow_empty=False,
                  ):

    # check empty
    if not value and not allow_empty:
        return "Não foi fornecido nem um valor"
    elif not value:
        return None

    # check datatype and regex
    if not isinstance(value, str):
        return "O valor fornecido não é uma string"
    else:
        is_valid = CPF_REGEX.search(value)

        if not is_valid:
            return "Caracteres digitados inválidos"

    cpf = value

    # defining the two vectors of validation --> http://www.macoratti.net/alg_cpf.htm
    lista_validacao_um = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    lista_validacao_dois = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    cpf = cpf.replace("-", "")
    cpf = cpf.replace(".", "")

    # extract the verifying digits as string for later comparison
    verificadores = cpf[-2:]

    # transforms the str into a list of characters
    cpf = list(cpf)
    # verifying the lenght of the cpf

    # Verificar mínimo
    if len(cpf) < 11:
        return "O CPF deve ter no mínimo 11 dígitos"

    # Verificar máximo
    if len(cpf) > 11:
        return "O CPF deve ter no máximo 11 dígitos"

    # casts each character to int
    cpf = [int(i) for i in cpf]

    # calculating the first digit
    cabeca = cpf[:9]
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
        return "CPF inválido"
        raise errors_br.InvalidCpfError()

    return True