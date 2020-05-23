# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
from math import * 
a = float(input("fale ai nego, a medida do lado : "))
b = float(input("fale ai nego, a medida do outro lado: "))
c = float(input("fale ai nego, a medida de outro outro lado: "))
print("Entradas:", a, ",", b, ",", c)
if (a > 0  and b > 0 and c > 0):
	
	if (a + b > c and a + c > b and c + b > a):
		if (a==b and b==c):
			x = "equilatero"
			print("Tipo de triangulo:", x)
		elif (a==b or b==c or a==c):
			x = "isosceles"
			print("Tipo de triangulo:", x)
		else:
			x = "escaleno"
			print("Tipo de triangulo:", x)
	else:
		x = "invalido"
		print("Tipo de triangulo:", x)
else:
	print("Tipo de triangulo:", x)
