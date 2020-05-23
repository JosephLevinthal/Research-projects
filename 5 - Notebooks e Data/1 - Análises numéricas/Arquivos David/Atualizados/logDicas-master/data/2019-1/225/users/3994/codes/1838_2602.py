from numpy import*
from numpy.linalg import*
vet = array(eval(input("Digite X,Y,Z: ")))
vet = vet.T
#QUANTIDADE
q = array([[2,1,4],[1,2,0],[2,3,2]])
v= dot(inv(q),vet)
print("estafilococo: ",round(v[0],1))
print("salmonela: ", round(v[1],1))
print("coli: ", round(v[2],1))

if v[0] == min(v):
	print("estafilococo")
elif v[1] == min(v):
	print("salmonela")
else:
	print("coli")