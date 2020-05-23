from numpy import*
from numpy.linalg import*
mat = array([[4,6,0],
				[2,7,8],
				[0,3,12]])
x = array(eval(input(" digite o vetor: ")))
v = dot(inv(mat),x.T)
print("plateia: ",round(v[0],0))
print("camarotes inferiores: ",round(v[1],0))
print("camarotes superiores: ", round(v[2],0))
if max(v)== v[0]:
	print("plateia")
elif(max(v)== v[1]):
	print("camarotes inferiores")
elif (max(v)== v[2]):
	print("camarotes superiores")