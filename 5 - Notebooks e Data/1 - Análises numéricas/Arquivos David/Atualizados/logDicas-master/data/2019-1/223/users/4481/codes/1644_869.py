# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
valor=float(input( "qual foi e o valor da compra" ))
if(valor < 200.00 ):
	mensagem = valor
else:
	mensagem = valor - valor/100*5
print( round( mensagem,2))