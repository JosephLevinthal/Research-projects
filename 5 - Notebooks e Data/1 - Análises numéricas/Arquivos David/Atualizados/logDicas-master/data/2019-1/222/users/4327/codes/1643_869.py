# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
p=float(input("valor da compra: "))
if(p>=200):
	print( round ((p - (p*0.05)),2) )
else:
	print(round (p,2))
	