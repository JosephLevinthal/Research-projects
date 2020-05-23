# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
c = float(input("escreva o consumo em kWh: "))
opcao = input("Qual o tipo de instalacao? (R/C/I): ")
print ("Entradas:", c ,"kWh e tipo", opcao )
if (opcao == "R") and (c <= 500) and (c > 0):
	vr = (c * 0.44)
	print ("Valor total: R$", round(vr, 2))
elif (opcao == "R") and (c > 500) and (c > 0):
	vr = (c * 0.65)
	print ("Valor total: R$", round(vr, 2))
elif (opcao == "C") and (c <= 1000) and (c > 0):
	vr = (c * 0.55)
	print ("Valor total: R$", round(vr, 2))
elif (opcao == "C") and (c > 1000) and (c > 0):
	vr = (c * 0.60)
	print ("Valor total: R$", round(vr, 2))
elif (opcao == "I") and (c <= 5000) and (c > 0):
	vr = (c * 0.55)
	print ("Valor total: R$", round(vr, 2))
elif (opcao == "I") and (c > 5000) and (c > 0):
	vr = (c * 0.60)
	print ("Valor total: R$", round(vr, 2))
else:
	print ("Dados invalidos")

	