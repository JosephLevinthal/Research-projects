compras = float(input("Qual o valor total de suas compras?"))

if(compras < 200.00):
	mensagem = compras
else:
	mensagem = compras - compras/100*5
print(round(mensagem,2))