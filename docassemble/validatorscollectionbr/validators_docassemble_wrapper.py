from validators_br import *
#from docassemble.base.util import validation_error

def validate_cpf(value):
    # ao executar a entrevista o docassemble executa as validações
    # antes do usuario preencher o campo, por isso só deve fazer a
    # validação se o campo estiver preenchido
    if not value:
        return True
    
    msg = validator_cpf(value)
    if msg != True:
#        validation_error(msg)
        return False
    else:
        return True

def validate_cnpj(value):
    # ao executar a entrevista o docassemble executa as validações
    # antes do usuario preencher o campo, por isso só deve fazer a
    # validação se o campo estiver preenchido
    if not value:
        return True
    
    msg = validator_cnpj(value)
    if msg != True:
#        validation_error(msg)
        return False
    else:
        return True

def validate_cnj(value):
    # ao executar a entrevista o docassemble executa as validações
    # antes do usuario preencher o campo, por isso só deve fazer a
    # validação se o campo estiver preenchido
    if not value:
        return True
    
    msg = validator_cnj(value)
    if msg != True:
#        validation_error(msg)
        return False
    else:
        return True