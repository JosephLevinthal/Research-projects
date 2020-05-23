# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("digite a coordenada de x"))
y = float(input("digite a coordenada de y"))
expressao = 2*x + y

if  (expressao == 3):
     mensagem = "ponto pertence a reta"
	
else:
  	 mensagem = "ponto nao pertence a reta"
	
print(mensagem)