from numpy import *

v = array(eval(input("insira os numeros:")))
	
m = sum(v)/size(v)
n = size(v)
d = 0	
for i in range(size(v)):
	
	d = d + ((v[i] - m)**2)/(n-1)
			 
			 
print(round(d**(1/2),3))