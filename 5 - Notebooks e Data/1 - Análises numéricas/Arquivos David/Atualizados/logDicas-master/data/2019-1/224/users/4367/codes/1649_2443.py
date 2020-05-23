# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
r=float(input("escolha o raio"))
a=float(input("escolha a altura"))
n_o= int(input("escolha 1 ou 2"))
if(n_o==1):
	v=(pi*a**2*(3*r-a))/3
	print(round(v, 4))
else:
	v=(4*pi*r**3/3)-(pi*a**2*(3*r-a)/3)
	print(round(v, 4))