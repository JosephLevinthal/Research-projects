from numpy import *
vet=(input("string: "))
b= ""

for i in range(len(vet)):
	if(vet[i]!="a" and vet[i]!="A"):
		b=b+vet[i]

print(b)		
