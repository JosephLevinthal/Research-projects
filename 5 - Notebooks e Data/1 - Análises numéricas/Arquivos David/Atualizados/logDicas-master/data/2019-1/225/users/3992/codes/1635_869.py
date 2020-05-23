# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
valor = float(input("valor da compra: R$"))
if( valor >= 200 ): 
	var = (valor - (valor*5)//100)
else: 
	var = valor
print(round(var, 2))
				  