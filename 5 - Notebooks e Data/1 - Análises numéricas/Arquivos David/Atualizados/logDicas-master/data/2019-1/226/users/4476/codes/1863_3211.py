from numpy import *
from numpy.linalg import *

H = array([[1,2,0.5,1.5],
			 [1.5,1,0.5,1],
			 [1,1,1,2.5],
			 [2.5,0.5,2,0.5]])

V = array(eval(input("Digite o vetor: ")))

M = dot(inv(H),V.T)

print("caminhada: ",round(M[0], 0))
print("corrida: ",round(M[1], 0))
print("bicicleta: ",round(M[2], 0))
print("natacao: ",round(M[3], 0))


if M[0] == max(M):
	print("caminhada")
elif M[1] == max(M):
	print("corrida")
elif M[2] == max(M):
	print("bicicleta")
else:
	print("natacao")

