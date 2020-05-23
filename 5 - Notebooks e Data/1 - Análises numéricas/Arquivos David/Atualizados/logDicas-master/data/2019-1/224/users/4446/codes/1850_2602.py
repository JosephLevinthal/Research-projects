from numpy import *
from numpy.linalg import *
vet=array(eval(input("digite o vetor: ")))

mat= array([[2,1,4],[1,2,0],[2,3,2]])

bac=dot(inv(mat),vet.T)

print("estafilococo: ", round(bac[0],1))
print("salmonela: ", round(bac[1],1))
print("coli: ", round(bac[2],1))
if (bac[0]==min(bac)):
	print("estafilococo")
elif (bac[1]==min(bac)):
	print("salmonela")
else:
	print("coli")

