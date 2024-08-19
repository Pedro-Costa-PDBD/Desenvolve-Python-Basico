import random
numero = random.randint(0,10)
print("Tente adivinhar o número que pensei(1 ao 10).")
while True:
    n = int(input("Tente seu chute: "))
    if n > numero:
        print("Muito alto, tente novamente.")
    elif n < numero:
        print("Muito baixo, tente novamente.")
    elif n == numero:
        print(f"Correto, o número era: {numero}.")
        break
