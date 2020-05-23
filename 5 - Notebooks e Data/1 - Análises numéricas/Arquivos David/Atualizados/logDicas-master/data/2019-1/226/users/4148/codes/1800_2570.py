from numpy import*
from math import*

j = array(eval(input('')))
p=1

m=sum(j)/size(j)

n = size(j)

for i in j:
	p = p*abs(i-m)
p = p**(1/n)
print(round(p, 3))