n = int(input(""))

soma=1
i=0
fim = n-1
 

while (i<=fim):
	soma = soma + (-1)**i/(2+i)*(2*i+1)
	i = i + 1
	
	
print(round(soma,8))