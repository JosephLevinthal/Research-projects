# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("Digite um preco: "))
if (x>= 200 ):
	x1 = x - x*0.05
	print(round(x1, 2))
else:
	print(round(x,2))