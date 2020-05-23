a=input("unidade de medida: ")
t=float(input("temp: "))
if (a.upper()=="C"):
	c=(t*9/5) + 32
	print(round(c,2))
if (a.upper()=="F"):
	f=(5/9)*(t - 32)
	print(round(f,2))
	
