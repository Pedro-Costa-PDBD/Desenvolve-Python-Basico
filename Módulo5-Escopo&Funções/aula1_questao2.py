import random
import math
n = int(input("Digite um número: "))
soma = 0
for x in range(n):
    soma = soma + random.randint(0,100)
print(f" A raiz quadrada da soma dos números é:", math.sqrt(soma))
