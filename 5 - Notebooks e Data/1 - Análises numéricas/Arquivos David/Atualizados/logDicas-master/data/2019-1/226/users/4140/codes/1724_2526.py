n=int(input())
m=int(input())
i=0
j=0
k=0
l=0
while(i<n):
	i=i+1
	if(n%i==0 and n!=i):
		j=j+i
print(j)
while(k<m):
	k=k+1
	if(m%k==0 and m!=k):
		l=l+k
print(l)
if(l==n and m==j):
	print("AMIGOS")
else:
	print("NAO AMIGOS")