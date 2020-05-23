# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
X = float(input("coordenada x: "))
Y = float(input("coordenada y: "))

if(2*X + Y - 3 == 0):
	print("ponto pertence a reta")
else:
	print("ponto nao pertence a reta")