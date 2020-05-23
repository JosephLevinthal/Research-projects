from numpy import *
vet = array(eval(input("Leituras de glicose: ")))
i = 0
o = 0
while(i < size(vet)):
	if(vet[i] > 99):
		print(i)
		o = o + 1
	i = i + 1
print(o)
	

