from numpy import *
from numpy.linalg import *

bac = array([[2,1,4], [1,2,0], [2,3,2]])
v = array(eval(input("Digite o vetor: ")))
v = v.T

qtd = dot(inv(bac), v.T)

print("estafilococo: ", round(qtd[0], 1))
print("salmonela: ", round(qtd[1], 1))
print("coli: ", round(qtd[2], 1))

if qtd[0] == min(qtd):
    print("estafilococo")
elif qtd[1] == min(qtd):
    print("salmonela")
else:
    print("coli")