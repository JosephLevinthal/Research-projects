# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu
from math import*

r = float(input('raio: '))
x = float(input('altura: '))
n = float(input('numero: '))

V= ((pi)* (x**2)*(3*r-x)/3)
if(n == 1):
	volume = V
else:
	volume = (((4*pi*(r**3))/3)- V)
print(round(volume, 4))