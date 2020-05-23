# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
valor_da_blusa=float(input("digite o valor: "))
desconto = valor_da_blusa*5/100
if valor_da_blusa >= 200:
	print(round(valor_da_blusa - desconto, 2))
else:
	print("sem desconto")