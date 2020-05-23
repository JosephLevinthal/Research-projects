# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
v0 = float(input())
a  = float(input())
D  = float(input())
R  = v0**2*sin(radians(2*a))/9.8
if D-0.1<R<D+0.1:
	print("sim")
else:
	print("nao")
