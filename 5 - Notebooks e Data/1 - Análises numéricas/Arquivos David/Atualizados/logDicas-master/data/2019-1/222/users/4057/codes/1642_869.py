# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
valor = float(input("Qual o preco da conta: "))

if valor > 200 :
	a = valor*(5/100)
	b = valor - a
	print(round(b, 2))
else: 
	print(round(valor, 2))