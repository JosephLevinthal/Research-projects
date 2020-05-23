from numpy import *
from math import *
p = array(eval(input("digite o vetor P: ")))
q = array(eval(input("digite o vetor Q: ")))
i = 0
s = 0
while(i<size(p)):
	s = s + (p[i]-q[i])**2
	i = i + 1
s = sqrt(s)
print(round(s,4))