import random
def embaralhar_palavras(frase):
    def embaralhar_palavra(palavra):
        if len(palavra) <= 3:
            return palavra
        meio = list(palavra[1:-1])
        random.shuffle(meio)
        return palavra[0] + ''.join(meio) + palavra[-1]
    palavras = frase.split()
    palavras_embaralhadas = [embaralhar_palavra(x) for x in palavras]
    return ' '.join(palavras_embaralhadas)
frase = input("Digite a frase: ")
resultado = embaralhar_palavras(frase)
print(resultado)