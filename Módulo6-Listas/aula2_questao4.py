lista1 = []
lista2 = []
inter = []
x = int(input("Digite a quantidade de elementos da lista 1:"))
print(f"Digite os {x} elementos da lista 1:")
for i in range(x):
    y = int(input("Valor: "))
    lista1.append(y)
z = int(input("Digite a quantidade de elementos da lista 2:"))
print(f"Digite os {z} elementos da lista 2:")
for i in range(z):
    w = int(input("Valor: "))
    lista2.append(w) 
for i in range(max(x, z)):
    if i < x:
        inter.append(lista1[i])
    if i < z:
        inter.append(lista2[i])

print(f'Lista intercalada: {inter}')