saldo = float(input("valor: "))
ru = int(input("quantos: "))
valru = float(input("valor: "))
pas = int(input("quantos: "))
valpas = float(input("valor: "))
if(saldo>=ru*valru+pas*valpas):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")
