from numpy import *
from numpy.linalg import *
ve = array(eval(input("Digite a quantidade dos alimentos [A, B, C,]: ")))
alimento = array([[2, 1, 4], [1, 2, 0], [2, 3, 2]])
ve = ve.T

# Resolucao do sistema de equacoes lineares
bacteria = solve(alimento, ve)

# Imprime o preco de cada fruta
print("estafilococo: ", round(bacteria[0], 1))
print("salmonela: ", round(bacteria[1], 1))
print("coli: ", round(bacteria[2], 1))

# Imprime nome da fruta mais cara
if bacteria[0] == min(bacteria):
    print("estafilococo")
elif bacteria[1] == min(bacteria):
    print("salmonela")
else:
    print("coli")

