n=int(input())
i=0
j=0
while(i<=n):
	i=i+1
	if(n%i==0):
		print(i)
		j=j+1
if(j==1):
	print("1 divisor")
else:
	print(j ,"divisores")
