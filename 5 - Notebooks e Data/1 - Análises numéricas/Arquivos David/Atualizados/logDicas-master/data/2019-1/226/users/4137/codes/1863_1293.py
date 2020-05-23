from numpy import*
from numpy.linalg import*
xyz = array(eval(input("Ingressos")))

mat = array([[4,6,0],
				 [2,7,8],
				 [0,3,12]])
a = xyz.T
b = dot(inv(mat), a)
s = b[0]
t = b[1]
v = b[2]
print("plateia:",round(s,0))
print("camarotes inferiores:", round(t,0))
print("camarotes superiores:", round(v,0))
if b[0]>b[1] and b[0] > b[2]:
	print("plateia")
elif b[1]>b[0] and b[1] > b[2]:
	print("camarotes inferiores")
elif b[2]>b[1] and b[2] > b[0]:
	print("camarotes superiores")