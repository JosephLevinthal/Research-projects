from numpy import*
from numpy.linalg import*

mat=array(eval(input("Entre com a matriz:")))

comida=array([[2,1,4],[1,2,0],[2,3,2]])
r=array(dot(inv(comida),mat.T))

print("estafilococo:",round(r[0],1))
print("salmonela:",round(r[1],1))
print("coli:",round(r[2],1))
if(r[0]<r[1]and r[0]<r[2]):
	print("estafilococo")
elif(r[1]<r[0]and r[1]<r[2]):
	print("salmonela")
elif(r[2]<r[1]and r[2]<r[0]):
	print("coli")