# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
p = float(input("Preco sem desconto: "))

if(p>=200):
	d= p - (p*5/100)
	print(round(d,2))
else:
	print(round(p,2))