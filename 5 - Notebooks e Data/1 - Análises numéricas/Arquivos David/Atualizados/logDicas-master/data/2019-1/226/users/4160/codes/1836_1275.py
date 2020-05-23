from numpy import*
from numpy.linalg import*
n= array(eval(input("Digite uma matriz: ")))


y = shape(n)[0]
total = zeros(y,dtype=int)

for i in range(y):
	total[i] = sum(n[i,:])
print(total)




