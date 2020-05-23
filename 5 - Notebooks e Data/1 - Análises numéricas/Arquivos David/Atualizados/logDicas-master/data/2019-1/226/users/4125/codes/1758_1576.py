from numpy import*
#v1 eusapia
#v2 barsanulfo
vet1 = array(eval(input("qual o vetor 1? ")))
vet2 = array(eval(input("qual o vetor 2? ")))
i = 0
b = 0
e = 0
#pedra 11 , papel 22, tesoura 33
while(i<size(vet1))and(i<size(vet2)):
		if(vet1[i] == 11 )and(vet2[i]==22): 
			b = b +1
		elif(vet1[i]==11)and(vet2[i]==33):
			e = e + 1 
		elif(vet1[i]==22)and(vet2[i]==33):
			b = b + 1
		elif(vet1[i]==22)and(vet2[i]==11):
			e = e + 1
		elif(vet1[i]==33)and(vet2[i]==11):
			b = b + 1
		elif(vet1[i]==33)and(vet2[i]==22):
			e = e + 1
		i = i + 1
print(i)
if(e>b):
	print("EUSAPIA")
elif(b>e):
	print("BARSANULFO")
elif(b==e):
	print("EMPATE")