from numpy import *

x = array(eval(input("Digite.; ")))

m = sum(x)/size(x)

aux=0

for i in range(size(x)):
	aux = aux + (x[i]-m)**2
	
d = round((aux/(size(x)-1))**(0.5),3)
print(d)
