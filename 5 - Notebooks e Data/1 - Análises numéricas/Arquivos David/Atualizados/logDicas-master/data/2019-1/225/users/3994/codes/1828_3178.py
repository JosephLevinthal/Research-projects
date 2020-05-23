from numpy import*
vet = array(eval(input("Digite: ")))
v = zeros(size(vet), dtype=int)
g=0
for i in range(size(vet)):
	if(vet[i]==0):
		g=g[i]+1
print(g)
		
	