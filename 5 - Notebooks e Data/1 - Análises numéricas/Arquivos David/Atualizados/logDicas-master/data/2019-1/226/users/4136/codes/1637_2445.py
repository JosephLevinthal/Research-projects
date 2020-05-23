esc = input("celcios ou fahrenheit? (c/f)")
vtemp = float(input("valor da temperatura: "))
if (esc == "c".upper()):
	ce = (vtemp*9/5)+ 32
	print(round(ce, 2))
else:
	f = (5/9)*(vtemp - 32)
	print(round(f, 2))