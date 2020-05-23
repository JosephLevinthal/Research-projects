n=int(input())
i=0
j=0
while(i<=n):
	i=i+1
	if(n%i==0 and n!=i):
		print(i)
		j=j+i
if(j==n):
	print("PERFEITO")
else:
	print("NAO PERFEITO")
		 
	