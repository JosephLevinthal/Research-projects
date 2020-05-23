# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
kw = float(input("consumo de energia(em kWh): "))
ti = input("tipo de instalacao: ").upper()
print("Entradas: ",kw," kWh e tipo ",ti)
if(((ti=="R")or (ti=="C")or(ti=="I"))and(kw>=0)):
	if(ti=="R"):
		if(kw<=500):
			v = kw*0.44
		else:
			v = kw*0.65
		#print("Valor total: R$ ",v)	
	elif(ti=="C"):
		if(kw<=1000):
			v = kw*0.55
		else:
			v = kw*0.60
	elif(ti=="I"):
		if(kw<=5000):
			v = kw*0.55
		else:
			v = kw*0.60
					
	print("Valor total: R$ ",round(v,2))				
else:
	print("Dados invalidos" )
#print("Valor total: R$ ",v)	