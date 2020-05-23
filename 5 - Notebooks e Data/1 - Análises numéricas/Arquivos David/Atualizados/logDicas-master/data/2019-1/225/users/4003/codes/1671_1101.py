# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

faixa = float(input("consumo em kWh: "))
tipo = input("tipo de instalacao (R, I ou C): ")
print("Entradas:", faixa, "kWh e tipo", tipo)

preco = 0.0

if (faixa < 0) :
   print("Dados invalidos")

elif(faixa <= 500) and (tipo == "R"):
		preco = faixa * 0.44
		print("Valor total: R$",round(preco,2 ))
elif(faixa > 500) and (tipo == "R"):
		preco = faixa * 0.65	
		print("Valor total: R$",round(preco,2))
		
elif(faixa <= 1000) and (tipo == "C"):
		preco = faixa * 0.55
		print("Valor total: R$",round(preco,2))
elif(faixa > 1000) and (tipo == "C"):
		preco = faixa * 0.60	
		print("Valor total: R$",round(preco,2))
		
elif(faixa <= 5000) and (tipo == "I"):
		preco = faixa * 0.55
		print("Valor total: R$",round(preco,2))
elif(faixa > 5000) and (tipo == "I"):
		preco = faixa * 0.60
		print("Valor total: R$",round(preco,2))