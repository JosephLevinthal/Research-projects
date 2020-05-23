from numpy import *
vet1 = array(eval(input("string:")))
vet2 = array(eval(input("vetores:")))
i = 0
j = 0

while(i>size(vet2)):
	if(vet1[0] == vet2[0]):
		i = i + 1
		j = j + 1
		vet2 = vet2 + i
print(round(i, 2))	