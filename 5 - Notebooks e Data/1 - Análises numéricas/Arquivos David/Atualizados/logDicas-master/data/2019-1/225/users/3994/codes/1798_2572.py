from numpy import*
vet = array(eval(input("Digite matricula: ")))
g = 0 
for i in range(size(vet)):
	if(vet[i]%2 !=0):
		g = g+1
v= zeros(g, dtype=int)
h=0
for i in range(size(vet)):
	if(vet[i]%2 !=0):
		v[h]= vet[i]
		h = h + 1
print(v)
	
		
