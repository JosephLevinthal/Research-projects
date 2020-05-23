a=float(input("consumo de energia(em kWh): "))
b=input("tipos de instalacao: ")
print("Entradas:", a,"kWh","e tipo",b)
if(a>0and(b=="R" or b=="I" or b=="C")):
	
	elif(b=="R")and(a<=500):
	msg=(a*0.44)
	print("Valor total:", "R$",msg)
	elif(b=="R")and(a>500):
	msg=(a*0.65)
	print("Valor total:", "R$",msg)
	elif(b=="C")and(a<=1000):
	msg=(a*0.55)
	print("Valor total:", "R$",msg)
	elif(b=="C")and(a>1000):
	msg=(a*0.60)
	print("Valor total:", "R$",msg)
	elif(b=="I")and(a<=5000):
	msg=(a*0.55)
	print("Valor total:", "R$",msg)
	elif(b=="I")and(a>5000):
	msg=(a*0,60)
	print("Valor total:", "R$",msg)
else:
	print("Dados invalidos")
