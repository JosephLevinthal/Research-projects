# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

#Programa que ira ler as coordenadas

X = float(input("Digite a coordenada X: "))
Y = float(input("Digite a coordenada Y: "))

if(2 * X + Y == 3):
	mensagem = "ponto pertence a reta"
else:
	mensagem = "ponto nao pertence a reta"
	
print(mensagem)	