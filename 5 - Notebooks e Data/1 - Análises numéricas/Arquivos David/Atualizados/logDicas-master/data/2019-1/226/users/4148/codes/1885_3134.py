from numpy import*
from math import*

y = array(eval(input()))

n = size(y)

m=0


for i in range(size(y)):	
	m = m + y[i]**2
m = (m/n)**(1/2)

print(round(m, 2))