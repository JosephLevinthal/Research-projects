# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

#entrada do valor
valor=float(input("Qual o valor da compra?: "))

#condicao
if (valor >= 200):
	var = valor - (valor * (5/100))
else:
	var = valor
	
#impressao do valor
print(round(var, 2))