from numpy import *
from math import *
x = array(eval(input("digite: ")))

m = sum(x)/size(x)

a = 0

for i in range(size(x)):
	a = a + (x[i] - m)**2 
d = sqrt(a / (size(x) - 1))
print(round(d, 3))