# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
a = float(input("digite o valor da compra: "))
desc = a - (a * (5/100))
if (a >= 200):
	print(round(desc,2))
else:
	print(round(a,2))