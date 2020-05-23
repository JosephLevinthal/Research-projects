from numpy import*
v= array(eval(input("vetor de presenca: ")))
n=0
k=0
for i in range(size(v)):
	if(v[i]>=70):
		n=n+1
m=zeros(n,dtype=int)
for j in range(size(v)):
	if(v[j]>=70):
		m[k]= j
		k=k+1
print(n)
print(m)