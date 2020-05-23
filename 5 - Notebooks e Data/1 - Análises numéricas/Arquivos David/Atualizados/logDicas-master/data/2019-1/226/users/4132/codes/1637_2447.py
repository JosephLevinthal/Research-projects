preco = float(input("Digite o preco: "))
pagamento = float(input("Digite o pagamento: "))

if (preco > pagamento):
	x = preco - pagamento
	round(x,2)
	mensagem = "Falta "  
else:
	x = pagamento - preco
	round(x,2)
	mensagem = "Troco de "
	
print(mensagem,x)