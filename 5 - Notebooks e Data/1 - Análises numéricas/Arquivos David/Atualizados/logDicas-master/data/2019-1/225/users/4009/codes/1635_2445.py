esc=input("escala de temperatura: ")

if(esc.upper=="C"):
	temp=float(input("temperatura: "))
	c=(5*(temp-32))/9
	print(round(c,2))
else:
	temp=float(input("temperatura: "))
	c=((9*temp)/(5)) + 32
	print(round(c,2))