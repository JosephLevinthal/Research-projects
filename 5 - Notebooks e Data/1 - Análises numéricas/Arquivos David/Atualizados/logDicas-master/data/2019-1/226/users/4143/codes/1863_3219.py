from numpy.linalg import*
from numpy import*
a = array(eval(input("Vetor: ")))

tot = 0 
for i in range(a):
	for j in range(a):
		if (i<j):
			tot = tot + a[i,j]
		elif (j<i):
			tot = tot + a[i,j]
b = mean(tot)
print(round(b,2))
