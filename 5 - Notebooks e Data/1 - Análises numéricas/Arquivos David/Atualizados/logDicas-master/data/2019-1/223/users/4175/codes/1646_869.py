# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("valor da compra: "))

y = 0.05
z = x*y
y = x-z

if x >= 200.00:
	print(round(y,2))
else:
	print(round(x,2))