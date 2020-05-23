from numpy import*
vet = array(eval(input("Vetor:")))

i = 0
p = 0
n = 0


while(i < size(vet)):
	if(vet[i] < 0):
		n = n + 1
	i = i + 1
	
tf = size(vet) - n

vt = zeros(tf, dtype = int)

i = 0
j = 0

while(i < size(vet)):
	if(vet[i]>=0):
		vt[j] = vet[i]
		j = j + 1
	i = i + 1
	
print(vt)
	
