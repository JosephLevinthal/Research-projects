n=int(input("digite um numero: "))
soma=0
i=0
while(i<n):
	soma=soma+((4)/(2*i+1))*(-1)**i
	i=i+1
	
print(round(soma,8))