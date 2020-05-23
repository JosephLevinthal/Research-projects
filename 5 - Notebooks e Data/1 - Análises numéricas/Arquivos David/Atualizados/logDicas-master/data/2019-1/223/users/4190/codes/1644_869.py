# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
valor= float(input("Qual o valor da compra? "))
if(valor<=200.00):
	preço = valor
else:
	preço = valor - valor*5/100
print(round(preço, 2))