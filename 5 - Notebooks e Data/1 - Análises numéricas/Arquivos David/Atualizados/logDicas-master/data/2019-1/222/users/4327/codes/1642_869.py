# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

a=float(input("valor da compra: "))

if(a >= 200):
	
	pdesc= a*0.95
	
	print(round(pdesc,2))
else:
	print(round(a,2))
