from numpy import *
from math import * 
v = array(eval(input("Digite: ")))

media = sum(v)/size(v)
aux=1
for i in range(size(v)):
	aux= aux * abs(v[i]-media)
	
aux = aux**(1/size(v))
print(round(aux,3))

	

	
