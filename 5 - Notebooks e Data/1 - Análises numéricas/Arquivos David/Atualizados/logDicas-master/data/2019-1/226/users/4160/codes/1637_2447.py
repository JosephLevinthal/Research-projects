preco = float(input("Digite o preco: "))
pag = float(input("Digite o pagamento: "))

if (preco > pag):
   resp = preco - pag
   print("Falta" , resp)
else: 	
	resp = pag - preco
	print("Troco de", resp)
