from numpy import*

vet = array(eval(input("vetor de alunos: ")))
a = 0

for i in range(size(vet)):
	if vet[i] % 3 == 0:
		a = a + 1

vect = zeros(a,dtype=int)
c = 0
for j in range(size(vet)):
	if vet[j] % 3 == 0:
		
		vect[c] == 
		c = c + 1

print(a)
print(vect)