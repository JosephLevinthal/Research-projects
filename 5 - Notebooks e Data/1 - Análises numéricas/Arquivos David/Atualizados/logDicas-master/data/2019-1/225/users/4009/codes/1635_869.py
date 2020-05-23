# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

valor=float(input("Valor: "))
desconto = valor*0.05
valorpago = valor - desconto

if(valor>=200):
	print(round(valorpago, 2))
else:
	print(round(valor, 2))