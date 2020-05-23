# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
import math
from math import *

r = float(input("raio: "))
x = float(input("altura: "))
op = int(input("1 ou 2: "))

VE = (4*math.pi*r**3)/(3)
VC = ((math.pi*(x**2))*(3*r - x))/(3)


if (op == 1):
	print(round(VC,4))

if (op == 2):
	print(round(VE - VC,4))