from numpy import*
from numpy.linalg import*
m = array(eval(input("a matriz: ")))
x = shape(m)[0]
y = 0
maior = 0
for i in range(x):
	for j in range(x):
		if(i != j):
			if(m[i,j] > maior):
				maior = m[i,j]
print(maior)
			
			