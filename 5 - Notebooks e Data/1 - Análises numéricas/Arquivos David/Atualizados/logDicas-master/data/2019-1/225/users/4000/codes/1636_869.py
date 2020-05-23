# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
valor = float(input("Qual o valor: "))
if (valor>=200):
	preco = valor - (5/100) * valor
else:
	preco = valor
	print(round(preco, 2))