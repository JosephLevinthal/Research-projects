# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preço=float(input("sem desconto:"))
desc=(preço*5/100)
sub=(preço- desc)
if(preço>=200):
	print(round(sub, 2))
else:
	print(round(preço, 2))	