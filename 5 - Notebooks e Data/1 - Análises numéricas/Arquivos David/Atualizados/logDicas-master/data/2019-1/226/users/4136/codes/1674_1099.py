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
if (a<b+c and b<c+a and c<:
	# Testa se medidas correspondem aas de um triangulo
	if (a<b + c and b<a + c and c<a+b):
		s = (a + b + c) / 2.0
		area = sqrt(s * (s-a) * (s-b) * (s-c))
		area = round(area, 3)
		print("Area:", area)
	else:
		print("Area: invalida")
else:
	print("Area: invalida")
