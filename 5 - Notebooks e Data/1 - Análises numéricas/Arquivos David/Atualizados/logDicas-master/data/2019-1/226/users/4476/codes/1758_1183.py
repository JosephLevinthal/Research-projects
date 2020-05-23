from numpy import*
v = array(eval(input("digite os valores: ")))

i = 0
n = 0

while (i < size(v)):
	if (v[i] <= 0):
		n = n + 1
	i = i + 1

tam_final = size(v) - n
vet_final = zeros(tam_final, dtype=int)

i = 0
j = 0

while (i < size(v)):
	if (v[i] >= 0):
		vet_final[j] = v[i]
		j = j + 1
	i = i + 1

print(vet_final)