from numpy import*
time = array(eval(input("Gols efetudados: ")))
adver =array(eval(input("Gols do adversario: ")))

vet = zeros(3, dtype=int)

for i in range(size(time)):
	if(time[i] > adver[i]):
		vet[0] = vet[0] +  1
	elif(time[i] == adver[i]):
		vet[1] = vet[1] + 1
	elif(time[i] < adver[i]):
		vet[2] = vet[2] + 1
print(vet)