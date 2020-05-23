# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
p = float(input("Digite o preco sem desconto: "))

if (p>=200):
	x= p -(p * 0.05)
	print(round(x,2))
else:
	print(p)