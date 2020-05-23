x=float(input())
n=int(input())
i=1
soma=0
while(i<n):
	calc=(((-1)**i)*(x**((2*i)+1)))/((2*i)+1)
	soma=soma+calc
	i=i+1
k=soma+x
print(round(k,6))
		