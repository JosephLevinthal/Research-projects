from math import *
x = eval(input("Digite aqui o angulo x: "))
k = int(input("Digite aqui o numero de termos da serie: "))
i = 1
s = 0
ang = 0
n = 2
while (s < k):
	ang = ang + ((x ** i) / factorial(i) * (-1) ** n)
	i = i + 2
	n = n + 1
	s = s + 1
print (round(ang, 10))