preco = float(input("Qual o valor 1 ?"))
pagamento = float(input("Qual o valor 2 ?"))

x = preco - pagamento
y = pagamento - preco
if (preco > pagamento):
	mensagem = "Falta "
	print(mensagem, round(x,2))
else:
	mensagem = "Troco de "
	print(mensagem, round (y, 2))

