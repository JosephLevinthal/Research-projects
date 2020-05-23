from numpy import *
from numpy.linalg import *
from math import *

vetor = array(eval(input("informe: ")))
vetor1 = vetor.T

vetor2 = dot(inv(vetor),vetor1)
i = 0

AZ = 0
CA = 0
FL = 0
PA = 0
WI = 0

if vetor[i] == "AZ":
	vetor[i] = vetor[i] + 1
	resultado = sum(vetor)
elif vetor [i] == "CA":
	vetor[i] = vetor[i] + 1
elif vetor[i] == "FL":
	vetor[i] = vetor[i] + 1
elif vetor[i] == "PA":
	vetor[i] = vetor[i] + 1
elif vetor[i] == "WI":
	vetor[i] = vetor[i] + 1

print (resultado)
print(vetor2)
