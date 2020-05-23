# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

x = float(input("Valor da Compra: "))

d = 5 / 100


if (x >= 200):
	mensagem = x - (d * x)
else:
	mensagem = x
	
print(round(mensagem, 2))