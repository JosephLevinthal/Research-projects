# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

a = int(input("Coordenada X: "))
b = int(input("Coordenada Y: "))

eq = 2*a + b

if (eq == 3):
	msg = "ponto pertence a reta"
else:
	msg = "ponto nao pertence a reta"

print(msg)	