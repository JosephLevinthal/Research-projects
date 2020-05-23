preco = float(input("preco sem desconto:"))
pagamento = float(input("valor a ser pago:"))
if(preco > pagamento):
	mensagem = "falta dinheiro"
	cont = (preco - pagamento)
else:
	mensagem = "troco de"
	cont = (pagamento - preco)
print(mensagem, round(cont,2))