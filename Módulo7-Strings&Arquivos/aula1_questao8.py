cpf = input("Digite o CPF na forma XXX.XXX.XXX-XX: ")
def calcular_primeiro_digito(cpf):
    multiplicador = list(range(10, 1, -1))
    soma = sum(int(digito) * multiplicador[i] for i, digito in enumerate(cpf[:9]))
    resto = soma % 11
    primeiroDigito = 0 if resto < 2 else 11 - resto
    return primeiroDigito
def calcular_segundo_digito(cpf):
    comPrimeiroDigitoCPF = cpf[:9] + str(calcular_primeiro_digito(cpf))
    multiplicador = list(range(11, 1, -1))
    soma = sum(int(digito) * multiplicador[i] for i, digito in enumerate(comPrimeiroDigitoCPF))
    resto = soma % 11
    segundoDigito = 0 if resto < 2 else 11 - resto
    return segundoDigito
def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    primeiroDigito = str(calcular_primeiro_digito(cpf))
    segundoDigito = str(calcular_segundo_digito(cpf))
    return cpf[-2:] == primeiroDigito + segundoDigito
print(f"CPF {'Válido' if validar_cpf(cpf) else 'Inválido'}")