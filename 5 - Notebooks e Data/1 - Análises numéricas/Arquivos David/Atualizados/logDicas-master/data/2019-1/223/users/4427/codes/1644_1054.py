# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

#ler as coordenadas de x e y
x=float(input("entrar com o valor de x: "))
y=float(input("entrar com o valor de y: "))

#condições
if (2*x + y == 3):
	mensagem = "ponto pertence a reta"
else:
	mensagem = "ponto nao pertence a reta"
	
#impessao da mensagem
print(mensagem)
