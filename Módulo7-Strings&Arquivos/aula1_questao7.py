import random
def encrypt(lista_nomes):
    chave_aleatoria = random.randint(1, 10)
    def criptografar_caractere(c, chave):
        novo_codigo = ord(c) + chave
        if novo_codigo > 126:
            novo_codigo = 33 + (novo_codigo - 127)
        return chr(novo_codigo)
    def criptografar_nome(nome, chave):
        return ''.join(criptografar_caractere(c, chave) for c in nome)
    nomes_criptografados = [criptografar_nome(nome, chave_aleatoria) for nome in lista_nomes]
    return nomes_criptografados, chave_aleatoria
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave = encrypt(nomes)
print(f"Chave de criptografia: {chave}")
print(f"Nomes criptografados: {nomes_criptografados}")