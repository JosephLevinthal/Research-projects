from numpy import*
from numpy.linalg import*
vetor = array(eval(input("qual o valor? ")))
x = size(vetor)
y = 0
for i in range(x):
	if(vetor[i] % 3 == 0):
		y = y + 1
print(y)
delta = zeros(y, dtype=int)
g = 0
for j in range(x):
	if(vetor[j] % 3 == 0):
		delta[g] = j
		g = g + 1
print(delta)