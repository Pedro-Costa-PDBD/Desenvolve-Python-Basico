nome_1 = input("Digite o nome do produto 1: ")
preco_1 = input("Digite o preço unitário do produto 1: ")
quantia_1 = input("Digite a quantidade do produto 1: ")
quantia_1 = int(quantia_1)
preco_1 = float(preco_1)
total_1 = preco_1 * quantia_1

nome_2 = input("Digite o nome do produto 2: ")
preco_2 = input("Digite o preço unitário do produto 2: ")
quantia_2 = input("Digite a quantidade do produto 2: ")
quantia_2 = int(quantia_2)
preco_2 = float(preco_2)
total_2 = preco_2 * quantia_2

nome_3 = input("Digite o nome do produto 3: ")
preco_3 = input("Digite o preço unitário do produto 3: ")
quantia_3 = input("Digite a quantidade do produto 3: ")
quantia_3 = int(quantia_3)
preco_3 = float(preco_3)
total_3 = preco_3 * quantia_3

total = total_1 + total_2 + total_3
print(f"Total: R${total:,.2f}")