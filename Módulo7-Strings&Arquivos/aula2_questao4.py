import re
def validador_senha(senha):
    if len(senha) < 8:
        return False
    if not re.search(r'[A-Z]', senha):
        return False
    if not re.search(r'[a-z]', senha):
        return False
    if not re.search(r'\d', senha):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        return False
    return True
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"
print(f"Senha 1 é: {validador_senha(senha1)}")
print(f"Senha 2 é: {validador_senha(senha2)}")
print(f"Senha 3 é: {validador_senha(senha3)}")