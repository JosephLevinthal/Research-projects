from numpy import*
from numpy.linalg import*

vet = array(eval(input("digite: ")))

al = array([[2,1,4],[1,2,0],[2,3,2]])

vi = dot(inv(al), vet.T)

print("estafilococo: ", round(vi[0], 1))
print("salmonela: ", round(vi[1], 1))
print("coli: ", round(vi[2], 1))

if vi[0] == min(vi):
	print("estafilococo")
elif vi[1]==min(vi):
	print("salmonela")
else:
	print("coli")