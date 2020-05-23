# Ao testar sua solução, não se limite ao caso de exemplo.

from math import *

# Leitura dos lados do triangulo a, b, and c
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))
x = "Tipo de triangulo: "
print("Entradas:", a, ",", b, ",", c)


if(a<0 or b<0 or c<0 or a+b<=c or b+c<=a or a+c<=b):
	print(x, " invalido")

else:
	if( a == b == c):
		print( x, "equilatero")
		
	else:
		if(a == b != c or c == a != b or c == b != a ):
			print( x, "isosceles")
			
		else:
			if( a != b or c != b ):
				print( x, "escaleno")
		
	
      