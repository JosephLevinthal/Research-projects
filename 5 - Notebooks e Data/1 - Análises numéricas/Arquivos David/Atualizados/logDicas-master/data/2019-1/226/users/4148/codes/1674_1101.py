# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
a = float(input("consumo de energia: "))
b = input("tipo de instalacao: r, i ou c").upper()
print("Entradas: ", a, "kwh e tipo ", b)

r1 = round(a*(0.44), 2)
r2 = round(a*(0.65), 2)
c1 = round(a*(0.55), 2)
c2 = round(a*(0.60), 2)
i1 = round(a*(0.55), 2)
i2 = round(a*(0.60), 2)
s = "Valor total: "	

if(a>0):
	if(a<=500) and (b=="R"):
		print(s, "R$ ", r1)
	elif(a>500) and (b=="R"):
		print(s, "R$ ", r2)
	elif(a<=1000 and b=="C"):
		print(s, "R$ ", c1)
	elif(a>1000 and b=="C"):
		print(s, "R$ ", c2)
	elif(a<=5000) and (b=="I"):
		print(s, "R$ ", i1)
	elif(a>5000) and (b=="I"):
		print(s, "R$ ", i2)
	else:
		print("Dados invalidos")
else:
	print("Dados invalidos")