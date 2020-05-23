from math import *

a = eval(input('angulo em radianos: '))
b = int(input('numero de termos da serie: '))
i = 0
c = 0
while b != 0:
	b -= 1
	c += (-1)**i*(a**(2*i+1))/factorial(2*i+1)
	i += 1
print(round(c,10))