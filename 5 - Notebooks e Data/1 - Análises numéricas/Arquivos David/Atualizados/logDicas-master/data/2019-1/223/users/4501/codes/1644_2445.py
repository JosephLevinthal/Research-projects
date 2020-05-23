c=input("ESCALA: ")
T=float(input("TEMPERATURA: "))

if(c.upper() == "F"):
	C=5/9 * (T-32)
	print(round(C, 2))
if(c.upper() == "C"):
	v=(T * 9/5) + 32
	print(round(v, 2))