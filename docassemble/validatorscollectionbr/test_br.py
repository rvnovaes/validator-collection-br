#from validators_docassemble_wrapper import validate_cpf

# cpf = '034.469.006-7a'
#cpf = '33333333333'
# cpf = 9889

#x = validate_cpf(cpf)
#print(x)

# cnpj = '034.469.006-7a'
# validator_cnpj(cnpj)

cpf = '22222222222'
value = list(cpf)

# verificar se os dígitos são iguais:
if all(i == value[0] for i in value):
    print("O CNPJ está inválido")
else:
    print("o CPF é válido")