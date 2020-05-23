from numpy import*
from numpy.linalg import*
vet = array(eval(input()))
bac = array([[2,1,4],[1,2,0],[2,3,2]])
tot = dot(inv(bac),vet.T)
print("estafilococo:",round(tot[0],1))
print("salmonela:",round(tot[1],1))
print("coli:",round(tot[2],1))
if tot[0] == min(tot):
	print("estafilococo")
elif tot[1] == min(tot):
	print("salmonela")
else:
	print("coli")