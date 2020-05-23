from numpy import *
from numpy.linalg import *

quantidade = array([[2,1,4],[1,2,0],[2,3,2]])

consumo = array(eval(input("X,Y,Z:")))
consumo = consumo.T

alimento = solve((quantidade),consumo)

print("estafilococo: ", round(alimento[0], 1))
print("salmonela: ", round(alimento[1], 1))
print("coli: ", round(alimento[2], 1))

if alimento[0] == min(alimento):
    print("estafilococo")
elif alimento[1] == min(alimento):
    print("salmonela")
else:
    print("coli")

