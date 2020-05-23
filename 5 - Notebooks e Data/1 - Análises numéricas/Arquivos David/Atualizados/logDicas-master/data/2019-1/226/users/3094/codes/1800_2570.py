from numpy import *
from math import *
a = array(eval(input("")))
p = 1
med = sum(a)/size(a)
n = size(a)
for l in a:
	p = p*abs(l- med)
p = p**(1/n)
print(round(p,3))