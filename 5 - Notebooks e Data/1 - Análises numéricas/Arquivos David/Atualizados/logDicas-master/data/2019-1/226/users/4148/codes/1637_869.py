# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
compra = float(input("valor da compra: "))
desconto = compra - (compra / 100) * 5 

if (compra >= 200):
	  print(round(desconto, 2))
	
else:
	  print(compra)
