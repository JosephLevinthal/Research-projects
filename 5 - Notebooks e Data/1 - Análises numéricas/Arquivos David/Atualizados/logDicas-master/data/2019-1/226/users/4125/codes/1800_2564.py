from numpy import*
time1 = array(eval(input("digite os gols: ")))
time2 = array(eval(input("digite os gols: ")))

vet = zeros(3, dtype=int)
for i in range(size(time1)):
	if time1[i]>time2[i]:
		vet[0] = vet[0] + 1
	elif time1[i]<time2[i]:
		vet[2] = vet[2] + 1
	elif time1[i]==time2[i]:
		vet[1] = vet[1] + 1
print(vet)