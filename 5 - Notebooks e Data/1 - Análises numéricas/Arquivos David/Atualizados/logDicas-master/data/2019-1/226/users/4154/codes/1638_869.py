# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
a = float(input("qual o valor: "))
if a < 200:
	print(a)
else:
	print(round(a-(a*5/100),2))