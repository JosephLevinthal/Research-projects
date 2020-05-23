from numpy import *
from numpy.linalg import *
alimentos=array(eval(input("dig o vetor de alimentos : ")))
tab = array([[2,1,4], 
				 [1,2,0], 
				 [2,3,2]])
resultado=dot(inv(tab),alimentos.T)
print("estafilococo: ", round(resultado[0], 1)) 
print("salmonela: ", round(resultado[1], 1))
print("coli: ", round(resultado[2], 1))

if resultado[0] == min(resultado):
    print("estafilococo")
elif resultado[1] == min(resultado):
    print("salmonela")
else:
    print("coli")