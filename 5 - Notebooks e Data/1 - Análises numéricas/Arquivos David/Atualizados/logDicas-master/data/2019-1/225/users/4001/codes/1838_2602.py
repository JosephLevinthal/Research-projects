from numpy import*
from numpy.linalg import *
vet = array(eval(input("Matriz: ")))
v = vet.T
#alimentos
a = array([[2, 1, 4], [1, 2, 0], [2, 3, 2]])
qtd = dot(inv(a), v)
#nomes e quantidades
print("estafilococo: ", round(qtd[0], 1))
print("salmonela: ", round(qtd[1], 1))
print("coli: ", round(qtd[2], 1))
#menor populacao
if (qtd[0] == min(qtd)):
	print("estafilococo")
elif (qtd[1] == min(qtd)):
	print("salmonela")
else:
	print("coli")