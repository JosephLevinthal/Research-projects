# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
n=float(input("digite o valor: "))
if ( n>=200):
	n= n - n*(5/100)
	print(round(n, 2))
else:
	print(round(n, 2))