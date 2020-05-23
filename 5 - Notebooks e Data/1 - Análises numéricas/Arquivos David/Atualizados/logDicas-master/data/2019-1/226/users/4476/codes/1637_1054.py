# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("coordenada x: "))
y = float(input("coordenada y: "))

p = (2*x + y)

if (p == 3):
	print("ponto pertence a reta")
	
else:
	print("ponto nao pertence a reta")