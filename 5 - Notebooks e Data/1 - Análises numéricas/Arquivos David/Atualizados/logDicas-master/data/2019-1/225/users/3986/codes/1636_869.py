# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x= float(input("preco: "))

if (x >= 200) : 
	y= x - 0.05 * x
	print(round(y, 2))

else : 
	print(round(x, 2))
