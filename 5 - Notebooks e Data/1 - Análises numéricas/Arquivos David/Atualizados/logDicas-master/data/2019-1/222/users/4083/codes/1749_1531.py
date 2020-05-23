from math import*

x = eval(input("angulo: "))
k = int(input("digite k: "))

c = 0 
z = 0
i = 0
b = 0
a = 1
b1 = 0
soma = 0

while	(i < k):
	b = a*(x**z/factorial(z))
	z = z + 2
	a = -a
	i = i + 1
	c = c + b

print(round(c, 10))	