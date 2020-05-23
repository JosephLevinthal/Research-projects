# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
c = float(input(" Digite o consumo: "))
i = input(" R/I/C? ")
print("Entradas:",c,"kWh e tipo ",i)
if((c<0 )or ((i!="R") and (i!="C") and (i!="I"))):
		mensagem= "Dados invalidos"
		print(mensagem)
else:
	if(i=="R"):
		if(c<=500):
			mensagem = round((c*0.44),2)
		else:
			mensagem = round((c*0.65),2)
		print("Valor total: R$", mensagem)
	elif(i=="C"):
		if(c<=1000):
			mensagem= round((c*0.55),2)
		else:
			mensagem= round((c*0.60),2)
		print("Valor total: R$", mensagem)
	elif(i=="I"):
		if(c<=5000):
			mensagem= round((c*0.55),2)
		else:
			mensagem= round((c*0.60),2)
		print("Valor total: R$", mensagem)

	
	
