esc = input("Temperatura em:")
valor = float(input("Valor da temperatura:"))
if(esc.upper()=="C"):
	F = (valor*1.8)+32
	print(round(F, 2))

if(esc.upper()=="F"):
	C = (5/9)*(valor-32)
	print(round(C, 2))