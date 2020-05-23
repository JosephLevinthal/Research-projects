from numpy import *
vetor = array(eval(input("Vetor: ")))
s = 0
a = 0
while (a < size(vetor)):
	if (vetor[a] < 0):
		s = s + 1
	a = a + 1
tf = size(vetor) - s
vf = zeros(tf, dtype = int)
j = 0
a = 0
while (a < size(vetor)):
	if (vetor[a] >= 0):
		vf[j] = vetor[a] 
		j = j + 1
	a = a + 1
print(vf)