x = input("Digite uma frase: ")
frase_mod = ''.join('*' if y in 'aeiouAEIOU' else y for y in x)
print(f"Frase alterada: {frase_mod}")