from numpy import*
from numpy.linalg import*
vet=array(eval(input("Digite o vetor: ")))
a=array([[10,12,15],
		   [6,8,12],
		   [12,12,18]])
a=a/60
r=dot(inv(a),vet.T)

print("cadeira: ", round(r[0],0))
print("bau: ",round(r[1],0))
print("mesa: ",round(r[2],0))

if(r[0]==max(r)):
	print("cadeira")
if(r[1]==max(r)):
	print("bau")
if(r[2]==max(r)):
	print("mesa")
