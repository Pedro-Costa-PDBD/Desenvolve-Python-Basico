from collections import Counter
def encontrar_anagramas(frase, palavra_objetivo):
    def sao_anagramas(palavra1, palavra2):
        return Counter(palavra1) == Counter(palavra2)
    palavras = frase.lower().split()
    anagramas = [palavra for palavra in palavras if sao_anagramas(palavra, palavra_objetivo.lower())]

    return anagramas
frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")
anagramas = encontrar_anagramas(frase, palavra_objetivo)
print(f"Anagramas: {anagramas}")