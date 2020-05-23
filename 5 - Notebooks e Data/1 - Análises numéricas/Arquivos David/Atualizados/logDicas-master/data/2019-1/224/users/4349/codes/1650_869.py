# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
entrada= float(input("preco da compra sem desconto: "))
desconto= entrada * 5/100
if (entrada>=200):
	print(round(entrada - desconto, 2))
else:
   print("sem desconto")