# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
r = float(input("r: "))
h = float(input("altura: "))
n = float(input("n1 ou n2 : "))
from math import *
n1 = 4 * pi * (r**3) / 3
n2 = (pi * (h ** 2) * (3*r - h)) / 3

if(n == "1"): 
	print(round(n1, 4))
else: 
	print(round(n2, 4))
	