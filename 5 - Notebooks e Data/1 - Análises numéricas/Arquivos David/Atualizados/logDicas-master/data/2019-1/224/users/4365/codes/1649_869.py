# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
val= float(input("valor da compra:"))

desc = val - val*5/100

if (val>=200):
	print(round(desc, 2))
else:
	print(round(val, 2))