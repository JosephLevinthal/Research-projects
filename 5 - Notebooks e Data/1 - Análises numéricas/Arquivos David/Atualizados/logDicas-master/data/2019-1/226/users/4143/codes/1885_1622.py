#maximo 75
from numpy import*
a = array(eval(input("ENTRAM NOI BUSAO: ")))
b = array(eval(input("saem do busao na parada: ")))
i= size(a)
u = 0
j=0
k=0
while(i>u):
	soma= k+ (a[u] - b[j])
	u= u + 1
	j= j+1
	k=soma
print(soma)

	