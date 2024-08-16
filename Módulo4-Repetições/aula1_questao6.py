exp = int(input("Digite a quantidade de experimentos: "))
exp_2 = exp
sapo = 0
rato = 0
coelho = 0
while exp > 0:
    cobaia = int(input("quantas cobaias foram utilizadas?: "))
    direcao = input("Qual cobaia foi utilizada?(S,R,C)?: ")
    if direcao == "S":
        sapo += cobaia
    elif direcao == "R":
        rato += cobaia
    elif direcao == "C":
        coelho += cobaia 
    exp -= 1
total = sapo + rato + coelho
percen_S = float(sapo * 100) / total
percen_R = float(rato * 100) / total
percen_C = float(coelho * 100) / total

print(f"Total: {exp_2} experimento(s)")
print(f"Total: {total} cobaias")
print(f"Total de Sapos: {sapo}")
print(f"Total de Ratos: {rato}")
print(f"Total de Coelhos: {coelho}")
print(f"Percentual de Sapos: {percen_S}%")
print(f"Percentual de Ratos: {percen_R}%")
print(f"Percentual de Coelhos: {percen_C}%")