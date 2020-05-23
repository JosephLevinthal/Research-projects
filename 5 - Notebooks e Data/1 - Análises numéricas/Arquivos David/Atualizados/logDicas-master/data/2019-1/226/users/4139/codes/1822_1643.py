from numpy import*
vet = array(eval(input("notas: ")))

i = 0
for x in range(size(vet)):
	if(vet[x]>=5):
		i += 1
print(i)
ap = zeros(i,dtype=int)
i = 0
a = 0
for y in range(size(vet)):
	if(vet[y]>=5):
		ap[i]= a
		i += 1
	a += 1
print(ap)