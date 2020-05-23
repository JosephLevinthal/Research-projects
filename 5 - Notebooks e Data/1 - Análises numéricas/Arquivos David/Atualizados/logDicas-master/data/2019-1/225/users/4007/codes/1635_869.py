# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código
valor = float(input("digite o valor: "))
vap = valor - (valor * 5/100)
if (valor >= 200.00):
	print(round(vap, 2))
	
else: 
	print(round(valor, 2))
	
   