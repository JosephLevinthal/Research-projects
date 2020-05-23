from numpy import*
med = array(eval(input("media dos alunos: ")))
fre = array(eval(input("frequencia do aluno: ")))
carh = int(input("cargahoraria: "))

vet = zeros(3,dtype=int)

for x in range(0,size(med)):
	if(med[x] >= 5) and (fre[x]>=(carh*0.75)):
		vet[0] = vet[0] +1
	elif(med[x] < 5)and(fre[x]>=(carh*0.75)):
		vet[1] = vet[1] +1
	else:
		vet[2] = vet[2] +1
print(vet)