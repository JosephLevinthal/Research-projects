# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
a=float(input("preco:"))
if (a >= 200):
	s = a*5/100
	p = a - s
	k = p
else:
	k = a
print(round(k,2 ))
	