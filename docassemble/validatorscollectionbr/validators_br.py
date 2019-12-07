import re
import numpy as np


def validator_cpf(value,
                  allow_empty=False,
                  ):

    # check empty
    if not value and not allow_empty:
        return "O campo está vazio"
    elif not value:
        return "O campo está vazio, mas ele não é obrigatório"

    # check datatype and regex
    if not isinstance(value, str):
        return "O valor digitado não é uma string"

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
        return "O valor tem menos de 11 dígitos"

    # Verificar máximo
    if len(cpf) > 11:
        return "O valor tem mais de 11 dígitos"

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