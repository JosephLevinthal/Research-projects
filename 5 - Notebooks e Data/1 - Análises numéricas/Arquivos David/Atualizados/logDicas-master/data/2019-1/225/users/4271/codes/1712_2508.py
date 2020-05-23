from math import*
n = int(input(""))
cont = 1
p = 0
x = 1
m = -1
while cont < n:
	m = m*(-1)
	p = p + (1/((x + 1)*(x + 2)*(x + 3)))*4
	x = x + 2
	cont = cont + 1
p = (round(p, 8))
pi = 3.0 + p
print(round(pi, 8))