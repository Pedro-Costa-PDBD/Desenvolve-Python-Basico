print("Digite números para se adicionar em uma lista (Ao menos 4)(0 para finalizar).")
lista = []
while True:
    x = int(input("Número: "))
    lista.append(x)
    if x == 0:
        break
print(lista)
print(lista[0:3])
print(lista[-2::])
print(lista[::-1])
print(lista[0::2])
print(lista[1::2])
