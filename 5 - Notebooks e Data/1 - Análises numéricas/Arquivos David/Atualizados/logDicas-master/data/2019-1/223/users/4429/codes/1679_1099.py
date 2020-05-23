# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
from math import*

a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))
print("Entradas:", a, ",", b, ",", c)
if (a > 0 and b > 0 and c > 0):
   print("Tipo de triangulo:")  
if (a + b > c and a + c > b and c + b > a):
		if (a == b and a == c):
			print("equilatero")
		elif (a == b or b == c or a == c):
			print("isosceles")
		else:
			print("escaleno")
else:
		print("invalido")

     
   

