from math import *
from numpy import *

n = array(eval(input()))

i = 0
x = 0
t = size(n)

while(i<t):
	x = x + ( log( n[i] +1)) 
	i = i + 1

m = exp(x/t)-1
print(round(m,2))