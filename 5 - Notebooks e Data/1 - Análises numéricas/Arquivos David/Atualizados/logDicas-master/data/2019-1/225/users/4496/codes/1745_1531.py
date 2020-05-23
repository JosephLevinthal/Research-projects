from math import*

x = eval(input("ang x: "))
n = int(input)

cont = 0
e = 1
d = 2
aux = 1

while(n<soma):
	e = e + (aux * (x**2)/factorial(d))
	if(aux == 1):
		aux = -1
	else:
		aux = 1

cont = cont + 1
e = e + 1
d = d + 2

print(round(n,10))