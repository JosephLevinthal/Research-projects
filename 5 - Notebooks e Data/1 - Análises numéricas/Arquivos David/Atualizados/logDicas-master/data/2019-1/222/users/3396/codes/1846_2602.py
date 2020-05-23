
from numpy import *
from numpy.linalg import *

bacteria = array([[2, 1, 4 ], [ 1, 2, 0], [ 2, 3, 2]])

alimento = array(eval(input("digite o vetor:")))

valor = dot(inv(bacteria), alimento.T)

print("estafilococo:", round(valor[0],1))
print("salmonela:", round(valor[1],1))
print("coli:", round(valor[2],1))

if valor[0] == min(valor):
    print("estafilococo")
elif valor[1] == min(valor):
    print("salmonela")
else:
    print("coli")
