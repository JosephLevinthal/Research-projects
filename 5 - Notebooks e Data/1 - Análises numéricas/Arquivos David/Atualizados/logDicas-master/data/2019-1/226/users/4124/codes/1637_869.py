# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco = float(input("Digite o preco: "))
if (preco >= 200):
	total = (preco - (5/100 * preco))
else:
	total = preco
print(round(total, 2))