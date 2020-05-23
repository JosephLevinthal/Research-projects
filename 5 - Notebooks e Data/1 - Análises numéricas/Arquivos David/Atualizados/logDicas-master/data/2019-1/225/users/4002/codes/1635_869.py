# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
valortotal =  float(input("valor: "))

if (valortotal >= 200):
	valor = (valortotal - valortotal*0.05)
	print(round(valor, 2))
else:
	valor = valortotal
	print(round(valor, 2))