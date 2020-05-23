from numpy import*
from math import*
x = array(eval(input("numeros:")))
m = sum(x)/size(x)
d = 0
for i in range(size(x)):
	d = d + ((x[i]) - m)**2
total = sqrt(d/(size(x)- 1))
print(round(total,3))
