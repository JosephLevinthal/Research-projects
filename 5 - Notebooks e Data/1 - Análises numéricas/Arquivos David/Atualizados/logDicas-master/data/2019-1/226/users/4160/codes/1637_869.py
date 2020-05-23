# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

preco = float(input(" Digite o preco sem desconto de uma compra: "))

if (preco >= 200 ):
	valor = preco-(preco * 0.05)
else: 
	valor = preco
	
print(round(valor,2))
 