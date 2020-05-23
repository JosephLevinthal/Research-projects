preco = float(input("digite o preco: "))
pagamento = float(input("digite o pagamento: "))
diferenca = preco - pagamento
troco = pagamento - preco
if(preco > pagamento) :
	print("Falta",diferenca)
else :
	print("Troco de",troco)

	
	