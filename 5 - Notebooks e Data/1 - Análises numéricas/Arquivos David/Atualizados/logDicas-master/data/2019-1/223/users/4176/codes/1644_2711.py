dinheiro= float(input("Grana disponivel: "))
broca= int(input("Quantidade de tickets: "))
vbroca= float(input("Valor dos tickets: "))
busao= int(input("Quantos passes?: "))
vbusao= float(input("Valor do passe: "))

if (dinheiro >= (broca*vbroca) + (busao*vbusao)):
	print("SUFICIENTE")
	
else:
	print("INSUFICIENTE")