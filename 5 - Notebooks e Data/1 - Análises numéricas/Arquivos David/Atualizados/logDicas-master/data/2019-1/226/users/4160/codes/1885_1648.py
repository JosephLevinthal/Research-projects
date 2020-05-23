from numpy import*
from numpy.linalg import*

v = array(eval(input("Vetor de frequencia: ")))
rep = 0 # contador de reprovados

for i in range(size(v)):
	if v[i] < 70:
		rep = rep + 1
print(rep)

v1 = zeros(rep,dtype=int)
a = 0  #vetor de entrada
b = 0  #vetor de saida

for a in range(size(v)):
	if v[a]<70:

		v1[b] = v[a]

print(v1)




