from numpy import*
mt = array(eval(input("num de gols feitos: ")))
ta =  array(eval(input("num de gols levados: ")))

vet = zeros(3, dtype=int)

for i in range(size(mt)):
	if mt[i]>ta[i]: #vitoria
		vet[0]= vet[0] + 1
	elif mt[i]==ta[i]:#empate
		vet[1] = vet[1] + 1
	elif mt[i]<ta[i]: #derrota
		vet[2] = vet[2] + 1
		
print(vet)