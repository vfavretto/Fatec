def valida_cpf(cpf):
    global resto
    cpf_numeros = ''.join(filter(str.isdigit, cpf))

    if len(cpf_numeros) != 11:
        return False

    if cpf_numeros == cpf_numeros[0] * 11:
        return False

    soma = 0
    for i in range(9):
        soma += int(cpf_numeros[i]) * (10 - i)
        resto = soma % 11

    if resto < 2:
        digito_verificador1 = 0
    else:
        digito_verificador1 = 11 - resto
    if digito_verificador1 != int(cpf_numeros[9]):
        return False

    soma = 0
    for i in range(10):
        soma += int(cpf_numeros[i]) * (11 - i)
        resto = soma % 11
    if resto < 2:
        digito_verificador2 = 0
    else:
        digito_verificador2 = 11 - resto

    if digito_verificador2 != int(cpf_numeros[10]):
        return False

    return True


#cpf = input("Digite o CPF (apenas números): ")
#if valida_cpf(cpf):
#    print("CPF válido! :D")
#else:
#    print("CPF inválido. :(")
