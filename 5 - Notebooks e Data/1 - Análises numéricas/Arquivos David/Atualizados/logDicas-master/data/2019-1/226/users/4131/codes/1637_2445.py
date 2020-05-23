gg= input("se C ou F (C/F) ")
valor= float(input("temp:"))
if(gg.upper() == "C"):
	ce = (valor*9/5)+ 32
	print(round(ce, 2))
else:
	f= (5/9)*(valor - 32)
	print(round(f, 2))




