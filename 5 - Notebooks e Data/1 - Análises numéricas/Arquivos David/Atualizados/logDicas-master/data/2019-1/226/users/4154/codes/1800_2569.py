from numpy import *
from math import *
a = array(eval(input()))
b = 0
for i in a:
	b += (i - sum(a)/size(a))**2
print(round(sqrt(b/(size(a)-1)),3))
