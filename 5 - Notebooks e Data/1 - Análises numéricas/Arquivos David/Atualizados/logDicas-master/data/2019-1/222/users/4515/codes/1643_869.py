# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
valorcompra = float(input("Valor da compra :"))

if(valorcompra >= 200):
	valorpagar = (valorcompra-(valorcompra*0.05))
else:
   valorpagar = (valorcompra)
	
print(round(valorpagar,2))
	
