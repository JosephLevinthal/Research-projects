# Elabore um programa que leia o conj de coneficientes a, b, c, d, f
a = 1.0
b = 2.0
c = 3.0
d = 4.0
e = 5.0
f = 6.0

# valor X
x = float (((c * e) - (b * f)) / ((a * e) - (b * d)))
	print(round(x, 1))

# valor Y
y = float (((a * f) - (c * d)) / ((a * e) - (b * d)))
	print(round(y, 1))

# Condicional
if (x, y > 0):
	print("Tem solucao")
else:
	print("Nao tem solucao")
	
	
	
