from numpy import *

vet = array(eval(input("Entrada: ")))
sub = zeros(6,dtype=float)

for i in range(size(vet)):
	bb = size(vet)
	if vet[i] == 2:
		sub[0]= sub[0] + 1 / bb * 100
	elif vet[i]== 3:
		sub[1]+= 1 / bb * 100
	elif vet[i]== 4:
		sub[2]+= 1 / bb * 100
	elif vet[i]== 5:
		sub[3]+= 1 / bb * 100
	elif vet[i]== 6:
		sub[4]+= 1 / bb * 100
	elif vet[i]== 7:
		sub[5]+= 1 / bb * 100

for i in range(size(sub)):
	sub[i] = round(sub[i], 1)
print(sub)	