# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
c=float(input("Consumo de energia: "))
t=input("Tipo de instalacao: ").upper()
print("Entradas:",c,"kWh e tipo", t)
if((t=='R')and(c<=500)):
	valor=round(c*0.44, 2)
	print("Valor total: R$ ",valor)
elif((t=='R')and(c>500)):
	valor=round(c*0.65, 2)
	print("Valor total: R$ ",valor)
elif((t=='C')and(c<=1000)):
	valor=round(c*0.55, 2)
	print("Valor total: R$ ",valor)
elif((t=='R')and(c>1000)):
	valor=round(c*0.6, 2)
	print("Valor total: R$ ",valor)
elif((t=='I')and(c<=5000)):
	valor=round(c*0.56, 2)
	print("Valor total: R$ ",valor)
elif((t=='I')and(c>5000)):
	valor=round(c*0.6, 2)
	print("Valor total: R$ ",valor)
else:
	valor='Dados invalidos'
	print(valor)
