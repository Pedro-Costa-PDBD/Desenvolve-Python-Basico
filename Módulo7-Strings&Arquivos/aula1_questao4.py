numeroCelular = input("Digite o número do celular: ")
if len(numeroCelular) == 8:
    numeroCelular = "9" + numeroCelular
elif len(numeroCelular) == 9:
    if numeroCelular[0] != "9":
        print("Número inválido. Um número com 9 dígitos deve começar com 9.")
        exit()
numeroFormatado = f"{numeroCelular[:5]}-{numeroCelular[5:]}"
print(f"Número formatado: {numeroFormatado}")