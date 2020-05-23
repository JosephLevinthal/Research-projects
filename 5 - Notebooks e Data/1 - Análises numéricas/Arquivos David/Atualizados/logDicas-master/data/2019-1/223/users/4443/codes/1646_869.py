# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

#Leitura do valor da compra
compra = float(input("Digite o valor da compra: "))

#Calculo do desconto
if (compra >= 200.0):
	compra = compra * 0.95
	print(round (compra, 2))

else:
	print(round (compra, 2))