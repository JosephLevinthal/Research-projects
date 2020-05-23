from numpy import *
from numpy.linalg import *

# Matriz do sistema linear (informado no enunciado)
frutas = array([[3 , 12 , 1], [12 , 0 , 2 ], [0 , 2 , 3]])

# Vetor de constantes (informado no enunciado)
compras = array([23.6, 52.6, 27.7])
compras = compras.T

# Resolucao do sistema de equacoes lineares
preco = dot(inv(frutas) , compras )

# Imprime o preco de cada fruta
print("abacate: ", round(preco[0], 1))
print("banana: ", round(preco[1], 1))
print("caqui: ", round(preco[2], 1))

# Imprime nome da fruta mais cara
if preco[0] == max(preco):
    print("abacate")
elif preco[1] == max(preco):
    print("banana")
else:
    print("caqui")

