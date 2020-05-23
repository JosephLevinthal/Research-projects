g = float(input("Digite quantas gramas tem no seu prato:"))
qtd_bebida = float (input("Digite a quantidade de bebida consumida:"))
qtd_sobremesa = float (input ("digite a quantidade de sobremesa consumida:"))
kg = (g/1000)
selfservice = 26.90
bebida = 3.5
sobremesa = 3
preco_final = (kg*selfservice)+(qtd_bebida*bebida)+(qtd_sobremesa*sobremesa)
print(round(preco_final,2))