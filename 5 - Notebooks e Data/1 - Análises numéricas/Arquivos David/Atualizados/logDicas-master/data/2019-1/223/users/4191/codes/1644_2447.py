preco=float(input("Valor do preco: "))
pagamento=float(input("Valor do pagamento: "))
if (preco>pagamento):
	mensagem = "Falta" + " " + str(preco - pagamento)
else:
	mensagem = "Troco de" + " "+str(pagamento - preco)
print(mensagem)
	
