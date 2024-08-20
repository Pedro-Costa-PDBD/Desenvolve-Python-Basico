import random
lista1 = []
lista2 = []
interseccao = []
for x in range(20):
    y = random.randint(0, 50)
    z = random.randint(0, 50)
    lista1.append(y)
    lista2.append(z)
print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
for y in lista1:
    if y in lista2 and y not in interseccao:
        interseccao.append(y)
print(f"Interseccao: {sorted(interseccao)}")
print("Contagem")
for x in interseccao:
    print(f"{x}: {lista1.count(x)}, {lista2.count(x)}")
