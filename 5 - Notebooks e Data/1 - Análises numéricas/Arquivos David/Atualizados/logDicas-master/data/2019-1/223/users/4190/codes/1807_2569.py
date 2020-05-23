from numpy import *

x = array(eval(input()))
m = mean(x)
d = 0

for i in range(size(x)):
	d = (((x[i]-m)**2)+d)
	e = d/(size(x)-1)
	r = e**(1/2)
print(round(r, 3))