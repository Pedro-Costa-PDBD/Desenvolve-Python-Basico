x20_50 = []
for i in range(20, 51):
    x20_50.append(i)
pares = [x for x in x20_50 if x % 2 == 0]
print(pares)

quadrado = [1,2,3,4,5,6,7,8,9]
quadrado2 = []
for x in quadrado:
    quadrado2.append(x**2)
print(quadrado2)

x7 = []
for i in range(1, 101):
    x7.append(i)
div_7 = [y for y in x7 if y % 7 == 0]
print(div_7)

x30 = []
x30_2 = []
for i in range(0, 30, 3):
    x30.append(i)
x30_2 = ["par" if x % 2 == 0 else "impar" for x in x30]
print(x30_2)