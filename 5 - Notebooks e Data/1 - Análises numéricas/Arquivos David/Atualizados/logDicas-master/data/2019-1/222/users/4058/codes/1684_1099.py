# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
from math import *

# Leitura dos lados do triangulo a, b, and c
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))

print("Entradas:", a, ",", b, ",", c)

# Testa se pelo menos uma das entradas eh negativa 
if (a<0 or b<0 or c<0 or (c>(a+b)) or (b>(c+a)) or (a>(b+c))):
	print("Tipo de triangulo: invalido")
elif (a==b and b==c):
	print("Tipo de triangulo: equilatero")
elif (a==b or b==c):
	print("Tipo de triangulo: isosceles")
else:
	print("Tipo de triangulo: escaleno")
		
