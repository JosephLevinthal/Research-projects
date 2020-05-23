c= float(input("consumo de energia: "))
t=input("residencias(r)/industrias(i)/comercios(c): ")
print("Entradas:",c,"kWh e tipo",t)
y="Dados invalidos"
if(((t.lower()!="r")and(t.lower()!="i")and(t.lower()!="c"))or(c<0)):
	print(y)
elif(c<=500)and(t.lower()=="r"):
	a=c*0.44
	print('Valor total: R$',round(a,2))
elif(c>500)and(t.lower()=="r"):
	a=c*0.65
	print('Valor total: R$',round(a,2))
elif(c<=1000)and(t.lower()=="c"):
	a=c*0.55
	print('Valor total: R$',round(a,2))
elif(c>1000)and(t.lower()=="c"):
	a=c*0.60
	print('Valor total: R$',round(a,2))
elif(c<=5000)and(t.lower()=="i"):
	a=c*0.55
	print("Valor total: R$",round(a,2))
elif(c>5000)and(t.lower()=="i"):
	a=c*0.60
	print("Valor total: R$",round(a,2))
	
