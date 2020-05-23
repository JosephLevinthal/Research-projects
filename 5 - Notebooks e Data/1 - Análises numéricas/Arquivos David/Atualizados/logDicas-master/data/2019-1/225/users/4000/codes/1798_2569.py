from numpy import*
x = array(eval(input("vetor: ")))
soma = 0
d = 0
for i in range(size(x)):
	soma=soma+x[i]
media = soma/size(x)
from math import*
for i in range(size(x)):
	d = d+ (x[i] - media)**2
	k = size(x)-1
	t = sqrt(d/k)
print(round(t,3))
	