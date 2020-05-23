# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
X = float(input("Coordenada x: "))
Y = float(input("Coordenada y: "))
if (2 * X + Y == 3):
	msg = "ponto pertence a reta"
else:
	msg = "ponto nao pertence a reta"
print(msg)