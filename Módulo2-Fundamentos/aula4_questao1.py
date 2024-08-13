comprimento = 10
comprimento = int(comprimento)
largura = 25
largura = int(largura)
area_m2 = comprimento * largura
preco_m2 = 2049.962
preco_m2 = float(preco_m2)  
preco_total = preco_m2 * area_m2

print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")