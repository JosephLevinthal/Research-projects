a=float(input("valor da luz:   "))
b=input(" R, I ou C:    ")
print("Entradas: ",a," kWh e tipo ",b)
if((b=="I")or(b=="R")or(b=="C"))and(a>=0):
	if(b=="R"):
		if(a>500):
			c=a*0.65
			print("Valor total: R$ ",round(c,2))
		else:
		   c=a*0.44
		   print("Valor total: R$ ",round(c,2))
	elif(b=="C"):
		if(a>1000):
			c=a*0.60
			print("Valor total: R$ ",round(c,2))
		else:
		   c=a*0.55
		   print("Valor total: R$ ",round(c,2))
	elif(b=="I"):
	   if(a>5000):
		   c=a*0.60
		   print("Valor total: R$ ",round(c,2))
	   else:
		   c=a*0.55
		   print("Valor total: R$ ",round(c,2))
else:
	print("Dados invalidos")