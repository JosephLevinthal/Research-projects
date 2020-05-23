from numpy import*
from numpy.linalg import*
m=array(eval(input("escreva o vetor com o valor das compras: ")))
l=shape(m)[0]
c=shape(m)[1]
t=0
for i in range(l):
	t=t+(m[i,0])*(m[i,1])
print(round(t, 2))