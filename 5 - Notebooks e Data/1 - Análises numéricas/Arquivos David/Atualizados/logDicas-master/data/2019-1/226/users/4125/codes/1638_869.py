# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
z = float(input("digite o preco: "))
if (z>=200):
	x1 = z - z*0.05
	print(round(x1,2))
else:
	print(round(z,2))