from numpy import*

vetor=array(eval(input("x: ")))

i=0
c=0
j=0
while(i<size(vetor)):
	if vetor[i]>=0:
		c=c+1
	i=i+1
v1=zeros(c, dtype=int)

i=0
while(i<size(vetor)):
	if vetor[i]>=0:
		v1[j]=vetor[i]
		j=j+1
	i=i+1
print(v1)