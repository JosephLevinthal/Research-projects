from numpy import*
vet = array(eval(input("Digite alunos: ")))
g=0
for i in range(size(vet)):
	if(vet[i]%5==0):
		g=g+1
print(g)
v= zeros(g, dtype=int)
h=0
for i in range(size(vet)):
	if(vet[i]%5==0):
		v[h]= i
		h = h+1
print(v)
	
	
		