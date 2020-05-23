# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
a = float(input("valor da compra:"))
b = a *0.05
if (a >= 200):
	valor1 = (a-b)
	print(round(valor1,2))
else:
	print(round(a,2))