# Leitura dos lados do triangulo a, b, and c
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))

print("Entradas: ", round(a,1), ",", round(b,1), ",", round(c,1))

# Testa se medidas correspondem aas de um triangulo
if ((a >= b + c) or (b >= a + c) or (c >= a + b) or (a < 0) or (b < 0) or (c < 0)):
	print("Tipo de triangulo: invalido")
	
else: 		
	if(a==b) and (b==c):
	  	print("Tipo de triangulo: equilatero")
	
	else:
		if(a==b) or (b==c) or (c==a):
			print("Tipo de triangulo: isosceles")
		else:
			print("Tipo de triangulo: escaleno")
