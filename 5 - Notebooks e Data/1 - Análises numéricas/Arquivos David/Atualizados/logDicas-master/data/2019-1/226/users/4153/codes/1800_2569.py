from numpy import *

x =  array(eval(input("Insira um vetor: ")))
m = sum(x)/size(x)
n = size(x)
d = 0
for i in range(size(x)):
	d = d + (x[i] - m)**2
print(round((d/(n-1))**(1/2),3))
