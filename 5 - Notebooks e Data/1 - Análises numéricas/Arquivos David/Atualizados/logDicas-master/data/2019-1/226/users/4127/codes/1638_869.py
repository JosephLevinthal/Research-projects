# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x= float(input("qual o preco sem desconto?"))

if (x>200):
	print(round( x-(x*5/100),2))
else: 
	print(round(x,2))
	