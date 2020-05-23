x=input("digite o ataque:").upper()
y=int(input("digite o valor:"))
z=int(input("digite o turno: "))

if(y<1) or (y>4):
	print("Entrada invalida")
elif(x!="CAUDA") and (x!="CUSPE") and (x!="PATADA"):
	print("Entrada invalida")
elif(x=="CAUDA"):
	h=y*z
	print(h)
elif(x=="CUSPE"):
	h=2*y*z
	print(h)
elif(x=="PATADA"):
	h=2*y-(5*z)
	print(h)

	