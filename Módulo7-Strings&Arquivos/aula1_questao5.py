frase = input("Digite uma frase: ")
vogais = "aeiou"
indicesVogais = []
contadorVogais = 0
for indice, letra in enumerate(frase):
    if letra.lower() in vogais:
        indicesVogais.append(indice)
        contadorVogais += 1
print(f"Quantidade de vogais na frase: {contadorVogais}")
print(f"Índices das vogais: {indicesVogais}")