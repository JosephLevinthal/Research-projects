from numpy import *

vetor = array(eval(input(" ")))
reprov = 0

for i in range(size(vetor)):
	
	if vetor[i] >= 70:
		a = 1
	else:
		reprov += 1

print(reprov)
vetorrep = zeros(reprov, dtype = int)
k=0
l = -1
for i in range(size(vetor)):
	l += 1
	if vetor[i] < 70:
		
		vetorrep[k] = l
		k += 1
			
print(vetorrep)