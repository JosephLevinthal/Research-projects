from numpy import*
from numpy.linalg import*

n= array(eval(input("horario dos funcionarios: ")))

x= shape(n)[1]
total=zeros((x),dtype=int)
for i in range(x):
	total[i]= sum(n[:,i])
x=1
for j in total:
	if j==max(total):
		print(x)
		x=x+1
	else:
		x=x+1

	