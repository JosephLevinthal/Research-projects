from numpy import *

medias = array(eval(input()))
fre = array(eval(input()))
ch = int(input())

vet = zeros(3,dtype=int)
mcarg = ch * 0.75
for x in range (size(medias)):
	if(fre[x]<mcarg):
		vet[2] = vet[2] +1
	elif(medias[x] < 5):
		vet[1] = vet[1] +1
	elif(medias[x] >5 and fre[x]>=mcarg):
		vet[0]=vet[0] +1
print(vet)