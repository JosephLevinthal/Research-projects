# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco = float(input("Digite aqui o preco da compra: "))

preco1 = preco - ((preco * 5) / 100)

if (preco >= 200.0):
	total = preco1
else:
	total = preco
	
print(round(total, 2))