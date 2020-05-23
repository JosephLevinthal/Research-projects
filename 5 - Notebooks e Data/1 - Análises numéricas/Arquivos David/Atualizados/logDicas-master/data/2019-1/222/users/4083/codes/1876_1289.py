from numpy import*
from numpy.linalg import*

v = array(eval(input("Digite o vetor: ")))
a = array([[1,2,0.5,1.5],[1.5,1,0.5,1],[1,1,1,2.5],[2.5,0.5,2,0.5]])
v = v.T
b = dot(inv(a), v)
print("caminhada:", round(b[0],1))
print("corrida:", round(b[1],1))
print("bicicleta:", round(b[2],1))
print("natacao:", round(b[3],1))
g = max(b)

if(b[0] == g):
	print("caminhada")
elif(b[1] == g):
	print("corrida")
elif(b[2] == g):
	print("bicicleta")
else:
	print("natacao")