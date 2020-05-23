from numpy import*
from numpy.linalg import*
v=array(eval(input("digite: ")))
vet=array([[10,12,9],
			  [4,4,6],
			  [2,2,2]])
vet=array(eval(input("digite: ")))
res=dot(inv(mat),vet.t)
print("laranja:",res[0])
print("manga:",res[1])
print("abacaxi",res[2])
if(res[0]==max(res)):
	print("abacax")


