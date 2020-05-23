# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("valor da compra: "))

if(x>=200):
	y=(x*0.05)
	print(round(x-y, 2))
else:
	print(round(x, 2))
