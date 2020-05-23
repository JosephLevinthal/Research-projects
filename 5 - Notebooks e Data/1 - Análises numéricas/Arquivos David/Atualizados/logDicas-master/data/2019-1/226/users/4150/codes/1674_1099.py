# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
# Ao testar sua solução, não se limite ao caso de exemplo.

from math import *

# Leitura dos lados do triangulo a, b, and c
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))

print("Entradas:", a, ",", b, ",", c)

# Testa se pelo menos uma das entradas eh negativa 
if (a >= b + c or b >= a + c or c >= b + a ):
   print("Tipo de triangulo: invalido")
else:
	if (a==b) and (b==c):
		print("Tipo de triangulo: equilatero")
	else:
		if (a != b) and (b!=a) and (c!=b):
			print("Tipo de triangulo: escaleno")
		else:
			print("Tipo de triangulo: isosceles")
