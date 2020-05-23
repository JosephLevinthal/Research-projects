esc = input("celsius ou fahrenheit? (C/N)")
vtemp = float(input("valor da temperatura:"))
if(esc.upper() == "C"):
	ce = (vtemp*9/5)+ 32
	print(round(ce, 2))
else:
	f = (5/9)*(vtemp - 32)
	print(round(f, 2))
