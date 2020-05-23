# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
r = float(input("Digite um numero: "))
h = float(input("Digite um numero: "))
n = float(input("Digite um numero: "))

if(n==1):
	x=((pi*h**2)*(3*r-h))/3
	
if(n==2):
	x=((4*pi*r**3)/3)-((pi*h**2)*(3*r-h))/3

print(round(x, 4))