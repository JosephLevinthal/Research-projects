from numpy import*
from math import*
vet = array(eval(input("vetor: ")))
vec = sum(vet)/size(vet)
i = 0
for y in vet:
	i = i + (y - vec)**2
i = sqrt(i/(size(vet) -1))
print(round(i,3))