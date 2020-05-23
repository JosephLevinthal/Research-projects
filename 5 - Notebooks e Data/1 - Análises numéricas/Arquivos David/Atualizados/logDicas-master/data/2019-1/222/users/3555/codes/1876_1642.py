from numpy import *
v = array(eval(input("quantidade de aluno por turma ")))
tam = shape(v)
ind = zeros(tam[0], dtype = int)

#print("quantidade de aluno por turma",v)
#print("vetor indice ",ind)
i=j=0 
d5 = 0
acm=0
#contar os divisiveis de 5
for i in range(tam[0]):
	if(v[i] % 5 == 0):
		d5 = d5 + 1

for j in range(tam[0]):
  	if(v[j]%5 == 0):
				ind[j]=j
indices = zeros(d5, dtype = int)
print( d5)
a = 0
m=0
for m in range(tam[0]-1):
	for a in range(d5):
		if(v[m] % 5 == 0):
			indices[a] = m 
			m = m+1
			
      		
				
#print(ind)		
print(indices)
