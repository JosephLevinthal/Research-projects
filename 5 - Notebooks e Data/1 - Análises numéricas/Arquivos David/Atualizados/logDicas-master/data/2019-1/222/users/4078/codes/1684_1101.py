# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
c =float(input("escreva o consumo em kwh: "))
opcao =input("qual o tipo de instalacao? (R/C/I): ")
print ("Entrada: ", c ,"kwh e tipo",opcao)
if (opcao == "R") and (c <= 500) and (c > 0):
	vr = (c * 0.44)
	print ("valor total: R$",round(vr, 2))
elif (opcao == "R") and (c > 500) and (c > 0):
		vr = (c * 0.65)
		print ("valor total: R$,",round(vr, 2))
elif (opcao == "c") and (c <= 1000) and (c > 0):
	vr = (c * 0.55)
	print ("valor total: R$",round(vr, 2))
elif (opcao == "c") and (c < 1000) and (c <0):
	vr = (c * 0.60)
	print ("valor total: R$",round(vr, 2))
elif (opcao == "I") and (c <=5000) and (c < 0):
	vr = (c * 0.55)
	print ("valor total: R$",round(vr, 2))
elif (opcao == "I") and (c < 5000) and (c > 0):
	vr = (c * 0.60)
	print ("valor total: R$", round(vr, 2))
else:
	print ("Dados invalidos")