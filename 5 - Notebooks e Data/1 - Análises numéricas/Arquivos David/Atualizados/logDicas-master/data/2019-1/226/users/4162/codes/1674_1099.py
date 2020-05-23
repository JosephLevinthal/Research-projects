# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
from math import *
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))
print("Entradas:", a, ",", b, ",", c)
if (a<b+c)and(b<a+c)and(c<a+b):
	if (a==b)and(b==c)and(c==a):
		print('Tipo de triangulo: equilatero')
	if (a==b)or(b==c)or(a==c):
		print("Tipo de triangulo: isosceles ")
	if(a!=b)and(b!=c)and(c!=a):
		print("Tipo de triangulo: escaleno ")
else:
	print("Tipo de triangulo: invalido")