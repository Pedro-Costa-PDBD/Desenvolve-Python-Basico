def verific_palindromo(frase):
    frase_normal = ''.join(char.lower() for char in frase if char.isalnum())
    return frase_normal == frase_normal[::-1]

while True:
    x = input('Digite uma frase (digite "fim" para encerrar): ')
    if x.lower() == "fim":
        break
    if verific_palindromo(x):
        print(f'"{x}" é palíndromo')
    else:
        print(f'"{x}" não é palíndromo')