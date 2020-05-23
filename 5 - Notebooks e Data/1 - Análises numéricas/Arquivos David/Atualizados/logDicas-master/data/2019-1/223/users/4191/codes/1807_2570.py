from numpy import *
from math import *
vet=array(eval(input("...")))
p=1
media=sum(vet)/size(vet)
for i in range(size(vet)):
	p=p*abs(vet[i]-media)
	
p=p**(1/size(vet))

print(round(p, 3))