preco = float(input("reais: "))
pagamento = float(input("reais: "))
if preco > pagamento:
	mensagem = "Falta"
	print(mensagem,round(preco-pagamento,2))
else:
	mensagem = "Troco de"
	print(mensagem,round(pagamento - preco,2)) 