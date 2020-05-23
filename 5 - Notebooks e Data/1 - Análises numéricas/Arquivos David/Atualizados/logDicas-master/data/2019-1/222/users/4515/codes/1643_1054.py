# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

coordx = float( input("Informe a coordenada X: "))
coordy = float( input("Informe a coordenada y: "))

if((2*coordx + coordy)-3 == 0):
	mensagem = "ponto pertence a reta"
else:	
	mensagem = "ponto nao pertence a reta"
print(mensagem)	
