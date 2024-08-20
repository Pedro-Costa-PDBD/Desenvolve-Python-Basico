import random
w= 0 #inicio da lista total
x= 0 #contador tamanho total
y= 0 #inicio da lista precoce
z= 0 #contador tamanho precoce
lista = []
for a in range(20):
    b = random.randint(-10, 10)
    lista.append(b)
for i in range(len(lista)):
    if lista[i] < 0:
        z += 1
        if z == 1:
            y = i
    else:
        if z > x:
            x = z
            w = y
        z = 0
print(lista)
del lista[w:w+x]
print(lista)