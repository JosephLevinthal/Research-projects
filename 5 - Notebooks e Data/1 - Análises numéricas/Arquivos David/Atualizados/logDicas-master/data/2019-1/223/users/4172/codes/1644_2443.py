# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
R = float(input("raio: "))
x = float(input("altura: "))
N = int(input("numero: "))

V1=4*pi*(R)**3/3
v2=(pi*x**2)*((3*R)-x)/3
be = (V1-v2)

if N==1 :
	mensagem = (v2)
else:
	mensagem = (be)
	
print(round(mensagem,4))

