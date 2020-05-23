# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
a=float(input("consumo de energia:"))
b=input("tipo de instalacao:")
print("Entradas:", a,"kWh e tipo", b.upper())

if((a<0) or (b.upper()!="R") and (b.upper()!="C") and (b.upper()!="I")):
	print("Dados invalidos")
elif(b.upper()=="R"):
	if(a<=500):
		r=a*0.44
	else:
		r=a*0.65
	print("Valor total: R$",round(r,2))
elif(b.upper()=="C"):
	if(a<=1000):
		r=a*0.55
	else:
		r=a*0.60
	print("Valor total: R$",round(r,2))
elif(b.upper()=="I"):
	if(a<=5000):
		r=a*0.55
	else:
		r=a*0.60	
	print("Valor total: R$",round(r,2))
	
	
	
