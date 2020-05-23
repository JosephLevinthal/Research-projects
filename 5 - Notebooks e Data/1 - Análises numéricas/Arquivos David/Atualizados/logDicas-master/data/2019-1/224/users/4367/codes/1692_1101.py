# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
e= float(input("Diga o consumo de energia (em kWh): "))
i= input("diga o tipo de instalacao R, I ou C: ")
print("Entradas:", e, "kWh e tipo", i.upper())

if(i.upper()== "R") and (e>0) and (e<=500):
	x= e*0.44
	print("Valor total: R$",round(x, 2))
elif(i.upper()== "R") and (e>0) and (e>500):
	x= e*0.65
	print("Valor total: R$",round(x, 2))
elif(i.upper()== "C") and (e>0) and (e<=1000):
	x= e*0.55
	print("Valor total: R$",round(x, 2))
elif(i.upper()== "C") and (e>0) and (e>1000):
	x= e*0.60
	print("Valor total: R$",round(x, 2))
elif(i.upper()== "I") and (e>0) and (e<=5000):
	x= e*0.55
	print("Valor total: R$",round(x, 2))
elif(i.upper()== "I") and (e>0) and (e>5000):
	x= e*0.60
	print("Valor total: R$",round(x, 2))
else:
	print("Dados invalidos")