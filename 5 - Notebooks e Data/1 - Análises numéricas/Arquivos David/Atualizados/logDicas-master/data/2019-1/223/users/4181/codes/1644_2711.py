valor=float(input("valor total"))
tick=float(input("valor total"))
valortic=float(input("valor total"))
quantpass=float(input("valor total"))
valorpass=float(input("valor total"))

if(valor >= tick*valortic + quantpass*valorpass):
	msg = "SUFICIENTE"
else:
	msg = "INSUFICIENTE"
print(msg)