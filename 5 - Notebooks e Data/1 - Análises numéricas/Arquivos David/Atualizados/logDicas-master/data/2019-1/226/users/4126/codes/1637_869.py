# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco= float(input("compra:"))
valor= preco*0.05

if(preco >= 200):
	print(round(preco-valor,2))
else:
	print(round(preco,2))