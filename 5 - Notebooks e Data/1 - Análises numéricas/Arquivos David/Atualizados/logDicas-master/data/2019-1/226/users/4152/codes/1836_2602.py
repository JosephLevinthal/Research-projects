from numpy import *
from numpy.linalg import *
vet = array(eval(input()))
vet = vet.T
mat = array([[2, 1, 4], [ 1, 2, 0], [ 2, 3, 2]])
soma = dot(inv(mat), vet)
print("estafilococo:", round(soma[0], 1))
print("salmonela:", round(soma[1], 1))
print("coli:", round(soma[2], 1))
if soma[0] == min(soma):
	print("estafilococo")
elif soma[1] == min(soma):
	print("salmonela")
else:
	print("coli")

