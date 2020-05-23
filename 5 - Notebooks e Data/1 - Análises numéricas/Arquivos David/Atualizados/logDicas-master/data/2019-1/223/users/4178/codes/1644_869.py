# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
num = float(input("Digite um preco: "))

if num >= 200:
	var1 = (5*num)/100
	print(round( num - var1, 2))
else:
	print(round(num, 2))


