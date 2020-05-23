opcao=input("em C/F?")
if(opcao=="C"):
	c=float(input("quantos graus?"))
	f=(9*c/5)+32
	print(round(f, 2))
else:
	f=float(input("quantos graus?"))
	c=(5/9)*(f-32)
	print(round(c, 2))