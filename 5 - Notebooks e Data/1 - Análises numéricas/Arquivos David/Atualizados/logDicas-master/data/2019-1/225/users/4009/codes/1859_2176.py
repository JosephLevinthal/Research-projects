from numpy import *
m= array(eval(input("")))
maior = m[0][1]
for i in range(len(m)):
	for j in range(len(m)):
		if(i!=j):
			if maior < m[i][j]:
				maior = m[i][j]
print(maior)