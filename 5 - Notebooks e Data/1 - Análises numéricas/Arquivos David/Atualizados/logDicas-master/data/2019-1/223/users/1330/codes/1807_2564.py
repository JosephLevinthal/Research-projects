from numpy import *

gols = array(eval(input()))
golsAdv = array(eval(input()))
vet = zeros(3, dtype=int)
e = 0
v = 0
d = 0
for x in range(size (gols)):
	if(gols[x] == golsAdv[x]):
		e = e + 1
		vet[1] = e
	elif(gols[x] > golsAdv[x]):
		v = v + 1
		vet[0] = v
	else:
		d = d + 1
		vet[2] = d
print(vet)