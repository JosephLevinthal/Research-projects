from numpy import*

v= array(eval(input("Insira o seu vetor: ")))
a1=0
cont=0
for i in range(size(v)):
	if(v[i]>=5):
		a1+=1
cont= zeros(a1, dtype=int)

j= 0
for i in range(size(v)):
	if(v[i]>=5):
		cont[j]= i
		j= j + 1
		
	

print(a1)
print(cont)