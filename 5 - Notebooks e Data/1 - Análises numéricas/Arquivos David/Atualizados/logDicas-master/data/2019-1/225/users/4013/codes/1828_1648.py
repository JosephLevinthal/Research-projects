from numpy import*
vet = array(eval(input("aulas frequentadas:")))
rp = 0
for i in range(size(vet)):
	if(vet[i] < 70):
		rp = rp + 1
print(rp)
v = zeros(rp , dtype=int)
j = 0
for i in range(size(vet)):
	if(vet[i] < 70):
		v[j] = i
		j = j + 1
	
print(v)