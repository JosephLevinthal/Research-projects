# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
valor = float(input("Digite valor: "))
if(valor >= 200):
	desconto = (valor - valor*5/100)
	print(round(desconto, 2))
else:
	print(round(valor, 2))