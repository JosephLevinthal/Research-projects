# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
faixa = float(input("faixa de consumo: "))
tipo = input("Tipo de instalacao (R, I ou C): ").upper()
print("Entradas:", faixa,"KWh","e tipo", tipo )

if(tipo == "R"):
	   if(faixa < 0):
			preco = "Dados invalidos"
		print(preco)
	   elif(faixa <= 500):
			preco = faixa * 0.44
	   else:
			preco = faixa * 0.65
   elif(tipo == "I"):
	   if(faixa < 0):
			preco = "Dados invalidos"
		print(preco)
	   elif(faixa <= 1000):
			preco = faixa * 0.55
	else:
		preco = faixa * 0.60
elif(tipo == "C"):
	if(faixa < 0):
		preco = "Dados invalidos"
		print(preco)
	elif(faixa <= 5000):
		preco = faixa * 0.55
	else: 
		preco = faixa * 0.60
else:
	preco = "Dados invalidos"
	print(preco)
msg = round(preco, 2)	
print("Valor total: R$" , msg)

		