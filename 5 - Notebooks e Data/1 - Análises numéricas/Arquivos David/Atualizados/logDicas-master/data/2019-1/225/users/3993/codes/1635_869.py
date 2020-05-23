# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
p = float(input("preco sem desconto"))
if (p >= 200):
	v = p - (5 / 100 * p)
else:
	v = p
print(round(v, 2))
	
	 
