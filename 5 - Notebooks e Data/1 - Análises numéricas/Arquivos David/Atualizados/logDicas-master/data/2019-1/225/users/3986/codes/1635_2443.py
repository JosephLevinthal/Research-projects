# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
r=float(input("raio do tanque :"))
x=float(input("altura: ")) 
n=int(input("opcao 1/2 ? :"))

from math import *

vE= (4 * pi * (r  ** 3)) / 3

vC= (pi * (x ** 2) * (3 * r - x)) / 3

if(n == 1) :
	print(round(vC, 4))

else :
	print(round(vE - vC, 4))
