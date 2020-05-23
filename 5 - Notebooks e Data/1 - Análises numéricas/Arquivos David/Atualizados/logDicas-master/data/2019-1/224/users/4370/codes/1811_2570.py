from numpy import *

x = array(eval(input("digite o vetor: ")))
s = 1
m = sum(x)/size(x)
for i in x:
	s = s * abs(i-m)
p = (s)**(1/size(x))
print(round(p,3))