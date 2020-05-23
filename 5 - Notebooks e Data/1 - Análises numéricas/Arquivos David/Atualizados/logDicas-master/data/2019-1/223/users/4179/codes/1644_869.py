# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
valor=float(input("Qual o valor da compra:? "))
if (valor >= 200):
	print(round(valor-valor*5/100,2))
else:
	print(round(valor,2))