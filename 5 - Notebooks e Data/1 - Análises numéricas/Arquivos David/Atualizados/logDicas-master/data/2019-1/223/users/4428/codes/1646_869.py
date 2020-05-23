# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

preco_inicial = float(input("Digite o preco: "))
porcentagem = ((preco_inicial/100)*5)


if (preco_inicial >=200):
	preco_final = preco_inicial - porcentagem
else:
	preco_final = preco_inicial
	
print (round(preco_final, 2))