# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
kw = float(input("Consumo de energia:"))
tp = input("Tipo de instalacao:").upper()

print("Entradas:", kw,"kWh e tipo", tp)

if(kw <= 500 and kw >= 0 and tp == "R"):
	print("Valor total: R$", round(0.44*kw, 2))
elif(kw > 500 and kw >= 0 and tp == "R"):
	print("Valor total: R$",round(0.65*kw, 2))
elif(kw <= 1000 and kw >= 0 and tp == "C"):
	print("Valor total: R$",round(0.55*kw, 2))
elif(kw > 1000 and kw >= 0 and tp == "C"):
	print("Valor total: R$",round(0.60*kw, 2))
elif(kw <= 5000 and kw >= 0 and tp == "I"):
	print("Valor total: R$",round(0.55*kw, 2))
elif(kw > 5000 and kw >= 0 and tp == "I"):
	print("Valor total: R$",round(0.60*kw, 2))
elif(tp != "C" or tp != "I" or tp != "R" or kw < 0 ):
	print("Dados invalidos")