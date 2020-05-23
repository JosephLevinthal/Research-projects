from math import*
x = eval(input("Insira o angulo: "))
k = int(input("Insira o numero de termos: "))

y = 0
i = 0
c = 1

aux=1
while(i < k):
	y = y + aux *  ((x **(c))/ factorial(c))
	i = i + 1
	c = c + 2
	if(aux == 1):
		aux = -1
	else:
		aux = 1

print(round(y, 10))