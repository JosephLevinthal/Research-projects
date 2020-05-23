# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

#Leitura dos valores para x e y
x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

#Determinacao do ponto no plano
z = (2 * x) + y
if (z == 3):
	print("ponto pertence a reta")
else:
	print("ponto nao pertence a reta")