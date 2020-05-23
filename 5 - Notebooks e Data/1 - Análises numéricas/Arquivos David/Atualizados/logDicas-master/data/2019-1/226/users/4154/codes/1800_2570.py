from numpy import *
from math import *
a = array(eval(input()))
b = 1
m = sum(a)/size(a)
for i in a:
	b *= sqrt((i-m)**2)
print(round(b**(1/size(a)),3))