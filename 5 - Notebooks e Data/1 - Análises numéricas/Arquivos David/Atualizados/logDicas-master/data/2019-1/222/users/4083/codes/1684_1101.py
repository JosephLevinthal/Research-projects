# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
consumo = float(input("Digite o consumo: "))
tipo = input("tipo de consumo: ").upper()

r  = consumo*(0.44)
r1 = consumo*(0.65)
c  = consumo*(0.55)
c1 = consumo*(0.60)
i  = consumo*(0.55)
i1 = consumo*(0.60)

print("Entradas:",consumo,"KWh  e tipo", tipo)

if (consumo <= 500 and tipo == "R"):
	 print("Valor total: R$",round(r, 2))
		
elif(consumo > 500 and tipo == "R"):
     print("Valor total: R$",round(r1, 2))
		
elif(consumo <= 1000 and tipo == "I"):
     print("Valor total: R$",round(i, 2))
		
elif(consumo > 1000 and tipo == "I"):
     print("Valor total: R$",round(i1, 2))
		
elif(consumo <= 5000 and tipo == "C"):
     print("Valor total: R$",round(c, 2))
		
elif(consumo > 5000 and tipo == "C"):
     print("Valor total: R$",round(c1, 2))
		
else:
	 print("Dados invalidos")