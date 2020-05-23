from numpy import *
from numpy.linalg import *

j = array(eval(input((""))))

tab = array([[2 , 1 , 4], [1 , 2 , 0], [2 , 3 , 2]])

# Vetor de constantes (informado no enunciado)
j = j.T

k = dot(inv(tab),j)

# Resolucao do sistema de equacoes lineares

# Imprime o preco de cada fruta
print("estafilococo: ", round(k[0], 1))
print("salmonela: ", round(k[1], 1))
print("coli: ", round(k[2], 1))

# Imprime nome da fruta mais cara
if k[0] == min(k):
    print("estafilococo")
elif k[1] == min(k):
    print("salmonela")
else:
    print("coli")