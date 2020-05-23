from numpy import*
from numpy.linalg import*

nota = array(eval(input("Notas: ")))
ap = 0 

for i in range(size(nota)): 
	if (nota[i]>=5):
		ap = ap + 1
print(ap)
i = 0
for i in range(size(nota)):
	if nota[i]>=5:
		print(i)

j = 0 #notas
m = 0 #v1

v1 = zeros(ap,dtype=int)
for j in range(size(nota)):
	if j>= 5:
		j = j  + 1
		nota[i] = v1[i] 
		print(v1)
		print(j)
for m in range(size(v1)):
	
	
	
	
	
	