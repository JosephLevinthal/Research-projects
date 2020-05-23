from numpy import*
a= array(eval(input("insira os vetores de A: ")))
b= array(eval(input("insira os vetores de B: ")))
q=size(b)
c=zeros(q,dtype=int)
i=0
j=-1
k=0
while k!=q:
	c[i]=b[j]
	i=i+1
	j=j-1
	k=k+1
	if a[i-1]>c[i-1]:
		print(a[i-1])
	if a[i-1]<c[i-1]:
		print(c[i-1])
