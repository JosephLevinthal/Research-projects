esca=input("entre coma a escala da temperatura: C/F")
temp=float(input("entre com o valor da temperatura: "))

if(esca.upper()=="C"):
	
	f=(temp*(9/5))+32
	
	print(round(f,2))
	
else:
	
	c=(5/9)*(temp-32)
	
	print(round(c,2))