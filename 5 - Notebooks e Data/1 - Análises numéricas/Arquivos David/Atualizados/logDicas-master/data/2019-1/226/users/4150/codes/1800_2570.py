from numpy import*
from math import*

v = array(eval(input("digite: ")))
p = 1
med = sum(v)/size(v)
n = size(v)

for i in v:
	p = p*abs(i - med)
p = p**(1/n)
print(round(p,3))
	
	