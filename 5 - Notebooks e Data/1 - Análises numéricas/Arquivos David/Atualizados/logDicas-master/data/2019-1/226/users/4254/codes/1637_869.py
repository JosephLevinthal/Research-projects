# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
valor = float(input("Digite o valor da compra: "))

if(valor >= 200.00):
	valordesc = valor - (5*valor/100)
else:
	valordesc = valor
	
print(round(valordesc,2))