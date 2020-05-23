# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
a = float(input("preco: "))
if (a >= 200):
	b = a*0.95
	print(round(b,2))
else:
	a = a
	print(round(a,2))