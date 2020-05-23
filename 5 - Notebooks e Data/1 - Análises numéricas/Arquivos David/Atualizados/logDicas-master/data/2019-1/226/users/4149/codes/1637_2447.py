preco=float(input("entre com o preco: "))
pago=float(input("entre com o valor: "))

if (pago<preco):
	
	falt= preco-pago
	print("Falta",round(falt,2))
	
else:
	troc= pago-preco
	print("Troco de",round(troc,2))