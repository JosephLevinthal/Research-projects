from numpy import*
x = array(eval(input("numeros")))
soma = 0
p = 1
for i in range(size(x)):
	soma = soma + x[i]
media = soma/size(x)
from math import*
for i in range(size(x)):
	p = p*abs(x[i] - media)
	t =p**(1/size(x))
print(round(t, 3))
	
	
