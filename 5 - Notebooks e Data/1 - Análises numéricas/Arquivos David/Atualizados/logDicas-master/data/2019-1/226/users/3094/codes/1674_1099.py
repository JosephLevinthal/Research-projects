# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
from math import *

a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))
x = ("Tipo de triangulo: ")
print("Entradas:", a, ",", b, ",", c)

# Testa se pelo menos uma das entradas eh negativa 
if (a < b+c and b < a+c and c < a+b ):
	if(a == b and b ==c):
		print("Tipo de triangulo: equilatero")
	elif(a == b and b != c or b == c and b !=a):
		print("Tipo de triangulo: isosceles")
	else:
		print("Tipo de triangulo: escaleno")
else:
	print("Tipo de triangulo: invalido")
		
		