from numpy import *

x = array(eval(input("Insira: ")))

n = size(x)
m = sum(x)/size(x)
p = 1
for i in range(size(x)):
	p = p * (abs(x[i] - m))
print(round(p **(1/n), 3))