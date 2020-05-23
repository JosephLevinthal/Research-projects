# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco = float(input("escreva o preco da compra: "))
if (preco >= 200.00):
	valor = (preco - (0.05 * preco))
else: 
	valor = preco
	
print(round(valor, 2))