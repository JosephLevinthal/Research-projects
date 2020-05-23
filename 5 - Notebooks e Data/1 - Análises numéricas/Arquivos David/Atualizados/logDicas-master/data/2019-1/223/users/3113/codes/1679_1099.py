# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
from math import *

# Leitura dos lados do triangulo a, b, and c
a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

print("Entradas:", a, ",", b, ",", c)

if (a<b+c and b<a+c and c<a+b):
	if (a==b and b==c):
		a="equilatero"
	else:
		if(a==b or b==c):
			a="isosceles"
		else:
			a="escaleno"
else:
	a="invalido"
	
print("Tipo de triangulo:",a)