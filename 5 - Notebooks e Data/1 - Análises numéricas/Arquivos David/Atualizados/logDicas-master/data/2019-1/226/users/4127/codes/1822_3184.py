from numpy import*
v= array(eval(input("seu vetor: ")))

for i in range(len(size(v)//2)):
	j=size(v)-1-i
	aux=v[i]
	v[i]=v[j]
	v[j]=aux
print(v)