from math import *
x = eval(input('Angulo: '))
k = int(input('NTermos: '))

c = 1
s = -1
r = x
e = 3

while (c<k):
	r = r+(s*(x**e/factorial(e)))
	s = s*(-1)
	e = e+2
	c += 1
print(round(r, 10))