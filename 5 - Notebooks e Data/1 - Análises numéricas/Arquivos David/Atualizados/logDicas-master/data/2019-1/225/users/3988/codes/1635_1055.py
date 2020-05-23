# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
v0 = float(input("v0:"))
a = radians(float(input("angulo:")))
D = float(input("d:"))
R = ((v0**2) * (sin(2*a)))/ 9.8
F = abs(R-D)
if (F<=0.1):
	T = "sim"
else:
	T = "nao"
print(T)