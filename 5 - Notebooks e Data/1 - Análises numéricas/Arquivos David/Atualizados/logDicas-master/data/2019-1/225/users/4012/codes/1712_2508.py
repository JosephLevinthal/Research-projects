from math import*
x = int(input(""))
cont = 1
p  = 0
n = 1
m = -1
while cont < x:
	m = m*(-1)
	p = p + (1/((n + 1)*(n + 2)*(n + 3)))*4*m
	n = n + 2
	cont = cont + 1
p = (round(p, 8))
pi = 3.0 + p
print(round(pi, 8))