from numpy import *

vet = array(eval(input("medias: ")))
while(size(vet) > 1):
	nm = 0
	for i in range (size(vet)):
		if (vet[i]>=5) and (vet[i] < 7):
			nm = nm + 1 
	print(nm)
	
	vet = array(eval(input("medias: ")))