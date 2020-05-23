preco = float(input("preco"))
pagamento = float(input("pagamento"))
x = preco - pagamento
y = pagamento - preco
if (preco > pagamento):
	mensagem = "Falta"
	print(mensagem, round(x,2))
else :
	mensagem = "Troco de "
	print(mensagem , round(y,2))




	
