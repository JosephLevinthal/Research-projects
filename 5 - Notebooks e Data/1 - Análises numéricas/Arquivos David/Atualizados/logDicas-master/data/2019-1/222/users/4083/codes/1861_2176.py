from numpy import*
from numpy.linalg import*

v = array(eval(input("Digite a matriz: ")))

a = shape(v)[0]
h = 0
maior = 0
for i in range(a):
	for j in range(a):
		if	(i != j):
			 if(v[i,j] > maior):
					maior = v[i,j]
print(maior)