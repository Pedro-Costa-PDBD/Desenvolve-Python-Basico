import random
num_elementos = random.randint(5, 20)
elementos = []
for x in range(num_elementos):
    valores = random.randint(1, 10)
    elementos.append(valores)
print(elementos)
print(sum(elementos))
print(sum(elementos)/len(elementos))