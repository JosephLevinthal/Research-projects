from numpy import *
from numpy.linalg import *

# Entrada das quantidades de alimentos
quantidade = array(eval(input("Digite as quantidades de alimentos: ")))

# Transpor o vetor quantidade para poder multiplicar
quantidadet = quantidade.T

matriz = array([[2, 1, 4],
					 [1, 2, 0],
					 [2, 3, 2]])

# Resolução do sitema AX = B
# Onde A = Matriz, X = Quantidade de bactérias e B = Quantidade de alimentos

X = dot(inv(matriz), quantidadet)

print("estafilococo:", round(X[0], 1))
print("salmonela:", round(X[1], 1))
print("coli:", round(X[2], 1))

# Verificando qual bactéria tem a menor população

if X[0] == min(X):
	print("estafilococo")
if X[1] == min(X):
	print("salmonela")
if X[2] == min(X):
	print("coli")