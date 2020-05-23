from numpy import *
from numpy.linalg import *
emb = array(eval(input("Vetor: ")))
mat = ([[4,5,2], [3,2,2], [2,3,3]])
soma = dot(inv(mat), emb.T)
print("grande: ", round(soma[0], 1))
print("medio: ", round(soma[1], 1))
print("pequeno: ", round(soma[2], 1))
if soma[0] == max(soma):
	print("grande")
elif soma[1] == max(soma):
	print("medio")
elif soma[2] == max(soma):
	print("pequeno")