from numpy import *
from math import *

v = array(eval(input()), dtype=float)
i = 1
calculo = 0 
while(i<size(v)):
	calculo = calculo + exp(v[i])
	i = i +1
	
final = log(calculo/exp(size(v)))
print(round(final,2))