from numpy import*                              #REFAZER - IMPORTANTE
from numpy.linalg import*
n= array(eval(input("Digite uma matriz: ")))
y = shape(n)[1]
total = zeros(y,dtype=int)

for i in range(y):
	total[i] = sum(n[:,i])
y=1
for j in total:
	if j==max(total):
		print(y)
		y = y + 1
	else:
		y = y + 1
