import validator_collection_br.validators_br as validators_br
from docassemble.base.util import validation_error


def validate_cpf(value):
    # ao executar a entrevista o docassemble executa as validações
    # antes do usuario preencher o campo,
    # por isso só deve fazer a validação se o campo estiver preenchido
    if not value:
        return True

    # passando o valor do docassemble para a função de validação
    try:
        value = validators_br.cpf(value)
    except Exception as e:
        msg = validation_error(e.value)
        validation_error(msg)

    return True

def validate_cnpj(value):
    # ao executar a entrevista o docassemble executa as validações
    # antes do usuario preencher o campo,
    # por isso só deve fazer a validação se o campo estiver preenchido
    if not value:
        return True

    # passando o valor do docassemble para a função de validação
    try:
        value = validators_br.cnpj(value)
    except Exception as e:
        msg = validation_error(e.value)
        validation_error(msg)

    return True
