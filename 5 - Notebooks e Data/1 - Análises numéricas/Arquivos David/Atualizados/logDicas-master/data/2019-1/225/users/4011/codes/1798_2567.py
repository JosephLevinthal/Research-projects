num = int(input())
arte=[]
i=num
while(i>0):
	j=i
	while(j>0):
		print('*', end='')
		if(j==1): print("")
		j-=1
	i-=1

i=1
while(i<=num):
	j=1
	while(j<=i):
		print('*', end='')
		if(j==i): print("")
		j+=1
	i+=1

	