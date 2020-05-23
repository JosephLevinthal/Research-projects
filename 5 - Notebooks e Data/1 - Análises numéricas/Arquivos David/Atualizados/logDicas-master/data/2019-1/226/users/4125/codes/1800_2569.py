from math import*
from numpy import*
x = array(eval(input("digite p x: ")))
m = sum(x)/size(x)
d= 0
for i in range(size(x)):
	d = ( d+ ((x[i]-m)**2))
t = sqrt(d/(size(x)-1))
print(round(t,3))