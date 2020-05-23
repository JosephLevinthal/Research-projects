from numpy import*
from numpy.linalg import*

# Matriz do sistema linear (informado no enunciado)
frutas = array([[2,1,4], [1,2,0], [2,3,2]])

# Vetor de constantes (informado no enunciado)
compras = array(eval(input("mg :")))
compras = compras.T

# Resolucao do sistema de equacoes lineares
preco = dot(inv(frutas),compras.T)

# Imprime o preco de cada fruta
print("estafilococo: ", round(preco[0], 1))
print("salmonela: ", round(preco[1], 1))
print("coli: ", round(preco[2], 1))

# Imprime nome da fruta mais cara
if preco[0] == min(preco):
    print("estafilococo")
elif preco[1] == min(preco):
    print("salmonela")
else:
    print("coli")
