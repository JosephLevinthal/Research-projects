# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
c = float(input("Consumo de energia: "))
t = input("Residencias(R), Industrias(I) ou Comercios(C): ").upper()

if(c<0 or  t != "R" and t != "I" and t != "C"):
	print("Entradas:", c ,"kWh e tipo", t)
	print("Dados invalidos")
elif(t=="R" and c <= 500):
	p=c*0.44
	print("Entradas:", c ,"kWh e tipo", t)
	print("Valor total: R$",round(p,2))
elif(t=="R" and c > 500):
	p=c*0.65
	print("Entradas:", c ,"kWh e tipo", t)
	print("Valor total: R$",round(p,2))
elif(t=="C" and c <= 1000):
	p=c*0.55
	print("Entradas:", c,"kWh e tipo", t)
	print("Valor total: R$",round(p,2))
elif(t=="C" and c > 1000):
	p=c*0.60
	print("Entradas:", c,"kWh e tipo", t)
	print("Valor total: R$",round(p,2))
elif(t=="I" and c <= 5000):
	p=c*0.55
	print("Entradas:", c,"kWh e tipo", t)
	print("Valor total: R$",round(p,2))
elif(t=="I" and c > 5000):
	p=c*0.60
	print("Entradas:", c,"kWh e tipo", t)
	print("Valor total: R$",round(p,2))
else:
	print("Entradas:", c ,"kWh e tipo", t)
	print("Dados invalidos")
	
