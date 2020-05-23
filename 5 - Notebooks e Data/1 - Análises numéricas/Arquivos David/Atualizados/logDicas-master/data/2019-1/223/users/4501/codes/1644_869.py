# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
a=float(input("preco: "))
d=a - (a * 5/100)
if(a >= 200.00):
	print(round(d, 2))