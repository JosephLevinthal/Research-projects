from numpy import *
vet = array(eval(input()))
while len(vet)>1:
	n=0
	for x in vet:
		if 5<=x<7:
			n+=1
	print(n)
	vet = array(eval(input()))
