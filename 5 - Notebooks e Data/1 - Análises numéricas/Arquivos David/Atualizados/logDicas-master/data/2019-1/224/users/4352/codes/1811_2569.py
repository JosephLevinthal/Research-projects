from numpy import*
from math import*
x = array(eval(input("digite um vetor: ")))
s = 0
m = sum(x)/size(x)
for i in x:
	s = s + (i - m)**2
	d = sqrt(s/(size(x)-1))
print(round(d, 3))