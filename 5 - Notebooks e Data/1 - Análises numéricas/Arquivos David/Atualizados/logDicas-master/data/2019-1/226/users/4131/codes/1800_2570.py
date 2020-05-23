from numpy import*
from  math import*
a = array(eval(input("coloque ai:")))
p = 1
med = sum(a)/size(a)
n = size(a)
for y in a:
	p = p*abs(y - med)
p = p**(1/n)
print(round(p,3))