preço = float(input("digite o valor do bagulho, nego:")) 
pagamento = float(input("informe o valor pago, peixenho:")) 
if preço>pagamento: 
	print("Falta" , preço - pagamento) 
else:
   print("Troco de" , pagamento - preço) 
