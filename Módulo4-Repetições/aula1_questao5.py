idade = float(0)
quantidade = int(input("Quantas pessoas realizaram a pesquisa?: "))
quantidade_2 = quantidade
while quantidade > 0:
    x = int(input("Digite a(s) idade(s): "))
    idade = float(idade + x)
    quantidade -= 1
idade = idade / quantidade_2
print(f"A média das idades é de {idade} anos")
