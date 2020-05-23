from numpy import*
faltas = array(eval(input("digite as faltas: ")))
vet = zeros(6, dtype = float)
for i in range(size(faltas)):
	if (faltas[i]==2):
		vet[0]= vet[0] + 1
	elif(faltas[i]==3):
		vet[1]= vet[1]+ 1
	elif(faltas[i]==4):
		vet[2] = vet[2]+ 1
	elif(faltas[i]==5):
		vet[3] = vet[3] + 1
	elif(faltas[i] ==6):
		vet[4] = vet[4] + 1
	elif(faltas[i] ==7):
		vet[5] = vet[5] + 1
a = sum(vet)
vet = vet*100
for j in range(size(vet)):
	vet[j] = round((vet[j]/a),1)
print(vet)