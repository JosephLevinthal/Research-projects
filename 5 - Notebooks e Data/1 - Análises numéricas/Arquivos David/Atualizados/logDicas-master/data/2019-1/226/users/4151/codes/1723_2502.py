
k=int(input("digite um numero: "))
		
soma=0
i=0
while(i<k):
	soma=soma+(12**(1/2))*((1/((2*i+1)*(3**i))))*((-1)**i)
	i=i+1
	
print(round(soma,8))