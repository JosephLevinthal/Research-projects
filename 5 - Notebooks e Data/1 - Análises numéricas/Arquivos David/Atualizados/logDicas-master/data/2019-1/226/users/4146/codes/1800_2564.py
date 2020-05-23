from numpy import *
gols = array(eval(input("Gols Feitos: ")))
contra = array(eval(input("Gols Contra: ")))
vet = zeros(3, dtype=int)
i = 0
for x in gols:
	if(x > contra[i]):
		vet[0] = vet[0] + 1
		i = i + 1
	elif(x == contra[i]):
		vet[1] = vet[1] + 1
		i = i + 1
	elif(x < contra[i]):
		vet[2] = vet[2] + 1
		i = i + 1
		
print(vet)		
		
		

