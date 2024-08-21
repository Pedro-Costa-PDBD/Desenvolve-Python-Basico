data = input("Digite a data de nascimento (dd/mm/aaaa): ")
meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
dia, mes, ano = map(int, data.split('/'))
print(f"Você nasceu em {dia} de {meses[mes-1]} de {ano}.")