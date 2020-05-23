# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
v0 = float(input("velocidade inicial"))
a = float(input("angulo do vetor"))
vg = float(input("aceleracao da gravidade"))
from math import*
R = (v0)**2 * (radians(sin(2 * a)))
if abs(R):
	mensagem = "sim"
else :
	mensagem = "nao"
print(mensagem)


			  