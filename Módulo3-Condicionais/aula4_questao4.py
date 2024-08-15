distancia = int(input("Digite a distância (Em Km): "))
peso = int(input("Digite o peso (Em Kg): "))
valor = 0

if distancia <= 100 and peso > 10:
    valor = peso * 1
    valor = valor + 10
    print(f"O valor pago será de: R${valor}")
elif distancia >= 101 and distancia <= 300 and peso > 10:
    valor = peso * 1.5
    valor = valor + 10
    print(f"O valor pago será de: R${valor}")
elif distancia > 300 and peso > 10:
    valor = peso * 2
    valor = valor + 10
    print(f"O valor pago será de: R${valor}")


if distancia <= 100 and not peso > 10:
    valor = peso * 1
    print(f"O valor pago será de: R${valor}")
elif distancia >= 101 and distancia <= 300 and not peso > 10:
    valor = peso * 1.5
    print(f"O valor pago será de: R${valor}")
elif distancia > 300 and not peso > 10:
    valor = peso * 2
    print(f"O valor pago será de: R${valor}")