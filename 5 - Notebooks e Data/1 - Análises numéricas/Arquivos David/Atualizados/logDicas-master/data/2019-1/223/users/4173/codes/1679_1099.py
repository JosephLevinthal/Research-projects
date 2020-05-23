# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))
print("Entradas:",  a,",", b,",", c)

	
if (a == b == c):
	d = "equilatero"
if  ((a == c) or ( b == c) or (c == b)):
	d = "isosceles"
if (a != c != b):
	d = "escaleno"
			

if ((a < 0 or b < 0 or c < 0) or (a+b < c) or (a+c < b) or (b+c < a)):
	  d = "invalido"

print("Tipo de triangulo:" ,d)

 




