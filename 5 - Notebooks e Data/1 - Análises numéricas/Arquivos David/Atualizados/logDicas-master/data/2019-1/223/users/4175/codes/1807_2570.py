from numpy import *
from math import *

x = array(eval(input()))

p = 1
m = sum(x)/size(x)

for i in x:
	p*=abs(i-m)
	w=p**(1/size(x))
print(round(w,3))