# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
v = float(input("digite o valor que foi pago: "))


if v >= 200:
	x = v*0.05
	print(round((v - x),2))
else:
	print(v)