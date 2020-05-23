from numpy import *

x = array(eval(input("Vetor: ")))
m = sum(x)/size(x)
n = size(x)
d = 0

for i in range(size(x)):
	d = d + ((x[i] - m)**2)/ (n - 1)
print(round(d**(1/2),3))
	

