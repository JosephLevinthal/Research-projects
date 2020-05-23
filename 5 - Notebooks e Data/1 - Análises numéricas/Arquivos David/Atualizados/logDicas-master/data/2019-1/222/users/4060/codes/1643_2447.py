preco=float(input("preco: "))
pagamento=float(input("pagamento: "))
if(preco>pagamento):
	men="Falta" 
	cont=(preco-pagamento)
else:
	men="Troco de"
	cont=(pagamento-preco)
print(men,round(cont, 2))	