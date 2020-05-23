from numpy import*
from numpy.linalg import*

v = array(eval(input("v: ")))

lugares = array([[4,6,0], [2,7,8], [0,3,12]])

d = dot(inv(lugares), v.T)
for i in range(size(d)):
	d[i] = d[i] 
print("plateia:", round(d[0], 0))
print("camarotes inferiores:", round(d[1], 0))
print("camarotes superiores:", round(d[2], 0))

if d[0] == max(d):
	print("plateia")
elif d[1] == max(d):
	print("camarotes inferiores")
elif d[2] == max(d):
	print("camarotes superiores")							  
							  