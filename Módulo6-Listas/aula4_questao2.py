x = str(input("Digite uma frase: "))
vogais = []
consoante = []
for y in x:
    if y not in "aeiouAEIOU":
        consoante.append(y)
for z in x:
    if z in "aeiouAEIOU":
        vogais.append(z)           
print(sorted(vogais))
print(consoante)