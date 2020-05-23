from numpy import *
from numpy.linalg import *
#leitura da matriz
m = array(eval(input()))
i = 0
j = 0 
#calculei o tamanhp
l = int(shape(m)[0])
c = int(shape(m)[1])
acm=0
qtd = 0
#somei os numeros da diagonal
for i in range(l):
	for j in range(c):
		if(i>j):
			acm = acm + m[i,j]
			qtd = qtd + 
			
print(round(acm/qtd,2))
			
				
