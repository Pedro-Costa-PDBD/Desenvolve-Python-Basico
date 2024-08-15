ano = int(input("Insira um ano: "))
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print("Este ano é: Bissexto.")
else:
    print("Este ano é: Não Bissexto.")