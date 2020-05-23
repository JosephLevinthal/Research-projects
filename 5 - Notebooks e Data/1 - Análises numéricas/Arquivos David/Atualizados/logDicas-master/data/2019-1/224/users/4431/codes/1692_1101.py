x=float(input("Digite o consumo de energia em kwh:"))
y=input("Digite R para residencias, I para industria e C para comercio: ").upper()
print("Entradas:",x,"kWh e tipo",y)
if((x<0)or((y!="R")and(y!="I")and(y!="C"))):
	print("Dados invalidos")
elif(y=="R"):
	if(x<=500):
		x=x*0.44
		print("Valor total: R$",(round(x,2)))	
	else:
		x=x*0.65
		print("Valor total: R$",(round(x,2)))	
elif(y=="C"):
	if(x<=1000):
		x=x*0.55
		print("Valor total: R$",(round(x,2)))	
	else:
		x=x*0.60
		print("Valor total: R$",(round(x,2)))	
elif(y=="I"):
	if(x<=5000):
		x=x*0.55
		print("Valor total: R$",(round(x,2)))	
	else:
		x=x*0.60
		print("Valor total: R$",(round(x,2)))	
		

	
		
		
	
	
  
	
	