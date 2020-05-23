from numpy import*
from numpy.linalg import*
mat=array([[4,6,0], 
			 [2,7,8], 
			 [0,3,12]])
vet=array(eval(input("d: ")))
res=dot(inv(mat),vet.T)
print("plateia:", res[0])
print("camarotes inferiores:", res[1])
print("camarotes superiores:", res[2])
if(res[0]==max(res)):
	print("plateia")
elif(res[1]==max(res)):
	print("camarotes inferiores")
else:
	print("camarotes superiores")