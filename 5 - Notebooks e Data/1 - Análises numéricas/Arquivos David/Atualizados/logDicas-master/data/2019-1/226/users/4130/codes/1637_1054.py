# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

num = int(input("Coordenada X: "))
num1 = int(input("Coordenada Y: "))

p = (2 * num) + num1

if (p == 3):
	mensagem = " ponto pertence a reta"
else:
	mensagem = " ponto nao pertence a reta"

print(mensagem)