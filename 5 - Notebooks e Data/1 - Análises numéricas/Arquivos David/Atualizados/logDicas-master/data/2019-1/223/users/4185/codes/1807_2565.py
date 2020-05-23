from numpy import*
vet1= array(eval(input("digite a media: ")))
vet2= array(eval(input("digite a frequencia: ")))
carg= int(input("digite a carg: "))
v3= zeros(3, dtype=int)

for i in range(size(vet1)):
	if (vet1[i] >= 5 and vet2[i] > ((carg)* 75/100)):
		v3[0]+= 1
	elif (vet1[i] < 5 and vet2[i] > ((carg)* 75/100)):
		v3[1]+= 1
	elif (vet2[i] < ((carg)* 75/100)):
		v3[2]+= 1
		
print(v3)
		 