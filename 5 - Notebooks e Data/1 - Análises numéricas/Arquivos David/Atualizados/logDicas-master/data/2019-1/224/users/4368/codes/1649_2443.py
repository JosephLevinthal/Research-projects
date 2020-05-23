# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
r = float(input("raio"))
x = float(input("altura"))
opção= int(input("1 ou 2"))
vAr = (pi*(x**2)*(3*r-x)/3)
vesf = (4*pi*(r**3)/3)
Vcombus = (vesf - vAr)
if (opção == 1):
	print( round (vAr,4))
if (opção == 2):
	print(round(Vcombus, 4))