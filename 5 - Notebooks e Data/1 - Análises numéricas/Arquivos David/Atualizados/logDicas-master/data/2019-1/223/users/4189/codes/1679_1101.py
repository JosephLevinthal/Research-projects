CO = float ( input (" Consumo de energy: "))
T = input("Tipo de in[C,R,I]: ").upper()

print("Entradas:",CO,"kWh","e","tipo",T)

if(CO>0):
	if ((CO<=500)and(T=="R")):
		Y=0.44
		X=(CO * Y)
		print("Valor total: R$",round(X,2))  
	elif ((T=="R") and (CO > 500)):
		A=0.65
		X= (CO * A)
		print("Valor total: R$", round(X,2))
	elif((CO<=1000)and(T=="C")):	
		P=0.55
		X= (CO * P)		
		print("Valor total: R$",round(X,2))
	elif((CO>1000)and(T=="C")):
		E=0.60
		X= (CO * E)		
		print("Valor total: R$",round(X,2))
	elif((CO==5000)and(T=="I")):
		Y=0.55
		X= (CO * Y)		
		print("Valor total: R$",round(X,2))
	elif((CO>5000)and(T=="I")):
		Y=0.60
		X= (CO * Y)		
		print("Valor total: R$",round (X,2))
else:	
	print("Dados invalidos")

