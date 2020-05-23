from math import*

x  = eval(input("valor de pi:"))
n  = int(input("numero de termos:"))
i = 0
z = 0
c = 1
f = 2
while(i < n):
	d = factorial(f)
	z = (x**c)/(d)*(-1**c) + z
	i = i + 1
	f = f + 2
	c = c + 1
	cos = 1 + z
print(round(cos,6))


