# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

preco = float(input("Digite o preco: "))

if(preco >= 200):
	preco = preco - preco * 0.05

print(round(preco,2))