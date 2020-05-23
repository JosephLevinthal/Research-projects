t = input("F ou C: ")
vt = float(input("valor da temperatura: "))
c = (5*vt - 5*32) / 9
f = (((9*vt)/5) + 32)
if(t == "C" ):
	print(round(f, 2))
else:
	print(round(c, 2))