# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
p=float(input("preco sem desconto:"))

pa=p*5
b=pa/100
pg=p-b

if(p>=200):
	print(round(pg,2))
else:
	print(round(p,2))
