from numpy import *
from math import *
vet=array(eval(input("...: ")))

d=0
media=sum(vet)/size(vet)
for i in range(size(vet)):
	d=d+(vet[i]-media)**2


d=(d/(size(vet)-1))**(1/2)
print(round(d, 3))	