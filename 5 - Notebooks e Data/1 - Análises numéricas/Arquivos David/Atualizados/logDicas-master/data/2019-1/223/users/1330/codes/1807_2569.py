from numpy import *
from math import *

vet = array(eval(input()))
soma = 0
d=0
for x in range(size(vet)):
	soma=soma+vet[x]
media = soma/size(vet)

for x in range(size(vet)):
	d = d + (vet[x]-media)**2
d = d / (size(vet)-1)

print(round(sqrt(d),3))