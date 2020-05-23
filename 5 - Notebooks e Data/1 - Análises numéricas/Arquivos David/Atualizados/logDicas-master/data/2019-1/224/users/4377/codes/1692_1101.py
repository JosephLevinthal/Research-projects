co=float(input("con"))
V=input("t")
V=V.upper()	
if(V=="R" and 0<co<=500):
	w=0.44
	t=co*w
	t=round(t,2)
	print("Entradas:", co, "kWh", "e tipo",V)
	print("Valor total: R$",t)

elif(V=="R"	and co>500):
	w=0.65
	t=co*w
	t=round(t,2)
	print("Entradas:", co, "kWh", "e tipo",V)
	print("Valor total: R$",t)
	
elif(V=="C"	and 0<co<=1000):	
	w=0.55
	t=co*w
	t=round(t,2)
	print("Entradas:", co, "kWh", "e tipo",V)
	print("Valor total: R$",t)
	
elif(V=="C"	and co>1000):	
	w=0.60
	t=co*w
	t=round(t,2)
	print("Entradas:", co, "kWh", "e tipo",V)
	print("Valor total: R$",t)
	
elif(V=="I" and 0<co<=5000):
	w=0.55
	t=co*w
	t=round(t,2)
	print("Entradas:", co, "kWh", "e tipo",V)
	print("Valor total:R$",t)
	
elif(V=="I"	and co>5000):
	w=0.60
	t=co*w
	t=round(t,2)
	print("Entradas:", co, "kWh", "e tipo",V)
	print("Valor total: R$",t)
	
elif(co<0):
	print("Entradas:", co, "kWh", "e tipo",V)
	print("Dados invalidos")
	
	
else:
	print("Entradas:", co, "kWh", "e tipo",V)
	print("Dados invalidos")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	