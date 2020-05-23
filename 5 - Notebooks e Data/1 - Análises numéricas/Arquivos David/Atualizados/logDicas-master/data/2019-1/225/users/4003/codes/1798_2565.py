from numpy import*

vet1 = array(eval(input("media:")))
vet2 = array(eval(input("frequencia:")))
vetn = zeros(3, dtype=int)
ch = int(input("carga horaria: "))

for elemento in range(size(vet1)):
	x = ch * 75/100
	if(vet1[elemento] >= 5) and (vet2[elemento] >= x):
		vetn[0] = vetn[0] + 1
	elif(vet1[elemento] < 5):
		vetn[1] = vetn[1] + 1
	elif(vet2[elemento] < x):
		vetn[2] = vetn[2] + 1

print(vetn)
		
