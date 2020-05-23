from numpy import*
vet= array(eval(input("digite os valores: ")))
while (size(vet) > 1):
	q = 0
	for i in range(size(vet)):
		if (5 <= vet[i] < 7):
			q = q + 1
	print(q)
	vet= array(eval(input("digite os valores: ")))
	