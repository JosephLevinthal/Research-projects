# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco=float(input("digite o preco"))
desconto=preco*5/100
if (preco>=200):
	valor=preco-desconto
else:
	valor=preco
print(round(valor,2))