from math import*
x = eval(input("digite o angulo: "))
k =int(input("digite o K: "))

soma = 0
i = 0
x1 = 3
r = 3
a = -1
b = x

while (i <= k):
	b =((a*x)**x1)/factorial(r)
	x1 = x1 + 2
	r = r + 2
	a = -a
	i = i + 1
	soma = x - b	
print(round(b, 10))