var1=float(input("consumo:")) 
var2=input("instalacao:")
print("Entradas:",var1,"kWh","e tipo",var2)

if((var1<0) and (var2!= "R", "I", "C")):
	print("Dados invalidos")
elif((var1 <=500) and (var2=="R")):
	print("Valor total: R$",(round(var1*0.44, 2)))
elif((var1>500) and (var2=="R")):
	print("Valor total: R$",(round(var1*0.65, 2)))
elif((var1>0) and (var1<=1000)) and ((var2=="C")):
	print("Valor total: R$",(round(var1*0.55, 2)))
elif((var1>1000)) and ((var2=="C")):
	print("Valor total: R$",(round(var1*0.60, 2)))
elif((var1>0)) and ((var1<5000)) and(var2=="I"):
	print("Valor total: R$",(round(var1*0.55, 2)))
elif((var1>5000)) and (var2=="I"):
	print("Valor total: R$",(round(var1*0.60, 2)))

	