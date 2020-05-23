from numpy import *
from numpy.linalg import *
v = array(eval(input("Horas de trabalho: ")))
n = zeros(7, dtype = int)

for j in range(7):
	n[j] = sum(v[:,j])
for i in range(size(n)):
	if(n[i] == max(n)):
		print(i+1)
	