from numpy import *
from math import *
n = array(eval(input('digite o vetor: ')))
s = 0
m = sum(n)/size(n)
for i in n:
	s = s + (i-m)**2
d = sqrt(s/(size(n)-1))
print(round(d,3))