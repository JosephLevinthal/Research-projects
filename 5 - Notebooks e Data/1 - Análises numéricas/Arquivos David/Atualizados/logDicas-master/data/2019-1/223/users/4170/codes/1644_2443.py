# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *

raio = float(input("raio:"))
x = float(input("altura:"))
op = int(input("opcao:"))

calota = pi/3 * x**2 * (3*raio - x)
if (op == 1):
	volume = calota
else:
	volume = 4/3 * pi *raio**3 - calota
print(round(volume,4))