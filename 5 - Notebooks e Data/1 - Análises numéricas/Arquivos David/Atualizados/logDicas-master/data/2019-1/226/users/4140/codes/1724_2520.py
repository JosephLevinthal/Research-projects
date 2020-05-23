n=int(input())
i=1
soma=0
while(i<=n):
	
	calc=(1/((i)**2))
	soma=soma+calc
	i=i+1
total=(soma*6)**0.5
print(round(total,6))