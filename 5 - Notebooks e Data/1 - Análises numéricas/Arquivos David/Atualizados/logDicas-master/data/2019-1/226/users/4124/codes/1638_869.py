# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

preco = float(input("Informe o preco: "))
if (preco >= 200):
	valor = preco - ((5/100) * preco)
else:
	valor = preco
print(round(valor,2))
