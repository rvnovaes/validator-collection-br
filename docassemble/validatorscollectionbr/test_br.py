from validators_docassemble_wrapper import validate_cpf

# cpf = '034.469.006-7a'
cpf = '034.469.111-00aaaaa'
# cpf = 9889

x = validate_cpf(cpf)
print(x)

# cnpj = '034.469.006-7a'
# validator_cnpj(cnpj)