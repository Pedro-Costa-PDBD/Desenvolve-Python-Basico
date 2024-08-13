Numero = int(input())
valor = Numero
notas = [100, 50, 20, 10, 5, 2, 1]
conta = 0
for i in range(len(notas)):
    conta = Numero // notas[i]
    Numero %= notas[i]
    print('{} nota(s) de R$ {},00'.format(conta, notas[i]))