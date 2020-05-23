# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

t = float(input("valor da compra: "))

if (t >= 200):
	t = t -(t / 100) * 5
	print(round(t, 2))
else:
	print(round(t, 2))