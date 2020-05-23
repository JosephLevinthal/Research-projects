from numpy import *

vet = array(eval(input('Faltas: ')))
nv = zeros(6, dtype=int)

for i in range(size(vet)):
	if vet[i]==2:
		nv[0] = nv[0]+1
	if vet[i]==3:
		nv[1] = nv[1]+1
	if vet[i]==4:
		nv[2] = nv[2]+1
	if vet[i]==5:
		nv[3]+=1
	if vet[i]==6:
		nv[4] = nv[4]+1
	if vet[i]==7:
		nv[5] = nv[5]+1
v = zeros(6)
for i in range(size(nv)):
	v[i] = round(((nv[i]*100)/size(vet)), 1)
print(v)
	