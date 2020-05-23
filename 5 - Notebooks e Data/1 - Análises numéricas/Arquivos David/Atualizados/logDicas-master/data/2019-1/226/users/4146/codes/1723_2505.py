from math import*

x = eval(input("Valor: "))
k = int(input("Termos: "))
c = 0
i = 0
z = 1
y = 0
while (c <= k - 1):
	y = (-1)**i * (x**z)/factorial(2*i + 1) + y
	c = c + 1
	i = i + 1
	z = z + 2

print(round(y, 10))	