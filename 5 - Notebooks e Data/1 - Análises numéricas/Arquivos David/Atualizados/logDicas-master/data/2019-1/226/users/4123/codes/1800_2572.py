from numpy import*
vet = array(eval(input()))
n = 0
g2 = ""
for x in vet:
	if x%2!=0:
		n += 1
nvet = zeros(n, dtype = int)
j = 0
for x in vet:
	if x%2!=0:
		nvet[j] = x
		j+=1
print(nvet)