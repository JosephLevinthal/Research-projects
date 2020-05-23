# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

x = float(input(" Digite a coordenada x do ponto P(x,y): "))
y = float(input(" Digite a coordenada y do ponto P(x,y): "))

if (2* x + y == 3):
	resposta = " ponto pertence a reta"
	
else: 
	resposta = "ponto nao pertence a reta"
	
print (resposta)
