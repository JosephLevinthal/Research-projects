# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
v0= float(input("valocidade inicial: "))
ang= float(input("angulo alpha :"))
dist= float(input("distancia horizontal :"))
g= 9.8

from math import *

R= (v0 ** 2) * sin (2 ** radians(ang)) / g

if abs(dist- R) <= 1 :
	print("sim")
	
else :
	print("nao")