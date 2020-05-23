from math import *

k = int(input('numero de termos: '))
n = k-1
i = 1
e = 0

while i<k :
	
	e += 1/factorial(i)
	i += 1
print(round(1+e,8))