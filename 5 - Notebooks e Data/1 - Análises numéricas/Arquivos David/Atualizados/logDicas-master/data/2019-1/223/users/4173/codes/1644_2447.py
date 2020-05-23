preco = float(input())
pagamento = float(input())
if (preco > pagamento):
   mensagem = "Falta" " " + str(preco - pagamento)
else:
	mensagem = "Troco de" " " + str(pagamento - preco)
print(mensagem)
	