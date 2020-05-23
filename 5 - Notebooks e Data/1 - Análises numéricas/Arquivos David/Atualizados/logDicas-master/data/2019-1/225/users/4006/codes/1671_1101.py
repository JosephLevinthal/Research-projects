# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
c=float(input("consumo de energia:"))
i=input("tipo de instalacoes:")
print("Entradas:", c, "kWh", "e", "tipo", i.upper())
if(c<0):
	print("Dados invalidos")
elif(c<=500)and(i=="R"):
	x=c*0.44
	print("Valor total: R$" ,round(x, 2))
elif(c>500)and(i=="R"):
	x=c*0.65
	print("Valor total: R$" ,round(x, 2))
elif(c<=1000)and(i=="C"):
	x=c*0.55
	print("Valor total: R$" ,round(x, 2))
elif(c>1000)and(i=="C"):
	x=c*0.60
	print("Valor total: R$" ,round(x, 2))
elif(c<=5000)and(i=="I"):
	x=c*0.55
	print("Valor total: R$" ,round(x, 2))
elif(c>5000)and(i=="I"):
	x=c*0.60
	print("Valor total: R$" ,round(x, 2))
