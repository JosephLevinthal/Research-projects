from numpy import *


v =  array(eval(input("compras ")))

i = 1
total=0
tam = shape(v)

for i in range(tam[0]):
	if(v[i]>80):
		v[i] = v[i] - 5
	total= float(total+v[i])

print(round(total,3))